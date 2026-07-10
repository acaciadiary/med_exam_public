import json
from pathlib import Path

# 定義禁用/低品質詞彙
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

def audit_exams():
    exam_dir = Path("public/data/exams")
    json_files = sorted(exam_dir.glob("**/*.json"))
    
    overall_report = {}
    total_low_quality_questions = 0
    
    for json_file in json_files:
        try:
            data = json.loads(json_file.read_text(encoding="utf-8-sig"))
        except Exception as e:
            print(f"Error reading {json_file}: {e}")
            continue
            
        dataset_id = data.get("id", json_file.stem)
        questions = data.get("questions", [])
        
        file_issues = []
        for q in questions:
            qid = q.get("id")
            q_num = q.get("question_number")
            explanation = str(q.get("explanation", ""))
            
            matched_patterns = []
            for pattern in BAD_PATTERNS:
                if pattern in explanation:
                    matched_patterns.append(pattern)
            
            if matched_patterns:
                file_issues.append({
                    "question_id": qid,
                    "question_number": q_num,
                    "matched_patterns": matched_patterns,
                    "explanation_snippet": explanation[:100] + "..." if len(explanation) > 100 else explanation
                })
        
        if file_issues:
            overall_report[dataset_id] = {
                "file_path": str(json_file),
                "issue_count": len(file_issues),
                "issues": file_issues
            }
            total_low_quality_questions += len(file_issues)
            
    # 將報告寫入檔案，避免終端機亂碼
    report_lines = []
    report_lines.append(f"=== 審計報告 ===")
    report_lines.append(f"總共掃描了 {len(json_files)} 份考卷")
    report_lines.append(f"發現含有低品質詞彙的考卷數量: {len(overall_report)}")
    report_lines.append(f"總低品質題目數: {total_low_quality_questions}")
    report_lines.append("")
    
    for dataset_id, info in overall_report.items():
        report_lines.append(f"考卷: {dataset_id} ({info['issue_count']} 題低品質)")
        for issue in info["issues"]:
            report_lines.append(f"  - 第 {issue['question_number']} 題 (ID: {issue['question_id']}): 命中詞彙 {issue['matched_patterns']}")
        report_lines.append("-" * 50)
        
    report_text = "\n".join(report_lines)
    
    # 輸出到檔案
    report_file = Path("scratch/audit_report.txt")
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text(report_text, encoding="utf-8")
    print(f"Audit completed. Report written to {report_file.absolute()}")

if __name__ == "__main__":
    audit_exams()
