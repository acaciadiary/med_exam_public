import json
import subprocess
import sys
from pathlib import Path


IMMUTABLE_FIELDS = [
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
]


def load_head(path):
    result = subprocess.run(
        ["git", "show", f"HEAD:{path.as_posix()}"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


def main():
    path = Path(sys.argv[1])
    before = load_head(path)
    after = json.loads(path.read_text(encoding="utf-8"))
    errors = []

    before_questions = before.get("questions", [])
    after_questions = after.get("questions", [])
    if len(before_questions) != len(after_questions):
        errors.append(f"question count changed: {len(before_questions)} -> {len(after_questions)}")

    for before_q, after_q in zip(before_questions, after_questions):
        for field in IMMUTABLE_FIELDS:
            if before_q.get(field) != after_q.get(field):
                errors.append(f"Q{after_q.get('question_number')} immutable field changed: {field}")

        removed_keys = set(before_q) - set(after_q)
        added_keys = set(after_q) - set(before_q)
        allowed_added = {
            "explanation",
            "key_point",
            "flashcard_front",
            "flashcard_back",
            "flashcard_summary",
            "review_status",
            "explanation_model",
            "explanation_generated_at",
        }
        if removed_keys:
            errors.append(f"Q{after_q.get('question_number')} keys removed: {sorted(removed_keys)}")
        unexpected_added = added_keys - allowed_added
        if unexpected_added:
            errors.append(f"Q{after_q.get('question_number')} unexpected keys added: {sorted(unexpected_added)}")

    if errors:
        print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    print(json.dumps({"ok": True, "question_count": len(after_questions)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
