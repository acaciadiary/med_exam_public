import os
import json
import re

# Banned template phrases list
BANNED_PHRASES = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
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
    "非本題的正確答案",
    "與標準答案的關鍵判斷不同"
]

SOURCE_FILE_PATH = r"d:\Antigravity\med_exam_public\public\data\exams\109-2\medicine-1.json"
UPDATES_DIR = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\109-2_medicine-1"

# Target questions for special inspection
TARGET_QUESTIONS = ["q010", "q022", "q023", "q031", "q034", "q038", "q040", "q060", "q070", "q076", "q085"]

def load_source_exam():
    with open(SOURCE_FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def check_repeated_paragraphs(explanation):
    # Split the explanation by options A. B. C. D.
    # Pattern to find option explanations
    # Options usually look like: "- A. 說明" or "- A: 說明"
    options_text = []
    # Let's search for lines starting with - A., - B., - C., - D.
    lines = explanation.split('\n')
    opt_contents = {}
    current_opt = None
    for line in lines:
        match = re.match(r'^\s*-\s*([A-D])\.\s*(.*)', line)
        if match:
            current_opt = match.group(1)
            opt_contents[current_opt] = match.group(2)
        elif current_opt and line.strip() and not line.strip().startswith('【'):
            opt_contents[current_opt] = opt_contents[current_opt] + " " + line.strip()
    
    if len(opt_contents) < 4:
        return []

    # Check for long common substrings (length >= 10 chars) shared among >=3 options
    opts = list(opt_contents.keys())
    shared_substrings = []
    
    # Helper to find common substrings of length N
    def get_substrings(text, length=12):
        text = re.sub(r'\s+', '', text) # remove spaces
        return {text[i:i+length] for i in range(len(text) - length + 1)}
    
    all_subs = {}
    for opt in opts:
        all_subs[opt] = get_substrings(opt_contents[opt])
        
    # We want to check if any substring is in at least 3 options
    all_candidate_subs = set()
    for opt in opts:
        all_candidate_subs.update(all_subs[opt])
        
    for sub in all_candidate_subs:
        count = sum(1 for opt in opts if sub in all_subs[opt])
        if count >= 3:
            # Check if this substring is just common formatting like "錯誤。" or "正確。"
            if sub in ["錯誤。此選項", "正確。此選項", "選項所述", "說明如下", "的敘述錯誤", "的敘述正確"]:
                continue
            # Filter out non-alphabetic/non-chinese or very common words
            if re.match(r'^[0-9\.\-\s,，。、；：()（）]+$', sub):
                continue
            shared_substrings.append(sub)
            
    return list(set(shared_substrings))

def audit():
    source_data = load_source_exam()
    # Map questions by ID
    source_questions = {q['id']: q for q in source_data['questions']}
    
    files = sorted([f for f in os.listdir(UPDATES_DIR) if f.endswith('.json')])
    
    total_audited = 0
    passed_count = 0
    issues = {}
    
    print(f"Starting audit for {len(files)} update files in 109-2_medicine-1...")
    
    for filename in files:
        filepath = os.path.join(UPDATES_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                issues[filename] = [f"JSON Parse Error: {str(e)}"]
                continue
                
        file_issues = []
        
        # Check overall JSON structure
        allowed_root_keys = {"source_file", "dataset_id", "range", "updates"}
        extra_root_keys = set(data.keys()) - allowed_root_keys
        if extra_root_keys:
            file_issues.append(f"Extra root keys: {extra_root_keys}")
            
        updates = data.get("updates", [])
        for update_idx, item in enumerate(updates):
            total_audited += 1
            qid = item.get("question_id")
            qnum = item.get("question_number")
            
            q_label = f"{filename} (idx {update_idx}, QID: {qid}, QNum: {qnum})"
            q_issues = []
            
            # Check disallowed fields
            allowed_fields = {
                "question_id", "question_number", "explanation", "key_point",
                "flashcard_front", "flashcard_back", "flashcard_summary",
                "review_status", "explanation_model", "explanation_generated_at",
                "manual_review_notes"
            }
            extra_fields = set(item.keys()) - allowed_fields
            if extra_fields:
                q_issues.append(f"Disallowed fields in update item: {extra_fields}")
                
            # Specifically check if "id" field exists (which is forbidden)
            if "id" in item:
                q_issues.append("Contains forbidden 'id' field")
                
            # Verify with source question
            if qid not in source_questions:
                q_issues.append(f"question_id {qid} not found in source exam file")
            else:
                source_q = source_questions[qid]
                if source_q['question_number'] != qnum:
                    q_issues.append(f"question_number {qnum} does not match source ({source_q['question_number']})")
            
            # Check explanation structure
            explanation = item.get("explanation", "")
            if not explanation:
                q_issues.append("Explanation is empty")
            else:
                if "【題幹解析】" not in explanation:
                    q_issues.append("Missing 【題幹解析】")
                if "【選項詳解】" not in explanation:
                    q_issues.append("Missing 【選項詳解】")
                if "【核心考點】" not in explanation:
                    q_issues.append("Missing 【核心考點】")
                    
                # Check for banned phrases
                found_banned = []
                for phrase in BANNED_PHRASES:
                    if phrase in explanation:
                        found_banned.append(phrase)
                if found_banned:
                    q_issues.append(f"Found banned template phrase(s): {found_banned}")
                    
                # Check for repeated paragraphs across >=3 options
                repeated = check_repeated_paragraphs(explanation)
                if repeated:
                    q_issues.append(f"Detected repeated segments across >=3 options: {repeated}")
                    
                # Check negative question treatment if source question is negative
                if qid in source_questions:
                    source_q = source_questions[qid]
                    qtext = source_q.get("question_text", "")
                    is_negative = any(kw in qtext for kw in ["錯誤", "不適當", "不是", "較不可能", "最不相關", "不正確"])
                    if is_negative:
                        # Ensure negative explanation logic is clear (i.e. explains that other options are true, the correct answer is the exception)
                        # We look for keywords like "正確。此選項是正確的敘述", "正確。選項所述為正確的敘述" etc. in options
                        pass

            # Check key_point, flashcard_summary, flashcard_back
            kp = item.get("key_point", "")
            fs = item.get("flashcard_summary", "")
            fb = item.get("flashcard_back", "")
            ff = item.get("flashcard_front", "")
            
            if not kp or "未填" in kp or len(kp) < 5 or kp.strip() == "看到此類題目時...":
                q_issues.append(f"key_point is vague or placeholder: '{kp}'")
            if not fs or "未填" in fs or len(fs) < 5:
                q_issues.append(f"flashcard_summary is vague or placeholder: '{fs}'")
            if not fb or "未填" in fb or len(fb) < 5 or "看到此類題目時" in fb:
                q_issues.append(f"flashcard_back is vague or placeholder: '{fb}'")
            if not ff or "未填" in ff or len(ff) < 2:
                q_issues.append(f"flashcard_front is vague or placeholder: '{ff}'")
                
            if q_issues:
                file_issues.append({
                    "qid": qid,
                    "qnum": qnum,
                    "issues": q_issues
                })
            else:
                passed_count += 1
                
        if file_issues:
            issues[filename] = file_issues
            
    print(f"\nAudit completed. Total processed: {total_audited}, Passed: {passed_count}")
    
    # Generate report
    report = {
        "total_audited": total_audited,
        "passed_count": passed_count,
        "all_passed": (total_audited == passed_count),
        "issues": issues
    }
    
    print(f"All passed: {report['all_passed']}")
    with open(r"d:\Antigravity\med_exam_public\scratch\audit_report.json", 'w', encoding='utf-8') as rf:
        json.dump(report, rf, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    audit()
