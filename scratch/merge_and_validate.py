import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

# 禁用詞列表
BANNED_PHRASES = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "題目中選項 A 所代表的鑑別或處置",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
    "標準答案所接受的判斷",
    "雖然與題目主題相關",
    "與標準答案的關鍵判斷不一致",
    "對照本題核心解析",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "原始解析重點指出",
    "原解析重點"
]

def clean_text(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()

def check_explanation_quality(question_number, explanation):
    issues = []
    
    # 檢查是否含有三大段
    if "【題幹解析】" not in explanation:
        issues.append(f"Q{question_number}: 缺少 【題幹解析】")
    if "【選項詳解】" not in explanation:
        issues.append(f"Q{question_number}: 缺少 【選項詳解】")
    if "【核心考點】" not in explanation:
        issues.append(f"Q{question_number}: 缺少 【核心考點】")
        
    # 檢查禁用詞
    for phrase in BANNED_PHRASES:
        if phrase in explanation:
            issues.append(f"Q{question_number}: 包含禁用詞 '{phrase}'")
            
    # 檢查選項 A-D 的標記
    for opt in ["- A.", "- B.", "- C.", "- D."]:
        if opt not in explanation:
            issues.append(f"Q{question_number}: 缺少選項標記 '{opt}'")
            
    # 檢查是否有同一個句子重複出現在多個選項中
    # 粗略切分選項來說明
    parts = explanation.split("- ")
    opt_texts = []
    for p in parts:
        if p.startswith("A.") or p.startswith("B.") or p.startswith("C.") or p.startswith("D."):
            opt_texts.append(p[2:].strip())
            
    if len(opt_texts) >= 3:
        # 尋找是否有長度大於 8 的子句重複出現在 3 個以上的選項中
        # 簡單用逗號、句號切分
        clauses_count = {}
        for text in opt_texts:
            clauses = re.split(r"[，。；、\s]", text)
            seen_in_this_opt = set()
            for c in clauses:
                c = c.strip()
                # 排除純英文單字 (如藥名、菌名) 的誤判：必須包含中文字，或長度大於 15
                has_chinese = bool(re.search(r"[\u4e00-\u9fa5]", c))
                if len(c) > 8 and (has_chinese or len(c) > 15):
                    seen_in_this_opt.add(c)
            for c in seen_in_this_opt:
                clauses_count[c] = clauses_count.get(c, 0) + 1
        
        for clause, count in clauses_count.items():
            if count >= 3:
                issues.append(f"Q{question_number}: 子句 '{clause}' 重複出現在 {count} 個選項中 (重複度過高)")
                
    return issues

def main():
    updates_dir = Path("scratch/rewrite_updates/108-2_medicine-2")
    source_file = Path("public/data/exams/108-2/medicine-2.json")
    
    if not source_file.exists():
        print(f"Error: Source file {source_file} not found.")
        sys.exit(1)
        
    if not updates_dir.exists():
        print(f"Error: Updates directory {updates_dir} not found.")
        sys.exit(1)
        
    # 讀取原始考卷
    with open(source_file, "r", encoding="utf-8") as f:
        source_data = json.load(f)
        
    questions = source_data.get("questions", [])
    q_dict = {q["id"]: q for q in questions}
    
    update_files = list(updates_dir.glob("*.json"))
    if not update_files:
        print("No update files found in the directory.")
        sys.exit(0)
        
    print(f"Found {len(update_files)} update files.")
    
    all_issues = []
    merged_count = 0
    now_ts = datetime.now(timezone.utc).isoformat()
    
    for uf in sorted(update_files):
        print(f"Processing {uf.name}...")
        try:
            with open(uf, "r", encoding="utf-8") as f:
                up_data = json.load(f)
        except Exception as e:
            all_issues.append(f"File {uf.name} is not valid JSON: {str(e)}")
            continue
            
        # 驗證結構
        if "updates" not in up_data:
            all_issues.append(f"File {uf.name} is missing 'updates' field.")
            continue
            
        updates = up_data["updates"]
        for up in updates:
            qid = up.get("question_id")
            qnum = up.get("question_number")
            
            if not qid or qnum is None:
                all_issues.append(f"File {uf.name} has update item with missing id/question_number")
                continue
                
            orig_q = q_dict.get(qid)
            if not orig_q:
                all_issues.append(f"QID {qid} (Q{qnum}) from {uf.name} not found in source file.")
                continue
                
            # 檢查品質
            expl = up.get("explanation", "")
            q_issues = check_explanation_quality(qnum, expl)
            if q_issues:
                all_issues.extend([f"[{uf.name}] {iss}" for iss in q_issues])
                
            # 檢查其他必備欄位
            for fld in ["key_point", "flashcard_summary", "flashcard_front", "flashcard_back"]:
                if not up.get(fld):
                    all_issues.append(f"[{uf.name}] Q{qnum}: 缺少欄位 '{fld}' 或內容為空。")
            
            # 若無嚴重問題 (或只列出警告，若要硬性阻擋，我們在後面判斷)
            # 將欄位 merge 到記憶體中的原始資料
            orig_q["explanation"] = expl
            orig_q["key_point"] = clean_text(up.get("key_point"))
            orig_q["flashcard_summary"] = clean_text(up.get("flashcard_summary"))
            orig_q["flashcard_front"] = clean_text(up.get("flashcard_front"))
            orig_q["flashcard_back"] = clean_text(up.get("flashcard_back"))
            orig_q["review_status"] = "ai_generated"
            orig_q["explanation_model"] = "codex-high-quality-rewrite"
            orig_q["explanation_generated_at"] = now_ts
            
            # 可選的 manual_review_notes 繼承
            if "manual_review_notes" in up:
                orig_q["manual_review_notes"] = up["manual_review_notes"]
                
            merged_count += 1
            
    if all_issues:
        print("\n=== FINDINGS AND ISSUES ===")
        for iss in all_issues:
            print(f"- {iss}")
        print("\nThere are quality or format issues. Please fix them before writing to source file.")
        # 為了安全，即使有問題，如果我們只是想跑測試，我們不寫入。
        # 不過如果只有少數警告，可以視情況決定。這裡我們不直接寫入以策安全。
        sys.exit(1)
    else:
        # 寫回原始考卷
        source_data["updated_at"] = now_ts
        with open(source_file, "w", encoding="utf-8") as f:
            json.dump(source_data, f, ensure_ascii=False, indent=2)
        print(f"\nAll check passed! Successfully merged {merged_count} questions into {source_file}.")

if __name__ == "__main__":
    main()
