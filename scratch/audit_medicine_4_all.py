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
    "此選項不是最佳答案",
    "此選項非最佳答案",
    "最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "原始解析重點指出",
    "作答時應回到題幹線索與標準答案比對",
    "非正確選項",
    "對照本題核心解析",
    "非最佳答案"
]

target_questions = [13, 36, 41, 44, 45, 47, 48, 49, 50, 59, 60, 71, 72, 77]

def audit_all():
    # 載入來源資料
    with open(source_path, "r", encoding="utf-8") as f:
        source_data = json.load(f)
    
    source_questions = {q["question_number"]: q for q in source_data.get("questions", [])}

    report = []
    failed_questions = {}
    passed_count = 0
    total_count = 0
    target_results = {}

    for file_name in update_files:
        file_path = os.path.join(updates_dir, file_name)
        if not os.path.exists(file_path):
            print(f"Error: file not found: {file_path}")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        for up in data.get("updates", []):
            total_count += 1
            q_num = up.get("question_number")
            q_id = up.get("question_id")
            exp = up.get("explanation", "")
            kp = up.get("key_point", "")
            fs = up.get("flashcard_summary", "")
            fb = up.get("flashcard_back", "")
            
            errors = []
            
            # 1. 欄位存在與長度
            if len(kp.strip()) < 5:
                errors.append(f"key_point 太短 ({len(kp)}字)")
            if len(fs.strip()) < 5:
                errors.append(f"flashcard_summary 太短 ({len(fs)}字)")
            if len(fb.strip()) < 5:
                errors.append(f"flashcard_back 太短 ({len(fb)}字)")
                
            # 2. 三大標題
            if "【題幹解析】" not in exp:
                errors.append("缺少【題幹解析】")
            if "【選項詳解】" not in exp:
                errors.append("缺少【選項詳解】")
            if "【核心考點】" not in exp:
                errors.append("缺少【核心考點】")
                
            # 3. 選項分割
            parts = re.split(r"-\s*[A-D]\.", exp)
            opts_content = []
            if len(parts) >= 5:
                for idx, char in enumerate(["A", "B", "C", "D"]):
                    opt_text = parts[idx+1]
                    if idx == 3:
                        opt_text = opt_text.split("【核心考點】")[0]
                    opt_text = opt_text.strip()
                    opts_content.append((char, opt_text))
                
                # A-D 內容重複比對
                for i in range(len(opts_content)):
                    for j in range(i+1, len(opts_content)):
                        c1, t1 = opts_content[i]
                        c2, t2 = opts_content[j]
                        if t1 == t2 and len(t1) > 10:
                            errors.append(f"選項 {c1} 與 {c2} 說明完全相同")
                        if len(t1) > 15 and len(t2) > 15 and t1[:15] == t2[:15]:
                            errors.append(f"選項 {c1} 與 {c2} 開頭 15 個字重複: '{t1[:15]}'")
                        if len(t1) > 15 and len(t2) > 15 and t1[-15:] == t2[-15:]:
                            errors.append(f"選項 {c1} 與 {c2} 結尾 15 個字重複: '{t1[-15:]}'")
            else:
                errors.append(f"無法正確分割選項 (得 {len(parts)-1} 個部分)")
                
            # 4. 禁用詞句
            for banned in banned_phrases:
                if banned in exp:
                    errors.append(f"說明包含禁用詞: '{banned}'")
                for field_name, field_val in [("key_point", kp), ("flashcard_summary", fs), ("flashcard_back", fb)]:
                    if banned in field_val:
                        errors.append(f"{field_name} 包含禁用詞: '{banned}'")
                        
            # 5. 跨選項句重複檢查 (3個選項以上)
            if len(opts_content) == 4:
                sentences = []
                for char, text in opts_content:
                    sents = re.split(r"[，。；；、\n]", text)
                    sents = [s.strip() for s in sents if len(s.strip()) > 8]
                    sentences.append((char, sents))
                    
                sents_count = {}
                for char, sents in sentences:
                    for s in set(sents):
                        sents_count[s] = sents_count.get(s, []) + [char]
                for s, chars in sents_count.items():
                    if len(chars) >= 3:
                        errors.append(f"句子 '{s}' 在 3 個以上選項重複: {chars}")

            # 6. 否定問法檢查
            src_q = source_questions.get(q_num)
            is_negative_q = False
            src_text = ""
            if src_q:
                src_text = src_q.get("question_text", "")
                for neg_word in ["錯誤", "不正確", "不合適", "非", "不宜", "不屬", "何者除外", "何者為非"]:
                    if neg_word in src_text:
                        is_negative_q = True
                        break
            
            if errors:
                failed_questions[q_num] = errors
            else:
                passed_count += 1
                
            if q_num in target_questions:
                target_results[q_num] = {
                    "errors": errors,
                    "is_negative": is_negative_q,
                    "explanation": exp,
                    "key_point": kp,
                    "flashcard_summary": fs,
                    "flashcard_back": fb,
                    "question_text": src_text
                }

    print(f"--- 統計結果 ---")
    print(f"總檢查題數: {total_count}")
    print(f"通過題數: {passed_count}")
    print(f"不通過題數: {len(failed_questions)}")
    print(f"未通過題號: {sorted(list(failed_questions.keys()))}")
    
    # 寫入詳細報告
    detailed_report = {
        "total_checked": total_count,
        "passed_count": passed_count,
        "failed_questions": failed_questions,
        "target_results": target_results
    }
    
    with open(r"d:\Antigravity\med_exam_public\scratch\audit_medicine_4_all_report.json", "w", encoding="utf-8") as f:
        json.dump(detailed_report, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    audit_all()
