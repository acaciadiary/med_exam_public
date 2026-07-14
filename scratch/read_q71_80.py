import json

with open('public/data/exams/114-2/medicine-3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = [q for q in data['questions'] if q.get('question_number') in range(71, 81)]

output = {
    "source_file": "public/data/exams/114-2/medicine-3.json",
    "dataset_id": "114-2_medicine-3",
    "questions": questions
}

with open('scratch/q71_80_raw.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Done. Saved to scratch/q71_80_raw.json")
