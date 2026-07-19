# -*- coding: utf-8 -*-
import json
import os

banned = [
    '非本題答案',
    '不是本題標準答案',
    '回到題幹線索',
    '請用題幹線索連回',
    '題目中選項',
    '不能最精準回答',
    '最符合題幹',
    '核心記憶點',
    '定義、機轉、典型表現或處置原則',
    '標準答案所接受的判斷',
    '雖然與題目主題相關',
    '與標準答案的關鍵判斷',
    '對照本題核心解析',
    '此選項不是最佳答案',
    '與正確答案的關鍵判斷',
    '與標準答案的關鍵判斷',
    '作答時應回到題幹線索',
    '熟悉疾病機轉、臨床表現、診斷檢查與治療原則'
]

json_path = r'd:\Antigravity\med_exam_public\scratch\rewrite_updates\109-2_medicine-4\q031-q040.json'
if not os.path.exists(json_path):
    print(f"File not found: {json_path}")
    exit(1)

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

found = []
for q in data['updates']:
    exp = q['explanation']
    q_num = q['question_number']
    for b in banned:
        if b in exp:
            found.append((q_num, b))

if found:
    print("FAILED: Found banned phrases:")
    for q_num, b in found:
        print(f"Question {q_num}: found '{b}'")
else:
    print("PASSED: No banned phrases found in explanation!")
