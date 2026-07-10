import os
import json
import re

update_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\108-1_medicine-6"
source_file = r"d:\Antigravity\med_exam_public\public\data\exams\108-1\medicine-6.json"

# Load source exam to mapping
with open(source_file, 'r', encoding='utf-8') as f:
    source_data = json.load(f)

source_q_map = {q['id']: q for q in source_data.get('questions', [])}

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
    "本題答案為",
    "答案選"
]

allowed_fields = {
    "question_id", "question_number", "explanation", "key_point",
    "flashcard_front", "flashcard_back", "flashcard_summary",
    "review_status", "explanation_model", "explanation_generated_at",
    "manual_review_notes"
}

audit_results = []
all_updates = []

for filename in sorted(os.listdir(update_dir)):
    if not filename.endswith('.json'):
        continue
    filepath = os.path.join(update_dir, filename)
    print(f"Auditing {filename}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"Error parsing {filename}: {e}")
            audit_results.append({
                "file": filename,
                "error": f"JSON parse error: {e}"
            })
            continue

    # Check structure
    if "updates" not in data:
        audit_results.append({
            "file": filename,
            "error": "Missing 'updates' array"
        })
        continue

    for idx, update in enumerate(data["updates"]):
        q_id = update.get("question_id")
        q_num = update.get("question_number")
        
        issue_list = []
        
        # Field validation
        extra_fields = set(update.keys()) - allowed_fields
        if extra_fields:
            issue_list.append(f"Contains forbidden fields: {list(extra_fields)}")

        # Check explanation
        explanation = update.get("explanation", "")
        
        if not explanation:
            issue_list.append("Explanation is empty")
        else:
            # Check structure
            if "【題幹解析】" not in explanation:
                issue_list.append("Missing 【題幹解析】")
            if "【選項詳解】" not in explanation:
                issue_list.append("Missing 【選項詳解】")
            if "【核心考點】" not in explanation:
                issue_list.append("Missing 【核心考點】")
            
            # Check options in options details
            options_sec = ""
            if "【選項詳解】" in explanation:
                parts = explanation.split("【選項詳解】")
                if len(parts) > 1:
                    options_sec = parts[1].split("【核心考點】")[0]
            
            # Count options
            for opt in ['A', 'B', 'C', 'D']:
                pattern = rf"-\s*{opt}\."
                if not re.search(pattern, options_sec):
                    issue_list.append(f"Missing detailed explanation for Option {opt}")
                else:
                    # check if the text for the option is too generic or short
                    opt_match = re.search(rf"-\s*{opt}\.\s*(.*?)(?=(-\s*[A-D]\.|\Z))", options_sec, re.DOTALL)
                    if opt_match:
                        opt_text = opt_match.group(1).strip()
                        if len(opt_text) < 10:
                            issue_list.append(f"Option {opt} explanation is too short ({len(opt_text)} chars): '{opt_text}'")
                        # check if same paragraph copied
                        # We can flag this if multiple options have identical text
            
            # Check banned phrases
            for phrase in banned_phrases:
                if phrase in explanation:
                    issue_list.append(f"Contains banned phrase: '{phrase}'")

        # Check flashcards & key points
        key_point = update.get("key_point", "")
        flash_sum = update.get("flashcard_summary", "")
        flash_back = update.get("flashcard_back", "")
        
        if not key_point or len(key_point.strip()) < 5:
            issue_list.append(f"key_point is empty or too short: '{key_point}'")
        if not flash_sum or len(flash_sum.strip()) < 5:
            issue_list.append(f"flashcard_summary is empty or too short: '{flash_sum}'")
        if not flash_back or len(flash_back.strip()) < 5:
            issue_list.append(f"flashcard_back is empty or too short: '{flash_back}'")

        for phrase in banned_phrases:
            if phrase in key_point:
                issue_list.append(f"key_point contains banned phrase: '{phrase}'")
            if phrase in flash_sum:
                issue_list.append(f"flashcard_summary contains banned phrase: '{phrase}'")
            if phrase in flash_back:
                issue_list.append(f"flashcard_back contains banned phrase: '{phrase}'")

        # Check source match
        if q_id not in source_q_map:
            issue_list.append(f"Question ID {q_id} not found in source exam")
        else:
            sq = source_q_map[q_id]
            if sq.get("question_number") != q_num:
                issue_list.append(f"Question number mismatch: source={sq.get('question_number')}, update={q_num}")

        # Record update for duplication checks
        all_updates.append({
            "file": filename,
            "q_num": q_num,
            "q_id": q_id,
            "issues": issue_list,
            "raw_update": update
        })

# Check duplicate / missing questions
q_nums_seen = {}
for item in all_updates:
    num = item["q_num"]
    q_nums_seen.setdefault(num, []).append(item["file"])

for num, files in q_nums_seen.items():
    if len(files) > 1:
        print(f"Warning: Question {num} is defined in multiple files: {files}")

# Check missing questions (expecting 1-80)
missing_nums = []
for i in range(1, 81):
    if i not in q_nums_seen:
        missing_nums.append(i)
if missing_nums:
    print(f"Warning: Missing questions: {missing_nums}")

# Print issues summary
issues_count = 0
passed_count = 0
rework_list = []

print("\n--- AUDIT DETAILS ---")
for item in sorted(all_updates, key=lambda x: x["q_num"]):
    if item["issues"]:
        issues_count += 1
        rework_list.append((item["q_num"], item["file"], item["issues"]))
        print(f"Q{item['q_num']} ({item['file']}) HAS ISSUES:")
        for issue in item["issues"]:
            print(f"  - {issue}")
    else:
        passed_count += 1

print(f"\nTotal audited: {len(all_updates)}")
print(f"Passed: {passed_count}")
print(f"Failed/Need Rework: {issues_count}")
if missing_nums:
    print(f"Missing Qs: {missing_nums}")

# Write detailed report to a file
report_file = r"d:\Antigravity\med_exam_public\scratch\audit_report.json"
with open(report_file, 'w', encoding='utf-8') as f:
    json.dump({
        "total": len(all_updates),
        "passed": passed_count,
        "failed": issues_count,
        "missing": missing_nums,
        "rework": [{
            "q_num": r[0],
            "file": r[1],
            "issues": r[2]
        } for r in rework_list]
    }, f, ensure_ascii=False, indent=2)
print(f"Report written to {report_file}")
