import json
import re
import subprocess
import sys
import io

# 強制輸出為 UTF-8 避免亂碼
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def get_original_json(filepath):
    try:
        # Run git show HEAD:<filepath>
        # We need to use forward slashes for git on Windows
        git_path = filepath.replace("\\", "/")
        cmd = ["git", "show", f"HEAD:{git_path}"]
        result = subprocess.run(cmd, text=True, capture_output=True, encoding="utf-8")
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            # Try origin/main
            cmd = ["git", "show", f"origin/main:{git_path}"]
            result = subprocess.run(cmd, text=True, capture_output=True, encoding="utf-8")
            if result.returncode == 0:
                return json.loads(result.stdout)
    except Exception as e:
        print(f"Error getting original json via git: {e}")
    return None

def audit():
    filepath = "public/data/exams/110-2/medicine-2.json"
    
    with open(filepath, "r", encoding="utf-8") as f:
        new_data = json.load(f)
        
    old_data = get_original_json(filepath)
    if old_data is None:
        print("Warning: Could not load original JSON from git. Will skip structural comparison, but continue with quality checks.")
    else:
        print("Successfully loaded original JSON from git for structural comparison.")
    
    questions = new_data.get("questions", [])
    total_questions = len(questions)
    
    # 禁用模板句
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
    ]
    
    # regex for "選項 A 所代表的..."
    option_represent_re = re.compile(r"選項\s*[A-D]\s*所代表的")
    
    passed_count = 0
    rework_list = []      # list of dict: {qnum, reason}
    review_needed = []    # list of dict: {qnum, reason}
    
    for q in questions:
        qnum = q.get("question_number")
        qid = q.get("id")
        
        # 1. 結構完整性檢查
        explanation = q.get("explanation", "")
        key_point = q.get("key_point", "")
        flashcard_summary = q.get("flashcard_summary", "")
        flashcard_back = q.get("flashcard_back", "")
        flashcard_front = q.get("flashcard_front", "")
        
        reasons = []
        
        # 檢查標題
        has_analysis = "【題幹解析】" in explanation
        has_options = "【選項詳解】" in explanation
        has_keypoint = "【核心考點】" in explanation
        
        if not (has_analysis and has_options and has_keypoint):
            missing = []
            if not has_analysis: missing.append("【題幹解析】")
            if not has_options: missing.append("【選項詳解】")
            if not has_keypoint: missing.append("【核心考點】")
            reasons.append(f"缺少標題: {', '.join(missing)}")
            
        # 2. 禁用詞檢查
        found_banned = []
        for p in banned_phrases:
            if p in explanation:
                found_banned.append(f"「{p}」")
        if option_represent_re.search(explanation):
            found_banned.append("「選項 X 所代表的...」")
            
        if found_banned:
            reasons.append(f"包含禁用模板句: {', '.join(found_banned)}")
            
        # 3. 選項詳解 A-D 檢查
        # 提取選項詳解部分的文字
        opt_details = {}
        if has_options:
            parts = explanation.split("【選項詳解】")
            if len(parts) > 1:
                opt_part = parts[1].split("【核心考點】")[0].strip()
                
                # 匹配 - A. 或 - (A) 等
                opt_matches = list(re.finditer(r"-\s*([A-D])\.", opt_part))
                if len(opt_matches) < 4:
                    opt_matches = list(re.finditer(r"-\s*\(([A-D])\)", opt_part))
                
                if len(opt_matches) < 4:
                    reasons.append(f"選項詳解格式不符或未完整列出 A-D 選項 (找到 {len(opt_matches)} 個)")
                else:
                    for i in range(len(opt_matches)):
                        start = opt_matches[i].end()
                        end = opt_matches[i+1].start() if i+1 < len(opt_matches) else len(opt_part)
                        opt_char = opt_matches[i].group(1)
                        opt_text = opt_part[start:end].strip()
                        opt_details[opt_char] = opt_text
                        
                    # 檢查是否過短或重複
                    for char, txt in opt_details.items():
                        clean_txt = re.sub(r"[^\w]", "", txt)
                        if len(clean_txt) < 8:
                            reasons.append(f"選項 {char} 說明過於簡短或無實質內容 (僅 {len(clean_txt)} 字)")
                    
                    # 檢查重複
                    checked_pairs = []
                    for c1 in opt_details:
                        for c2 in opt_details:
                            if c1 != c2 and (c2, c1) not in checked_pairs:
                                checked_pairs.append((c1, c2))
                                t1 = opt_details[c1]
                                t2 = opt_details[c2]
                                if t1 == t2 and len(t1) > 0:
                                    reasons.append(f"選項 {c1} 與選項 {c2} 的解析內容完全相同")
            else:
                reasons.append("無法解析選項詳解區塊")
                
        # 4. key_point, flashcard_summary, flashcard_back 等欄位檢查
        if not key_point or len(key_point.strip()) < 5:
            reasons.append(f"key_point 過短或為空 (當前: '{key_point}')")
        if not flashcard_summary or len(flashcard_summary.strip()) < 5:
            reasons.append(f"flashcard_summary 過短或為空 (當前: '{flashcard_summary}')")
        if not flashcard_back or len(flashcard_back.strip()) < 5:
            reasons.append(f"flashcard_back 過短或為空 (當前: '{flashcard_back}')")
            
        # 檢查 key_point / flashcards 裡是否有禁用詞
        for p in banned_phrases:
            if p in key_point or p in flashcard_summary or p in flashcard_back:
                reasons.append(f"學習欄位包含禁用詞「{p}」")

        # 5. 檢查是否有非允許的欄位被修改
        if old_data:
            old_q = None
            for oq in old_data.get("questions", []):
                if oq.get("id") == qid or oq.get("question_number") == qnum:
                    old_q = oq
                    break
            
            if old_q:
                # 比較題目文字、選項文字、答案、ID等是否保持原本的樣子
                if q.get("question_text") != old_q.get("question_text"):
                    reasons.append("題目文字被修改")
                # options 可能是 list of dict 或 dict，這裡作直接比對
                if q.get("options") != old_q.get("options"):
                    reasons.append("選項文字被修改")
                if q.get("correct_answer") != old_q.get("correct_answer"):
                    reasons.append("單選答案被修改")
                if q.get("correct_answers") != old_q.get("correct_answers"):
                    reasons.append("複選答案被修改")
                if q.get("id") != old_q.get("id"):
                    reasons.append("ID被修改")
            else:
                reasons.append("在原始資料中找不到對應的題號/ID")

        # 6. 醫學疑義或官方答案疑義 (標記為人工複核)
        review_reasons = []
        notes = q.get("manual_review_notes", [])
        if notes:
            review_reasons.append(f"manual_review_notes: {', '.join(notes)}")
            
        # 檢查是否在 explanation 中有明確的疑義字眼
        for keyword in ["官方答案", "答案有誤", "人工複核", "爭議", "答案疑義"]:
            if keyword in explanation and keyword not in [r.split(":")[0] for r in review_reasons]:
                pos = explanation.find(keyword)
                context = explanation[max(0, pos-20):min(len(explanation), pos+30)]
                review_reasons.append(f"解析中提及 {keyword}: ...{context}...")
                
        if review_reasons:
            review_needed.append({
                "question_number": qnum,
                "reasons": review_reasons
            })

        # 彙整結果
        if reasons:
            rework_list.append({
                "question_number": qnum,
                "reasons": reasons
            })
        else:
            passed_count += 1

    # 輸出結果
    print("=== 審查結果 ===")
    print(f"1. 審查範圍與題數: 第 1 - 100 題，共 {total_questions} 題")
    print(f"2. 通過題數: {passed_count} 題")
    
    print("\n3. 需要返工題號清單:")
    if not rework_list:
        print("無，全數通過")
    else:
        for item in rework_list:
            print(f"- 第 {item['question_number']} 題: {'; '.join(item['reasons'])}")
            
    print("\n4. 疑似需人工複核題號與原因:")
    if not review_needed:
        print("無")
    else:
        for item in review_needed:
            print(f"- 第 {item['question_number']} 題: {'; '.join(item['reasons'])}")
            
    # 結論
    print("\n5. 最終審查結論:")
    if rework_list:
        print("【建議暫停】有部分題目未通過審查，需要返工修改。")
    else:
        print("【可以通過】全數通過審查，沒有需要返工的題目。")

if __name__ == "__main__":
    audit()
