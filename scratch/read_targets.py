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

target_questions = [16, 37, 39, 41, 44, 51, 52, 54, 57, 58, 66, 75, 78, 79]
output_path = r"d:\Antigravity\med_exam_public\scratch\targets_output.txt"

def read_targets():
    with open(output_path, "w", encoding="utf-8") as out:
        for file_name in update_files:
            file_path = os.path.join(updates_dir, file_name)
            if not os.path.exists(file_path):
                continue
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            for up in data.get("updates", []):
                q_num = up.get("question_number")
                if q_num in target_questions or up.get("manual_review_notes"):
                    out.write(f"==================================================\n")
                    out.write(f"檔案: {file_name} | 題號: {q_num}\n")
                    out.write(f"ID: {up.get('question_id')}\n")
                    out.write(f"Manual Review Notes: {up.get('manual_review_notes')}\n")
                    
                    # 搜尋可能跟疑義、官方、有誤、錯誤、勘誤、爭議相關的句子
                    exp = up.get("explanation", "")
                    out.write(f"--- 詳解內容 ---\n")
                    out.write(exp + "\n")
                    out.write(f"==================================================\n\n")

if __name__ == "__main__":
    read_targets()
