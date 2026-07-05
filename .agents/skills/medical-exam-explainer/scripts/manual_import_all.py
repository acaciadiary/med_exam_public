import subprocess
import os
from pathlib import Path

def main():
    subagents = {
        "medicine-1": "384e0c09-9ce7-4786-b7b7-8e02a5fd94d7",
        "medicine-2": "1d6c5b53-5e14-486e-81b1-51e7b9ddc6b7",
        "medicine-3": "25da3133-a15b-40cf-9c2f-bc2efab6dbbe",
        "medicine-4": "0036db40-940e-4d5d-bc42-f93512e38a68",
        "medicine-5": "7f63e7c5-7966-4358-b455-357684c013e6",
        "medicine-6": "ab85b12f-0fe2-41b5-9caa-ebac0c577fd5"
    }
    
    worktrees_dir = Path(r"C:\Users\User\.gemini\antigravity\brain\575d181b-558b-484e-91cf-9773f3458a8c\.system_generated\worktrees")
    
    for subj, sid in subagents.items():
        # Find matching worktree dir
        matched_wt = None
        for wt in worktrees_dir.glob(f"subagent-{subj}-*"):
            matched_wt = wt
            break
            
        if not matched_wt:
            print(f"Error: Worktree for {subj} not found.")
            continue
            
        # Possible paths to search for done files
        search_dirs = [
            matched_wt / "scratch" / f"115-1_{subj}",
            Path(rf"C:\Users\User\.gemini\antigravity\brain\{sid}\scratch")
        ]
        
        for sd in search_dirs:
            if not sd.exists():
                continue
                
            # glob for batch_*_done.json
            for done_file in sd.glob("batch_*_done.json"):
                print(f"Found {done_file.name} in {sd}. Running import...")
                
                json_path = Path("public") / "data" / "exams" / "115-1" / f"{subj}.json"
                # We need to pass the done path. If it's outside the worktree, we pass its absolute path.
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
