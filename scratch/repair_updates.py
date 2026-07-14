import json

def repair_q56():
    fpath = "scratch/rewrite_updates/114-2_medicine-3/q051-q060.json"
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for up in data["updates"]:
        if up["question_number"] == 56:
            # Replace in explanation
            up["explanation"] = up["explanation"].replace(
                "若符合定義的 5 項指標",
                "若符合該標準 5 項指標"
            )
            print("Repaired Q56!")
            
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def repair_q80():
    fpath = "scratch/rewrite_updates/114-2_medicine-3/q071-q080.json"
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for up in data["updates"]:
        if up["question_number"] == 80:
            # Replace in explanation
            up["explanation"] = up["explanation"].replace(
                "這是醫師的專業責任與法定義務。",
                "這是醫師的專業責任與法定職責。"
            )
            print("Repaired Q80!")
            
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    repair_q56()
    repair_q80()
