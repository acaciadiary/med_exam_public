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
    if len(sys.argv) < 4:
        print("Usage: python helper_import.py <subject_json_path> <done_batch_path> <progress_json_path>")
        sys.exit(1)
        
    json_path = Path(sys.argv[1])
    done_path = Path(sys.argv[2])
    progress_path = Path(sys.argv[3])
    
    if not json_path.exists():
        print(f"Error: {json_path} does not exist.")
        sys.exit(1)
    if not done_path.exists():
        print(f"Error: {done_path} does not exist.")
        sys.exit(1)
        
    # Read original data
    with open(json_path, 'r', encoding='utf-8') as f:
        original_data = json.load(f)
        
    # Read done batch data
    with open(done_path, 'r', encoding='utf-8') as f:
        done_data = json.load(f)
        
    # Build dictionary of original questions
    questions_dict = {q["id"]: q for q in original_data.get("questions", [])}
    
    issues = []
    success_count = 0
    now = datetime.now(timezone.utc).isoformat()
    
    # Process each item in done_data
    items_to_process = done_data if isinstance(done_data, list) else done_data.get("items", [])
    
    for item in items_to_process:
        qid = item.get("question_id")
        if not qid:
            continue
            
        orig_q = questions_dict.get(qid)
        if not orig_q:
            print(f"Warning: Question ID {qid} not found in original dataset. Skipping.")
            continue
            
        # Check standard answer consistency
        orig_ans = orig_q.get("correct_answer")
        done_ans = item.get("correct_answer")
        if done_ans and clean(done_ans) != clean(orig_ans):
            issues.append(f"QID {qid}: Answer mismatch! Original: {orig_ans}, Generated: {done_ans}")
            # Do NOT update answer, but proceed with explanation
            
        # Extract fields
        explanation = clean_preserve_newlines(item.get("explanation"))
        key_point = clean(item.get("key_point"))
        flashcard_front = clean(item.get("flashcard_front"))
        flashcard_back = clean(item.get("flashcard_back"))
        flashcard_summary = clean(item.get("flashcard_summary"))
        
        # Check explanation quality
        if not explanation:
            issues.append(f"QID {qid}: Missing explanation")
            continue
        if len(explanation) < 24:
            issues.append(f"QID {qid}: Short explanation ({len(explanation)} chars)")
            
        # Merge fields
        orig_q["explanation"] = explanation
        orig_q["key_point"] = key_point
        orig_q["flashcard_front"] = flashcard_front
        orig_q["flashcard_back"] = flashcard_back
        orig_q["flashcard_summary"] = flashcard_summary
        
        # Update review status and model
        orig_q["review_status"] = "ai_generated"
        orig_q["explanation_model"] = "antigravity-subagent"
        orig_q["explanation_generated_at"] = now
        
        # Optionally category if provided
        if item.get("category"):
            orig_q["category"] = clean(item.get("category"))
            orig_q["category_confidence"] = clean(item.get("category_confidence") or "medium")
            orig_q["category_source"] = "auto"
            
        success_count += 1
        
    # Write back to original JSON
    original_data["updated_at"] = now
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(original_data, f, ensure_ascii=False, indent=2)
        
    # Update progress JSON
    progress_data = {"completed": 0, "total": len(original_data.get("questions", [])), "issues": []}
    if progress_path.exists():
        try:
            with open(progress_path, 'r', encoding='utf-8') as f:
                progress_data = json.load(f)
        except Exception:
            pass
            
    # Calculate how many are actually completed in the dataset
    completed_in_dataset = sum(1 for q in original_data.get("questions", []) if q.get("review_status") == "ai_generated")
    progress_data["completed"] = completed_in_dataset
    
    # Append new issues, avoid duplicates
    existing_issues = set(progress_data.get("issues", []))
    for iss in issues:
        if iss not in existing_issues:
            progress_data["issues"].append(iss)
            
    # Save progress
    progress_path.parent.mkdir(parents=True, exist_ok=True)
    with open(progress_path, 'w', encoding='utf-8') as f:
        json.dump(progress_data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully imported {success_count} questions. Total completed: {completed_in_dataset}/{progress_data['total']}. Issues found: {len(issues)}")

if __name__ == "__main__":
    main()
