import os
import json
import re

updates_dir = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\114-2_medicine-5"
source_file_path = r"d:\Antigravity\med_exam_public\public\data\exams\114-2\medicine-5.json"

banned_patterns = [
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
    "原始解析重點指出"
]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def audit():
    source_data = load_json(source_file_path)
    # create a map of source questions by question_number and question_id
    source_by_num = {q["question_number"]: q for q in source_data["questions"]}
    source_by_id = {q["id"]: q for q in source_data["questions"]}

    files = sorted([f for f in os.listdir(updates_dir) if f.endswith(".json")])
    
    total_reviewed = 0
    passed_count = 0
    passed_files = []
    failed_files = []
    
    repairs = {}
    manual_reviews = []
    
    allowed_fields = {
        "question_id", "question_number", "explanation", "key_point",
        "flashcard_front", "flashcard_back", "flashcard_summary",
        "review_status", "explanation_model", "explanation_generated_at",
        "manual_review_notes"
    }

    for file_name in files:
        file_path = os.path.join(updates_dir, file_name)
        try:
            update_data = load_json(file_path)
        except Exception as e:
            print(f"Error parsing {file_name}: {e}")
            failed_files.append(file_name)
            continue
            
        file_ok = True
        file_errors = []
        
        # Verify top-level structure
        if "updates" not in update_data:
            file_errors.append("Missing 'updates' key at root")
            file_ok = False
            failed_files.append(file_name)
            continue
            
        for update in update_data["updates"]:
            total_reviewed += 1
            q_num = update.get("question_number")
            q_id = update.get("question_id")
            
            q_errors = []
            
            # Check fields mapping with source
            if q_num not in source_by_num:
                q_errors.append(f"Question number {q_num} not found in source")
            else:
                src_q = source_by_num[q_num]
                if q_id != src_q["id"]:
                    q_errors.append(f"Question ID mismatch: update '{q_id}', source '{src_q['id']}'")
            
            # Check for forbidden fields
            extra_fields = set(update.keys()) - allowed_fields
            if extra_fields:
                q_errors.append(f"Contains forbidden fields: {list(extra_fields)}")
                
            # Check required fields
            explanation = update.get("explanation", "")
            key_point = update.get("key_point", "")
            fc_summary = update.get("flashcard_summary", "")
            fc_back = update.get("flashcard_back", "")
            
            if not explanation:
                q_errors.append("explanation field is empty")
            if not key_point:
                q_errors.append("key_point field is empty")
            if not fc_summary:
                q_errors.append("flashcard_summary field is empty")
            if not fc_back:
                q_errors.append("flashcard_back field is empty")
                
            # Check structure of explanation
            if explanation:
                has_stem = "【題幹解析】" in explanation
                has_opts = "【選項詳解】" in explanation
                has_core = "【核心考點】" in explanation
                if not (has_stem and has_opts and has_core):
                    missing = []
                    if not has_stem: missing.append("【題幹解析】")
                    if not has_opts: missing.append("【選項詳解】")
                    if not has_core: missing.append("【核心考點】")
                    q_errors.append(f"Explanation missing headers: {', '.join(missing)}")
                
                # Check options A-D individual reasons
                opts_part = ""
                if has_opts:
                    parts = explanation.split("【選項詳解】")
                    if len(parts) > 1:
                        opts_part = parts[1].split("【核心考點】")[0]
                
                # Check for duplicate descriptions in options
                opt_texts = {}
                for opt_label in ['A', 'B', 'C', 'D']:
                    pattern = rf"(?:^|[\-\*\s]+){opt_label}[\.\:\s\uFF1A\uFF0E](.*?)(?=(?:^|[\-\*\s]+)[A-D][\.\:\s\uFF1A\uFF0E]|$)"
                    match = re.search(pattern, opts_part, re.DOTALL | re.MULTILINE)
                    if match:
                        opt_texts[opt_label] = match.group(1).strip()
                    else:
                        opt_texts[opt_label] = ""
                
                # Check if options are missing or copy-pasted
                missing_opts = [k for k, v in opt_texts.items() if not v]
                if missing_opts:
                    # try another pattern
                    for opt_label in ['A', 'B', 'C', 'D']:
                        pattern = rf"(?:^|[\-\*\s]+)\(?{opt_label}\)?[\.\:\s\uFF1A\uFF0E\uFF09\u0029](.*?)(?=(?:^|[\-\*\s]+)\(?[A-D]\)?[\.\:\s\uFF1A\uFF0E\uFF09\u0029]|$)"
                        match = re.search(pattern, opts_part, re.DOTALL | re.MULTILINE)
                        if match:
                            opt_texts[opt_label] = match.group(1).strip()
                    missing_opts = [k for k, v in opt_texts.items() if not v]
                    
                if missing_opts:
                    q_errors.append(f"Could not parse or missing options: {missing_opts}")
                else:
                    # check for duplicates
                    vals = list(opt_texts.values())
                    for i in range(len(vals)):
                        for j in range(i+1, len(vals)):
                            if vals[i] == vals[j] and len(vals[i]) > 5:
                                q_errors.append(f"Options {list(opt_texts.keys())[i]} and {list(opt_texts.keys())[j]} have identical text")
                                break
                                
                # Check for banned patterns
                found_banned = []
                for pat in banned_patterns:
                    if pat in explanation:
                        found_banned.append(pat)
                if found_banned:
                    q_errors.append(f"Contains banned patterns: {found_banned}")
                    
            # Check key_point, flashcard_summary, flashcard_back for vague placeholders
            vague_words = ["最佳答案", "核心記憶點", "題幹線索", "診斷與處置原則", "定義、機轉", "此選項"]
            for field, val in [("key_point", key_point), ("flashcard_summary", fc_summary), ("flashcard_back", fc_back)]:
                found_vague = [w for w in vague_words if w in val]
                if len(val) < 5:
                    q_errors.append(f"{field} is too short ({len(val)} chars)")
                if found_vague:
                    if any(w in val for w in ["不是最佳答案", "與正確答案", "原始解析"]):
                        q_errors.append(f"{field} contains vague/banned content: {found_vague}")

            # Check manual review notes
            notes = update.get("manual_review_notes", [])
            if notes:
                manual_reviews.append((q_num, notes))
            if explanation and any(kw in explanation for kw in ["官方答案", "爭議", "疑義", "人工複核", "補充提醒"]):
                if q_num not in [m[0] for m in manual_reviews]:
                    manual_reviews.append((q_num, ["Explanation contains potential answer controversy keywords"]))

            if q_errors:
                repairs[q_num] = q_errors
                file_ok = False
                
        if file_ok:
            passed_files.append(file_name)
        else:
            failed_files.append(file_name)
            
    result = {
        "total_reviewed": total_reviewed,
        "total_passed": total_reviewed - len(repairs),
        "total_failed": len(repairs),
        "passed_files": passed_files,
        "failed_files": failed_files,
        "repairs": repairs,
        "manual_reviews": manual_reviews
    }
    
    out_path = r"d:\Antigravity\med_exam_public\scratch\audit_results.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"Audit results written to {out_path}")

if __name__ == "__main__":
    audit()
