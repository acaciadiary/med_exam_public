import json
import os
from datetime import datetime, timezone, timedelta

def main():
    source_path = "public/data/exams/114-2/medicine-3.json"
    target_dir = "scratch/rewrite_updates/114-2_medicine-3"
    target_path = os.path.join(target_dir, "q001-q010.json")
    
    # 確保目標資料夾存在
    os.makedirs(target_dir, exist_ok=True)
    
    # 讀取來源考卷
    with open(source_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    questions = data.get("questions", [])
    
    # 取得當前台北時間的 ISO 字串
    tz_taipei = timezone(timedelta(hours=8))
    now_str = datetime.now(tz_taipei).isoformat()
    
    updates = []
    # 提取第 1 到 10 題 (question_number 1 到 10)
    for q in questions:
        q_num = q.get("question_number")
        if 1 <= q_num <= 10:
            update_item = {
                "question_id": q.get("id"),
                "question_number": q_num,
                "explanation": q.get("explanation"),
                "key_point": q.get("key_point"),
                "flashcard_front": q.get("flashcard_front"),
                "flashcard_back": q.get("flashcard_back"),
                "flashcard_summary": q.get("flashcard_summary"),
                "review_status": "ai_generated",
                "explanation_model": "codex-high-quality-rewrite",
                "explanation_generated_at": now_str,
                "manual_review_notes": []
            }
            updates.append(update_item)
            
    # 組裝成規定的 update JSON 結構
    result = {
        "source_file": "public/data/exams/114-2/medicine-3.json",
        "dataset_id": "114-2_medicine-3",
        "range": { "start": 1, "end": 10 },
        "updates": updates
    }
    
    # 寫入目標檔案
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully extracted questions 1-10 to {target_path}")

if __name__ == "__main__":
    main()
