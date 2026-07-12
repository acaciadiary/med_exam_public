import json

source_path = 'public/data/exams/109-1/medicine-1.json'
with open(source_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = [q for q in data['questions'] if 31 <= q['question_number'] <= 40]

output_path = 'scratch/q31_q40_raw.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(questions)} questions to {output_path}")
