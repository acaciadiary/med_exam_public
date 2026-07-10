import os
import json
import re

update_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\108-1_medicine-6"

def get_similarity(s1, s2):
    s1 = re.sub(r'[^\w]', '', s1)
    s2 = re.sub(r'[^\w]', '', s2)
    if not s1 or not s2:
        return 0
    words1 = set(s1)
    words2 = set(s2)
    return len(words1 & words2) / len(words1 | words2)

results = []

for filename in sorted(os.listdir(update_dir)):
    if not filename.endswith('.json'):
        continue
    filepath = os.path.join(update_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for update in data.get("updates", []):
        q_num = update.get("question_number")
        q_id = update.get("question_id")
        explanation = update.get("explanation", "")
        manual_notes = update.get("manual_review_notes", [])
        
        # Extract option texts
        options_sec = ""
        if "【選項詳解】" in explanation:
            parts = explanation.split("【選項詳解】")
            if len(parts) > 1:
                options_sec = parts[1].split("【核心考點】")[0]
        
        opts = {}
        for opt in ['A', 'B', 'C', 'D']:
            opt_match = re.search(rf"-\s*{opt}\.\s*(.*?)(?=(-\s*[A-D]\.|\Z))", options_sec, re.DOTALL)
            if opt_match:
                opts[opt] = opt_match.group(1).strip()
            else:
                opts[opt] = ""

        # Compare similarities
        sims = []
        for o1 in ['A', 'B', 'C', 'D']:
            for o2 in ['A', 'B', 'C', 'D']:
                if o1 < o2 and opts[o1] and opts[o2]:
                    sim = get_similarity(opts[o1], opts[o2])
                    if sim > 0.8:
                        sims.append((o1, o2, sim))

        results.append({
            "q_num": q_num,
            "file": filename,
            "manual_notes": manual_notes,
            "similar_options": sims,
            "options": opts
        })

print("=== Manual Review Notes Found ===")
for r in results:
    if r["manual_notes"]:
        print(f"Q{r['q_num']} ({r['file']}): {r['manual_notes']}")

print("\n=== Similar Options Found (Similarity > 0.8) ===")
for r in results:
    if r["similar_options"]:
        print(f"Q{r['q_num']} ({r['file']}):")
        for sim in r["similar_options"]:
            print(f"  - {sim[0]} and {sim[1]} are very similar (sim={sim[2]:.2f})")
            print(f"    {sim[0]}: {r['options'][sim[0]]}")
            print(f"    {sim[1]}: {r['options'][sim[1]]}")
