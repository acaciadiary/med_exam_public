import os
import json
import re

# 定義路徑
REWRITE_DIR = "d:/Antigravity/med_exam_public/scratch/rewrite_updates/109-1_medicine-1"
SOURCE_EXAM_PATH = "d:/Antigravity/med_exam_public/public/data/exams/109-1/medicine-1.json"

# 載入來源考卷
with open(SOURCE_EXAM_PATH, "r", encoding="utf-8") as f:
    source_data = json.load(f)

# 整理來源考卷題目
source_questions = {}
if isinstance(source_data, list):
    for q in source_data:
        source_questions[q["question_number"]] = q
elif isinstance(source_data, dict):
    # 若是字典，看看 questions 欄位
    q_list = source_data.get("questions", [])
    for q in q_list:
        source_questions[q["question_number"]] = q

# 禁用模板詞/低品質句清單
BANNED_PHRASES = [
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
    "熟悉疾病機轉",
    "臨床表現、診斷檢查與治療原則"
]

# 檢查檔案
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

all_updates = []
errors = []
warnings = []
passed_questions = []
needs_rework = {}  # question_number -> reason
manual_review_needed = []

allowed_file_fields = {"source_file", "dataset_id", "range", "updates"}
allowed_update_fields = {
    "question_id", "question_number", "explanation", "key_point",
    "flashcard_front", "flashcard_back", "flashcard_summary",
    "review_status", "explanation_model", "explanation_generated_at",
    "manual_review_notes"
}

total_audited = 0

for file_name in files_to_review:
    file_path = os.path.join(REWRITE_DIR, file_name)
    if not os.path.exists(file_path):
        errors.append(f"檔案不存在: {file_path}")
        continue
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        errors.append(f"無法解析 JSON: {file_name}, 錯誤: {str(e)}")
        continue
    
    # 檢查外層欄位
    extra_file_fields = set(data.keys()) - allowed_file_fields
    if extra_file_fields:
        errors.append(f"檔案 {file_name} 包含不允許的外層欄位: {extra_file_fields}")
    
    updates = data.get("updates", [])
    for upd in updates:
        total_audited += 1
        q_num = upd.get("question_number")
        q_id = upd.get("question_id")
        
        rework_reasons = []
        
        # 檢查更新欄位
        extra_upd_fields = set(upd.keys()) - allowed_update_fields
        if extra_upd_fields:
            rework_reasons.append(f"包含不允許的題目更新欄位: {extra_upd_fields}")
            
        # 對照來源題目
        src_q = source_questions.get(q_num)
        if not src_q:
            rework_reasons.append(f"來源考卷找不到題號 {q_num}")
        else:
            if src_q.get("id") != q_id:
                rework_reasons.append(f"Question ID 不匹配。來源: {src_q.get('id')}, 更新: {q_id}")
                
        # 1. 檢查結構：每題是否都有【題幹解析】【選項詳解】【核心考點】
        explanation = upd.get("explanation", "")
        if "【題幹解析】" not in explanation:
            rework_reasons.append("缺少【題幹解析】")
        if "【選項詳解】" not in explanation:
            rework_reasons.append("缺少【選項詳解】")
        if "【核心考點】" not in explanation:
            rework_reasons.append("缺少【核心考點】")
            
        # 2. 選項 A-D 詳解與具體理由
        opt_det = ["- A.", "- B.", "- C.", "- D."]
        for opt in opt_det:
            if opt not in explanation:
                rework_reasons.append(f"選項詳解缺少選項 {opt.replace('-', '').strip()} 的解釋")
        
        # 檢查是否 A-D 共用同一段話，或者內容過於簡短
        # 我們可以用簡單的長度檢查或重複檢查
        # 尋找選項段落
        opt_texts = []
        for i in range(len(opt_det)):
            opt = opt_det[i]
            start_idx = explanation.find(opt)
            if start_idx != -1:
                # 找到下一個選項或【核心考點】的位置作為終點
                next_indices = []
                for next_opt in opt_det[i+1:]:
                    idx = explanation.find(next_opt, start_idx)
                    if idx != -1:
                        next_indices.append(idx)
                idx_kp = explanation.find("【核心考點】", start_idx)
                if idx_kp != -1:
                    next_indices.append(idx_kp)
                
                end_idx = min(next_indices) if next_indices else len(explanation)
                opt_content = explanation[start_idx:end_idx].strip()
                opt_texts.append(opt_content)
                
                # 檢查選項內是否包含醫學理由，或者是複製貼上
                # 若選項解釋長度太短
                if len(opt_content) < 15:
                    rework_reasons.append(f"選項 {opt.replace('-', '').strip()} 的解釋太短 ({len(opt_content)}字): '{opt_content}'")
        
        # 檢查選項是否重複
        if len(opt_texts) == 4:
            # 移除選項標記後比較內容
            clean_opts = [re.sub(r'^-\s*[A-D]\.\s*', '', o).strip() for o in opt_texts]
            if len(set(clean_opts)) < 4:
                rework_reasons.append("選項詳解存在重複的解釋內容 (可能複製貼上)")
                
        # 3. & 4. 禁用模板詞與低品質句
        found_banned = []
        for phrase in BANNED_PHRASES:
            if phrase in explanation:
                found_banned.append(phrase)
        if found_banned:
            rework_reasons.append(f"包含禁用或低品質模板句: {found_banned}")
            
        # 5. key_point, flashcard_summary, flashcard_back 是否具體可用
        kp = upd.get("key_point", "")
        fc_sum = upd.get("flashcard_summary", "")
        fc_back = upd.get("flashcard_back", "")
        
        if len(kp.strip()) < 5:
            rework_reasons.append(f"key_point 太短或空泛: '{kp}'")
        if len(fc_sum.strip()) < 5:
            rework_reasons.append(f"flashcard_summary 太短或空泛: '{fc_sum}'")
        if len(fc_back.strip()) < 5:
            rework_reasons.append(f"flashcard_back 太短或空泛: '{fc_back}'")
            
        # 檢查 key_point / flashcard 是否含有空話
        for phrase in ["熟悉", "掌握", "診斷檢查與治療原則", "疾病機轉"]:
            if phrase in kp and len(kp) < 20:
                rework_reasons.append(f"key_point 含有空泛的詞彙: '{kp}'")
                
        # 6. 官方答案疑義 / 需人工複核
        manual_notes = upd.get("manual_review_notes", [])
        if manual_notes:
            manual_review_needed.append((q_num, f"manual_review_notes: {manual_notes}"))
        
        # 在 explanation 中找關鍵字
        review_keywords = ["答案有誤", "官方答案", "疑義", "人工複核", "爭議", "答案給錯", "更正答案"]
        for kw in review_keywords:
            if kw in explanation and q_num not in [m[0] for m in manual_review_needed]:
                manual_review_needed.append((q_num, f"詳解中提及關鍵字 '{kw}'"))
                break
                
        if rework_reasons:
            needs_rework[q_num] = "; ".join(rework_reasons)
        else:
            passed_questions.append(q_num)

# 將結果寫入檔案以避免控制台亂碼
output_path = "d:/Antigravity/med_exam_public/scratch/audit_report.txt"
with open(output_path, "w", encoding="utf-8") as out:
    def write_line(text):
        out.write(text + "\n")
        print(text)

    write_line(f"=== 審查結果 ===")
    write_line(f"審查範圍: 109-1/medicine-1.json (第 1 - 80 題)")
    write_line(f"總審查題數: {total_audited}")
    write_line(f"通過題數: {len(passed_questions)}")
    write_line(f"返工題數: {len(needs_rework)}")
    write_line(f"可合併的 update 檔:")
    if len(needs_rework) == 0:
        write_line("  - 全部 8 個檔案均無返工題，皆可合併！")
    else:
        # 找出沒有任何返工題目的檔案
        for file_name in files_to_review:
            file_path = os.path.join(REWRITE_DIR, file_name)
            if not os.path.exists(file_path):
                continue
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                upds = data.get("updates", [])
                has_rework = False
                for upd in upds:
                    if upd.get("question_number") in needs_rework:
                        has_rework = True
                        break
                if not has_rework:
                    write_line(f"  - {file_name} (通過)")
                else:
                    write_line(f"  - {file_name} (有返工題，暫不可合併)")
            except:
                pass

    write_line(f"\n=== 需要返工題號清單 ===")
    for q_num in sorted(needs_rework.keys()):
        write_line(f"第 {q_num} 題: {needs_rework[q_num]}")

    write_line(f"\n=== 疑似需人工複核題號 ===")
    for q_num, reason in sorted(manual_review_needed, key=lambda x: x[0]):
        write_line(f"第 {q_num} 題: {reason}")

    write_line(f"\n=== 錯誤資訊 ===")
    for err in errors:
        write_line(err)

