import os
import json
import sys
import re
from pathlib import Path
from datetime import datetime, timezone

# 禁用模板句清單
BANNED_TEMPLATES = [
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
    "原始解析重點指出"
]

def check_banned_phrases(text, q_num):
    issues = []
    if not text:
        return issues
    for phrase in BANNED_TEMPLATES:
        if phrase in text:
            issues.append(f"第 {q_num} 題含有禁用模板句: '{phrase}'")
    return issues

def validate_update_file(file_path, source_questions):
    issues = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return [f"無法解析 JSON 檔案 {file_path.name}: {e}"], None

    # 檢查基本結構
    required_keys = ["source_file", "dataset_id", "range", "updates"]
    for k in required_keys:
        if k not in data:
            issues.append(f"缺少必要欄位: '{k}'")
    
    if issues:
        return issues, None

    updates = data["updates"]
    if not isinstance(updates, list):
        return ["'updates' 必須是一個陣列"], None

    valid_updates = []
    for u in updates:
        q_num = u.get("question_number")
        q_id = u.get("question_id")
        
        if q_num is None or q_id is None:
            issues.append(f"更新項目中缺少 question_number 或 question_id")
            continue
            
        # 尋找原始題目
        orig_q = source_questions.get(q_id)
        if not orig_q:
            issues.append(f"在原始考卷中找不到 question_id: {q_id}")
            continue
            
        if orig_q.get("question_number") != q_num:
            issues.append(f"題目 ID {q_id} 與題號 {q_num} 在原始考卷中不匹配")
            continue

        # 檢驗詳解內容
        exp = u.get("explanation", "")
        if not exp:
            issues.append(f"第 {q_num} 題缺少 explanation")
            continue
            
        # 檢驗是否有三段標題
        for header in ["【題幹解析】", "【選項詳解】", "【核心考點】"]:
            if header not in exp:
                issues.append(f"第 {q_num} 題的詳解缺少結構標題: {header}")

        # 檢驗選項詳解是否有 A-D 各自說明
        for opt in ["- A.", "- B.", "- C.", "- D."]:
            if opt not in exp:
                issues.append(f"第 {q_num} 題的選項詳解中可能缺少選項說明: {opt}")

        # 檢驗禁用詞
        phrase_issues = check_banned_phrases(exp, q_num)
        issues.extend(phrase_issues)

        # 檢查 key_point 等其他欄位是否存在且不為空
        for field in ["key_point", "flashcard_summary", "flashcard_front", "flashcard_back"]:
            val = u.get(field, "")
            if not val or not str(val).strip():
                issues.append(f"第 {q_num} 題的欄位 {field} 為空")
            else:
                field_phrase_issues = check_banned_phrases(str(val), f"{q_num} ({field})")
                issues.extend(field_phrase_issues)

        valid_updates.append(u)
        
    return issues, valid_updates

def main():
    source_path = Path("public/data/exams/110-2/medicine-2.json")
    updates_dir = Path("scratch/rewrite_updates/110-2_medicine-2")
    
    if not source_path.exists():
        print(f"錯誤：找不到來源考卷檔案 {source_path}")
        sys.exit(1)
        
    # 讀取來源考卷
    with open(source_path, 'r', encoding='utf-8') as f:
        source_data = json.load(f)
        
    source_questions = {q["id"]: q for q in source_data.get("questions", [])}
    
    if not updates_dir.exists():
        print(f"提示：更新目錄 {updates_dir} 還不存在，將為您建立。")
        updates_dir.mkdir(parents=True, exist_ok=True)
        sys.exit(0)
        
    json_files = list(updates_dir.glob("*.json"))
    if not json_files:
        print("沒有找到待合併的 updates JSON 檔案。")
        sys.exit(0)
        
    all_success = True
    merged_count = 0
    now_ts = datetime.now(timezone.utc).isoformat()
    
    for jf in sorted(json_files):
        print(f"正在驗證: {jf.name}")
        issues, valid_updates = validate_update_file(jf, source_questions)
        
        if issues:
            print(f"  [FAIL] 驗證失敗，有以下問題:")
            for iss in issues:
                print(f"    - {iss}")
            all_success = False
        else:
            print("  [OK] 驗證成功，準備合併...")
            for u in valid_updates:
                q_id = u["question_id"]
                q = source_questions[q_id]
                
                # 更新欄位
                q["explanation"] = u["explanation"].strip()
                q["key_point"] = u["key_point"].strip()
                q["flashcard_summary"] = u["flashcard_summary"].strip()
                q["flashcard_front"] = u["flashcard_front"].strip()
                q["flashcard_back"] = u["flashcard_back"].strip()
                q["review_status"] = "ai_generated"
                q["explanation_model"] = "codex-high-quality-rewrite"
                q["explanation_generated_at"] = now_ts
                
                merged_count += 1
                
    if not all_success:
        print("\n部分檔案驗證失敗。在所有問題修正之前，不會寫入原始考卷。")
        sys.exit(1)
        
    # 寫回原始考卷
    source_data["updated_at"] = now_ts
    with open(source_path, 'w', encoding='utf-8') as f:
        json.dump(source_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n[SUCCESS] 合併成功！共更新了 {merged_count} 題。")
    print(f"來源考卷 {source_path.name} 已更新。")
    
if __name__ == "__main__":
    main()
