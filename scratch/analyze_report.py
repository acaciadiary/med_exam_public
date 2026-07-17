import json
from pathlib import Path

def main():
    report_path = Path("reports/all-content-trust.json")
    if not report_path.exists():
        print("Error: reports/all-content-trust.json not found")
        return
        
    with open(report_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    summary = data.get("summary", {})
    files = data.get("files", [])
    
    # Categories of files
    clean_files = []
    only_repeated_files = []
    banned_phrase_files = []
    
    for f in files:
        path = f.get("path")
        dataset_id = f.get("dataset_id")
        risk_score = f.get("risk_score", 0)
        issue_counts = f.get("issue_counts", {})
        review_status_counts = f.get("review_status_counts", {})
        
        has_banned = "banned_template_phrase" in issue_counts
        has_repeated = "repeated_option_segment" in issue_counts
        
        file_info = {
            "path": path,
            "dataset_id": dataset_id,
            "risk_score": risk_score,
            "issue_counts": issue_counts,
            "review_status_counts": review_status_counts,
            "question_count": f.get("question_count", 0)
        }
        
        if risk_score == 0:
            clean_files.append(file_info)
        elif has_banned:
            banned_phrase_files.append(file_info)
        elif has_repeated and not has_banned:
            only_repeated_files.append(file_info)
            
    print(f"Clean files (risk_score == 0): {len(clean_files)}")
    print(f"Files with ONLY repeated option segments: {len(only_repeated_files)}")
    print(f"Files with banned template phrases (and possibly repeated segments): {len(banned_phrase_files)}")
    
    # Generate markdown report text
    md = []
    md.append("# 醫學國考詳解品質檢視報告\n")
    md.append(f"檢測時間: {data.get('generated_at')}\n")
    md.append("## 1. 總體統計\n")
    md.append(f"- **總考卷數**: {summary.get('dataset_count')} 張")
    md.append(f"- **總題目數**: {summary.get('question_count')} 題")
    md.append(f"- **有品質問題的考卷數**: {summary.get('risky_file_count')} 張")
    md.append(f"- **完全符合規範的考卷數**: {len(clean_files)} 張")
    md.append(f"- **已人工審查比例 (reviewed)**: {summary.get('reviewed_rate') * 100:.2f}% ({summary.get('review_status_counts', {}).get('reviewed', 0)} / {summary.get('question_count')} 題)\n")
    
    md.append("### 偵測到的品質問題統計")
    md.append("| 問題類型 | 出現次數 | 說明 |")
    md.append("| --- | --- | --- |")
    md.append(f"| 禁用範本句 (banned_template_phrase) | {summary.get('issue_counts', {}).get('banned_template_phrase', 0)} | 包含無實質醫學意義的罐頭回覆，如「對照本題核心解析」等 |")
    md.append(f"| 重複選項段落 (repeated_option_segment) | {summary.get('issue_counts', {}).get('repeated_option_segment', 0)} | 在同一題的多個選項中重複貼上相同的文字段落 |")
    md.append("\n")
    
    md.append("### 禁用範本句統計")
    md.append("| 禁用範本句 | 出現次數 |")
    md.append("| --- | --- |")
    for phrase, count in summary.get("phrase_counts", {}).items():
        md.append(f"| {phrase} | {count} |")
    md.append("\n")
    
    md.append("## 2. 考卷詳細狀態分類\n")
    
    md.append("### A. 需要優先修正的考卷（含有禁用範本句 & 重複選項段落）\n")
    md.append("這類考卷含有「對照本題核心解析」、「與標準答案的關鍵判斷不一致」等 AI 範本句，品質風險最高，應優先整張重寫。")
    md.append("| 考卷路徑 | 題數 | 風險分數 | 禁用範本句數 | 重複段落數 | 審查狀態 |")
    md.append("| --- | --- | --- | --- | --- | --- |")
    for f in sorted(banned_phrase_files, key=lambda x: -x["risk_score"]):
        status_str = ", ".join([f"{k}: {v}" for k, v in f["review_status_counts"].items()])
        md.append(f"| [{f['dataset_id']}](file:///{f['path']}) | {f['question_count']} | {f['risk_score']} | {f['issue_counts'].get('banned_template_phrase', 0)} | {f['issue_counts'].get('repeated_option_segment', 0)} | {status_str} |")
    md.append("\n")
    
    md.append("### B. 需要修正重複段落的考卷（僅含有重複選項段落）\n")
    md.append("這類考卷沒有 AI 範本句，但在同一個題目中的多個選項間複製了相同的疾病總論或解析段落。需要修正選項細節。")
    md.append("| 考卷路徑 | 題數 | 風險分數 | 重複段落數 | 審查狀態 |")
    md.append("| --- | --- | --- | --- | --- |")
    for f in sorted(only_repeated_files, key=lambda x: -x["risk_score"]):
        status_str = ", ".join([f"{k}: {v}" for k, v in f["review_status_counts"].items()])
        md.append(f"| [{f['dataset_id']}](file:///{f['path']}) | {f['question_count']} | {f['risk_score']} | {f['issue_counts'].get('repeated_option_segment', 0)} | {status_str} |")
    md.append("\n")
    
    md.append("### C. 完全符合品質規範的考卷（Risk Score = 0）\n")
    md.append(f"這 {len(clean_files)} 張考卷已通過 Content Trust 檢查，無任何禁用句或重覆選項段落。")
    md.append("<details><summary>點擊展開完整乾淨考卷清單</summary>\n")
    md.append("| 考卷路徑 | 題數 | 審查狀態 |")
    md.append("| --- | --- | --- |")
    for f in sorted(clean_files, key=lambda x: x["dataset_id"]):
        status_str = ", ".join([f"{k}: {v}" for k, v in f["review_status_counts"].items()])
        md.append(f"| [{f['dataset_id']}](file:///{f['path']}) | {f['question_count']} | {status_str} |")
    md.append("\n</details>\n")
    
    # Save md report to artifacts
    out_md_path = Path("C:/Users/User/.gemini/antigravity/brain/b37b9ded-3c18-4349-adc3-c70972c875f2/exam_explanation_quality_report.md")
    out_md_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_md_path, "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(md) + "\n")
        
    print(f"Generated report saved to {out_md_path}")

if __name__ == "__main__":
    main()
