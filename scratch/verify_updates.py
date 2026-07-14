import json
import os

files = [
    "scratch/rewrite_updates/114-2_medicine-3/q051-q060.json",
    "scratch/rewrite_updates/114-2_medicine-3/q061-q070.json",
    "scratch/rewrite_updates/114-2_medicine-3/q071-q080.json"
]

banned_phrases = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "原始解析重點指出",
    "作答時應回到題幹線索與標準答案比對",
    "定義",
    "機轉",
    "典型表現",
    "處置原則"
]

def main():
    for fpath in files:
        if not os.path.exists(fpath):
            print(f"{fpath} does not exist.")
            continue
        
        raw_bytes = open(fpath, "rb").read()
        
        # Test UTF-8
        is_utf8 = False
        try:
            raw_bytes.decode("utf-8")
            is_utf8 = True
        except UnicodeDecodeError:
            pass
            
        # Test CP950
        is_cp950 = False
        try:
            raw_bytes.decode("cp950")
            is_cp950 = True
        except UnicodeDecodeError:
            pass
            
        print(f"{fpath}: UTF-8={is_utf8}, CP950={is_cp950}")
        
        # Determine active encoding
        if is_utf8 and not is_cp950:
            encoding = "utf-8"
        elif is_cp950 and not is_utf8:
            encoding = "cp950"
        elif is_utf8 and is_cp950:
            # Can be both if it only contains ASCII
            encoding = "utf-8"
        else:
            encoding = "utf-8" # fallback
            
        # Load and scan
        try:
            content = raw_bytes.decode(encoding)
            data = json.loads(content)
            print(f"Successfully parsed as JSON using {encoding}!")
            
            # Check for banned phrases
            for up in data.get("updates", []):
                qnum = up.get("question_number")
                for k, v in up.items():
                    if isinstance(v, str):
                        for phrase in banned_phrases:
                            if phrase in v:
                                print(f"  [BANNED] Q{qnum} {k}: contains '{phrase}'")
        except Exception as e:
            print(f"Failed to parse {fpath}: {e}")

if __name__ == "__main__":
    main()
