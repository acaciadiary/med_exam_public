import json
import sys
from pathlib import Path


def recover_text(value):
    if not isinstance(value, str):
        return value
    try:
        return value.encode("cp950").decode("utf-8")
    except UnicodeError:
        return value


def recover(value):
    if isinstance(value, dict):
        return {key: recover(val) for key, val in value.items()}
    if isinstance(value, list):
        return [recover(item) for item in value]
    return recover_text(value)


def main():
    source = Path(sys.argv[1])
    out = Path(sys.argv[2])
    data = json.loads(source.read_text(encoding="utf-8"))
    readable = recover(data)
    slim = {
        "id": readable.get("id"),
        "year": readable.get("year"),
        "subject": readable.get("subject"),
        "questions": [],
    }
    for q in readable.get("questions", []):
        slim["questions"].append(
            {
                "id": q.get("id"),
                "question_number": q.get("question_number"),
                "question_text": q.get("question_text"),
                "options": q.get("options"),
                "correct_answer": q.get("correct_answer"),
                "correct_answers": q.get("correct_answers"),
                "answer_status": q.get("answer_status"),
            }
        )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(slim, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
