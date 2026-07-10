import json
import sys
from pathlib import Path
from datetime import datetime, timezone

def merge_updates(exam_json_path, updates_dir_path):
    exam_file = Path(exam_json_path)
    updates_dir = Path(updates_dir_path)
    
    if not exam_file.exists():
        print(f"Error: Exam file {exam_file} does not exist.")
        sys.exit(1)
        
    if not updates_dir.exists():
        print(f"Error: Updates directory {updates_dir} does not exist.")
        sys.exit(1)
        
    # 讀取原始考卷
    try:
        exam_data = json.loads(exam_file.read_text(encoding="utf-8-sig"))
    except Exception as e:
        print(f"Error loading exam JSON: {e}")
        sys.exit(1)
        
    # 將原始題目建立索引，加快尋找速度
    questions = exam_data.get("questions", [])
    q_dict = {q.get("id"): q for q in questions}
    
    # 讀取所有 updates JSON
    update_files = sorted(updates_dir.glob("*.json"))
    if not update_files:
        print(f"No update JSON files found in {updates_dir}")
        return
        
    merged_count = 0
    now_str = datetime.now(timezone.utc).isoformat()
    
    for uf in update_files:
        try:
            update_data = json.loads(uf.read_text(encoding="utf-8-sig"))
        except Exception as e:
            print(f"Error loading update JSON {uf.name}: {e}")
            continue
            
        updates_list = update_data.get("updates", [])
        for item in updates_list:
            qid = item.get("question_id")
            if not qid:
                continue
                
            if qid not in q_dict:
                print(f"Warning: Question {qid} not found in target exam file.")
                continue
                
            orig_q = q_dict[qid]
            
            # 更新允許的欄位
            allowed_fields = [
                "explanation", "key_point", "flashcard_front", "flashcard_back", 
                "flashcard_summary", "manual_review_notes"
            ]
            for field in allowed_fields:
                if field in item:
                    orig_q[field] = item[field]
            
            # 強制標示 AI 產生狀態與時間
            orig_q["review_status"] = item.get("review_status", "ai_generated")
            orig_q["explanation_model"] = item.get("explanation_model", "codex-high-quality-rewrite")
            orig_q["explanation_generated_at"] = item.get("explanation_generated_at", now_str)
            
            merged_count += 1
            
    # 將結果寫回原始考卷
    try:
        exam_file.write_text(json.dumps(exam_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Successfully merged {merged_count} questions into {exam_file.name}")
    except Exception as e:
        print(f"Error writing merged JSON back to file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge_updates.py <exam_json_path> <updates_dir_path>")
        sys.exit(1)
        
    merge_updates(sys.argv[1], sys.argv[2])
