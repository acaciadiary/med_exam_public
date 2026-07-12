import json
import sys
import re

update_file = 'scratch/rewrite_updates/109-1_medicine-4/q041-q050.json'
source_file = 'public/data/exams/109-1/medicine-4.json'

# 1. 載入 JSON
try:
    with open(update_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error parsing update JSON: {e}")
    sys.exit(1)

try:
    with open(source_file, 'r', encoding='utf-8') as f:
        source_data = json.load(f)
except Exception as e:
    print(f"Error parsing source JSON: {e}")
    sys.exit(1)

# 2. 檢查頂層欄位
allowed_top_keys = {"source_file", "dataset_id", "range", "updates"}
top_keys = set(data.keys())
if not top_keys.issubset(allowed_top_keys):
    print(f"Top keys contain disallowed fields: {top_keys - allowed_top_keys}")
    sys.exit(1)

# 3. 檢查 range
if data.get("range") != {"start": 41, "end": 50}:
    print(f"Range is incorrect: {data.get('range')}")
    sys.exit(1)

# 4. 檢查 updates 欄位與內容
allowed_update_keys = {
    "question_id", "question_number", "explanation", "key_point",
    "flashcard_front", "flashcard_back", "flashcard_summary",
    "review_status", "explanation_model", "explanation_generated_at",
    "manual_review_notes"
}

banned_phrases = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "題目中選項 A 所代表",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "原始解析重點指出"
]

source_questions = {q['question_number']: q for q in source_data['questions']}

for upd in data['updates']:
    num = upd.get('question_number')
    qid = upd.get('question_id')
    
    # 檢查欄位
    upd_keys = set(upd.keys())
    if not upd_keys.issubset(allowed_update_keys):
        print(f"Question {num} contains disallowed fields: {upd_keys - allowed_update_keys}")
        sys.exit(1)
        
    # 檢查題號與ID是否匹配
    if num not in range(41, 51):
        print(f"Question number {num} out of range 41-50")
        sys.exit(1)
        
    orig_q = source_questions.get(num)
    if not orig_q:
        print(f"Question {num} not found in source")
        sys.exit(1)
        
    if orig_q['id'] != qid:
        print(f"Question ID mismatch for {num}: expected {orig_q['id']}, got {qid}")
        sys.exit(1)
        
    # 檢查三大標題
    explanation = upd.get('explanation', '')
    for header in ["【題幹解析】", "【選項詳解】", "【核心考點】"]:
        if header not in explanation:
            print(f"Question {num} explanation missing header: {header}")
            sys.exit(1)
            
    # 檢查禁用模板句
    for phrase in banned_phrases:
        if phrase in explanation:
            print(f"Question {num} explanation contains banned phrase: '{phrase}'")
            sys.exit(1)

print("ALL CHECKS PASSED SUCCESSFULLY!")
