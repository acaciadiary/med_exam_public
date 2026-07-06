import json
from pathlib import Path
from datetime import datetime, timezone

json_path = Path("public/data/exams/113-2/medicine-6.json")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

now = datetime.now(timezone.utc).isoformat()
for q in data["questions"]:
    qnum = q.get("question_number")
    if 1 <= qnum <= 20:
        q["review_status"] = "ai_generated"
        q["explanation_model"] = "antigravity-subagent"
        q["explanation_generated_at"] = now

data["updated_at"] = now
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully updated Q1-Q20 in the original JSON file.")
