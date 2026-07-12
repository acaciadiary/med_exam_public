import json
import sys

path = 'd:/Antigravity/med_exam_public/scratch/rewrite_updates/109-1_medicine-1/q041-q050.json'

try:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"JSON Parse Error: {e}")
    sys.exit(1)

print("JSON parsed successfully!")
print(f"source_file: {data.get('source_file')}")
print(f"dataset_id: {data.get('dataset_id')}")
print(f"range: {data.get('range')}")
print(f"Number of updates: {len(data.get('updates', []))}")

# Check updates fields
allowed_fields = {
    'question_id', 'question_number', 'explanation', 'key_point',
    'flashcard_front', 'flashcard_back', 'flashcard_summary',
    'review_status', 'explanation_model', 'explanation_generated_at',
    'manual_review_notes'
}

banned_terms = [
    '非本題答案', '不是本題標準答案', '回到題幹線索', '請用題幹線索連回',
    '題目中選項 A 所代表的鑑別或處置', '不能最精準回答本題', '最符合題幹',
    '核心記憶點', '定義、機轉、典型表現或處置原則', '此選項不是最佳答案',
    '與正確答案的關鍵判斷點不一致', '原始解析重點指出', '作答時應回到題幹線索與標準答案比對',
    '熟悉疾病機轉、臨床表現、診斷檢查與治療原則'
]

has_errors = False

for idx, u in enumerate(data.get('updates', [])):
    qnum = u.get('question_number')
    qid = u.get('question_id')
    print(f"Checking Q{qnum} (ID: {qid})...")
    
    # Check fields
    u_fields = set(u.keys())
    extra_fields = u_fields - allowed_fields
    if extra_fields:
        print(f"  Error: Extra fields found in Q{qnum}: {extra_fields}")
        has_errors = True
        
    missing_fields = allowed_fields - u_fields
    if missing_fields:
        print(f"  Error: Missing fields in Q{qnum}: {missing_fields}")
        has_errors = True
        
    # Check structure of explanation
    explanation = u.get('explanation', '')
    for header in ['【題幹解析】', '【選項詳解】', '【核心考點】']:
        if header not in explanation:
            print(f"  Error: Explanation for Q{qnum} is missing header: {header}")
            has_errors = True
            
    # Check banned terms in explanation, key_point, flashcards
    text_to_check = f"{explanation} {u.get('key_point')} {u.get('flashcard_front')} {u.get('flashcard_back')} {u.get('flashcard_summary')}"
    for term in banned_terms:
        if term in text_to_check:
            print(f"  Error: Q{qnum} contains banned term: '{term}'")
            has_errors = True

if has_errors:
    print("Validation FAILED!")
    sys.exit(1)
else:
    print("All validations PASSED successfully!")
