import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("public/data/exams/110-2/medicine-2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

target_qnums = [7, 26, 40, 43]
for q in data.get("questions", []):
    qnum = q.get("question_number")
    if qnum in target_qnums:
        print(f"=== 第 {qnum} 題 ===")
        print("manual_review_notes:", q.get("manual_review_notes"))
        print("explanation:")
        print(q.get("explanation"))
        print("\n" + "="*40 + "\n")
