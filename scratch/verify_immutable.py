import json
import subprocess
import sys
from pathlib import Path

def get_git_file(filepath):
    # Retrieve the HEAD version of the file from git
    cmd = ["git", "show", f"HEAD:{filepath}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8-sig', errors='ignore')
    if res.returncode != 0:
        return None
    return json.loads(res.stdout)

def main():
    filepath = "public/data/exams/110-1/medicine-1.json"
    
    current_data = json.loads(Path(filepath).read_text(encoding='utf-8-sig'))
    git_data = get_git_file(filepath)
    
    if not git_data:
        print("Warning: No git history found for comparison. Skipping check.")
        sys.exit(0)
        
    curr_qs = current_data.get("questions", [])
    git_qs = git_data.get("questions", [])
    
    if len(curr_qs) != len(git_qs):
        print(f"Error: Question count mismatch! Git: {len(git_qs)}, Current: {len(curr_qs)}")
        sys.exit(1)
        
    all_ok = True
    print(f"Comparing {len(curr_qs)} questions...")
    
    # 這是我們要守護的指定 79 個題號，其餘題目完全不應該有變更！
    target_qnums = {
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35, 38, 42, 44, 46, 51,
        54, 56, 58, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 72, 74, 75, 76, 77,
        78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
        96, 97, 98, 99, 100
    }
    
    for q_idx in range(len(curr_qs)):
        cq = curr_qs[q_idx]
        gq = git_qs[q_idx]
        qnum = cq.get("question_number")
        
        # 1. 檢查不可變欄位
        immutable_fields = ["id", "question_number", "question_text", "options", "correct_answer", "correct_answers", "answer_status", "answer_source"]
        
        for field in immutable_fields:
            if cq.get(field) != gq.get(field):
                print(f"ERROR: Immutable field '{field}' changed for question {qnum}!")
                print(f"  Expected: {gq.get(field)}")
                print(f"  Got     : {cq.get(field)}")
                all_ok = False
                
        # 2. 檢查未指定的題號是否被改動
        if qnum not in target_qnums:
            # 檢查 explanation 是否有任何變更
            if cq.get("explanation") != gq.get("explanation"):
                print(f"ERROR: Question {qnum} was NOT in the target list but its explanation was modified!")
                all_ok = False
                
    if all_ok:
        print("\nAll checks PASSED! No immutable fields were modified, and only the 79 target questions had explanation updates.")
        sys.exit(0)
    else:
        print("\nChecks FAILED. Some immutable fields were modified or non-target questions were changed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
