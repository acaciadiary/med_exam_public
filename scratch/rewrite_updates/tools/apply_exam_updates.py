import argparse
import copy
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


ALLOWED_UPDATE_KEYS = {
    "question_id",
    "question_number",
    "explanation",
    "key_point",
    "flashcard_front",
    "flashcard_back",
    "flashcard_summary",
    "review_status",
    "explanation_model",
    "explanation_generated_at",
    "manual_review_notes",
}

MERGE_FIELDS = {
    "explanation",
    "key_point",
    "flashcard_front",
    "flashcard_back",
    "flashcard_summary",
    "review_status",
    "explanation_model",
    "explanation_generated_at",
}

IMMUTABLE_FIELDS = {
    "id",
    "question_number",
    "question_text",
    "options",
    "correct_answer",
    "correct_answers",
    "answer_status",
    "answer_source",
    "official_correction",
    "official_corrections",
    "answer_note",
}

BANNED_PHRASES = [
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "作答時應回到題幹線索",
    "本題核心在於依題幹線索判斷",
    "標準答案為",
    "原始解析重點指出",
    "既有解析重點",
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def fail(errors, message):
    errors.append(message)


def get_questions(exam):
    questions = exam.get("questions")
    if not isinstance(questions, list):
        raise ValueError("source exam has no questions list")
    return questions


def validate_update_file(update_path, source_file, dataset_id, questions_by_number, questions_by_id, allow_partial_range=False):
    errors = []
    manual_review = []
    data = load_json(update_path)

    if data.get("source_file") != source_file:
        fail(errors, f"{update_path}: source_file mismatch")
    if data.get("dataset_id") != dataset_id:
        fail(errors, f"{update_path}: dataset_id mismatch")

    range_obj = data.get("range") or {}
    start = range_obj.get("start")
    end = range_obj.get("end")
    updates = data.get("updates")
    if not isinstance(start, int) or not isinstance(end, int) or start > end:
        fail(errors, f"{update_path}: invalid range")
    if not isinstance(updates, list):
        fail(errors, f"{update_path}: updates must be a list")
        return errors, manual_review, []

    expected_numbers = list(range(start, end + 1))
    seen_numbers = []
    valid_updates = []
    for item in updates:
        keys = set(item)
        extra = keys - ALLOWED_UPDATE_KEYS
        if extra:
            fail(errors, f"{update_path}: Q{item.get('question_number')} extra keys {sorted(extra)}")

        qnum = item.get("question_number")
        qid = item.get("question_id")
        seen_numbers.append(qnum)
        source_q = questions_by_number.get(qnum)
        if source_q is None:
            fail(errors, f"{update_path}: Q{qnum} not found in source")
            continue
        if qid != source_q.get("id"):
            fail(errors, f"{update_path}: Q{qnum} question_id mismatch")
        if questions_by_id.get(qid) is not source_q:
            fail(errors, f"{update_path}: Q{qnum} question_id does not map to source question")
        if not (start <= qnum <= end):
            fail(errors, f"{update_path}: Q{qnum} outside declared range")

        explanation = item.get("explanation") or ""
        for heading in ("【題幹解析】", "【選項詳解】", "【核心考點】"):
            if heading not in explanation:
                fail(errors, f"{update_path}: Q{qnum} missing heading {heading}")
        for option in ("A", "B", "C", "D"):
            if not re.search(rf"(?:^|\n)\s*[-*]?\s*{option}[.．、]", explanation):
                fail(errors, f"{update_path}: Q{qnum} missing option {option} explanation")
        for phrase in BANNED_PHRASES:
            if phrase in explanation or phrase in str(item.get("key_point") or "") or phrase in str(item.get("flashcard_summary") or ""):
                fail(errors, f"{update_path}: Q{qnum} banned phrase {phrase}")

        notes = item.get("manual_review_notes", [])
        if notes:
            manual_review.append({"question_number": qnum, "notes": notes})
        valid_updates.append(item)

    if allow_partial_range:
        missing_from_range = [qnum for qnum in seen_numbers if qnum not in expected_numbers]
        if missing_from_range:
            fail(errors, f"{update_path}: question_numbers outside range {missing_from_range}")
    elif seen_numbers != expected_numbers:
        fail(errors, f"{update_path}: expected question_numbers {expected_numbers}, got {seen_numbers}")

    return errors, manual_review, valid_updates


def write_json(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-file", required=True)
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--updates", nargs="+", required=True)
    parser.add_argument("--merge", action="store_true")
    parser.add_argument("--allow-partial-range", action="store_true")
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    exam = load_json(args.source_file)
    before = copy.deepcopy(exam)
    questions = get_questions(exam)
    questions_by_number = {q.get("question_number"): q for q in questions}
    questions_by_id = {q.get("id"): q for q in questions}

    all_errors = []
    manual_review = []
    all_updates = []
    for update_path in args.updates:
        errors, notes, valid_updates = validate_update_file(
            update_path,
            args.source_file.replace("\\", "/"),
            args.dataset_id,
            questions_by_number,
            questions_by_id,
            args.allow_partial_range,
        )
        all_errors.extend(errors)
        manual_review.extend(notes)
        all_updates.extend(valid_updates)

    if all_errors:
        report = {
            "source_file": args.source_file,
            "dataset_id": args.dataset_id,
            "merge": False,
            "errors": all_errors,
            "manual_review": manual_review,
        }
        write_json(args.report, report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        sys.exit(1)

    merged_numbers = []
    if args.merge:
        for item in all_updates:
            q = questions_by_number[item["question_number"]]
            for field in MERGE_FIELDS:
                if field in item:
                    q[field] = item[field]
            merged_numbers.append(item["question_number"])

        for before_q, after_q in zip(get_questions(before), questions):
            for field in IMMUTABLE_FIELDS:
                if before_q.get(field) != after_q.get(field):
                    all_errors.append(f"immutable field changed: Q{after_q.get('question_number')} {field}")
            if set(before_q) != set(after_q):
                removed = set(before_q) - set(after_q)
                added = set(after_q) - set(before_q)
                if removed or added:
                    all_errors.append(
                        f"question keys changed: Q{after_q.get('question_number')} removed={sorted(removed)} added={sorted(added)}"
                    )

        if all_errors:
            report = {
                "source_file": args.source_file,
                "dataset_id": args.dataset_id,
                "merge": False,
                "errors": all_errors,
                "manual_review": manual_review,
            }
            write_json(args.report, report)
            print(json.dumps(report, ensure_ascii=False, indent=2))
            sys.exit(1)

        write_json(args.source_file, exam)

    report = {
        "source_file": args.source_file,
        "dataset_id": args.dataset_id,
        "merge": bool(args.merge),
        "update_file_count": len(args.updates),
        "question_count": len(all_updates),
        "merged_question_numbers": merged_numbers,
        "manual_review": manual_review,
        "errors": [],
    }
    write_json(args.report, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
