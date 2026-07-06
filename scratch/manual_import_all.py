import subprocess
import os
from pathlib import Path

def main():
    worktrees_dir = Path(r"C:\Users\User\.gemini\antigravity\brain\2a39f9c8-7812-4bff-9156-190a09a71256\.system_generated\worktrees")
    
    if not worktrees_dir.exists():
        print(f"Error: Worktrees directory {worktrees_dir} not found.")
        return
        
    for matched_wt in worktrees_dir.glob("subagent-medicine-*"):
        name_parts = matched_wt.name.split("-")
        if len(name_parts) < 3:
            continue
        subj = name_parts[1] + "-" + name_parts[2] # e.g. medicine-1
        
        sd = matched_wt / "scratch" / f"114-1_{subj}"
        if not sd.exists():
            continue
            
        for done_file in sd.glob("batch_*_done.json"):
            print(f"Found {done_file.name} in {sd}. Running import...")
            
            json_path = Path("public") / "data" / "exams" / "114-1" / f"{subj}.json"
            done_path = done_file.resolve()
            progress_path = Path("reports") / f"progress_{subj}.json"
            
            cmd = [
                "python",
                "scratch/helper_import.py",
                str(json_path),
                str(done_path),
                str(progress_path)
            ]
            
            res = subprocess.run(cmd, cwd=str(matched_wt), capture_output=True, text=True, encoding='utf-8', errors='ignore')
            print(f"Stdout: {res.stdout.strip()}")
            if res.returncode != 0:
                print(f"Error running import for {subj} {done_file.name}: {res.stderr}")
            else:
                print(f"Successfully processed {done_file.name} for {subj}")

if __name__ == "__main__":
    main()
