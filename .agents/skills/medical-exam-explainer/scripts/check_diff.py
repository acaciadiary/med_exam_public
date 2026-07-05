import json
import subprocess
import sys
from pathlib import Path

def get_git_file(filepath):
    # Retrieve the HEAD version of the file from git
    cmd = ["git", "show", f"HEAD:{filepath}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    if res.returncode != 0:
        return None
    return json.loads(res.stdout)

def main():
    dest_dir = Path("public/data/exams/115-1")
    all_ok = True
    
    for i in range(1, 7):
        subj = f"medicine-{i}"
        filepath = f"public/data/exams/115-1/{subj}.json"
        
        current_data = json.loads(Path(filepath).read_text(encoding='utf-8'))
        git_data = get_git_file(filepath)
        
        if not git_data:
            print(f"[{subj}] Warning: No git history found for comparison. Skipping check.")
            continue
            
        curr_qs = current_data.get("questions", [])
        git_qs = git_data.get("questions", [])
        
        if len(curr_qs) != len(git_qs):
            print(f"[{subj}] Error: Question count mismatch! Git: {len(git_qs)}, Current: {len(curr_qs)}")
            all_ok = False
            continue
            
        print(f"[{subj}] Comparing {len(curr_qs)} questions...")
        
        for q_idx in range(len(curr_qs)):
            cq = curr_qs[q_idx]
            gq = git_qs[q_idx]
            
            # Check immutable fields
            immutable_fields = ["id", "question_number", "question_text", "options", "correct_answer", "correct_answers", "answer_status", "answer_source", "answer_note"]
            
            for field in immutable_fields:
                if cq.get(field) != gq.get(field):
                    print(f"[{subj}] ERROR: Field '{field}' changed for question {cq.get('id')}!")
                    print(f"  Expected: {gq.get(field)}")
                    print(f"  Got     : {cq.get(field)}")
                    all_ok = False
                    
            # Check JSON structure (no missing or renamed keys except explanation updates)
            curr_keys = set(cq.keys())
            git_keys = set(gq.keys())
            
            # Subagents are allowed to add explanation fields if they were missing, but not remove or rename database metadata keys.
            removed_keys = git_keys - curr_keys
            if removed_keys:
                print(f"[{subj}] ERROR: Keys removed from question {cq.get('id')}: {removed_keys}")
                all_ok = False
                
    if all_ok:
        print("\nAll checks PASSED! No immutable fields (question text, options, correct answers, or structures) were modified.")
        sys.exit(0)
    else:
        print("\nChecks FAILED. Some immutable fields or structures were modified.")
        sys.exit(1)

if __name__ == "__main__":
    main()
