import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/112-2/medicine-1.json"
DATASET_ID = "112-2_medicine-1"
OUT_DIR = Path("scratch/rewrite_updates/112-2_medicine-1")
STAMP = "2026-07-13T00:00:00+08:00"
NEGATIVE_CUES = (
    "錯誤",
    "不是",
    "不會",
    "不供應",
    "尚未出現",
    "最不適當",
    "最不可能",
    "最無關",
    "沒有",
    "不需要",
    "並非",
    "不受",
    "關聯性最小",
)


DATA = {
    1: {
        "topic": "瞳孔對光反射 / posterior commissure / Edinger-Westphal 核",
        "analysis": "題幹描述右眼受光後雙側瞳孔縮小，重點是對側 consensual light reflex 的中樞連結。視網膜訊息到達頂蓋前區後，會經後聯合把訊息送到對側 Edinger-Westphal 核，再經動眼神經副交感路徑造成縮瞳。",
        "options": {
            "A": "前聯合主要連結兩側大腦半球前部，與瞳孔對光反射的頂蓋前區到 E-W 核路徑無關。",
            "B": "後聯合是頂蓋前區訊息跨至對側 Edinger-Westphal 核的重要通路，因此可產生直接與間接對光反射。",
            "C": "視神經交叉處理部分視網膜纖維交叉，位置在傳入視覺路徑，不是頂蓋前區到對側 E-W 核的連結。",
            "D": "上小腦腳交叉屬小腦輸出與運動協調路徑，和瞳孔副交感反射路徑不同。",
        },
        "core": "瞳孔對光反射的雙側性來自 pretectal area 經 posterior commissure 連到兩側 E-W 核；看到 consensual light reflex 要想到後聯合。",
        "key": "頂蓋前區到對側 Edinger-Westphal 核的連結主要經後聯合。",
    },
    2: {
        "topic": "Clarke 背核 / 下肢無意識本體覺 / dorsal spinocerebellar tract",
        "analysis": "題目問由 Clarke 背核發出、傳遞下肢本體感覺的路徑。Clarke nucleus 接收下肢與軀幹無意識本體覺，主要投射形成背側脊髓小腦徑進入小腦。",
        "options": {
            "A": "背側脊髓小腦徑來自 Clarke 背核，傳遞同側下肢與軀幹的無意識本體覺，是本題正確配對。",
            "B": "腹側脊髓小腦徑主要傳遞脊髓中間神經元與下肢運動活動相關訊息，並非 Clarke 背核的典型輸出。",
            "C": "楔狀核小腦徑傳遞上肢與上軀幹本體覺，對應 accessory cuneate nucleus，不是下肢 Clarke 背核。",
            "D": "吻端脊髓小腦徑主要與上肢無意識本體覺相關，不是本題下肢 Clarke 背核路徑。",
        },
        "core": "Clarke nucleus 對應下肢無意識本體覺，走 dorsal spinocerebellar tract；上肢類似資訊則想到 cuneocerebellar tract。",
        "key": "Clarke 背核主要發出背側脊髓小腦徑，傳遞下肢無意識本體覺。",
    },
    3: {
        "topic": "基底核直接路徑 / 間接路徑 / subthalamic nucleus",
        "analysis": "題目問何者不是 direct basal ganglia pathway 的主要構造。直接路徑為 cortex 到 striatum，再抑制 GPi/SNr，最後影響 thalamus；subthalamic nucleus 是間接路徑的重要站點。",
        "options": {
            "A": "殼核屬於 striatum，是直接路徑接收皮質輸入的重要結構。",
            "B": "內蒼白球是直接路徑的輸出核，受 striatum 抑制後改變對丘腦的抑制。",
            "C": "丘腦下核主要位於間接路徑中，經興奮 GPi/SNr 增加對丘腦抑制，因此不是直接路徑主要構造。",
            "D": "丘腦是基底核輸出影響皮質運動活動前的重要中繼站，屬直接路徑功能鏈的一部分。",
        },
        "core": "直接路徑重點是 striatum 抑制 GPi/SNr 以釋放丘腦；subthalamic nucleus 是間接路徑的高頻考點。",
        "key": "丘腦下核屬於基底核間接路徑，不是直接路徑的主要站點。",
    },
    4: {
        "topic": "海馬 / 乳頭體 / fornix / Papez circuit",
        "analysis": "題目問海馬到乳頭體的連結。Papez circuit 中，海馬的主要輸出經穹窿到乳頭體，之後再到前丘腦核與扣帶迴，和記憶迴路有關。",
        "options": {
            "A": "終紋主要連結杏仁核到下視丘與隔區，不是海馬到乳頭體的纖維束。",
            "B": "穹窿是海馬輸出到乳頭體的主要白質束，正是本題所問連結。",
            "C": "內側前腦束與獎賞、自律與下視丘相關通路較有關，不是 Papez circuit 的海馬至乳頭體段。",
            "D": "內側縱束整合眼球運動與前庭訊息，和海馬乳頭體連結無關。",
        },
        "core": "海馬到乳頭體走 fornix；杏仁核相關常見纖維則是 stria terminalis。",
        "key": "海馬至乳頭體的主要連結纖維是穹窿。",
    },
    5: {
        "topic": "交感節前神經元 / lateral horn / Clarke nucleus",
        "analysis": "題目問交感節前神經元何者錯誤。交感節前神經元位在 T1-L2 脊髓側角，解剖上屬 lamina VII，可受下視丘下行路徑調控；Clarke 背核則處理本體覺。",
        "options": {
            "A": "交感節前神經元位於胸腰髓側角，側角屬灰質 lamina VII，所以此敘述正確。",
            "B": "下視丘可透過 hypothalamospinal tract 調控自律神經節前神經元，所以此敘述正確。",
            "C": "Clarke 背核是本體覺中繼核，不是交感節前神經元所在處；題目問錯誤，故選此項。",
            "D": "胸髓包含交感節前神經元，特別是 T1-L2 節段的側角，因此此敘述正確。",
        },
        "core": "交感節前神經元在 T1-L2 lateral horn；Clarke nucleus 是下肢本體覺，不要把兩者混在一起。",
        "key": "交感節前神經元位於胸腰髓側角 lamina VII，不位於 Clarke 背核。",
    },
    6: {
        "topic": "眼動脈 / optic canal / 眼眶血管",
        "analysis": "題目考眼眶血管走行。眼動脈是內頸動脈分支，和視神經一起經視神經管進入眼眶，供應眼球與眼眶內容物。",
        "options": {
            "A": "眼動脈經視神經管入眼眶，通常伴隨視神經走行，是正確敘述。",
            "B": "眼動脈來自內頸動脈，不是中腦膜動脈分支；中腦膜動脈多屬上頷動脈系統。",
            "C": "眼靜脈主要經眶上裂與海綿竇交通，選項說眼下靜脈通過共同腱環進入眼眶不正確。",
            "D": "淚動脈走向眼眶外上方供應淚腺，位於視神經外側而非內側。",
        },
        "core": "眼動脈是 ICA 分支，經 optic canal 入眼眶；眶上裂則是多數眼外肌神經與眼靜脈的重要通道。",
        "key": "眼動脈是內頸動脈分支，與視神經一起經視神經管入眼眶。",
    },
    7: {
        "topic": "頸外靜脈 / SCM 表淺 / subclavian vein",
        "analysis": "題目考頸外靜脈的位置與回流。頸外靜脈屬淺層靜脈，跨過胸鎖乳突肌表面，收集頭皮與部分顏面淺層靜脈血後注入鎖骨下靜脈。",
        "options": {
            "A": "頸外靜脈是淺層靜脈，不屬於頸動脈鞘內的深層靜脈系統。",
            "B": "它通常位於胸鎖乳突肌表面，不是在該肌深層。",
            "C": "迷走神經走在頸動脈鞘內，伴行的是內頸靜脈與頸動脈，不是頸外靜脈。",
            "D": "頸外靜脈收集部分顏面與頭頸淺層血液，最後匯入鎖骨下靜脈，故此敘述正確。",
        },
        "core": "頸外靜脈是 SCM 表淺的靜脈，回流到 subclavian vein；頸動脈鞘內才是內頸靜脈和迷走神經。",
        "key": "頸外靜脈位於胸鎖乳突肌表淺，收集淺層頭頸血後注入鎖骨下靜脈。",
    },
    8: {
        "topic": "頸靜脈孔 / CN IX X XI / 聲音嘶啞與舌後感覺",
        "analysis": "聲音嘶啞提示迷走神經或喉返神經功能受損，舌後三分之一與口咽感覺喪失提示舌咽神經受損。CN IX、X、XI 共同通過頸靜脈孔，因此顱底腫瘤最可能在此。",
        "options": {
            "A": "盲孔位在前顱窩附近，與 CN IX、X 通過及聲音嘶啞無直接關係。",
            "B": "圓孔通過上頷神經 V2，主要影響臉部中段感覺，不會同時造成舌後感覺喪失與聲音嘶啞。",
            "C": "頸靜脈孔通過舌咽、迷走與副神經，能解釋口咽與舌後三分之一感覺喪失及聲音嘶啞。",
            "D": "枕骨大孔通過延髓、脊髓與椎動脈等，典型不會選擇性造成 CN IX、X 的顱底孔症候群。",
        },
        "core": "聲音嘶啞加舌後三分之一感覺問題要想到 CN X 和 CN IX；共同出口是 jugular foramen。",
        "key": "CN IX、X、XI 通過頸靜脈孔，病灶可造成舌後感覺喪失與聲音嘶啞。",
    },
    9: {
        "topic": "甲狀舌骨膜 / internal laryngeal nerve",
        "analysis": "題目問穿過甲狀舌骨膜進入喉部的神經。上喉神經內支和 superior laryngeal artery 一起穿過甲狀舌骨膜，提供聲帶以上喉黏膜感覺。",
        "options": {
            "A": "舌咽神經主要供應咽部、舌後三分之一與莖突咽肌，不穿過甲狀舌骨膜入喉。",
            "B": "內喉神經是上喉神經內支，穿過甲狀舌骨膜，供應聲帶以上感覺，正是本題答案。",
            "C": "外喉神經走向環甲肌，主要是運動支，不是穿膜進入喉腔的感覺支。",
            "D": "喉返神經由下方進入喉部，供應多數喉內肌與聲帶以下感覺，不經甲狀舌骨膜。",
        },
        "core": "穿 thyroid membrane 是 internal laryngeal nerve；支配 cricothyroid 則想到 external laryngeal nerve。",
        "key": "內喉神經穿過甲狀舌骨膜，供應聲帶以上喉黏膜感覺。",
    },
    10: {
        "topic": "共同腱環 / orbital apex / CN IV",
        "analysis": "共同腱環包圍視神經管與眶上裂中央部分，內有 CN III、VI、鼻睫神經等結構；滑車神經進入眼眶後走在腱環外上方，不在共同腱環內。",
        "options": {
            "A": "動眼神經上下支通過共同腱環內進入眼眶，支配多數眼外肌。",
            "B": "滑車神經經眶上裂入眼眶，但走在共同腱環外，支配上斜肌；題目問不會出現在環內，故選此項。",
            "C": "第五對中與眼眶相關的鼻睫神經分支通過腱環內；雖非整個 CN V 都在環內，但此選項不如 CN IV 明確排除。",
            "D": "外展神經通過共同腱環內，支配外直肌。",
        },
        "core": "共同腱環內記 CN III、VI、鼻睫神經與視神經相關構造；CN IV 在腱環外是常考例外。",
        "key": "滑車神經經眶上裂入眼眶，但不在共同腱環內。",
    },
    11: {
        "topic": "鼓室 / auditory tube / 前壁",
        "analysis": "耳咽管連接鼻咽與鼓室，用來平衡中耳壓力。它在鼓室的開口位於前壁，並與鼓膜張肌半管相鄰。",
        "options": {
            "A": "耳咽管開口於鼓室前壁，是中耳與鼻咽相通的壓力平衡通道。",
            "B": "後壁主要與乳突竇、錐隆起等構造相關，不是耳咽管開口處。",
            "C": "內壁面向內耳，含岬、前庭窗與蝸窗等構造，不是耳咽管開口。",
            "D": "外壁主要由鼓膜形成，不是耳咽管開口所在。",
        },
        "core": "鼓室前壁有 auditory tube；後通乳突、內鄰內耳、外為鼓膜。",
        "key": "耳咽管開口於鼓室前壁。",
    },
    12: {
        "topic": "聲門裂開啟 / posterior cricoarytenoid",
        "analysis": "題目問哪條肌肉收縮會打開聲門裂。後環杓肌是唯一主要外展聲帶的喉內肌，收縮時使杓狀軟骨旋轉並打開聲門。",
        "options": {
            "A": "後環杓肌外展聲帶、打開聲門裂，是呼吸時開聲門的關鍵肌肉。",
            "B": "外側環杓肌內收聲帶，作用是關閉聲門裂，不是打開。",
            "C": "橫杓肌使兩側杓狀軟骨靠近，內收聲帶後部，會關閉聲門裂。",
            "D": "斜杓肌也參與關閉喉入口與內收，不是主要打開聲門的肌肉。",
        },
        "core": "唯一外展聲帶、打開 rima glottidis 的喉內肌是 posterior cricoarytenoid。",
        "key": "後環杓肌收縮可外展聲帶並打開聲門裂。",
    },
    13: {
        "topic": "翼下頷縫 / buccinator",
        "analysis": "翼下頷縫是上咽縮肌與頰肌的共同附著纖維縫。頰肌部分起自翼下頷縫，協助把食物保持在齒列間。",
        "options": {
            "A": "口輪匝肌圍繞口裂，主要作用於閉唇與噘嘴，不是翼下頷縫的典型起點。",
            "B": "笑肌由腮腺筋膜與咬肌筋膜區域到口角，與翼下頷縫無主要起始關係。",
            "C": "顴大肌由顴骨到口角，負責上提口角，不起自翼下頷縫。",
            "D": "頰肌部分起自翼下頷縫，也是咀嚼時維持食團位置的重要肌肉。",
        },
        "core": "pterygomandibular raphe 連著 buccinator 與 superior constrictor，是口腔與咽部交界的常考附著點。",
        "key": "頰肌部分起自翼下頷縫。",
    },
    14: {
        "topic": "竇房結 / crista terminalis / SVC-RA junction",
        "analysis": "竇房結是心臟主要節律點，最常位在右心房上部，靠近上腔靜脈開口與界嵴上端交界處。",
        "options": {
            "A": "冠狀竇開口附近較接近房室結位置，不是竇房結最常位置。",
            "B": "竇房結位於界嵴靠近上腔靜脈與右心房交界處，是典型解剖位置。",
            "C": "房室間隔內較符合房室結與傳導束區域，不是竇房結。",
            "D": "上腔靜脈與心房間隔交界不是標準描述；竇房結更靠右心房外側壁與界嵴上端。",
        },
        "core": "SA node 在 SVC 進入右心房處附近、靠 crista terminalis；AV node 才接近冠狀竇口與房室間隔。",
        "key": "竇房結最常位於界嵴上端、靠近上腔靜脈與右心房交界。",
    },
    15: {
        "topic": "胸骨左緣穿刺傷 / 右心室前表面",
        "analysis": "心臟胸肋面主要由右心室構成。第四肋間胸骨左緣的穿刺傷會先碰到靠前胸壁的右心室。",
        "options": {
            "A": "左心房主要位於心臟後方，形成心底，不是胸骨左緣前方最先受傷的部位。",
            "B": "左心室形成心尖與左下緣較多，但前胸壁中央胸骨旁主要不是左心室。",
            "C": "右心房在右側心緣較明顯，不是第四肋間胸骨左緣最前方主要結構。",
            "D": "右心室形成大部分胸肋面，位於胸骨後方，胸骨左緣穿刺最可能先傷及右心室。",
        },
        "core": "心臟前表面大多是右心室；後方才是左心房，心尖多為左心室。",
        "key": "第四肋間胸骨左緣穿刺最可能先傷及右心室。",
    },
    16: {
        "topic": "肺小舌 / 左肺上葉",
        "analysis": "肺小舌是左肺上葉的一部分，可視為左肺對應右肺中葉的解剖特徵，位於心切跡下方。",
        "options": {
            "A": "右肺上葉沒有 lingula；右肺有上、中、下三葉。",
            "B": "左肺上葉包含肺小舌，是本題正確位置。",
            "C": "左肺下葉位於斜裂下後方，不包含肺小舌。",
            "D": "右肺下葉也不含肺小舌。",
        },
        "core": "Lingula 是 left superior lobe 的舌狀突起，常被拿來和右肺中葉對比。",
        "key": "肺小舌位於左肺上葉。",
    },
    17: {
        "topic": "肋溝 / VAN",
        "analysis": "肋溝位在肋骨下緣，肋間神經血管束在其中由上到下排列為 vein、artery、nerve，也就是 VAN。",
        "options": {
            "A": "動脈在中間，不是最上方，因此順序不對。",
            "B": "神經在最下方，不是最上方；此排列錯誤。",
            "C": "由上到下為肋間靜脈、肋間動脈、肋間神經，符合 VAN。",
            "D": "神經不在最上方，動脈也不在最下方，因此錯誤。",
        },
        "core": "肋骨下緣肋溝內排列是 VAN；胸腔穿刺要靠肋骨上緣走，避免傷到下緣神經血管束。",
        "key": "肋溝內由上到下排列為肋間靜脈、肋間動脈、肋間神經。",
    },
    18: {
        "topic": "橫膈中央肌腱 / IVC / T8",
        "analysis": "穿過橫膈中央肌腱的是下腔靜脈，位置約 T8。食道與迷走神經幹穿過食道裂孔，主動脈則經主動脈裂孔。",
        "options": {
            "A": "主動脈經 T12 的主動脈裂孔，位於橫膈腳後方，不穿中央肌腱。",
            "B": "食道經 T10 食道裂孔，並非中央肌腱。",
            "C": "迷走神經幹伴食道通過食道裂孔，不是中央肌腱的主要穿行物。",
            "D": "下腔靜脈穿過中央肌腱的腔靜脈孔，約在 T8，是正確答案。",
        },
        "core": "橫膈孔記憶：T8 IVC、T10 esophagus、T12 aorta；只有 IVC 穿中央肌腱。",
        "key": "下腔靜脈穿過橫膈中央肌腱。",
    },
    19: {
        "topic": "大腸特徵 / greater curvature",
        "analysis": "題目問不是大腸特徵。大腸有腸脂垂、結腸帶與結腸袋；大彎是胃的解剖構造。",
        "options": {
            "A": "腸脂垂是結腸表面脂肪突起，屬大腸特徵。",
            "B": "結腸帶是大腸縱行肌聚集成三條帶狀構造，屬大腸特徵。",
            "C": "結腸袋是結腸分節膨出的外觀，屬大腸特徵。",
            "D": "大彎是胃的外側長弧緣，不是大腸特徵；題目問不是，故選此項。",
        },
        "core": "大腸三特徵：taeniae coli、haustra、omental appendices；greater curvature 屬胃。",
        "key": "大彎是胃的構造，不是大腸特徵。",
    },
    20: {
        "topic": "直接腹股溝疝氣 / medial inguinal fossa / Hesselbach triangle",
        "analysis": "直接型腹股溝疝氣由腹壁薄弱處直接突出，位在下腹壁動脈內側，對應腹股溝內側窩與 Hesselbach triangle。",
        "options": {
            "A": "腹股溝外側窩在下腹壁動脈外側，對應間接型疝氣經深腹股溝環進入。",
            "B": "腹股溝內側窩位於下腹壁動脈內側，是直接型腹股溝疝氣好發處。",
            "C": "膀胱上窩更靠內側，和膀胱上疝相關，不是典型直接腹股溝疝氣位置。",
            "D": "鼠蹊韌帶下方較屬股疝氣路徑，不是直接腹股溝疝氣。",
        },
        "core": "直接疝在 inferior epigastric vessels 內側，間接疝在外側並經深環。",
        "key": "直接型腹股溝疝氣好發於腹股溝內側窩。",
    },
    21: {
        "topic": "闌尾初期痛 / periumbilical pain / T10",
        "analysis": "闌尾源自中腸，初期內臟痛常以肚臍周圍疼痛表現，對應 T10 皮節；後期腹膜受刺激才轉為右下腹局部痛。",
        "options": {
            "A": "T6 較接近上腹部皮節，不是典型闌尾內臟痛投射。",
            "B": "T10 對應肚臍皮節，也是中腸闌尾初期內臟痛的投射節段。",
            "C": "L1 較偏腹股溝區域，不是肚臍周圍闌尾痛的典型節段。",
            "D": "L5 屬下肢皮節，與闌尾初期內臟痛無關。",
        },
        "core": "闌尾炎初期 periumbilical pain 對應 T10；局部腹膜炎後才移到 McBurney point。",
        "key": "闌尾炎初期肚臍周圍內臟痛與 T10 節段相關。",
    },
    22: {
        "topic": "腹股溝管 / round ligament of uterus",
        "analysis": "女性腹股溝管內有子宮圓韌帶，男性則有精索。卵巢韌帶、子宮薦骨韌帶與主韌帶都位於骨盆內，並不通過腹股溝管。",
        "options": {
            "A": "子宮圓韌帶由子宮角走向大陰唇，會通過腹股溝管，是正確答案。",
            "B": "卵巢韌帶連接卵巢與子宮，位於骨盆內，不通過腹股溝管。",
            "C": "子宮薦骨韌帶由子宮頸向薦骨，位於骨盆深部，不走腹股溝管。",
            "D": "主韌帶支撐子宮頸並含子宮血管，位於闊韌帶基部，不通過腹股溝管。",
        },
        "core": "女性腹股溝管通過 round ligament；男性通過 spermatic cord。",
        "key": "子宮圓韌帶會延伸通過腹股溝管。",
    },
    23: {
        "topic": "陰莖血管 / Buck fascia / deep dorsal vein",
        "analysis": "題目考陰莖背側血管筋膜層次。陰莖深背靜脈位於陰莖背面、Buck fascia 深層，走在兩條陰莖背動脈之間。",
        "options": {
            "A": "陰莖背動脈位於 Buck fascia 深層，不是在淺層；淺層較有 superficial dorsal vein。",
            "B": "陰莖海綿體勃起主要由深動脈供血，背動脈主要供應龜頭與皮膚，不是海綿體主要來源。",
            "C": "陰莖深背靜脈位於背面且在 Buck fascia 深層，敘述正確。",
            "D": "陰莖有豐富淋巴回流，龜頭與皮膚可回流至腹股溝或骨盆淋巴結，因此此敘述錯誤。",
        },
        "core": "Buck fascia 深層有 deep dorsal vein、dorsal arteries 與 dorsal nerves；勃起供血重點是 deep artery of penis。",
        "key": "陰莖深背靜脈走在陰莖背面且位於 Buck fascia 深層。",
    },
    24: {
        "topic": "輸尿管血供 / obturator artery",
        "analysis": "輸尿管血供來自沿途附近血管，上段可由腎、性腺動脈等，中下段可由髂內、子宮、膀胱動脈分支供應；閉孔動脈不是典型輸尿管血供來源。",
        "options": {
            "A": "下膀胱動脈可供應男性遠端輸尿管與膀胱附近區域，因此可列入輸尿管血供。",
            "B": "閉孔動脈主要供應內收肌區與髖關節附近，不是輸尿管的典型供血來源；題目問不供應，故選此項。",
            "C": "子宮動脈在女性骨盆會跨越輸尿管，並可供應遠端輸尿管。",
            "D": "髂內動脈及其分支可供應骨盆段輸尿管。",
        },
        "core": "輸尿管血供是分段、沿途就近供應；骨盆段常來自 iliac、uterine、vesical 系統，obturator artery 不是典型來源。",
        "key": "閉孔動脈不是輸尿管的典型血液供應來源。",
    },
    25: {
        "topic": "直腸內臟感覺 / pelvic splanchnic / S2-S4 DRG",
        "analysis": "直腸尤其骨盆內臟的一般內臟感覺，常隨副交感 pelvic splanchnic nerve 回到 S2-S4，初級感覺神經元胞體位於對應背根神經節。",
        "options": {
            "A": "L4-L5 較偏下肢體感覺節段，不是直腸內臟感覺主要回傳節段。",
            "B": "L1-L3 可涉及部分骨盆或交感相關痛覺，但本題一般直腸內臟感覺最佳答案為 S2-S4。",
            "C": "S2-S4 是 pelvic splanchnic nerve 對應節段，直腸內臟感覺初級神經元位於這些背根神經節。",
            "D": "T10-T12 較常對應中腸或上腹部內臟痛，不是直腸主要節段。",
        },
        "core": "骨盆副交感與許多骨盆內臟感覺記 S2-S4；初級感覺神經元胞體在 DRG。",
        "key": "直腸一般內臟感覺初級神經元主要位於 S2-S4 背根神經節。",
    },
    26: {
        "topic": "三角肌粗隆 / humerus",
        "analysis": "三角肌粗隆是肱骨外側中段的粗糙突起，為三角肌附著處。",
        "options": {
            "A": "胸骨是前胸壁骨，不具有三角肌粗隆。",
            "B": "鎖骨有三角肌附著的鎖骨外側三分之一，但三角肌粗隆不在鎖骨上。",
            "C": "肱骨外側中段有三角肌粗隆，是三角肌止點。",
            "D": "肩胛骨提供三角肌起點之一，但沒有名為三角肌粗隆的構造。",
        },
        "core": "Deltoid tuberosity 是 humerus 的三角肌止點。",
        "key": "三角肌粗隆位於肱骨。",
    },
    27: {
        "topic": "屈肌支持帶 / Guyon canal / ulnar artery",
        "analysis": "腕隧道內、屈肌支持帶深層有正中神經與屈肌肌腱；尺動脈與尺神經走在屈肌支持帶淺層的 Guyon canal 區域。",
        "options": {
            "A": "尺動脈位於屈肌支持帶淺層，與尺神經一起經 Guyon canal 區域通過。",
            "B": "正中神經在屈肌支持帶深層的腕隧道內，不在淺層。",
            "C": "屈拇長肌腱通過腕隧道，位於屈肌支持帶深層。",
            "D": "屈指淺肌腱也在腕隧道內，位於屈肌支持帶深層。",
        },
        "core": "腕隧道在 flexor retinaculum 深層；ulnar artery/nerve 通過淺層 Guyon canal。",
        "key": "尺動脈位於屈肌支持帶的淺層。",
    },
    28: {
        "topic": "前十字韌帶 / intracapsular extrasynovial",
        "analysis": "前十字韌帶位於膝關節囊內，但被滑膜反折排除在滑液腔外，因此是 intracapsular but extrasynovial。",
        "options": {
            "A": "ACL 在關節囊內，但不是滑液囊內；說兩者都在內不正確。",
            "B": "ACL 位於關節囊內、滑液囊外，是標準描述。",
            "C": "ACL 不是關節囊外構造，所以此敘述錯誤。",
            "D": "ACL 並非關節囊外，也非完全在滑液囊外的囊外韌帶。",
        },
        "core": "十字韌帶是 intracapsular, extrasynovial；這是膝關節解剖常考句。",
        "key": "前十字韌帶位於關節囊內，但在滑液囊外。",
    },
    29: {
        "topic": "膝跳反射 / femoral nerve / L2-L4",
        "analysis": "膝跳反射是敲擊髕韌帶造成股四頭肌伸膝，反射弧經股神經，主要測 L2-L4，臨床常強調 L4。",
        "options": {
            "A": "T9-T12 與腹壁或軀幹節段較相關，不是膝跳反射主要節段。",
            "B": "T11-L1 仍偏上腰腹壁與髂腹股溝區，不是股四頭肌反射主節段。",
            "C": "L2-L4 經股神經支配股四頭肌，是膝跳反射主要檢測節段。",
            "D": "L5-S2 較接近跟腱反射或下肢其他肌群，不是膝跳反射主節段。",
        },
        "core": "Knee jerk = femoral nerve = L2-L4；Achilles reflex 才多記 S1。",
        "key": "膝跳反射主要檢測 L2-L4 節段。",
    },
    30: {
        "topic": "腓骨長肌 / 足底橫行 / 第一蹠骨與內側楔骨",
        "analysis": "腓骨長肌肌腱繞過外踝後進入足底，從外側斜跨足底至第一蹠骨基底與內側楔骨，支撐橫弓與外翻足部。",
        "options": {
            "A": "腓骨短肌止於第五蹠骨粗隆，不橫跨足底到第一蹠骨與楔骨。",
            "B": "腓骨長肌由外側跨過足底，附著於第一蹠骨與內側楔骨，是正確答案。",
            "C": "屈拇長肌經足底內側到大拇趾遠節趾骨，不附著第一蹠骨與楔骨。",
            "D": "屈趾長肌分到外側四趾遠節趾骨，不是橫跨足底到第一蹠骨的肌腱。",
        },
        "core": "Fibularis longus tendon 橫跨足底到第一蹠骨與內側楔骨；fibularis brevis 止於第五蹠骨。",
        "key": "腓骨長肌肌腱從外側橫跨足底，止於第一蹠骨與內側楔骨。",
    },
    31: {
        "topic": "旋前圓肌 / median nerve",
        "analysis": "正中神經在肘窩區常穿過旋前圓肌兩頭之間進入前臂。旋前圓肌中央撕裂最可能直接傷及正中神經。",
        "options": {
            "A": "橈神經在肘部外側分支至深支與淺支，與旋前圓肌中央不是最直接關係。",
            "B": "尺神經經肱骨內上髁後方進入前臂，並不穿過旋前圓肌中央。",
            "C": "正中神經穿行於旋前圓肌兩頭之間，旋前圓肌撕裂最可能直接影響它。",
            "D": "尺神經不穿旋前圓肌，因此不需要同時選正中神經與尺神經。",
        },
        "core": "Pronator teres syndrome 牽涉 median nerve；ulnar nerve 走內上髁後方。",
        "key": "正中神經穿過旋前圓肌兩頭之間，最容易受旋前圓肌中央傷害影響。",
    },
    32: {
        "topic": "第三週胚胎 / gastrulation / pharyngeal arch",
        "analysis": "第三週主要事件包括原條形成、脊索形成與三胚層建立。咽弓主要在第四週開始明顯出現，因此第三週結束時尚未出現。",
        "options": {
            "A": "原條是第三週 gastrulation 的核心構造，已經出現。",
            "B": "脊索在第三週形成，參與軸向誘導。",
            "C": "中胚層在第三週 gastrulation 中形成，已經存在。",
            "D": "咽弓典型於第四週出現，第三週結束時尚未明顯形成。",
        },
        "core": "第三週記 gastrulation、三胚層、notochord；第四週才常考 pharyngeal arches。",
        "key": "咽弓通常第四週才明顯出現，不是第三週結束前的構造。",
    },
    33: {
        "topic": "甲狀腺發育 / foramen cecum / ultimobranchial body",
        "analysis": "甲狀腺來自原始咽底內胚層增厚，起點在舌盲孔，之後沿甲狀舌管下降。濾泡旁 C 細胞來自第四咽囊相關的 ultimobranchial body。選項把起點說成門齒窩，故錯。",
        "options": {
            "A": "甲狀腺濾泡上皮主要由原始咽部內胚層增厚形成，敘述正確。",
            "B": "甲狀腺憩室會從咽底下降到頸部腹側位置，敘述正確。",
            "C": "甲狀腺憩室離開咽部的起點是舌盲孔 foramen cecum，不是門齒窩；題目問錯誤，故選此項。",
            "D": "甲狀腺 C 細胞與第四咽囊衍生的 ultimobranchial body 相關，敘述可接受。",
        },
        "core": "甲狀腺下降起點是 foramen cecum；看到 incisive fossa 要排除。",
        "key": "甲狀腺憩室起自舌盲孔，不是門齒窩。",
    },
    34: {
        "topic": "中腎管 / seminal vesicle",
        "analysis": "男性內生殖管多由中腎管衍生。精囊由中腎管末端旁芽形成；前列腺與尿道球腺主要來自尿生殖竇內胚層。",
        "options": {
            "A": "前列腺主要由尿生殖竇內胚層芽生形成，不是中腎管末端。",
            "B": "前列腺囊是副中腎管殘跡相關構造，不是中腎管末端形成精囊的答案。",
            "C": "精囊由中腎管末端長出的芽形成，是本題正確答案。",
            "D": "尿道球腺來自尿生殖竇，不是中腎管末端。",
        },
        "core": "Wolffian duct 衍生 epididymis、ductus deferens、seminal vesicle、ejaculatory duct；prostate 來自 urogenital sinus。",
        "key": "精囊由中腎管末端形成。",
    },
    35: {
        "topic": "第四週靜脈回流 / sinus venosus / endometrial vein",
        "analysis": "胚胎第四週注入原始心臟靜脈竇的主要靜脈包含卵黃囊靜脈、臍靜脈與總主靜脈。子宮內膜靜脈屬母體子宮血管，不直接注入胎兒心臟。",
        "options": {
            "A": "卵黃囊靜脈會將卵黃囊血液帶回胚胎心臟，會注入靜脈竇。",
            "B": "臍靜脈帶來胎盤含氧血，會回到胎兒循環。",
            "C": "總主靜脈是早期胚胎體循環回流至靜脈竇的重要血管。",
            "D": "子宮內膜靜脈是母體側血管，不直接注入胎兒心臟；題目問不注入，故選此項。",
        },
        "core": "早期胎兒心臟靜脈流入記 vitelline、umbilical、common cardinal veins。",
        "key": "子宮內膜靜脈屬母體血管，不直接注入胎兒心臟。",
    },
    36: {
        "topic": "舟形頭 / sagittal suture craniosynostosis",
        "analysis": "舟形頭 scaphocephaly 是顱骨前後徑變長、左右徑變窄的長楔形頭，典型由矢狀縫過早閉合造成。",
        "options": {
            "A": "前囟閉合異常不是典型造成舟形頭的答案。",
            "B": "後囟也不是造成前後徑拉長舟形頭的主要縫線。",
            "C": "冠狀縫早閉常造成短頭或斜頭型變化，不是典型舟形頭。",
            "D": "矢狀縫早閉限制左右擴張，代償前後增長，形成舟形頭。",
        },
        "core": "Scaphocephaly = sagittal suture premature closure。",
        "key": "矢狀縫過早閉合會造成舟形頭。",
    },
    37: {
        "topic": "泌尿上皮 / transitional epithelium",
        "analysis": "泌尿道如腎盂、輸尿管與膀胱的上皮需適應伸展，主要是移形上皮，又稱 urothelium。",
        "options": {
            "A": "單層上皮無法概括泌尿上皮多層且可伸展的特性。",
            "B": "偽複層上皮常見於呼吸道等，不是典型尿路上皮。",
            "C": "移形上皮可隨尿液充盈伸展，是泌尿上皮的正確分類。",
            "D": "類上皮組織不是尿路上皮的標準組織學分類。",
        },
        "core": "Urothelium = transitional epithelium，可伸展且保護尿路免受尿液刺激。",
        "key": "泌尿上皮主要屬於移形上皮。",
    },
    38: {
        "topic": "微小管直徑 / 25 nm",
        "analysis": "細胞骨架尺寸常考：微絲約 7 nm，中間絲約 10 nm，微小管外徑約 25 nm。",
        "options": {
            "A": "2 到 2.5 nm 太小，低於常見細胞骨架纖維直徑。",
            "B": "20 到 25 nm 符合微小管約 25 nm 的平均外徑。",
            "C": "200 到 250 nm 遠大於微小管，接近較大細胞結構尺度。",
            "D": "2000 到 2500 nm 已是微米等級，遠超過微小管直徑。",
        },
        "core": "微小管約 25 nm；中間絲約 10 nm；微絲約 7 nm。",
        "key": "微小管平均直徑約 20-25 nm。",
    },
    39: {
        "topic": "軟骨類型 / epiglottis elastic cartilage",
        "analysis": "題目問軟骨何者正確。會厭需要彈性與回彈，因此為彈性軟骨；胎兒骨骼模型和關節面多為透明軟骨，椎間盤則主要為纖維軟骨。",
        "options": {
            "A": "胎兒長骨模型主要是透明軟骨，不是一開始由纖維軟骨構成。",
            "B": "滑液關節的關節軟骨面主要為透明軟骨，不是彈性軟骨。",
            "C": "椎間盤特別是纖維環富含纖維軟骨，不是單純透明軟骨。",
            "D": "會厭軟骨需要彈性回復，屬於彈性軟骨，敘述正確。",
        },
        "core": "透明軟骨：關節面與胎兒骨架模型；纖維軟骨：椎間盤；彈性軟骨：會厭與耳廓。",
        "key": "會厭軟骨屬於彈性軟骨。",
    },
    40: {
        "topic": "中樞膠細胞 / astrocyte subtypes",
        "analysis": "題目問 CNS 膠細胞何者錯誤。原漿性星狀膠細胞主要位於灰質，纖維性星狀膠細胞主要位於白質；寡突膠細胞形成 CNS 髓鞘，微小膠細胞是吞噬細胞。",
        "options": {
            "A": "寡突膠細胞負責 CNS 髓鞘形成與維持，敘述正確。",
            "B": "原漿性星狀膠細胞主要在灰質，不是白質；題目問錯誤，故選此項。",
            "C": "微小膠細胞源自單核吞噬系統，是 CNS 主要吞噬與免疫監視細胞，敘述正確。",
            "D": "纖維性星狀膠細胞突起較長較直、較少，原漿性者突起較多且分枝，敘述正確。",
        },
        "core": "Protoplasmic astrocyte 在灰質；fibrous astrocyte 在白質。",
        "key": "原漿性星狀膠細胞主要位於灰質，不是白質。",
    },
    41: {
        "topic": "細支氣管 / smooth muscle / 無軟骨腺體",
        "analysis": "細支氣管相較支氣管，沒有軟骨板與黏膜下腺，但管壁有平滑肌並含彈性纖維，上皮逐漸由纖毛柱狀變為單層立方。",
        "options": {
            "A": "細支氣管越往遠端上皮會變低，並非整段都為具纖毛偽複層柱狀上皮。",
            "B": "細支氣管管壁有平滑肌，可調節氣道阻力，是正確敘述。",
            "C": "細支氣管沒有軟骨板與黏膜下腺，這是和支氣管的差異。",
            "D": "細支氣管仍有彈性纖維，有助呼吸週期中的回彈。",
        },
        "core": "Bronchiole 有 smooth muscle、無 cartilage、無 submucosal gland。",
        "key": "細支氣管管壁具有平滑肌，但沒有軟骨板與腺體。",
    },
    42: {
        "topic": "胰臟 / centroacinar cells",
        "analysis": "胰臟外分泌腺泡有泡心細胞，代表閏管細胞伸入腺泡中心，是區分胰臟與唾液腺的重要特徵；耳下腺沒有泡心細胞。",
        "options": {
            "A": "耳下腺與胰臟都可見漿液性腺泡及酵素原顆粒，不是胰臟獨有。",
            "B": "泡心細胞是胰臟特徵，耳下腺沒有，是正確答案。",
            "C": "小葉間管可見於多種外分泌腺，不是胰臟獨有。",
            "D": "閏管在胰臟與耳下腺皆可見，不能用來區分。",
        },
        "core": "Pancreas 特徵是 centroacinar cells；parotid 是純漿液腺但無泡心細胞。",
        "key": "泡心細胞存在於胰臟，不存在於耳下腺。",
    },
    43: {
        "topic": "唾液腺 / intercalated duct / sublingual gland",
        "analysis": "題目問唾液腺何者錯誤。閏管在耳下腺較發達，在舌下腺最不發達；舌下腺以黏液腺為主。",
        "options": {
            "A": "耳下腺主要為漿液腺，敘述正確。",
            "B": "閏管在舌下腺並非最發達，通常耳下腺較發達；題目問錯誤，故選此項。",
            "C": "下頜下腺為混合腺，以漿液性成分較多，敘述可接受。",
            "D": "線紋管底部有粒線體與基底膜皺褶，利於離子運輸，敘述正確。",
        },
        "core": "Parotid 純漿液且閏管明顯；sublingual 黏液為主且閏管不發達。",
        "key": "唾液腺閏管不是在舌下腺最發達。",
    },
    44: {
        "topic": "腎小管上皮 / papillary duct",
        "analysis": "近曲小管、遠曲小管與集尿小管多為單層立方上皮。乳頭管，也就是 Bellini duct，管徑較大，常呈單層柱狀或較高上皮，因此不是主要單層立方。",
        "options": {
            "A": "乳頭管上皮較高，可為單層柱狀，並非主要單層立方；題目問不是，故選此項。",
            "B": "近曲小管典型為單層立方上皮，具刷狀緣。",
            "C": "集尿小管多為單層立方上皮，往乳頭管逐漸變高。",
            "D": "遠曲小管主要為單層立方上皮，刷狀緣不明顯。",
        },
        "core": "腎小管多為 simple cuboidal；papillary duct 管徑大且上皮較高，是常見例外。",
        "key": "乳頭管主要不是單層立方上皮，可呈較高柱狀上皮。",
    },
    45: {
        "topic": "蔓狀叢 / atypical vein / countercurrent heat exchange",
        "analysis": "蔓狀叢是精索內包繞睪丸動脈的靜脈網，具較厚肌肉壁，屬非典型靜脈，有助逆流熱交換與睪丸降溫。",
        "options": {
            "A": "蔓狀叢不是僅有環走平滑肌層，靜脈壁結構較特殊且肌肉較厚。",
            "B": "肌肉層描述不能只限於一般中膜層概念，蔓狀叢被列為非典型靜脈。",
            "C": "蔓狀叢位於精索內、睪丸外周附近，不是在睪丸實質中。",
            "D": "蔓狀叢有較厚肌肉壁，屬非典型靜脈，敘述正確。",
        },
        "core": "Pampiniform plexus 是精索內非典型靜脈網，功能是睪丸動脈逆流熱交換。",
        "key": "蔓狀叢有較厚肌肉壁，屬於非典型靜脈。",
    },
    46: {
        "topic": "三級絨毛 / syncytial knots / 胎盤成熟",
        "analysis": "三級絨毛含胎兒血管，外層為合胞滋養層。懷孕晚期細胞滋養層變薄不連續，合胞體結增加，可用來評估絨毛成熟度。",
        "options": {
            "A": "合胞體結數量會隨胎盤絨毛成熟增加，可作為成熟度指標，敘述正確。",
            "B": "懷孕晚期細胞滋養層通常變薄且不連續，不是完整且顯著的外層。",
            "C": "三級絨毛具有胎兒血管，也有合胞滋養層，此敘述錯誤。",
            "D": "三級絨毛基質除間葉細胞與纖維母細胞外，也含血管與其他基質成分，不是只含這兩者。",
        },
        "core": "Tertiary villi 特色是含血管；胎盤成熟可見 syncytial knots 增加、屏障變薄。",
        "key": "合胞體結數目可協助評估胎盤絨毛成熟度。",
    },
    47: {
        "topic": "膜通透性 / glucose / transporter",
        "analysis": "簡單擴散最適合小型非極性分子或未帶電脂溶性分子。葡萄糖體積較大且親水，需 GLUT 或 SGLT 等蛋白協助跨膜。",
        "options": {
            "A": "二氧化碳小且非極性，可快速簡單擴散通過細胞膜。",
            "B": "甘油雖具極性，但小分子可相對有限地穿膜，也可有 aquaglyceroporin；不如葡萄糖依賴轉運蛋白。",
            "C": "醋酸在未解離型態可較容易通過脂質雙層。",
            "D": "葡萄糖親水且較大，通常需 GLUT 或 SGLT 等蛋白協助進出細胞，是最不能單純擴散者。",
        },
        "core": "大而親水的營養分子通常需要 transporter；CO2 這類小非極性分子可簡單擴散。",
        "key": "葡萄糖需藉由轉運蛋白進出細胞，不能有效簡單擴散。",
    },
    48: {
        "topic": "視網膜 / cones rods / 數量與視覺敏銳度",
        "analysis": "題目問最不適當。錐細胞解析度高是因為在黃斑中央凹有高度集中與低匯聚，而不是因為總數比桿細胞多；事實上桿細胞總數遠多於錐細胞。",
        "options": {
            "A": "感光細胞外節位於視網膜外層、遠離玻璃體，方向描述正確。",
            "B": "錐細胞總數不是遠多於桿細胞；錐細胞解析度高主要因中央凹分布與神經匯聚少，故此敘述最不適當。",
            "C": "亮適應涉及視紫質分解與感光系統敏感度下降，通常比暗適應快，敘述可接受。",
            "D": "錐細胞需較強光，暗處偵測微弱光源時不要用中央凹直視，改用旁視可動員桿細胞，敘述合理。",
        },
        "core": "Rods 數量多、暗視敏感；cones 在中央凹解析度高，但總數少於 rods。",
        "key": "錐細胞對視覺敏銳度貢獻高不是因為總數多於桿細胞。",
    },
    49: {
        "topic": "去大腦僵直 / midbrain lesion / extensor rigidity",
        "analysis": "病灶位於中腦四疊體中線附近，會切斷紅核以上對屈肌的促進並保留橋腦網狀脊髓徑對伸肌的促進，形成去大腦僵直，四肢伸直僵硬。",
        "options": {
            "A": "上下肢皆伸直僵硬符合去大腦僵直，常見於紅核以下或中腦嚴重病灶造成伸肌張力優勢。",
            "B": "上肢屈曲、下肢伸直較符合去皮質姿勢，病灶通常在紅核以上。",
            "C": "下肢屈曲、上肢伸直不是此類中腦病灶的典型姿勢。",
            "D": "完全失去張力不符合橋腦網狀脊髓徑仍促進伸肌的設定。",
        },
        "core": "Decerebrate rigidity 是上下肢伸直；decorticate posture 是上肢屈曲、下肢伸直。",
        "key": "中腦紅核以下功能受損可造成去大腦僵直，表現為上下肢伸直僵硬。",
    },
    50: {
        "topic": "交感反應 / fight-or-flight / 瞳孔散大",
        "analysis": "極大生命威脅時交感神經活化，典型反應包括血壓上升、血糖上升、支氣管擴張與瞳孔散大。瞳孔縮小屬副交感優勢反應，最不可能出現。",
        "options": {
            "A": "交感活化使心輸出量與血管張力上升，血壓升高是典型反應。",
            "B": "交感反應會造成瞳孔散大，不是縮小；題目問最不可能，故選此項。",
            "C": "腎上腺素與交感活化會促進肝醣分解與糖質新生，血糖升高合理。",
            "D": "交感 beta-2 作用會使支氣管平滑肌放鬆，有助通氣。",
        },
        "core": "Fight-or-flight：mydriasis、bronchodilation、血糖升高、血壓上升；miosis 是副交感。",
        "key": "重大威脅下交感活化會使瞳孔散大，不會使瞳孔縮小。",
    },
    51: {
        "topic": "制約記憶 / corpus callosum / bilateral cortical storage",
        "analysis": "切斷 optic chiasm 不影響兩眼表現，表示記憶不是靠視交叉單一路徑傳遞；切斷 corpus callosum 後未訓練側眼不能表現，表示兩側大腦皮質可各自存放或接收該制約記憶，左右半球間需靠胼胝體整合。",
        "options": {
            "A": "結果強調跨半球傳遞與雙側可存放，不是單純某一側皮質功能側化。",
            "B": "若記憶僅存於左腦皮質，無法解釋正常情況左右眼皆能表現且需胼胝體傳遞。",
            "C": "記憶提取不必然必須經右腦皮質；左眼受訓後左眼仍可表現。",
            "D": "左右眼皆可表現但切斷胼胝體後右眼不能表現，最適合說明記憶可在左右皮質存放或經胼胝體轉移。",
        },
        "core": "此題重點不是 optic chiasm，而是 corpus callosum 對左右大腦皮質記憶表現的連結作用。",
        "key": "該制約記憶可存放於左右大腦皮質，跨半球表現需胼胝體連結。",
    },
    52: {
        "topic": "IPSP / glycine receptor / chloride channel",
        "analysis": "抑制性突觸後電位常由 Cl- 進入或 K+ 外流造成膜電位更負。甘胺酸受體是脊髓與腦幹常見的 ligand-gated chloride channel，開啟後造成 IPSP。",
        "options": {
            "A": "AMPA 受體主要讓 Na+ 內流造成快速 EPSP，屬興奮性麩胺酸受體。",
            "B": "NMDA 受體也是興奮性麩胺酸受體，通透 Na+、K+ 與 Ca2+，不造成典型 IPSP。",
            "C": "甘胺酸受體開啟 Cl- 通道，使膜電位超極化或穩定，造成 IPSP。",
            "D": "尼古丁受體是陽離子通道，活化多造成去極化興奮。",
        },
        "core": "Glycine 和 GABA-A 都是 Cl- channel 型抑制性受體；AMPA/NMDA/nicotinic 多為興奮性陽離子通道。",
        "key": "甘胺酸受體開啟氯離子通道，最可能造成 IPSP。",
    },
    53: {
        "topic": "Serotonin / SSRI / depression",
        "analysis": "血清素多存在於腸嗜鉻細胞與血小板等周邊組織；受體多為 GPCR，只有 5-HT3 是離子通道。SSRI 抑制血清素再攝取，是治療憂鬱症常用藥物。",
        "options": {
            "A": "人體血清素最多在消化道，血小板也含量高，不是大腦最多。",
            "B": "血清素受體大多是 G protein-coupled receptor，只有 5-HT3 是離子通道型。",
            "C": "血清素神經元通常清醒時活性較高，睡眠時下降，REM 期更低。",
            "D": "SSRI 可提高突觸間血清素作用，臨床用於憂鬱症等疾病，敘述正確。",
        },
        "core": "Serotonin 多在腸道；受體大多 GPCR；SSRI 是憂鬱症常用治療。",
        "key": "選擇性血清素再攝取抑制劑可用於治療憂鬱症。",
    },
    54: {
        "topic": "fast pain / A-delta fiber / glutamate",
        "analysis": "Fast pain 是尖銳、定位較準的疼痛，主要由有髓鞘 A-delta 纖維傳遞，傳導速度比 C fiber 快。",
        "options": {
            "A": "C 纖維通常無髓鞘，傳遞慢痛與灼痛，不是有髓鞘 fast pain 纖維。",
            "B": "疼痛初級傳入常釋放 glutamate 或 substance P，不是通常釋放 serotonin。",
            "C": "A-delta 纖維有髓鞘、傳導較快，負責 fast pain，是正確答案。",
            "D": "Fast pain 因傳導快且定位較精確，選項說較 slow pain 不能精確定位是反向錯誤。",
        },
        "core": "Fast pain = myelinated A-delta = sharp, well localized；slow pain = unmyelinated C fiber。",
        "key": "Fast pain 主要由有髓鞘 A-delta 纖維傳遞。",
    },
    55: {
        "topic": "興奮收縮偶合 / T-tubule / 平滑肌",
        "analysis": "題目問錯誤。骨骼肌與心肌有 T-tubule 與 DHPR 參與，但平滑肌沒有典型橫小管系統，鈣來源與調控方式也不同，因此不能說三種肌肉都需要動作電位傳入 T-tubule。",
        "options": {
            "A": "平滑肌沒有典型 T-tubule，且收縮可由多種訊號引發；把心肌、骨骼肌、平滑肌都說成需 T-tubule 是錯誤。",
            "B": "T-tubule 上的 L-type voltage-dependent Ca2+ channel 又稱 dihydropyridine receptor，敘述正確。",
            "C": "骨骼肌 DHPR 活化會機械性改變 RyR 構型，促使肌漿網釋放鈣，敘述正確。",
            "D": "心肌 L-type Ca2+ channel 讓鈣流入，引發 calcium-induced calcium release，敘述正確。",
        },
        "core": "骨骼肌：DHPR 機械偶合 RyR；心肌：Ca2+ influx 觸發 CICR；平滑肌沒有典型 T-tubule。",
        "key": "平滑肌沒有典型橫小管，因此不是三種肌肉都需動作電位傳入 T-tubule。",
    },
    56: {
        "topic": "CO2 transport / bicarbonate / carbaminohemoglobin / 2,3-BPG",
        "analysis": "CO2 在血中以溶解、碳酸氫根，以及與血紅素胺基端形成 carbaminohemoglobin 運送。2,3-BPG 主要調節氧與血紅素親和力，選項所說增加 CO2 與 Fe2+ 結合並非主要機制。",
        "options": {
            "A": "部分 CO2 直接溶於血漿，屬正常運送形式之一。",
            "B": "紅血球碳酸酐酶使 CO2 與水形成碳酸，再解離為 H+ 與 HCO3-，是主要運送機制。",
            "C": "2,3-BPG 主要影響氧解離曲線，CO2 不是靠 Fe2+ 結合運送；此敘述與 CO2 運送最無關。",
            "D": "CO2 可與血紅素蛋白的胺基端結合形成 carbaminohemoglobin，屬運送形式之一。",
        },
        "core": "CO2 運送以 bicarbonate 最多，其次 carbamino compounds 和溶解態；2,3-BPG 是氧親和力調節者。",
        "key": "2,3-BPG 減少與 CO2 運送機制最無關。",
    },
    57: {
        "topic": "SA node / funny current / Na+",
        "analysis": "題目問心臟調控何者錯誤。竇房結自發去極化受 funny current 的 Na+ 內流、Ca2+ 通道與 K+ 外流共同影響，因此說與 Na+ 無關是錯誤。",
        "options": {
            "A": "SA node 同時受交感與副交感調控，以改變心率，敘述正確。",
            "B": "AV node 也受交感與副交感調控，以改變傳導速度，敘述正確。",
            "C": "強迷走刺激可減慢心率，並可降低心房收縮力；整體迷走對心室收縮力影響較小，但此項不如 D 明確錯誤。",
            "D": "SA node 第四期去極化包含 funny Na+ current，並非與鈉離子無關；題目問錯誤，故選此項。",
        },
        "core": "SA node pacemaker potential 重要離子包括 funny Na+ current、T/L-type Ca2+ 與 K+ conductance 改變。",
        "key": "竇房結膜電位調控與 funny Na+ current 有關，不能說與鈉離子無關。",
    },
    58: {
        "topic": "心臟收縮期 / S2 / semilunar valve closure",
        "analysis": "第二心音來自主動脈瓣與肺動脈瓣關閉，標誌心室收縮期結束、舒張期開始。因此在正常心臟收縮期中不會聽到第二心音作為收縮期內事件。",
        "options": {
            "A": "T 波代表心室再極化，發生在收縮後段附近，可與機械收縮期重疊。",
            "B": "第二心音是半月瓣關閉、收縮期結束的聲音，嚴格說不屬於收縮期中發生的現象。",
            "C": "主動脈壓在心室射血期達高峰，屬收縮期現象。",
            "D": "肺動脈壓也在右心室射血期上升達高峰，屬收縮期現象。",
        },
        "core": "S1 開始心室收縮期；S2 結束心室收縮期並開始舒張期。",
        "key": "第二心音代表半月瓣關閉，標誌心室收縮期結束。",
    },
    59: {
        "topic": "運動 / cardiac output / total peripheral resistance",
        "analysis": "長時間費力運動時，心率與心搏量上升，使心輸出量明顯增加；骨骼肌血管擴張使總周邊阻力下降或不會顯著上升。",
        "options": {
            "A": "健康成人費力運動時心輸出量可大幅增加，以供應肌肉氧需求，敘述正確。",
            "B": "運動時骨骼肌血管擴張，總周邊阻力通常下降，不是顯著增加。",
            "C": "耗氧量增加數倍主要靠心輸出量與氧萃取增加，不是心搏量單獨以倍數增加即可解釋。",
            "D": "老化通常使最大心輸出量下降，不會隨年齡緩慢增加。",
        },
        "core": "Exercise increases cardiac output and oxygen extraction; TPR tends to fall because skeletal muscle vasodilation dominates。",
        "key": "費力長時間運動會使心輸出量顯著增加。",
    },
    60: {
        "topic": "Starling forces / net filtration pressure",
        "analysis": "淨過濾壓可用 (毛細血管靜水壓 + 組織膠體滲透壓) - (組織靜水壓 + 血漿膠體滲透壓) 計算。本題為 (15+3)-(0+28) = -10 mmHg，負值表示液體傾向回到微血管。",
        "options": {
            "A": "-16 mmHg 方向雖是流入微血管，但數值計算錯誤。",
            "B": "-10 mmHg 且液體傾向流入微血管，符合 Starling forces 計算。",
            "C": "40 mmHg 為正值且流出，未正確扣除血漿膠體滲透壓。",
            "D": "46 mmHg 更明顯錯估各壓力方向，與公式不符。",
        },
        "core": "NFP = Pc + πi - Pi - πc；正值過濾、負值回吸收。",
        "key": "本題淨過濾壓為 -10 mmHg，液體傾向流入微血管。",
    },
    61: {
        "topic": "平靜呼吸作功 / inspiration active / expiration passive",
        "analysis": "健康者平靜呼吸時，吸氣需橫膈與外肋間肌收縮作功；呼氣主要靠肺與胸壁彈性回縮，通常是被動過程。",
        "options": {
            "A": "平靜呼吸時主要只有吸氣階段需要肌肉作功，正確。",
            "B": "平靜呼氣通常是被動彈性回縮，不是唯一需要作功的階段。",
            "C": "吸氣主動、呼氣被動，兩者作功量不相同。",
            "D": "吸氣需要肌肉收縮，因此不能說兩階段都不需作功。",
        },
        "core": "Quiet breathing: inspiration active, expiration passive；用力呼吸時呼氣肌才明顯參與。",
        "key": "健康者平靜呼吸時主要只有吸氣需要作功。",
    },
    62: {
        "topic": "CO poisoning / oxygen saturation / oxygen content",
        "analysis": "三管都暴露在相同 PO2 40 mmHg 下，溶解氧分壓會趨同。貧血使總氧含量下降但飽和度百分比可接近正常；一氧化碳血紅素使剩餘可用 Hb 氧親和力左移，因此以可結合位點計算的氧飽和百分比可最高，但總氧含量不會相同。",
        "options": {
            "A": "平衡後三管血液氧分壓由相同氣體決定，不會甲最高。",
            "B": "乙管 Hb 濃度減半會使總氧含量約下降，但飽和度百分比不會變成甲的 50%。",
            "C": "丙管有 COHb，使剩餘 Hb 對氧親和力升高、氧解離曲線左移，在 PO2 40 mmHg 下飽和百分比可最高。",
            "D": "氧氣總含量取決於 Hb 濃度與可用結合位點，貧血與 COHb 都會降低總含量，不會三者相同。",
        },
        "core": "Oxygen content 看 Hb amount；oxygen saturation 看可用 Hb 位點比例；CO 會降低總含量並使曲線左移。",
        "key": "COHb 會使剩餘血紅素氧親和力上升，因此丙管血氧飽和百分比可最高。",
    },
    63: {
        "topic": "唾液分泌 / autonomic regulation / Ca2+",
        "analysis": "副交感使唾液量多且較水樣，交感使分泌較少且較黏稠。唾腺受自主神經調控時，細胞內鈣離子是重要第二訊息，例如 muscarinic M3 與 alpha-adrenergic 路徑可提高 Ca2+。",
        "options": {
            "A": "副交感通常使唾液分泌量較多，交感不是量較多的主要狀態。",
            "B": "交感作用下唾液較黏稠；副交感較水樣，選項方向相反。",
            "C": "唾腺細胞受自主神經刺激時會使用 Ca2+ 等訊息因子，敘述最適當。",
            "D": "唾腺效應細胞主要受 muscarinic 與 adrenergic 受體調控，不是以 nicotinic 受體為主要效應受體。",
        },
        "core": "Salivation: parasympathetic = watery, high volume；sympathetic = more viscous；Ca2+ 是重要訊號。",
        "key": "自主神經調控唾腺分泌時，鈣離子是重要細胞內訊息因子。",
    },
    64: {
        "topic": "胃酸分泌 / parietal cell / carbonic anhydrase",
        "analysis": "壁細胞產生胃酸需要碳酸酐酶生成 H+ 與 HCO3-，H+ 再由 H+/K+ ATPase 分泌到胃腔，Cl- 也進入胃腔形成 HCl。",
        "options": {
            "A": "GRP 主要刺激 G cell 分泌 gastrin，再間接促進胃酸，不是直接刺激壁細胞生成胃酸的主要說法。",
            "B": "胃酸分泌關鍵是 H+/K+ ATPase，不是 H+-Cl- cotransporter。",
            "C": "黏液素主要保護黏膜，不是直接抑制 Gs 蛋白以打開氯離子通道來抑制胃酸的機制。",
            "D": "壁細胞需要碳酸酐酶產生 H+，才能有效分泌胃酸，敘述正確。",
        },
        "core": "Parietal cell acid secretion 需要 carbonic anhydrase 與 H+/K+ ATPase；gastrin、ACh、histamine 促進分泌。",
        "key": "胃酸生成需要碳酸酐酶參與。",
    },
    65: {
        "topic": "血漿滲透壓 / 2Na + glucose/18 + BUN/2.8",
        "analysis": "血漿滲透壓估算公式為 2[Na+] + glucose/18 + BUN/2.8。代入 2x135 + 180/18 + 56/2.8 = 270 + 10 + 20 = 300 mOsm/kg H2O。",
        "options": {
            "A": "300 符合 2Na + glucose/18 + BUN/2.8 的計算結果。",
            "B": "310 高估了本題數值，可能多加了鉀或換算錯誤。",
            "C": "320 也高於正確估算，與公式不符。",
            "D": "330 明顯過高，不符合鈉、葡萄糖與 BUN 代入結果。",
        },
        "core": "Serum osmolality ≈ 2Na + glucose/18 + BUN/2.8；本題為 300。",
        "key": "本題血漿滲透壓估算為 300 mOsm/kg H2O。",
    },
    66: {
        "topic": "Bartter syndrome / TAL / NCC",
        "analysis": "Bartter syndrome 是亨利氏環上升厚支 thick ascending limb 的 NKCC2、ROMK、ClC-Kb 等異常，功能上類似 loop diuretic。Na-Cl cotransporter 位於遠曲小管，與 Gitelman syndrome 較相關。",
        "options": {
            "A": "Na+-Cl- cotransporter 位於遠曲小管，非 TAL 的主要 Bartter 致病通道；題目問最不可能，故選此項。",
            "B": "NKCC2 是 TAL 管腔側重要轉運蛋白，Bartter 可由其缺陷造成。",
            "C": "ClC-Kb 氯離子通道異常可造成 Bartter syndrome。",
            "D": "ROMK 參與 TAL 鉀回收與 NKCC2 運作，其缺陷也是 Bartter 機轉之一。",
        },
        "core": "Bartter = TAL = NKCC2/ROMK/ClC-Kb；Gitelman = DCT = Na-Cl cotransporter。",
        "key": "Na+-Cl- cotransporter 位於遠曲小管，最不符合 Bartter syndrome 的 TAL 機轉。",
    },
    67: {
        "topic": "Oxytocin / milk ejection / progesterone",
        "analysis": "催產素促進排乳與子宮平滑肌收縮，分娩時有正回饋。黃體素通常維持妊娠、降低子宮興奮性，不會刺激催產素促進子宮收縮的作用。",
        "options": {
            "A": "催產素使乳腺肌上皮細胞收縮，是排乳反射主要荷爾蒙，正確。",
            "B": "嬰兒吸吮乳房可刺激下視丘-後葉釋放催產素，正確。",
            "C": "黃體素通常抑制子宮收縮、維持妊娠，不會刺激催產素促收縮作用；題目問錯誤，故選此項。",
            "D": "分娩時子宮頸擴張促進催產素分泌，進一步增強收縮，屬正回饋。",
        },
        "core": "Oxytocin 負責 milk ejection 與 uterine contraction；progesterone 通常維持子宮安定。",
        "key": "黃體素不會刺激催產素促進子宮收縮的作用。",
    },
    68: {
        "topic": "Growth hormone / JAK-STAT / acromegaly / glucose",
        "analysis": "生長激素受體屬 cytokine receptor，活化需二聚合並啟動 JAK-STAT。GH 促進蛋白合成、抗胰島素作用使血糖上升；長期 GH 不足反而較可能低血糖或生長不良，不會造成血糖升高。",
        "options": {
            "A": "GH 受體二聚合是訊號活化的重要步驟，敘述正確。",
            "B": "GH 過多會促進蛋白質合成與組織生長，敘述正確。",
            "C": "體抑素類似物可抑制 GH 分泌，用於肢端肥大症治療，敘述正確。",
            "D": "GH 具有升糖與抗胰島素作用；長期不足不會造成血糖升高，題目問錯誤故選此項。",
        },
        "core": "GH 過多會升糖、促生長；GH 不足不會造成高血糖。",
        "key": "長期生長激素分泌不足不會造成血糖升高。",
    },
    69: {
        "topic": "SGLT / secondary active transport / insulin independent",
        "analysis": "SGLT 使用鈉離子電化學梯度進行次級主動運輸，主要在腸道與腎小管吸收葡萄糖。胰島素主要調控 GLUT4，不直接調控 SGLT。",
        "options": {
            "A": "SGLT 是 Na+-glucose cotransport，屬次級主動運輸，不是促進性擴散。",
            "B": "肝臟與脂肪組織主要使用 GLUT 系列；SGLT 重要分布在腸道與腎近端小管。",
            "C": "胰島素主要調控 GLUT4 轉位，通常不直接調控 SGLT 運送葡萄糖，敘述最適當。",
            "D": "SGLT2 抑制劑增加尿糖排出，通常降低血糖，不會導致血糖升高。",
        },
        "core": "SGLT 是鈉依賴次級主動運輸；GLUT4 才是胰島素調控重點。",
        "key": "胰島素通常不直接調控 SGLT 的葡萄糖運送。",
    },
    70: {
        "topic": "Tyrosine-derived hormones / melatonin exclusion",
        "analysis": "酪胺酸衍生荷爾蒙包括 catecholamines 與 thyroid hormones，與壓力反應、新陳代謝、生長發育高度相關。生理時鐘主要與松果體 melatonin 相關，而 melatonin 由 tryptophan 衍生。",
        "options": {
            "A": "腎上腺素與正腎上腺素來自酪胺酸，和壓力反應密切相關。",
            "B": "生理時鐘主要由褪黑激素調節，而褪黑激素由色胺酸衍生，與酪胺酸衍生荷爾蒙關聯最小。",
            "C": "甲狀腺素來自酪胺酸碘化，深度調控新陳代謝。",
            "D": "甲狀腺素對生長與神經發育重要，因此與酪胺酸衍生荷爾蒙有關。",
        },
        "core": "Tyrosine-derived hormones 包含 catecholamines 和 thyroid hormones；melatonin 是 tryptophan-derived。",
        "key": "生理時鐘與褪黑激素較相關，和酪胺酸衍生荷爾蒙關聯最小。",
    },
    71: {
        "topic": "Aldosterone / zona glomerulosa",
        "analysis": "腎上腺皮質三層：絲球帶分泌 mineralocorticoids 如 aldosterone，束狀帶分泌 glucocorticoids，網狀帶分泌 androgens。",
        "options": {
            "A": "絲球帶分泌醛固酮，是正確答案。",
            "B": "束狀帶主要分泌 cortisol，不是 aldosterone。",
            "C": "網狀帶主要分泌 androgen，不是 aldosterone。",
            "D": "腎上腺髓質分泌 catecholamines，不是 aldosterone。",
        },
        "core": "GFR 記憶：glomerulosa-salt、fasciculata-sugar、reticularis-sex。",
        "key": "醛固酮主要由腎上腺皮質絲球帶分泌。",
    },
    72: {
        "topic": "Granulosa cells / estrogen / bone resorption",
        "analysis": "顆粒細胞 aromatase 活性可把 theca cell 來的 androgen 轉為 estrogen。若顆粒細胞類固醇生成低落，雌激素下降，會使骨吸收增加，也會減少子宮內膜增生並使 FSH 失去負回饋而上升。",
        "options": {
            "A": "雌激素下降會降低而非增進子宮內膜增生。",
            "B": "雌激素不足會增加破骨細胞相關骨吸收，是最可能結果。",
            "C": "雌激素與 inhibin 下降會減少負回饋，FSH 通常上升而非降低。",
            "D": "卵巢類固醇低落時 LH 不一定降低，常因負回饋減少而上升或失衡。",
        },
        "core": "Granulosa cells produce estrogen via aromatase；estrogen protects bone and supports endometrial proliferation。",
        "key": "顆粒細胞類固醇生成低落會使雌激素下降，導致骨吸收增加。",
    },
    73: {
        "topic": "Sex differentiation / MIS / Müllerian ducts",
        "analysis": "胚胎性別分化中，Sertoli cells 分泌 Müllerian-inhibiting substance，使副中腎管退化；Leydig cells 產生 testosterone 促進男性內外生殖器分化。",
        "options": {
            "A": "MIS 直接參與胚胎性別分化，使 Müllerian ducts 退化，是最相關選項。",
            "B": "FSH 調控性腺功能，但不是胚胎管道性別分化的主要決定因子。",
            "C": "Androgen-binding protein 參與睪丸內維持高 androgen 環境，較偏生精功能，不是最核心分化訊號。",
            "D": "Inhibin 主要負回饋抑制 FSH，不是胚胎性別分化主要訊號。",
        },
        "core": "男性分化兩大訊號：MIS 退化 Müllerian ducts；testosterone/DHT 促進 Wolffian ducts 與外生殖器男性化。",
        "key": "Müllerian-inhibiting substance 與胚胎性別分化最相關。",
    },
    74: {
        "topic": "Fetal hemoglobin / oxygen affinity",
        "analysis": "胎兒 HbF 含 gamma chains，和 2,3-BPG 結合較弱，因此對氧氣親和力高於母體 HbA，有利胎盤氧氣由母體轉移給胎兒。",
        "options": {
            "A": "胎兒心跳較快不是 Hb 對氧親和力較高的分子原因。",
            "B": "胎兒使用 HbF，母體主要使用 HbA，兩者結構差異造成胎兒氧親和力較高。",
            "C": "體內含氧量不同不是造成 Hb 親和力差異的根本原因。",
            "D": "胎兒產生較多 Hb 可影響氧含量，但不是 Hb 對氧結合力較強的原因。",
        },
        "core": "HbF binds 2,3-BPG poorly, so O2 affinity is higher than HbA。",
        "key": "胎兒與母體使用不同血紅蛋白，HbF 對氧親和力較高。",
    },
    75: {
        "topic": "Uncompetitive inhibitor / Vmax and Km decrease",
        "analysis": "非競爭性抑制劑 uncompetitive inhibitor 只結合 ES complex，使有效酵素-受質複合體被移除，因此 Vmax 下降，表觀 Km 也下降。",
        "options": {
            "A": "Uncompetitive inhibition 會使 Vmax 與 Km 同時下降，符合本題。",
            "B": "Vmax 不變較不像 uncompetitive；competitive inhibition 才常見 Vmax 不變、Km 上升。",
            "C": "Vmax 下降但 Km 上升不是 uncompetitive 的典型結果。",
            "D": "Vmax 不變、Km 上升是 competitive inhibition 的典型變化。",
        },
        "core": "Uncompetitive inhibitor lowers both Vmax and Km；competitive raises Km only；pure noncompetitive lowers Vmax only。",
        "key": "非競爭性抑制劑會使 Vmax 下降、Km 下降。",
    },
    76: {
        "topic": "Steady state / ES complex",
        "analysis": "Michaelis-Menten 的 steady state assumption 指反應初期後，酵素-受質複合體 ES 的形成速率約等於分解速率，使 ES 濃度近似維持穩定。",
        "options": {
            "A": "穩態不是活化能為零；酵素降低活化能但不讓其成為零。",
            "B": "穩態是一個速率假設，不是泛指所有酵素催化分子機制。",
            "C": "ES 複合體形成與分解速率相等，讓 ES 濃度近似不變，正是 steady state。",
            "D": "最大速率是 Vmax，需在受質飽和時達成，不等於穩態定義。",
        },
        "core": "Steady state assumption: d[ES]/dt ≈ 0，也就是 ES formation rate equals breakdown rate。",
        "key": "酵素與受質複合體形成和分解速率相等，是酵素動力學穩態的意義。",
    },
    77: {
        "topic": "One-carbon transfer / biotin / lysine",
        "analysis": "題目問含碳原子團轉移反應何者錯誤。Biotin 是羧化反應輔因子，通常以共價鍵接在酵素 lysine 殘基上，而不是 cysteine；pyruvate carboxylase 反應本身則是 biotin 參與的正確例子。",
        "options": {
            "A": "Tetrahydrofolate 可攜帶多種氧化態的一碳單位，敘述正確。",
            "B": "S-adenosylmethionine 由 methionine 與 ATP 形成，是重要 methyl donor，敘述正確。",
            "C": "Biotin 不是與 cysteine 結合，而是常接在 lysine 殘基上；題目問錯誤，故選此項。",
            "D": "TPP 參與 pyruvate dehydrogenase 將 pyruvate 轉為 acetyl-CoA，敘述正確。",
        },
        "core": "Biotin 是 carboxylation 輔因子，連在 enzyme lysine residue；THF 與 SAM 是常見一碳與甲基轉移工具。",
        "key": "Biotin 通常接在酵素 lysine 殘基上，不是 cysteine。",
    },
    78: {
        "topic": "Amino group transport / glutamine and alanine",
        "analysis": "肌肉、肝臟與腎臟間運送胺基主要靠 alanine 與 glutamine。Alanine 連結肌肉與肝臟的 glucose-alanine cycle；glutamine 是安全攜帶氮到肝腎的重要形式。",
        "options": {
            "A": "Phenylalanine 與 aspartate 不是肌肉、肝、腎間主要氮運送組合。",
            "B": "Serine 與 valine 可參與代謝，但不是主要胺基攜帶者組合。",
            "C": "Glutamine 與 alanine 是組織間運送氮的主要胺基酸，符合本題。",
            "D": "Glutamate 在細胞內轉胺很重要，但血中跨器官安全運氮主要是 glutamine 與 alanine。",
        },
        "core": "Nitrogen transport between tissues: alanine and glutamine。",
        "key": "肌肉、肝臟與腎臟間胺基運送主要靠 glutamine 與 alanine。",
    },
    79: {
        "topic": "Azaserine / glutamine analog / purine synthesis",
        "analysis": "Azaserine 是 glutamine analog，會抑制需要 glutamine 作為胺基供應者的反應，因此可抑制嘌呤核苷酸合成。",
        "options": {
            "A": "N10-formyl-THF 提供嘌呤環一碳單位，但 azaserine 主要不是抑制其合成。",
            "B": "PRPP 合成受 PRPP synthetase 調控，azaserine 主要不是抑制 PRPP 生成。",
            "C": "Ribose 5-phosphate 來自 pentose phosphate pathway，並非 azaserine 的主要作用點。",
            "D": "Azaserine 抑制 glutamine-dependent amidotransferase 反應，使 glutamine 不能作為嘌呤合成原料，正確。",
        },
        "core": "Azaserine 抑制 glutamine-dependent steps in purine synthesis。",
        "key": "Azaserine 主要抑制 glutamine 作為嘌呤核苷酸合成原料。",
    },
    80: {
        "topic": "E. coli DNA polymerase I / no 3-to-5 polymerase",
        "analysis": "DNA polymerase I 具有 5'→3' polymerase、3'→5' exonuclease proofreading、以及 5'→3' exonuclease 去除 RNA primer 的活性；聚合方向不會是 3'→5'。",
        "options": {
            "A": "DNA polymerase I 有 5'→3' DNA 聚合活性，可延長新股 DNA。",
            "B": "DNA 聚合酶不能以 3'→5' 方向聚合 DNA；題目問沒有的活性，故選此項。",
            "C": "DNA polymerase I 有 5'→3' exonuclease 活性，可移除 RNA primer。",
            "D": "DNA polymerase I 有 3'→5' exonuclease 活性，用於 proofreading。",
        },
        "core": "DNA polymerase synthesizes 5' to 3'；Pol I 另有 3'→5' proofreading 和 5'→3' exonuclease。",
        "key": "大腸桿菌 DNA polymerase I 沒有 3'→5' DNA 聚合活性。",
    },
    81: {
        "topic": "PCR components / ATP not required",
        "analysis": "PCR 需要模板 DNA、primers、耐熱 DNA polymerase、dNTPs、Mg2+ 與緩衝液。DNA 合成能量來自 dNTP 本身的三磷酸鍵，不需額外 ATP。",
        "options": {
            "A": "PCR 需要 DNA polymerase 進行延伸，通常使用耐熱聚合酶。",
            "B": "PCR 通常不需加入 ATP，因為聚合反應使用 dNTP 作為原料與能量來源。",
            "C": "dNTPs 是新 DNA 鏈合成的四種原料，必須加入。",
            "D": "Mg2+ 是 DNA polymerase 活性所需輔因子，通常必須加入。",
        },
        "core": "PCR needs template, primers, thermostable polymerase, dNTPs, Mg2+；not ATP。",
        "key": "PCR 通常不需要額外加入 ATP。",
    },
    82: {
        "topic": "HNPCC / Lynch syndrome / mismatch repair",
        "analysis": "遺傳性非息肉症大腸直腸癌又稱 Lynch syndrome，典型由 DNA mismatch repair genes 如 MLH1、MSH2、MSH6、PMS2 缺陷造成，導致 microsatellite instability。",
        "options": {
            "A": "核苷酸切除修復缺陷典型與 xeroderma pigmentosum 相關，不是 HNPCC 主因。",
            "B": "鹼基切除修復處理小型鹼基損傷，非 HNPCC 典型核心。",
            "C": "重組修復缺陷可見於 BRCA 相關腫瘤風險，不是 HNPCC 主要機轉。",
            "D": "Mismatch repair 缺陷造成 Lynch syndrome/HNPCC，是本題正確答案。",
        },
        "core": "HNPCC/Lynch syndrome = mismatch repair defect = microsatellite instability。",
        "key": "HNPCC 主要是 DNA 錯誤配對修復缺陷。",
    },
    83: {
        "topic": "Initiation codon / methionine / N-formylmethionine",
        "analysis": "AUG 是起始密碼子。真核蛋白質合成起始胺基酸是 methionine；細菌起始使用 N-formylmethionine。",
        "options": {
            "A": "細菌起始胺基酸不是一般 methionine，而是 N-formylmethionine。",
            "B": "真核起始不是 N-formylmethionine，而是 methionine。",
            "C": "真核為 methionine，細菌為 N-formylmethionine，敘述正確。",
            "D": "此選項把真核與細菌起始胺基酸顛倒了。",
        },
        "core": "Start codon AUG：eukaryote starts with Met；bacteria starts with fMet。",
        "key": "真核起始胺基酸為 methionine，細菌為 N-formylmethionine。",
    },
    84: {
        "topic": "Histones / basic amino acids / DNA",
        "analysis": "組織蛋白富含 lysine、arginine 等鹼性胺基酸，帶正電，可和帶負電的 DNA 磷酸骨架結合，形成 nucleosome。",
        "options": {
            "A": "Histones 不是富含酸性胺基酸；酸性會較不利於結合 DNA 負電骨架。",
            "B": "Histones 主要包裝 DNA，不是以 RNA 為主要結合對象。",
            "C": "Histones 富含鹼性胺基酸並與 DNA 結合，敘述正確。",
            "D": "雖富含鹼性胺基酸，但主要功能是與 DNA 結合，不是 RNA。",
        },
        "core": "Histones are basic proteins rich in lysine and arginine that bind negatively charged DNA。",
        "key": "組織蛋白富含鹼性胺基酸並與 DNA 結合。",
    },
    85: {
        "topic": "mRNA 5' cap / 7-methylguanosine / 5'-5' triphosphate",
        "analysis": "真核 mRNA 5' cap 是 7-methylguanosine 透過不尋常的 5'-to-5' triphosphate linkage 接到 mRNA 5' 端，有助穩定、輸出與轉譯起始。",
        "options": {
            "A": "鍵結不是 5'-to-3' diphosphate，而是 5'-to-5' triphosphate。",
            "B": "7-methylguanosine 以 5'-to-5' triphosphate linkage 接到 mRNA，是正確敘述。",
            "C": "5' cap 的鹼基是 7-methylguanosine，不是 N6-methyladenosine。",
            "D": "O6-methylguanosine 與 5'-to-3' diphosphate linkage 都不是標準 mRNA cap。",
        },
        "core": "Eukaryotic 5' cap = 7-methylguanosine linked 5' to 5' via triphosphate bridge。",
        "key": "真核 mRNA 5' cap 是 7-methylguanosine 以 5'-to-5' triphosphate linkage 連接。",
    },
    86: {
        "topic": "trp operon attenuation / tryptophan fine tuning",
        "analysis": "Attenuation 是細菌 trp operon 依細胞內 tryptophan 多寡，透過 leader peptide translation 速度影響 mRNA secondary structure，進而微調轉錄是否提前終止。",
        "options": {
            "A": "色胺酸存在時通常抑制 trp operon 表現，不是增進轉錄表現。",
            "B": "Attenuation 可因應細胞內微量 tryptophan 改變，調節 operon 轉錄表現，最符合定義。",
            "C": "Attenuation 的直接效果是影響轉錄提前終止，不是直接抑制 trp mRNA 轉譯。",
            "D": "它作用於 leader/attenuator 區域，不是在 operon 每個基因各自 promoter 上。",
        },
        "core": "trp attenuation couples translation of leader peptide to transcription termination, fine-tuning low tryptophan changes。",
        "key": "trp operon attenuation 可因應細胞中 tryptophan 微量變化調節轉錄。",
    },
    87: {
        "topic": "Succinate dehydrogenase / Complex II / TCA and ETC",
        "analysis": "Succinate dehydrogenase 位於粒線體內膜，既是 TCA cycle 將 succinate 氧化成 fumarate 的酵素，也是電子傳遞鏈 complex II。",
        "options": {
            "A": "Succinate dehydrogenase 同時屬於 TCA cycle 與 ETC complex II，位於內膜，正確。",
            "B": "Succinyl-CoA synthetase 是 TCA 中 substrate-level phosphorylation 酵素，不是 ETC 複合體。",
            "C": "Malate dehydrogenase 參與 TCA，但不是電子傳遞鏈複合體。",
            "D": "Isocitrate dehydrogenase 參與 TCA 產生 NADH/CO2，但不位於 ETC 複合體中。",
        },
        "core": "Complex II = succinate dehydrogenase，是 TCA 與 ETC 的交會點。",
        "key": "Succinate dehydrogenase 同時參與 TCA cycle 與電子傳遞鏈 complex II。",
    },
    88: {
        "topic": "Gluconeogenesis / ATP and GTP / PEPCK",
        "analysis": "葡萄糖新生不是糖解完全逆轉，需繞過不可逆步驟。由 pyruvate 到 glucose 需要 pyruvate carboxylase、PEPCK 等，消耗 ATP 與 GTP，且反應分布在粒線體、細胞質與內質網。",
        "options": {
            "A": "葡萄糖新生部分步驟在粒線體與內質網，不是全部在細胞質。",
            "B": "Pyruvate 轉成 glucose 需消耗 ATP 與 GTP，敘述正確。",
            "C": "糖解不可逆步驟需由不同酵素繞過，不是完全相同酵素反向。",
            "D": "PEPCK 是將 oxaloacetate 轉成 phosphoenolpyruvate，不是反向。",
        },
        "core": "Gluconeogenesis costs energy: 4 ATP + 2 GTP + 2 NADH per glucose from pyruvate。",
        "key": "葡萄糖新生由 pyruvate 形成 glucose 需要消耗 ATP 與 GTP。",
    },
    89: {
        "topic": "Glycolysis regulation / enolase",
        "analysis": "糖解作用主要調控步驟是 hexokinase/glucokinase、PFK-1、pyruvate kinase。Enolase 雖參與糖解，但不是主要速率調控酵素。",
        "options": {
            "A": "己糖激酶催化葡萄糖磷酸化，是糖解調控點之一。",
            "B": "磷酸果糖激酶 PFK-1 是糖解最重要限速酵素。",
            "C": "烯醇化酶催化 2-phosphoglycerate 到 PEP，但不是主要速率調控者；題目問並非主要，故選此項。",
            "D": "丙酮酸激酶催化最後不可逆步驟，是糖解調控點之一。",
        },
        "core": "Glycolysis key regulatory enzymes: hexokinase/glucokinase, PFK-1, pyruvate kinase。",
        "key": "Enolase 不是糖解作用速率的主要調控酵素。",
    },
    90: {
        "topic": "Acetyl-CoA carboxylase / citrate / insulin / AMPK",
        "analysis": "Acetyl-CoA carboxylase 受檸檬酸與胰島素活化，受 AMPK 磷酸化抑制。Coenzyme A 本身不是 ACC 活性的主要調控者。",
        "options": {
            "A": "胰島素促進去磷酸化並活化 ACC，有利脂肪酸合成。",
            "B": "Coenzyme A 不是 ACC 的主要活性調控因子；題目問最不受調控，故選此項。",
            "C": "檸檬酸是能量充足訊號，可促進 ACC 聚合與活化。",
            "D": "AMPK 在能量不足時磷酸化並抑制 ACC，減少脂肪酸合成。",
        },
        "core": "ACC activated by citrate/insulin, inhibited by AMPK and palmitoyl-CoA。",
        "key": "輔酶 A 不是 acetyl-CoA carboxylase 的主要調控因子。",
    },
    91: {
        "topic": "Vitamin K / isoprenoid / quinone",
        "analysis": "維生素 K 是脂溶性萘醌類分子，具有 isoprenoid side chain，參與凝血因子 glutamate 殘基的 gamma-carboxylation。",
        "options": {
            "A": "7-dehydrocholesterol 是維生素 D3 前驅物，不是維生素 K 來源。",
            "B": "Arachidonate 是前列腺素、白三烯等 eicosanoids 前驅物，不是維生素 K。",
            "C": "維生素 K 具有 isoprenoid 側鏈，屬 isoprenoid/quinone 類衍生物，正確。",
            "D": "Pregnenolone 是類固醇荷爾蒙前驅物，不是維生素 K。",
        },
        "core": "Vitamin K is a fat-soluble quinone with isoprenoid side chain, required for gamma-carboxylation of clotting factors。",
        "key": "維生素 K 是 isoprenoid 類衍生物。",
    },
    92: {
        "topic": "Peripheral membrane proteins / no transmembrane segment",
        "analysis": "周邊膜蛋白以離子鍵、氫鍵或與其他膜蛋白互動附著在膜表面，可被改變 pH 或離子強度分離；具有穿膜結構的是 integral membrane protein。",
        "options": {
            "A": "改變 pH 或離子強度可破壞非共價作用，使周邊膜蛋白脫離，敘述正確。",
            "B": "周邊膜蛋白不具有穿透脂雙層的跨膜區；題目問錯誤，故選此項。",
            "C": "周邊膜蛋白可透過離子鍵與膜脂頭部或膜蛋白結合，敘述正確。",
            "D": "氫鍵也可穩定周邊膜蛋白與膜表面或其他蛋白互動，敘述正確。",
        },
        "core": "Peripheral membrane proteins attach noncovalently to membrane surface; integral proteins span or embed in lipid bilayer。",
        "key": "膜周邊蛋白沒有穿透膜結構。",
    },
    93: {
        "topic": "Tryptophan / serotonin / dopamine exclusion",
        "analysis": "色胺酸是必需胺基酸，也是血清素與褪黑激素前驅物。多巴胺來自酪胺酸，不是色胺酸代謝產物。",
        "options": {
            "A": "色胺酸是人體必需胺基酸，必須由飲食攝取。",
            "B": "色胺酸羥化酶是血清素合成限速酵素，功能不足可能和情緒障礙相關，敘述可接受。",
            "C": "色胺酸是 serotonin 合成前驅物，敘述正確。",
            "D": "Dopamine 由 tyrosine 經 DOPA 形成，不是 tryptophan 代謝形成；題目問錯誤，故選此項。",
        },
        "core": "Tryptophan -> serotonin/melatonin；tyrosine -> dopamine/norepinephrine/epinephrine。",
        "key": "色胺酸不會代謝形成多巴胺，多巴胺來自酪胺酸。",
    },
    94: {
        "topic": "Asparagine / glucogenic amino acid / aspartate",
        "analysis": "Asparagine 是非必需胺基酸，可由 asparaginase 分解為 aspartate 與 ammonia。Aspartate/asparagine 為生糖性胺基酸，不是生酮性胺基酸。",
        "options": {
            "A": "Asparagine 是非必需胺基酸，人體可合成，敘述正確。",
            "B": "Asparagine 可經 asparaginase 轉為 aspartate，敘述正確。",
            "C": "Asparagine/aspartate 進入 oxaloacetate 代謝，屬生糖性，不是生酮性；題目問錯誤，故選此項。",
            "D": "Asparaginase 可分解血中 asparagine，臨床也用於某些白血病治療，敘述正確。",
        },
        "core": "Asparagine is glucogenic via aspartate to oxaloacetate, not ketogenic。",
        "key": "天門冬醯胺是生糖性胺基酸，不是生酮性胺基酸。",
    },
    95: {
        "topic": "ETC Complex IV / cytochrome c oxidase",
        "analysis": "電子傳遞鏈中，Complex IV 又稱 cytochrome c oxidase，將電子傳給氧氣並把氧還原成水。",
        "options": {
            "A": "Complex I 接收 NADH 電子並傳給 ubiquinone，不直接將氧還原為水。",
            "B": "Complex II 是 succinate dehydrogenase，把 FADH2 電子送入 ubiquinone，不還原氧。",
            "C": "Complex III 將電子由 ubiquinol 傳給 cytochrome c，不是氧的還原位點。",
            "D": "Complex IV 接收 cytochrome c 電子，將 O2 還原成 H2O，是正確答案。",
        },
        "core": "Complex IV/cytochrome c oxidase is the terminal ETC enzyme that reduces oxygen to water。",
        "key": "Complex IV 可將氧氣還原成水。",
    },
    96: {
        "topic": "CDK regulation / cyclin / phosphorylation / ubiquitin",
        "analysis": "CDK 催化活性直接受 cyclin 結合、活化或抑制性 phosphorylation，以及 kinase/phosphatase 調控。Ubiquitin 主要標記 cyclin 或其他蛋白降解，間接改變 CDK 活性，不是直接調控其催化活性。",
        "options": {
            "A": "Cyclin 與 CDK 結合是 CDK 活化的核心直接調控。",
            "B": "Kinase 可磷酸化 CDK，直接改變其活性。",
            "C": "Phosphatase 去除 CDK 上特定位點磷酸，也可直接調控活性。",
            "D": "Ubiquitin 主要透過蛋白降解調整 cyclin 量，屬間接調控，不直接調控 CDK 催化活性。",
        },
        "core": "CDK activity is directly controlled by cyclins and phosphorylation state; ubiquitin controls protein abundance indirectly。",
        "key": "Ubiquitin 不直接調控 CDK 催化活性，而是透過蛋白降解間接影響。",
    },
    97: {
        "topic": "GPCR / insulin receptor / RTK",
        "analysis": "Angiotensin、prostaglandin 與 epinephrine 常透過 GPCR 家族受體傳訊。Insulin receptor 是 receptor tyrosine kinase，不是 GPCR。",
        "options": {
            "A": "Angiotensin II 的 AT1 receptor 屬 GPCR，因此可直接透過 GPCR 訊號。",
            "B": "許多 prostaglandin receptors 屬 GPCR，會活化 cAMP 或 Ca2+ 相關路徑。",
            "C": "Epinephrine 的 alpha 與 beta adrenergic receptors 都是 GPCR。",
            "D": "Insulin receptor 是 receptor tyrosine kinase，通常不直接結合 GPCR 進行傳訊。",
        },
        "core": "Insulin uses RTK; catecholamines、angiotensin、prostaglandins 多用 GPCR。",
        "key": "Insulin receptor 是受體酪胺酸激酶，不是 GPCR。",
    },
    98: {
        "topic": "GAP / Ras / GTP hydrolysis",
        "analysis": "GTPase activating proteins 會結合小型 GTPase 如 Ras，促進 GTP 水解成 GDP，使 Ras 從活化狀態關閉。",
        "options": {
            "A": "cGMP 是第二訊息分子，不是 GAP 主要直接調節的 GTPase 蛋白。",
            "B": "Ras 是小型 GTPase，GAP 直接促進其 GTP 水解，故為正確答案。",
            "C": "DAG 是膜脂衍生第二訊息分子，活化 PKC，不是 GAP 的典型直接結合目標。",
            "D": "Adenylyl cyclase 是生成 cAMP 的酵素，不是 Ras GAP 直接調節的主要對象。",
        },
        "core": "GAP turns Ras off by accelerating GTP hydrolysis; GEF turns Ras on by promoting GDP-GTP exchange。",
        "key": "GAPs 直接作用於 Ras 等小型 GTPase，促進 GTP 水解。",
    },
    99: {
        "topic": "RNA quantification / RIP / RT-qPCR",
        "analysis": "題目問最不可能用來測定特定 RNA 的數量。RT-qPCR、RNA-seq 與 microarray 都可用於 RNA 表現量測定；RNA immunoprecipitation 主要用來找 RNA-binding protein 結合哪些 RNA，不是單純定量某特定 RNA 的首選方法。",
        "options": {
            "A": "RNA immunoprecipitation 主要研究 RNA 與蛋白質交互作用，最不適合單純測定細胞中特定 RNA 數量。",
            "B": "RNA deep sequencing 可用 reads 數估計 RNA 表現量，能做定量分析。",
            "C": "RNA microarray 可用探針訊號比較 RNA 表現量。",
            "D": "RT-real time PCR 是測定特定 RNA 數量最常用且靈敏的方法之一。",
        },
        "core": "RNA abundance: RT-qPCR, RNA-seq, microarray；RIP focuses on RNA-protein association。",
        "key": "RNA immunoprecipitation 主要測 RNA-蛋白結合，不是測定特定 RNA 數量的首選。",
    },
    100: {
        "topic": "Restriction enzymes / sequence-specific DNA endonuclease",
        "analysis": "限制酶是細菌防禦系統的一部分，能辨識特定 DNA 序列，並在該序列或附近切割雙股 DNA，因此屬序列特異性 DNA 內切酶。",
        "options": {
            "A": "限制酶不是細胞膜通道，也不是靠阻止病毒進入細胞發揮作用。",
            "B": "限制酶切割 DNA，不是特異性 ribonuclease，也不是用來降解 mRNA。",
            "C": "限制酶是 sequence-specific DNA endonuclease，會切割特定辨識序列的 DNA，敘述正確。",
            "D": "催化胺基酸接到 tRNA 的是 aminoacyl-tRNA synthetase，不是 restriction enzyme。",
        },
        "core": "Restriction enzymes are sequence-specific DNA endonucleases used by bacteria and molecular cloning。",
        "key": "限制酶是具序列特異性的 DNA 內切酶。",
    },
}


def build_explanation(item, source_q):
    options_text = source_q["options"]
    correct = source_q["correct_answer"]
    is_negative = any(cue in source_q["question_text"] for cue in NEGATIVE_CUES)
    lines = [
        "【題幹解析】",
        item["analysis"],
        "",
        "【選項詳解】",
    ]
    for opt in ("A", "B", "C", "D"):
        if is_negative:
            label = "本題答案" if opt == correct else "非答案"
        else:
            label = "正確" if opt == correct else "錯誤"
        lines.append(f"- {opt}. {options_text[opt]}：{label}。{item['options'][opt]}")
    lines.extend(["", "【核心考點】", item["core"]])
    return "\n".join(lines)


def main():
    exam = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    questions = {q["question_number"]: q for q in exam["questions"]}
    missing = sorted(set(questions) - set(DATA))
    extra = sorted(set(DATA) - set(questions))
    if missing or extra:
        raise SystemExit(f"question coverage mismatch: missing={missing}, extra={extra}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for start in range(1, 101, 10):
        end = start + 9
        updates = []
        for qnum in range(start, end + 1):
            q = questions[qnum]
            item = DATA[qnum]
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": qnum,
                    "explanation": build_explanation(item, q),
                    "key_point": item["key"],
                    "flashcard_front": item["topic"],
                    "flashcard_back": item["key"],
                    "flashcard_summary": f"{item['topic']} -> {item['key']}",
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
        print(out_path)


if __name__ == "__main__":
    main()
