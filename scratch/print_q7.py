import json
with open("public/data/exams/110-2/medicine-2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data.get("questions", []):
    if q.get("question_number") == 7:
        print(q.get("explanation"))
