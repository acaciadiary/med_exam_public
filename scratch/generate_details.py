import json

path = 'd:/Antigravity/med_exam_public/public/data/exams/109-1/medicine-5.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data.get('questions', [])

target_questions = []
for q in questions:
    num = q.get('question_number')
    if 61 <= num <= 70:
        target_questions.append(q)

out_path = 'd:/Antigravity/med_exam_public/scratch/q61_70_details.md'
with open(out_path, 'w', encoding='utf-8') as out:
    out.write("# 109-1 Medicine-5 Q61-Q70 原始資料\n\n")
    for q in target_questions:
        out.write(f"## 題號 {q.get('question_number')} (ID: {q.get('question_id')})\n")
        out.write(f"**題目**：\n{q.get('question_text')}\n\n")
        out.write("**選項**：\n")
        opts = q.get('options', {})
        if isinstance(opts, dict):
            for key, val in opts.items():
                out.write(f"- **{key}**: {val}\n")
        else:
            out.write(f"{opts}\n")
        out.write(f"\n**正確答案**: {q.get('correct_answer')} / {q.get('correct_answers')}\n\n")
        out.write(f"**目前解析**:\n```text\n{q.get('explanation')}\n```\n\n")
        out.write(f"**Key Point**: {q.get('key_point')}\n\n")
        out.write(f"**Flashcard Front**: {q.get('flashcard_front')}\n\n")
        out.write(f"**Flashcard Back**: {q.get('flashcard_back')}\n\n")
        out.write(f"**Flashcard Summary**: {q.get('flashcard_summary')}\n\n")
        out.write("---\n\n")

print("Done! Details written to scratch/q61_70_details.md")
