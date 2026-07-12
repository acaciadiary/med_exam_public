import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

source_path = 'd:/Antigravity/med_exam_public/public/data/exams/109-1/medicine-1.json'

with open(source_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data.get('questions', [])
q41 = [q for q in questions if q.get('question_number') == 41][0]

for k, v in q41.items():
    if k not in ['explanation', 'question_text', 'options']:
        print(f"{k}: {repr(v)}")
