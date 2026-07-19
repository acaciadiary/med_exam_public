import json
import os

def validate():
    # Load update file
    update_path = 'scratch/rewrite_updates/109-2_medicine-4/q061-q070.json'
    if not os.path.exists(update_path):
        print(f"Error: Update file {update_path} does not exist!")
        return

    with open(update_path, encoding='utf-8') as f:
        upd = json.load(f)

    # Load source file
    source_file_path = 'public/data/exams/109-2/medicine-4.json'
    with open(source_file_path, encoding='utf-8') as f:
        src = json.load(f)

    src_questions = {q['id']: q for q in src['questions']}

    # Verify fields
    assert upd['source_file'] == source_file_path, f"source_file mismatch: {upd['source_file']} vs {source_file_path}"
    assert upd['dataset_id'] == '109-2_medicine-4', f"dataset_id mismatch: {upd['dataset_id']}"
    assert upd['range']['start'] == 61, f"range start mismatch: {upd['range']['start']}"
    assert upd['range']['end'] == 70, f"range end mismatch: {upd['range']['end']}"

    banned_phrases = [
        '非本題答案', '不是本題標準答案', '回到題幹線索', '請用題幹線索連回',
        '題目中選項 A 所代表的鑑別或處置', '不能最精準回答本題', '最符合題幹',
        '核心記憶點', '定義、機轉、典型表現或處置原則', '標準答案所接受的判斷',
        '雖然與題目主題相關', '與標準答案的關鍵判斷不一致', '對照本題核心解析'
    ]

    print(f"Checking {len(upd['updates'])} updates...")
    warnings_count = 0
    for u in upd['updates']:
        qid = u['question_id']
        qnum = u['question_number']
        print(f"Checking Q{qnum} ({qid})...")
        
        # Check matching in source
        if qid not in src_questions:
            print(f"  [ERROR] Question ID {qid} not found in source!")
            return
        src_q = src_questions[qid]
        if src_q['question_number'] != qnum:
            print(f"  [ERROR] Question number mismatch for {qid}: {src_q['question_number']} vs {qnum}")
            return
        if not (61 <= qnum <= 70):
            print(f"  [ERROR] Question number {qnum} out of range!")
            return
        
        # Check explanation structure
        exp = u['explanation']
        if '【題幹解析】' not in exp:
            print(f"  [ERROR] Q{qnum} missing '【題幹解析】'")
            return
        if '【選項詳解】' not in exp:
            print(f"  [ERROR] Q{qnum} missing '【選項詳解】'")
            return
        if '【核心考點】' not in exp:
            print(f"  [ERROR] Q{qnum} missing '【核心考點】'")
            return
        
        # Check banned phrases
        for phrase in banned_phrases:
            if phrase in exp:
                print(f"  [WARNING] Found banned phrase \"{phrase}\" in Q{qnum}")
                warnings_count += 1
                
        # Check repeated option segment (check if any long sentence is reused)
        # We can extract the text inside option A, B, C, D
        options_part = exp.split('【選項詳解】')[1].split('【核心考點】')[0]
        opt_lines = [line.strip() for line in options_part.split('\n') if line.strip().startswith('-')]
        
        # Look for duplicate sentences of length > 10 chars
        sentences = []
        for line in opt_lines:
            # simple sentence split
            parts = [p.strip() for p in line.replace('，', ',').replace('。', '.').replace('；', ';').split('.') if len(p.strip()) > 10]
            sentences.extend(parts)
            
        # check duplicate sentences
        seen = set()
        duplicates = set()
        for s in sentences:
            if s in seen:
                duplicates.add(s)
            else:
                seen.add(s)
                
        if duplicates:
            for dup in duplicates:
                print(f"  [WARNING] Q{qnum} has duplicated segment in options: \"{dup[:30]}...\"")
                warnings_count += 1

    print(f"Verification completed. Warnings found: {warnings_count}")

if __name__ == '__main__':
    validate()
