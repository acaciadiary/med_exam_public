import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/113-1/medicine-5.json"
DATASET_ID = "113-1_medicine-5"
OUT_DIR = Path("scratch/rewrite_updates/113-1_medicine-5")
STAMP = "2026-07-16T00:00:00+08:00"


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def make_explanation(analysis, options, core):
    return (
        "【題幹解析】\n"
        + analysis.strip()
        + "\n\n【選項詳解】\n"
        + "\n".join(f"- {letter}. {text.strip()}" for letter, text in options.items())
        + "\n\n【核心考點】\n"
        + core.strip()
    )


DATA = {
    31: {
        "analysis": "題目問哪一種減重手術同時具有限制進食量（restriction）與造成部分吸收不良（malabsorption）的效果。Roux-en-Y 胃繞道會做出小胃囊並繞過部分近端小腸，因此同時符合兩種機轉。",
        "options": {
            "A": "腹腔鏡調節式胃束帶（AGB）主要靠束帶縮小胃入口、限制食量，屬於 restrictive procedure，沒有腸道繞道造成的吸收不良。",
            "B": "Roux-en-Y 胃腸繞道（RYGB）以小胃囊限制攝食，並讓食物繞過部分胃、十二指腸與近端空腸，兼具 restriction 與 malabsorption，最符合題意。",
            "C": "垂直束帶胃成形術主要也是限制胃容量，沒有典型的小腸繞道吸收不良效果。",
            "D": "胃內水球是內視鏡暫時性占位裝置，機轉是增加飽足感與限制攝食，並非吸收不良型手術。",
        },
        "core": "減重手術分類要抓機轉：胃束帶、胃水球、垂直束帶胃成形偏 restrictive；Roux-en-Y gastric bypass 同時有小胃囊與腸道繞道，所以是 restriction plus malabsorption。",
        "key": "Roux-en-Y gastric bypass 同時具有限制攝食與部分吸收不良效果。",
        "summary": "Bariatric surgery -> RYGB = restriction + malabsorption",
        "front": "減重手術：哪一種兼具 restriction 與 malabsorption？",
        "back": "Roux-en-Y 胃繞道；小胃囊限制攝食，腸道繞道造成部分吸收不良。",
    },
    32: {
        "analysis": "題目問肝硬化臨床表徵何者錯誤。肝硬化可有雌激素代謝下降、門脈高壓、hyperdynamic circulation；肌肉痙攣常與有效循環量不足、低血壓傾向與利尿劑等因素相關，不是高平均動脈壓。",
        "options": {
            "A": "正確。蜘蛛痣與手掌紅斑常與肝臟對性荷爾蒙代謝下降、雌激素效應增加有關。",
            "B": "大方向是門脈高壓造成臍周側枝循環與腹壁雜音；嚴格說常見描述是再通的臍靜脈而非臍動脈，題目官方答案未選此項，建議保留文字疑義。",
            "C": "正確。肝硬化常有 hyperdynamic circulation，表現為心輸出量與心跳上升、周邊血管阻力下降。",
            "D": "錯誤。肝硬化肌肉痙攣常見於有效動脈血容量不足、腹水、利尿劑使用與腎素-血管張力素系統活化；高平均動脈壓不是典型關聯。",
        },
        "core": "肝硬化不是只有肝功能差，也會造成門脈高壓與全身血流動力學改變。肌肉痙攣多與低有效循環量、電解質與利尿治療相關，看到高平均動脈壓要警覺。",
        "key": "肝硬化肌肉痙攣不典型由高平均動脈壓造成；常與有效循環量不足、腹水與利尿劑相關。",
        "summary": "Cirrhosis signs -> muscle cramps relate to low effective volume, not high MAP",
        "front": "肝硬化肌肉痙攣的典型關聯？",
        "back": "常與腹水、利尿劑、低有效循環量與 RAAS 活化有關；不是高平均動脈壓。",
        "notes": ["Q32 選項 B 使用「臍動脈」描述 Cruveilhier-Baumgarten murmur，常規應為臍靜脈/臍旁靜脈，建議人工確認題目文字。"],
    },
    33: {
        "analysis": "本題考 Crohn disease 的流行病學與腸外表現。Crohn disease 是慢性復發性發炎性腸病，不會靠手術根治；可侵犯從口腔到肛門的任何部位，抽菸是重要危險因子。",
        "options": {
            "A": "錯誤。Crohn disease 可因狹窄、瘻管或膿瘍接受手術，但手術不能治癒疾病，術後仍可能復發。",
            "B": "錯誤。Crohn disease 可侵犯整個消化道，最常見在末端迴腸與右側大腸，不是主要只侵犯大腸；主要侵犯大腸較符合 ulcerative colitis。",
            "C": "正確。Crohn disease 在已開發國家、較高社經族群較常見，抽菸會增加發病與復發風險。",
            "D": "不精確。Crohn disease 可有腸外表現，但 pyoderma gangrenosum、ankylosing spondylitis 常不一定與腸道發炎嚴重度平行；周邊關節炎等才較常與腸道活動度相關。",
        },
        "core": "Crohn disease 的考點是跳躍性、全層發炎、可侵犯全消化道，抽菸是危險因子且手術不能根治。腸外表現要分辨是否與腸道活動度平行。",
        "key": "Crohn disease 不能以手術根治，抽菸是危險因子，常侵犯末端迴腸與右側大腸。",
        "summary": "Crohn disease -> smoking risk, transmural skip lesions, surgery not curative",
        "front": "Crohn disease：抽菸與手術治癒性？",
        "back": "抽菸是危險因子；手術處理併發症但不能根治，仍可能復發。",
    },
    34: {
        "analysis": "胃神經內分泌腫瘤來自胃黏膜的 enterochromaffin-like cell 等神經內分泌細胞，與 GIST 的 interstitial cell of Cajal 不同。題目問錯誤敘述，因此來源細胞混淆是關鍵。",
        "options": {
            "A": "錯誤。interstitial cell of Cajal 是胃腸道基質瘤（GIST）的來源，不是胃神經內分泌腫瘤的來源。",
            "B": "正確。Type II gastric NET 與 gastrinoma、Zollinger-Ellison syndrome 及 MEN1 相關。",
            "C": "正確。局部可切除的胃神經內分泌腫瘤治療重點是完整切除，依型別、大小、侵犯深度決定內視鏡或手術方式。",
            "D": "正確。Type III 通常為散發型、與高胃泌素血症無關，惡性度與轉移風險較高，預後最差。",
        },
        "core": "Gastric NET 與 GIST 的來源要分清楚：NET 是神經內分泌細胞，GIST 才是 Cajal cell。胃 NET 的 type III 最具侵襲性。",
        "key": "Interstitial cell of Cajal 是 GIST 來源，不是胃神經內分泌腫瘤來源。",
        "summary": "Gastric NET -> ECL/neuroendocrine cells, not Cajal cells",
        "front": "胃神經內分泌腫瘤與 GIST 的來源細胞差異？",
        "back": "胃 NET 來自神經內分泌細胞；GIST 才來自 interstitial cell of Cajal。",
    },
    35: {
        "analysis": "35 歲女性長期使用口服避孕藥、肝臟 6 公分腫瘤且腹腔內有少量液體，官方答案指向肝細胞腺瘤破裂或出血。題幹的影像描述 peripheral enhancement with centripetal progression 較像血管瘤，因此本題需保留人工確認註記。",
        "options": {
            "A": "官方答案。Hepatocellular adenoma 好發年輕女性，與口服避孕藥及同化類固醇相關；較大的腺瘤有出血、破裂與少數惡性轉化風險，可造成急性腹痛與腹腔液體。",
            "B": "錯誤。Focal nodular hyperplasia 多為中心疤痕、放射狀血管供應，通常不與口服避孕藥造成的出血破裂強烈連結。",
            "C": "錯誤。Hamartoma 不是此類年輕女性 OCP 相關、急性疼痛肝腫瘤的典型診斷。",
            "D": "需注意。Hemangioma 的典型影像確實是 peripheral nodular enhancement with centripetal fill-in，但題目同時給 OCP、6 公分與腹腔液體，官方答案採肝細胞腺瘤邏輯。",
        },
        "core": "年輕女性長期 OCP + 肝腫瘤 + 急性腹痛/出血風險，要想到 hepatocellular adenoma；但 peripheral enhancement with centripetal progression 是 hemangioma 的典型影像語，需人工核對官方題目。",
        "key": "OCP 相關、可出血破裂的良性肝腫瘤是 hepatocellular adenoma。",
        "summary": "Liver tumor + OCP + hemorrhage risk -> hepatocellular adenoma",
        "front": "年輕女性長期 OCP，肝腫瘤急性腹痛與出血風險？",
        "back": "優先考 hepatocellular adenoma；但若影像是典型向心性填充，需鑑別 hemangioma。",
        "notes": ["Q35 影像描述 peripheral enhancement with centripetal progression 典型較像 hemangioma，但官方答案為 liver cell adenoma，建議人工確認。"],
    },
    36: {
        "analysis": "Charcot triad 是急性膽管炎的經典三徵：發燒、黃疸、右上腹痛。若再加上低血壓與意識改變，稱 Reynolds pentad，代表病情更嚴重。",
        "options": {
            "A": "發燒是 Charcot triad 的一項，反映膽道感染與菌血症風險。",
            "B": "黃疸是 Charcot triad 的一項，來自膽道阻塞造成膽紅素上升。",
            "C": "右上腹腫塊不是 Charcot triad；膽管炎典型是疼痛而非摸到腫塊。",
            "D": "右上腹痛是 Charcot triad 的一項，常與膽道阻塞及發炎有關。",
        },
        "core": "Charcot triad = fever + jaundice + right upper quadrant pain；不要把右上腹腫塊混入三徵。",
        "key": "Charcot triad 包含發燒、黃疸、右上腹痛，不包含右上腹腫塊。",
        "summary": "Acute cholangitis -> Charcot triad = fever, jaundice, RUQ pain",
        "front": "急性膽管炎 Charcot triad？",
        "back": "發燒、黃疸、右上腹痛。",
    },
    37: {
        "analysis": "BD-IPMN 的 high-risk stigmata 包括阻塞性黃疸、增強 mural nodule >=5 mm、主胰管明顯擴張（約 >=10 mm）。發燒不是判斷 BD-IPMN 惡性風險的 high-risk feature。",
        "options": {
            "A": "Jaundice 若由胰頭囊性病灶造成，屬 high-risk stigmata，提示可能已有阻塞與惡性風險。",
            "B": "Fever 不是 IPMN 惡性風險分層的 high-risk feature；除非另有感染或膽管炎情境，不能用來判定 IPMN 高風險。",
            "C": "主胰管大於 1 cm 是 high-risk stigmata，提示 main duct involvement 或高惡性風險。",
            "D": "Enhancing mural nodule 大於 5 mm 是 high-risk stigmata，與惡性或高度異生風險相關。",
        },
        "core": "IPMN high-risk features 看阻塞性黃疸、主胰管顯著擴張與增強壁結節；發燒不是標準惡性風險特徵。",
        "key": "BD-IPMN high-risk feature 不包括 fever。",
        "summary": "BD-IPMN -> high-risk: jaundice, MPD >=10 mm, enhancing mural nodule >=5 mm",
        "front": "BD-IPMN high-risk feature 不包括？",
        "back": "Fever；高風險重點是阻塞性黃疸、主胰管 >=10 mm、增強壁結節 >=5 mm。",
    },
    38: {
        "analysis": "病人血鈣 15.5 mg/dL、PTH 明顯升高且有意識改變，符合嚴重高血鈣危象。第一步是恢復血容量、增加腎臟鈣排泄，因此先大量 isotonic saline 補液。",
        "options": {
            "A": "Furosemide 不是一開始就連續使用；若未先補足血容量，會加重脫水與腎功能惡化。利尿劑只在補液後、容量過多時謹慎考慮。",
            "B": "正確。Normal saline rehydration 是嚴重高血鈣急性處置第一步，可矯正脫水並促進 calciuresis。",
            "C": "副甲狀腺切除可作為根本治療，但急診初始處置仍需先穩定病人與降鈣，不是第一個動作。",
            "D": "Cinacalcet 可用於部分副甲狀腺功能亢進控制，但口服起效較慢，不適合取代高血鈣危象初期補液。",
        },
        "core": "嚴重高血鈣急救先補 isotonic saline；等容量恢復後才考慮其他降鈣策略。不要一開始就給 loop diuretic。",
        "key": "高血鈣危象初始處置是 normal saline rehydration。",
        "summary": "Severe hypercalcemia -> first step normal saline hydration",
        "front": "嚴重高血鈣危象第一步處置？",
        "back": "先以 normal saline 補液，恢復血容量並促進尿鈣排泄。",
    },
    39: {
        "analysis": "術後 TSH 稍高、free T4 正常是亞臨床甲狀腺低下。是否補充 thyroxine 取決於懷孕、症狀、TSH 高度、甲狀腺腫或結節等；TSH receptor antibody 是 Graves disease 相關抗體，不是補充甲狀腺素的典型理由。",
        "options": {
            "A": "懷孕時甲狀腺素需求增加，亞臨床低下也可能影響母胎，通常較積極補充。",
            "B": "剩餘甲狀腺有結節或腫大時，可考慮補充或追蹤，以避免 TSH 刺激與處理低下狀態。",
            "C": "冠心病患者若補充需低劑量慢慢調整；但亞臨床低下與心血管風險相關，臨床上會納入治療考量。",
            "D": "TSH receptor antibody 主要支持 Graves disease/自體免疫甲亢相關診斷，不是此病人術後亞臨床低下需補充 thyroxine 的理由。",
        },
        "core": "亞臨床甲狀腺低下補不補，要看 TSH 高度、懷孕、症狀、抗 TPO、甲狀腺腫與心血管因素；TRAb 是 Graves 相關，不是低下補充的典型指標。",
        "key": "TSH receptor antibody 不是術後亞臨床甲狀腺低下補充 thyroxine 的典型適應症。",
        "summary": "Subclinical hypothyroidism -> TRAb is not a usual indication for thyroxine",
        "front": "亞臨床甲狀腺低下補 thyroxine：哪個不是典型理由？",
        "back": "TSH receptor antibody；它主要與 Graves disease 相關。",
    },
    40: {
        "analysis": "12 歲男童嚴重高血壓、尿 VMA 上升、腎上腺腫塊，最像嗜鉻細胞瘤。術前需先 alpha blockade 控制血壓，再視情況加 beta blocker；spironolactone 不是嗜鉻細胞瘤術前標準降壓準備。",
        "options": {
            "A": "最不適當。Spironolactone 用於原發性醛固酮症等 mineralocorticoid 相關高血壓；嗜鉻細胞瘤術前應以 alpha blocker（如 phenoxybenzamine 或 doxazosin）為核心。",
            "B": "可接受。腎上腺嗜鉻細胞瘤在充分術前準備後可手術切除，許多病例可採腹腔鏡，是否開腹需依大小、侵犯與惡性疑慮判斷。",
            "C": "正確。術中高血壓危象可用 nitroprusside、phentolamine 等快速降壓藥控制。",
            "D": "正確。若術後復發或懷疑多發/轉移病灶，MIBG scan 可用於偵測嗜鉻細胞瘤或副神經節瘤病灶。",
        },
        "core": "嗜鉻細胞瘤手術前先 alpha blockade，再補足血容量；不能用 spironolactone 取代 alpha blockade。",
        "key": "嗜鉻細胞瘤術前降壓準備首重 alpha blockade，不是 spironolactone。",
        "summary": "Pheochromocytoma -> pre-op alpha blockade, not spironolactone",
        "front": "嗜鉻細胞瘤術前降壓準備？",
        "back": "先 alpha blockade（如 phenoxybenzamine/doxazosin）並補足血容量。",
    },
    41: {
        "analysis": "保留乳房治療需能完整切除腫瘤並保留可接受外觀，且病灶不應是多中心、瀰漫或無法定位清除。多處不在同一象限的不確定顯微鈣化代表可能多中心病灶，較不適合保乳。",
        "options": {
            "A": "E 罩杯且腫瘤約 2 公分，通常有機會達到足夠切緣與可接受外觀，不是保乳禁忌。",
            "B": "腋下淋巴結轉移不是保乳的絕對禁忌；可搭配腋下處置、全身治療與放射治療。",
            "C": "最不適合。多處且不在同一象限的可疑顯微鈣化，可能代表 multicentric disease 或廣泛 DCIS，難以用單一局部切除達到安全切緣。",
            "D": "侵犯性乳癌本身不等於不能保乳；早期單一病灶可採乳房保留手術合併放射治療。",
        },
        "core": "保乳禁忌重點是多中心病灶、瀰漫可疑鈣化、無法取得陰性切緣或無法接受放療；淋巴結陽性或侵犯性乳癌本身不是絕對禁忌。",
        "key": "多象限可疑顯微鈣化最不適合乳房保留治療。",
        "summary": "Breast-conserving therapy -> multicentric suspicious microcalcifications are unfavorable",
        "front": "乳癌何者最不適合保留乳房？",
        "back": "多處、不同象限的可疑顯微鈣化，因可能多中心或廣泛 DCIS。",
    },
    42: {
        "analysis": "乳房攝影是族群篩檢主要工具，但在緻密乳房中敏感度下降，這也是年輕女性篩檢效果較差的原因之一。題目問錯誤敘述，C 把緻密乳房的影響說反了。",
        "options": {
            "A": "正確。Mammography 是歐美乳癌大量篩檢最常用且證據最完整的工具。",
            "B": "正確。乳房超音波受操作者影響，較不適合作為單獨大規模篩檢工具，但可作為特定族群或診斷輔助。",
            "C": "錯誤。Mammography 在緻密乳房的敏感度較差，不是較好；50 歲以上效果較好，部分原因是乳房密度下降、腫瘤生長速度與基礎風險不同。",
            "D": "正確。50 歲以下篩檢效益較受限制，原因包括乳房較緻密、偽陽性較多，以及部分腫瘤生長較快。",
        },
        "core": "Mammography 在脂肪性乳房較容易看出病灶，在 dense breast 敏感度下降；年輕女性常因乳房較緻密而篩檢表現較差。",
        "key": "緻密乳房會降低 mammography 敏感度。",
        "summary": "Mammography -> dense breasts reduce sensitivity",
        "front": "Mammography 在緻密乳房的敏感度？",
        "back": "下降；緻密組織會遮蔽病灶。",
    },
    43: {
        "analysis": "21 歲女性、超音波 BI-RADS 2 且疑似 fibroadenoma，屬良性影像。年輕女性乳房緻密，通常以超音波追蹤為主，不會優先安排乳房攝影。",
        "options": {
            "A": "可考慮。雖 BI-RADS 2 多為良性，若症狀或臨床判斷需要，可安排 6-12 個月超音波追蹤確認穩定。",
            "B": "較不考慮。21 歲乳房緻密且輻射暴露需斟酌，BI-RADS 2 良性病灶通常不需進一步 mammography。",
            "C": "可視情況考慮。若病灶快速變大、影像不典型或病人焦慮，可安排 core needle biopsy，但不是每例必要。",
            "D": "可考慮。疼痛困擾可給止痛藥與支持性處置，並追蹤症狀。",
        },
        "core": "年輕女性疑似纖維腺瘤且 BI-RADS 2，以超音波與臨床追蹤為主；mammography 通常不是第一線。",
        "key": "21 歲 BI-RADS 2 疑似 fibroadenoma，較不需乳房攝影。",
        "summary": "Young fibroadenoma BI-RADS 2 -> ultrasound follow-up, not routine mammography",
        "front": "21 歲疑似 fibroadenoma，BI-RADS 2，較不考慮？",
        "back": "乳房攝影；年輕乳房緻密且良性影像，多以超音波追蹤。",
    },
    44: {
        "analysis": "幼兒嘔吐合併腹部 X 光若呈現近端腸阻塞或 double bubble，鑑別常包括十二指腸蹼、環狀胰與腸旋轉不良併扭轉。胃蹼造成的是胃出口或胃內阻塞，較不符合典型十二指腸阻塞鑑別。",
        "options": {
            "A": "最不可能。Gastric web 位於胃，通常造成胃出口相關阻塞，不是典型 double bubble/十二指腸阻塞影像的主要鑑別。",
            "B": "十二指腸蹼可造成近端十二指腸阻塞，是幼兒嘔吐與 double bubble 的重要鑑別。",
            "C": "環狀胰會壓迫十二指腸第二部，造成十二指腸阻塞，是典型鑑別。",
            "D": "腸旋轉不良併中腸扭轉可造成近端腸阻塞與膽汁性嘔吐，需列入急症鑑別。",
        },
        "core": "幼兒近端十二指腸阻塞的鑑別包含 duodenal web、annular pancreas、malrotation with volvulus；gastric web 較不像同一組典型鑑別。",
        "key": "幼兒疑似十二指腸阻塞時，胃蹼是較不可能的鑑別。",
        "summary": "Pediatric proximal obstruction -> duodenal web/annular pancreas/malrotation, not gastric web",
        "front": "幼兒近端十二指腸阻塞較不可能鑑別？",
        "back": "胃蹼；典型要想到十二指腸蹼、環狀胰、腸旋轉不良併扭轉。",
    },
    45: {
        "analysis": "本題考鼠蹊部疝氣的解剖。兒童常見間接型鼠蹊疝氣，從腹壁下動脈外側經內鼠蹊環進入；提睪肌來自腹內斜肌，是正確敘述。",
        "options": {
            "A": "錯誤。間接型鼠蹊疝氣從 inferior epigastric vessels 外側突出，直接型才在其內側、Hesselbach triangle。",
            "B": "錯誤。Iliohypogastric nerve 不與精索一起穿出外鼠蹊環；大腿內側上方感覺較與 ilioinguinal/genitofemoral 分支相關。",
            "C": "正確。Cremaster muscle 主要由 internal oblique muscle 延伸而來，包繞精索與睪丸。",
            "D": "錯誤。Testicular artery 直接來自主動脈腹部段，不是內髂動脈。",
        },
        "core": "鼠蹊疝氣解剖要記 inferior epigastric vessels 內外側：indirect 在外側，direct 在內側；cremaster 來自 internal oblique。",
        "key": "提睪肌由腹內斜肌延伸而來。",
        "summary": "Inguinal anatomy -> cremaster from internal oblique",
        "front": "提睪肌來源？間接疝與腹壁下動脈的位置？",
        "back": "提睪肌來自腹內斜肌；間接疝在 inferior epigastric vessels 外側。",
    },
    46: {
        "analysis": "頸部胸鎖乳突肌前緣皮膚小開口並有分泌物，是第二鰓裂瘻管的典型位置。甲狀舌管瘻管則多在頸中線，會隨吞嚥或伸舌移動。",
        "options": {
            "A": "錯誤。甲狀舌管瘻管通常位於頸部中線，與舌骨、甲狀舌管殘跡相關，不是胸鎖乳突肌前緣側頸開口。",
            "B": "正確。Second branchial remnant fistula 常在胸鎖乳突肌前緣有外口，可有黏液樣分泌物或反覆感染。",
            "C": "錯誤。淋巴結發炎可有腫痛紅熱，但不典型形成先天性小開口與持續分泌物。",
            "D": "錯誤。淋巴管瘤多為柔軟囊性腫塊，常在後頸三角，不是典型皮膚瘻管開口。",
        },
        "core": "側頸、胸鎖乳突肌前緣的小開口與分泌物，優先想到第二鰓裂瘻管；中線病灶才想到甲狀舌管。",
        "key": "第二鰓裂瘻管常在胸鎖乳突肌前緣有皮膚開口與分泌物。",
        "summary": "Lateral neck opening anterior to SCM -> second branchial cleft fistula",
        "front": "胸鎖乳突肌前緣小開口有分泌物，最可能？",
        "back": "第二鰓裂遺跡瘻管。",
    },
    47: {
        "analysis": "1 歲半外傷兒童昏迷、低血壓、低血氧，GCS E1V1M4 約 6 分，屬需積極處置的重症外傷。GCS <=8、無法保護呼吸道或氧合不佳時應插管，不能因仍有自發呼吸就不插管。",
        "options": {
            "A": "錯誤。GCS 約 6 分且血氧 90%、休克，不能視為呼吸道安全；兒童重症外傷需保護 airway，插管是合理處置。",
            "B": "正確。Primary/secondary survey 要全身檢查，尋找外傷、內出血與可壓迫止血來源。",
            "C": "正確。10 kg 兒童 isotonic crystalloid 20 mL/kg 約 200 mL；多次輸液仍休克需及早輸血。",
            "D": "正確。穩定或初步復甦後可用全身 CT 評估多重外傷，但不能延誤復甦。",
        },
        "core": "兒童外傷先 ABC。GCS <=8 或氧合差代表不能保護呼吸道，需插管；休克復甦以 20 mL/kg 等張液起步，無效則輸血。",
        "key": "兒童重症外傷 GCS <=8 不應因有自發呼吸就延後插管。",
        "summary": "Pediatric trauma -> GCS <=8 needs airway protection",
        "front": "兒童外傷 GCS 約 6 分但仍自發呼吸，可以不插管嗎？",
        "back": "不可以；GCS <=8/氧合差需保護呼吸道。",
    },
    48: {
        "analysis": "承上題，兒童外傷輸血後血壓改善但仍需監測。胸管立即引流量是否需開胸，兒童通常看大量初始血胸或持續出血；10 kg 兒童 230 mL 約 23 mL/kg，未必一放出就等同立即開胸，需看持續出血與生命徵象。",
        "options": {
            "A": "正確。意識不清即使初始 CT 無出血，仍需追蹤 GCS、瞳孔與神經變化，惡化時重做頭部 CT。",
            "B": "正確。外傷休克復甦後仍要追蹤抽血、生命徵象、尿量與輸血反應。",
            "C": "正確。兒童可有肺挫傷或血胸而沒有明顯肋骨骨折；影像與氧合狀態需綜合判斷。",
            "D": "錯誤。胸管初始 230 mL 血性引流在 10 kg 兒童需嚴密評估，但是否立即開胸通常取決於大量初始出血、持續出血速率與血流動力學，不是單看此數字立刻開胸。",
        },
        "core": "外傷性血胸開胸適應症看大量初始引流、持續高流量出血與休克。兒童要用體重換算並看趨勢，不能只因一次引流就直接開胸。",
        "key": "兒童血胸是否開胸要看引流量/體重、持續出血與生命徵象。",
        "summary": "Traumatic hemothorax -> thoracotomy depends on massive or ongoing bleeding",
        "front": "兒童外傷血胸，胸管初始引流後一定立刻開胸嗎？",
        "back": "不一定；需看大量/持續出血、體重換算與血流動力學。",
    },
    49: {
        "analysis": "兒童腸套疊最常見為迴盲部套疊，典型表現為陣發性腹痛、嘔吐、血便與香腸狀腫塊。無腹膜炎或穿孔時，空氣或水溶性/靜水壓灌腸復位常是第一線治療。",
        "options": {
            "A": "錯誤。2 的法則是 Meckel diverticulum 的記憶口訣，不是腸套疊的主要臨床表現。",
            "B": "錯誤。99mTc-pertechnetate scan 用於偵測含異位胃黏膜的 Meckel diverticulum，不是腸套疊確診首選。",
            "C": "錯誤。最常見先天性胃腸道畸形是 Meckel diverticulum，不是腸套疊。",
            "D": "正確。大多數單純性腸套疊可用影像導引的 hydrostatic 或 pneumatic reduction，若有腹膜炎、穿孔或復位失敗才手術。",
        },
        "core": "腸套疊與 Meckel diverticulum 常被混考：2 的法則與 99mTc scan 是 Meckel；單純腸套疊治療常先灌腸復位。",
        "key": "單純性腸套疊多可先做 hydrostatic/pneumatic reduction。",
        "summary": "Intussusception -> nonoperative enema reduction for uncomplicated cases",
        "front": "單純性兒童腸套疊第一線處置？",
        "back": "影像導引空氣或靜水壓灌腸復位。",
    },
    50: {
        "analysis": "糞便潛血陽性後大腸鏡發現 1 公分有莖性息肉，最適當是內視鏡息肉切除並送病理。僅切片或觀察會留下可能腺瘤性病灶與癌化風險。",
        "options": {
            "A": "正確。Pedunculated polyp 通常可直接內視鏡 polypectomy，兼具診斷與治療。",
            "B": "錯誤。只切片無法完整移除息肉，也可能漏掉局部高級別病變或早期癌。",
            "C": "錯誤。1 公分有莖性息肉沒有侵犯癌證據時，不需直接做腹腔鏡前位切除。",
            "D": "錯誤。糞便潛血陽性且已見息肉，不應單純觀察，應切除並病理檢查。",
        },
        "core": "大腸鏡看到可切除息肉，標準處置是 polypectomy 並送病理；手術保留給不可內視鏡切除或疑似侵犯癌等情境。",
        "key": "1 公分有莖性大腸息肉最適當處置是內視鏡息肉切除。",
        "summary": "Pedunculated colon polyp -> endoscopic polypectomy",
        "front": "1 公分有莖性乙狀結腸息肉處置？",
        "back": "內視鏡息肉切除並送病理。",
    },
    51: {
        "analysis": "Pelvic floor 主要包括 levator ani 與 coccygeus。Levator ani 由 puborectalis、pubococcygeus、iliococcygeus 組成；gluteus maximus 是臀大肌，不屬於骨盆底肌群。",
        "options": {
            "A": "Puborectalis 是 levator ani 的一部分，維持 anorectal angle 與 continence。",
            "B": "Iliococcygeus 是 levator ani 的一部分，屬骨盆底肌群。",
            "C": "Pubococcygeus 是 levator ani 的一部分，屬骨盆底肌群。",
            "D": "Gluteus maximus 是臀部伸髖肌，不是 pelvic floor 的組成。",
        },
        "core": "骨盆底肌群記 levator ani：puborectalis、pubococcygeus、iliococcygeus；臀大肌不在其中。",
        "key": "Gluteus maximus 不屬於 pelvic floor。",
        "summary": "Pelvic floor -> levator ani, not gluteus maximus",
        "front": "Pelvic floor 不包括哪個肌肉？",
        "back": "Gluteus maximus；骨盆底重點是 levator ani 三肌。",
    },
    52: {
        "analysis": "降結腸位於左側腹，手術游離 splenic flexure 時容易牽扯脾臟與脾周韌帶。降結腸癌手術大出血最常見原因是脾臟撕裂傷。",
        "options": {
            "A": "正確。左側結腸與脾彎游離時可能造成 splenic capsular tear，是降結腸/左側結腸手術常見大出血來源。",
            "B": "錯誤。上腸繫膜靜脈較接近右側結腸、小腸與胰頭區域，不是降結腸癌手術最常見出血原因。",
            "C": "錯誤。下腔靜脈位於後腹腔中線偏右，受傷嚴重但不是降結腸手術最常見原因。",
            "D": "錯誤。主動脈撕裂罕見且災難性，非一般降結腸癌手術最常見大出血來源。",
        },
        "core": "左側結腸手術要小心脾彎與脾臟被膜，splenic injury 是重要出血併發症。",
        "key": "降結腸癌手術大出血最常見原因是脾臟撕裂傷。",
        "summary": "Descending colon surgery bleeding -> splenic tear",
        "front": "降結腸癌手術大出血常見原因？",
        "back": "脾臟撕裂傷，尤其在脾彎游離時。",
    },
    53: {
        "analysis": "本題是組合題。腹腔鏡闌尾切除可檢視腹腔、傷口感染較少且恢復較快；開放手術不能像腹腔鏡一樣完整檢查腹腔。延遲性闌尾炎若形成膿瘍，腹腔鏡或影像導引引流可能有角色，不能說完全沒有助益。",
        "options": {
            "A": "不對。ћ 與 ѝ 為合理敘述，但 ќ 是錯的，故此組合不完整。",
            "B": "不對。ћ 合理，但 ќ 與 ў 為錯誤敘述；題目問錯誤者，還需排除 ћ。",
            "C": "不對。ќ 錯，但 ѝ 是安全手術原則，並非錯誤敘述。",
            "D": "正確。ќ 錯在開放式闌尾切除不能像腹腔鏡一樣檢查整個腹膜腔；ў 錯在延遲性闌尾炎/膿瘍時引流可能有幫助，不能一概不施行。",
        },
        "core": "腹腔鏡闌尾切除的優勢包括較好腹腔檢視與較少傷口感染。延遲性闌尾炎合併膿瘍時，治療策略可包含抗生素與引流，不能說腹腔鏡引流一定無益。",
        "key": "闌尾切除比較題中，錯誤敘述為 ќ 與 ў。",
        "summary": "Appendectomy comparison -> false statements: open explores whole cavity; drainage never useful",
        "front": "腹腔鏡 vs 開放式闌尾切除：哪兩句錯？",
        "back": "ќ 與 ў；完整腹腔檢視是腹腔鏡優勢，延遲性膿瘍可考慮引流。",
    },
    54: {
        "analysis": "腹腔鏡手術多用 CO2 氣腹，但壓力通常約 12-15 mmHg，不是 25 mmHg。其他敘述關於急性膽囊炎手術較困難、NG 減壓、膽道攝影方式與污染結石取出原則皆合理。",
        "options": {
            "A": "不完整。ћ、ѝ、ў 正確，但漏掉 џ。",
            "B": "錯誤。ќ 說氣腹壓力 25 mmHg 過高，不是正確敘述。",
            "C": "錯誤。包含 ќ，因此整組不正確。",
            "D": "正確。ћ、ѝ、ў、џ 為正確敘述；排除錯誤的 ќ。",
        },
        "core": "腹腔鏡 CO2 pneumoperitoneum 常用壓力約 12-15 mmHg。急性膽囊炎較困難，必要時做 cholangiogram；膽囊破裂要用取物袋並清除散落結石。",
        "key": "腹腔鏡氣腹壓力通常約 12-15 mmHg，25 mmHg 過高。",
        "summary": "Laparoscopy -> CO2 pneumoperitoneum usually 12-15 mmHg",
        "front": "腹腔鏡常用 CO2 氣腹壓力？",
        "back": "約 12-15 mmHg；25 mmHg 不是常規設定。",
    },
    55: {
        "analysis": "單孔腹腔鏡容易發生器械在體內外互相碰撞，因此需要長短不一、細長且高品質影像設備來改善操作。題目問錯誤敘述，B 把 varied-length instruments 的好處說反。",
        "options": {
            "A": "正確。較長器械可達到手術區域並增加操作角度。",
            "B": "錯誤。長短不一的器械可錯開手柄位置，減少體外器械碰撞，並改善單孔手術的 ergonomics。",
            "C": "正確。高畫質鏡頭可改善視野，對單孔手術尤其重要。",
            "D": "正確。Slimline instruments 有助於減少體內與體外碰撞。",
        },
        "core": "Single-incision laparoscopic surgery 的限制是 triangulation 變差與器械碰撞；長短不一、細長器械與好鏡頭可降低困難。",
        "key": "Varied-length instruments 可減少單孔腹腔鏡體外器械碰撞。",
        "summary": "Single-incision laparoscopy -> varied-length instruments reduce clashing",
        "front": "單孔腹腔鏡為何使用長短不一器械？",
        "back": "錯開手柄、減少體外碰撞並改善操作。",
    },
    56: {
        "analysis": "本題考骨腫瘤好發年齡與部位。Chondroblastoma 典型發生於青少年、長骨骨骺。其他選項混淆 Ollier 與 Maffucci、GCT 復發率與 simple bone cyst 好發族群。",
        "options": {
            "A": "錯誤。Ollier disease 是多發性 enchondromatosis；若合併血管瘤，稱 Maffucci syndrome。",
            "B": "正確。Chondroblastoma 好發於青少年長骨 epiphysis，如股骨遠端、脛骨近端、肱骨近端。",
            "C": "錯誤。Giant cell tumor 可局部侵襲且刮除後有復發風險，不能說復發率極低。",
            "D": "錯誤。Simple bone cyst 好發於兒童與青少年，常在肱骨近端或股骨近端，不是成年人肱骨遠端。",
        },
        "core": "骨腫瘤常考年齡與位置：chondroblastoma = 青少年 epiphysis；simple bone cyst = 兒少 proximal humerus/femur；Ollier 不等於 Maffucci。",
        "key": "Chondroblastoma 好發於青少年長骨骨骺。",
        "summary": "Bone tumors -> chondroblastoma in adolescent epiphysis",
        "front": "Chondroblastoma 好發年齡與位置？",
        "back": "青少年長骨骨骺。",
    },
    57: {
        "analysis": "人工關節置換感染預防重點是選對預防性抗生素、在切皮前適當時間給藥，並避免不必要延長。一般多在切皮前 60 分鐘內給予；vancomycin/fluoroquinolone 因輸注較久可提早。",
        "options": {
            "A": "正確。依手術類型、常見菌與病人過敏/耐藥風險選擇 prophylactic antibiotics，是降低感染的核心措施。",
            "B": "不最適當。多數預防性抗生素應在切皮前 60 分鐘內完成給藥；120 分鐘是特定需長時間輸注藥物的例外，不是一般原則。",
            "C": "錯誤。預防性抗生素通常不需延長到術後 72 小時，過度使用會增加抗藥性與副作用。",
            "D": "錯誤。Vancomycin 或 clindamycin 不是常規人人使用，通常保留給 beta-lactam 過敏或 MRSA 風險等情境。",
        },
        "core": "手術預防性抗生素三件事：選對藥、切皮前適時給、不要過度延長。人工關節常見目標是皮膚菌，依院內規範與病人風險調整。",
        "key": "人工關節置換預防感染應適當選擇並按時給予預防性抗生素。",
        "summary": "Arthroplasty infection prevention -> appropriate prophylactic antibiotics",
        "front": "人工關節置換預防感染最適當原則？",
        "back": "選擇合適預防性抗生素，於切皮前適當時間給予，不常規延長或人人用 vancomycin。",
    },
    58: {
        "analysis": "單純性肘關節脫臼復位後若穩定，治療重點是短期固定後早期活動，避免長期僵硬。固定至少 2 個月會增加 stiffness，並非適當處置。",
        "options": {
            "A": "正確。Simple elbow dislocation 閉鎖復位後多可穩定，慢性再發性脫臼較少。",
            "B": "正確。肘關節後脫臼最常見，前脫臼較少見。",
            "C": "最不適當。若復位後穩定，通常短期固定後早期復健；固定 2 個月會造成肘關節僵硬。",
            "D": "正確。若復位後仍不穩、合併骨折或神經血管問題，可考慮手術治療。",
        },
        "core": "肘關節脫臼復位後要避免長期固定；穩定者短期 immobilization 後 early motion。",
        "key": "穩定的單純肘脫臼不應固定至少 2 個月。",
        "summary": "Simple elbow dislocation -> early motion after short immobilization",
        "front": "穩定單純肘關節脫臼復位後，固定多久？",
        "back": "短期固定後早期活動；長期 2 個月固定不適當。",
    },
    59: {
        "analysis": "20 歲年輕男性四部分近端肱骨骨折，大小結節與外科頸移位超過 1 公分。年輕人應盡量保留自身肱骨頭，最適當為開放復位內固定。",
        "options": {
            "A": "正確。年輕病人移位性 proximal humerus fracture 通常以 ORIF 恢復解剖位置與肩功能。",
            "B": "錯誤。半肩人工關節較常用於高齡、粉碎嚴重且肱骨頭不可重建者，不是 20 歲首選。",
            "C": "錯誤。多部位移位超過 1 公分的嚴重骨折，閉鎖復位經皮鋼針較難穩定與準確重建。",
            "D": "錯誤。全肩人工關節不適合年輕急性近端肱骨骨折作為首選，除非特殊不可重建情境。",
        },
        "core": "年輕病人移位性近端肱骨多部分骨折，以保頭與解剖復位為主；人工關節多留給高齡或不可重建病例。",
        "key": "年輕人移位性近端肱骨多部分骨折首選 ORIF。",
        "summary": "Young displaced proximal humerus fracture -> ORIF",
        "front": "20 歲移位性近端肱骨四部分骨折，首選？",
        "back": "開放復位內固定，盡量保留肱骨頭。",
    },
    60: {
        "analysis": "ACL 主要限制脛骨前移，也參與旋轉穩定。ACL 可分前內側束與後外側束；膝伸直時後外側束較緊，膝屈曲時前內側束較緊。因此說伸直時後外側束鬆弛是錯的。",
        "options": {
            "A": "正確。ACL 的主要功能是防止 anterior tibial translation。",
            "B": "正確。ACL 參與膝關節旋轉穩定與 screw-home mechanism 相關控制。",
            "C": "最不適當。Posterolateral bundle 在膝伸直時較緊，屈曲時相對較鬆；題目敘述相反。",
            "D": "正確。ACL 依脛骨附著位置與張力行為常分為 anteromedial bundle 與 posterolateral bundle。",
        },
        "core": "ACL 兩束張力：AM bundle 屈曲較緊，PL bundle 伸直較緊。ACL 主要防止脛骨前移。",
        "key": "ACL posterolateral bundle 在膝伸直時較緊，不是鬆弛。",
        "summary": "ACL bundles -> PL tight in extension, AM tight in flexion",
        "front": "ACL 後外側束何時較緊？",
        "back": "膝伸直時較緊；前內側束在屈曲時較緊。",
    },
    61: {
        "analysis": "斷指再接的典型適應症包括拇指、多指、小孩斷指與較遠端乾淨切斷。單指多段截肢代表 crush/avulsion 或多節段損傷，技術困難且功能預後差，較不適合。",
        "options": {
            "A": "拇指對手部功能極重要，拇指截肢是再接強適應症。",
            "B": "多指截肢會嚴重影響手功能，通常積極考慮再接。",
            "C": "小孩癒合與神經恢復潛力較好，斷指再接適應症較寬。",
            "D": "最不適當。單指多段截肢血管、神經、肌腱與骨骼損傷複雜，成功率與功能預後較差，通常不是理想適應症。",
        },
        "core": "斷指再接強適應症：thumb、multiple digits、children。單指嚴重 crush/avulsion 或多段截肢預後差，較不建議。",
        "key": "單指多段截肢不是理想的手指再接適應症。",
        "summary": "Replantation indications -> thumb, multiple digits, child; not single multi-level injury",
        "front": "斷指再接強適應症？哪個較不適當？",
        "back": "拇指、多指、小孩適合；單指多段截肢較不適合。",
    },
    62: {
        "analysis": "L5/S1 spondylolisthesis 常使 L5 神經根在椎間孔處受到牽拉或壓迫，造成下肢酸麻。題目為 L5 on S1 第一級滑脫，最可能受壓迫為 L5 nerve root。",
        "options": {
            "A": "L3 神經根位置較高，與 L5/S1 滑脫的典型壓迫不符。",
            "B": "L4 神經根較常與 L4/5 病灶相關，不是 L5/S1 滑脫最典型受壓根。",
            "C": "正確。L5/S1 椎弓解離性滑脫常造成 L5 神經根在椎間孔受壓。",
            "D": "S1 神經根較常與 L5/S1 椎間盤突出壓迫 traversing root 相關；滑脫造成 foraminal stenosis 時常影響 exiting L5 root。",
        },
        "core": "椎弓解離性 L5/S1 spondylolisthesis 常壓迫 exiting L5 root；和椎間盤突出壓迫 traversing root 的概念要分清楚。",
        "key": "L5 on S1 spondylolisthesis 最常壓迫 L5 神經根。",
        "summary": "L5/S1 spondylolisthesis -> L5 nerve root compression",
        "front": "L5 on S1 spondylolisthesis 最可能壓迫哪條神經根？",
        "back": "L5 nerve root。",
    },
    63: {
        "analysis": "Klippel-Feil syndrome 是胚胎早期頸椎分節失敗造成先天性頸椎融合。典型三徵是短頸、低後髮際與頸部活動受限，且可合併泌尿、心肺、神經與聽力異常。",
        "options": {
            "A": "正確。受孕後第 3-8 週左右體節分節失敗，造成頸椎先天融合。",
            "B": "錯誤。Klippel-Feil 可合併腎臟泌尿、生殖、心肺、神經與聽力障礙，並不少見。",
            "C": "錯誤。典型是低後髮際（low posterior hairline），不是高後髮際。",
            "D": "錯誤。典型是短頸與頸部活動受限，不是頸部較長。",
        },
        "core": "Klippel-Feil syndrome = congenital cervical fusion due to segmentation failure；短頸、低後髮際、頸活動受限是經典三徵。",
        "key": "Klippel-Feil syndrome 由胚胎早期頸椎分節失敗造成。",
        "summary": "Klippel-Feil -> cervical segmentation failure, short neck, low hairline",
        "front": "Klippel-Feil syndrome 的成因與三徵？",
        "back": "頸椎分節失敗；短頸、低後髮際、頸活動受限。",
    },
    64: {
        "analysis": "完全性鹿角結石體積大、佔據腎盂腎盞，單靠 ESWL 或 ureteroscopy 清石率不足。最佳治療通常是經皮腎臟碎石取石術（PCNL），必要時分期或合併其他方式。",
        "options": {
            "A": "ESWL 對小結石較適合；完整鹿角結石體積大且常為感染石，單用震波清石率差。",
            "B": "輸尿管鏡可處理部分上泌尿道結石，但對 complete staghorn stone 通常效率與清石率不足。",
            "C": "正確。PCNL 可直接建立腎臟通道碎石取石，是完全性鹿角結石的主要治療選擇。",
            "D": "尿液鹼化主要用於尿酸結石等特定結石，不能處理完整鹿角結石的機械負荷與感染風險。",
        },
        "core": "Staghorn stone 尤其 complete type，治療目標是最大化 stone-free rate 並控制感染，首選 PCNL。",
        "key": "完全性鹿角結石最佳選擇是 PCNL。",
        "summary": "Complete staghorn stone -> percutaneous nephrolithotomy",
        "front": "Complete renal staghorn stone 首選治療？",
        "back": "經皮腎臟碎石取石術（PCNL）。",
    },
    65: {
        "analysis": "Ta、低惡性度、0.5 公分包皮陰莖鱗癌屬表淺早期病灶，治療應盡量器官保留，如局部切除、雷射、包皮環切或 Mohs。根除性陰莖手術過度治療。",
        "options": {
            "A": "可考慮。小型低度表淺病灶可用雷射等器官保留方式，需適當追蹤。",
            "B": "最不建議。陰莖根除手術對 0.5 公分 Ta 低惡性度病灶過度治療，功能與心理傷害大。",
            "C": "可考慮。病灶在包皮且早期時，包皮環切可同時治療與取得病理。",
            "D": "可考慮。Mohs micrographic surgery 可用於選擇性早期病灶以保留組織。",
        },
        "core": "早期低度陰莖癌以 organ-sparing therapy 為主；根除性手術留給較進展或無法局部控制的病灶。",
        "key": "小型 Ta 低度包皮鱗癌最不建議陰莖根除手術。",
        "summary": "Early penile SCC -> organ-sparing, not radical penectomy",
        "front": "0.5 cm Ta 低度陰莖/包皮 SCC，最不建議？",
        "back": "陰莖根除手術；早期病灶以器官保留為主。",
    },
    66: {
        "analysis": "IMDC metastatic RCC risk factors 包括 Karnofsky performance status 低、診斷到治療時間短、hemoglobin 低、corrected calcium 高、neutrophil 高、platelet 高。LDH 是 MSKCC/Heng 以外其他模型常見項目，但不是 IMDC 項目。",
        "options": {
            "A": "Performance status 是 IMDC 風險因子之一，反映病人體能與預後。",
            "B": "正確答案。LDH 不是 IMDC 六項風險因子；它較常見於其他腫瘤或舊模型的風險評估。",
            "C": "Hemoglobin 低於正常下限是 IMDC 風險因子之一。",
            "D": "Corrected serum calcium 高於正常上限是 IMDC 風險因子之一。",
        },
        "core": "IMDC 六因子：低 KPS、診斷至治療 <1 年、低 Hb、高 corrected Ca、高 neutrophil、高 platelet；沒有 LDH。",
        "key": "LDH 不是 IMDC metastatic RCC risk factor。",
        "summary": "IMDC RCC risk -> no LDH",
        "front": "IMDC metastatic RCC risk factors 不包括？",
        "back": "LDH；IMDC 包括 KPS、時間、Hb、Ca、neutrophil、platelet。",
    },
    67: {
        "analysis": "轉移性攝護腺癌的核心是 androgen deprivation therapy，手術去勢與 LHRH agonist/antagonist 都可達到去勢效果。早期且預期壽命超過 10 年者，優先考慮根治性治療或積極監測，不是先給賀爾蒙治療。",
        "options": {
            "A": "正確。睪丸切除與 LHRH agonist 都可達到去勢治療效果，用於轉移性攝護腺癌。",
            "B": "錯誤。早期攝護腺癌且預期壽命 >10 年，應依風險分層考慮根除性攝護腺切除、放療或主動監測；單獨賀爾蒙治療不是首選根治策略。",
            "C": "正確。TURP 是處理膀胱出口阻塞症狀的手術，不是攝護腺癌根除手術。",
            "D": "正確。LHRH agonist 與 antagonist 都可用於 ADT，差異在起效、testosterone flare 與個別風險。",
        },
        "core": "早期可治癒攝護腺癌看風險分層與預期壽命，治療目標是根治或監測；ADT 主要用於轉移性或特定合併治療情境。",
        "key": "早期且預期壽命 >10 年攝護腺癌，不應首先考慮單獨賀爾蒙治療。",
        "summary": "Early prostate cancer -> curative options/active surveillance, not first-line hormone alone",
        "front": "早期攝護腺癌、預期壽命 >10 年，首選賀爾蒙治療嗎？",
        "back": "不是；依風險考慮根治手術、放療或主動監測。",
    },
    68: {
        "analysis": "BPH 是老年男性常見良性腫瘤，與年齡、雄激素/雌激素平衡、發炎與遺傳因素都有關。說其成因與遺傳無關過於絕對。",
        "options": {
            "A": "正確。BPH 是男性最常見良性腫瘤之一，盛行率隨年齡增加。",
            "B": "正確。前列腺阻塞與下泌尿道症狀常隨年齡增加而更常見。",
            "C": "最不恰當。BPH 有家族與遺傳傾向，尤其較早發或較嚴重病例；不能說與遺傳無關。",
            "D": "正確。老化後 androgen/estrogen 比例改變，雌激素相對影響可能參與 BPH 發生。",
        },
        "core": "BPH 是年齡相關疾病，但不是單純老化；荷爾蒙、基質上皮互動、發炎與遺傳都可能參與。",
        "key": "BPH 成因不能說與遺傳無關。",
        "summary": "BPH -> age-related but genetic factors may contribute",
        "front": "BPH 成因與遺傳完全無關嗎？",
        "back": "不是；家族與遺傳因素可能參與，尤其早發或嚴重病例。",
    },
    69: {
        "analysis": "題目官方答案選 A，但 Peyronie's disease 常被認為與陰莖白膜反覆微創傷後癒合異常、纖維斑塊形成有關；A 本身看起來是正確敘述。B、C、D 也多為合理敘述，因此本題建議人工複核官方答案。",
        "options": {
            "A": "官方答案標示為錯誤，但常規醫學知識認為 Peyronie's disease 確實可能與 tunica albuginea 微創傷後異常癒合與纖維化有關；此處需人工確認。",
            "B": "正確。Peyronie's disease 可造成勃起疼痛、陰莖彎曲與畸形，並影響性交功能。",
            "C": "正確。Peyronie's disease 與糖尿病、高血壓、Dupuytren contracture 等纖維化或血管代謝相關狀態有關聯。",
            "D": "正確。Collagenase clostridium histolyticum 注射是特定穩定期、可觸及斑塊且彎曲達標病例的非手術治療選項之一。",
        },
        "core": "Peyronie's disease 是 tunica albuginea 纖維斑塊造成陰莖彎曲與疼痛；創傷後異常癒合是常見病因假說。此題官方答案與常規知識可能衝突，勿自行改答案，應人工複核。",
        "key": "Peyronie's disease 常與白膜微創傷後異常癒合及纖維斑塊有關；本題官方答案需複核。",
        "summary": "Peyronie disease -> fibrosis of tunica albuginea; official answer likely needs review",
        "front": "Peyronie's disease 常見病因假說？",
        "back": "陰莖白膜微創傷後異常癒合形成纖維斑塊；本題官方答案 A 建議複核。",
        "notes": ["Q69 官方答案為 A，但 A 敘述符合常見 Peyronie's disease 病因假說，建議人工複核官方答案或題目文字。"],
    },
    70: {
        "analysis": "原發性膀胱輸尿管逆流是先天性 UVJ 抗逆流機制不全，常因輸尿管膀胱內段太短或接合處發育異常。續發性則來自膀胱高壓、出口阻塞或神經性膀胱。",
        "options": {
            "A": "膀胱內壓過高會克服抗逆流機制，屬續發性 VUR 原因。",
            "B": "膀胱出口阻塞使膀胱壓上升，屬續發性 VUR 原因。",
            "C": "正確。UVJ 先天結構/功能異常造成抗逆流機制不足，是原發性 VUR 的核心原因。",
            "D": "神經性膀胱造成排尿功能障礙與高壓，屬續發性 VUR。",
        },
        "core": "Primary VUR = UVJ congenital incompetence；secondary VUR = high-pressure bladder/outlet obstruction/neurogenic bladder。",
        "key": "原發性 VUR 來自 UVJ 抗逆流機制病變。",
        "summary": "Primary VUR -> UVJ abnormality",
        "front": "原發性膀胱輸尿管逆流原因？",
        "back": "膀胱輸尿管接合處（UVJ）抗逆流機制異常。",
    },
    71: {
        "analysis": "有排尿障礙合併 VUR 的孩童，若下泌尿道功能不佳，先處理膀胱排尿問題可降低膀胱壓與逆流。直接重建輸尿管或注射治療若未處理膀胱功能，效果較差。",
        "options": {
            "A": "錯誤。直接輸尿管重建未先改善膀胱排尿功能，可能仍因高壓膀胱導致失敗或復發。",
            "B": "錯誤。輸尿管開口注射適用部分 VUR，但有排尿障礙時需先處理下泌尿道功能。",
            "C": "正確。先導尿或清潔間歇導尿，改善膀胱排空與壓力，是此情境的第一步。",
            "D": "錯誤。膀胱擴大是較後線、嚴重低順應性膀胱的處置，不是第一步。",
        },
        "core": "VUR 合併 voiding dysfunction 時，先處理膀胱功能與排空，再談抗逆流手術。",
        "key": "排尿障礙合併 VUR 的孩童，先導尿改善下泌尿道功能。",
        "summary": "VUR + voiding dysfunction -> treat bladder emptying first",
        "front": "孩童 VUR 合併排尿障礙，第一步？",
        "back": "先導尿/改善下泌尿道排尿功能。",
    },
    72: {
        "analysis": "肝臟鈍傷常見表現包括肝撕裂、被膜下血腫與肝實質內出血。門靜脈栓塞不是典型鈍性肝外傷常見傷害，較少見。",
        "options": {
            "A": "肝臟撕裂傷是鈍性肝外傷常見型態之一。",
            "B": "被膜下血腫也是常見鈍性肝傷表現。",
            "C": "肝實質內出血可見於鈍性肝外傷。",
            "D": "最少見。門靜脈栓塞不是肝臟鈍性創傷的常見直接傷害型態。",
        },
        "core": "Blunt liver trauma 常見 laceration、subcapsular hematoma、intraparenchymal hemorrhage；portal vein thrombosis 相對少見。",
        "key": "肝鈍傷最少見的是門靜脈栓塞。",
        "summary": "Blunt liver trauma -> portal vein thrombosis is uncommon",
        "front": "肝臟鈍性創傷較少見傷害？",
        "back": "門靜脈栓塞。",
    },
    73: {
        "analysis": "Budd-Chiari syndrome 是肝靜脈流出道阻塞，可發生在小肝靜脈、主要肝靜脈到下腔靜脈入口附近。它不是膽管、門靜脈或肝動脈阻塞。",
        "options": {
            "A": "膽管阻塞造成阻塞性黃疸或膽管炎，不稱 Budd-Chiari syndrome。",
            "B": "門靜脈阻塞會造成門脈高壓等問題，但不是 Budd-Chiari 的定義。",
            "C": "肝動脈阻塞屬肝臟動脈供血問題，不是 Budd-Chiari。",
            "D": "正確。Budd-Chiari syndrome 指 hepatic venous outflow obstruction，核心是肝靜脈流出受阻。",
        },
        "core": "Budd-Chiari = hepatic vein outflow obstruction；portal vein thrombosis 是另一個概念。",
        "key": "Budd-Chiari syndrome 是肝靜脈阻塞。",
        "summary": "Budd-Chiari -> hepatic vein outflow obstruction",
        "front": "Budd-Chiari syndrome 阻塞哪個構造？",
        "back": "肝靜脈/肝靜脈流出道。",
    },
    74: {
        "analysis": "14 歲青少年肩部疼痛半年，X 光若呈侵襲性骨病灶、骨膜反應或 metaphysis around shoulder，最符合 osteogenic sarcoma。骨肉瘤好發青少年長骨幹骺端。",
        "options": {
            "A": "骨轉移在 14 歲並非常見第一診斷；兒童青少年原發性骨惡性腫瘤較需考慮。",
            "B": "骨淋巴瘤可侵犯骨，但典型年齡與影像若為侵襲性成骨病灶，不如 osteosarcoma 典型。",
            "C": "正確。Osteogenic sarcoma 好發青少年長骨 metaphysis，可有疼痛、腫脹與侵襲性 X 光表現。",
            "D": "Chondrosarcoma 多見於成人，青少年較少，且肩部 X 光若為骨肉瘤型表現時不優先。",
        },
        "core": "青少年長骨幹骺端疼痛 + 侵襲性骨病灶，優先想到 osteosarcoma；chondrosarcoma 多偏成人。",
        "key": "青少年肩部侵襲性骨病灶最可能 osteogenic sarcoma。",
        "summary": "Adolescent aggressive bone lesion -> osteosarcoma",
        "front": "14 歲肩部侵襲性骨腫瘤最可能？",
        "back": "Osteogenic sarcoma，常見於青少年長骨幹骺端。",
    },
    75: {
        "analysis": "術後尿滯留常見風險包括年齡、男性、BPH、輸液過多、脊椎/硬膜外麻醉、鴉片類止痛與肛門直腸手術。官方答案選 A，但男性通常本身是風險因子，因此此題建議人工複核題意是否問「最不特異」或另有前提。",
        "options": {
            "A": "官方答案。男性確實較容易因前列腺與下泌尿道因素發生尿滯留；若題目要選最不適當，此項與一般知識有衝突，需人工確認。",
            "B": "正確。術中術後輸液過多使膀胱快速膨脹，會增加尿滯留風險。",
            "C": "正確。脊椎或硬膜外麻醉會抑制膀胱感覺與逼尿肌反射，較易造成尿滯留。",
            "D": "正確。肛門直腸手術疼痛、反射性括約肌痙攣與麻醉止痛因素，使尿滯留風險較高。",
        },
        "core": "術後尿滯留風險常見於男性、高齡、BPH、脊椎/硬膜外麻醉、過多輸液、鴉片類止痛與肛門直腸手術。此題官方答案與一般風險因子可能不一致，需人工複核。",
        "key": "術後尿滯留常見風險包括男性、脊椎/硬膜外麻醉、過多輸液與肛門直腸手術；本題官方答案需複核。",
        "summary": "Postoperative urinary retention -> male sex is usually a risk factor; official answer needs review",
        "front": "術後急性尿滯留常見風險因子？",
        "back": "男性、高齡/BPH、脊椎或硬膜外麻醉、過多輸液、肛門直腸手術等；本題 A 建議複核。",
        "notes": ["Q75 官方答案為 A，但男性通常是術後尿滯留風險因子，建議人工複核題意與官方答案。"],
    },
    76: {
        "analysis": "骨盆骨折合併低血壓、FAST 無腹腔積液，代表出血來源很可能在骨盆後腹腔。初步處置已做後，下一步應快速控制骨盆出血；若題目選項中沒有骨盆固定作為最先初步處置，緊急血管攝影栓塞是最適合的 definitive hemorrhage control。",
        "options": {
            "A": "正確。持續休克、骨盆骨折且 FAST 陰性時，骨盆動脈出血需考慮 angiography with embolization。",
            "B": "錯誤。FAST 無腹腔積液時，剖腹探查不是最優先；除非有腹內出血證據或腹膜炎。",
            "C": "骨盆加壓帶是早期重要處置，但題幹說經初步處置後發現骨盆骨折且仍休克，最需要進一步止血控制；在本題選項中 A 較適合。",
            "D": "錯誤。Tranexamic acid 若使用應盡早在外傷後 3 小時內給予，不是 3 小時後才給。",
        },
        "core": "骨盆骨折休克 + FAST negative，要想到後腹腔/骨盆出血；初步固定與復甦後，血管攝影栓塞是重要止血方式。",
        "key": "骨盆骨折休克且 FAST 陰性，下一步考慮緊急血管攝影栓塞。",
        "summary": "Pelvic fracture shock + FAST negative -> angiography/embolization",
        "front": "骨盆骨折休克、FAST 陰性，止血下一步？",
        "back": "緊急血管攝影與栓塞，並持續復甦與骨盆穩定。",
    },
    77: {
        "analysis": "穿刺性肢體外傷需辨認 hard signs of vascular injury，包括搏動性出血、擴大血腫、缺血、thrill 或 bruit。聽到雜音代表可能動靜脈瘻或血管傷，應立即請血管外科評估。",
        "options": {
            "A": "錯誤。下肢穿刺傷因血管較大且位置常受傷，血管傷不少見；不能說上肢較下肢更易作為通則。",
            "B": "不夠精準。神經受傷提示附近重要構造可能受傷，但是否立即照會血管外科要看血管傷徵象與檢查，不如 bruit 直接。",
            "C": "正確。傷處聽到 bruit 是血管傷 hard sign/重要徵象，需立即血管外科評估。",
            "D": "錯誤。噴血時先直接加壓止血；盲目用器械夾血管可能傷害神經血管束，不是最佳現場止血方式。",
        },
        "core": "肢體穿刺傷看到 hard signs，尤其 pulsatile bleeding、expanding hematoma、bruit/thrill、ischemia，要立即血管外科處理。",
        "key": "穿刺性肢體傷口有 bruit，代表可能血管傷，需立即血管外科評估。",
        "summary": "Penetrating extremity trauma -> bruit suggests vascular injury",
        "front": "穿刺性肢體傷何種發現最提示血管傷？",
        "back": "傷處有 bruit/thrill、搏動性出血、缺血或擴大血腫。",
    },
    78: {
        "analysis": "病人 GCS E1M1V1、雙側瞳孔放大無光反射、血氧 88%，有立即 airway failure 風險。DNR 是不施行心肺復甦，並不必然等於拒絕插管或急救性呼吸道處置；若無明確 DNI，應先處理可立即危及生命的低氧與呼吸道。",
        "options": {
            "A": "不適當。嚴重昏迷與低血氧需立即處置，等待家屬同意會延誤救命 airway management。",
            "B": "正確。GCS 3 且血氧低，應立即氣管內插管保護呼吸道與改善氧合。",
            "C": "錯誤。血氧 88% 且深昏迷，繼續觀察會延誤處置。",
            "D": "錯誤。DNR 不等於 DNI；除非明確拒絕插管或符合特定安寧緩和決策，不能單憑 DNR 註記放棄必要 airway management。",
        },
        "core": "DNR 是不做 CPR，不自動等於不插管。急診深昏迷、不能保護呼吸道或低氧時，若無明確 DNI，仍應處理 airway。",
        "key": "DNR 不等於 DNI；GCS 3 且低氧應立即插管。",
        "summary": "DNR vs airway -> DNR does not automatically prohibit intubation",
        "front": "DNR 註記是否等於不能插管？",
        "back": "不等於；若無明確 DNI，深昏迷低氧仍需立即 airway management。",
    },
    79: {
        "analysis": "醫師守密義務有例外，例如法律規定、病人同意、或為避免他人重大且迫近危害。即使可揭露，也應採最小必要揭露，告知適當對象；不能為了減少傷害就儘量告知病人身旁親友。",
        "options": {
            "A": "正確。病人資訊原則上需保密，除非病人/代理人同意或法律另有規定。",
            "B": "正確。若保密會導致他人嚴重傷害，醫師可在必要範圍內揭露，以保護可能受害者。",
            "C": "正確。當病人表達嚴重傷害他人的意圖時，醫師應說明保密有界線，必要時將採保護措施。",
            "D": "最不恰當。揭露應限於必要對象與必要內容，例如可能受害者或主管機關；不是儘量告知病人身旁親友。",
        },
        "core": "保密例外採必要性與最小揭露原則。可為避免重大危害揭露，但不能無差別告知親友。",
        "key": "醫療保密例外仍須最小必要揭露，不是儘量告知親友。",
        "summary": "Confidentiality exception -> disclose minimum necessary to appropriate parties",
        "front": "病人可能傷害他人時，醫師可怎麼揭露？",
        "back": "可在必要範圍內向適當對象揭露；不可無差別告知親友。",
    },
    80: {
        "analysis": "15 歲病人確診淋球菌尿道炎，屬須通報與需完整治療、伴侶處理及 HIV/其他 STI 評估的情境。未成年人仍有隱私與醫療自主需尊重，但法定傳染病通報義務不能因病人請求而免除。",
        "options": {
            "A": "錯誤。淋病需依法通報並接受適當抗生素治療，不能不通報或讓病人自行買藥。",
            "B": "錯誤。淋病本身即需通報，不是等 HIV 陽性才通報；自行購藥也不符合公共衛生與治療原則。",
            "C": "不最佳。未成年人不代表所有性病資訊都必須直接告知監護人；需在法律、保護需求與病人隱私間審慎處理。",
            "D": "正確。醫師應告知病人法定通報義務，說明完整治療、追蹤、伴侶處理與 HIV 檢驗的重要性，同時盡量維護其隱私。",
        },
        "core": "法定傳染病有通報義務；青少年性健康照護要兼顧隱私、保護與公共衛生，不可不通報或只叫病人自行買藥。",
        "key": "淋病為須通報傳染病，應告知通報義務並強調完整治療。",
        "summary": "Gonorrhea in minor -> mandatory reporting + confidential counseling/treatment",
        "front": "未成年淋病病人要求不要告知家長，醫師重點？",
        "back": "告知法定通報義務，維護隱私並說明完整治療、追蹤與檢驗重要性。",
    },
}


def converted_existing_updates():
    updates = {}
    for path in sorted(Path("scratch").glob("updates_113-1_medicine-5_*.json")):
        for item in load_json(path):
            qid = item["id"]
            qnum = int(qid.rsplit("_", 1)[1])
            explanation = item["explanation"]
            if qnum == 7:
                explanation = explanation.replace(
                    "- A, B, D. 錯誤。這些電解質在小腸中後段仍可被有效吸收，通常不需常規特別補充。",
                    "- A. 錯誤。鉀離子可在小腸與結腸等多處吸收，Billroth II 繞過十二指腸並不會讓鉀成為最需要常規特別補充的項目。\n"
                    "- B. 錯誤。鈉離子在整段小腸與結腸均可有效吸收，通常不是 Billroth II 術後最典型的缺乏營養素。\n"
                    "- D. 錯誤。鎂離子雖可能受整體營養狀態影響，但 Billroth II 繞過十二指腸最典型影響的是鈣與鐵吸收，不是鎂作為本題最佳答案。",
                )
            elif qnum == 11:
                explanation = explanation.replace(
                    "- A, B, D. 錯誤。此案例上肢無力程度遠重於下肢，且保留了大部分下肢功能（肌力3~4分），符合Central Cord Syndrome，而非Anterior Cord Syndrome（前脊髓症候群通常以運動完全喪失及痛溫覺喪失為主，但保留本體感覺，且無上下肢顯著不對稱的特徵）。",
                    "- A. 錯誤。雖然 central cord syndrome 判斷正確，但 ASIA B 代表僅保留感覺、沒有有效運動功能；本題下肢仍有 3~4 分肌力，不符合 B 級。\n"
                    "- B. 錯誤。ASIA C 可有運動保留，但本題典型是上肢比下肢更弱的 central cord syndrome，不是 anterior cord syndrome。\n"
                    "- D. 錯誤。ASIA E 代表感覺與運動功能正常；本題有明顯上肢無力與感覺異常，不符合 E 級，也不是 anterior cord syndrome。",
                )
            elif qnum == 15:
                explanation = explanation.replace(
                    "- A, C, D. 錯誤。Gilula's arcs 定義上僅有3條。",
                    "- A. 錯誤。Gilula's arcs 不是 2 條；少算會漏掉遠排腕骨近端弧線。\n"
                    "- C. 錯誤。Gilula's arcs 定義上不是 4 條，不能把其他腕骨邊界任意加進標準三弧線。\n"
                    "- D. 錯誤。Gilula's arcs 不是 5 條；臨床標準判讀使用三條連續弧線。",
                )
            updates[qnum] = {
                "question_id": qid,
                "question_number": qnum,
                "explanation": explanation,
                "key_point": item.get("key_point", ""),
                "flashcard_front": item.get("flashcard_front", ""),
                "flashcard_back": item.get("flashcard_back", ""),
                "flashcard_summary": item.get("flashcard_summary", ""),
                "review_status": "ai_generated",
                "explanation_model": "codex-high-quality-rewrite",
                "explanation_generated_at": STAMP,
                "manual_review_notes": [],
            }
    return updates


def new_update(q):
    qnum = q["question_number"]
    data = DATA[qnum]
    return {
        "question_id": q["id"],
        "question_number": qnum,
        "explanation": make_explanation(data["analysis"], data["options"], data["core"]),
        "key_point": data["key"],
        "flashcard_front": data["front"],
        "flashcard_back": data["back"],
        "flashcard_summary": data["summary"],
        "review_status": "ai_generated",
        "explanation_model": "codex-high-quality-rewrite",
        "explanation_generated_at": STAMP,
        "manual_review_notes": data.get("notes", []),
    }


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    exam = load_json(SOURCE_FILE)
    questions = {q["question_number"]: q for q in exam["questions"]}
    updates = converted_existing_updates()
    for qnum in range(31, 81):
        updates[qnum] = new_update(questions[qnum])

    missing = [qnum for qnum in range(1, 81) if qnum not in updates]
    if missing:
        raise SystemExit(f"missing updates: {missing}")

    for start in range(1, 81, 10):
        end = start + 9
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": [updates[qnum] for qnum in range(start, end + 1)],
        }
        write_json(OUT_DIR / f"q{start:03d}-q{end:03d}.json", payload)


if __name__ == "__main__":
    main()
