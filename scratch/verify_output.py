# -*- coding: utf-8 -*-
import json

data_path = 'scratch/rewrite_updates/109-1_medicine-4/q061-q070.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

banned = [
    '非本題答案', 
    '不是本題標準答案', 
    '回到題幹線索', 
    '請用題幹線索連回', 
    '題目中選項 A 所代表的鑑別或處置', 
    '不能最精準回答本題', 
    '最符合題幹', 
    '核心記憶點', 
    '與正確答案的關鍵判斷點不一致', 
    '此選項不是最佳答案', 
    '原始解析重點指出'
]

issues = []
for u in data['updates']:
    q_num = u['question_number']
    
    # 檢查 flashcard_front 是否有 /
    if '/' in u['flashcard_front']:
        issues.append(f"Q{q_num}: flashcard_front contains '/' -> {repr(u['flashcard_front'])}")
    
    # 檢查 flashcard_front 是否為問句
    ff = u['flashcard_front'].strip()
    if not (ff.endswith('？') or ff.endswith('?') or '何者' in ff or '幾' in ff or '多少' in ff or '什麼' in ff or '哪' in ff):
        issues.append(f"Q{q_num}: flashcard_front might not be a question -> {repr(u['flashcard_front'])}")
        
    # 檢查各欄位是否包含禁用詞
    for field in ['explanation', 'key_point', 'flashcard_front', 'flashcard_back', 'flashcard_summary']:
        val = u.get(field, '')
        for b in banned:
            if b in val:
                issues.append(f"Q{q_num}: {field} contains banned phrase '{b}'")

if issues:
    print("Verification failed! Found issues:")
    for issue in issues:
        print(" -", issue)
else:
    print("Verification passed! No banned keywords, slashes, or invalid questions found.")
