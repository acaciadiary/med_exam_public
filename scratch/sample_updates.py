import json
import os
import sys

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

output_path = r"d:\Antigravity\med_exam_public\scratch\sample_output.txt"

def sample():
    with open(output_path, "w", encoding="utf-8") as out:
        for file_name in update_files:
            file_path = os.path.join(updates_dir, file_name)
            if not os.path.exists(file_path):
                continue
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            updates = data.get("updates", [])
            if updates:
                # 抽樣第一題
                first_q = updates[0]
                out.write(f"==================================================\n")
                out.write(f"檔案: {file_name} | 題號: {first_q.get('question_number')}\n")
                out.write(f"ID: {first_q.get('question_id')}\n")
                out.write(f"--- 詳解 ---\n")
                out.write(str(first_q.get("explanation")) + "\n")
                out.write(f"--- Key Point ---\n")
                out.write(str(first_q.get("key_point")) + "\n")
                out.write(f"--- Flashcard Summary ---\n")
                out.write(str(first_q.get("flashcard_summary")) + "\n")
                out.write(f"--- Flashcard Back ---\n")
                out.write(str(first_q.get("flashcard_back")) + "\n")
                out.write(f"--- Manual Review Notes ---\n")
                out.write(str(first_q.get("manual_review_notes")) + "\n")
                out.write(f"==================================================\n\n")
    print(f"Sample output written to {output_path}")

if __name__ == "__main__":
    sample()
