import json
from pathlib import Path
from datetime import datetime, timezone

def main():
    exam_path = Path("public/data/exams/109-2/medicine-4.json")
    updates_dir = Path("scratch/rewrite_updates/109-2_medicine-4")
    
    if not exam_path.exists():
        print(f"Error: {exam_path} not found.")
        return
        
    if not updates_dir.exists():
        print(f"Error: {updates_dir} not found.")
        return
        
    with open(exam_path, "r", encoding="utf-8") as f:
        exam_data = json.load(f)
        
    questions = exam_data.get("questions", [])
    q_map = {q["id"]: q for q in questions}
    
    updated_count = 0
    now = datetime.now(timezone.utc).isoformat()
    
    # Scan all json files in updates_dir
    for file_path in sorted(updates_dir.glob("*.json")):
        print(f"Reading update file: {file_path.name}")
        with open(file_path, "r", encoding="utf-8") as f:
            up_data = json.load(f)
            
        updates = up_data.get("updates", [])
        for item in updates:
            qid = item.get("question_id")
            if not qid:
                print(f"  Warning: missing question_id in an item in {file_path.name}")
                continue
                
            if qid not in q_map:
                print(f"  Warning: question_id {qid} not found in medicine-4.json. Skipping.")
                continue
                
            orig_q = q_map[qid]
            
            # Save updates
            orig_q["explanation"] = item["explanation"].strip()
            orig_q["key_point"] = item.get("key_point", "").strip()
            orig_q["flashcard_summary"] = item.get("flashcard_summary", "").strip()
            orig_q["flashcard_front"] = item.get("flashcard_front", "").strip()
            orig_q["flashcard_back"] = item.get("flashcard_back", "").strip()
            orig_q["review_status"] = "ai_generated"
            orig_q["explanation_model"] = "codex-high-quality-rewrite"
            orig_q["explanation_generated_at"] = now
            
            if item.get("manual_review_notes"):
                orig_q["manual_review_notes"] = item.get("manual_review_notes")
                
            updated_count += 1
            
    # Write back
    exam_data["updated_at"] = now
    with open(exam_path, "w", encoding="utf-8") as f:
        json.dump(exam_data, f, ensure_ascii=False, indent=2)
        
    print(f"\nMerge completed! Updated {updated_count} out of {len(questions)} questions.")

if __name__ == "__main__":
    main()
