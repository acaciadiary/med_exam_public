import os
import json
import re

update_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\108-1_medicine-6"

search_keywords = ["複核", "人工", "疑義", "錯誤", "勘誤", "官方答案", "有誤", "修正", "不一致"]

results = []

for filename in sorted(os.listdir(update_dir)):
    if not filename.endswith('.json'):
        continue
    filepath = os.path.join(update_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for update in data.get("updates", []):
        q_num = update.get("question_number")
        explanation = update.get("explanation", "")
        
        found = []
        for kw in search_keywords:
            if kw in explanation:
                # Find matching sentence
                sentences = re.split(r'[。，\n]', explanation)
                matching_s = [s for s in sentences if kw in s]
                found.append(f"'{kw}' in: {matching_s}")
                
        if found:
            results.append((q_num, filename, found))

print(f"=== Found {len(results)} questions mentioning review keywords ===")
for q_num, filename, found in results:
    print(f"Q{q_num} ({filename}):")
    for f in found:
        print(f"  - {f}")
