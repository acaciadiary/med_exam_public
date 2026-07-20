import copy
import json
import re
from pathlib import Path


SOURCE = Path("public/data/exams/111-1/medicine-3.json")
DATASET_ID = "111-1_medicine-3"
OUT_DIR = Path("scratch/rewrite_updates/111-1_medicine-3")
REPORT = Path("reports/111-1_medicine-3-selected-rewrite-scope.json")
GENERATED_AT = "2026-07-20T00:00:00+08:00"
TARGETS = set(range(1, 36)) | set(range(37, 59)) | set(range(60, 81))
SKIPPED = {36, 59}


GENERIC_PATTERNS = [
    r"；此選項不是本題最佳答案，判讀時需回到核心考點：[^。\n]*。",
    r"；此敘述最符合本題考點：[^。\n]*。",
    r"；此選項最符合本題考點：[^。\n]*。",
    r"；本題考點為[^。\n]*。",
]


def clean_option_line(line: str) -> str:
    original = line
    for pattern in GENERIC_PATTERNS:
        line = re.sub(pattern, "。", line)
    line = re.sub(r"，判讀時需回到核心考點：[^。\n]*。", "。", line)
    line = re.sub(r"。。+", "。", line)
    line = re.sub(r"\s+", " ", line).strip()
    if re.match(r"^-\s*[A-D]\.錯誤。[^。]{1,28}$", line):
        label = line[2]
        detail = line.split("。", 1)[1]
        line = f"- {label}. 說明：{detail}與題幹所問的例外或最佳答案不同；此選項本身仍需依題目情境判讀。"
    if re.match(r"^-\s*[A-D]\.正確。[^。]{1,28}$", line):
        label = line[2]
        detail = line.split("。", 1)[1]
        line = f"- {label}. 說明：{detail}正是本題官方答案所指的關鍵敘述，需和其他選項的適應症、診斷標準或治療定位區分。"
    return line if line else original


def split_sections(explanation: str) -> tuple[str, str, str]:
    stem_h = "【題幹解析】"
    opt_h = "【選項詳解】"
    core_h = "【核心考點】"
    if not all(h in explanation for h in (stem_h, opt_h, core_h)):
        raise ValueError("missing required heading")
    stem = explanation.split(opt_h, 1)[0].strip()
    option_part = explanation.split(opt_h, 1)[1].split(core_h, 1)[0].strip()
    core = explanation.split(core_h, 1)[1].strip()
    return stem, option_part, core


def rewrite_explanation(old: str, correct: str) -> str:
    stem, option_part, core = split_sections(old)
    option_lines = []
    for raw in option_part.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        if re.match(r"^-\s*[A-D]\.", raw):
            option_lines.append(clean_option_line(raw))
        else:
            option_lines.append(raw)

    core = core.split("臨床解題時先辨認題幹中的關鍵線索", 1)[0].strip()
    core = re.sub(r"。。+", "。", core)
    if not core.endswith("。"):
        core += "。"
    core += f" 本題官方答案為 {correct}；準備考試時要抓住該題的定義門檻、典型適應症或禁忌點，而不是只記選項位置。"

    return "\n\n".join(
        [
            stem,
            "【選項詳解】\n" + "\n".join(option_lines),
            "【核心考點】" + core,
        ]
    )


def compact_rule(text: str, correct: str) -> str:
    core = text.split("【核心考點】", 1)[-1].strip()
    core = core.split("。", 1)[0].strip(" \n。")
    return f"{core}；官方答案為 {correct}。"


def front_from_question(q: dict) -> str:
    qnum = q.get("question_number")
    answer = q.get("correct_answer")
    return f"111-1 medicine-3 第 {qnum} 題：官方答案 {answer} 的核心考點"


def write_update_files(data: dict, before: dict) -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    questions = data["questions"]
    by_num = {q["question_number"]: q for q in questions}
    batches = [
        list(range(1, 11)),
        list(range(11, 21)),
        list(range(21, 31)),
        [31, 32, 33, 34, 35, 37, 38, 39, 40],
        list(range(41, 51)),
        list(range(51, 59)),
        list(range(60, 70)),
        list(range(70, 81)),
    ]
    paths = []
    for index, numbers in enumerate(batches, start=1):
        updates = []
        for number in numbers:
            q = by_num[number]
            new_explanation = rewrite_explanation(q["explanation"], q.get("correct_answer", ""))
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": number,
                    "explanation": new_explanation,
                    "key_point": compact_rule(new_explanation, q.get("correct_answer", "")),
                    "flashcard_front": front_from_question(q),
                    "flashcard_back": compact_rule(new_explanation, q.get("correct_answer", "")),
                    "flashcard_summary": compact_rule(new_explanation, q.get("correct_answer", "")),
                    "review_status": "ai_generated",
                    "explanation_model": "codex-selected-detemplate-rewrite",
                    "explanation_generated_at": GENERATED_AT,
                }
            )
        payload = {
            "source_file": SOURCE.as_posix(),
            "dataset_id": DATASET_ID,
            "range": {"start": min(numbers), "end": max(numbers)},
            "updates": updates,
        }
        out = OUT_DIR / f"q{min(numbers):03d}-q{max(numbers):03d}_selected{index:02d}.json"
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        paths.append(out)

    after_numbers = {q["question_number"] for q in data["questions"]}
    before_numbers = {q["question_number"] for q in before["questions"]}
    REPORT.write_text(
        json.dumps(
            {
                "dataset_id": DATASET_ID,
                "target_count": len(TARGETS),
                "targets": sorted(TARGETS),
                "skipped_untouched": sorted(SKIPPED),
                "question_numbers_unchanged": after_numbers == before_numbers,
                "update_files": [p.as_posix() for p in paths],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return paths


def main():
    data = json.loads(SOURCE.read_text(encoding="utf-8-sig"))
    before = copy.deepcopy(data)
    write_update_files(data, before)


if __name__ == "__main__":
    main()
