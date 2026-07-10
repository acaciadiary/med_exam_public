import json

source_file = r"d:\Antigravity\med_exam_public\public\data\exams\108-1\medicine-6.json"

with open(source_file, 'r', encoding='utf-8') as f:
    source = json.load(f)

print("=== Scanning source exam for non-standard answers ===")
for q in source.get("questions", []):
    q_num = q.get("question_number")
    correct_answers = q.get("correct_answers", [])
    correct_answer = q.get("correct_answer", "")
    answer_status = q.get("answer_status", "standard")
    
    issues = []
    if len(correct_answers) > 1:
        issues.append(f"Multiple correct answers: {correct_answers}")
    if len(correct_answers) == 0:
        issues.append("No correct answers listed in correct_answers")
    if answer_status != "standard":
        issues.append(f"Non-standard answer status: {answer_status}")
        
    if issues:
        print(f"Q{q_num} (id: {q['id']}): {', '.join(issues)} (Official Answer: {correct_answer})")
