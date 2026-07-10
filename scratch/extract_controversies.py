import os
import json

updates_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\114-2_medicine-5"

def extract():
    files = sorted([f for f in os.listdir(updates_dir) if f.endswith(".json")])
    flagged_questions = [15, 18, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    
    results = {}
    
    for file_name in files:
        file_path = os.path.join(updates_dir, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for u in data.get("updates", []):
            num = u.get("question_number")
            if num in flagged_questions:
                notes = u.get("manual_review_notes", [])
                expl = u.get("explanation", "")
                
                # Extract paragraph containing keywords
                keywords = ["官方答案", "爭議", "疑義", "人工複核", "補充提醒", "送分", "給分"]
                found_sentences = []
                for line in expl.split("\n"):
                    if any(kw in line for kw in keywords):
                        found_sentences.append(line.strip())
                
                results[num] = {
                    "manual_review_notes": notes,
                    "highlighted_explanation_lines": found_sentences
                }
                
    out_path = r"d:\Antigravity\med_exam_public\scratch\controversy_details.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("Done")

if __name__ == "__main__":
    extract()
