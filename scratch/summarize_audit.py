import json
from pathlib import Path

BAD_PATTERNS = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "作答時應回到題幹線索",
    "原始解析"
]

def summarize_exams():
    exam_dir = Path("public/data/exams")
    json_files = sorted(exam_dir.glob("**/*.json"))
    
    summary = []
    total_issues = 0
    
    for json_file in json_files:
        try:
            data = json.loads(json_file.read_text(encoding="utf-8-sig"))
        except Exception as e:
            continue
            
        dataset_id = data.get("id", json_file.stem)
        questions = data.get("questions", [])
        
        issue_count = 0
        for q in questions:
            explanation = str(q.get("explanation", ""))
            if any(pattern in explanation for pattern in BAD_PATTERNS):
                issue_count += 1
                
        if issue_count > 0:
            summary.append((dataset_id, issue_count, len(questions)))
            total_issues += issue_count
            
    print("=== 考卷低品質詳解統計 ===")
    print(f"總共發現 {len(summary)} 份考卷含有低品質詳解，共計 {total_issues} 題。")
    print("-" * 50)
    for dataset_id, count, total in summary:
        percentage = (count / total) * 100
        print(f"- {dataset_id}: {count} / {total} 題 ({percentage:.1f}%)")
    print("-" * 50)

if __name__ == "__main__":
    summarize_exams()
