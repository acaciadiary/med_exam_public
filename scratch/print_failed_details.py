import json
import os

updates_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\109-2_medicine-4"
update_files = [
    "q001-q010.json",
    "q011-q020.json",
    "q021-q030.json",
    "q031-q040.json",
    "q041-q050.json",
    "q051-q060.json",
    "q061-q070.json",
    "q071-q080.json"
]

target_questions = [13, 14, 18, 36, 41, 44, 45, 47, 48, 49, 50, 59, 60, 71, 72, 76, 77]

results = []

for file_name in update_files:
    file_path = os.path.join(updates_dir, file_name)
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for up in data.get("updates", []):
        q_num = up.get("question_number")
        if q_num in target_questions:
            results.append((q_num, up))

results.sort(key=lambda x: x[0])

out_lines = []
for q_num, up in results:
    out_lines.append("="*60)
    out_lines.append(f"QUESTION NUMBER: {q_num}")
    out_lines.append(f"QUESTION ID: {up.get('question_id')}")
    out_lines.append(f"EXPLANATION:")
    out_lines.append(up.get("explanation", ""))
    out_lines.append(f"KEY POINT: {up.get('key_point', '')}")
    out_lines.append(f"FLASHCARD SUMMARY: {up.get('flashcard_summary', '')}")
    out_lines.append(f"FLASHCARD BACK: {up.get('flashcard_back', '')}")
    out_lines.append("\n")

with open(r"d:\Antigravity\med_exam_public\scratch\failed_details.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Done.")
