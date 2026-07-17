import json
import os

def main():
    json_path = r"d:\Antigravity\med_exam_public\public\data\exams\109-2\medicine-1.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions'][70:80]
    
    output_path = r"d:\Antigravity\med_exam_public\scratch\q71-80_raw.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as fout:
        for q in questions:
            fout.write(f"## Question {q['question_number']} (ID: {q['id']})\n")
            fout.write(f"**Text**: {q['question_text']}\n\n")
            fout.write("**Options**:\n")
            options = q.get('options', {})
            if isinstance(options, dict):
                for k, v in options.items():
                    fout.write(f"- {k}: {v}\n")
            elif isinstance(options, list):
                for opt in options:
                    fout.write(f"- {opt}\n")
            fout.write(f"\n**Correct Answer**: {q.get('correct_answer')}\n\n")
            fout.write(f"**Old Explanation**:\n{q.get('explanation')}\n\n")
            fout.write(f"**Old Key Point**:\n{q.get('key_point')}\n")
            fout.write(f"**Old Flashcard Front**:\n{q.get('flashcard_front')}\n")
            fout.write(f"**Old Flashcard Back**:\n{q.get('flashcard_back')}\n")
            fout.write(f"**Old Flashcard Summary**:\n{q.get('flashcard_summary')}\n")
            fout.write("="*40 + "\n\n")
            
    print(f"Dumped 10 questions to {output_path}")

if __name__ == '__main__':
    main()
