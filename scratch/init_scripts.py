import shutil
from pathlib import Path

def main():
    skill_scripts_dir = Path(r"d:\Antigravity\med_exam_public\.agents\skills\medical-exam-explainer\scripts")
    scratch_dir = Path(r"d:\Antigravity\med_exam_public\scratch")
    scratch_dir.mkdir(parents=True, exist_ok=True)
    
    current_conv_id = "2a39f9c8-7812-4bff-9156-190a09a71256"
    
    # 1. Copy helper_export.py (no change needed)
    shutil.copy(skill_scripts_dir / "helper_export.py", scratch_dir / "helper_export.py")
    print("Copied helper_export.py")
    
    # 2. Copy and modify helper_import.py
    helper_import_content = (skill_scripts_dir / "helper_import.py").read_text(encoding="utf-8")
    # Replace qid = item.get("question_id") with qid = item.get("question_id") or item.get("id")
    helper_import_content = helper_import_content.replace(
        'qid = item.get("question_id")',
        'qid = item.get("question_id") or item.get("id")'
    )
    (scratch_dir / "helper_import.py").write_text(helper_import_content, encoding="utf-8")
    print("Copied and modified helper_import.py")
    
    # 3. Copy and modify check_progress.py
    check_progress_content = (skill_scripts_dir / "check_progress.py").read_text(encoding="utf-8")
    check_progress_content = check_progress_content.replace(
        'worktrees_dir = Path(r"C:\\Users\\User\\.gemini\\antigravity\\brain\\575d181b-558b-484e-91cf-9773f3458a8c\\.system_generated\\worktrees")',
        f'worktrees_dir = Path(r"C:\\Users\\User\\.gemini\\antigravity\\brain\\{current_conv_id}\\.system_generated\\worktrees")'
    )
    check_progress_content = check_progress_content.replace('"115-1"', '"114-1"')
    (scratch_dir / "check_progress.py").write_text(check_progress_content, encoding="utf-8")
    print("Copied and modified check_progress.py")
    
    # 4. Copy and modify manual_import_all.py (rewrite logic to be dynamic)
    manual_import_content = f"""import subprocess
import os
from pathlib import Path

def main():
    worktrees_dir = Path(r"C:\\Users\\User\\.gemini\\antigravity\\brain\\{current_conv_id}\\.system_generated\\worktrees")
    
    if not worktrees_dir.exists():
        print(f"Error: Worktrees directory {{worktrees_dir}} not found.")
        return
        
    for matched_wt in worktrees_dir.glob("subagent-medicine-*"):
        name_parts = matched_wt.name.split("-")
        if len(name_parts) < 3:
            continue
        subj = name_parts[1] + "-" + name_parts[2] # e.g. medicine-1
        
        sd = matched_wt / "scratch" / f"114-1_{{subj}}"
        if not sd.exists():
            continue
            
        for done_file in sd.glob("batch_*_done.json"):
            print(f"Found {{done_file.name}} in {{sd}}. Running import...")
            
            json_path = Path("public") / "data" / "exams" / "114-1" / f"{{subj}}.json"
            done_path = done_file.resolve()
            progress_path = Path("reports") / f"progress_{{subj}}.json"
            
            cmd = [
                "python",
                "scratch/helper_import.py",
                str(json_path),
                str(done_path),
                str(progress_path)
            ]
            
            res = subprocess.run(cmd, cwd=str(matched_wt), capture_output=True, text=True, encoding='utf-8', errors='ignore')
            print(f"Stdout: {{res.stdout.strip()}}")
            if res.returncode != 0:
                print(f"Error running import for {{subj}} {{done_file.name}}: {{res.stderr}}")
            else:
                print(f"Successfully processed {{done_file.name}} for {{subj}}")

if __name__ == "__main__":
    main()
"""
    (scratch_dir / "manual_import_all.py").write_text(manual_import_content, encoding="utf-8")
    print("Created dynamic manual_import_all.py")
    
    # 5. Copy and modify check_diff.py
    check_diff_content = (skill_scripts_dir / "check_diff.py").read_text(encoding="utf-8")
    check_diff_content = check_diff_content.replace('"public/data/exams/115-1"', '"public/data/exams/114-1"')
    check_diff_content = check_diff_content.replace('"public/data/exams/115-1/{subj}.json"', '"public/data/exams/114-1/{subj}.json"')
    (scratch_dir / "check_diff.py").write_text(check_diff_content, encoding="utf-8")
    print("Copied and modified check_diff.py")
    
if __name__ == "__main__":
    main()
