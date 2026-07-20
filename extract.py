import json
import sys

def main():
    try:
        with open('public/data/exams/108-2/medicine-4.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        targets = [1, 7, 8, 9, 11, 12, 13, 15, 16, 17]
        for q in data['questions']:
            if q['question_number'] in targets:
                print(f"Q{q['question_number']}: {q['question_text']}")
                for k, v in q['options'].items():
                    print(f"  {k}: {v}")
                print(f"  Answer: {q['correct_answer']}\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
