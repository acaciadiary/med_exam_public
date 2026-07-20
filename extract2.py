import json
with open('d:\\Antigravity\\med_exam_public\\scratch\\tasks\\108-2_medicine-2\\batch_6.json', encoding='utf-8') as f:
    data = json.load(f)
print(type(data))
if isinstance(data, dict):
    print(data.keys())
