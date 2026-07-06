import os
import json
from pathlib import Path

def main():
    worktrees_dir = Path(r"C:\Users\User\.gemini\antigravity\brain\2a39f9c8-7812-4bff-9156-190a09a71256\.system_generated\worktrees")
    progress = {}
    
    for i in range(1, 7):
        subj = f"medicine-{i}"
        progress[subj] = {
            "completed": 0,
            "total": 0,
            "issues": [],
            "status": "not_started"
        }
        
    if not worktrees_dir.exists():
        print(json.dumps({"error": f"Worktrees dir {worktrees_dir} not found"}, ensure_ascii=False))
        return
        
    for p in worktrees_dir.glob("subagent-explanation-writer-medicine-*"):
        name_parts = p.name.split("-")
        if len(name_parts) >= 5:
            subj = name_parts[3] + "-" + name_parts[4]  # e.g., medicine-1
            
            # 1. Read the actual json file in this worktree to get accurate completed count
            exam_file = p / "public" / "data" / "exams" / "114-1" / f"{subj}.json"
            if exam_file.exists():
                try:
                    with open(exam_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    questions = data.get("questions", [])
                    total = len(questions)
                    
                    # Count questions processed by subagents (explanation_model has 'subagent' in it)
                    completed = sum(1 for q in questions if "subagent" in str(q.get("explanation_model", "")).lower())
                    
                    progress[subj]["total"] = total
                    progress[subj]["completed"] = completed
                    if completed == total and total > 0:
                        progress[subj]["status"] = "completed"
                    elif completed > 0:
                        progress[subj]["status"] = "processing"
                except Exception as e:
                    progress[subj]["status"] = f"error_reading_json: {e}"
            
            # 2. Read the progress json file in this worktree to get any issues
            prog_file = p / "reports" / f"progress_{subj}.json"
            if prog_file.exists():
                try:
                    with open(prog_file, 'r', encoding='utf-8') as f:
                        prog_data = json.load(f)
                    progress[subj]["issues"] = prog_data.get("issues", [])
                except Exception:
                    pass
                
    print(json.dumps(progress, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
