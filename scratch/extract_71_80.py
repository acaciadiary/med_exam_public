import json

with open('d:/Antigravity/med_exam_public/public/data/exams/109-1/medicine-1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data['questions'][70:80]
with open('d:/Antigravity/med_exam_public/scratch/questions_71_80.txt', 'w', encoding='utf-8') as out:
    for q in questions:
        out.write(f"Number: {q['question_number']}\n")
        out.write(f"ID: {q['id']}\n")
        out.write(f"Text: {q['question_text']}\n")
        out.write(f"Options: {json.dumps(q['options'], ensure_ascii=False)}\n")
        out.write(f"Answer: {q['correct_answer']}\n")
        out.write(f"Expl: {q['explanation']}\n")
        out.write("-" * 50 + "\n")
