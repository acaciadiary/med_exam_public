import json

source_file = r"d:\Antigravity\med_exam_public\public\data\exams\108-1\medicine-6.json"
update_file = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\108-1_medicine-6\q021-q030.json"

with open(source_file, 'r', encoding='utf-8') as f:
    source = json.load(f)

with open(update_file, 'r', encoding='utf-8') as f:
    update = json.load(f)

q26_source = [q for q in source['questions'] if q['question_number'] == 26][0]
q26_update = [q for q in update['updates'] if q['question_number'] == 26][0]

output = []
output.append("=== SOURCE Q26 ===")
output.append(json.dumps(q26_source, ensure_ascii=False, indent=2))
output.append("\n=== UPDATE Q26 ===")
output.append(json.dumps(q26_update, ensure_ascii=False, indent=2))

with open(r"d:\Antigravity\med_exam_public\scratch\q26_dump.txt", "w", encoding="utf-8") as out_f:
    out_f.write("\n".join(output))

print("Dumped successfully to scratch/q26_dump.txt")
