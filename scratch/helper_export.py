import sys
import json
import os
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: python helper_export.py <subject_json_path> <batch_size>")
        sys.exit(1)
        
    json_path = Path(sys.argv[1])
    batch_size = int(sys.argv[2])
    
    if not json_path.exists():
        print(f"Error: {json_path} does not exist.")
        sys.exit(1)
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    questions = data.get("questions", [])
    subject = data.get("subject", "unknown")
    year = data.get("year", "unknown")
    
    # We want to export all questions in chunks
    chunks = [questions[i:i + batch_size] for i in range(0, len(questions), batch_size)]
    
    scratch_dir = Path("scratch") / f"{year}_{subject}"
    scratch_dir.mkdir(parents=True, exist_ok=True)
    
    manifest = {
        "year": year,
        "subject": subject,
        "total_questions": len(questions),
        "batch_size": batch_size,
        "batches": []
    }
    
    for idx, chunk in enumerate(chunks, start=1):
        batch_file = scratch_dir / f"batch_{idx:02d}_todo.json"
        batch_data = {
            "year": year,
            "subject": subject,
            "batch_id": idx,
            "questions": []
        }
        for q in chunk:
            batch_data["questions"].append({
                "id": q.get("id"),
                "question_number": q.get("question_number"),
                "question_text": q.get("question_text"),
                "options": q.get("options"),
                "correct_answer": q.get("correct_answer"),
                "category": q.get("category"),
                "explanation": q.get("explanation")  # include original just for reference
            })
            
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, ensure_ascii=False, indent=2)
            
        manifest["batches"].append({
            "batch_id": idx,
            "todo_file": str(batch_file),
            "done_file": str(scratch_dir / f"batch_{idx:02d}_done.json"),
            "question_count": len(chunk)
        })
        
    with open(scratch_dir / "manifest.json", 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        
    print(f"Exported {len(questions)} questions into {len(chunks)} batches in {scratch_dir}")

if __name__ == "__main__":
    main()
