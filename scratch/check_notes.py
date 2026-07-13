import json
import os

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

def check_counts_and_notes():
    total_q = 0
    all_notes = []
    
    for file_name in update_files:
        file_path = os.path.join(updates_dir, file_name)
        if not os.path.exists(file_path):
            print(f"File not found: {file_name}")
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        updates = data.get("updates", [])
        q_count = len(updates)
        total_q += q_count
        print(f"File {file_name}: {q_count} questions (Range: {data.get('range')})")
        
        for up in updates:
            q_num = up.get("question_number")
            mrn = up.get("manual_review_notes", [])
            if mrn:
                all_notes.append((q_num, file_name, mrn))
                
            # 同時也搜一下有沒有「爭議」或「疑慮」等詞
            exp = up.get("explanation", "")
            for keyword in ["爭議", "疑慮", "有誤", "錯誤", "勘誤", "疑義"]:
                # 排除 A-D 的「錯誤」兩個字，我們只搜「答案有誤」或「答案錯誤」或「官方」或「疑義」或「爭議」
                if keyword in exp:
                    # 如果只是單純「錯誤。」，這是選項詳解的開頭，要排除
                    # 我們可以排除 "- X. 錯誤。"
                    clean_exp = exp
                    for opt in ["A", "B", "C", "D"]:
                        clean_exp = clean_exp.replace(f"- {opt}. 錯誤", "")
                    if keyword in clean_exp:
                        print(f"Found keyword '{keyword}' in Q{q_num} ({file_name})")

    print(f"Total questions in updates: {total_q}")
    print(f"Total manual_review_notes found: {len(all_notes)}")
    for q_num, f_name, mrn in all_notes:
        print(f"Q{q_num} in {f_name}: {mrn}")

if __name__ == "__main__":
    check_counts_and_notes()
