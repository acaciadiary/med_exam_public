import json
import os
import re

update_path = "scratch/rewrite_updates/108-1_medicine-6/q061-q070.json"
banned_words = [
    "非本題答案", "不是本題標準答案", "回到題幹線索", "請用題幹線索連回",
    "題目中選項", "不能最精準回答本題", "最符合題幹", "核心記憶點",
    "定義、機轉、典型表現或處置原則", "此選項不是最佳答案", 
    "與正確答案的關鍵判斷點不一致", "原始解析重點指出", 
    "作答時應回到題幹線索與標準答案比對", "熟悉疾病機轉", "的基本判斷能力"
]

print("Starting validation...")

if not os.path.exists(update_path):
    print(f"Error: Update file not found at {update_path}")
    exit(1)

try:
    with open(update_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error: JSONDecodeError: {e}")
    exit(1)

# Check structure
required_top_keys = {"source_file", "dataset_id", "range", "updates"}
missing_top_keys = required_top_keys - set(data.keys())
if missing_top_keys:
    print(f"Error: Missing top-level keys: {missing_top_keys}")
    exit(1)

source_file = data["source_file"]
dataset_id = data["dataset_id"]
updates = data["updates"]

if source_file != "public/data/exams/108-1/medicine-6.json":
    print(f"Error: source_file mismatch: {source_file}")
    exit(1)

if dataset_id != "108-1_medicine-6":
    print(f"Error: dataset_id mismatch: {dataset_id}")
    exit(1)

if len(updates) != 10:
    print(f"Error: updates length should be 10, but got {len(updates)}")
    exit(1)

required_item_keys = {
    "question_id", "question_number", "explanation", "key_point",
    "flashcard_front", "flashcard_back", "flashcard_summary",
    "review_status", "explanation_model", "explanation_generated_at",
    "manual_review_notes"
}

for i, item in enumerate(updates):
    q_num = item.get("question_number")
    q_id = item.get("question_id")
    print(f"Checking Q{q_num} (ID: {q_id})...")
    
    missing_item_keys = required_item_keys - set(item.keys())
    if missing_item_keys:
        print(f"Error: Q{q_num} is missing keys: {missing_item_keys}")
        exit(1)
        
    extra_keys = set(item.keys()) - required_item_keys
    if extra_keys:
        print(f"Error: Q{q_num} has unexpected keys: {extra_keys}")
        exit(1)
        
    explanation = item["explanation"]
    
    # Check sections
    for sec in ["【題幹解析】", "【選項詳解】", "【核心考點】"]:
        if sec not in explanation:
            print(f"Error: Q{q_num} explanation is missing section: {sec}")
            exit(1)
            
    # Check option lines
    for opt in ["- A.", "- B.", "- C.", "- D."]:
        if opt not in explanation:
            print(f"Error: Q{q_num} explanation is missing option description: {opt}")
            exit(1)
            
    # Check banned words
    for word in banned_words:
        if word in explanation:
            print(f"Warning: Q{q_num} explanation contains banned word: '{word}'")
            # We fail the validation on banned words to ensure high quality
            exit(1)
            
    # Check other fields
    if item["review_status"] != "ai_generated":
        print(f"Error: Q{q_num} review_status should be 'ai_generated'")
        exit(1)
        
    if item["explanation_model"] != "codex-high-quality-rewrite":
        print(f"Error: Q{q_num} explanation_model should be 'codex-high-quality-rewrite'")
        exit(1)

print("Validation PASSED successfully!")
