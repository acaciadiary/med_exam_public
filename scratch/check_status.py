import json
from pathlib import Path

json_path = Path("public/data/exams/113-2/medicine-6.json")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data.get("questions", [])
print(f"Total questions: {len(questions)}")

empty_count = 0
invalid_format_count = 0
banned_words_count = 0

banned_words = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "題目中選項 A 所代表的鑑別或處置",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則"
]

for q in questions:
    exp = q.get("explanation", "")
    qid = q.get("id")
    qnum = q.get("question_number")
    
    if not exp.strip():
        empty_count += 1
        continue
        
    # Check format
    has_tigan = "【題幹解析】" in exp
    has_options = "【選項詳解】" in exp
    has_core = "【核心考點】" in exp
    
    if not (has_tigan and has_options and has_core):
        invalid_format_count += 1
        print(f"Q {qnum} ({qid}) missing required headers")
        continue
        
    # Check banned words
    found_banned = [w for w in banned_words if w in exp]
    if found_banned:
        banned_words_count += 1
        print(f"Q {qnum} ({qid}) has banned words: {found_banned}")

print(f"Empty: {empty_count}")
print(f"Invalid format: {invalid_format_count}")
print(f"Has banned words: {banned_words_count}")
