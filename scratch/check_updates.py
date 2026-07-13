import json

filepath = 'scratch/rewrite_updates/110-2_medicine-3/q041-q050.json'

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("[OK] JSON file successfully parsed!")
    print(f"Source file: {data.get('source_file')}")
    print(f"Dataset ID: {data.get('dataset_id')}")
    print(f"Range: {data.get('range')}")
    print(f"Number of questions found: {len(data.get('updates', []))}")
    
    banned_phrases = [
        "非本題答案",
        "不是本題標準答案",
        "回到題幹線索",
        "請用題幹線索連回",
        "題目中選項 A",
        "不能最精準回答",
        "最符合題幹",
        "核心記憶點",
        "定義、機轉、典型表現",
        "此選項不是最佳答案",
        "與正確答案的關鍵判斷點",
        "作答時應回到",
        "熟悉疾病機轉",
        "基本判斷能力"
    ]
    
    found_banned = False
    for u in data['updates']:
        qnum = u['question_number']
        exp = u['explanation']
        for bp in banned_phrases:
            if bp in exp:
                print(f"[FAIL] Warning: Q{qnum} contains banned phrase: '{bp}'")
                found_banned = True
                
    if not found_banned:
        print("[OK] No banned phrases found in the explanations! Excellent quality control.")
except Exception as e:
    print(f"[ERROR] Error validating file: {e}")
