import json
from pathlib import Path


source = Path("public/data/exams/113-2/medicine-4.json")
data = json.loads(source.read_text(encoding="utf-8"))
out = Path("scratch/rewrite_updates/113-2_medicine-4/q051-q060.json")
out.parent.mkdir(parents=True, exist_ok=True)

replacements = {
    52: [("不溫定的血漿銅藍蛋白", "不穩定的血漿銅藍蛋白")],
    59: [("負性病表不符", "負性表現不符")],
}

updates = []
for q in data["questions"][50:60]:
    n = q["question_number"]
    expl = q["explanation"]
    for old, new in replacements.get(n, []):
        expl = expl.replace(old, new)
    updates.append(
        {
            "question_id": q["id"],
            "question_number": n,
            "explanation": expl,
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
    "range": {"start": 51, "end": 60},
    "updates": updates,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
