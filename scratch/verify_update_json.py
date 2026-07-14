# -*- coding: utf-8 -*-
import json
import os
import sys

update_path = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\110-1_medicine-6\q061-q070.json"
source_path = r"d:\Antigravity\med_exam_public\public\data\exams\110-1\medicine-6.json"

banned_phrases = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "題目中選項 A 所代表的鑑別或處置",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "原始解析重點指出",
    "熟悉疾病機轉、臨床表現、診斷檢查與治療原則"
]

print("Starting validation...")

# Load update file
if not os.path.exists(update_path):
    print(f"Error: Update file not found at {update_path}")
    sys.exit(1)

with open(update_path, "r", encoding="utf-8") as f:
    try:
        update_data = json.load(f)
    except Exception as e:
        print(f"Error parsing update JSON: {e}")
        sys.exit(1)

# Load source file
if not os.path.exists(source_path):
    print(f"Error: Source file not found at {source_path}")
    sys.exit(1)

with open(source_path, "r", encoding="utf-8") as f:
    try:
        source_data = json.load(f)
    except Exception as e:
        print(f"Error parsing source JSON: {e}")
        sys.exit(1)

# Check top level keys
required_top_keys = ["source_file", "dataset_id", "range", "updates"]
for k in required_top_keys:
    if k not in update_data:
        print(f"Error: Missing top-level key '{k}'")
        sys.exit(1)

# Check range
rng = update_data["range"]
if rng.get("start") != 61 or rng.get("end") != 70:
    print(f"Error: Range should be 61 to 70, got {rng}")
    sys.exit(1)

updates = update_data["updates"]
if len(updates) != 10:
    print(f"Error: Updates should have exactly 10 items, got {len(updates)}")
    sys.exit(1)

# Index source questions by number
source_qs = {q["question_number"]: q for q in source_data["questions"]}

# Check each update
for i, item in enumerate(updates):
    qnum = item.get("question_number")
    qid = item.get("question_id")
    
    if qnum is None or qid is None:
        print(f"Error at index {i}: Missing question_number or question_id")
        sys.exit(1)
        
    if qnum not in source_qs:
        print(f"Error at index {i}: Question number {qnum} not found in source file")
        sys.exit(1)
        
    sq = source_qs[qnum]
    if sq["id"] != qid:
        print(f"Error at index {i}: ID mismatch. Expected {sq['id']}, got {qid}")
        sys.exit(1)
        
    # Check fields
    required_update_fields = [
        "question_id", "question_number", "explanation", "key_point",
        "flashcard_front", "flashcard_back", "flashcard_summary",
        "review_status", "explanation_model", "explanation_generated_at",
        "manual_review_notes"
    ]
    
    for fld in required_update_fields:
        if fld not in item:
            print(f"Error in question {qnum}: Missing field '{fld}'")
            sys.exit(1)
            
    # Check headings in explanation
    exp = item["explanation"]
    headings = ["【題幹解析】", "【選項詳解】", "【核心考點】"]
    for hd in headings:
        if hd not in exp:
            print(f"Error in question {qnum}: Heading '{hd}' not found in explanation")
            sys.exit(1)
            
    # Check banned phrases
    for phrase in banned_phrases:
        if phrase in exp:
            print(f"Warning/Error in question {qnum}: Banned phrase '{phrase}' found in explanation")
            sys.exit(1)

print("Validation PASSED successfully! All fields match source questions, structure is correct, and no banned phrases found.")
