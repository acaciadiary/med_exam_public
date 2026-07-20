import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/108-1/medicine-3.json"
DATASET_ID = "108-1_medicine-3"
OUT_DIR = Path("scratch/rewrite_updates/108-1_medicine-3")
STAMP = "2026-07-20T00:00:00+08:00"

TARGET_BATCHES = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    [26, 28, 29, 30, 31, 32, 33, 34, 35],
    [40, 42, 44, 45, 46, 47, 48, 49, 51, 52],
    [53, 55, 56, 57, 58, 59, 60, 61, 62, 63],
    [64, 65, 66, 67, 68, 69, 70, 71, 72, 73],
    [74, 76, 77, 78, 80],
]


def make_explanation(analysis, options, core):
    lines = ["【題幹解析】", analysis.strip(), "", "【選項詳解】"]
    for letter in ("A", "B", "C", "D"):
        lines.append(f"- {letter}. {options[letter].strip()}")
    lines.extend(["", "【核心考點】", core.strip()])
    return "\n".join(lines)


REWRITES = {
    1: {
        "analysis": "這題考偶然發現的空蝶鞍如何處置。病人月經正常，血糖、血壓、free T4、TSH 與清晨 cortisol 都沒有顯示腦下垂體功能低下或腫瘤壓迫症狀，最適合的做法是說明良性可能性並追蹤，而不是立即治療。",
        "options": {
            "A": "經蝶鞍手術用於有壓迫症狀、腫瘤或需要病理診斷的病灶；本題只是影像偶發空蝶鞍且內分泌功能正常，沒有手術適應症。",
            "B": "放射治療用於特定殘存或復發腦下垂體腫瘤；空蝶鞍本身不是放射治療的標的。",
            "C": "Bromocriptine 主要治療泌乳素瘤或高泌乳素血症；題幹沒有月經異常、泌乳或泌乳素升高線索。",
            "D": "病人無症狀且腦下垂體軸檢查正常，最恰當是 reassurance，必要時安排後續內分泌追蹤。",
        },
        "key": "無症狀空蝶鞍且腦下垂體功能正常時，以說明與追蹤為主。",
        "front": "空蝶鞍偶發發現、內分泌正常：下一步？",
        "back": "以 reassurance 與追蹤為主；只有腫瘤、壓迫症狀或內分泌異常才考慮進一步治療。",
    },
    2: {
        "analysis": "這題考高血鈉的水分缺乏估算與矯正速度。意識不清且血鈉 160 mEq/L 時，要先估算自由水缺乏並緩慢矯正，避免血漿滲透壓下降太快造成腦水腫。",
        "options": {
            "A": "全身水量通常男性約體重 60%、女性約 50%，選項把男女比例寫反。",
            "B": "70 公斤男性的自由水缺乏約為 70 x 0.6 x (160/140 - 1)，約 6 L，不是約 5 L。",
            "C": "不易感知水分流失通常約 10 mL/kg/day，發燒、喘或高代謝時更多；5 mL/kg/day過低。",
            "D": "慢性或不確定時間的高血鈉，一般每日矯正不超過約 10 mEq/L，以降低腦水腫風險。",
        },
        "key": "高血鈉矯正要慢，通常每日下降不超過約 10 mEq/L。",
        "front": "高血鈉矯正速度",
        "back": "慢性或時間不明高血鈉應緩慢補自由水，避免每日下降超過約 10 mEq/L。",
    },
    3: {
        "analysis": "慢性腹瀉吃麵粉後加劇、貧血、低鈣與 IgA anti-tissue transglutaminase 陽性，組合最符合麩質敏感性腸病變，也就是 celiac disease。",
        "options": {
            "A": "Irritable bowel syndrome 可有腹瀉與腹痛，但不會造成 anti-tTG IgA 陽性、貧血或低鈣等吸收不良證據。",
            "B": "Celiac disease 由麩質誘發小腸絨毛萎縮，會有腹瀉、缺鐵性貧血、低鈣，且 anti-tTG IgA 是重要檢驗線索。",
            "C": "嗜酸性胃腸炎常與過敏、嗜酸球增加或腸壁浸潤相關，題幹重點是麵粉誘發與 celiac 血清學陽性。",
            "D": "Crohn disease 可有腹瀉與吸收不良，但常見腹痛、體重下降、肛周病灶或發炎指標，anti-tTG IgA 不是其典型診斷依據。",
        },
        "key": "慢性腹瀉加麩質誘發且 anti-tTG IgA 陽性，優先診斷 celiac disease。",
        "front": "麵粉後腹瀉、anti-tTG IgA 陽性",
        "back": "最符合 celiac disease，常合併吸收不良造成貧血與低鈣。",
    },
    4: {
        "analysis": "這題考瓣膜病的病因、雜音與血流動力學。二尖瓣狹窄的典型原因仍是風濕性心臟病，病程常延遲多年才表現。",
        "options": {
            "A": "二尖瓣狹窄最常見原因是風濕性慢性發炎，常在中年女性被診斷，臺灣隨風濕熱減少而病例下降，敘述正確。",
            "B": "Marfan 可造成主動脈根部擴張與主動脈瓣逆流，但嚴重主動脈逆流常使主動脈瓣關閉聲變小，不是 S2 變大聲。",
            "C": "急性中重度瓣膜逆流合併心衰竭時，可用血管擴張劑作為穩定病況的橋接治療，並非不應使用。",
            "D": "單純二尖瓣狹窄主要使左心房與肺靜脈壓上升，左心室舒張末壓通常不會像主動脈瓣狹窄那樣升高。",
        },
        "key": "二尖瓣狹窄典型病因是風濕性心臟病，血流瓶頸在左心房到左心室之間。",
        "front": "二尖瓣狹窄常見原因",
        "back": "風濕性慢性發炎最典型；單純 MS 主要升高左心房壓，不一定升高 LVEDP。",
    },
    5: {
        "analysis": "這題依心電圖判讀 WPW 旁道位置；題庫文字未保留圖像，只能依官方答案說明。官方答案為左側側壁旁道，通常要看 delta wave 與胸前導程、肢導程極性來定位。",
        "options": {
            "A": "右心室側壁旁道會呈現不同的 delta wave 與 QRS 軸向；依官方圖像判讀並非此位置。",
            "B": "左側側壁旁道常由特定導程的 delta wave 極性支持；本題官方答案採此定位。",
            "C": "前中膈旁道較接近 His-Purkinje 區域，心電圖表現與左側側壁不同，且消融風險也不同。",
            "D": "後中膈旁道常有下壁導程負向 delta wave 等線索；本題官方判讀不是後中膈。",
        },
        "key": "WPW 旁道定位需依 delta wave 與各導程 QRS 極性判讀；本題官方圖像指向左側側壁。",
        "front": "WPW 旁道定位：左側側壁",
        "back": "依 ECG delta wave 極性定位；本題圖像官方答案為 left lateral accessory pathway。",
    },
    6: {
        "analysis": "慢性腎臟病老人疲倦無力，心電圖題最常考高血鉀的 peaked T wave、PR 延長、QRS 變寬到 sine-wave 的變化；官方答案為高血鉀症。",
        "options": {
            "A": "高血鈣典型心電圖是 QT interval 縮短，與腎病患者急性危險心電圖變化的考點不同。",
            "B": "低血鈣會造成 QT interval 延長，通常不是題幹所指的高血鉀型心電圖。",
            "C": "高血鉀可造成肌肉無力、傳導變慢、尖高 T 波與 QRS 變寬，慢性腎臟病是重要危險因子。",
            "D": "低血鉀常見 ST depression、T wave flattening 與 U wave，和高血鉀的尖高 T 波方向相反。",
        },
        "key": "CKD 病人合併無力與典型 ECG 變化時，要優先想到高血鉀。",
        "front": "高血鉀 ECG",
        "back": "尖高 T 波、PR 延長、QRS 變寬；CKD 是常見背景。",
    },
    7: {
        "analysis": "病毒感染後胸痛、姿勢會影響疼痛、心肌酶與 D-dimer 正常、心超音波無局部壁運動異常且有少量心包膜積液，最符合急性心包膜炎。",
        "options": {
            "A": "急性冠心病通常較會有心肌酶上升、局部壁運動異常或典型缺血 ECG 變化；本題線索較支持心包膜發炎。",
            "B": "心肌炎可在病毒感染後發生，但常有心肌酶上升、心收縮功能下降或心律不整；題幹心臟收縮功能正常。",
            "C": "心包膜炎常有姿勢性胸痛、發炎指數上升、廣泛 ECG 變化及少量心包膜積液，與題幹最吻合。",
            "D": "肺栓塞常有呼吸困難、低氧、D-dimer 升高或右心負荷線索；本題 D-dimer 正常且有心包膜積液。",
        },
        "key": "姿勢性胸痛加心包膜積液，要優先診斷急性心包膜炎。",
        "front": "姿勢性胸痛、少量心包膜積液",
        "back": "最符合急性心包膜炎，常見於病毒感染後。",
    },
    8: {
        "analysis": "固定性第二心音分裂、右軸偏移、V1 rSR'、右心房與肺動脈擴大，代表左向右分流造成右心容量負荷，典型診斷是心房中膈缺損。",
        "options": {
            "A": "心房中膈缺損造成右心容量負荷與肺血流增加，固定性 S2 分裂是高產值體徵。",
            "B": "心室中膈缺損常有胸骨左緣全收縮期雜音，長期可肺高壓，但固定性 S2 分裂不是典型線索。",
            "C": "主動脈縮窄常見上肢高血壓、股脈延遲與上下肢壓差，不會以固定性 S2 分裂為主。",
            "D": "法洛氏四合症多在兒童期以發紺、蹲踞或右心室流出道阻塞表現，不符合此成人無發紺情境。",
        },
        "key": "固定性 S2 分裂加右心容量負荷，是 secundum ASD 的典型考點。",
        "front": "固定性 S2 分裂、V1 rSR'",
        "back": "最支持心房中膈缺損造成右心容量負荷。",
    },
    9: {
        "analysis": "Ankle-brachial index 是踝部收縮壓除以上臂收縮壓。本題 dorsalis pedis 收縮壓 90、上臂收縮壓 150，因此 ABI = 90/150 = 0.6。",
        "options": {
            "A": "ABI 以踝部收縮壓除以上臂收縮壓，90/150 等於 0.6，表示周邊動脈疾病可能性高。",
            "B": "ABI 不需要下肢舒張壓；使用收縮壓即可計算。",
            "C": "0.9 會來自錯誤分母或數字代入；本題正確計算是 0.6。",
            "D": "Dorsalis pedis artery 是 ABI 常用的踝部測量動脈之一，仍可計算。",
        },
        "key": "ABI = 踝部收縮壓 / 上臂收縮壓；本題 90/150 = 0.6。",
        "front": "ABI 計算",
        "back": "用踝部收縮壓除以上臂收縮壓，不需舒張壓。",
    },
    10: {
        "analysis": "Abdominojugular reflux 陽性代表腹部加壓後頸靜脈壓持續升高，反映右心無法處理增加的靜脈回流，常見於容量負荷或右心衰竭狀態。",
        "options": {
            "A": "Pressure overload 指壓力負荷，例如高血壓或瓣膜狹窄；本檢查主要反映靜脈回流增加後右心充盈壓上升。",
            "B": "頸靜脈明顯鼓脹代表右心充盈壓高，最符合 volume overload 或右心衰竭相關的容量問題。",
            "C": "NYHA 第四級是休息時也有症狀的功能分類，不能只靠 abdominojugular reflex 判定。",
            "D": "陽性檢查反映右側心臟壓力或容量處理能力，不等同於左側心衰竭診斷。",
        },
        "key": "Abdominojugular reflux 陽性代表右心充盈壓升高，常見於容量負荷。",
        "front": "Abdominojugular reflux 陽性",
        "back": "腹部加壓後 JVP 持續升高，提示 volume overload 或右心衰竭。",
    },
    16: {
        "analysis": "8 公分 HCC 合併主門靜脈腫瘤栓塞與多處肺轉移，已屬進展期且有肝外轉移；肝功能仍保留時，治療重點是全身性治療。",
        "options": {
            "A": "肝臟移植適用於符合 Milan criteria 等早期 HCC；大型腫瘤、門靜脈主幹侵犯與肺轉移都排除移植。",
            "B": "手術切除可考慮於局限肝內且肝功能足夠的病灶；主門靜脈腫瘤栓塞加肺轉移不是切除適應症。",
            "C": "RFA 適合小型、局部腫瘤，通常小於 3 公分效果較佳；8 公分且有遠端轉移不適合。",
            "D": "Sorafenib 是傳統考題中進展期 HCC、有血管侵犯或肝外轉移且肝功能保留時的標靶治療選項。",
        },
        "key": "HCC 有門靜脈侵犯或肝外轉移時，局部根治治療通常不適合，應考慮全身治療。",
        "front": "HCC + 主門靜脈栓塞 + 肺轉移",
        "back": "屬進展期 HCC；傳統考點選 sorafenib 等全身性標靶治療。",
    },
    17: {
        "analysis": "肝腎症候群是晚期肝病造成腎血管收縮與功能性腎衰竭，常與腹水、有效循環血量不足有關；治療可用白蛋白合併血管收縮劑，根本治療仍是肝移植。",
        "options": {
            "A": "第一型 HRS 是快速惡化、預後差；第二型較慢性且常與難治性腹水相關，選項把兩型特徵顛倒。",
            "B": "HRS 常發生在有腹水的肝硬化病人，不是通常沒有腹水。",
            "C": "Terlipressin 可收縮內臟血管、改善有效循環血量，常與 albumin 併用治療 HRS。",
            "D": "HRS 主要是功能性腎衰竭，肝移植後腎功能可能改善，因此不能說移植也不會改善。",
        },
        "key": "HRS 治療可用 terlipressin 加 albumin；根本治療是肝移植。",
        "front": "肝腎症候群治療",
        "back": "血管收縮劑如 terlipressin 加 albumin 可改善；肝移植可逆轉部分病例。",
    },
    18: {
        "analysis": "IBD 在年輕成人有發病高峰，亞洲已開發國家的發生率近年上升；早期抗生素暴露也被認為會增加未來 IBD 風險。闌尾切除的保護效果主要針對潰瘍性大腸炎，不是同時降低 UC 與 Crohn。",
        "options": {
            "A": "1 與 2 正確，但漏掉嬰兒期抗生素暴露增加 IBD 風險的第 3 點。",
            "B": "1、2、3 都是正確敘述；第 4 點把 appendectomy 對 UC 的保護效果過度套用到 Crohn disease。",
            "C": "第 2 點正確，但第 4 點不正確，且漏掉第 1、3 點。",
            "D": "第 4 點錯在 appendectomy 並不能顯著降低 UC 與 Crohn 兩者風險，因此不可全選。",
        },
        "key": "IBD 常在年輕成人發病、亞洲上升；appendectomy 的保護關聯主要是 UC，不是 Crohn。",
        "front": "IBD 流行病學與 appendectomy",
        "back": "20-40 歲常見、亞洲增加、早期抗生素暴露增風險；appendectomy 不同時保護 UC 和 Crohn。",
    },
    19: {
        "analysis": "大腸癌常早期無症狀；右側病灶較容易慢性隱性出血而造成缺鐵性小球性貧血，左側或直腸病灶較常排便習慣改變或阻塞症狀。",
        "options": {
            "A": "選項把左右側症狀顛倒；右側常以貧血表現，左側較常排便異常或腸阻塞。",
            "B": "第一期大腸癌常沒有症狀，不能因腫瘤在腸道內就認為早期很容易出血有症狀。",
            "C": "近年右側癌比例有增加趨勢，但不能說顯著多於左側大腸與直腸癌個案。",
            "D": "大腸癌慢性出血造成缺鐵性貧血，典型為小球性、低色素性貧血。",
        },
        "key": "大腸癌慢性出血常造成缺鐵性小球性貧血，尤其右側病灶可較隱匿。",
        "front": "大腸癌貧血型態",
        "back": "慢性失血導致缺鐵性小球性貧血；右側較常以貧血表現。",
    },
    20: {
        "analysis": "Zollinger-Ellison syndrome 是 gastrinoma 分泌 gastrin 造成胃酸過多、難治性潰瘍、逆流性食道炎與腹瀉，並與 MEN1 有關。",
        "options": {
            "A": "Gastrinoma 不是胰島 beta cell tumor；beta cell 分泌 insulin，gastrin 來自 G cell 或神經內分泌腫瘤。",
            "B": "ZES 在消化性潰瘍中少見，約 0.1-1%，由 gastrinoma 引起，且可與 MEN type 1 相關。",
            "C": "腹瀉是 ZES 重要表現，來自胃酸過多造成腸黏膜刺激與脂肪吸收不良，不算相當罕見。",
            "D": "Gastrinoma 可為惡性且可能轉移，尤其散發型或較大腫瘤，不能說罕有惡性可能。",
        },
        "key": "ZES = gastrinoma 分泌 gastrin，造成難治潰瘍、腹瀉，並與 MEN1 相關。",
        "front": "Zollinger-Ellison syndrome",
        "back": "Gastrinoma 導致高胃酸；可見難治潰瘍、腹瀉，與 MEN1 有關。",
    },
    21: {
        "analysis": "這題考胰臟癌危險因子與檢驗治療限制。抽菸是明確可修正危險因子，約占相當比例；遺傳、腫瘤標記與晚期治療都不能被過度誇大。",
        "options": {
            "A": "抽菸是胰臟癌重要危險因子，約 20-25% 病例與抽菸有關，敘述正確。",
            "B": "家族或胚系突變只占少數胰臟癌，不是 80% 以上都有遺傳傾向。",
            "C": "CA19-9 和 CEA 不適合作一般篩檢，敏感度與陽性預測值不足，且 CA19-9 可受膽道阻塞影響。",
            "D": "晚期轉移胰臟癌的單用 gemcitabine 效果有限，一年存活率不會高到 70%；現代常依體能考慮 FOLFIRINOX 或 gemcitabine 加 nab-paclitaxel。",
        },
        "key": "胰臟癌重要危險因子包括抽菸；CA19-9 不能作一般篩檢。",
        "front": "胰臟癌與抽菸、CA19-9",
        "back": "抽菸約與 20-25% 病例相關；CA19-9 不適合一般族群篩檢。",
    },
    22: {
        "analysis": "慢性腎病肌酸酐 6.3 mg/dL 時，常見鉀排泄下降、高磷、活性維生素 D 減少造成低鈣；高血鈉不是 CKD 最典型或最常見的酸鹼電解質異常。",
        "options": {
            "A": "鈉 148 mEq/L 為高血鈉，CKD 並不典型造成高血鈉，除非有水分攝取不足或水分流失等其他因素，因此最少見。",
            "B": "鉀 5.6 mEq/L 是高血鉀，腎排鉀能力下降時常見。",
            "C": "磷 5.5 mg/dL 是高磷血症，腎臟排磷下降時常見。",
            "D": "鈣 8.0 mg/dL 偏低，CKD 因活性維生素 D 不足與高磷可造成低鈣。",
        },
        "key": "進階 CKD 常見高鉀、高磷、低鈣；高血鈉相對少見。",
        "front": "CKD 常見電解質",
        "back": "高鉀、高磷、低鈣常見；高血鈉通常不是 CKD 本身典型表現。",
    },
    23: {
        "analysis": "透析病人磷高、鈣也高、PTH 不高，重點是控制高磷且避免再提高鈣或過度抑制副甲狀腺。最適合使用磷結合劑，臨床上會偏向非鈣型磷結合劑。",
        "options": {
            "A": "磷結合劑可降低腸道磷吸收，是高磷血症的核心治療；因鈣已高，實務上會避免鈣型製劑。",
            "B": "維他命 D3 會增加鈣磷吸收並抑制 PTH；本題鈣高且 PTH 不高，不適合。",
            "C": "擬鈣劑用於次發性副甲狀腺亢進、PTH 偏高者；本題 PTH 88 pg/mL 並不高。",
            "D": "高鈣透析液會增加血鈣，病人已有高鈣，不是合適處置。",
        },
        "key": "透析病人高磷合併高鈣、PTH 不高時，優先降磷且避免再升高鈣。",
        "front": "透析高磷、高鈣、PTH 不高",
        "back": "使用磷結合劑，通常偏向非鈣型；避免維生素 D、擬鈣劑或高鈣透析液。",
    },
    24: {
        "analysis": "腎移植後 3 個月新發高血糖，考 tacrolimus 造成 post-transplant diabetes mellitus。Calcineurin inhibitor 可傷害胰島 beta cell 分泌並增加糖尿病風險。",
        "options": {
            "A": "Mycophenolate mofetil 主要副作用是腸胃不適、骨髓抑制與感染風險，較不是移植後糖尿病主因。",
            "B": "Tacrolimus 是移植後新發糖尿病的重要藥物原因，與胰島 beta cell 毒性及胰島素分泌下降有關。",
            "C": "Sirolimus 可造成高血脂、傷口癒合不良等問題，也可能影響代謝，但本題最典型答案是 tacrolimus。",
            "D": "Everolimus 屬 mTOR inhibitor，代謝副作用以高血脂等較常考，移植後糖尿病最典型仍是 tacrolimus。",
        },
        "key": "Tacrolimus 是移植後新發糖尿病的高產值藥物原因。",
        "front": "腎移植後新發糖尿病",
        "back": "最常考 tacrolimus，因 calcineurin inhibitor 影響 beta cell 與胰島素分泌。",
    },
    25: {
        "analysis": "嘔吐造成胃酸與氯離子流失，常見 chloride-responsive metabolic alkalosis 與體液不足；此時尿氯最能反映是否為嘔吐造成的腎前性低血容量狀態。",
        "options": {
            "A": "FeNa 可用於部分 AKI 鑑別，但在嘔吐造成代謝性鹼中毒時，腎臟可能因 bicarbonaturia 帶出鈉，使 FeNa 判讀失真。",
            "B": "尿液與血漿尿素比可反映尿素再吸收，但特異性不如尿氯直接對應嘔吐造成的氯缺乏。",
            "C": "Fractional excretion of chloride 或尿氯在嘔吐相關低血容量與代謝性鹼中毒時最有用，低尿氯支持腎前性原因。",
            "D": "尿滲透壓可反映 ADH 作用與濃縮能力，但不能像氯排泄那樣直接區分嘔吐相關體液不足。",
        },
        "key": "嘔吐合併代謝性鹼中毒時，尿氯比尿鈉更可靠。",
        "front": "嘔吐 AKI：prerenal vs intrinsic",
        "back": "看 fractional excretion of chloride 或尿氯；嘔吐時 FeNa 可能被 bicarbonaturia 影響。",
    },
    26: {
        "analysis": "題目問最少發生 eosinophilia。藥物性間質性腎炎、膽固醇栓塞與部分血管炎可見嗜酸球增加；microscopic polyangiitis 是 ANCA 相關小血管炎，典型不是嗜酸球增多。",
        "options": {
            "A": "Microscopic polyangiitis 典型是 pauci-immune crescentic GN 與肺腎症候群，嗜酸球增多不是其主要特徵。",
            "B": "Atheroembolic disease 可有 eosinophilia、低補體、 livedo reticularis 與腎功能惡化。",
            "C": "NSAID 誘發間質性腎炎屬藥物過敏相關腎損傷，可合併嗜酸球增多或嗜酸球尿。",
            "D": "Polyarteritis nodosa 為中小動脈壞死性血管炎，有時可伴隨過敏或嗜酸球增加；相較之下 MPA 更不典型。",
        },
        "key": "ANCA 相關 microscopic polyangiitis 不是 eosinophilia 的典型血管炎；要和 EGPA 區分。",
        "front": "AKI + eosinophilia 鑑別",
        "back": "藥物性 AIN、膽固醇栓塞常見；MPA 最不典型。",
    },
    28: {
        "analysis": "年輕人服用 NSAID 後迅速出現大量蛋白尿、低白蛋白、高血脂與水腫，尿中血尿很少，這是腎病症候群；NSAID 可誘發 minimal change disease。",
        "options": {
            "A": "HUS 會有微血管溶血性貧血、血小板低下與急性腎損傷，題幹沒有血小板低或溶血線索。",
            "B": "Minimal change disease 可在 NSAID 後出現，典型是大量蛋白尿、低白蛋白、高脂血症與明顯水腫。",
            "C": "RPGN 通常是腎炎症候群，會有明顯血尿、紅血球圓柱、腎功能快速惡化，蛋白尿不會是唯一主軸。",
            "D": "IgA nephropathy 常在上呼吸道感染後出現肉眼血尿或顯微血尿，與本題 NSAID 後腎病症候群不合。",
        },
        "key": "NSAID 後大量蛋白尿與腎病症候群，要想到 minimal change disease。",
        "front": "NSAID 後 nephrotic syndrome",
        "back": "大量蛋白尿、低白蛋白、高血脂、水腫，最符合 minimal change disease。",
    },
    29: {
        "analysis": "高尿酸血症可來自嘌呤生成增加或尿酸排泄下降。HPRT 缺陷會使 purine salvage 受阻、de novo purine synthesis 增加，造成高尿酸血症，且 HPRT 位於 X 染色體。",
        "options": {
            "A": "HPRT 基因位在 X 染色體，缺陷可造成 Lesch-Nyhan 或 Kelley-Seegmiller spectrum，因嘌呤代謝異常而高尿酸。",
            "B": "尿酸主要經腎臟排泄，肝功能不全不是高尿酸血症的主要機制。",
            "C": "利尿劑會降低腎臟尿酸排泄而升高尿酸，尤其 thiazide 與 loop diuretics 常見。",
            "D": "AML 化療可能造成 tumor lysis 高尿酸，預防常用 allopurinol、febuxostat 或 rasburicase，不是 benzbromarone 作首選預防。",
        },
        "key": "HPRT 缺陷是 X-linked purine salvage 問題，會造成高尿酸血症。",
        "front": "HPRT 缺陷與高尿酸",
        "back": "HPRT 位於 X 染色體；缺陷使嘌呤生成增加，導致高尿酸。",
    },
    30: {
        "analysis": "題目問錯誤敘述。CPPD 的急性發作像痛風，但典型好發於老人，常侵犯膝、腕等大關節；不是常發生在年輕男性。",
        "options": {
            "A": "CPPD 急性發作又稱 pseudogout，臨床可像急性痛風，因此需要關節液結晶分析鑑別。",
            "B": "CPPD 典型好發於老年人，與退化、血色素沉著症、副甲狀腺亢進等相關；說常發生於年輕男性是錯誤敘述。",
            "C": "Calcium apatite deposition 可在慢性腎衰竭與高磷血症背景下較常見，敘述合理。",
            "D": "結晶誘發的急性關節炎可用 NSAID、colchicine 或 glucocorticoid 等方式控制發炎，敘述可接受。",
        },
        "key": "CPPD pseudogout 典型是老人急性關節炎，不是年輕男性常見病。",
        "front": "CPPD 好發族群",
        "back": "Pseudogout 多見於老年人；急性表現可模仿痛風。",
    },
    31: {
        "analysis": "多發性肌炎是發炎性肌病的一種，但許多疾病或藥物可造成類似近端肌無力與 CK 上升；statin 是重要鑑別。",
        "options": {
            "A": "Statin 可造成肌痛、肌炎樣表現，甚至免疫媒介壞死性肌病，臨床可類似 polymyositis。",
            "B": "50 歲以上發炎性肌病常需考慮 inclusion body myositis、皮肌炎或惡性腫瘤相關肌病；polymyositis 不是最常見診斷。",
            "C": "關節攣縮不是 polymyositis 的典型常見表現，較需考慮其他肌病或長期失用狀態。",
            "D": "皮下鈣化較典型見於 juvenile dermatomyositis，不是 polymyositis 的常見特徵。",
        },
        "key": "Statin 可造成類 polymyositis 表現；年長肌病要想到 inclusion body myositis 等鑑別。",
        "front": "Polymyositis 與 statin",
        "back": "Statin 可引起肌炎樣表現或免疫媒介壞死性肌病。",
    },
    32: {
        "analysis": "顳動脈炎即 giant cell arteritis，屬大中型血管炎，好發 50 歲以上，常與 polymyalgia rheumatica 共病，需及早類固醇以避免失明。",
        "options": {
            "A": "Giant cell arteritis 侵犯大中型動脈，特別是顱外頸動脈分支，不屬於中小型血管炎。",
            "B": "顳動脈炎常與風濕性多肌痛一起發生，病人可有肩臀帶疼痛與晨僵。",
            "C": "此病幾乎都見於 50 歲以上，20-40 歲女性不是典型族群。",
            "D": "對高劑量類固醇通常反應良好，且疑似時應盡快治療以保護視力。",
        },
        "key": "顳動脈炎是 50 歲以上大中型血管炎，常合併 PMR，類固醇反應佳。",
        "front": "Temporal arteritis 與 PMR",
        "back": "Giant cell arteritis 常合併 polymyalgia rheumatica，需及早類固醇。",
    },
    33: {
        "analysis": "此題在資料庫為全給分題，官方接受 A、B、C、D。依臨床常規，SLE 合併持續高抗心脂抗體且已發生 DVT，最核心處置通常是長期抗凝，傳統首選 warfarin；其他選項在標準 APS 靜脈栓塞處置中有爭議，因此應保留官方全給分並提示需人工複核。",
        "options": {
            "A": "Aspirin 可用於部分高風險抗磷脂抗體陽性但未血栓病人，或作為輔助考量；但已發生 DVT 時，單用 aspirin 通常不足。",
            "B": "Warfarin 抗凝並控制 INR 約 2-3 是 APS 靜脈血栓的傳統標準治療方向，最符合臨床核心。",
            "C": "高劑量類固醇可用於 SLE 活動或災難性 APS 等特殊情境，但單純 DVT 不是以類固醇立即治療為主。",
            "D": "NOAC 在高風險 APS，特別是多重抗體陽性或動脈事件，通常不優先於 warfarin；作為本題全給分選項需視官方命題脈絡複核。",
        },
        "key": "APS 發生 DVT 時核心是抗凝；此題官方全給分，需保留答案狀態並標示臨床爭議。",
        "front": "SLE + aCL 高 + DVT",
        "back": "臨床核心為 warfarin 抗凝；本題資料庫為全給分，其他選項需人工複核官方脈絡。",
    },
    34: {
        "analysis": "HCC 的主因有地區差異。非洲與部分亞洲地區常見 aflatoxin B1 暴露合併 HBV；歐美較重視 HCV、酒精與 NASH；臺灣傳統上 HBV/HCV 重要。",
        "options": {
            "A": "Europe 與 US 的 HCC 重要因子包括 HCV、酒精與 NASH，Wilson disease 不是最主要因子，HBV 也不是該組合的最佳描述。",
            "B": "中國 HCC 的重要因子以 HBV 與 aflatoxin 等為主，不能說主要是 HCV 與 NASH。",
            "C": "非洲部分地區 HCC 與 aflatoxin B1 暴露及慢性 B 型肝炎高度相關，組合正確。",
            "D": "臺灣 HCC 傳統主要與 HBV、HCV 有關，酒精與原發性膽汁性膽管炎不是最重要組合。",
        },
        "key": "非洲 HCC 高產值病因組合是 aflatoxin B1 加慢性 HBV。",
        "front": "HCC 地區病因：Africa",
        "back": "Africa 常考 aflatoxin B1 與 hepatitis B chronic infection。",
    },
    35: {
        "analysis": "CA19-9 是胰臟癌追蹤與預後輔助指標，不是診斷必要條件，也不適合作一般篩檢；術前數值常與腫瘤負荷、期別或可切除性相關。",
        "options": {
            "A": "部分胰臟癌病人 CA19-9 不升高，Lewis antigen 陰性者也可能無法產生 CA19-9，因此不是診斷必要條件。",
            "B": "CA19-9 對一般族群陽性預測值不足，且膽道阻塞等良性狀況也會升高，不建議作篩檢。",
            "C": "術前 CA19-9 越高通常代表腫瘤負荷較大，與期別、可切除性與預後有相關。",
            "D": "術後 CA19-9 若未下降或再上升，常提示殘存、復發或預後較差，不能說與預後無關。",
        },
        "key": "CA19-9 可輔助胰臟癌分期與追蹤，但不能作診斷必要條件或一般篩檢。",
        "front": "胰臟癌 CA19-9",
        "back": "術前值與腫瘤負荷/期別相關；不適合一般篩檢，也非診斷必需。",
    },
    40: {
        "analysis": "CHOP 後出現便秘、腹脹、ileus 與指尖麻木，代表自主神經與周邊神經毒性；CHOP 中最典型造成這些副作用的是 vincristine。",
        "options": {
            "A": "Cyclophosphamide 常考骨髓抑制、出血性膀胱炎與 SIADH，不是 ileus 加指尖麻木的典型主因。",
            "B": "Adriamycin/doxorubicin 主要副作用是心肌毒性、骨髓抑制與黏膜炎，不以 ileus 為典型。",
            "C": "Prednisolone 可造成高血糖、感染風險、情緒變化與肌病，但不典型造成自主神經性腸麻痺。",
            "D": "Vincristine 抑制微小管，典型副作用是周邊神經病變、自主神經病變、便秘與麻痺性腸阻塞。",
        },
        "key": "Vincristine 的高產值毒性是周邊神經病變與麻痺性腸阻塞。",
        "front": "CHOP 後 ileus、手麻",
        "back": "想到 vincristine neurotoxicity，包括便秘、ileus 與周邊神經病變。",
    },
    42: {
        "analysis": "題目問 glioblastoma 的錯誤敘述。Temozolomide 對 MGMT promoter methylation、也就是 MGMT 被沉默的腫瘤效果較好；若 MGMT 有表現，會修復烷化劑造成的 DNA 傷害而降低療效。",
        "options": {
            "A": "Glioblastoma 預後差，即使標準治療平均存活仍常小於 2 年，敘述正確。",
            "B": "初始治療通常是最大安全切除，接續放射治療合併 temozolomide，敘述正確。",
            "C": "MGMT 有表現會修復 temozolomide 造成的 O6-methylguanine DNA 損傷，反而較抗藥；有效預測因子是 MGMT promoter methylation。",
            "D": "Bevacizumab 可用於復發 glioblastoma，能減少血管通透性與周邊水腫，並改善 progression-free survival。",
        },
        "key": "Glioblastoma 對 temozolomide 較敏感的線索是 MGMT promoter methylation，而不是 MGMT 表現增加。",
        "front": "GBM：MGMT 與 temozolomide",
        "back": "MGMT methylation 代表修復酵素被沉默，temozolomide 效果較好。",
    },
    44: {
        "analysis": "Light's criteria 用來分辨 transudate 與 exudate，需要比較肋膜液與血清的蛋白質及 LDH。其他選項混淆了肋膜液生成吸收、ADA 意義與結核培養敏感度。",
        "options": {
            "A": "肋膜液主要由 parietal pleura 的微血管產生，並由 parietal pleura 的淋巴吸收；選項把來源與吸收寫錯。",
            "B": "Light's criteria 需看 pleural fluid/serum protein ratio、pleural fluid/serum LDH ratio 與 pleural fluid LDH，因此要測 LDH 與 total protein。",
            "C": "ADA 升高，特別是淋巴球性滲出液 ADA >40-50 U/L，較支持結核性肋膜炎，不是高度懷疑淋巴瘤的典型判讀。",
            "D": "結核性肋膜積液常是免疫反應為主，肋膜液培養陽性率有限，不能說大多可培養出結核菌。",
        },
        "key": "Light's criteria 以肋膜液與血清的 protein、LDH 分辨 transudate/exudate。",
        "front": "Light's criteria",
        "back": "比較 pleural fluid 與 serum 的 protein、LDH；ADA 高較支持 TB pleuritis。",
    },
    45: {
        "analysis": "肺腺癌標靶題要分清 EGFR 與 ALK。ALK translocation 患者常較年輕、較少抽菸；EGFR 在東亞肺腺癌比例較高，而 T790M 是 EGFR TKI 抗藥機轉，不是 ALK 抗藥。",
        "options": {
            "A": "東亞肺腺癌 EGFR 突變率常約 40-50%，10-20% 比較接近西方族群或較低估。",
            "B": "第四期 EGFR 突變肺腺癌可用 EGFR TKI 控制並延長存活，但通常不是治癒。",
            "C": "ALK translocation 肺腺癌病人年齡中位數通常較整體肺腺癌年輕，常見於少抽菸者。",
            "D": "Exon 20 T790M 是 EGFR TKI 抗藥突變，不是 ALK translocation 治療後常見抗藥機轉。",
        },
        "key": "ALK translocation 肺腺癌常見於較年輕、少抽菸族群；T790M 是 EGFR 抗藥考點。",
        "front": "肺腺癌 ALK translocation",
        "back": "ALK 病人通常較年輕；EGFR T790M 不屬於 ALK 抗藥機轉。",
    },
    46: {
        "analysis": "慢性乾咳超過 8 週且胸部 X 光正常時，要先回頭找常見可逆原因；高血壓藥物中的 ACE inhibitor 是乾咳常見原因，因此問藥史最優先。",
        "options": {
            "A": "肺功能檢查可評估 asthma 或 COPD，但在有高血壓用藥史的乾咳病人，先確認 ACE inhibitor 較低成本且高產值。",
            "B": "鼻竇 X 光可評估上呼吸道咳嗽症候群，但不是本題最優先線索。",
            "C": "ACE inhibitor 可造成長期乾咳；題幹特別給高血壓用藥史，最應先詢問抗高血壓藥物。",
            "D": "24 小時食道 pH 可評估 GERD 相關咳嗽，但通常在病史與初步處置後才考慮。",
        },
        "key": "慢性乾咳且 CXR 正常，要先檢查是否使用 ACE inhibitor。",
        "front": "高血壓病人慢性乾咳",
        "back": "先問抗高血壓藥物，特別是 ACE inhibitor。",
    },
    47: {
        "analysis": "老人多年漸進性運動喘、杵狀指、雙下肺細囉音，典型指向間質性肺病，尤其肺纖維化。缺乏發燒、急性濕囉音或局部腫瘤線索。",
        "options": {
            "A": "肺纖維化常見漸進性活動喘、乾咳、杵狀指與雙側肺底 velcro-like fine crackles，最符合本題。",
            "B": "肺水腫通常較急性，常有端坐呼吸、濕囉音、心衰竭或胸部 X 光鬱血線索，不以杵狀指為主。",
            "C": "肺炎多有急性發燒、咳痰、局部濕囉音或浸潤，題幹多年病程不支持。",
            "D": "肺癌可造成咳嗽、體重減輕、咳血或局部病灶；雙側肺底細囉音加多年活動喘更像纖維化。",
        },
        "key": "肺纖維化典型表現是漸進性活動喘、杵狀指與雙側肺底細囉音。",
        "front": "老人、杵狀指、雙下肺 fine crackles",
        "back": "最符合肺纖維化或間質性肺病。",
    },
    48: {
        "analysis": "抗結核四合一藥物中，pyrazinamide 最典型造成高尿酸血症與痛風發作；ethambutol 也可能影響尿酸，但考題最常指向 pyrazinamide。",
        "options": {
            "A": "Isoniazid 常考肝炎、周邊神經病變與需補 pyridoxine，不是最典型痛風藥物。",
            "B": "Rifampin 常考橘紅色體液、肝毒性與藥物交互作用，不是最可能造成痛風者。",
            "C": "Ethambutol 可造成視神經炎，也可讓尿酸上升，但在四個選項中不如 pyrazinamide 典型。",
            "D": "Pyrazinamide 會降低尿酸排泄，最容易誘發高尿酸血症與痛風。",
        },
        "key": "Pyrazinamide 是抗結核藥中最常考的高尿酸與痛風誘發藥物。",
        "front": "抗結核藥造成痛風",
        "back": "最典型是 pyrazinamide；ethambutol可影響尿酸但不是本題最佳答案。",
    },
    49: {
        "analysis": "健康成人門診肺炎常見病原包括肺炎鏈球菌、黴漿菌與嗜血桿菌。Acinetobacter baumannii 較常見於院內感染、呼吸器相關肺炎或重症照護環境。",
        "options": {
            "A": "肺炎鏈球菌是社區型肺炎最常見典型病原之一。",
            "B": "黴漿菌是年輕或健康成人非典型社區型肺炎常見病原。",
            "C": "鮑氏不動桿菌多與院內、呼吸器、抗生素暴露或重症病人相關，對健康門診社區肺炎最不可能。",
            "D": "嗜血桿菌可造成社區型肺炎，尤其在有慢性肺病或吸菸者更常見。",
        },
        "key": "健康成人社區型肺炎最不典型的是 Acinetobacter baumannii。",
        "front": "健康成人 CAP 病原",
        "back": "S. pneumoniae、Mycoplasma、H. influenzae 可見；Acinetobacter 多屬院內重症背景。",
    },
    51: {
        "analysis": "甲狀腺髓質癌來源是濾泡旁 C 細胞，會分泌 calcitonin，並可與 MEN2 的 RET 突變相關。",
        "options": {
            "A": "濾泡上皮細胞可產生乳突癌、濾泡癌與未分化癌等，不是髓質癌來源。",
            "B": "濾泡旁 C 細胞分泌 calcitonin，是 medullary thyroid cancer 的細胞來源。",
            "C": "淋巴球細胞來源會考慮甲狀腺淋巴瘤，不是髓質癌。",
            "D": "纖維母細胞不是甲狀腺髓質癌的來源細胞。",
        },
        "key": "Medullary thyroid cancer 來自 calcitonin-producing C cells。",
        "front": "甲狀腺髓質癌來源",
        "back": "濾泡旁 C 細胞，會分泌 calcitonin，與 MEN2/RET 相關。",
    },
    52: {
        "analysis": "糖尿病分類題要抓常見型態與診斷切點。第 2 型糖尿病最常見，與肥胖、胰島素阻抗和家族遺傳相關；診斷標準不是空腹血糖 100 或 A1c 6.0%。",
        "options": {
            "A": "第 1 型糖尿病常在兒童、青少年或年輕成人發病，與自體免疫破壞 beta cell 有關；說好發 30 歲以上不精確。",
            "B": "糖尿病診斷通常是空腹血糖 >=126 mg/dL、HbA1c >=6.5%、OGTT 2 小時 >=200 或典型症狀加隨機血糖 >=200；100 與 6% 尚未達標準。",
            "C": "第 2 型糖尿病與肥胖、胰島素阻抗及家族史密切相關，是臨床最常見型態。",
            "D": "妊娠糖尿病多在懷孕中後期因胎盤荷爾蒙造成胰島素阻抗被篩出，不是好發於前 3 個月。",
        },
        "key": "第 2 型糖尿病最常見，與肥胖、胰島素阻抗與家族史相關。",
        "front": "糖尿病診斷與分類",
        "back": "DM 診斷切點：FPG >=126 或 HbA1c >=6.5；T2DM 最常見。",
    },
    53: {
        "analysis": "脂蛋白代謝題重點是 chylomicron 最大、在腸道形成並帶 apoB-48；apolipoprotein 是脂蛋白表面的蛋白質，作為結構、受體配體或酵素輔因子。",
        "options": {
            "A": "最大的脂蛋白是乳糜粒 chylomicron，不是 VLDL。",
            "B": "Apolipoprotein 是脂蛋白的重要蛋白成分，參與脂質運輸、受體辨識與酵素活化，敘述正確。",
            "C": "Chylomicron 在小腸黏膜形成並帶 apoB-48；VLDL 才主要在肝臟形成。",
            "D": "胰島素阻抗常造成三酸甘油脂上升、HDL 下降與小而密 LDL 增加，不是 HDL 上升。",
        },
        "key": "Apolipoprotein 參與脂蛋白代謝；最大脂蛋白是 chylomicron。",
        "front": "Apolipoprotein 功能",
        "back": "作為脂蛋白結構、受體配體與酵素輔因子；chylomicron 最大且源自小腸。",
    },
    55: {
        "analysis": "半年來陣發性心悸、冒汗、頭痛與血壓突然升高，是 catecholamine episodic release 的典型三聯症與高血壓表現，最需考慮嗜鉻細胞瘤。",
        "options": {
            "A": "嗜鉻細胞瘤會間歇分泌 catecholamine，造成陣發性高血壓、頭痛、心悸與冒汗，正好對應這位病人的反覆發作型症狀。",
            "B": "甲狀腺亢進可心悸怕熱體重下降，但通常不是反覆短暫劇烈血壓飆高合併頭痛冒汗的典型組合。",
            "C": "庫欣氏症多為慢性中心性肥胖、紫紋、近端肌無力與高血壓，不以陣發性 catecholamine 症狀為主。",
            "D": "原發性醛固酮過高症常見頑固高血壓與低血鉀，通常不造成陣發性頭痛冒汗心悸。",
        },
        "key": "陣發性頭痛、心悸、冒汗與高血壓，要想到嗜鉻細胞瘤。",
        "front": "陣發性高血壓三聯症",
        "back": "頭痛、心悸、冒汗，最典型是 pheochromocytoma。",
    },
    56: {
        "analysis": "人工瓣膜術後 2 個月內屬早期 prosthetic valve endocarditis，常與手術或醫療照護相關，最典型病原是 coagulase-negative staphylococci，尤其 Staphylococcus epidermidis。",
        "options": {
            "A": "Haemophilus influenzae 屬 HACEK 相關鑑別之一，但不是早期人工瓣膜心內膜炎最典型病原。",
            "B": "VRE 可見於醫療照護相關感染，但在考題中早期人工瓣膜心內膜炎最典型仍是表皮葡萄球菌。",
            "C": "肺炎鏈球菌可造成感染性心內膜炎但相對少見，且不是術後早期 PVE 的代表病原。",
            "D": "Staphylococcus epidermidis 能形成 biofilm，常污染或感染人工材料，是早期 PVE 的高產值答案。",
        },
        "key": "術後早期人工瓣膜心內膜炎最常考 Staphylococcus epidermidis。",
        "front": "早期 prosthetic valve endocarditis",
        "back": "術後 2 個月內常見 coagulase-negative staph，尤其 S. epidermidis。",
    },
    57: {
        "analysis": "導尿管相關尿路感染的預防重點是避免不必要導尿、盡早移除、無菌置放與維持密閉引流；常規抗生素或膀胱沖洗不但無益，還可能增加感染與抗藥性。",
        "options": {
            "A": "常規在尿道口塗抗生素不是最有效預防措施，也會增加抗藥與刺激風險。",
            "B": "不建議常規口服抗生素預防 CAUTI，因為效益有限且會促進抗藥菌。",
            "C": "導管材質可影響風險，但 CAUTI 最重要因素是導尿適應症、留置時間與照護技術，不是材質品質最大。",
            "D": "經尿管沖洗膀胱會破壞閉鎖系統，即使加入抗生素也可能增加感染機會，敘述正確。",
        },
        "key": "CAUTI 預防核心是少放、早拔、無菌置放與密閉引流；避免常規抗生素沖洗。",
        "front": "CAUTI 預防",
        "back": "不要常規口服/局部抗生素或膀胱沖洗；重點是減少留置與維持閉鎖系統。",
    },
    58: {
        "analysis": "Q fever 由 Coxiella burnetii 引起，可急性發燒、肺炎或肝炎，也可慢性化；有瓣膜病或人工瓣膜者最怕慢性 Q fever 心內膜炎。",
        "options": {
            "A": "臺灣可有本土 Q fever 個案，並非以境外移入為主。",
            "B": "Q fever 的紅疹並不典型，不能用皮膚紅疹作為診斷依據。",
            "C": "原有瓣膜疾病者感染 Coxiella burnetii 後可能發展為慢性心內膜炎，是重要併發症。",
            "D": "Q fever 可造成慢性感染，尤其慢性心內膜炎或血管感染，因此不是只會急性感染。",
        },
        "key": "Q fever 可慢性化並造成心內膜炎，特別是已有瓣膜病者。",
        "front": "Q fever 慢性併發症",
        "back": "Coxiella burnetii 可造成慢性心內膜炎；紅疹不典型。",
    },
    59: {
        "analysis": "乾酪性壞死肉芽腫和多核巨細胞提示結核或某些黴菌感染。肺癌化療後免疫較弱，初步應做抗酸染色、培養、特殊染色並先隔離排除開放性結核；直接給 amphotericin B 不恰當。",
        "options": {
            "A": "痰液抗酸抹片與結核菌培養可評估是否有活動性肺結核，屬合理初步處置。",
            "B": "病理切片特殊染色如 AFB、GMS/PAS 可協助分辨分枝桿菌或黴菌，合理。",
            "C": "疑似肺結核且可能具傳染性時，先隔離直到排除開放性結核是合理感染管制。",
            "D": "Amphotericin B 毒性高，且尚未確認為需此藥治療的侵襲性黴菌；在結核鑑別未完成前立即給藥最不恰當。",
        },
        "key": "乾酪性肉芽腫先做 TB/黴菌檢查與感染管制，不應未確診就直接 amphotericin B。",
        "front": "Caseating granuloma 初步處置",
        "back": "做 AFB/culture/特殊染色並隔離排除 TB；不要貿然給 amphotericin B。",
    },
    60: {
        "analysis": "HIV 進入 CD4 T cell 需要 CD4 受體與共同受體。CCR5-delta32 若兩個對偶基因都缺失，會讓 R5-tropic HIV 難以進入細胞，對感染有保護效果。",
        "options": {
            "A": "CCR2 不是經典造成 HIV 感染抵抗的 32-bp deletion 共同受體。",
            "B": "CCR5 的 32 鹼基對缺失若為同型合子，可使 CCR5 表面表現缺陷，降低 HIV 感染風險。",
            "C": "CXCR4 可作為 HIV 共同受體，常見於部分晚期病毒株，但不是 delta32 保護突變的位置。",
            "D": "CXCR6 不是本題所問的經典 HIV 32-bp deletion 保護受體。",
        },
        "key": "CCR5-delta32 homozygous 可保護宿主免於典型 R5 HIV 感染。",
        "front": "HIV co-receptor delta32",
        "back": "CCR5 兩個 allele 都有 32-bp deletion 時，R5 HIV 難以進入細胞。",
    },
    61: {
        "analysis": "馬拉松高溫環境後昏迷、痙攣、體溫 40.8°C，且已有肝腎傷害，符合 exertional heat stroke。診斷關鍵是高核心體溫合併中樞神經功能異常。",
        "options": {
            "A": "熱痙攣主要是運動後肌肉痙攣，意識通常清楚，不會有 40.8°C 昏迷與器官傷害。",
            "B": "熱衰竭可有虛弱、暈眩與體溫上升，但通常沒有嚴重中樞神經異常；本題已昏迷痙攣。",
            "C": "中暑定義為高體溫合併中樞神經異常，可伴隨橫紋肌溶解、肝腎損傷，最符合。",
            "D": "熱昏厥多為周邊血管擴張與姿勢性暈厥，體溫與器官傷害不會如此嚴重。",
        },
        "key": "Heat stroke = 高核心體溫加中樞神經異常，是急症。",
        "front": "高溫運動後昏迷、T 40.8",
        "back": "診斷中暑；關鍵是高體溫合併 CNS dysfunction。",
    },
    62: {
        "analysis": "中暑不是下視丘 set point 被前列腺素調高的發燒，而是散熱失敗造成熱傷害；因此退燒藥無效，治療重點是快速降溫與支持治療。",
        "options": {
            "A": "Acetaminophen 對中暑無效，且病人可能已有肝傷害，使用它降溫最不適宜。",
            "B": "昏迷病人需要保護呼吸道，必要時插管是合理處置。",
            "C": "運動性中暑常有脫水與循環不足，補充生理食鹽水是支持治療的一部分。",
            "D": "痙攣可用 benzodiazepine，如 lorazepam 控制，避免增加代謝產熱與傷害。",
        },
        "key": "中暑要快速物理降溫；acetaminophen 不能治療 heat stroke。",
        "front": "中暑最不適宜處置",
        "back": "不要用 acetaminophen 降溫；應快速冷卻、補液、保護呼吸道並控制痙攣。",
    },
    63: {
        "analysis": "茶色尿、尿潛血 4+ 但顯微鏡無紅血球、CK 42,700 U/L，代表橫紋肌溶解造成 myoglobinuria 與 AKI。治療重點是大量等張液維持高尿量，以沖洗肌紅蛋白。",
        "options": {
            "A": "維持尿量每小時 200-300 mL 是橫紋肌溶解常用治療目標，可降低 myoglobin 對腎小管傷害。",
            "B": "酸化尿液會增加 myoglobin 在腎小管沉積風險；若考慮尿液鹼化也是在特定情境，不是酸化。",
            "C": "每天 2,500 mL 對嚴重 rhabdomyolysis 通常不足，應依尿量與循環狀態積極補液。",
            "D": "透析用於難治高鉀、嚴重酸中毒、容量超載或尿毒症等適應症；題幹尚未顯示需立即透析。",
        },
        "key": "橫紋肌溶解治療核心是大量輸液，目標尿量約 200-300 mL/hr。",
        "front": "Rhabdomyolysis：茶色尿、CK 很高",
        "back": "積極補等張液並維持尿量 200-300 mL/hr；不要酸化尿液。",
    },
    64: {
        "analysis": "CSF 開口壓高、白血球以淋巴球為主、蛋白只輕度上升，較像病毒、結核或隱球菌等慢性/亞急性腦膜炎型態。Klebsiella pneumoniae 細菌性腦膜炎通常為嗜中性球為主、蛋白高且葡萄糖低。",
        "options": {
            "A": "HSV 可造成病毒性腦炎或腦膜腦炎，CSF 可呈淋巴球為主，因此不能排除。",
            "B": "結核性腦膜炎常有高開口壓、淋巴球為主與亞急性病程，屬可能病原。",
            "C": "Cryptococcus neoformans 常造成高開口壓與淋巴球性腦膜炎，尤其免疫低下者要考慮。",
            "D": "Klebsiella pneumoniae 屬急性化膿性細菌性腦膜炎型態，通常嗜中性球為主，與本題 CSF 最不吻合。",
        },
        "key": "淋巴球性 CSF 加高開口壓較支持 HSV、TB、Cryptococcus；Klebsiella 最不典型。",
        "front": "淋巴球性腦膜炎鑑別",
        "back": "高壓淋巴球 CSF 可見 TB/crypto/viral；Klebsiella 多為急性細菌性型態。",
    },
    65: {
        "analysis": "承上題 CSF 培養出 yeast，最典型考 cryptococcal meningitis。治療誘導期為 amphotericin B 加 flucytosine，並要找免疫低下原因與肺部或血液播散證據；echinocandin 對隱球菌與中樞感染效果差。",
        "options": {
            "A": "Amphotericin B 加 flucytosine 是 cryptococcal meningitis 的標準誘導治療。",
            "B": "隱球菌腦膜炎常與 HIV/AIDS 相關，因此 HIV screening 是必要評估。",
            "C": "胸部 X 光、血液黴菌培養與 cryptococcal antigen 可評估肺部來源與播散，合理。",
            "D": "Echinocandin 對 Cryptococcus 活性不足且中樞穿透差，用於 yeast meningitis 尤其隱球菌時是錯誤選擇。",
        },
        "key": "Cryptococcal meningitis 誘導治療是 amphotericin B 加 flucytosine，不用 echinocandin。",
        "front": "CSF yeast、腦膜炎",
        "back": "考 Cryptococcus；治療 amphotericin B + flucytosine，並篩檢 HIV。",
    },
    66: {
        "analysis": "CURB-65 評估 confusion、urea、respiratory rate、blood pressure、age。此 21 歲病人意識清楚、RR 24、血壓未達低血壓標準、年齡未滿 65，臨床低風險，可門診治療並安排追蹤。",
        "options": {
            "A": "在已知項目中 CURB-65 為低分，且年輕、意識清楚、生命徵象尚可，官方答案為不需住院、可門診治療。",
            "B": "一般病房住院通常用於較高 CURB-65 分數、低氧、共病失控或無法口服/追蹤者；題幹未達。",
            "C": "加護病房需呼吸衰竭、休克或重症肺炎標準；本題血壓與意識不支持。",
            "D": "雖然 CURB-65 包含 urea，但題幹其他四項皆低風險，考題依原則判定為門診治療，不因未抽血即完全無法判定。",
        },
        "key": "年輕 CAP 病人 CURB-65 低分且無重症線索時，可門診治療。",
        "front": "CURB-65 低風險 CAP",
        "back": "意識清楚、RR<30、BP 未達低血壓、年齡<65，通常門診治療。",
    },
    67: {
        "analysis": "運動誘發氣喘或支氣管收縮的預防，最常用是在運動前吸入短效 beta-2 agonist，可快速支氣管擴張並預防症狀。",
        "options": {
            "A": "短效吸入型 beta-2 agonist 如 albuterol，可在運動前使用，是預防運動誘發支氣管收縮的最佳選擇。",
            "B": "口服 aminophylline 副作用多、治療窗窄，已不是預防運動誘發氣喘的首選。",
            "C": "吸入型抗膽鹼劑對部分阻塞性肺病有用，但預防運動誘發氣喘效果不如 SABA。",
            "D": "Cromolyn 可有預防效果，但起效與可近性不如運動前 SABA，考題最佳答案仍是 SABA。",
        },
        "key": "運動誘發氣喘預防首選是運動前吸入 SABA。",
        "front": "Exercise-induced bronchoconstriction 預防",
        "back": "運動前使用短效吸入 beta-2 agonist。",
    },
    68: {
        "analysis": "周全性老年評估包括認知、情緒、營養與功能。MMSE 是常用認知篩檢工具，傳統切點常以 24 分以下視為異常，但要注意教育程度會影響判讀。",
        "options": {
            "A": "MMSE 可用於心智狀態評估，24 分以下常作為認知異常篩檢切點；題幹提到高中教育程度，也支持此切點可用。",
            "B": "GDS-15 常以 0-4 正常、5 分以上需注意，超過 8 分偏向較明顯憂鬱，但不能直接等同確診憂鬱症。",
            "C": "MNA 短版分數越高營養越好，低分才表示營養不良或風險；高於 10 分不是營養不良。",
            "D": "Barthel index 分數越高功能越好；31-60 分通常屬較重度依賴，不是輕度失能。",
        },
        "key": "MMSE 24 分以下常作為認知異常篩檢切點，但需考慮教育程度。",
        "front": "CGA 認知評估",
        "back": "MMSE 可用於篩檢；傳統 24 分以下視為異常。",
    },
    69: {
        "analysis": "狂犬病暴露後預防需依暴露類別給予傷口處理、免疫球蛋白與疫苗。此題採傳統 5 劑疫苗時程，第 0、3、7、14、28 天。",
        "options": {
            "A": "第 0、3、7、14、28 天共 5 次，是本題官方採用的暴露後疫苗注射時程。",
            "B": "第 0、7、14、28 天少了第 3 天劑量，不符合此題所採 5 劑時程。",
            "C": "第 0、7、28 天共 3 次不足以對應本題傳統暴露後完整時程。",
            "D": "第 0、14、28 天共 3 次也缺少早期第 3、7 天劑量，不是本題答案。",
        },
        "key": "狂犬病暴露後疫苗傳統時程為第 0、3、7、14、28 天。",
        "front": "Rabies PEP 疫苗時程",
        "back": "本題採 5 劑：第 0、3、7、14、28 天。",
    },
    70: {
        "analysis": "半年反覆胸痛，檢查排除器質性原因後仍過度擔心、持續尋醫與檢查，核心是對身體症狀的過度想法、焦慮與行為，最符合 DSM-5 身體症狀障礙症。",
        "options": {
            "A": "重度憂鬱症需以低落情緒、失去興趣、睡眠食慾與自殺意念等為核心；題幹主軸是身體症狀與就醫行為。",
            "B": "輕鬱性情感障礙症是慢性低落情緒至少 2 年，題幹沒有長期憂鬱心境主軸。",
            "C": "身體症狀障礙症強調一個或多個身體症狀伴隨過度擔心、時間精力投入與反覆求醫，最符合。",
            "D": "焦慮症範圍很廣；本題焦慮集中在身體症狀與疾病擔憂，DSM-5 最精準分類是身體症狀障礙症。",
        },
        "key": "反覆身體症狀、排除嚴重疾病後仍過度求醫，考 somatic symptom disorder。",
        "front": "檢查正常仍持續擔心身體病",
        "back": "DSM-5 最符合身體症狀障礙症。",
    },
    71: {
        "analysis": "證據層級比較中，系統性回顧與統合分析若品質良好，通常高於單一世代研究、病例對照研究與專家意見。",
        "options": {
            "A": "世代研究可提供因果時間序列與風險估計，但仍是單一觀察性研究，層級低於高品質統合分析。",
            "B": "專家意見受個人經驗影響，通常位於證據層級底部。",
            "C": "統合分析整合多個研究結果，尤其納入隨機試驗時，證據層級最高。",
            "D": "個案對照研究適合罕見疾病與回溯暴露分析，但受偏差影響較大，層級低於世代研究與統合分析。",
        },
        "key": "在列出的研究型態中，meta-analysis 的證據層級最高。",
        "front": "EBM 證據層級最高",
        "back": "高品質系統性回顧/統合分析通常高於 cohort、case-control 與 expert opinion。",
    },
    72: {
        "analysis": "題目問沒有從事基層醫療服務的單位。衛生所、社區醫療群與基層診所都直接或組織性提供基層照護；社區健康營造中心偏向健康促進與社區動員，不是基層醫療服務提供單位。",
        "options": {
            "A": "衛生所是地方公共衛生與部分基層醫療的重要據點，有提供基層服務。",
            "B": "社區健康營造中心主要做健康促進、社區參與與資源整合，不是直接從事基層醫療的單位。",
            "C": "社區醫療群由基層診所等組成，目的就是強化社區基層照護與轉診合作。",
            "D": "基層診所是最典型的第一線基層醫療服務提供者。",
        },
        "key": "社區健康營造中心偏健康促進，不是直接基層醫療服務單位。",
        "front": "臺灣社區醫療：非基層醫療服務單位",
        "back": "社區健康營造中心主要是健康促進與社區營造。",
    },
    73: {
        "analysis": "末期癌症安寧病人意識不清、臥床、極度虛弱消瘦，只能少量半固體進食時，治療目標是舒適與尊嚴。若仍可經口接受少量食物，應以病人能接受的經口進食為主，不強迫人工營養。",
        "options": {
            "A": "鼻胃管可能造成不適、嗆咳、約束與吸入風險，末期安寧情境通常不會因營養不足而常規放置。",
            "B": "周邊靜脈人工營養與水分不一定改善末期癌症生活品質，還可能造成水腫、分泌物增加或不適。",
            "C": "中央靜脈全靜脈營養侵入性高，對瀕死末期癌症通常沒有明確舒適利益。",
            "D": "繼續給予可接受的少量經口食物，符合舒適照護與病人可承受程度，是最適當作法。",
        },
        "key": "末期安寧照護的營養目標是舒適；可經口少量就不強迫管灌或 TPN。",
        "front": "末期癌症安寧營養",
        "back": "以病人可接受的經口食物為主，避免無益人工營養。",
    },
    74: {
        "analysis": "題幹為甲狀腺無痛腫大合併頸部淋巴結，且有超音波圖像。資料庫文字未保留圖，但官方答案為乳突狀癌；典型超音波線索包括低回音、微鈣化、邊緣不規則、縱向大於橫向與可疑頸部淋巴結。",
        "options": {
            "A": "甲狀腺炎常是瀰漫性變化，可有疼痛或甲狀腺功能異常，頸部淋巴結轉移樣表現不是典型。",
            "B": "乳突狀癌最常見甲狀腺癌，常可有頸部淋巴結轉移；若超音波見微鈣化或可疑結節，最支持此診斷。",
            "C": "甲狀腺瘤通常是良性濾泡性腫瘤，不應造成可疑頸部淋巴結轉移。",
            "D": "良性多發性結節多為多顆良性結節，若合併無痛頸部淋巴結與可疑超音波特徵，惡性較需優先考慮。",
        },
        "key": "甲狀腺可疑結節合併頸部淋巴結，要高度懷疑 papillary thyroid carcinoma。",
        "front": "甲狀腺結節 + 頸部淋巴結",
        "back": "超音波若有微鈣化、低回音、不規則邊緣，最支持乳突狀癌。",
    },
    76: {
        "analysis": "古柯鹼造成急性冠心症來自交感神經刺激、冠狀動脈痙攣與血栓風險。急性期避免單純 beta blocker，因可能造成 unopposed alpha stimulation，使血管收縮惡化。",
        "options": {
            "A": "Benzodiazepine 可降低交感興奮、焦慮與血壓心跳，是古柯鹼急性毒性常用處置。",
            "B": "Morphine 可止痛與減少交感反應，並非本題所問禁忌藥物。",
            "C": "Phentolamine 是 alpha blocker，可用於嚴重高血壓或血管痙攣相關情境，不是禁忌。",
            "D": "Propranolol 為非選擇性 beta blocker，急性古柯鹼冠心症中可能使 alpha 收縮無拮抗而惡化，屬禁忌考點。",
        },
        "key": "急性 cocaine-associated ACS 避免單純 beta blocker，尤其 propranolol。",
        "front": "Cocaine ACS 禁忌",
        "back": "避免 propranolol 等 beta blocker，以免 unopposed alpha vasoconstriction。",
    },
    77: {
        "analysis": "此病人有嚴重高血鉀 7.7、 bradycardia、低血壓與代謝性酸中毒。急救重點是穩定心肌、把鉀暫時移入細胞、並排鉀；快速灌注 1 L 生理食鹽水不能有效降低血鉀，CKD 病人還可能容量負荷過多。",
        "options": {
            "A": "酸中毒時給 bicarbonate 可促進鉀暫時移入細胞，對部分嚴重高血鉀病人可作輔助治療。",
            "B": "葡萄糖加胰島素能快速把鉀移入細胞，是嚴重高血鉀的核心處置之一。",
            "C": "生理食鹽水快速灌注不能可靠地把鉀移入細胞或排出體外，且 CKD 病人可能容量超載；以稀釋鉀離子作理由不恰當。",
            "D": "靜脈鈣劑可穩定心肌細胞膜，拮抗高血鉀對心臟傳導的危險影響，是急救第一步之一。",
        },
        "key": "嚴重高血鉀急救：鈣劑護心、胰島素葡萄糖移鉀、必要時 bicarbonate/透析；生理食鹽水不能稀釋治療高鉀。",
        "front": "嚴重高血鉀處置",
        "back": "IV calcium 穩定心肌，insulin/glucose 移鉀；NS 1 L 不是降鉀治療。",
    },
    78: {
        "analysis": "急性闌尾炎可有轉移痛、食慾不佳、右下腹壓痛、發燒與特殊徵象。若問敏感度，右下腹痛或壓痛最常出現；psoas sign 等特殊徵象特異度較高但敏感度低。",
        "options": {
            "A": "Psoas sign 可提示後盲腸闌尾刺激腰大肌，但不是所有闌尾炎都有，敏感度低。",
            "B": "轉移痛很有診斷價值，但並非每位病人都出現，敏感度低於右下腹痛。",
            "C": "右下腹痛/壓痛是闌尾炎最常見臨床表現之一，在列出的症狀徵象中敏感度最高。",
            "D": "發燒可出現但早期可能沒有，本題病人也無發燒，因此敏感度不高。",
        },
        "key": "闌尾炎症狀中，右下腹痛最敏感；psoas sign 較偏特異但不敏感。",
        "front": "Appendicitis 敏感度最高線索",
        "back": "右下腹痛/壓痛比 migration pain、fever、psoas sign 更敏感。",
    },
    80: {
        "analysis": "Jonsen 四主題法是臨床倫理個案分析工具，四格為 medical indications、patient preferences、quality of life、contextual features。Nonmaleficence 是倫理原則之一，但不是四主題法的格子名稱。",
        "options": {
            "A": "不傷害原則屬生物醫學倫理四原則之一，不是 Jonsen 四主題法的四個主題。",
            "B": "醫療適應症是四主題法之一，用來分析診斷、治療目標與醫療效益風險。",
            "C": "病人偏好是四主題法之一，關注病人意願、決策能力與知情同意。",
            "D": "生活品質是四主題法之一，評估治療對病人功能、痛苦與可接受生活狀態的影響。",
        },
        "key": "Jonsen 四主題法：醫療適應症、病人偏好、生活品質、脈絡因素。",
        "front": "Jonsen four boxes",
        "back": "不是 nonmaleficence；四格是 medical indications、patient preferences、quality of life、contextual features。",
    },
}


def main():
    source = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    questions = {q["question_number"]: q for q in source["questions"]}
    expected = [n for batch in TARGET_BATCHES for n in batch]
    missing = [n for n in expected if n not in REWRITES or n not in questions]
    extra = sorted(set(REWRITES) - set(expected))
    if missing or extra:
        raise SystemExit(f"coverage mismatch missing={missing} extra={extra}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for batch_index, numbers in enumerate(TARGET_BATCHES, start=1):
        updates = []
        for number in numbers:
            rewrite = REWRITES[number]
            q = questions[number]
            explanation = make_explanation(rewrite["analysis"], rewrite["options"], rewrite["key"])
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": number,
                    "explanation": explanation,
                    "key_point": rewrite["key"],
                    "flashcard_front": rewrite["front"],
                    "flashcard_back": rewrite["back"],
                    "flashcard_summary": rewrite["key"],
                    "review_status": "ai_generated",
                    "explanation_model": "codex-high-quality-rewrite",
                    "explanation_generated_at": STAMP,
                }
            )
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": min(numbers), "end": max(numbers)},
            "updates": updates,
        }
        suffix = "selected" if numbers != list(range(min(numbers), max(numbers) + 1)) else "full"
        out_path = OUT_DIR / f"batch{batch_index:02d}_q{min(numbers):03d}-q{max(numbers):03d}_{suffix}.json"
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
