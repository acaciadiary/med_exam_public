import subprocess
import os
from pathlib import Path

def main():
    worktrees_dir = Path(r"C:\Users\User\.gemini\antigravity\brain\c8c7be1a-959c-42f9-a349-5995ea2ef29a\.system_generated\worktrees")
    
    if not worktrees_dir.exists():
        print(f"Error: Worktrees directory {worktrees_dir} not found.")
        return
        
    for matched_wt in worktrees_dir.glob("subagent-*"):
        name_lower = matched_wt.name.lower()
        subj = None
        for i in range(1, 7):
            if f"medicine-{i}" in name_lower or f"medicine {i}" in name_lower:
                subj = f"medicine-{i}"
                break
        if not subj:
            continue
        
        sd = matched_wt / "scratch" / f"114-2_{subj}"
        if not sd.exists():
            continue
            
        for done_file in sd.glob("batch_*_done.json"):
            print(f"Found {done_file.name} in {sd}. Running import...")
            
            json_path = Path("public") / "data" / "exams" / "114-2" / f"{subj}.json"
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
