import json
import os

update_file = r'D:\Antigravity\med_exam_public\scratch\rewrite_updates\109-2_medicine-2\q091-q100.json'
source_file = r'D:\Antigravity\med_exam_public\public\data\exams\109-2\medicine-2.json'

with open(update_file, 'r', encoding='utf-8') as f:
    up_data = json.load(f)

with open(source_file, 'r', encoding='utf-8') as f:
    src_data = json.load(f)

assert up_data['source_file'] == "public/data/exams/109-2/medicine-2.json"
assert up_data['dataset_id'] == "109-2_medicine-2"
assert up_data['range'] == {"start": 91, "end": 100}

src_questions = src_data['questions']
src_q_map = {q['question_number']: q for q in src_questions}

# 禁用詞清單
banned_phrases = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "題目中選項 A 所代表的鑑別或處置",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
    "標準答案所接受的判斷",
    "雖然與題目主題相關",
    "與標準答案的關鍵判斷不一致",
    "對照本題核心解析",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致"
]

print("Starting validation...")
errors = []

for up in up_data['updates']:
    num = up['question_number']
    q_id = up['question_id']
    print(f"Checking Q{num}...")
    
    if num not in range(91, 101):
        errors.append(f"Q{num} is out of assigned range [91, 100].")
        continue
        
    if num not in src_q_map:
        errors.append(f"Q{num} not found in source file.")
        continue
        
    src_q = src_q_map[num]
    if src_q['id'] != q_id:
        errors.append(f"Q{num} ID mismatch. Expected: {src_q['id']}, Got: {q_id}")
        
    # Check allowed fields
    allowed_keys = {
        "question_id", "question_number", "explanation", "key_point",
        "flashcard_front", "flashcard_back", "flashcard_summary",
        "review_status", "explanation_model", "explanation_generated_at",
        "manual_review_notes"
    }
    for k in up.keys():
        if k not in allowed_keys:
            errors.append(f"Q{num} has forbidden field: {k}")
            
    # Check banned phrases in explanation
    exp = up['explanation']
    for bp in banned_phrases:
        if bp in exp:
            errors.append(f"Q{num} contains banned phrase: '{bp}'")
            
    # Check repeated option segments
    lines = [line.strip() for line in exp.split('\n') if line.strip().startswith(('- A.', '- B.', '- C.', '- D.'))]
    # Simple check for repeated long substrings in options
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            # Compare paragraphs
            text_i = lines[i][4:].strip()
            text_j = lines[j][4:].strip()
            if len(text_i) > 20 and len(text_j) > 20:
                if text_i == text_j:
                     errors.append(f"Q{num} has identical option explanations for {lines[i][:4]} and {lines[j][:4]}")

if errors:
    print("Validation failed:")
    for err in errors:
        print(f" - {err}")
    exit(1)
else:
    print("All checks passed successfully!")
