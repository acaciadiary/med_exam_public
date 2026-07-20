import json
import sys
from pathlib import Path

BANNED_PHRASES = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
    "標準答案所接受的判斷",
    "雖然與題目主題相關",
    "與標準答案的關鍵判斷不一致",
    "對照本題核心解析",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "與標準答案的關鍵判斷不一致",
    "作答時應回到題幹線索"
]

def audit_explanation(qid, explanation):
    issues = []
    
    # 1. 檢查三個基本標題
    for header in ["【題幹解析】", "【選項詳解】", "【核心考點】"]:
        if header not in explanation:
            issues.append(f"Missing header {header}")
            
    # 2. 檢查禁用模板句
    for p in BANNED_PHRASES:
        if p in explanation:
            issues.append(f"Contains banned phrase: '{p}'")
            
    # 3. 檢查選項重複內容
    # 抓出選項詳解的部分，切出 A, B, C, D
    if "【選項詳解】" in explanation:
        parts = explanation.split("【選項詳解】")[1]
        if "【核心考點】" in parts:
            parts = parts.split("【核心考點】")[0]
        
        option_lines = [line.strip() for line in parts.split("\n") if line.strip().startswith("- ")]
        
        # 如果能抓到至少三個選項，做重合段落檢查
        if len(option_lines) >= 3:
            # 檢查是否有長度大於 10 的子字串重複出現在 3 個以上的選項中
            # 這邊用比較簡單的比對方式：任兩選項之間的句字比對
            import re
            sentences = []
            for opt in option_lines:
                # 切出句子
                opt_s = re.split(r'[，。；：\(\)]', opt)
                opt_s = [s.strip() for s in opt_s if len(s.strip()) > 10]
                sentences.append(opt_s)
                
            # 檢查是否有同一個句子出現在三個選項以上
            for i in range(len(sentences)):
                for s in sentences[i]:
                    count = 1
                    for j in range(len(sentences)):
                        if i == j:
                            continue
                        # 模糊比對，如果該句子是另一個選項子句的 substring 或相似度高
                        for other_s in sentences[j]:
                            if s in other_s or other_s in s:
                                count += 1
                                break
                    if count >= 3:
                        issues.append(f"Repeated segment in multiple options: '{s}'")
                        break
    return issues

def main():
    updates_dir = Path("scratch/rewrite_updates/110-1_medicine-1")
    if not updates_dir.exists():
        print("No updates directory found.")
        sys.exit(1)
        
    all_ok = True
    for json_file in sorted(updates_dir.glob("*.json")):
        print(f"Auditing {json_file.name}...")
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"  [ERROR] Failed to parse JSON: {e}")
            all_ok = False
            continue
            
        updates = data.get("updates", [])
        for item in updates:
            qid = item.get("question_id")
            explanation = item.get("explanation", "")
            issues = audit_explanation(qid, explanation)
            
            # 檢查 key_point 或是 flashcard_summary 是否為空
            if not item.get("key_point"):
                issues.append("Empty key_point")
            if not item.get("flashcard_summary"):
                issues.append("Empty flashcard_summary")
                
            if issues:
                print(f"  [FAIL] QID {qid} ({item.get('question_number')}):")
                for iss in issues:
                    print(f"    - {iss}")
                all_ok = False
                
    if all_ok:
        print("\nAll update files PASSED the anti-AI quality gate!")
        sys.exit(0)
    else:
        print("\nSome update files FAILED the quality gate.")
        sys.exit(1)

if __name__ == "__main__":
    main()
