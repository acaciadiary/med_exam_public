import os
import json
import re

REWRITE_DIR = "d:/Antigravity/med_exam_public/scratch/rewrite_updates/109-1_medicine-1"
SOURCE_EXAM_PATH = "d:/Antigravity/med_exam_public/public/data/exams/109-1/medicine-1.json"

with open(SOURCE_EXAM_PATH, "r", encoding="utf-8") as f:
    source_data = json.load(f)

source_questions = {}
if isinstance(source_data, list):
    for q in source_data:
        source_questions[q["question_number"]] = q
elif isinstance(source_data, dict):
    q_list = source_data.get("questions", [])
    for q in q_list:
        source_questions[q["question_number"]] = q

files_to_review = [
    "q001-q010.json",
    "q011-q020.json",
    "q021-q030.json",
    "q031-q040.json",
    "q041-q050.json",
    "q051-q060.json",
    "q061-q070.json",
    "q071-q080.json"
]

# regex 禁用模式
BANNED_PATTERNS = [
    r"非本題答案",
    r"不是本題.*答案",
    r"回到題幹.*線索",
    r"請用題幹.*連回",
    r"選項\s*[A-D]\s*所代表的",
    r"不能最.*回答本題",
    r"最符合題幹",
    r"核心記憶點",
    r"定義、機轉、典型表現或處置原則",
    r"此選項不是.*答案",
    r"與正確答案的.*不一致",
    r"原始解析.*指出",
    r"作答時應回到.*線索",
    r"熟悉.*機轉",
    r"臨床表現、診斷檢查與治療原則"
]

report_lines = []
rework_questions = {}
manual_reviews = []
total_questions = 0

for file_name in files_to_review:
    file_path = os.path.join(REWRITE_DIR, file_name)
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    updates = data.get("updates", [])
    for upd in updates:
        total_questions += 1
        q_num = upd.get("question_number")
        q_id = upd.get("question_id")
        explanation = upd.get("explanation", "")
        kp = upd.get("key_point", "")
        fc_front = upd.get("flashcard_front", "")
        fc_back = upd.get("flashcard_back", "")
        fc_sum = upd.get("flashcard_summary", "")
        notes = upd.get("manual_review_notes", [])
        
        rework_reasons = []
        
        # 1. 檢查關鍵欄位格式與值
        if upd.get("review_status") != "ai_generated":
            rework_reasons.append(f"review_status 應為 'ai_generated'，但為 '{upd.get('review_status')}'")
        if upd.get("explanation_model") != "codex-high-quality-rewrite":
            rework_reasons.append(f"explanation_model 應為 'codex-high-quality-rewrite'，但為 '{upd.get('explanation_model')}'")
            
        # 2. 檢查三大標題
        for tag in ["【題幹解析】", "【選項詳解】", "【核心考點】"]:
            if tag not in explanation:
                rework_reasons.append(f"缺少 {tag}")
                
        # 3. 檢查 A-D 是否都有
        for letter in ["A", "B", "C", "D"]:
            if f"- {letter}." not in explanation:
                rework_reasons.append(f"缺少 - {letter}. 的選項說明")
                
        # 4. 檢查禁用詞的 regex 匹配
        for pattern in BANNED_PATTERNS:
            match = re.search(pattern, explanation)
            if match:
                rework_reasons.append(f"explanation 含有禁用模板模式 '{pattern}' (匹配到: '{match.group(0)}')")
            if re.search(pattern, kp):
                rework_reasons.append(f"key_point 含有禁用模板模式 '{pattern}'")
            if re.search(pattern, fc_back):
                rework_reasons.append(f"flashcard_back 含有禁用模板模式 '{pattern}'")
                
        # 5. 檢查 key_point / flashcards 的具體性
        # 如果 key_point 含有 "本題"、"選項"、"正確答案"、"考查" 等字眼，可能是不夠具體，因為 core point 應該是可複用的醫學規則
        if any(w in kp for w in ["本題在於", "選項A", "選項B", "選項C", "選項D", "此題考"]):
            rework_reasons.append(f"key_point 含有不具體、非複用性醫學規則的字眼: '{kp}'")
            
        if len(kp.strip()) < 10:
            rework_reasons.append(f"key_point 過短 ({len(kp)}字): '{kp}'")
        if len(fc_front.strip()) < 8:
            rework_reasons.append(f"flashcard_front 過短 ({len(fc_front)}字): '{fc_front}'")
        if len(fc_back.strip()) < 10:
            rework_reasons.append(f"flashcard_back 過短 ({len(fc_back)}字): '{fc_back}'")
        if len(fc_sum.strip()) < 10:
            rework_reasons.append(f"flashcard_summary 過短 ({len(fc_sum)}字): '{fc_sum}'")
            
        # 6. 官方答案疑義 / 人工複核
        if notes:
            manual_reviews.append((q_num, f"manual_review_notes 註記: {notes}"))
        else:
            # 檢查 explanation 內是否提到答案疑義
            if any(w in explanation for w in ["答案有誤", "答案疑義", "官方答案有問題", "更正答案", "皆正確", "皆給分"]):
                manual_reviews.append((q_num, f"詳解文字疑似提及官方答案疑義"))
                
        if rework_reasons:
            rework_questions[q_num] = rework_reasons

# 將結果寫入檔案以避免控制台亂碼
report_path = "d:/Antigravity/med_exam_public/scratch/audit_report_details.txt"
with open(report_path, "w", encoding="utf-8") as out:
    def write_line(text):
        out.write(text + "\n")

        
    write_line("========================================")
    write_line("     醫學考卷詳解 updates 詳細審查報告")
    write_line("========================================")
    write_line(f"審查範圍: 109-1_medicine-1 考卷，共 8 個 update JSON 檔案。")
    write_line(f"來源考卷檔: {SOURCE_EXAM_PATH}")
    write_line(f"總審查題數: {total_questions} 題")
    write_line(f"通過題數: {total_questions - len(rework_questions)} 題")
    write_line(f"需要返工題數: {len(rework_questions)} 題")
    
    write_line("\n--- 可合併的 update 檔清單 ---")
    # 對於這 8 個檔案，看哪些是完全無返工題目的
    for file_name in files_to_review:
        file_path = os.path.join(REWRITE_DIR, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        upds = data.get("updates", [])
        file_reworks = [u.get("question_number") for u in upds if u.get("question_number") in rework_questions]
        if not file_reworks:
            write_line(f"✔ {file_name} : 完全通過，可立即合併")
        else:
            write_line(f"❌ {file_name} : 含有需要返工的題目 ({file_reworks})，暫不可合併")
            
    write_line("\n--- 需要返工的題目詳情 ---")
    if not rework_questions:
        write_line("無。所有題目皆符合品質要求。")
    else:
        for q_num, reasons in sorted(rework_questions.items()):
            write_line(f"\n第 {q_num} 題:")
            for r in reasons:
                write_line(f"  - 原因: {r}")
                
    write_line("\n--- 疑似需人工複核題號 (醫學內容/官方答案疑義) ---")
    if not manual_reviews:
        write_line("無。")
    else:
        for q_num, desc in sorted(manual_reviews, key=lambda x: x[0]):
            write_line(f"第 {q_num} 題: {desc}")
            
    write_line("\n--- 結論與建議 ---")
    if len(rework_questions) > 0:
        write_line("建議暫停下一波寫作，先完成返工題目的修正與覆核。")
    else:
        write_line("全部題目皆通過品質審查。建議可以合併，並可以繼續下一波寫作。")
    write_line("========================================")
