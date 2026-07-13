# -*- coding: utf-8 -*-
import json
import sys

def main():
    filepath = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\110-2_medicine-3\q061-q070.json"
    print("Reading file:", filepath)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("JSON parse failed:", e)
        sys.exit(1)

    print("JSON parsed successfully!")
    print("Dataset ID:", data.get("dataset_id"))
    print("Source File:", data.get("source_file"))
    print("Range:", data.get("range"))
    print("Updates count:", len(data.get("updates", [])))

    banned_phrases = [
        "非本題答案",
        "不是本題標準答案",
        "回到題幹線索",
        "請用題幹線索連回",
        "不能最精準回答本題",
        "最符合題幹",
        "核心記憶點",
        "定義、機轉、典型表現或處置原則",
        "此選項不是最佳答案",
        "與正確答案的關鍵判斷點不一致",
        "作答時應回到題幹線索與標準答案比對",
        "熟悉疾病機轉、臨床表現、診斷檢查與治療原則",
        "原始解析重點指出",
        "既存解析指出",
        "既有解析指出",
    ]

    has_errors = False
    for item in data.get("updates", []):
        q_num = item.get("question_number")
        q_id = item.get("question_id")
        
        # 欄位檢查
        required_fields = [
            "question_id", "question_number", "explanation", "key_point",
            "flashcard_front", "flashcard_back", "flashcard_summary",
            "review_status", "explanation_model", "explanation_generated_at",
            "manual_review_notes"
        ]
        
        for field in required_fields:
            if field not in item:
                print(f"Q{q_num} ({q_id}): Missing field '{field}'")
                has_errors = True
        
        # 禁用詞檢查
        item_str = json.dumps(item, ensure_ascii=False)
        for phrase in banned_phrases:
            if phrase in item_str:
                print(f"Q{q_num} ({q_id}): Contains banned phrase '{phrase}'")
                has_errors = True
                
        # 格式檢查
        explanation = item.get("explanation", "")
        if "【題幹解析】" not in explanation:
            print(f"Q{q_num} ({q_id}): Missing '【題幹解析】'")
            has_errors = True
        if "【選項詳解】" not in explanation:
            print(f"Q{q_num} ({q_id}): Missing '【選項詳解】'")
            has_errors = True
        if "【核心考點】" not in explanation:
            print(f"Q{q_num} ({q_id}): Missing '【核心考點】'")
            has_errors = True
            
        for opt in ["A.", "B.", "C.", "D."]:
            if f"- {opt}" not in explanation and f"\n{opt}" not in explanation:
                print(f"Q{q_num} ({q_id}): Missing option detail for {opt}")
                has_errors = True

    if has_errors:
        print("Validation FAILED with errors.")
        sys.exit(1)
    else:
        print("All checks passed successfully!")

if __name__ == "__main__":
    main()
