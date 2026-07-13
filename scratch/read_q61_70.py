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

out_path = 'd:/Antigravity/med_exam_public/scratch/q61_70_raw.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    for q in target_questions:
        out.write(f"=== Question {q.get('question_number')} ({q.get('question_id')}) ===\n")
        out.write(f"Text:\n{q.get('question_text')}\n")
        out.write("Options:\n")
        opts = q.get('options', [])
        for idx, opt in enumerate(opts):
            if isinstance(opt, dict):
                out.write(f"  {opt.get('option_id', idx)}: {opt.get('option_text', '')}\n")
            else:
                out.write(f"  {idx}: {opt}\n")
        out.write(f"Correct Answer: {q.get('correct_answer')}\n")
        out.write(f"Current Explanation:\n{q.get('explanation')}\n")
        out.write(f"Key Point: {q.get('key_point')}\n")
        out.write(f"Flashcard Front: {q.get('flashcard_front')}\n")
        out.write(f"Flashcard Back: {q.get('flashcard_back')}\n")
        out.write(f"Flashcard Summary: {q.get('flashcard_summary')}\n")
        out.write("\n" + "="*80 + "\n\n")

print("Done! Output written to scratch/q61_70_raw.txt")
