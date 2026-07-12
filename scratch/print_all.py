import json

source_path = 'd:/Antigravity/med_exam_public/public/data/exams/109-1/medicine-1.json'
dest_path = 'd:/Antigravity/med_exam_public/scratch/q41_q50_raw.txt'

with open(source_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data.get('questions', [])
target_qs = [q for q in questions if 41 <= q.get('question_number', 0) <= 50]

with open(dest_path, 'w', encoding='utf-8') as out:
    for q in target_qs:
        qnum = q.get('question_number')
        qid = q.get('id')
        qtext = q.get('question_text')
        answer = q.get('correct_answer')
        options = q.get('options', {})
        explanation = q.get('explanation', '')
        
        out.write(f"=== Q{qnum} (ID: {qid}) ===\n")
        out.write(f"Question: {qtext}\n")
        out.write(f"Answer: {answer}\n")
        out.write("Options:\n")
        for key, val in options.items():
            out.write(f"  - {key}: {val}\n")
        out.write("Existing Explanation:\n")
        out.write(explanation)
        out.write("\n" + "-" * 50 + "\n\n")

print(f"Written raw questions to {dest_path}")
