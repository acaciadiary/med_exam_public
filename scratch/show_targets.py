import os
import json

UPDATES_DIR = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\109-2_medicine-1"
TARGET_QIDS = [
    "109-2_medicine-1_010",
    "109-2_medicine-1_022",
    "109-2_medicine-1_023",
    "109-2_medicine-1_031",
    "109-2_medicine-1_034",
    "109-2_medicine-1_038",
    "109-2_medicine-1_040",
    "109-2_medicine-1_060",
    "109-2_medicine-1_070",
    "109-2_medicine-1_076",
    "109-2_medicine-1_085"
]

def show_targets():
    files = sorted([f for f in os.listdir(UPDATES_DIR) if f.endswith('.json')])
    found = {}
    for filename in files:
        filepath = os.path.join(UPDATES_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for update in data.get("updates", []):
                qid = update.get("question_id")
                if qid in TARGET_QIDS:
                    found[qid] = {
                        "filename": filename,
                        "update": update
                    }
                    
    with open(r"d:\Antigravity\med_exam_public\scratch\show_targets.txt", "w", encoding="utf-8") as out:
        for qid in TARGET_QIDS:
            if qid not in found:
                out.write(f"=== QID {qid} NOT FOUND ===\n")
                continue
            info = found[qid]
            update = info["update"]
            out.write(f"==================================================\n")
            out.write(f"QID: {qid} (in {info['filename']})\n")
            out.write(f"explanation:\n{update.get('explanation')}\n")
            out.write(f"key_point: {update.get('key_point')}\n")
            out.write(f"flashcard_summary: {update.get('flashcard_summary')}\n")
            out.write(f"flashcard_back: {update.get('flashcard_back')}\n")
            out.write(f"manual_review_notes: {update.get('manual_review_notes')}\n")
            out.write(f"==================================================\n\n")

if __name__ == "__main__":
    show_targets()
