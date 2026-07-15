import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/113-1/medicine-3.json"
DATASET_ID = "113-1_medicine-3"
OUT_DIR = Path("scratch/rewrite_updates/113-1_medicine-3")
STAMP = "2026-07-15T00:00:00+08:00"


DATA = {
    1: {
        "topic": "妊娠糖尿病",
        "analysis": "題目問 GDM 敘述何者最不適當。GDM 重點是 24-28 週篩檢、先以營養治療與血糖監測控制，未達標時再加藥；最常被考的陷阱是產後第二型糖尿病風險會明顯增加，不是接近一般孕婦。",
        "options": {
            "A": "24-28 週是一般風險孕婦常規篩檢 GDM 的時程，選項正確。",
            "B": "確診後先做飲食控制、運動與自我血糖監測，若達標可不需藥物，選項正確。",
            "C": "生活型態治療無法達標時可使用胰島素，部分情境也會考慮 metformin 或 glyburide 等口服藥，選項正確。",
            "D": "GDM 代表未來第二型糖尿病風險大幅升高，產後仍需追蹤糖代謝，因此說風險與未罹患 GDM 女性接近是錯誤敘述。",
        },
        "core": "GDM 的考點是篩檢時程、階梯式治療與長期代謝風險；產後糖尿病風險升高是關鍵警訊。",
        "key": "GDM 產後第二型糖尿病風險明顯上升，不能視為與一般女性相同。",
    },
    2: {
        "topic": "預後評估量表",
        "analysis": "題目要辨認量表與適用對象是否配對。APACHE II 用於 ICU 重症，IPI 用於非何杰金氏淋巴瘤，TIMI 用於急性冠心症；BODE 則是 COPD 預後量表，不是壓傷量表。",
        "options": {
            "A": "APACHE II 評估加護病房重症病人的疾病嚴重度與死亡風險，配對正確。",
            "B": "BODE 包含 BMI、氣流阻塞、呼吸困難與運動能力，用於 COPD 預後，不用來評估 pressure injury，故最不恰當。",
            "C": "International Prognostic Index 是非何杰金氏淋巴瘤常用預後工具，配對正確。",
            "D": "TIMI risk score 可用於急性冠心症風險分層，包括 NSTE-ACS，配對正確。",
        },
        "core": "臨床量表要記對族群：APACHE II 重症、BODE COPD、IPI 淋巴瘤、TIMI 急性冠心症。",
        "key": "BODE Index 是 COPD 預後量表，不是壓傷評估量表。",
    },
    3: {
        "topic": "預後量表中的年齡",
        "analysis": "承上題比較四個量表是否納入年齡。APACHE II、IPI、TIMI risk score 都有年齡相關項目；BODE Index 由 BMI、FEV1、dyspnea、6-minute walk distance 組成，沒有年齡。",
        "options": {
            "A": "只有一種納入年齡會漏掉 APACHE II、IPI 與 TIMI，數量太少。",
            "B": "兩種也仍少算一個含年齡的量表。",
            "C": "APACHE II、IPI、TIMI 三種納入年齡；BODE 不納入年齡，故共有三種。",
            "D": "四種全都納入年齡不正確，因 BODE Index 沒有年齡項目。",
        },
        "core": "BODE 的四個字母就是記憶點，沒有 age；其他三個量表才有年齡。",
        "key": "APACHE II、IPI、TIMI 含年齡，BODE 不含年齡。",
    },
    4: {
        "topic": "腎病症候群水腫",
        "analysis": "病人晨起眼瞼與臉部水腫、無端坐呼吸或夜間陣發性呼吸困難，較像低白蛋白造成的腎病症候群水腫，而非心衰竭或甲狀腺毒症。最符合的是嚴重低白蛋白血症。",
        "options": {
            "A": "NT-proBNP 2500 pg/mL 支持心衰竭，但題幹缺乏平躺喘、夜間喘醒等典型鬱血症狀，不是最符合。",
            "B": "Albumin 1.8 g/dL 可造成低膠體滲透壓與眼瞼水腫，最符合腎病症候群或嚴重蛋白流失表現。",
            "C": "TSH 9.0 可見於甲狀腺低下，但題幹沒有怕冷、便祕、黏液性水腫等主軸，且眼瞼水腫更像低白蛋白。",
            "D": "Free T4 2.8 ng/dL 指向甲狀腺毒症，通常不會造成這種低白蛋白型全身水腫。",
        },
        "core": "晨起眼瞼水腫加全身水腫要想到腎病症候群；抽血最直接線索是低白蛋白。",
        "key": "腎病症候群水腫最符合低白蛋白血症。",
    },
    5: {
        "topic": "低血鈣體徵",
        "analysis": "敲擊面神經誘發同側臉部抽動是 Chvostek sign；血壓計加壓誘發腕手痙攣是 Trousseau sign。兩者都是神經肌肉興奮性增加，典型指向低血鈣。",
        "options": {
            "A": "高血鈣較常有便祕、多尿、意識改變與 QT 縮短，不會造成 Chvostek/Trousseau sign。",
            "B": "低血鈣會增加神經肌肉興奮性，導致臉部抽動與 carpal spasm，是本題答案。",
            "C": "高血磷可伴隨低血鈣，但題目問最直接的離子異常，應選低血鈣。",
            "D": "低血磷可造成肌肉無力、橫紋肌溶解或呼吸肌無力，不是這兩個體徵的典型原因。",
        },
        "core": "Chvostek sign 與 Trousseau sign 是低血鈣的經典臨床體徵。",
        "key": "臉部抽動與腕手痙攣代表低血鈣造成神經肌肉興奮性上升。",
    },
    6: {
        "topic": "心導管壓力波形",
        "analysis": "本題考心導管壓力曲線。肥厚型阻塞性心肌症有 Brockenbrough-Braunwald-Morrow sign；心包填塞 y descent 變鈍；縮窄性心包膜炎有 dip-and-plateau 或 square root sign，且 RV 收縮壓通常不高。",
        "options": {
            "A": "Brockenbrough-Braunwald sign 典型見於肥厚型阻塞性心肌症，不是主動脈瓣狹窄；AS 的早搏後壓差邏輯不同。",
            "B": "心包填塞時右心房壓上升，但 y descent 受限而變鈍；明顯 y descent 反而較支持縮窄性心包膜炎。",
            "C": "縮窄性心包膜炎常有右心室 dip-and-plateau/square root sign，右心室收縮壓多低於 50 mmHg，敘述正確。",
            "D": "限制性心肌病可有雙心室舒張壓接近，但右心室舒張末期壓力不會高於右心室收縮壓的 1/3 這種說法不典型。",
        },
        "core": "心包填塞是 y descent 變鈍；縮窄性心包膜炎是明顯 y descent 與 square root sign。",
        "key": "縮窄性心包膜炎的心導管特徵是 square root sign。",
    },
    7: {
        "topic": "NSTE-ACS 處置",
        "analysis": "NSTE-ACS 的重點是以 troponin 判斷 NSTEMI、依風險決定侵入性治療時機。GRACE >140 屬高風險，即使暫時穩定，也應考慮早期侵入性策略。",
        "options": {
            "A": "NSTE-ACS 可有 ST depression 或 T wave inversion，但急診心電圖不一定超過半數都有新的 ST 下降；深度 T 波倒置也不是最常見表現。",
            "B": "Troponin 上升已符合心肌壞死證據，即使 CK 正常仍可診斷 NSTEMI，選項錯誤。",
            "C": "Aspirin 與 P2Y12 inhibitor 常用，但 GPIIb/IIIa inhibitor 不是所有病人例行三合一使用，需依高風險或介入情境決定。",
            "D": "血行動力穩定但 GRACE >140 仍屬高風險 NSTE-ACS，通常應在 24 小時內安排冠狀動脈攝影並考慮血流重建，敘述正確。",
        },
        "core": "NSTE-ACS 高風險指標如 GRACE >140 會推動早期侵入性治療；troponin 比 CK 更關鍵。",
        "key": "GRACE >140 的 NSTE-ACS 應考慮 24 小時內侵入性評估。",
    },
    8: {
        "topic": "核醫心肌灌流造影",
        "analysis": "題目問錯誤敘述。Tl-201 類似鉀離子，主要經 Na/K ATPase 主動攝取，半衰期約 73 小時而非 12 小時；Tc-99m sestamibi 半衰期約 6 小時，與粒線體膜電位相關。",
        "options": {
            "A": "心肌同位素攝取與血流及心肌細胞存活相關，是心肌灌流造影的基礎。",
            "B": "Tl-201 的半衰期約 73 小時，不是 12 小時；雖可有再分布現象，但此選項的半衰期與描述不正確。",
            "C": "Tc-99m sestamibi 半衰期約 6 小時，進入心肌後主要受膜電位影響而滯留，作為灌流示蹤劑可接受。",
            "D": "Tl-201 與鉀離子有相似生物學特性，會被心肌細胞主動攝取，敘述正確。",
        },
        "core": "Tl-201 像鉀、半衰期長且可再分布；Tc-99m sestamibi 半衰期約 6 小時。",
        "key": "Tl-201 半衰期不是 12 小時。",
    },
    9: {
        "topic": "左心房黏液瘤",
        "analysis": "姿勢性昏厥、全身症狀、心尖部舒張中期低頻音與中風，配合左心房腫瘤，符合左心房黏液瘤。考點是好發左心房、女性較多、手術切除為主，以及脆弱絨毛狀表面易栓塞。",
        "options": {
            "A": "心房黏液瘤女性較多，男女比例不是 3:1 男性較多。",
            "B": "治療以手術完整切除為主；術後不因復發率高而例行長期 heparin 或 NOAC 預防中風。",
            "C": "黏液瘤最常發生在左心房，通常為單發，不是大部分在右心房且常多發。",
            "D": "黏液瘤可呈絨毛狀、膠凍樣且易碎，表面碎片或血栓脫落可造成腦中風等栓塞，敘述正確。",
        },
        "core": "左心房黏液瘤會造成姿勢性瓣口阻塞與栓塞；最常在左心房，治療為手術切除。",
        "key": "黏液瘤脆弱絨毛狀表面脫落可造成全身性栓塞。",
    },
    10: {
        "topic": "心房顫動抗凝血",
        "analysis": "高齡、有高血壓與心肌梗塞病史的心房顫動病人，中風風險高，需要抗凝血。DOAC 各有劑量與反轉劑特色；dabigatran 有 idarucizumab 可作為特異性反轉劑。",
        "options": {
            "A": "此病人 CHA2DS2-VASc 分數高，不應說不需要抗凝血。",
            "B": "Dabigatran 發生危急出血或需緊急手術時，可使用 idarucizumab 反轉抗凝作用，敘述正確。",
            "C": "Apixaban 一般為一天兩次；若希望一天一次，較常想到 rivaroxaban 或 edoxaban。",
            "D": "Aspirin 不能取代抗凝血作為心房顫動中風預防，即使出血風險高也應調整風險而非改 aspirin。",
        },
        "core": "心房顫動中風預防以抗凝血為核心；dabigatran 的特異性反轉劑是 idarucizumab。",
        "key": "Dabigatran 有特異性 reversal agent idarucizumab。",
    },
    11: {
        "topic": "心雜音動態變化",
        "analysis": "題目問錯誤敘述。右心雜音通常吸氣變大，左心雜音多在吐氣較明顯；Valsalva 與站立會降低前負荷，蹲下會增加前負荷與後負荷。",
        "options": {
            "A": "Valsalva 降低靜脈回流，多數雜音包含主動脈狹窄會變短變弱，敘述正確。",
            "B": "三尖瓣逆流是右心雜音，吸氣時因回流量增加而變大聲，不是吐氣時變大聲，故錯誤。",
            "C": "站立降低前負荷，二尖瓣逆流雜音通常變小，敘述正確。",
            "D": "蹲下增加前負荷與後負荷，可減少 HOCM 左心室出口阻塞，雜音變小，敘述正確。",
        },
        "core": "右心雜音吸氣增強；HOCM 雜音在前負荷下降時變大、蹲下時變小。",
        "key": "三尖瓣逆流雜音是吸氣變大聲，不是吐氣。",
    },
    12: {
        "topic": "肥厚型心肌症",
        "analysis": "HCM 多為遺傳性肌節蛋白疾病，出生時未必已有肥厚；若有出口阻塞，治療應避免降低前負荷或後負荷，並以 beta-blocker、non-DHP CCB 等減慢心率。少數會進展為終末期擴大型表現。",
        "options": {
            "A": "HCM 進展成擴大型心肌症或終末期收縮功能不全的比例低，通常小於 10%，敘述正確。",
            "B": "多數病人不是出生時就有明顯左心室肥厚，肥厚常隨年齡發展而出現。",
            "C": "有出口阻塞時不應以血管擴張為原則，因降低後負荷可能加劇阻塞；重點是減慢心率與減少收縮力。",
            "D": "運動時血壓反應異常，尤其血壓不上升或下降，才是猝死風險線索；血壓增加 30 mmHg 不是危險因子。",
        },
        "core": "HOCM 治療避免 vasodilator 與脫水，優先減慢心率、降低收縮力。",
        "key": "HCM 只有少數會進展為擴大型心肌症。",
    },
    13: {
        "topic": "血壓測量",
        "analysis": "血壓袖帶太小會讓測量值被高估，不是低估。小腿收縮壓通常比上臂高，兩臂收縮壓差距正常多在 10 mmHg 內。",
        "options": {
            "A": "上肢與下肢血壓差異可受主動脈閉鎖不全或周邊血管疾病影響，敘述可接受。",
            "B": "小腿收縮壓通常因周邊脈波放大而比上臂高約 10-20 mmHg，敘述正確。",
            "C": "袖帶長度約手臂周徑 80%、寬度約 40% 是正確原則；但小袖帶會高估血壓，不是低估，故錯誤。",
            "D": "兩側上臂收縮壓差通常應小於或等於約 10 mmHg，若明顯較大需考慮血管病變。",
        },
        "core": "血壓袖帶太小會高估，太大會低估；袖帶大小是血壓測量常考陷阱。",
        "key": "不合適的小袖帶會明顯高估血壓。",
    },
    14: {
        "topic": "心室性心律不整與猝死",
        "analysis": "心臟猝死常與缺血性心臟病造成的 VT/VF 有關。ICD 可以終止致命心律不整、降低猝死，但 ICD shock 代表病人本身仍是高風險族群，不會使後續死亡率與心衰竭風險大幅減少。",
        "options": {
            "A": "心室性心律不整需靠心電圖、植入裝置紀錄或電生理誘發確認，敘述正確。",
            "B": "若可能，取得 12 導程心電圖有助判斷起源與潛在心臟病，敘述正確。",
            "C": "ICD 能快速終止 VT/VF，但啟動本身代表復發與心衰竭風險仍高，不代表往後死亡率大幅減少，故錯誤。",
            "D": "急性處置首要是血流動力穩定，必要時立即電擊或急救，敘述正確。",
        },
        "core": "ICD 是保護裝置，不是把高風險病人變成低風險；ICD shock 後仍需找原因與優化治療。",
        "key": "ICD 終止心律不整不代表後續死亡率與心衰竭風險大幅下降。",
    },
    15: {
        "topic": "轉胺酶大幅上升",
        "analysis": "AST/ALT 超過 1000 IU/L 常見於缺血性肝炎、急性病毒性肝炎、藥物或毒物性肝炎，也可見於嚴重自體免疫性肝炎。脂肪性肝炎通常為輕到中度升高。",
        "options": {
            "A": "自體免疫性肝炎急性發作時可有明顯轉胺酶升高，可能超過 1000。",
            "B": "缺血性肝炎常因肝臟低灌流造成 AST/ALT 急遽大幅上升，是典型原因。",
            "C": "脂肪性肝炎多為慢性輕中度轉胺酶升高，較不會出現 AST/ALT >1000，是本題答案。",
            "D": "藥物性肝炎，尤其 acetaminophen 或嚴重 DILI，可造成非常高的轉胺酶。",
        },
        "core": "AST/ALT >1000 先想缺血、毒物/藥物、急性病毒或嚴重免疫性肝炎；脂肪肝通常不會這麼高。",
        "key": "脂肪性肝炎較少造成 aminotransferase >1000 IU/L。",
    },
    16: {
        "topic": "克隆氏症治療",
        "analysis": "右下腹痛、腹瀉、體重減輕、發燒、鵝卵石樣病灶、結節性紅斑與關節痛，指向 Crohn disease。治療無效時可升級生物製劑等藥物，不是直接以手術作為下一步標準治療。",
        "options": {
            "A": "Crohn disease 與腸道菌叢、遺傳與免疫失調有關，敘述正確。",
            "B": "Crohn 可侵犯全腸胃道，跳躍性病灶與瘻管、膿瘍、狹窄是典型特徵。",
            "C": "非乾酪性肉芽腫是 Crohn 的經典病理線索，雖非每例都有。",
            "D": "5-ASA、類固醇或傳統免疫抑制劑無效時，通常考慮 anti-TNF、anti-integrin、anti-IL-12/23 等生物製劑；手術主要用於併發症或局部難治病灶，故此敘述錯誤。",
        },
        "core": "Crohn 的藥物治療可升級到生物製劑；手術不是藥物無效後一律的下一步。",
        "key": "Crohn disease 難治時常升級生物製劑，手術保留給併發症或局部難治。",
    },
    17: {
        "topic": "胃藥機轉",
        "analysis": "胃酸由 parietal cell 分泌，受 histamine H2 receptor、gastrin 與迷走神經刺激調控。Chief cell 主要分泌 pepsinogen，不是 H2 blocker 的主要作用細胞。",
        "options": {
            "A": "制酸劑直接中和胃酸，提高胃內 pH，敘述正確。",
            "B": "H2 receptor antagonist 阻斷的是 parietal cell 上的 H2 receptor，以降低胃酸分泌；chief cell 說法錯誤。",
            "C": "PPI 不可逆抑制 parietal cell 的 H+/K+-ATPase，是強效抑酸機轉，敘述正確。",
            "D": "長期 PPI 停藥後可能出現 rebound acid hypersecretion，敘述正確。",
        },
        "core": "胃酸分泌主角是 parietal cell；chief cell 主分泌 pepsinogen。",
        "key": "H2 blocker 作用在 parietal cell，不是 chief cell。",
    },
    18: {
        "topic": "急性上消化道出血",
        "analysis": "急性出血早期血紅素可能尚未下降，因血漿與紅血球一起流失，需經輸液或體液重新分布後才被稀釋。因此不能因初始 Hb 正常就排除嚴重出血。",
        "options": {
            "A": "病史可協助判斷潰瘍、肝硬化靜脈曲張、NSAID 或抗凝血使用等出血原因，處置合理。",
            "B": "生命徵象、姿勢性低血壓與休克徵象是評估嚴重出血的關鍵，處置合理。",
            "C": "急性大量出血初期 Hb 可正常，不能因此判斷沒有嚴重出血，故最不恰當。",
            "D": "活動性出血或可見血管的潰瘍需內視鏡止血，可降低再出血與不良結果，敘述正確。",
        },
        "core": "急性出血早期 Hb 可能騙人；先看生命徵象與臨床灌流。",
        "key": "初始血紅素正常不能排除嚴重急性上消化道出血。",
    },
    19: {
        "topic": "腸胃道吸收",
        "analysis": "不同營養素有典型吸收部位：鐵主要在十二指腸，鈣多在上端小腸；膽酸在末端迴腸回收；脂溶性維生素為 A、D、E、K。分泌型腹瀉禁食仍持續。",
        "options": {
            "A": "鐵與鈣主要在十二指腸與近端小腸吸收，敘述正確。",
            "B": "膽酸主要在末端迴腸吸收，不是大腸。",
            "C": "A、D、E、K 是脂溶性維生素，不是水溶性。",
            "D": "分泌型腹瀉即使禁食仍不會明顯改善；滲透型腹瀉才會因禁食減輕。",
        },
        "core": "近端小腸吸收鐵與鈣，末端迴腸吸收膽酸與 B12；分泌型腹瀉禁食仍持續。",
        "key": "鐵與鈣主要在上端小腸吸收。",
    },
    20: {
        "topic": "急性腸阻塞",
        "analysis": "小腸阻塞較大腸阻塞常見，術後沾黏是小腸阻塞常見原因。大腸阻塞最常見原因通常是大腸癌，腸扭轉不是最常見原因。",
        "options": {
            "A": "整體而言小腸阻塞比大腸阻塞常見，敘述正確。",
            "B": "術後沾黏是小腸阻塞最常見原因之一，敘述正確。",
            "C": "大腸阻塞最常見原因是大腸癌；volvulus 雖可造成阻塞，但不是最常見原因，故錯誤。",
            "D": "乙狀結腸扭轉可先以內視鏡減壓與置管，若壞死或穿孔則需手術，敘述正確。",
        },
        "core": "大腸阻塞第一常見原因是癌症；乙狀結腸扭轉可內視鏡減壓。",
        "key": "腸扭轉不是大腸阻塞最常見原因。",
    },
    21: {
        "topic": "肝細胞癌影像診斷",
        "analysis": "HCC 可在高風險族群中以典型動脈相增強、門脈或延遲相 washout 的影像表現診斷。高風險背景包括肝硬化，不一定要同時有 B 型或 C 型肝炎。",
        "options": {
            "A": "單純脂肪肝背景若未明確屬高風險肝硬化族群，即使影像典型，也較不能直接免切片診斷 HCC。",
            "B": "肝硬化病人是 HCC 高風險族群，5 公分腫瘤有動脈相增強與 venous washout，符合非侵入性 HCC 診斷條件。",
            "C": "只有動脈相與靜脈相都增強，缺乏 washout，不是典型 HCC 影像模式。",
            "D": "沒有 arterial enhancement 不符合典型 HCC 影像診斷；單純 hypodense 不足以免切片確診。",
        },
        "core": "高風險肝臟背景加上 arterial phase hyperenhancement 與 washout，可支持 HCC 影像診斷。",
        "key": "肝硬化病人若肝腫瘤有 arterial enhancement 與 venous washout，可免切片診斷 HCC。",
    },
    22: {
        "topic": "B 型肝炎篩檢族群",
        "analysis": "HBV 篩檢重點族群包括孕婦、HCV 感染者、免疫抑制治療前病人、血液透析、HIV、注射藥物與高盛行地區出生者等。單純女女性行為者並非最主要需加強篩檢的高風險分類。",
        "options": {
            "A": "孕婦需篩檢 HBV，因可安排新生兒免疫預防並降低垂直傳染。",
            "B": "WSW 本身不是 HBV 加強篩檢的典型高風險族群，相較其他選項最不需要特別加強。",
            "C": "HCV 感染者可能有共同感染或治療相關 HBV 再活化風險，需篩檢 HBV。",
            "D": "免疫抑制劑可能造成 HBV reactivation，治療前應篩檢。",
        },
        "core": "免疫抑制前、孕婦與 HCV 感染者是 HBV 篩檢重點；題目考相對不需要者。",
        "key": "單純 WSW 不是 HBV 加強篩檢的典型高風險族群。",
    },
    23: {
        "topic": "肝硬化腹水治療",
        "analysis": "肝硬化腹水合併水腫的基本處置是限鈉與利尿劑，常用 spironolactone:furosemide 約 100:40 的比例。血鈉 130 mEq/L 可限水，但不應補鈉或大量 normal saline 使腹水惡化。",
        "options": {
            "A": "腹水病人應限鈉，不應每天補充鈉離子 4 g；補鈉會加重水腫與腹水。",
            "B": "限水、每日鈉攝取約 2 g，加上 furosemide 40 mg 與 spironolactone 100 mg，是較恰當組合。",
            "C": "每天給 normal saline 會增加鈉水負荷，通常會惡化腹水與水腫。",
            "D": "normal saline 加補鈉都與腹水治療方向相反，且沒有使用利尿劑控制體液。",
        },
        "core": "肝硬化腹水：限鈉、spironolactone 為主合併 furosemide；不要補鹽水。",
        "key": "肝硬化腹水應限制鈉攝取並使用 spironolactone/furosemide。",
    },
    24: {
        "topic": "血液透析血管通路",
        "analysis": "病人 eGFR 6 且計畫長期血液透析，若時間允許應預先建立永久血管通路。自體動靜脈瘻管通暢率較佳、感染與血栓較少，是優先選擇。",
        "options": {
            "A": "Arteriovenous fistula 是長期血液透析首選通路，需提前建立等待成熟，故最優先。",
            "B": "AV graft 成熟較快但感染與血栓風險較 AV fistula 高，通常在自體血管不適合時考慮。",
            "C": "雙腔導管適合緊急或短期透析，感染與狹窄風險高，不是長期優先。",
            "D": "隧道式導管可作較長期暫時通路，但仍不如 AV fistula 作為長期首選。",
        },
        "core": "血液透析長期通路優先順序：AV fistula 優於 AV graft，導管通常作暫時或不得已選項。",
        "key": "長期血液透析血管通路首選自體動靜脈瘻管。",
    },
    25: {
        "topic": "急性間質性腎炎",
        "analysis": "AIN 常由藥物過敏引起，但典型發燒、皮疹、嗜伊紅性白血球三聯徵其實少見。尿液可有白血球、白血球圓柱、血尿。類固醇可能加速恢復，但改善長期腎臟存活的證據不穩定，不能當作確定敘述。",
        "options": {
            "A": "發燒、紅疹、嗜伊紅性白血球增加只在少數藥物性 AIN 出現，敘述正確。",
            "B": "AIN 尿液可見膿尿、白血球圓柱與顯微血尿，敘述正確。",
            "C": "若有典型藥物暴露與時間序，停藥後改善，可臨床診斷，不一定每例都需腎切片。",
            "D": "類固醇可能縮短腎功能恢復時間，但是否改善長期腎臟存活並非確定結論，因此此敘述過度肯定而錯誤。",
        },
        "core": "AIN 先停可疑藥物；類固醇是否有長期腎存活利益需謹慎，不可過度宣稱。",
        "key": "AIN 類固醇可加速恢復的證據較強，改善長期腎存活則不確定。",
    },
    26: {
        "topic": "逆流性腎病變",
        "analysis": "成人 reflux nephropathy 常有兒時反覆泌尿道感染或尿床，影像常見腎臟疤痕、萎縮與不規則輪廓，且多為不對稱。若說對稱性萎縮，就不典型。",
        "options": {
            "A": "兒時尿床或反覆 UTI 支持膀胱輸尿管逆流與後續腎疤痕，屬典型病史。",
            "B": "慢性腎臟病時可呈輕度蛋白尿且尿沉渣相對不活躍，敘述可接受。",
            "C": "Reflux nephropathy 常造成不對稱疤痕與不規則萎縮，不是對稱性萎縮，故不是典型特徵。",
            "D": "控制血壓、特別是伴蛋白尿時使用 RAAS blockade，可延緩腎功能惡化。",
        },
        "core": "Reflux nephropathy 的影像重點是不對稱腎疤痕與萎縮。",
        "key": "成人逆流性腎病變不是典型對稱性腎萎縮。",
    },
    27: {
        "topic": "雙側尿路阻塞",
        "analysis": "雙側尿路阻塞可導致無尿、氮血症、代謝性酸中毒、高血鉀；解除阻塞後也可能有腎源性尿崩樣多尿。姿勢性低血壓較指向低血容量或自主神經問題，不是阻塞的典型鑑別提示。",
        "options": {
            "A": "AKI 合併無尿要高度懷疑雙側尿路阻塞或單腎阻塞。",
            "B": "腎衰竭合併姿勢性低血壓較支持腎前性低灌流，最不需要把雙側阻塞列為主要鑑別。",
            "C": "阻塞性腎病可造成氮血症、酸中毒與高血鉀，需納入鑑別。",
            "D": "阻塞後可出現 acquired nephrogenic diabetes insipidus 與解除阻塞後多尿，需想到尿路阻塞。",
        },
        "core": "無尿、高血鉀酸中毒與阻塞後多尿都提示雙側尿路阻塞；姿勢性低血壓偏腎前性。",
        "key": "Postural hypotension 不是雙側尿路阻塞的典型提示。",
    },
    28: {
        "topic": "狼瘡性腎炎病理",
        "analysis": "SLE 合併蛋白尿、腎功能惡化與高血壓，腎切片可能看到免疫複合體沉積造成的 proliferative 或 membranous lupus nephritis，也可能有 crescents。FSGS 不是典型狼瘡性腎炎分類病灶。",
        "options": {
            "A": "Diffuse proliferative lupus nephritis 可有 diffuse subendothelial immune deposits，是典型嚴重類型。",
            "B": "Focal segmental glomerulosclerosis 不是狼瘡性腎炎典型病理分類，最不可能作為本題切片主病變。",
            "C": "Membranous lupus nephritis 可見 subepithelial immune complex deposits，屬 lupus nephritis 類型之一。",
            "D": "嚴重 proliferative lupus nephritis 可有 endocapillary proliferation 與 crescent formation。",
        },
        "core": "狼瘡性腎炎是免疫複合體病，常見 subendothelial 或 subepithelial deposits；FSGS 不是典型分類。",
        "key": "FSGS 最不像典型狼瘡性腎炎切片主病變。",
    },
    29: {
        "topic": "內生性急性腎損傷",
        "analysis": "鑑別腎前性與內生性 AKI 時，腎前性常有 FeNa <1%、尿滲透壓高、BUN/Cr >20；內生性急性腎小管壞死常見 muddy brown granular casts。",
        "options": {
            "A": "FeNa <1% 通常支持腎前性低灌流，不支持內生性 AKI。",
            "B": "尿液滲透壓 >500 代表腎小管濃縮能力保留，較像腎前性。",
            "C": "BUN/Cr >20 也常見於腎前性氮血症。",
            "D": "尿沉渣出現顆粒性圓柱體，特別是 muddy brown casts，支持 intrinsic AKI/急性腎小管壞死。",
        },
        "core": "內生性 AKI 看尿沉渣；muddy brown granular casts 是 ATN 高產值線索。",
        "key": "Granular casts 支持 intrinsic AKI。",
    },
    30: {
        "topic": "慢性腎臟病貧血",
        "analysis": "CKD 貧血的主因是腎臟 EPO 生成不足，並可合併鐵利用不良、慢性發炎、尿毒性血小板功能異常造成出血等。題目問錯誤原因，EPO 過多與 CKD 貧血相反。",
        "options": {
            "A": "CKD 是紅血球生成素不足，不是過多，因此此選項錯誤。",
            "B": "慢性發炎與 hepcidin 上升會造成鐵利用不良，會加重貧血。",
            "C": "尿毒症可造成血小板功能異常與出血傾向，使貧血惡化。",
            "D": "慢性發炎會抑制造血並影響鐵代謝，是 CKD 貧血成因之一。",
        },
        "core": "CKD 貧血核心是 EPO 不足加上發炎與鐵利用障礙。",
        "key": "慢性腎臟病貧血不是 EPO 過多，而是 EPO 不足。",
    },
    31: {
        "topic": "CPPD disease",
        "analysis": "CPPD 又稱假性痛風，較常見於老年人，常侵犯膝關節。關節液可見菱形或棒狀、弱陽性雙折光結晶；X 光 chondrocalcinosis 是常見線索。",
        "options": {
            "A": "CPPD 較常見於老年人，不是年輕人，故此句錯。",
            "B": "CPPD 與副甲狀腺亢進、血色素沉著症、低鎂等代謝疾病有關，說與 primary hyperparathyroidism 無關不對。",
            "C": "CPPD 常侵犯膝關節，關節液可見菱形或棒狀、正雙折光結晶，是最適當敘述。",
            "D": "Chondrocalcinosis 是 CPPD 典型影像，不是痛風常見特徵。",
        },
        "core": "CPPD：老人、膝關節、chondrocalcinosis、rhomboid positively birefringent crystals。",
        "key": "CPPD 關節液常見菱形正雙折光結晶。",
    },
    32: {
        "topic": "全身性硬化症分類",
        "analysis": "Diffuse cutaneous systemic sclerosis 較容易早期內臟侵犯，包括快速進展間質性肺病與 scleroderma renal crisis；limited 型較常見 CREST 特徵與肺高壓。",
        "options": {
            "A": "Joint contractures 與廣泛皮膚硬化較相關，較常見於 diffuse 型，不是 limited 型。",
            "B": "快速進展 ILD 較常見於 diffuse cutaneous systemic sclerosis，敘述最適當。",
            "C": "Calcinosis cutis 是 CREST/limited 型較典型，不是 diffuse 型較常見。",
            "D": "Scleroderma renal crisis 較常見於 diffuse 型，尤其早期皮膚快速進展者，不是 limited 型。",
        },
        "core": "Diffuse 型硬皮症內臟侵犯較早且較重，包含 ILD 與 renal crisis。",
        "key": "快速進展 ILD 較常見於 diffuse cutaneous systemic sclerosis。",
    },
    33: {
        "topic": "巨細胞動脈炎",
        "analysis": "Giant cell arteritis 多發生於 50 歲以上，女性較多，常合併 polymyalgia rheumatica。治療以 glucocorticoid 為主，tocilizumab 可作為減少類固醇暴露或復發控制的選項。",
        "options": {
            "A": "GCA 幾乎是 50 歲以上疾病，小於 50 歲不典型。",
            "B": "女性較男性常見，男性較常見的說法錯。",
            "C": "Tocilizumab 抑制 IL-6 receptor，可用於 GCA 治療，是正確敘述。",
            "D": "GCA 合併 PMR 的比例遠高於 5%，常見約數十百分比，故此敘述錯。",
        },
        "core": "GCA：大於 50 歲、女性較多、可合併 PMR；治療可用 steroid 與 tocilizumab。",
        "key": "Tocilizumab 可用於 giant cell arteritis。",
    },
    34: {
        "topic": "慢性蕁麻疹治療",
        "analysis": "超過 6 週、找不到明確過敏原的反覆 wheals，符合慢性自發性蕁麻疹。第一線治療是第二代 H1 antihistamine；計程車司機更應避免鎮靜性第一代抗組織胺。",
        "options": {
            "A": "Desloratadine 是第二代 H1 antihistamine，嗜睡較少，適合作為第一線每日治療。",
            "B": "Diphenhydramine 是第一代抗組織胺，鎮靜與抗膽鹼副作用較明顯，對職業駕駛不理想。",
            "C": "全身性類固醇不作為慢性蕁麻疹長期第一線，可短期救急但不適合本題。",
            "D": "外用強效類固醇對蕁麻疹風團幫助有限，且不處理肥大細胞/組織胺機轉。",
        },
        "core": "慢性自發性蕁麻疹第一線是第二代 H1 antihistamine。",
        "key": "慢性蕁麻疹優先使用低鎮靜第二代抗組織胺。",
    },
    35: {
        "topic": "SLE 確診評估",
        "analysis": "年輕女性反覆發燒、關節炎、血球低下、蛋白尿與肋膜積水，高度懷疑 SLE 併腎炎。ANA、抗磷脂質抗體與腎切片都有助於分類或確診病情；肺部 CT 對 SLE 確診幫助最小。",
        "options": {
            "A": "ANA 是 SLE 高敏感度篩檢與分類重要項目，有助確診。",
            "B": "抗磷脂質抗體可評估 SLE 相關抗磷脂質症候群，也屬重要免疫評估。",
            "C": "肺部 CT 可評估肺病變，但對本例 SLE 疾病確診本身最無幫助。",
            "D": "腎切片可確認 lupus nephritis 類型與治療強度，對病情確診與分型很有幫助。",
        },
        "core": "疑似 SLE 要靠免疫血清與受侵犯器官評估；肺部 CT 不是確診核心。",
        "key": "肺部 CT 對此例 SLE 確診最無幫助。",
    },
    36: {
        "topic": "腦轉移常見原發癌",
        "analysis": "腦轉移常見原發部位包括肺癌、乳癌與黑色素瘤，也可見腎癌、腸胃道癌。前列腺癌相對較常轉移骨骼，腦轉移機率較低。",
        "options": {
            "A": "肺癌是成人腦轉移最常見來源之一。",
            "B": "乳癌也常發生腦轉移，尤其 HER2-positive 或 triple-negative 亞型。",
            "C": "前列腺癌以骨轉移最典型，腦轉移相對少見，因此是本題答案。",
            "D": "黑色素瘤具有高度腦轉移傾向，是常見來源之一。",
        },
        "core": "腦轉移常見來源：肺、乳、黑色素瘤；前列腺癌典型是骨轉移。",
        "key": "前列腺癌相對較少造成腦轉移。",
    },
    37: {
        "topic": "卵巢上皮癌治療",
        "analysis": "卵巢上皮癌治療重點是腫瘤減積手術加 platinum-taxane 化療，BRCA 狀態與預後、維持治療相關。Optimal cytoreduction 通常指無肉眼殘存或殘存腫瘤小於 1 公分，不是 1 到 2 公分。",
        "options": {
            "A": "Optimal resection 不是殘餘 1-2 公分；傳統多以殘餘腫瘤小於 1 公分，現代更強調無肉眼殘存，故錯誤。",
            "B": "BRCA1/2 胚系或體細胞突變與卵巢上皮癌風險及治療選擇相關。",
            "C": "Paclitaxel 加 carboplatin 是常用有效輔助化療組合。",
            "D": "Histologic grade 會影響預後與風險評估，敘述正確。",
        },
        "core": "卵巢癌減積手術預後與殘餘腫瘤大小高度相關，目標是盡量無殘存。",
        "key": "Optimal cytoreduction 不是殘餘腫瘤 1-2 公分。",
    },
    38: {
        "topic": "乳癌標靶藥物",
        "analysis": "本題考標靶藥物配對。Pertuzumab 抗 HER2，denosumab 抗 RANKL，ribociclib 抑制 CDK4/6；everolimus 是 mTOR inhibitor，不是 EGFR inhibitor。",
        "options": {
            "A": "Pertuzumab 是抗 HER2 單株抗體，配對正確。",
            "B": "Denosumab 是抗 RANK ligand 抗體，可用於骨相關事件預防等，配對正確。",
            "C": "Ribociclib 是 CDK4/6 inhibitor，配對正確。",
            "D": "Everolimus 抑制 mTOR pathway，不是 EGFR 抑制劑，配對錯誤。",
        },
        "core": "Everolimus = mTOR inhibitor；乳癌標靶配對題常考 HER2、CDK4/6、RANKL、mTOR。",
        "key": "Everolimus 的主要標靶是 mTOR，不是 EGFR。",
    },
    39: {
        "topic": "癌症治療副作用",
        "analysis": "Tumor lysis syndrome 預防核心是高風險辨識、大量輸液、監測電解質與使用 allopurinol 或 rasburicase；尿液鹼化已非最重要且可能增加鈣磷沉積風險。",
        "options": {
            "A": "TLS 預防最重要不是 urine alkalization，而是水分補充與降尿酸策略，因此最不恰當。",
            "B": "Rituximab 輸注時發燒、寒顫、支氣管痙攣屬 infusion reaction，敘述正確。",
            "C": "CAR-T 重要急性毒性包括 cytokine release syndrome 與神經毒性，敘述正確。",
            "D": "Taxane 過敏常在早期療程，platinum 過敏常在多次暴露後出現，敘述正確。",
        },
        "core": "TLS 預防以 hydration 與 uric acid control 為主，尿液鹼化不是核心首選。",
        "key": "預防 tumor lysis syndrome 最重要不是尿液鹼化。",
    },
    40: {
        "topic": "Rituximab 與 PML",
        "analysis": "Rituximab 抗 CD20，會造成 B 細胞耗竭與免疫抑制，少數但嚴重風險包括 JC virus 再活化引起 progressive multifocal leukoencephalopathy。",
        "options": {
            "A": "Rituximab 不會特別增加潰瘍性大腸炎發生率，且有些免疫疾病反而可能使用生物製劑治療。",
            "B": "Rituximab 可用於部分類風濕性關節炎治療，不是最可能增加的疾病。",
            "C": "腎病症候群不是 rituximab 治療後最典型增加的感染性併發症，部分腎病還會用 rituximab。",
            "D": "PML 是 JC virus 在免疫抑制下再活化造成的嚴重脫髓鞘疾病，rituximab 會增加此風險。",
        },
        "core": "Rituximab 的罕見嚴重感染風險要記 PML/JC virus。",
        "key": "Rituximab 可能增加 progressive multifocal leukoencephalopathy 風險。",
    },
    41: {
        "topic": "急性淋巴性白血病治療",
        "analysis": "ALL 治療包含誘導、鞏固與維持治療；Ph+ ALL 需加 TKI。中樞神經預防與治療以 intrathecal chemotherapy 等為主，imatinib 中樞神經穿透不足，不能視為理想 CNS 選項。",
        "options": {
            "A": "現代 ALL 治療初次完全緩解率可高於 80%，敘述正確。",
            "B": "維持治療常包含 6-mercaptopurine 與 methotrexate，時間約 2 年以上，敘述正確。",
            "C": "Philadelphia chromosome positive ALL 應加入 TKI，包含維持或整體治療策略，敘述正確。",
            "D": "Imatinib CNS 穿透有限，CNS 預防與治療應靠鞘內化療/放療等，不是理想選項，故最不適當。",
        },
        "core": "Ph+ ALL 要加 TKI，但 CNS disease 仍需鞘內治療；不要把 imatinib 當理想 CNS 治療。",
        "key": "Imatinib 不是 Ph+ ALL 中樞神經預防與治療的理想選項。",
    },
    42: {
        "topic": "急性失血後貧血",
        "analysis": "急性出血初期血紅素可能仍接近正常；輸液復甦後血液被稀釋，才會看到 Hb/Hct 下降。身體會增加 EPO，數日後網狀紅血球上升。",
        "options": {
            "A": "急性大量出血初期可休克但血紅素只輕度下降或尚未明顯下降，敘述正確。",
            "B": "Optimal fluid resuscitation 後會血液稀釋，出現 hemodilution，不是 hemoconcentration，故錯誤。",
            "C": "骨髓代償後周邊血 reticulocyte 會上升，敘述正確。",
            "D": "腎臟感受缺氧後 EPO 上升以刺激造血，敘述正確。",
        },
        "core": "急性失血補液後 Hb/Hct 下降是稀釋效應，不是濃縮。",
        "key": "急性出血復甦後通常 hemodilution，而非 hemoconcentration。",
    },
    43: {
        "topic": "骨髓增生性腫瘤突變",
        "analysis": "典型 BCR-ABL 陰性的 MPN 包括 PV、ET、primary myelofibrosis，常見 driver mutations 是 JAK2、CALR、MPL。FLT3 較常與 AML 相關，不是 MPN 常見突變。",
        "options": {
            "A": "JAK2 V617F 是 MPN 最常見突變之一，尤其 PV。",
            "B": "MPL 突變可見於 ET 或 primary myelofibrosis。",
            "C": "CALR 突變常見於 JAK2 陰性的 ET 或 myelofibrosis。",
            "D": "FLT3 主要與急性骨髓性白血病風險與預後相關，最不像 MPN 常見突變。",
        },
        "core": "MPN driver mutation 三寶：JAK2、CALR、MPL。",
        "key": "FLT3 不是典型 MPN 常見 driver mutation。",
    },
    44: {
        "topic": "多發性骨髓瘤",
        "analysis": "Multiple myeloma 常見 CRAB：高血鈣、腎功能異常、貧血、骨病灶。骨病灶以 lytic lesion 為主，骨掃描依賴成骨活性，對純溶骨病灶敏感度不佳。",
        "options": {
            "A": "骨髓瘤有免疫球蛋白功能低下，容易感染，肺炎鏈球菌是重要病原之一。",
            "B": "骨痛、背痛或病理性骨折是常見表現。",
            "C": "溶骨病灶造成高血鈣是常見併發症。",
            "D": "骨掃描對骨髓瘤溶骨病灶不如 X 光 skeletal survey、低劑量 CT、MRI 或 PET/CT；說 bone scan 更精確不適當。",
        },
        "core": "骨髓瘤骨病灶是 lytic，bone scan 可能低估。",
        "key": "多發性骨髓瘤骨病灶不宜說 bone scan 比 X 光更精確。",
    },
    45: {
        "topic": "間質性肺病治療",
        "analysis": "ILD 治療依病因不同而異。IPF 不以傳統免疫抑制作為降低死亡率的標準；COP 常對類固醇反應良好；IPF 抗纖維化藥物可減緩 FVC 下降並改善疾病進展風險。",
        "options": {
            "A": "IPF 使用傳統免疫抑制治療不會降低死亡率，某些組合反而有害。",
            "B": "Cryptogenic organizing pneumonia 對 systemic corticosteroids 常有良好症狀與影像改善，是最適當敘述。",
            "C": "Pirfenidone 與 nintedanib 可減緩 IPF 進展；不能簡化成對死亡率完全沒有改善意義。",
            "D": "CTD-associated ILD 可依情況使用免疫抑制劑，也可能合併抗纖維化治療，並非不可併用。",
        },
        "core": "COP 對類固醇反應佳；IPF 以抗纖維化治療為主，避免傳統免疫抑制濫用。",
        "key": "Cryptogenic organizing pneumonia 常可用類固醇改善。",
    },
    46: {
        "topic": "阻塞型睡眠呼吸中止嚴重度",
        "analysis": "OSA 嚴重度主要看睡眠檢查 AHI、血氧下降程度與白天症狀。BMI 是危險因子與共病評估，不是直接分級嚴重度的指標。",
        "options": {
            "A": "AHI 是 OSA 嚴重度分級核心指標。",
            "B": "夜間最低血氧與缺氧負荷反映疾病嚴重度與風險。",
            "C": "BMI 是 OSA 的重要危險因子，但不是嚴重度分級指標，因此是本題答案。",
            "D": "白天嗜睡反映症狀負擔，也常納入臨床嚴重度判斷。",
        },
        "core": "OSA 嚴重度看 AHI、缺氧與症狀；BMI 是風險因子。",
        "key": "BMI 不是 OSA 嚴重度指標。",
    },
    47: {
        "topic": "年輕人非典型肺炎",
        "analysis": "18 歲、發燒咳嗽、雙下肺炎但白血球不高，符合非典型肺炎表現。Mycoplasma pneumoniae 常見於年輕人，可有較輕的實驗室發炎反應。",
        "options": {
            "A": "金黃色葡萄球菌肺炎常見於流感後、壞死性肺炎或嚴重感染，不是此典型年輕人非典型肺炎。",
            "B": "Mycoplasma pneumoniae 常造成青少年或年輕成人非典型肺炎，白血球可不高，最可能。",
            "C": "Klebsiella pneumoniae 較常見於酒癮、糖尿病或衰弱病人，常有大葉肺炎與濃痰。",
            "D": "Pseudomonas 多見於結構性肺病、住院或免疫低下，不符合此健康年輕人。",
        },
        "core": "年輕人、白血球不高、非典型肺炎表現要想到 Mycoplasma。",
        "key": "健康年輕成人非典型肺炎常見 Mycoplasma pneumoniae。",
    },
    48: {
        "topic": "敗血症治療",
        "analysis": "敗血症治療重點是早期抗生素、感染源控制、輸液維持灌流，若輸液後仍低血壓則給 vasopressor。碳酸氫鈉不是治療首要目標，除非特定嚴重酸中毒情境才考慮。",
        "options": {
            "A": "及早給予合適抗生素可改善敗血症存活，敘述正確。",
            "B": "敗血症酸中毒主要要改善灌流與感染，bicarbonate 不是首要治療目標，故最不適當。",
            "C": "靜脈輸液以恢復有效循環與器官灌流是初期治療核心。",
            "D": "輸液後仍低血壓或需維持 MAP 時，應考慮 norepinephrine 等升壓劑。",
        },
        "core": "敗血症處置：抗生素、輸液、感染源控制、必要時升壓；不要把矯正數字當首要目標。",
        "key": "敗血症酸中毒的首要治療不是 bicarbonate，而是恢復灌流與控制感染。",
    },
    49: {
        "topic": "低血氧但胸部 X 光正常",
        "analysis": "急性低血氧而胸部 X 光無明顯異常時，要想到肺栓塞、右至左分流、氣喘或早期小氣道問題，以及肝肺症候群等。氣胸與肺水腫通常會在 X 光看到異常。",
        "options": {
            "A": "包含氣胸 3；氣胸通常胸部 X 光可見異常，因此不合適。",
            "B": "包含氣胸 3 且漏掉肺栓塞，組合不佳。",
            "C": "肺栓塞、右至左分流、肝硬化相關肝肺症候群與氣喘都可在 X 光相對正常時造成低血氧，最符合。",
            "D": "包含氣胸與肺水腫，兩者多半會有 X 光異常，不符合題幹。",
        },
        "core": "低血氧但 CXR 正常：PE、shunt、asthma、hepatopulmonary syndrome 要列入。",
        "key": "胸部 X 光正常的急性低血氧可見於 PE、右左分流、氣喘與肝硬化相關分流。",
    },
    50: {
        "topic": "氣喘診斷",
        "analysis": "氣喘診斷最有價值的是證明可變性氣流阻塞，例如肺功能檢查見 obstructive pattern 且支氣管擴張劑後 FEV1 有可逆性改善，或支氣管激發試驗陽性。",
        "options": {
            "A": "動脈血氣可評估急性嚴重發作與呼吸衰竭，但不是診斷氣喘最有價值工具。",
            "B": "胸部 X 光可排除其他疾病，但多數氣喘病人可能正常。",
            "C": "肺功能檢查能客觀證明可逆性氣流阻塞，是診斷氣喘最有價值檢查。",
            "D": "心電圖主要用於排除心臟問題，不能診斷氣喘。",
        },
        "core": "氣喘診斷要客觀證明可變性氣流阻塞，首選肺功能檢查。",
        "key": "肺功能檢查最有助於診斷氣喘。",
    },
    51: {
        "topic": "肺結核影像",
        "analysis": "慢性咳嗽有痰數月，胸部 X 光若呈現上肺葉浸潤、空洞或纖維化，最符合肺結核。題目附圖雖未呈現於文字，但官方答案指向肺結核，應以慢性症狀與典型影像判讀。",
        "options": {
            "A": "肺結核常有慢性咳嗽、痰、體重下降或夜間盜汗，影像可見上肺葉病灶或空洞，最可能。",
            "B": "肺膿瘍多有發燒、惡臭痰與 air-fluid level，不是本題最可能診斷。",
            "C": "一般肺炎多為急性病程，數月咳痰較不典型。",
            "D": "肺癌可造成慢性咳嗽或腫塊，但 30 歲男性與題目影像語境較支持結核。",
        },
        "core": "慢性咳嗽加典型胸片上肺葉病灶要先想到肺結核。",
        "key": "慢性咳痰數月且胸片典型時，肺結核最可能。",
    },
    52: {
        "topic": "嗜鉻細胞瘤",
        "analysis": "嗜鉻細胞瘤診斷需先以生化證據確認 catecholamine/metanephrine 過量，再做影像定位。傳統 rule of ten 包括約 10% bilateral、extra-adrenal、malignant 等；不是 10% unilateral，因大多數其實是單側腎上腺腫瘤。",
        "options": {
            "A": "頭痛、焦慮恐慌、多尿、姿勢性低血壓與高血糖都可見於兒茶酚胺過量。",
            "B": "診斷需生化檢查加影像定位，兩者都重要，敘述正確。",
            "C": "Rule of ten 不會說 10% unilateral；大多數是 unilateral adrenal tumor，因此此選項錯誤。",
            "D": "CT 與 MRI 對定位嗜鉻細胞瘤都有高敏感度，敘述可接受。",
        },
        "core": "Pheochromocytoma rule of ten 常考 bilateral、extra-adrenal、malignant；不是 unilateral。",
        "key": "嗜鉻細胞瘤多數為單側腎上腺腫瘤，不是只有 10%。",
    },
    53: {
        "topic": "淋巴球性腦垂體炎",
        "analysis": "Lymphocytic hypophysitis 常見於孕期或產後女性，可有高泌乳素、頭痛、視野症狀與腦垂體功能低下。MRI 常見腦垂體腫大與柄部增厚，不是 empty sella。",
        "options": {
            "A": "產後女性常見，可因 stalk effect 出現高泌乳素血症，敘述正確。",
            "B": "急性發炎期 MRI 多為 pituitary enlargement 或 stalk thickening；empty sella 不是典型表現，故錯誤。",
            "C": "腦垂體腫大可壓迫周邊構造造成頭痛與視覺異常，敘述正確。",
            "D": "部分病人經類固醇治療後發炎緩解，腦垂體功能可恢復，敘述正確。",
        },
        "core": "淋巴球性腦垂體炎影像是腦垂體腫大，不是空蝶鞍。",
        "key": "Lymphocytic hypophysitis 的 MRI 典型不是 empty sella。",
    },
    54: {
        "topic": "庫欣氏症候群",
        "analysis": "Cushing syndrome 常見中心性肥胖、水牛肩、紫紋、近端肌肉無力、感染風險與血栓風險上升。肌病變典型是 proximal myopathy，造成爬樓梯或起身困難，不是 distal myopathy。",
        "options": {
            "A": "中心性肥胖與 buffalo hump 是典型 Cushing 外觀。",
            "B": "Cushing 是近端肌肉無力造成爬樓梯困難；選項寫遠端肌肉無力，故錯誤。",
            "C": "高皮質醇會免疫抑制，也可造成嗜中性球增加，感染風險上升。",
            "D": "Cushing syndrome 會增加靜脈血栓風險，包括 DVT/PE。",
        },
        "core": "Cushing 肌病變是 proximal myopathy。",
        "key": "庫欣氏症候群造成近端肌肉無力，不是遠端肌肉無力。",
    },
    55: {
        "topic": "甲狀腺功能檢查",
        "analysis": "TSH 是初篩甲狀腺功能的重要檢查，但若懷疑腦下垂體或下視丘疾病，單看 TSH 可能誤判，需搭配 free T4 甚至其他垂體軸評估。",
        "options": {
            "A": "Tg antibody 與 TPO antibody 有助判斷自體免疫甲狀腺疾病，敘述正確。",
            "B": "甲狀腺抗體陽性者較容易發生甲狀腺功能異常，敘述正確。",
            "C": "內源性甲狀腺毒症通常 thyroglobulin 上升；外源性服用甲狀腺素造成者 thyroglobulin 低，是例外。",
            "D": "中樞性甲狀腺功能異常不能靠單獨 TSH 鑑別，需看 free T4 與垂體狀態，故最不適當。",
        },
        "core": "疑似中樞性甲狀腺病變時，TSH 不能單獨解讀，必須搭配 free T4。",
        "key": "單獨 TSH 不能鑑別腦下垂體造成的甲狀腺功能異常。",
    },
    56: {
        "topic": "第二型糖尿病",
        "analysis": "第二型糖尿病核心病生理是胰島素阻抗、相對胰島素分泌不足與肝臟葡萄糖輸出增加。需要胰島素治療代表 beta cell 功能惡化或控制需求增加，不會因此變成第一型糖尿病。",
        "options": {
            "A": "胰島素阻抗是第二型糖尿病核心特徵之一。",
            "B": "第二型糖尿病也有不同程度 beta cell 功能衰退與胰島素分泌不足。",
            "C": "肝臟葡萄糖新生增加會造成空腹高血糖，是重要機轉。",
            "D": "第二型糖尿病人開始注射胰島素後仍是第二型糖尿病，不會轉變成第一型，故錯誤。",
        },
        "core": "糖尿病分類看病生理，不看是否使用胰島素。",
        "key": "第二型糖尿病使用胰島素後不會變成第一型糖尿病。",
    },
    57: {
        "topic": "血糖調控",
        "analysis": "Whipple triad 包括低血糖症狀、當下低血糖測值、血糖恢復後症狀改善。正常空腹血糖下限不是 50 mg/dL；50 已接近或屬低血糖範圍。",
        "options": {
            "A": "症狀在血糖恢復後改善是 Whipple triad 的一部分，敘述正確。",
            "B": "一般正常空腹血漿血糖下限約 70 mg/dL，50 mg/dL 太低，故最不適當。",
            "C": "肝臟與腎臟都能進行 gluconeogenesis，尤其禁食時重要。",
            "D": "低血糖時第一步是胰島素下降，接著 glucagon 與 epinephrine 等反調節荷爾蒙上升。",
        },
        "core": "Whipple triad 與反調節荷爾蒙是低血糖核心；正常空腹血糖不是 50 mg/dL。",
        "key": "正常空腹血糖下限約 70 mg/dL，不是 50 mg/dL。",
    },
    58: {
        "topic": "高尿酸血症",
        "analysis": "高尿酸與代謝症候群、腎結石及急性尿酸腎病變相關。但無症狀高尿酸血症通常不一律給降尿酸藥，需依尿酸值、腎病、結石、腫瘤溶解風險等情境決定。",
        "options": {
            "A": "代謝症候群常伴隨高尿酸血症，敘述正確。",
            "B": "尿酸急遽升高可造成急性尿酸腎病變與急性腎衰竭，敘述正確。",
            "C": "長期高尿酸可增加尿酸結石與腎臟問題風險，敘述正確。",
            "D": "無症狀高尿酸不應一律積極給降尿酸藥，需個別化判斷，故最不適當。",
        },
        "core": "無症狀高尿酸血症不是看到就一定用藥；先看症狀與高風險情境。",
        "key": "無症狀高尿酸血症不一定需要降尿酸藥。",
    },
    59: {
        "topic": "醫療照護相關肺炎預防",
        "analysis": "醫療照護相關或院內肺炎與口咽移生、誤吸、住院時間和抗藥菌有關。預防 VAP 的床頭抬高通常建議約 30-45 度，不是 15-20 度。",
        "options": {
            "A": "抗藥性菌在口咽移生後誤吸，是院內肺炎重要機轉與危險因子。",
            "B": "早發性院內肺炎較常見社區型病原，如肺炎鏈球菌或嗜血桿菌，敘述正確。",
            "C": "若無特定抗藥菌且臨床反應佳，較短療程可減少後續抗藥菌選汰，敘述可接受。",
            "D": "床頭抬高預防吸入通常目標約 30-45 度；15-20 度不足以作為標準作業，故錯誤。",
        },
        "core": "預防院內/呼吸器肺炎的床頭抬高通常是 30-45 度。",
        "key": "床頭抬高 15-20 度不是減少醫療照護相關肺炎的標準角度。",
    },
    60: {
        "topic": "妊娠抗生素禁忌",
        "analysis": "懷孕用藥要避開會影響胎兒骨骼與牙齒的藥物。Tetracycline 會沉積於胎兒骨骼與牙齒，造成牙齒變色及骨生長影響，通常應避免。",
        "options": {
            "A": "Azithromycin 在懷孕常被視為相對安全，可用於特定感染。",
            "B": "Clindamycin 在懷孕可使用於多種厭氧菌或皮膚軟組織感染情境。",
            "C": "Erythromycin 多數情境可於懷孕使用，但需注意特定鹽類與腸胃副作用。",
            "D": "Tetracycline 會影響胎兒牙齒與骨骼發育，懷孕婦女應避免。",
        },
        "core": "孕婦抗生素禁忌常考 tetracycline：牙齒變色、骨骼影響。",
        "key": "懷孕應避免 tetracycline。",
    },
    61: {
        "topic": "結核性腦膜炎",
        "analysis": "TB meningitis CSF 常見淋巴球增多、低糖、高蛋白。AFB smear 敏感度低；PCR 可快速輔助，但陰性不能排除，培養仍是重要確診工具，不能說已取代培養成為最主要診斷。",
        "options": {
            "A": "CSF 淋巴球增多是 TB meningitis 典型表現，敘述正確。",
            "B": "CSF glucose 下降常見，敘述正確。",
            "C": "AFB stain 陽性率低，少於一半很合理，敘述正確。",
            "D": "PCR 可加速診斷但未取代培養；培養仍重要且可做藥敏，因此此敘述錯誤。",
        },
        "core": "TB meningitis：淋巴球、低糖、高蛋白；PCR 快但不能完全取代培養。",
        "key": "結核菌 PCR 不能說已取代培養成為最主要診斷工具。",
    },
    62: {
        "topic": "嚴重 Campylobacter 感染",
        "analysis": "Campylobacter jejuni 多數腸炎可支持療法或 macrolide，但本例為 80 歲肝硬化、低血壓、黃疸且血液培養陽性，屬嚴重敗血症情境；在藥敏前需選擇能涵蓋嚴重革蘭陰性菌血症的抗生素。",
        "options": {
            "A": "TMP-SMX 不是嚴重 Campylobacter jejuni 菌血症的經驗首選，抗藥性與涵蓋不足需考慮。",
            "B": "Metronidazole 主要涵蓋厭氧菌與部分原蟲，對 Campylobacter jejuni 不適合作為單一治療。",
            "C": "Ampicillin 對 Campylobacter 抗藥性常見，嚴重菌血症經驗治療不足。",
            "D": "Carbapenem 對嚴重敗血症與菌血症提供較廣泛且可靠涵蓋，在藥敏前為本題最適當選擇。",
        },
        "core": "Campylobacter 腸炎與嚴重菌血症治療強度不同；肝硬化休克菌血症需可靠經驗性涵蓋。",
        "key": "嚴重 Campylobacter jejuni 菌血症在藥敏前可選 carbapenem。",
    },
    63: {
        "topic": "HIV 病毒特徵",
        "analysis": "HIV 主要感染帶 CD4 receptor 的 T helper cells、macrophages 與 dendritic cells，並使用 CCR5 或 CXCR4 作為 co-receptor。題目選項 A 把 CD4 寫成 CD8，是關鍵錯誤。",
        "options": {
            "A": "HIV 進入細胞主要靠 CD4 receptor 加 CCR5/CXCR4，不是 CD8 receptor，也不是主要感染 CD8 T 細胞，故錯誤。",
            "B": "HIV 是 RNA retrovirus，需 reverse transcriptase 將 RNA 轉成 DNA，敘述正確。",
            "C": "病毒 DNA 會進入細胞核並整合到宿主基因組，形成 provirus，敘述正確。",
            "D": "全球 HIV 傳播仍以性行為傳染為重要主軸，異性間不安全性行為在全球負擔中佔重要比例，敘述可接受。",
        },
        "core": "HIV 的受器是 CD4，不是 CD8；共同受器是 CCR5 或 CXCR4。",
        "key": "HIV 主要與 CD4 receptor 和 CCR5/CXCR4 結合進入細胞。",
    },
    64: {
        "topic": "糖尿病足感染與骨髓炎",
        "analysis": "糖尿病足潰瘍合併黃綠色膿液且常泡水，需考慮 Pseudomonas 與骨髓炎。骨髓炎診斷以 probe-to-bone、MRI 與骨切片培養較可靠；表面 swab 常受污染，不能取代骨培養。",
        "options": {
            "A": "Probe-to-bone 若觸及骨頭，對糖尿病足骨髓炎有高度提示價值，敘述正確。",
            "B": "MRI 對骨髓炎敏感度高於 X 光，尤其早期病灶，敘述正確。",
            "C": "Wound swab 常反映表面移生菌，與骨切片培養不一定一致；說骨切片不必要是錯誤。",
            "D": "長期接觸水與黃綠色分泌物提示 Pseudomonas 風險，可考慮 piperacillin-tazobactam 或 cefepime。",
        },
        "core": "糖尿病足骨髓炎的培養以深部組織或骨切片較可信，表面 swab 不可靠。",
        "key": "傷口表面 swab 不能取代骨切片培養。",
    },
    65: {
        "topic": "水泡性皮膚軟組織感染",
        "analysis": "Vibrio vulnificus 典型與海水、鹹水或生食海鮮相關，尤其肝病或免疫低下者可出現 hemorrhagic bullae 與壞死性筋膜炎。淡水接觸不是它的典型危險因子。",
        "options": {
            "A": "Coxsackievirus 可造成手足口病，小水泡分布於手、足、口腔，敘述正確。",
            "B": "Vibrio vulnificus 風險是海水/鹹水或海鮮暴露，不是淡水，故錯誤。",
            "C": "SSSS 與 TEN 外觀可相似，皮膚切片分層位置可協助鑑別。",
            "D": "快速蔓延、紅黑色水泡、麻木或疼痛不成比例要警覺壞死性筋膜炎，敘述正確。",
        },
        "core": "Vibrio vulnificus = 海水/海鮮暴露加 hemorrhagic bullae，常見於肝病高風險者。",
        "key": "Vibrio vulnificus 的暴露風險是鹹水或海鮮，不是淡水。",
    },
    66: {
        "topic": "LEARN 看診模式",
        "analysis": "LEARN 是跨文化醫療溝通模式：Listen、Explain、Acknowledge、Recommend、Negotiate。選項中只有 R: Recommend 對應正確。",
        "options": {
            "A": "L 是 Listen，傾聽病人對問題的看法，不是 Label。",
            "B": "E 是 Explain，說明醫師對疾病的理解，不是 Effect。",
            "C": "A 是 Acknowledge，承認並回應差異與相似處，不是 Affect。",
            "D": "R 是 Recommend，提出治療建議，對應正確。",
        },
        "core": "LEARN：Listen、Explain、Acknowledge、Recommend、Negotiate。",
        "key": "LEARN 模式中的 R 代表 Recommend。",
    },
    67: {
        "topic": "失智症照護",
        "analysis": "阿茲海默症是最常見失智症；可逆原因常見包括譫妄、憂鬱、藥物、甲狀腺與 B12 等。臺灣失智共同照護中心提供診斷後支持與照護資源，是家醫與社區照護重要網絡。",
        "options": {
            "A": "最常見失智症是阿茲海默症，不是血管性失智症。",
            "B": "可回復性認知障礙常考憂鬱、藥物、內分泌或代謝問題；焦慮症不是最常見原因。",
            "C": "臺灣各縣市設有失智共同照護中心，提供個案管理、照護諮詢與資源連結，敘述正確。",
            "D": "血管性失智症除控制危險因子外，部分病人仍可考慮 AChEIs 改善認知症狀，不能說沒有助益。",
        },
        "core": "失智照護不只診斷，還要連結共同照護中心與社區資源。",
        "key": "臺灣失智共同照護中心提供失智症病人服務。",
    },
    68: {
        "topic": "身體症狀與家庭功能評估",
        "analysis": "病人症狀長期、檢查反覆正常，且與喪偶後對中風與成為子女負擔的擔憂相關。家庭醫學處置重點是理解脈絡與壓力源，先做家庭功能與心理社會評估，不急著重複高階檢查或直接轉介。",
        "options": {
            "A": "已做多項檢查無異常，直接安排 PET 會強化疾病焦慮且低價值。",
            "B": "已看過多家醫院與神經相關檢查，無新神經缺損時再轉神經科不是最佳下一步。",
            "C": "精神科評估可能有幫助，但家庭醫學初步可先建立關係與評估家庭壓力，不宜一開始就轉出。",
            "D": "喪偶、擔心成為子女負擔與慢性身體症狀相關，進行家庭功能評估最適當。",
        },
        "core": "身體化或疾病焦慮的家庭醫學處置要先理解心理社會與家庭脈絡。",
        "key": "慢性無器質性解釋症狀合併喪偶壓力時，下一步可做家庭功能評估。",
    },
    69: {
        "topic": "三段五級預防",
        "analysis": "初段預防是在疾病發生前降低風險，如衛教與疫苗；次段預防是早期發現早期治療，如篩檢；三段預防是疾病已發生後減少併發症與失能。",
        "options": {
            "A": "早期發現早期治療屬次段預防，不是初段預防。",
            "B": "注射疫苗預防流感屬初段預防，不是次段預防。",
            "C": "高血壓病人服藥以減少中風、心衰竭等併發症，屬三段預防，敘述正確。",
            "D": "衛生教育屬健康促進/初段預防，不是次段預防。",
        },
        "core": "初段防發生，次段早發現，三段減併發症與失能。",
        "key": "控制高血壓以減少併發症屬三段預防。",
    },
    70: {
        "topic": "肥胖治療",
        "analysis": "BMI 33.2 kg/m2 已達肥胖，依臺灣常用規範，BMI 達一定門檻可考慮藥物治療，尤其合併危險因子時。題幹只說來諮詢，不能直接判定行為改變階段；藥物資格是最客觀正確敘述。",
        "options": {
            "A": "來門診諮詢不等於一定已進入 contemplation；行為改變階段需詢問動機與準備度。",
            "B": "飲食、運動與行為治療重要，但題目問最正確，藥物治療資格更直接由 BMI 判斷。",
            "C": "BMI 33.2 已符合可考慮減重藥物治療的門檻，因此最正確。",
            "D": "跨理論模式可用於健康行為介入，但不能說已證實具有穩定長期效果作為最正確敘述。",
        },
        "core": "肥胖治療先評估 BMI、共病與動機；BMI 足夠高時可納入藥物治療。",
        "key": "BMI 33.2 kg/m2 符合可考慮減重藥物治療的條件。",
    },
    71: {
        "topic": "門把症候群",
        "analysis": "Hand-on-the-Doorknob Syndrome 指病人快離開時才提出真正擔心或難以啟齒的問題，常反映害怕被拒絕、羞於開口或測試醫師是否願意傾聽。",
        "options": {
            "A": "這不是醫師不想處理困難病人的行為，而是病人互動中的延遲提問。",
            "B": "病人害怕醫師拒絕或覺得問題麻煩，但仍想提出，是最貼切含義。",
            "C": "此現象不是病人不想回答、想趕快離開，而是臨走才吐露重要議題。",
            "D": "它不等同於身體化病人要求更多檢查，可發生於任何敏感或重要問題。",
        },
        "core": "門把症候群是在離開前提出真正問題，醫師要留意背後焦慮與未說出口需求。",
        "key": "Hand-on-the-Doorknob Syndrome 常代表病人想問但怕被拒絕。",
    },
    72: {
        "topic": "煤礦工人塵肺症與矽肺症",
        "analysis": "矽肺症比煤礦工人塵肺症更明顯增加結核與部分黴菌感染風險，也與肺癌、硬皮症及蛋殼狀肺門淋巴結鈣化較相關。煤礦工人塵肺症相對較少有這些特徵。",
        "options": {
            "A": "肺癌風險增加較典型與矽肺症相關，不是 CWP 相對特徵。",
            "B": "硬皮症與 silica exposure 的關聯較典型，不是 CWP 特徵。",
            "C": "肺門淋巴結蛋殼狀鈣化較常考矽肺症，不是 CWP 特徵。",
            "D": "相較矽肺症，CWP 罹患肺結核或黴菌感染的風險較低，敘述正確。",
        },
        "core": "Silicosis 特別要記 TB、fungal infection、scleroderma、egg-shell calcification。",
        "key": "煤礦工人塵肺症相較矽肺症，TB 或黴菌感染風險較低。",
    },
    73: {
        "topic": "末期病人疼痛控制",
        "analysis": "末期疼痛控制首選途徑通常是口服，因方便、非侵入且可穩定調整；針劑可用於無法口服、急性嚴重疼痛或需快速滴定時，但不是首選給藥途徑。",
        "options": {
            "A": "疼痛評估需涵蓋生理、心理、社會與靈性層面，敘述正確。",
            "B": "末期病人止痛給藥首選通常為口服；針劑雖快但非首選，故錯誤。",
            "C": "Nociceptive pain 通常對 opioid 反應良好，敘述正確。",
            "D": "骨轉移疼痛有發炎與骨膜刺激成分，NSAID 可作為重要選項之一，敘述可接受。",
        },
        "core": "安寧止痛原則：能口服就口服，規則給藥並依疼痛型態調整。",
        "key": "末期疼痛控制首選給藥途徑通常是口服，不是針劑。",
    },
    74: {
        "topic": "腹部中央鈣化",
        "analysis": "慢性胰臟炎可造成胰臟實質或胰管鈣化，位置在上腹中央或偏中線，是腹部正中央鈣化的典型原因。其他選項多位於骨盆、臀部或血管走向。",
        "options": {
            "A": "慢性胰臟炎的胰臟鈣化常位於上腹中央，最符合 central abdominal calcification。",
            "B": "膀胱結石位於骨盆腔中央偏下，不是腹部正中央上腹鈣化。",
            "C": "臀部注射鈣化位於臀部軟組織，不在腹部中央。",
            "D": "髂靜脈或股靜脈鈣化沿骨盆或腹股溝血管走向，不是典型腹部中央鈣化。",
        },
        "core": "胰臟鈣化是慢性胰臟炎影像高產值線索。",
        "key": "慢性胰臟炎最可能造成腹部中央鈣化。",
    },
    75: {
        "topic": "肝血管瘤影像",
        "analysis": "典型 hepatic hemangioma 在動態增強 CT/MRI 呈周邊結節狀不連續增強，隨時間向中心填入。MRI 通常 T2 高訊號、T1 低訊號。",
        "options": {
            "A": "早期 wash-out 比較讓人想到 HCC 或惡性腫瘤，不是血管瘤典型。",
            "B": "周邊結節狀顯影並逐漸向中央填入是肝血管瘤最典型影像特徵。",
            "C": "血管瘤 T1 多為低訊號，不是高訊號結節。",
            "D": "血管瘤 T2 通常非常高訊號，不是低訊號。",
        },
        "core": "肝血管瘤影像關鍵：peripheral nodular enhancement with centripetal fill-in。",
        "key": "肝血管瘤典型為周邊結節狀增強與中央逐漸填入。",
    },
    76: {
        "topic": "Parkland formula",
        "analysis": "Parkland formula 計算二度與三度燒傷面積，不把一度燒傷列入。輸液量為 4 mL x 體重 kg x %TBSA，前 24 小時給完，其中前 8 小時給一半。",
        "options": {
            "A": "二度 20% 加三度 5% 等於 25%；4 x 50 x 25 = 5000 mL，前 8 小時給一半為 2500 mL，正確。",
            "B": "3500 mL 是把面積或前 8 小時比例算錯後的過量選項。",
            "C": "4500 mL 接近把一度燒傷部分納入或未正確取半，錯誤。",
            "D": "5500 mL 超過 Parkland 前 8 小時計算量，錯誤。",
        },
        "core": "Parkland 只算二度與三度：4 mL x kg x %TBSA，前 8 小時給一半。",
        "key": "本題前 8 小時輸液量為 2500 mL。",
    },
    77: {
        "topic": "急性心肌梗塞處置",
        "analysis": "急性胸痛合併疑似 STEMI 時，不能因早期心肌酵素正常就排除心肌梗塞。Troponin 可能需數小時才上升，處置應依心電圖與臨床風險即時進行。",
        "options": {
            "A": "胸痛到急診後 10 分鐘內完成心電圖是標準急診流程，敘述正確。",
            "B": "若疑似下壁或右心室梗塞，加做右側心電圖可評估 RV infarction，處置合理。",
            "C": "床邊超音波可評估心臟功能、心包積液與主動脈根部線索，有助鑑別主動脈剝離。",
            "D": "心肌酵素早期可能正常，不能據此排除心肌梗塞，故最不適當。",
        },
        "core": "急性心肌梗塞早期不能等 troponin；STEMI 診斷與再灌流以 ECG 和臨床為先。",
        "key": "心肌酵素正常不能排除早期心肌梗塞。",
    },
    78: {
        "topic": "緩和治療症狀控制",
        "analysis": "Morphine 可用於癌末疼痛與呼吸困難，但治療呼吸困難通常從低劑量開始並謹慎滴定，不是使用止痛劑量的雙倍。緩和治療強調症狀緩解與副作用平衡。",
        "options": {
            "A": "Morphine 仍是癌末中重度疼痛重要首選，但需監測嗜睡、便祕與呼吸抑制等副作用。",
            "B": "Morphine 可減輕呼吸困難，但起始劑量通常低於或謹慎相對於止痛劑量，不是止痛劑量雙倍，故錯誤。",
            "C": "類固醇可改善腸阻塞、水腫或顱內壓升高造成的嘔吐，敘述正確。",
            "D": "Dopamine antagonist 如 metoclopramide、haloperidol 等可用於某些難治性噁心嘔吐，敘述正確。",
        },
        "core": "鴉片類可治療呼吸困難，但要低劑量開始、逐步滴定。",
        "key": "癌末呼吸困難使用 morphine 不應以止痛劑量雙倍作起始。",
    },
    79: {
        "topic": "不予急救與病人自主",
        "analysis": "本案病人先前清楚表達病情惡化時不願插管，雖未簽署文件，家屬仍應尊重病人已知意願，協助完成不予急救同意書或相關程序，而不是以子女意見取代病人意願。",
        "options": {
            "A": "沒有文件不代表可忽略病人已明確表達的意願；醫療決策應優先尊重病人自主。",
            "B": "病人曾口頭明確表示不願急救，家屬應依其意願簽署不予急救同意書，敘述正確。",
            "C": "若已插管，仍可依法律與醫療倫理程序討論撤除或終止維生醫療，不能說一定不得撤除。",
            "D": "不予急救與撤除維生醫療在安寧緩和醫療條例中同屬末期病人生命維持處置脈絡，不宜說適用完全不同規範作為本案正解。",
        },
        "core": "末期醫療決策優先尊重病人已知意願；家屬角色是協助呈現病人意願，不是改寫它。",
        "key": "病人曾明確口頭表達 DNR 意願時，家屬應協助遵照其意願。",
    },
    80: {
        "topic": "代理醫療決定",
        "analysis": "當病人無意識且未留下明確指示時，代理人應採 substituted judgment：根據自己對病人價值觀、偏好與人生目標的了解，選擇病人最可能想要的治療，而不是代理人自己的偏好。",
        "options": {
            "A": "這是代理人把自己放進病人情境的選擇，容易變成代理人偏好，不是最優先。",
            "B": "醫療效果很重要，但代理決定不只看醫學最佳，還要符合病人價值觀。",
            "C": "依據對病人的了解選擇病人最希望的治療，符合 substituted judgment，是最優先考量。",
            "D": "多數人能接受的選擇不一定符合個別病人的價值與意願，不能優先於病人中心判斷。",
        },
        "core": "代理決定第一原則是 substituted judgment；無法得知時才退而求其次用 best interest。",
        "key": "醫療代理人應優先依病人價值觀作替代判斷。",
    },
}


def build_explanation(item):
    return (
        f"【題幹解析】\n{item['analysis']}\n\n"
        "【選項詳解】\n"
        f"- A. {item['options']['A']}\n"
        f"- B. {item['options']['B']}\n"
        f"- C. {item['options']['C']}\n"
        f"- D. {item['options']['D']}\n\n"
        f"【核心考點】\n{item['core']}"
    )


def main():
    exam = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    by_number = {q["question_number"]: q for q in exam["questions"]}
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for start in range(1, 81, 10):
        end = start + 9
        updates = []
        for number in range(start, end + 1):
            q = by_number[number]
            item = DATA[number]
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": number,
                    "explanation": build_explanation(item),
                    "key_point": item["key"],
                    "flashcard_front": item["topic"],
                    "flashcard_back": item["key"],
                    "flashcard_summary": f"{item['topic']}：{item['key']}",
                    "review_status": "ai_generated",
                    "explanation_model": "codex-high-quality-rewrite",
                    "explanation_generated_at": STAMP,
                    "manual_review_notes": [],
                }
            )
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates,
        }
        out_path = OUT_DIR / f"q{start:03d}-q{end:03d}.json"
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
