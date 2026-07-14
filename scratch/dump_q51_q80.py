import json

def main():
    with open('public/data/exams/114-2/medicine-3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = [q for q in data['questions'] if 51 <= q['question_number'] <= 80]
    
    with open('scratch/q51_q80_source.txt', 'w', encoding='utf-8') as out:
        for q in questions:
            out.write(f"Q{q['question_number']}: {q['question_text'].strip()}\n")
            for k, v in q['options'].items():
                out.write(f"  {k}: {v.strip()}\n")
            out.write(f"Ans: {q.get('correct_answer')} {q.get('correct_answers')}\n")
            out.write("-" * 50 + "\n")

if __name__ == '__main__':
    main()
