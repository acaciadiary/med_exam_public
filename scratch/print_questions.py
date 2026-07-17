import json

SOURCE_FILE_PATH = r"d:\Antigravity\med_exam_public\public\data\exams\109-2\medicine-1.json"
TARGET_QIDS = [
    "109-2_medicine-1_010",
    "109-2_medicine-1_017",
    "109-2_medicine-1_020",
    "109-2_medicine-1_022",
    "109-2_medicine-1_023",
    "109-2_medicine-1_031",
    "109-2_medicine-1_034",
    "109-2_medicine-1_038",
    "109-2_medicine-1_040",
    "109-2_medicine-1_060",
    "109-2_medicine-1_070",
    "109-2_medicine-1_085"
]

def print_details():
    with open(SOURCE_FILE_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = {q['id']: q for q in data['questions']}
    
    with open(r"d:\Antigravity\med_exam_public\scratch\questions_info.txt", "w", encoding="utf-8") as out:
        for qid in TARGET_QIDS:
            if qid not in questions:
                out.write(f"=== QID {qid} NOT FOUND ===\n")
                continue
            q = questions[qid]
            out.write(f"==================================================\n")
            out.write(f"QID: {qid}\n")
            out.write(f"Question: {q.get('question_text')}\n")
            out.write(f"Options:\n")
            for k, v in q.get('options', {}).items():
                out.write(f"  {k}: {v}\n")
            out.write(f"Correct Answer: {q.get('correct_answer')}\n")
            out.write(f"==================================================\n\n")

if __name__ == "__main__":
    print_details()
