import json

source_file = r"public/data/exams/109-1/medicine-4.json"
output_file = r"scratch/q51-q60_raw.json"

with open(source_file, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = [q for q in data.get("questions", []) if 51 <= q.get("question_number", 0) <= 60]

# Write to json with utf-8 and pretty print
with open(output_file, "w", encoding="utf-8") as out:
    json.dump(questions, out, ensure_ascii=False, indent=2)

print("Finished writing to scratch/q51-q60_raw.json")
