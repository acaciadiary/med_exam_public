import json
import os
import re

source_path = r"d:\Antigravity\med_exam_public\public\data\exams\109-2\medicine-4.json"
updates_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\109-2_medicine-4"
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
    "非本題的答案",
    "不是本題答案",
    "不是本題的答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
    "此選項不是最佳答案",
    "最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "原始解析重點指出",
    "作答時應回到題幹線索與標準答案比對",
    "熟悉疾病機轉、臨床表現、診斷檢查與治療原則",
    "代表的鑑別或處置",
    "非正確選項"
]

allowed_fields = {
    "question_id", "question_number", "explanation", "key_point",
    "flashcard_front", "flashcard_back", "flashcard_summary",
    "review_status", "explanation_model", "explanation_generated_at",
    "manual_review_notes"
}

target_rework_questions = [3, 13, 14, 29, 32, 71, 72, 76]

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
    medical_flags = []
    rework_details = {}

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
                
            # 2. 對照 source
            src_q = source_questions.get(q_num)
            if not src_q:
                errors.append(f"在來源考卷中找不到題號 {q_num}")
                src_text = ""
                src_answer = ""
            else:
                src_text = src_q.get("question_text", "")
                src_answer = src_q.get("answer", "")
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
            opts_found = {}
            for opt in ["A", "B", "C", "D"]:
                pattern = rf"-\s*{opt}\."
                if not re.search(pattern, exp):
                    errors.append(f"找不到選項說明: - {opt}.")
                else:
                    opts_found[opt] = True

            # 5. 禁用詞檢查
            for phrase in banned_phrases:
                if phrase in exp:
                    errors.append(f"包含禁用詞: '{phrase}'")
                for field in ["key_point", "flashcard_summary", "flashcard_back"]:
                    val = up.get(field, "")
                    if val and phrase in val:
                        errors.append(f"{field} 包含禁用詞: '{phrase}'")
            
            # 6. 選項內容拆分與重複性檢查
            parts = re.split(r"-\s*[A-D]\.", exp)
            opts_content = []
            if len(parts) >= 5:
                # 正常拆分成 4 個選項
                for idx, opt_char in enumerate(["A", "B", "C", "D"]):
                    # 選項詳解結束於下一個標題（例如【核心考點】）
                    opt_text = parts[idx+1]
                    if idx == 3: # D. 之後可能會接 【核心考點】
                        opt_text = opt_text.split("【核心考點】")[0]
                    opt_text = opt_text.strip()
                    opts_content.append((opt_char, opt_text))
                
                # A-D 是否有各自的具體醫學理由，而不是共用同一段話，或內容完全相同
                for i in range(len(opts_content)):
                    for j in range(i+1, len(opts_content)):
                        char1, text1 = opts_content[i]
                        char2, text2 = opts_content[j]
                        if text1 == text2 and len(text1) > 10:
                            errors.append(f"選項 {char1} 與 {char2} 的說明內容完全相同")
                        # 檢查句首重複或段落相似度
                        # 比如兩個選項的開頭 15 個字一樣
                        if len(text1) > 15 and len(text2) > 15 and text1[:15] == text2[:15]:
                            errors.append(f"選項 {char1} 與 {char2} 開頭 15 個字重複: '{text1[:15]}'")
            else:
                errors.append(f"無法正確分割 A-D 選項 (分割出 {len(parts)-1} 個部分)")

            # 檢查是否有同一長句或同一核心段落出現在三個以上選項
            # 我們可以用簡單的 sliding window 或比對句子
            sentences = []
            for opt_char, opt_text in opts_content:
                # 斷句
                sents = re.split(r"[，。；；、\n]", opt_text)
                sents = [s.strip() for s in sents if len(s.strip()) > 8]
                sentences.append((opt_char, sents))
            
            # 檢查是否有任何句子（長度 > 8）出現在 3 個以上的選項中
            all_sents_count = {}
            for opt_char, sents in sentences:
                for s in set(sents): # 同一選項內去重
                    all_sents_count[s] = all_sents_count.get(s, []) + [opt_char]
            
            for s, opts in all_sents_count.items():
                if len(opts) >= 3:
                    errors.append(f"句子 '{s}' 同時出現在三個以上的選項中: {opts}")

            # 7. 否定問法檢查
            is_negative_q = False
            for neg_word in ["錯誤", "不正確", "不合適", "非", "不宜", "不屬", "何者除外", "何者為非"]:
                if neg_word in src_text:
                    is_negative_q = True
                    break
            
            if is_negative_q:
                # 在否定問題中，應該說明正確答案（即「錯誤的敘述」）為什麼是錯的，
                # 以及其他選項（正確的敘述）在醫學上為什麼是正確或合理的。
                # 我們可以藉由關鍵字來粗略檢查，或至少檢查有沒有做這個描述。
                # 這裡我們先做一個標記，在人工複核時重點看否定問法題目的解釋邏輯。
                pass

            # 8. 欄位長度/具體性檢查
            kp = up.get("key_point", "").strip()
            fs = up.get("flashcard_summary", "").strip()
            fb = up.get("flashcard_back", "").strip()
            
            if len(kp) < 5:
                errors.append(f"key_point 太短 ({len(kp)} 字)")
            if len(fs) < 5:
                errors.append(f"flashcard_summary 太短 ({len(fs)} 字)")
            if len(fb) < 5:
                errors.append(f"flashcard_back 太短 ({len(fb)} 字)")
                
            # 9. 醫學錯誤 / 官方答案疑義 / 人工複核
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

            # 如果是先前被要求返工的 8 題，我們記錄其詳解內容，以便輸出給我們看
            if q_num in target_rework_questions:
                rework_details[q_num] = {
                    "question_text": src_text,
                    "answer": src_answer,
                    "explanation": exp,
                    "key_point": kp,
                    "flashcard_summary": fs,
                    "flashcard_back": fb,
                    "errors": errors,
                    "is_negative": is_negative_q
                }

    # 輸出成 json 以便之後我們在程式中讀取
    output_report = {
        "total_checked": total_checked,
        "passed": passed_questions,
        "failed": all_errors,
        "medical_flags": medical_flags,
        "rework_details": rework_details
    }
    with open(r"d:\Antigravity\med_exam_public\scratch\audit_109_2_medicine_4_report.json", "w", encoding="utf-8") as f:
        json.dump(output_report, f, ensure_ascii=False, indent=2)

    print(f"Audit Completed.")
    print(f"Total checked: {total_checked}")
    print(f"Passed: {len(passed_questions)}")
    print(f"Failed: {len(all_errors)}")
    print(f"Failed questions: {list(all_errors.keys())}")

if __name__ == "__main__":
    audit()
