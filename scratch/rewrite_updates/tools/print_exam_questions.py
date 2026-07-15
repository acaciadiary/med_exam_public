import argparse
import json
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int)
    args = parser.parse_args()

    data = json.loads(Path(args.source).read_text(encoding="utf-8-sig"))
    questions = data["questions"]
    end = args.end if args.end is not None else len(questions)
    for q in questions:
        number = q["question_number"]
        if number < args.start or number > end:
            continue
        answer = q.get("correct_answers") or q.get("correct_answer")
        print(f"Q{number:03d} {q['id']} ans={answer} status={q.get('answer_status')}")
        print(q["question_text"])
        for option in ("A", "B", "C", "D"):
            print(f"  {option}. {q['options'].get(option)}")
        print()


if __name__ == "__main__":
    main()
