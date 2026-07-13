import json
import os
import re

source_path = r"d:\Antigravity\med_exam_public\public\data\exams\110-2\medicine-3.json"
updates_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\110-2_medicine-3"
update_files = [
    "q001-q010.json",
    "q011-q020.json",
    "q021-q030.json",
    "q031-q040.json",
    "q041-q050.json",
    "q051-q060.json",
    "q061-q070.json",
    "q071-q080.json"
]

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
    "原始解析重點指出",
    "作答時應回到題幹線索與標準答案比對",
    "熟悉疾病機轉、臨床表現、診斷檢查與治療原則",
    "代表的鑑別或處置"
]

allowed_fields = {
    "question_id", "question_number", "explanation", "key_point",
    "flashcard_front", "flashcard_back", "flashcard_summary",
    "review_status", "explanation_model", "explanation_generated_at",
    "manual_review_notes"
}

def audit():
    # 載入 source
    with open(source_path, "r", encoding="utf-8") as f:
        source_data = json.load(f)
    
    # 建立 source dict
    source_questions = {}
    for q in source_data.get("questions", []):
        source_questions[q["question_number"]] = q

    total_checked = 0
    all_errors = {}
    passed_questions = []
    has_extra_fields = []
    medical_flags = []

    for file_name in update_files:
        file_path = os.path.join(updates_dir, file_name)
        if not os.path.exists(file_path):
            print(f"Error: file not found: {file_path}")
            continue
        
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                update_data = json.load(f)
            except Exception as e:
                print(f"Error parsing JSON {file_name}: {e}")
                continue
            
        for up in update_data.get("updates", []):
            q_num = up.get("question_number")
            q_id = up.get("question_id")
            
            total_checked += 1
            errors = []
            
            # 1. 欄位檢查
            fields = set(up.keys())
            extra = fields - allowed_fields
            if extra:
                errors.append(f"包含未允許欄位: {extra}")
                has_extra_fields.append(q_num)
                
            # 2. 對照 source
            src_q = source_questions.get(q_num)
            if not src_q:
                errors.append(f"在來源考卷中找不到題號 {q_num}")
            else:
                if src_q.get("id") != q_id:
                    errors.append(f"question_id 不符。來源: {src_q.get('id')}, 更新: {q_id}")
            
            # 3. 三大標題檢查
            exp = up.get("explanation", "")
            if "【題幹解析】" not in exp:
                errors.append("缺少【題幹解析】標題")
            if "【選項詳解】" not in exp:
                errors.append("缺少【選項詳解】標題")
            if "【核心考點】" not in exp:
                errors.append("缺少【核心考點】標題")
                
            # 4. A-D 各成一行
            for opt in ["A", "B", "C", "D"]:
                pattern = rf"-\s*{opt}\."
                if not re.search(pattern, exp):
                    errors.append(f"找不到選項說明: - {opt}.")
            
            # 5. 禁用詞檢查
            for phrase in banned_phrases:
                if phrase in exp:
                    errors.append(f"包含禁用詞: '{phrase}'")
                if phrase in up.get("key_point", ""):
                    errors.append(f"key_point 包含禁用詞: '{phrase}'")
                if phrase in up.get("flashcard_summary", ""):
                    errors.append(f"flashcard_summary 包含禁用詞: '{phrase}'")
                if phrase in up.get("flashcard_back", ""):
                    errors.append(f"flashcard_back 包含禁用詞: '{phrase}'")
                    
            # 6. 重複內容檢查
            opts_content = []
            parts = re.split(r"-\s*[A-D]\.", exp)
            if len(parts) >= 5:
                for idx, opt_char in enumerate(["A", "B", "C", "D"]):
                    opt_text = parts[idx+1].strip()
                    opts_content.append((opt_char, opt_text))
                for i in range(len(opts_content)):
                    for j in range(i+1, len(opts_content)):
                        char1, text1 = opts_content[i]
                        char2, text2 = opts_content[j]
                        if text1 == text2 and len(text1) > 10:
                            errors.append(f"選項 {char1} 與 {char2} 的說明內容完全相同")
            
            # 7. 欄位長度/具體性檢查
            kp = up.get("key_point", "").strip()
            fs = up.get("flashcard_summary", "").strip()
            fb = up.get("flashcard_back", "").strip()
            
            if len(kp) < 5:
                errors.append(f"key_point 太短 ({len(kp)} 字)")
            if len(fs) < 5:
                errors.append(f"flashcard_summary 太短 ({len(fs)} 字)")
            if len(fb) < 5:
                errors.append(f"flashcard_back 太短 ({len(fb)} 字)")
                
            # 8. 醫學錯誤 / 官方答案疑義
            mrn = up.get("manual_review_notes", [])
            if mrn:
                medical_flags.append((q_num, mrn))
            if "人工複核" in exp or "官方答案" in exp or "答案疑義" in exp:
                if q_num not in [m[0] for m in medical_flags]:
                    medical_flags.append((q_num, ["說明中提及人工複核/答案疑義"]))
            
            if errors:
                all_errors[q_num] = errors
            else:
                passed_questions.append(q_num)

    # 輸出成 json 以便之後我們在程式中讀取
    output_report = {
        "total_checked": total_checked,
        "passed": passed_questions,
        "failed": all_errors,
        "medical_flags": medical_flags
    }
    with open(r"d:\Antigravity\med_exam_public\scratch\audit_report.json", "w", encoding="utf-8") as f:
        json.dump(output_report, f, ensure_ascii=False, indent=2)

    print(f"Total checked: {total_checked}")
    print(f"Passed: {len(passed_questions)}")
    print(f"Failed: {len(all_errors)}")

if __name__ == "__main__":
    audit()
