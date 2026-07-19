import json
import os

target_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\109-2_medicine-4"
output_md = r"d:\Antigravity\med_exam_public\scratch\failed_questions_view.md"
report_path = r"d:\Antigravity\med_exam_public\scratch\audit_109_2_medicine_4_report.json"

with open(report_path, "r", encoding="utf-8") as f:
    report = json.load(f)

failed_errors = report.get("failed", {})
failed_nums = [int(k) for k in failed_errors.keys()]

# 收集這些題目的詳細內容
question_details = {}

for file_name in os.listdir(target_dir):
    if not file_name.endswith(".json"):
        continue
    file_path = os.path.join(target_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for up in data.get("updates", []):
            q_num = up.get("question_number")
            if q_num in failed_nums:
                question_details[q_num] = {
                    "explanation": up.get("explanation"),
                    "errors": failed_errors[str(q_num)],
                    "key_point": up.get("key_point"),
                    "flashcard_summary": up.get("flashcard_summary"),
                    "flashcard_back": up.get("flashcard_back")
                }

with open(output_md, "w", encoding="utf-8") as out:
    out.write("# 自動審查未通過題目之詳情\n\n")
    for q_num in sorted(failed_nums):
        details = question_details[q_num]
        out.write(f"## Q{q_num:03d}\n")
        out.write(f"- **自動審查檢出問題**: {details['errors']}\n\n")
        out.write("### 詳解內容\n")
        out.write("```markdown\n")
        out.write(details['explanation'])
        out.write("\n```\n\n")
        out.write(f"- **key_point**: {details['key_point']}\n")
        out.write(f"- **flashcard_summary**: {details['flashcard_summary']}\n")
        out.write(f"- **flashcard_back**: {details['flashcard_back']}\n")
        out.write("\n" + "="*50 + "\n\n")

print(f"Extracted failed questions to {output_md}")
