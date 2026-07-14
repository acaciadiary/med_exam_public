import json
import sys

with open('public/data/exams/110-1/medicine-6.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

output = []
for q in d['questions']:
    if 51 <= q['question_number'] <= 60:
        output.append(f"=== Q{q['question_number']} (ID: {q['id']}) ===")
        output.append(q['question_text'])
        output.append(str(q['options']))
        output.append(f"Correct: {q['correct_answer']}")
        output.append(f"Explanation:\n{q['explanation']}")
        output.append(f"Key Point: {q.get('key_point', '')}")
        output.append(f"Flashcard Front: {q.get('flashcard_front', '')}")
        output.append(f"Flashcard Back: {q.get('flashcard_back', '')}")
        output.append(f"Flashcard Summary: {q.get('flashcard_summary', '')}")
        output.append('-'*50)

with open('scratch/q51_q60_raw.txt', 'w', encoding='utf-8') as out_f:
    out_f.write('\n'.join(output))
