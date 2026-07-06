import json
from pathlib import Path

def main():
    json_path = Path("public/data/exams/113-2/medicine-5.json")
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
        
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    questions = data.get("questions", [])
    print(f"Total questions: {len(questions)}")
    
    empty_explanations = []
    short_explanations = []
    missing_sections = []
    banned_phrases = []
    
    banned_list = [
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
        qid = q.get("id")
        qnum = q.get("question_number")
        exp = q.get("explanation", "").strip()
        
        if not exp:
            empty_explanations.append(qnum)
            continue
            
        if len(exp) < 50:
            short_explanations.append((qnum, len(exp)))
            
        # Check sections
        has_tugan = "【題幹解析】" in exp
        has_option = "【選項詳解】" in exp
        has_core = "【核心考點】" in exp
        
        if not (has_tugan and has_option and has_core):
            missing_sections.append((qnum, has_tugan, has_option, has_core))
            
        # Check banned phrases
        found_banned = [p for p in banned_list if p in exp]
        if found_banned:
            banned_phrases.append((qnum, found_banned))
            
    print(f"Empty explanations ({len(empty_explanations)}): {empty_explanations}")
    print(f"Short explanations ({len(short_explanations)}): {short_explanations}")
    print(f"Missing sections ({len(missing_sections)}): {missing_sections}")
    print(f"Banned phrases ({len(banned_phrases)}): {banned_phrases}")

if __name__ == "__main__":
    main()
