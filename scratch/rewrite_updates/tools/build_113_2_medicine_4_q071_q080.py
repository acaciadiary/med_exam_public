import json
from pathlib import Path


source = Path("public/data/exams/113-2/medicine-4.json")
data = json.loads(source.read_text(encoding="utf-8"))
out = Path("scratch/rewrite_updates/113-2_medicine-4/q071-q080.json")
out.parent.mkdir(parents=True, exist_ok=True)

manual = {
    76: [
        "來源資料欄位疑似混入第 77 題：question_text 內含壞死性筋膜炎題目與第 77 題題幹，options 欄位則為 35/45/55/65；未修改題目、選項或答案，詳解依 question_text 中可見的壞死性筋膜炎 A-D 敘述解析。"
    ]
}

replacements = {
    74: [("GBM 飾別", "GBM 鑑別")],
}

updates = []
for q in data["questions"][70:80]:
    n = q["question_number"]
    expl = q["explanation"]
    for old, new in replacements.get(n, []):
        expl = expl.replace(old, new)
    updates.append(
        {
            "question_id": q["id"],
            "question_number": n,
            "explanation": expl,
            "key_point": q.get("key_point", ""),
            "flashcard_front": q.get("flashcard_front", ""),
            "flashcard_back": q.get("flashcard_back", ""),
            "flashcard_summary": q.get("flashcard_summary", ""),
            "review_status": "ai_generated",
            "explanation_model": "codex-high-quality-rewrite",
            "explanation_generated_at": "2026-07-09T14:00:00+08:00",
            "manual_review_notes": manual.get(n, []),
        }
    )

payload = {
    "source_file": "public/data/exams/113-2/medicine-4.json",
    "dataset_id": "113-2_medicine-4",
    "range": {"start": 71, "end": 80},
    "updates": updates,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
