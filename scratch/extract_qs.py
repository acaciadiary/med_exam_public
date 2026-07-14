import json
import os

source_path = "public/data/exams/114-2/medicine-3.json"
output_path = "scratch/temp_qs.json"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(source_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# The data could be a list or a dict with "questions" key
questions = data.get("questions", data) if isinstance(data, dict) else data

# Filter questions 51 to 60
target_qs = [q for q in questions if 51 <= q.get("question_number", 0) <= 60]

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(target_qs, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(target_qs)} questions to {output_path}")
