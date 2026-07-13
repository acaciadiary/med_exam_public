import json
import os
import re

update_file_path = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\110-2_medicine-3\q011-q020.json"
source_file_path = r"d:\Antigravity\med_exam_public\public\data\exams\110-2\medicine-3.json"

print("Starting validation...")

# 1. Check if files exist
if not os.path.exists(update_file_path):
    print(f"Error: Update file does not exist at {update_file_path}")
    exit(1)

if not os.path.exists(source_file_path):
    print(f"Error: Source file does not exist at {source_file_path}")
    exit(1)

# 2. Try parsing JSON
try:
    with open(update_file_path, "r", encoding="utf-8") as f:
        update_data = json.load(f)
    print("Success: Update JSON successfully parsed.")
except Exception as e:
    print(f"Error: Failed to parse update JSON. Error: {e}")
    exit(1)

try:
    with open(source_file_path, "r", encoding="utf-8") as f:
        source_data = json.load(f)
    print("Success: Source JSON successfully parsed.")
except Exception as e:
    print(f"Error: Failed to parse source JSON. Error: {e}")
    exit(1)

# 3. Check top-level keys
allowed_top_keys = {"source_file", "dataset_id", "range", "updates"}
actual_top_keys = set(update_data.keys())
extra_top_keys = actual_top_keys - allowed_top_keys
if extra_top_keys:
    print(f"Error: Found forbidden top-level keys in update JSON: {extra_top_keys}")
    exit(1)

# 4. Check range
rng = update_data.get("range", {})
start = rng.get("start")
end = rng.get("end")
if start != 11 or end != 20:
    print(f"Error: Expected range 11-20, but got {start}-{end}")
    exit(1)

# 5. Check dataset_id
if update_data.get("dataset_id") != "110-2_medicine-3":
    print(f"Error: Expected dataset_id '110-2_medicine-3', but got '{update_data.get('dataset_id')}'")
    exit(1)

# 6. Check updates keys and range
updates = update_data.get("updates", [])
if len(updates) != 10:
    print(f"Error: Expected exactly 10 updates, but got {len(updates)}")
    exit(1)

allowed_update_keys = {
    "question_id", "question_number", "explanation", "key_point",
    "flashcard_front", "flashcard_back", "flashcard_summary",
    "review_status", "explanation_model", "explanation_generated_at",
    "manual_review_notes"
}

forbidden_phrases = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "題目中選項 A 所代表的鑑別或處置",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "原始解析重點指出",
    "作答時應回到題幹線索與標準答案比對"
]

source_questions = {q["question_number"]: q for q in source_data.get("questions", [])}

for idx, q_update in enumerate(updates):
    num = q_update.get("question_number")
    qid = q_update.get("question_id")
    
    # Check if number is in range
    if num is None or not (11 <= num <= 20):
        print(f"Error: Update item at index {idx} has out-of-range or missing number: {num}")
        exit(1)
        
    expected_qid = f"110-2_medicine-3_{num:03d}"
    if qid != expected_qid:
        print(f"Error: Expected question_id '{expected_qid}' for question {num}, but got '{qid}'")
        exit(1)
        
    # Check forbidden keys inside updates
    actual_keys = set(q_update.keys())
    extra_keys = actual_keys - allowed_update_keys
    if extra_keys:
        print(f"Error: Question {num} has forbidden keys: {extra_keys}")
        exit(1)
        
    # Check explanation structure
    explanation = q_update.get("explanation", "")
    headings = ["【題幹解析】", "【選項詳解】", "【核心考點】"]
    for h in headings:
        if h not in explanation:
            print(f"Error: Question {num} explanation is missing heading: {h}")
            exit(1)
            
    # Check if each option has its own explanation
    for opt in ["- A.", "- B.", "- C.", "- D."]:
        if opt not in explanation:
            print(f"Error: Question {num} explanation is missing option description: {opt}")
            exit(1)
            
    # Check for forbidden filler phrases
    for fp in forbidden_phrases:
        if fp in explanation:
            print(f"Error: Question {num} explanation contains banned phrase: '{fp}'")
            exit(1)
            
    # Compare with source
    if num not in source_questions:
        print(f"Error: Question {num} not found in source exam paper questions list")
        exit(1)
        
    source_q = source_questions[num]
    if source_q["id"] != qid:
        print(f"Error: Question {num} id '{qid}' does not match source id '{source_q['id']}'")
        exit(1)

print("Success: All 10 questions passed validation checks successfully!")
