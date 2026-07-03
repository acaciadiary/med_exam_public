import json
import os

def parse_prompt(b):
    p_path = f"reports/gemini_prompts/{b}.md"
    if not os.path.exists(p_path):
        print(f"Error: {p_path} not found")
        return None
    with open(p_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find JSON input
    input_pos = content.find("請處理以下 JSON 輸入：")
    if input_pos != -1:
        start_idx = content.find('{', input_pos)
    else:
        start_idx = content.find('{')
        
    brace_count = 0
    end_idx = -1
    for i in range(start_idx, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break
    
    json_str = content[start_idx:end_idx]
    prompt_data = json.loads(json_str)
    return prompt_data

batches = [
    "110-2_medicine-3_batch-006",
    "110-2_medicine-4_batch-001",
    "110-2_medicine-4_batch-002",
    "110-2_medicine-4_batch-003",
    "110-2_medicine-4_batch-004",
    "110-2_medicine-4_batch-005"
]

out_lines = []
for b in batches:
    data = parse_prompt(b)
    if not data:
        continue
    out_lines.append(f"========================================\nBATCH: {b}\n========================================")
    out_lines.append(f"Dataset ID: {data.get('dataset_id')}")
    out_lines.append(f"Allowed Categories: {data.get('allowed_categories')}")
    out_lines.append(f"Category Group: {data.get('category_group')}")
    for q in data.get('questions', []):
        out_lines.append(f"\nQ{q.get('question_number')}: {q.get('question_id')}")
        out_lines.append(f"Text: {q.get('question_text')}")
        out_lines.append("Options:")
        for opt, val in q.get('options', {}).items():
            out_lines.append(f"  {opt}: {val}")
        out_lines.append(f"Correct: {q.get('correct_answer')}")
        if q.get('answer_note'):
            out_lines.append(f"Answer Note: {q.get('answer_note')}")
    out_lines.append("\n")

os.makedirs("scratch", exist_ok=True)
with open("scratch/assigned_questions.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print("Done writing scratch/assigned_questions.txt")
