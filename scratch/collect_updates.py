import shutil
from pathlib import Path

def main():
    worktrees_dir = Path(r"C:\Users\User\.gemini\antigravity\brain\9d27ddda-2782-4473-9bd8-943b58d6f4f1\.system_generated\worktrees")
    dest_dir = Path("scratch/rewrite_updates/110-1_medicine-1")
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    if not worktrees_dir.exists():
        print(f"Error: Worktrees directory {worktrees_dir} does not exist.")
        return
        
    print(f"Searching worktrees for update files...")
    
    copied_count = 0
    # Walk through each subagent directory in worktrees
    for subagent_dir in worktrees_dir.iterdir():
        if not subagent_dir.is_dir():
            continue
            
        src_path = subagent_dir / "scratch" / "rewrite_updates" / "110-1_medicine-1"
        if src_path.exists():
            for json_file in src_path.glob("*.json"):
                dest_file = dest_dir / json_file.name
                shutil.copy2(json_file, dest_file)
                print(f"Copied {json_file.name} from {subagent_dir.name}")
                copied_count += 1
                
    print(f"Collection complete. Copied {copied_count} files to {dest_dir}.")

if __name__ == "__main__":
    main()
