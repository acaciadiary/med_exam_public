import json
with open('d:\\Antigravity\\med_exam_public\\scratch\\tasks\\108-2_medicine-2\\batch_6.json', encoding='utf-8') as f:
    data = json.load(f)
qs = []
for q in data['questions']:
    if q['question_number'] in [81, 83, 84, 85, 86, 88, 90, 95]:
        qs.append(q)
with open('d:\\Antigravity\\med_exam_public\\extract_q.json', 'w', encoding='utf-8') as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)
