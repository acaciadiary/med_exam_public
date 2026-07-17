import json
import os

def check():
    path = "D:\\Antigravity\\med_exam_public\\scratch\\rewrite_updates\\109-2_medicine-2\\q011-q020.json"
    if not os.path.exists(path):
        print(f"Error: {path} does not exist")
        return False
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return False
        
    print("Outer structure:")
    print(f"source_file: {data.get('source_file')}")
    print(f"dataset_id: {data.get('dataset_id')}")
    print(f"range: {data.get('range')}")
    
    updates = data.get('updates', [])
    print(f"Number of updates: {len(updates)}")
    
    forbidden_words = [
        "非本題答案",
        "不是本題標準答案",
        "回到題幹線索",
        "請用題幹線索連回",
        "題目中選項 A 所代表的鑑別或處置",
        "不能最精準回答本題",
        "最符合題幹",
        "核心記憶點",
        "定義、機轉、典型表現或處置原則",
        "標準答案所接受的判斷",
        "雖然與題目主題相關",
        "與標準答案的關鍵判斷不一致",
        "對照本題核心解析",
        "此選項不是最佳答案",
        "與正確答案的關鍵判斷點不一致"
    ]
    
    required_keys = [
        "question_id", "question_number", "explanation", "key_point",
        "flashcard_front", "flashcard_back", "flashcard_summary",
        "review_status", "explanation_model", "explanation_generated_at",
        "manual_review_notes"
    ]
    
    all_pass = True
    for idx, item in enumerate(updates):
        q_num = item.get('question_number')
        print(f"\nChecking question {q_num}:")
        
        # Check required keys
        for key in required_keys:
            if key not in item:
                print(f"  [-] Missing key: {key}")
                all_pass = False
        
        explanation = item.get('explanation', '')
        
        # Check forbidden words
        for word in forbidden_words:
            if word in explanation:
                print(f"  [-] Contains forbidden word: '{word}'")
                all_pass = False
                
        # Check structure in explanation
        if "【題幹解析】" not in explanation:
            print("  [-] Missing 【題幹解析】 in explanation")
            all_pass = False
        if "【選項詳解】" not in explanation:
            print("  [-] Missing 【選項詳解】 in explanation")
            all_pass = False
        if "【核心考點】" not in explanation:
            print("  [-] Missing 【核心考點】 in explanation")
            all_pass = False
            
    if all_pass:
        print("\nAll checks PASSED!")
    else:
        print("\nSome checks FAILED!")
        
if __name__ == '__main__':
    check()
