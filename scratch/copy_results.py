import shutil
from pathlib import Path

def main():
    current_conv_id = "2a39f9c8-7812-4bff-9156-190a09a71256"
    worktrees_dir = Path(r"C:\Users\User\.gemini\antigravity\brain") / current_conv_id / ".system_generated" / "worktrees"
    parent_dir = Path(r"d:\Antigravity\med_exam_public")
    
    if not worktrees_dir.exists():
        print(f"Worktrees directory {worktrees_dir} not found.")
        return
        
    for i in range(1, 7):
        subj = f"medicine-{i}"
        # Search for a directory matching subagent-explanation-writer-medicine-i-*
        matched_wts = list(worktrees_dir.glob(f"subagent-explanation-writer-{subj}-*"))
        if not matched_wts:
            print(f"No worktree found for {subj}")
            continue
            
        wt = matched_wts[0]
        src_json = wt / "public" / "data" / "exams" / "114-1" / f"{subj}.json"
        dest_json = parent_dir / "public" / "data" / "exams" / "114-1" / f"{subj}.json"
        
        if src_json.exists():
            shutil.copy(src_json, dest_json)
            print(f"Copied {src_json} to {dest_json}")
            
            # Also copy progress JSON and reports
            src_progress = wt / "reports" / f"progress_{subj}.json"
            dest_progress = parent_dir / "reports" / f"progress_{subj}.json"
            if src_progress.exists():
                shutil.copy(src_progress, dest_progress)
                print(f"Copied progress for {subj}")
        else:
            print(f"Source JSON not found at {src_json}")

if __name__ == "__main__":
    main()
