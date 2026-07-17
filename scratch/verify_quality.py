import json
from pathlib import Path

def main():
    exam_path = Path("public/data/exams/109-2/medicine-2.json")
    if not exam_path.exists():
        print(f"Error: {exam_path} not found.")
        return
        
    with open(exam_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    banned_phrases = [
        "非本題答案",
        "不是本題標準答案",
        "回到題幹線索",
        "請用題幹線索連回",
        "題目中選項 A 所代表的鑑別或處置",
        "不能最精準回答本題",
        "最符合題幹",
        "核心記憶點",
        "定義、機轉、典型表現或處置原則",
        "標準答案所接受的判斷",
        "雖然與題目主題相關",
        "與標準答案的關鍵判斷不一致",
        "對照本題核心解析",
        "此選項不是最佳答案",
        "與正確答案的關鍵判斷點不一致"
    ]
    
    issues_found = 0
    questions = data.get("questions", [])
    
    print(f"Auditing {len(questions)} questions for banned phrases...\n")
    
    for q in questions:
        q_num = q.get("question_number")
        explanation = q.get("explanation", "")
        
        # Check for banned phrases
        for phrase in banned_phrases:
            if phrase in explanation:
                print(f"Question {q_num}: Found banned phrase '{phrase}'")
                issues_found += 1
                
        # Check if the explanation structure is correct
        required_headers = ["【題幹解析】", "【選項詳解】", "【核心考點】"]
        for header in required_headers:
            if header not in explanation:
                print(f"Question {q_num}: Missing header '{header}'")
                issues_found += 1
                
        # Check options A-D explanation detail
        for opt in ["A", "B", "C", "D"]:
            opt_header = f"- {opt}."
            if opt_header not in explanation:
                print(f"Question {q_num}: Missing option explanation header '{opt_header}'")
                issues_found += 1
                
    if issues_found == 0:
        print("Success! No quality issues (banned phrases or structural errors) found in medicine-2.json.")
    else:
        print(f"\nAudit complete. Found {issues_found} potential quality issues.")

if __name__ == "__main__":
    main()
