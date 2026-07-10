import json
from pathlib import Path


source = Path("public/data/exams/113-2/medicine-4.json")
data = json.loads(source.read_text(encoding="utf-8"))
out = Path("scratch/rewrite_updates/113-2_medicine-4/q061-q070.json")
out.parent.mkdir(parents=True, exist_ok=True)

updates = []
for q in data["questions"][60:70]:
    updates.append(
        {
            "question_id": q["id"],
            "question_number": q["question_number"],
            "explanation": q["explanation"],
            "key_point": q.get("key_point", ""),
            "flashcard_front": q.get("flashcard_front", ""),
            "flashcard_back": q.get("flashcard_back", ""),
            "flashcard_summary": q.get("flashcard_summary", ""),
            "review_status": "ai_generated",
            "explanation_model": "codex-high-quality-rewrite",
            "explanation_generated_at": "2026-07-09T14:00:00+08:00",
            "manual_review_notes": [],
        }
    )

payload = {
    "source_file": "public/data/exams/113-2/medicine-4.json",
    "dataset_id": "113-2_medicine-4",
    "range": {"start": 61, "end": 70},
    "updates": updates,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
