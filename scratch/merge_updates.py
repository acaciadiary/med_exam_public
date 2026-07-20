import os
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

def clean(value):
    import re
    return re.sub(r"\s+", " ", str(value or "")).strip()

def clean_preserve_newlines(value):
    import re
    text = str(value or "").replace("\r\n", "\n").strip()
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text

def main():
    target_json_path = Path("public/data/exams/110-1/medicine-1.json")
    updates_dir = Path("scratch/rewrite_updates/110-1_medicine-1")
    
    if not target_json_path.exists():
        print(f"Error: Target file {target_json_path} does not exist.")
        sys.exit(1)
        
    if not updates_dir.exists():
        print(f"Error: Updates directory {updates_dir} does not exist. No updates to merge.")
        sys.exit(1)
        
    # Read original exam data
    with open(target_json_path, 'r', encoding='utf-8-sig') as f:
        exam_data = json.load(f)
        
    questions_dict = {q["id"]: q for q in exam_data.get("questions", [])}
    
    success_count = 0
    issues = []
    
    # Read all update JSONs in updates_dir
    update_files = sorted(list(updates_dir.glob("*.json")))
    print(f"Found {len(update_files)} update files in {updates_dir}.")
    
    for uf in update_files:
        print(f"Processing {uf.name}...")
        try:
            with open(uf, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
        except Exception as e:
            issues.append(f"Failed to parse JSON for file {uf.name}: {e}")
            continue
            
        # Verify dataset_id
        if batch_data.get("dataset_id") != "110-1_medicine-1":
            issues.append(f"File {uf.name} has incorrect dataset_id: {batch_data.get('dataset_id')}")
            continue
            
        updates = batch_data.get("updates", [])
        for item in updates:
            qid = item.get("question_id")
            if not qid:
                issues.append(f"File {uf.name} contains update with missing question_id.")
                continue
                
            orig_q = questions_dict.get(qid)
            if not orig_q:
                issues.append(f"Question ID {qid} from {uf.name} not found in target exam.")
                continue
                
            # Perform verification of correct_answer if provided in update
            if "correct_answer" in item:
                if clean(item["correct_answer"]) != clean(orig_q.get("correct_answer")):
                    issues.append(f"QID {qid}: correct_answer mismatch. Original: {orig_q.get('correct_answer')}, Update: {item['correct_answer']}")
            
            # Merge fields
            orig_q["explanation"] = clean_preserve_newlines(item.get("explanation"))
            orig_q["key_point"] = clean(item.get("key_point"))
            
            # Optional learning helper fields
            for field in ["flashcard_front", "flashcard_back", "flashcard_summary", "review_status", "explanation_model", "explanation_generated_at"]:
                if field in item:
                    if field in ["flashcard_front", "flashcard_back", "flashcard_summary"]:
                        orig_q[field] = clean(item[field])
                    else:
                        orig_q[field] = item[field]
                        
            success_count += 1
            
    if issues:
        print("\n=== Issues Found during Merge ===")
        for issue in issues:
            print(f"- {issue}")
        print("=================================\n")
        # Exit with error if any issue
        sys.exit(1)
        
    # Write back to original JSON
    exam_data["updated_at"] = datetime.now(timezone.utc).isoformat()
    with open(target_json_path, 'w', encoding='utf-8-sig') as f:
        json.dump(exam_data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully merged {success_count} question updates into {target_json_path}.")

if __name__ == "__main__":
    main()
