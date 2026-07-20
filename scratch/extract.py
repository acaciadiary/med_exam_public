import json

target_qs = ["53", "54", "55", "56", "57", "59", "60", "61", "62", "64"]

with open(r'd:\Antigravity\med_exam_public\public\data\exams\108-2\medicine-3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

extracted = {}
for q in data.get('questions', []):
    q_num = str(q.get('question_number', ''))
    if q_num in target_qs:
        extracted[q_num] = q

with open(r'd:\Antigravity\med_exam_public\scratch\temp_extract_qs.json', 'w', encoding='utf-8') as f:
    json.dump(extracted, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(extracted)} questions.")
