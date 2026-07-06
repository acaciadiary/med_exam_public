import json
from pathlib import Path

def main():
    json_path = Path("public/data/exams/113-2/medicine-5.json")
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
        
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    questions = data.get("questions", [])
    
    # Core points for Q12 to Q20
    fixes = {
        12: "\n\n【核心考點】\n輕度創傷性腦出血（出血量小且無中線偏移或腦壓增高）以內科保守治療為主，不具備開顱手術適應症，重點在維持收縮壓 > 100 mmHg 及 PaCO2 正常偏低（35~40 mmHg）。",
        13: "\n\n【核心考點】\n舟形頭主要起因於矢狀縫過早融合，多屬非綜合症性的孤立病變，預後良好且罕見合併上頜骨發育不全或水腦症。",
        14: "\n\n【核心考點】\n手指遠端伸肌腱斷裂會導致遠端指間關節（DIP）無法伸直，臨床上稱為槌狀指；而近端指間關節（PIP）處的伸肌腱中央束斷裂則會導致 PIP 屈曲、DIP 過伸的鈕扣孔畸形。",
        15: "\n\n【核心考點】\nMathes-Nahai 筋膜皮瓣分類：Type A 為直接皮膚動脈供血；Type B 為肌間隔穿支供血（如橈動脈前臂皮瓣）；Type C 為肌皮穿支供血。筋膜皮瓣分類不包含 Type D。",
        16: "\n\n【核心考點】\n頸部淋巴結 Level IA（頦下區）由雙側二腹肌前腹、舌骨及正中線圍成；而 Level IB（頜下區）則由二腹肌前腹、後腹及下頜骨下緣圍成。",
        17: "\n\n【核心考點】\n口腔癌 AJCC 第八版分期：侵犯深度（DOI）> 10 mm 即使腫瘤小於 4 cm 亦會被判定為 T3；同側多發且最大徑 ≤ 6 cm 且無囊外延伸（ENE-）定義為 N2b。",
        18: "\n\n【核心考點】\n褥瘡深及骨頭、肌腱或肌肉屬於最嚴重的第四期（Stage IV）。重建手術必須在徹底清創後，首選具有良好血流與足夠厚度的局部皮瓣（如局部臀大肌皮瓣）進行覆蓋，植皮與直接縫合並不適用。",
        19: "\n\n【核心考點】\n二尖瓣閉鎖不全（MR）在左心室收縮期發生逆流，因此典型聽診雜音為心尖處最響亮且向左腋下傳導的全收縮期雜音（holosystolic murmur）。",
        20: "\n\n【核心考點】\n使用雙側內乳動脈（BIMA）會減少胸骨血供，增加術後胸骨感染裂開風險。重度肥胖（BMI > 35）、糖尿病控制差（HbA1c > 8.0%）、末期腎病以及鎖骨下動脈狹窄（雙側收縮壓差達 50 mmHg）皆為其相對禁忌症。"
    }
    
    updated_count = 0
    for q in questions:
        qnum = q.get("question_number")
        if qnum in fixes:
            exp = q.get("explanation", "")
            if "【核心考點】" not in exp:
                q["explanation"] = exp.strip() + fixes[qnum]
                updated_count += 1
                
    if updated_count > 0:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Successfully added missing '【核心考點】' to {updated_count} questions.")
    else:
        print("No missing core points were added.")

if __name__ == "__main__":
    main()
