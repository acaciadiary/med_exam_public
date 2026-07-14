import os
import json
import glob

def merge():
    source_file_path = "public/data/exams/110-1/medicine-6.json"
    updates_dir = "scratch/rewrite_updates/110-1_medicine-6"
    
    if not os.path.exists(source_file_path):
        print(f"Error: Source file {source_file_path} not found.")
        return
        
    with open(source_file_path, "r", encoding="utf-8") as f:
        source_data = json.load(f)
        
    questions = source_data.get("questions", [])
    question_map = {q["id"]: q for q in questions}
    
    update_files = glob.glob(os.path.join(updates_dir, "q*.json"))
    if not update_files:
        print(f"Error: No update files found in {updates_dir}.")
        return
        
    merged_count = 0
    
    for up_path in sorted(update_files):
        print(f"Processing update file: {up_path}")
        with open(up_path, "r", encoding="utf-8") as f:
            up_data = json.load(f)
            
        updates = up_data.get("updates", [])
        for update in updates:
            q_id = update["question_id"]
            if q_id in question_map:
                target_q = question_map[q_id]
                
                # 合併允許的欄位
                allowed_fields = [
                    "explanation",
                    "key_point",
                    "flashcard_summary",
                    "flashcard_front",
                    "flashcard_back",
                    "review_status",
                    "explanation_model",
                    "explanation_generated_at",
                    "manual_review_notes"
                ]
                
                for field in allowed_fields:
                    if field in update:
                        target_q[field] = update[field]
                
                merged_count += 1
            else:
                print(f"Warning: Question ID {q_id} from {up_path} not found in source file.")
                
    # 寫回原始檔案
    with open(source_file_path, "w", encoding="utf-8") as f:
        json.dump(source_data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully merged {merged_count} question updates into {source_file_path}.")

if __name__ == "__main__":
    merge()
