import os
import json

UPDATES_DIR = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\109-2_medicine-1"
TARGET_QIDS = [
    "109-2_medicine-1_017",
    "109-2_medicine-1_020"
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
                    
    with open(r"d:\Antigravity\med_exam_public\scratch\show_targets_extra.txt", "w", encoding="utf-8") as out:
        for qid in TARGET_QIDS:
            if qid not in found:
                out.write(f"=== QID {qid} NOT FOUND ===\n")
                continue
            info = found[qid]
            update = info["update"]
            out.write(f"==================================================\n")
            out.write(f"QID: {qid} (in {info['filename']})\n")
            out.write(f"explanation:\n{update.get('explanation')}\n")
            out.write(f"==================================================\n\n")

if __name__ == "__main__":
    show_targets()
