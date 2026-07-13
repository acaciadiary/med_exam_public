import json
import os

def main():
    filepath = "public/data/exams/110-2/medicine-2.json"
    artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\7755ca7f-7f3f-4769-bf17-eb0468b1a6d2"
    out_path = os.path.join(artifact_dir, "flagged_questions.md")
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    target_qnums = [7, 26, 40, 43]
    questions_map = {q.get("question_number"): q for q in data.get("questions", [])}
    
    md_content = []
    md_content.append("# 110-2 Medicine-2 疑似需人工複核題詳情")
    md_content.append("以下為審查中發現疑似有官方答案疑義、題幹排版錯亂或倫理爭議，因而標記為「疑似需人工複核」的題目詳情：\n")
    
    for qnum in target_qnums:
        q = questions_map.get(qnum)
        if not q:
            continue
        
        md_content.append(f"## 第 {qnum} 題")
        md_content.append(f"**題目識別碼 (ID):** `{q.get('id')}`  ")
        md_content.append(f"**官方公佈答案:** `{q.get('correct_answer')}`")
        
        md_content.append("\n### 題目與選項")
        md_content.append(f"**題幹:**\n{q.get('question_text')}\n")
        
        md_content.append("**選項:**")
        opts = q.get("options", [])
        for opt in opts:
            if isinstance(opt, dict):
                md_content.append(f"- {opt.get('alias', '')}. {opt.get('text', '')}")
            else:
                md_content.append(f"- {opt}")
            
        md_content.append("\n### 詳解與解析內容")
        md_content.append(f"```text\n{q.get('explanation')}\n```")
        
        md_content.append("\n### 學習欄位與狀態")
        md_content.append(f"- **核心考點 (Key Point):** {q.get('key_point')}")
        md_content.append(f"- **Flashcard Summary:** {q.get('flashcard_summary')}")
        md_content.append(f"- **Flashcard Back:** {q.get('flashcard_back')}")
        md_content.append(f"- **Manual Review Notes:** {q.get('manual_review_notes')}")
        md_content.append("\n" + "-"*50 + "\n")
        
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))
    print(f"Report generated successfully at: {out_path}")

if __name__ == "__main__":
    main()
