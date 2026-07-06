import json
from pathlib import Path

json_path = Path("public/data/exams/113-2/medicine-6.json")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

banned = [
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

for q in data["questions"]:
    exp = q.get("explanation", "")
    found = [w for w in banned if w in exp]
    if found:
        print(f"Q{q.get('question_number')}: {found}")
