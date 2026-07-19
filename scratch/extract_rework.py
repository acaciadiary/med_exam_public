import json
import os

report_path = r"d:\Antigravity\med_exam_public\scratch\audit_109_2_medicine_4_report.json"
output_md = r"d:\Antigravity\med_exam_public\scratch\rework_questions_view.md"

with open(report_path, "r", encoding="utf-8") as f:
    report = json.load(f)

rework_details = report.get("rework_details", {})

with open(output_md, "w", encoding="utf-8") as out:
    out.write("# 8題返工對象之審查詳情\n\n")
    for q_num_str, details in sorted(rework_details.items(), key=lambda x: int(x[0])):
        q_num = int(q_num_str)
        out.write(f"## Q{q_num:03d}\n")
        out.write(f"- **是否為否定問法**: {'是' if details['is_negative'] else '否'}\n")
        out.write(f"- **自動審查錯誤**: {details['errors']}\n")
        out.write(f"- **標準答案**: {details['answer']}\n")
        out.write(f"- **題幹字串**: {details['question_text'][:200]}\n\n")
        out.write("### 詳解內容\n")
        out.write("```markdown\n")
        out.write(details['explanation'])
        out.write("\n```\n\n")
        out.write(f"- **key_point**: {details['key_point']}\n")
        out.write(f"- **flashcard_summary**: {details['flashcard_summary']}\n")
        out.write(f"- **flashcard_back**: {details['flashcard_back']}\n")
        out.write("\n" + "="*50 + "\n\n")

print(f"Extracted rework details to {output_md}")
