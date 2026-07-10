import os
import json
import re

update_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\108-1_medicine-6"

hollow_patterns = [
    r"熟悉.*(機轉|表現|診斷|治療|原則)",
    r"掌握.*(機轉|表現|診斷|治療|原則)",
    r"了解.*(機轉|表現|診斷|治療|原則)",
    r"學習.*(機轉|表現|診斷|治療|原則)",
    r"臨床診斷與治療原則",
    r"診斷與處置原則",
    r"病理機制及鑑別診斷",
    r"基本判斷能力",
    r"基本判斷"
]

results = []

for filename in sorted(os.listdir(update_dir)):
    if not filename.endswith('.json'):
        continue
    filepath = os.path.join(update_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for update in data.get("updates", []):
        q_num = update.get("question_number")
        key_point = update.get("key_point", "")
        flash_sum = update.get("flashcard_summary", "")
        flash_back = update.get("flashcard_back", "")
        
        matches = []
        for pat in hollow_patterns:
            if re.search(pat, key_point):
                matches.append(f"key_point matches '{pat}': {key_point}")
            if re.search(pat, flash_sum):
                matches.append(f"flashcard_summary matches '{pat}': {flash_sum}")
            if re.search(pat, flash_back):
                matches.append(f"flashcard_back matches '{pat}': {flash_back}")
                
        if matches:
            results.append((q_num, filename, matches))

print(f"=== Found {len(results)} questions with potentially hollow learning fields ===")
for q_num, filename, matches in results:
    print(f"Q{q_num} ({filename}):")
    for m in matches:
        print(f"  - {m}")
