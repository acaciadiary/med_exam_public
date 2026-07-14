import json
import os
import re

def main():
    target_path = "scratch/rewrite_updates/114-2_medicine-3/q001-q010.json"
    
    if not os.path.exists(target_path):
        print(f"Error: Target file {target_path} does not exist.")
        return
        
    with open(target_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"JSON Parse Error: {e}")
            return
            
    # 1. 檢查根層級欄位
    allowed_root_keys = {"source_file", "dataset_id", "range", "updates"}
    root_keys = set(data.keys())
    extra_root_keys = root_keys - allowed_root_keys
    missing_root_keys = allowed_root_keys - root_keys
    
    if extra_root_keys:
        print(f"Error: Extra root keys found: {extra_root_keys}")
    if missing_root_keys:
        print(f"Error: Missing root keys: {missing_root_keys}")
        
    # 2. 檢查 range 格式
    r = data.get("range", {})
    if not isinstance(r, dict) or "start" not in r or "end" not in r:
        print("Error: 'range' format is incorrect. Should be {'start': X, 'end': Y}")
        
    # 3. 檢查 updates 陣列中的每個 item
    updates = data.get("updates", [])
    if not isinstance(updates, list) or len(updates) == 0:
        print("Error: 'updates' is empty or not a list")
        return
        
    allowed_item_keys = {
        "question_id", "question_number", "explanation", "key_point",
        "flashcard_front", "flashcard_back", "flashcard_summary",
        "review_status", "explanation_model", "explanation_generated_at",
        "manual_review_notes"
    }
    
    banned_words = [
        "非本題答案",
        "不是本題標準答案",
        "回到題幹線索",
        "請用題幹線索連回",
        "題目中選項 A 所代表的鑑別或處置",
        "不能最精準回答本題",
        "最符合題幹",
        "核心記憶點",
        "定義、機轉、典型表現或處置原則",
        "此選項不是最佳答案",
        "與正確答案的關鍵判斷點不一致",
        "原始解析重點指出",
        "作答時應回到題幹線索與標準答案比對",
        "熟悉疾病機轉、臨床表現、診斷檢查與治療原則",
        "心臟內科的基本判斷能力",
        "的基本判斷能力"
    ]
    
    errors = []
    
    for i, q in enumerate(updates):
        q_num = q.get("question_number")
        q_id = q.get("question_id")
        
        # 檢查欄位
        item_keys = set(q.keys())
        extra_keys = item_keys - allowed_item_keys
        missing_keys = allowed_item_keys - item_keys
        
        if extra_keys:
            errors.append(f"Q{q_num} ({q_id}): Extra keys found: {extra_keys}")
        if missing_keys:
            errors.append(f"Q{q_num} ({q_id}): Missing keys: {missing_keys}")
            
        explanation = q.get("explanation", "")
        if not explanation:
            errors.append(f"Q{q_num} ({q_id}): Explanation is empty")
            continue
            
        # 檢查三大標題
        for header in ["【題幹解析】", "【選項詳解】", "【核心考點】"]:
            if header not in explanation:
                errors.append(f"Q{q_num} ({q_id}): Missing header {header} in explanation")
                
        # 檢查 A, B, C, D 選項
        for opt in ["A", "B", "C", "D"]:
            pattern = rf"-\s+{opt}\."
            if not re.search(pattern, explanation):
                errors.append(f"Q{q_num} ({q_id}): Option {opt} explanation not found in the format '- {opt}.'")
                
        # 檢查禁用詞
        for bw in banned_words:
            if bw in explanation:
                errors.append(f"Q{q_num} ({q_id}): Explanation contains banned word '{bw}'")
                
        # 檢查 key_point 等欄位是否為空
        for field in ["key_point", "flashcard_front", "flashcard_back", "flashcard_summary"]:
            val = q.get(field, "")
            if not val:
                errors.append(f"Q{q_num} ({q_id}): Field '{field}' is empty")
                
    if errors:
        print("Validation failed with the following errors:")
        for err in errors:
            print(f"- {err}")
    else:
        print("Validation passed successfully! No errors found.")

if __name__ == "__main__":
    main()
