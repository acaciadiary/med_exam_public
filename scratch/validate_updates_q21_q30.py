import json
import os

allowed_keys = {
  'question_id', 'question_number', 'explanation', 'key_point',
  'flashcard_front', 'flashcard_back', 'flashcard_summary',
  'review_status', 'explanation_model', 'explanation_generated_at',
  'manual_review_notes'
}

banned_phrases = [
  '非本題答案', '不是本題標準答案', '回到題幹線索', '請用題幹線索連回',
  '題目中選項 A 所代表的鑑別或處置', '不能最精準回答本題', '最符合題幹',
  '核心記憶點', '定義、機轉、典型表現或處置原則', '此選項不是最佳答案',
  '與正確答案的關鍵判斷點不一致', '作答時應回到題幹線索與標準答案比對',
  '熟悉疾病機轉、臨床表現、診斷檢查與治療原則', '心臟內科的基本判斷能力',
  '原始解析重點指出'
]

path = 'scratch/rewrite_updates/109-1_medicine-1/q021-q030.json'

with open(path, encoding='utf-8') as f:
  data = json.load(f)

# Validate top-level keys
assert data['source_file'] == 'public/data/exams/109-1/medicine-1.json', 'source_file mismatch'
assert data['dataset_id'] == '109-1_medicine-1', 'dataset_id mismatch'
assert data['range'] == 'q021-q030', 'range mismatch'

updates = data['updates']
assert len(updates) == 10, f'Expected 10 updates, got {len(updates)}'

warnings_found = 0
for idx, up in enumerate(updates):
  qnum = up['question_number']
  print(f'Checking Q{qnum}...')
  
  # Check keys
  keys = set(up.keys())
  if keys != allowed_keys:
    raise AssertionError(f'Q{qnum} keys mismatch: {keys ^ allowed_keys}')
  
  # Check headings
  exp = up['explanation']
  for h in ['【題幹解析】', '【選項詳解】', '【核心考點】']:
    assert h in exp, f'Q{qnum} explanation missing heading {h}'
  
  # Check options A-D in explanation
  for opt in ['- A.', '- B.', '- C.', '- D.']:
    assert opt in exp, f'Q{qnum} explanation missing option {opt}'
  
  # Check banned phrases
  for phrase in banned_phrases:
    if phrase in exp:
      print(f'WARNING: Q{qnum} contains banned phrase: "{phrase}"')
      warnings_found += 1
    if phrase in up['key_point']:
      print(f'WARNING: Q{qnum} key_point contains banned phrase: "{phrase}"')
      warnings_found += 1
    if phrase in up['flashcard_back']:
      print(f'WARNING: Q{qnum} flashcard_back contains banned phrase: "{phrase}"')
      warnings_found += 1

if warnings_found == 0:
  print('All checks passed successfully! No issues found.')
else:
  print(f'Done checking. Found {warnings_found} warning(s).')
