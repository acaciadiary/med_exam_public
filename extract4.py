import json
with open('d:\\Antigravity\\med_exam_public\\extract_q.json', encoding='utf-8') as f:
    data = json.load(f)
with open('d:\\Antigravity\\med_exam_public\\qs.md', 'w', encoding='utf-8') as f:
    for q in data:
        f.write(f"### Q{q['question_number']}: {q['question_text']}\n")
        for k, v in q['options'].items():
            f.write(f"- {k}: {v}\n")
        f.write(f"**Ans**: {q['correct_answer']}\n\n")
        f.write(f"**Original Expl**:\n{q.get('original_explanation', '')}\n\n")
