import json
from datetime import datetime, timezone, timedelta
from pathlib import Path


SOURCE_FILE = "public/data/exams/110-2/medicine-1.json"
DATASET_ID = "110-2_medicine-1"
OUT_DIR = Path("scratch/rewrite_updates/110-2_medicine-1")
MODEL = "codex-high-quality-rewrite"
GENERATED_AT = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")


SPECS = {
    1: {
        "analysis": "本題是否定式解剖題，要找「不是」內頸動脈（internal carotid artery, ICA）直接分支的血管。ICA 在顱內可給出眼動脈、後交通動脈、前脈絡叢動脈，終末分支為前大腦動脈與中大腦動脈；前交通動脈則連接兩側前大腦動脈。",
        "reasons": {
            "A": "眼動脈是內頸動脈進入顱腔後的重要分支，會經視神經管進入眼眶，因此不是本題要找的例外。",
            "B": "中大腦動脈是內頸動脈的終末分支之一，供應大腦半球外側面大部分區域，因此屬於 ICA 分支系統。",
            "C": "前脈絡叢動脈通常由內頸動脈發出，供應內囊、視徑與脈絡叢等構造，因此是 ICA 分支。",
            "D": "前交通動脈連接左右前大腦動脈，屬 Willis 環的交通支，不是內頸動脈直接發出的分支，故為答案。",
        },
        "core": "內頸動脈的高頻分支包括眼動脈、後交通動脈、前脈絡叢動脈，以及 ACA/MCA 終末分支；前交通動脈是兩側 ACA 之間的連接。",
    },
    2: {
        "analysis": "右側胸段半側脊髓損傷符合 Brown-Sequard syndrome。皮質脊髓徑與後柱在脊髓內同側傳導，痛溫覺的脊髓丘腦徑則在進入脊髓後不久交叉，因此會出現同側下肢無力與本體/震動覺受損、對側痛溫覺受損。",
        "reasons": {
            "A": "右側皮質脊髓徑受損會造成右側、病灶以下的上運動神經元型無力，胸段病灶主要影響右下肢，故正確。",
            "B": "震動覺走後柱，胸段右半切會影響右側下肢震動覺，不是左側。",
            "C": "痛覺纖維進入脊髓後交叉到對側上行，右側脊髓丘腦徑受損較會造成左側病灶以下痛溫覺異常，不是右側。",
            "D": "胸段病灶位於支配上肢的頸膨大以下，不會造成左側上肢無力。",
        },
        "core": "Brown-Sequard syndrome：同側運動與後柱感覺受損，對側痛溫覺受損；胸段病灶主要表現在下肢。",
    },
    3: {
        "analysis": "腭扁桃腺血流主要來自外頸動脈系統的咽部、舌部與顎部相關分支；題目要找不供應腭扁桃腺者。上甲狀腺動脈主要往甲狀腺與喉部，不是腭扁桃腺供血來源。",
        "reasons": {
            "A": "面動脈可發出扁桃腺支及升腭動脈，常是腭扁桃腺的重要供血來源。",
            "B": "舌動脈的背舌支可供應舌根與扁桃腺附近區域，因此可參與腭扁桃腺供血。",
            "C": "升咽動脈供應咽壁與扁桃腺區域，是腭扁桃腺血流來源之一。",
            "D": "上甲狀腺動脈主要供應甲狀腺、喉部與鄰近肌肉，通常不供應腭扁桃腺，故為答案。",
        },
        "core": "腭扁桃腺供血記面動脈扁桃腺支/升腭、舌動脈背舌支、升咽動脈；上甲狀腺動脈偏向甲狀腺與喉部。",
    },
    4: {
        "analysis": "大岩神經（greater petrosal nerve）來自面神經膝狀神經節，沿顳骨岩部前面的大岩神經溝前行。本題考顱底骨性溝的位置。",
        "reasons": {
            "A": "蝶骨有卵圓孔、圓孔、棘孔與翼突等重要構造，但大岩神經溝不位於蝶骨。",
            "B": "頂骨主要形成顱蓋上外側部，與大岩神經在顱底的走行無關。",
            "C": "大岩神經溝位於顳骨岩部前面，這是本題的定位重點，故正確。",
            "D": "枕骨包含枕骨大孔、舌下神經管等構造，不是大岩神經溝的位置。",
        },
        "core": "大岩神經溝位於顳骨岩部前面；大岩神經是面神經副交感纖維通往翼腭神經節的重要路徑。",
    },
    5: {
        "analysis": "本題比較顱底孔洞通過的神經。盲孔多為導血管通道，通常沒有神經通過；其他選項均有明確神經穿行。",
        "reasons": {
            "A": "頸靜脈孔有舌咽、迷走、副神經（CN IX, X, XI）通過，因此不是答案。",
            "B": "圓孔有上頷神經（CN V2）通過，是典型顱底孔洞配對。",
            "C": "篩後孔可有篩後神經與血管通過，因此仍有神經成分。",
            "D": "盲孔通常只與導血管相關，沒有固定神經通過，故為答案。",
        },
        "core": "顱底孔洞要配對神經：頸靜脈孔 IX/X/XI，圓孔 V2，篩後孔篩後神經；盲孔通常無神經。",
    },
    6: {
        "analysis": "題目考腹主動脈分支起點高低。腸繫膜上動脈與腎上腺中動脈多在 L1 附近，腎動脈約 L1-L2，睪丸/卵巢動脈較低，約 L2 自腹主動脈發出。",
        "reasons": {
            "A": "腸繫膜上動脈起點約 L1，下於腹腔幹但仍高於性腺動脈。",
            "B": "腎上腺中動脈多在 L1 附近自腹主動脈側面發出，不是最低。",
            "C": "腎動脈約在 L1-L2 之間，位置通常仍高於睪丸動脈。",
            "D": "睪丸動脈約在 L2 高度由腹主動脈前外側發出，在四者中起點最低，故正確。",
        },
        "core": "腹主動脈分支由高到低可抓：SMA/腎上腺中動脈、腎動脈、性腺動脈；性腺動脈通常最低。",
    },
    7: {
        "analysis": "直腸上段血流來自直腸上動脈，直腸上動脈是腸繫膜下動脈（inferior mesenteric artery, IMA）的終末分支。直腸中、下動脈則較偏髂內動脈系統。",
        "reasons": {
            "A": "腸繫膜上動脈供應中腸衍生腸段，至橫結腸近端/脾曲前，不是直腸上段主來源。",
            "B": "腸繫膜下動脈終末分支為直腸上動脈，供應直腸上段，故為答案。",
            "C": "腰動脈供應後腹壁與脊髓相關分支，不是直腸上段主要血流。",
            "D": "髂內動脈系統供應直腸中、下段較重要，但直腸上段主要來自 IMA。",
        },
        "core": "直腸血供分層：上直腸動脈來自 IMA，中/下直腸動脈多來自髂內動脈系統。",
    },
    8: {
        "analysis": "L1 屬 T1-L2 交感外流節段，因此可同時具有白交通支與灰交通支。白交通支帶有交感節前有髓纖維進入交感鏈；灰交通支帶有交感節後無髓纖維回到脊神經。",
        "reasons": {
            "A": "L1 確實有白交通支且含節前纖維，但不是只有白交通支，還有灰交通支。",
            "B": "白交通支的纖維是節前有髓纖維，不是節後纖維。",
            "C": "白、灰交通支都存在的描述對，但白交通支不是節後纖維。",
            "D": "L1 同時有白與灰交通支，且分別含節前與節後交感纖維，故正確。",
        },
        "core": "白交通支只在 T1-L2，帶節前有髓交感纖維；灰交通支幾乎所有脊神經都有，帶節後無髓纖維。",
    },
    9: {
        "analysis": "男性尿道分為膀胱內部、前列腺部、膜部與海綿體部。海綿體尿道穿過陰莖尿道海綿體，長度遠長於其他三段。",
        "reasons": {
            "A": "膀胱內尿道部很短，只穿過膀胱壁，並非最長。",
            "B": "前列腺尿道約數公分，長於膜部但短於海綿體部。",
            "C": "膜性尿道短且狹窄，通過尿生殖膈區域，不是最長。",
            "D": "海綿體尿道沿陰莖海綿體前行，是男性尿道最長的部分，故正確。",
        },
        "core": "男性尿道最長是海綿體部；膜部短、窄且臨床上外傷重要。",
    },
    10: {
        "analysis": "膝關節包含股脛關節與股髕關節，關節面由股骨、脛骨與髕骨參與。腓骨雖在膝外側附近，形成上脛腓關節，但不屬膝關節關節面。",
        "reasons": {
            "A": "股骨遠端髁與脛骨平台形成股脛關節，是膝關節主要構成骨。",
            "B": "脛骨近端平台參與股脛關節，是膝關節構成骨。",
            "C": "腓骨頭與脛骨形成上脛腓關節，不進入膝關節腔，也不構成膝關節面，故為答案。",
            "D": "髕骨與股骨滑車面形成股髕關節，是膝關節的一部分。",
        },
        "core": "膝關節由股骨、脛骨、髕骨構成；腓骨靠近膝但屬上脛腓關節，不構成膝關節。",
    },
    11: {
        "analysis": "胸段脊髓的節段性髓動脈會隨脊神經根進入椎管，常來自肋間後動脈或腰動脈等後方節段性動脈。胸內動脈與肋間前動脈偏前胸壁供血。",
        "reasons": {
            "A": "椎動脈可供應頸髓與形成前/後脊髓動脈，但題目限定胸腔分支時不是主要來源。",
            "B": "胸內動脈沿胸骨旁下降，主要供應前胸壁與乳房等區域，不是胸段髓動脈典型來源。",
            "C": "肋間前動脈供應前外側胸壁，較不會形成進入脊髓的節段性髓動脈。",
            "D": "肋間後動脈會發出脊髓支，經椎間孔進入並可形成節段性髓動脈，故正確。",
        },
        "core": "胸段脊髓節段性髓動脈常來自肋間後動脈的脊髓支，走椎間孔進入椎管。",
    },
    12: {
        "analysis": "大腦白質纖維分為聯合纖維、連合纖維與投射纖維。聯合纖維連接同側大腦皮質區；胼胝體連接左右半球，屬連合纖維，不是聯合纖維。",
        "reasons": {
            "A": "鉤束連接同側額葉與顳葉，是聯合纖維。",
            "B": "弓狀束連接同側語言相關皮質區，是長聯合纖維。",
            "C": "扣帶束位於扣帶回內，連接同側邊緣系統相關區域，屬聯合纖維。",
            "D": "胼胝體連接左右大腦半球，是連合纖維，不是聯合纖維，故為答案。",
        },
        "core": "聯合纖維連同側；連合纖維連兩側，代表是胼胝體。",
    },
    13: {
        "analysis": "多數感覺訊息在到達大腦皮質前會經丘腦中繼；嗅覺是重要例外，初級嗅覺路徑可先投射至嗅皮質，不需先經丘腦。",
        "reasons": {
            "A": "視覺訊息經外側膝狀體（LGN）投射至初級視覺皮質，屬丘腦中繼。",
            "B": "嗅覺由嗅球與嗅束投射至初級嗅覺皮質，初級路徑不先經丘腦，故正確。",
            "C": "體感覺經 VPL/VPM 等丘腦核後投射至初級體感覺皮質。",
            "D": "聽覺經內側膝狀體（MGN）中繼後到初級聽覺皮質。",
        },
        "core": "嗅覺是感覺系統中「不先經丘腦」的經典例外；視覺、聽覺、體感覺都經丘腦。",
    },
    14: {
        "analysis": "痛覺調控牽涉脊髓背角膠狀質（lamina II）與下行抑制路徑如縫核脊髓徑；背柱內側蹄系主要傳精細觸覺、本體覺與震動覺，和痛覺調控較間接。脊髓小腦徑主要傳無意識本體覺與協調資訊，與痛覺調控關聯最少。",
        "reasons": {
            "A": "lamina II 是膠狀質，參與痛覺傳入調節與閘門控制，關聯高。",
            "B": "縫核脊髓徑屬下行疼痛調控系統，可釋放 serotonin 等抑制痛覺傳遞。",
            "C": "脊髓小腦徑主要與無意識本體覺及運動協調相關，和痛覺調控關聯最少，故為答案。",
            "D": "背柱內側蹄系不是主要痛覺路徑，但臨床上與感覺調節、觸覺互動仍比脊髓小腦徑更接近感覺傳導議題。",
        },
        "core": "痛覺調控看背角 lamina II 與下行抑制路徑；脊髓小腦徑主司本體覺/協調，最不像痛覺調控構造。",
    },
    15: {
        "analysis": "菱形窩是第四腦室底，位於橋腦與延腦背側，可見面神經丘、舌下神經三角、迷走神經三角等表面隆起。下橄欖體位於延腦腹外側表面，不在菱形窩內。",
        "reasons": {
            "A": "面神經丘位於橋腦背側的第四腦室底，屬菱形窩構造。",
            "B": "下橄欖體位於延腦腹外側，不在第四腦室底的菱形窩中，故為答案。",
            "C": "舌下神經三角在延腦背側、第四腦室底，是菱形窩構造。",
            "D": "迷走神經三角也在第四腦室底，屬菱形窩可見構造。",
        },
        "core": "菱形窩等於第四腦室底；下橄欖體在延腦腹外側，不在菱形窩。",
    },
    16: {
        "analysis": "動眼神經完全麻痺時，內直肌、上直肌、下直肌、下斜肌與提上瞼肌失去功能；滑車神經支配上斜肌、外旋神經支配外直肌仍保留，因此眼球被外直肌拉向外、上斜肌拉向下。",
        "reasons": {
            "A": "正上方需要上直肌與下斜肌等動眼神經肌肉參與，CN III 麻痺時無法形成。",
            "B": "內上方需要內直肌與上直肌/下斜肌，均受 CN III 影響，不符合。",
            "C": "外直肌（CN VI）仍可外展，上斜肌（CN IV）仍可使眼球向下內旋，合併呈外下方，故正確。",
            "D": "內下方需要內直肌功能，但內直肌由 CN III 支配，已麻痺。",
        },
        "core": "完全 CN III palsy 的眼位是 down and out，因 CN VI 外直肌與 CN IV 上斜肌相對保留。",
    },
    17: {
        "analysis": "氣管由環狀軟骨下緣開始，食道由咽在環狀軟骨後方延續而來，兩者上端約在 C6 高度。這是頸部解剖常考水平。",
        "reasons": {
            "A": "C2 過高，接近上咽部與上頸椎，不是氣管/食道起點。",
            "B": "C4 接近甲狀軟骨與喉部較高位置，仍高於食道、氣管起始。",
            "C": "C6 約為環狀軟骨下緣，氣管與食道在此高度開始，故正確。",
            "D": "T1 已到胸廓入口附近，低於氣管與食道的最上端。",
        },
        "core": "環狀軟骨、氣管起點、食道起點常抓 C6。",
    },
    18: {
        "analysis": "舌下神經支配幾乎所有舌內外肌，但腭舌肌是例外，由迷走神經經咽神經叢支配。題目要找不是 CN XII 支配者。",
        "reasons": {
            "A": "頦舌肌由舌下神經支配，負責伸舌，是 CN XII 測試重點。",
            "B": "舌骨舌肌由舌下神經支配，參與壓低舌頭。",
            "C": "莖突舌肌由舌下神經支配，參與後縮與抬舌。",
            "D": "腭舌肌由迷走神經支配，不是舌下神經支配，故為答案。",
        },
        "core": "舌肌支配的例外：腭舌肌由 CN X；其餘多由 CN XII。",
    },
    19: {
        "analysis": "心瓣膜聽診點不是瓣膜解剖位置，而是血流聲音傳導最清楚的位置。二尖瓣聽診點在左第 5 肋間鎖骨中線附近，也就是心尖部。",
        "reasons": {
            "A": "主動脈瓣聽診點是右第 2 肋間胸骨旁，不是左第 2 肋間。",
            "B": "肺動脈瓣聽診點是左第 2 肋間胸骨旁，不是右側。",
            "C": "三尖瓣常在左胸骨下緣第 4-5 肋間聽診，不是右側第四肋間。",
            "D": "二尖瓣在左第 5 肋間鎖骨中線心尖部聽診最清楚，故正確。",
        },
        "core": "聽診點：Aortic 右 2、Pulmonic 左 2、Tricuspid 左下胸骨緣、Mitral 左 5 MCL。",
    },
    20: {
        "analysis": "右肺有三葉與水平裂、斜裂；左肺兩葉且無水平裂。右肺水平裂大約沿第 4 肋骨/肋軟骨高度走行。",
        "reasons": {
            "A": "左右肺葉數相反：右肺三葉、左肺二葉，因此此敘述錯。",
            "B": "右肺水平裂約對應第 4 肋骨下緣或第 4 肋軟骨高度，故正確。",
            "C": "右肺門與奇靜脈弓有關，但不是位在食道與奇靜脈之間這種簡化排列。",
            "D": "左肺門鄰近主動脈弓與降主動脈，食道在更後內側；此描述不是正確定位。",
        },
        "core": "右肺三葉且有水平裂；水平裂大約在第 4 肋骨高度。",
    },
    21: {
        "analysis": "疼痛敏感的胸膜主要是壁層胸膜。肋胸膜與周邊膈胸膜由肋間神經傳痛；縱隔胸膜與中央膈胸膜則由膈神經。題目選項中最符合胸膜炎疼痛主要傳導者為肋間神經。",
        "reasons": {
            "A": "迷走神經支配臟層胸膜等自主神經成分，但臟層胸膜對痛覺不敏感，不是主要疼痛路徑。",
            "B": "大內臟神經傳胸腹內臟交感纖維，與壁層胸膜痛覺不是主要配對。",
            "C": "喉返神經支配喉部運動與感覺，不負責胸膜炎疼痛。",
            "D": "肋間神經支配肋胸膜與周邊膈胸膜的體壁痛覺，是胸膜炎尖銳胸痛的重要傳導路徑，故正確。",
        },
        "core": "壁層胸膜痛覺：肋胸膜靠肋間神經，中央膈胸膜/縱隔胸膜靠膈神經。",
    },
    22: {
        "analysis": "本題是否定式，考肋間肌在呼吸中的角色。平靜呼吸主要靠橫膈收縮，肋間肌多為支撐肋間隙；內外肋間肌不會在平靜呼吸中規律交替作為主要升降肋骨機制。",
        "reasons": {
            "A": "平靜吸氣時肋間肌有助維持肋間空間，避免胸壁在負壓下內陷，描述合理。",
            "B": "平靜呼吸主要由橫膈驅動，說內外肋間肌交替收縮以升降肋骨過度簡化且不恰當，故為錯誤答案。",
            "C": "打噴嚏屬用力呼氣動作，肋間肌與腹肌可快速收縮以增加胸腔壓力，描述合理。",
            "D": "深呼吸時外肋間肌、內肋間肌不同部位與輔助肌可協助抬高或壓低肋骨，增加通氣幅度。",
        },
        "core": "平靜呼吸主角是橫膈；肋間肌在平靜吸氣多維持胸壁，深呼吸/用力呼吸時才更明顯參與肋骨運動。",
    },
    23: {
        "analysis": "上縱隔由前往後大致為胸腺/靜脈層、動脈層、氣管、食道。題目四組中，頭臂靜脈在前，主動脈弓較後，氣管再後，食道最後，最符合解剖排列。",
        "reasons": {
            "A": "氣管與食道位於較後方，不會排在主動脈弓與肺動脈幹之前。",
            "B": "頭臂靜脈、主動脈弓、氣管、食道符合上縱隔由前到後的典型順序，故正確。",
            "C": "肺動脈幹主要屬中縱隔心包內構造，且氣管與食道順序被放錯。",
            "D": "頭臂靜脈應位於主動脈弓更前方，不是排在主動脈弓後。",
        },
        "core": "上縱隔前後順序可記：靜脈在前、動脈在中、氣管、食道在後。",
    },
    24: {
        "analysis": "十二指腸懸肌（ligament of Treitz）含平滑肌與骨骼肌成分，附著於十二指腸空腸曲，來自橫膈右腳附近，是上消化道與下消化道分界的重要標誌。",
        "reasons": {
            "A": "腰大肌位於後腹壁，與十二指腸懸肌來源不是典型配對。",
            "B": "腰方肌屬後腹壁肌，並不形成十二指腸懸肌。",
            "C": "十二指腸懸肌與橫膈右腳相關，傳統解剖描述為來自橫膈，故正確。",
            "D": "肋下肌位於胸壁內面，與十二指腸空腸曲懸吊無關。",
        },
        "core": "Treitz ligament 來自橫膈右腳附近，標示十二指腸空腸曲。",
    },
    25: {
        "analysis": "肝臟內臟面可見胃、食道、十二指腸、右腎、右腎上腺與結腸等壓跡。胰臟位於胃後方、較靠後腹壁，通常不是肝臟內臟面典型壓跡。",
        "reasons": {
            "A": "右腎上腺壓跡位於肝右葉後上方內臟面，可見於肝臟。",
            "B": "食道壓跡可在肝左葉後方附近見到，屬肝臟內臟面相關壓跡。",
            "C": "胰臟壓跡不是肝臟內臟面的典型可見壓跡，故為答案。",
            "D": "結腸壓跡來自肝曲/橫結腸鄰近肝臟下方，是常見內臟面壓跡。",
        },
        "core": "肝臟內臟面常見食道、胃、十二指腸、結腸、右腎與右腎上腺壓跡；胰臟壓跡不典型。",
    },
    26: {
        "analysis": "薦髓 S2-S4 的副交感節前纖維經骨盆內臟神經（pelvic splanchnic nerves）進入下腹下神經叢/骨盆神經叢，支配骨盆臟器與遠端大腸。",
        "reasons": {
            "A": "腹下神經主要帶交感纖維進入骨盆，不是薦部副交感節前纖維的主要路徑。",
            "B": "陰部神經是體神經，支配會陰皮膚與骨骼肌，不是副交感節前纖維主要路徑。",
            "C": "骨盆內臟神經來自 S2-S4，攜帶副交感節前纖維進入骨盆神經叢，故正確。",
            "D": "閉孔神經來自腰神經叢，支配大腿內收肌群，與骨盆副交感無關。",
        },
        "core": "骨盆副交感 = S2-S4 pelvic splanchnic nerves；不要和交感 hypogastric nerve 或體神經 pudendal nerve 混淆。",
    },
    27: {
        "analysis": "尿道海綿體破裂常涉及海綿體尿道，尿液可進入淺會陰隙，沿 Colles fascia 連續到陰囊、陰莖與下腹前壁；不會進入睪丸或大腿深筋膜下。",
        "reasons": {
            "A": "淺會陰隙與陰囊筋膜連續，尿液外滲常堆積於陰囊，故正確。",
            "B": "睪丸有鞘膜等包覆，尿液不會直接外滲進入睪丸實質。",
            "C": "前列腺位於深部骨盆，較與後尿道損傷相關，不是尿道海綿體破裂最常堆積處。",
            "D": "Scarpa/Colles fascia 在大腿近端受闊筋膜限制，尿液通常不會進入大腿。",
        },
        "core": "海綿體尿道破裂：尿液進淺會陰隙，可到陰囊、陰莖、下腹前壁，但不進大腿。",
    },
    28: {
        "analysis": "足底內側的肌腱交叉稱 Henry knot，主要是長拇趾屈肌（flexor hallucis longus, FHL）與長趾屈肌（flexor digitorum longus, FDL）肌腱交叉。",
        "reasons": {
            "A": "脛前肌與脛後肌分別在足背/足底內側附著，並非 Henry knot 的兩條交叉肌腱。",
            "B": "腓骨長肌與腓骨短肌都屬外側腔肌群，走行不形成足底內側的 Henry knot。",
            "C": "FHL 與 FDL 在足底內側交叉，是 Henry knot 的典型構造，故正確。",
            "D": "拇趾短屈肌與趾短屈肌位於足底肌層，不是題目所問的長肌腱交叉。",
        },
        "core": "足底內側 Henry knot = FHL 與 FDL 肌腱交叉。",
    },
    29: {
        "analysis": "跗骨隧道位於內踝後方，內容物包括脛後肌腱、長趾屈肌腱、後脛動靜脈、脛神經、長拇趾屈肌腱；發炎或壓迫最典型傷及脛神經。",
        "reasons": {
            "A": "脛神經通過跗骨隧道，受壓會造成足底感覺與足內在肌症狀，故正確。",
            "B": "腓腸神經走小腿後外側與足外側皮膚，不通過跗骨隧道。",
            "C": "腓深神經走足背，主要支配第一趾蹼感覺與伸肌，不在跗骨隧道。",
            "D": "腓淺神經走小腿外側至足背皮膚，也不在跗骨隧道內。",
        },
        "core": "跗骨隧道內容物可記 Tom, Dick, And Nervous Harry；神經是 tibial nerve。",
    },
    30: {
        "analysis": "旋前圓肌屬前臂前腔屈肌/旋前肌群，由正中神經支配；旋後肌屬後腔深層，由橈神經深支/後骨間神經支配。",
        "reasons": {
            "A": "旋前圓肌由正中神經，旋後肌由橈神經系統支配，故正確。",
            "B": "此選項將兩者神經支配顛倒。",
            "C": "旋後肌不是正中神經支配，而是橈神經深支系統。",
            "D": "旋前圓肌不是橈神經支配，而是正中神經。",
        },
        "core": "前臂 pronator teres = median nerve；supinator = radial nerve deep branch/posterior interosseous nerve。",
    },
    31: {
        "analysis": "關節盤是纖維軟骨構造，可改善關節面配合與分隔關節腔。胸鎖關節與顳顎關節都具有關節盤；肩、髖以盂唇/髖臼唇較典型，不是關節盤。",
        "reasons": {
            "A": "肩關節與髖關節主要有盂唇/髖臼唇，不是典型關節盤組合。",
            "B": "胸鎖關節有關節盤，但肩關節不是典型關節盤。",
            "C": "顳顎關節有關節盤，但髖關節主要是髖臼唇。",
            "D": "胸鎖關節與顳顎關節均有關節盤，故正確。",
        },
        "core": "常考關節盤：TMJ、胸鎖關節、遠端橈尺關節、膝半月板等；肩髖多記 labrum。",
    },
    32: {
        "analysis": "絨毛膜絨毛發育：初級絨毛有細胞滋養層與融合滋養層；次級絨毛加入胚外中胚層/間葉；三級絨毛才出現胎兒微血管。",
        "reasons": {
            "A": "融合滋養層從初級絨毛就存在，不是三級絨毛才有。",
            "B": "細胞滋養層也從初級絨毛就存在，不是三級特有。",
            "C": "間葉組織在次級絨毛已出現，不是三級絨毛才有。",
            "D": "微血管出現代表三級絨毛形成，故正確。",
        },
        "core": "絨毛分期：primary = trophoblast，secondary = mesenchyme，tertiary = capillaries。",
    },
    33: {
        "analysis": "腹側腸繫膜只保留在前腸尾端相關區域，形成小網膜與鐮狀韌帶等構造；中腸與後腸一般沒有腹側腸繫膜保留。",
        "reasons": {
            "A": "原始咽屬較頭端前腸相關構造，但題目問尾端仍保留腹側腸繫膜者，最典型是前腸。",
            "B": "腹側腸繫膜在前腸尾端保留，形成肝胃、肝十二指腸韌帶與鐮狀韌帶等，故正確。",
            "C": "中腸主要有背側腸繫膜，腹側腸繫膜不保留。",
            "D": "後腸也不保留腹側腸繫膜。",
        },
        "core": "腹側腸繫膜只在前腸尾端保留，衍生小網膜與鐮狀韌帶。",
    },
    34: {
        "analysis": "中耳聽小骨源自第 1、2 咽弓。鎚骨與砧骨主要來自第 1 咽弓 Meckel cartilage，鐙骨主要來自第 2 咽弓 Reichert cartilage。",
        "reasons": {
            "A": "鎚骨、砧骨與鐙骨合計來自第 1 與第 2 咽弓，故正確。",
            "B": "第 3 咽弓與舌骨大角、莖突咽肌等較相關，不形成聽小骨組合。",
            "C": "第 3、4 咽弓不是聽小骨的主要來源。",
            "D": "第 4、6 咽弓多與喉軟骨/肌肉相關，不是鎚砧鐙的來源。",
        },
        "core": "聽小骨：malleus/incus 第 1 弓，stapes 第 2 弓。",
    },
    35: {
        "analysis": "先天斜頸常與胸鎖乳突肌纖維化、短縮或發育異常相關，造成頭偏向患側、臉轉向對側。",
        "reasons": {
            "A": "斜角肌異常可影響頸部或胸廓出口，但不是先天斜頸最典型肌肉。",
            "B": "胸鎖乳突肌發育或纖維化異常是先天斜頸的典型原因，故正確。",
            "C": "脊柱前肌群位於頸椎前方，並非先天斜頸最常見病灶。",
            "D": "舌下肌群主要參與舌骨與喉部動作，不是先天斜頸主因。",
        },
        "core": "先天斜頸最常考胸鎖乳突肌。",
    },
    36: {
        "analysis": "皮膚附屬器如汗腺、毛囊、皮脂腺多由體表外胚層向下增生形成；神經嵴則與黑色素細胞、周邊神經等較相關。",
        "reasons": {
            "A": "汗腺分泌部由體表外胚層衍生的表皮芽深入真皮形成，故正確。",
            "B": "神經嵴可形成黑色素細胞、周邊神經與腎上腺髓質等，不是汗腺分泌部主要來源。",
            "C": "咽弓中胚層與頭頸肌肉、血管等發育較相關，不形成汗腺。",
            "D": "間葉組織可形成結締組織與真皮成分，但汗腺上皮分泌部源自外胚層。",
        },
        "core": "皮膚腺體上皮多源自體表外胚層。",
    },
    37: {
        "analysis": "運動終板是神經肌肉接合處。突觸後膜是肌纖維膜（sarcolemma），形成接合皺襞以增加乙醯膽鹼受體分布面積；突觸小泡在神經末梢。",
        "reasons": {
            "A": "突觸間隙位於軸突終端與肌纖維膜之間，不是軸突終端與許旺細胞之間。",
            "B": "乙醯膽鹼受體主要位於突觸後肌纖維膜，不是軸突終端。",
            "C": "接合皺襞由肌纖維膜形成，用來增加突觸後表面積，故正確。",
            "D": "突觸小泡位於運動神經軸突終端，不在肌纖維膜上。",
        },
        "core": "NMJ：ACh 小泡在神經端，ACh receptor 與 junctional folds 在肌纖維膜。",
    },
    38: {
        "analysis": "雙層膜胞器包括細胞核、粒線體與葉綠體等。核套由內外兩層核膜構成；溶酶體與過氧化體是單層膜，脂肪小滴是磷脂單層表面。",
        "reasons": {
            "A": "溶酶體是單層膜胞器，不是雙層膜。",
            "B": "過氧化質體也是單層膜胞器。",
            "C": "核套含內核膜與外核膜，為雙層膜結構，故正確。",
            "D": "脂肪小滴表面通常為磷脂單層與蛋白質，不是雙層膜胞器。",
        },
        "core": "雙層膜記 nucleus、mitochondria；lysosome/peroxisome 是單層膜。",
    },
    39: {
        "analysis": "間質成長是基質內細胞分裂並從內部擴張，軟骨可因軟骨細胞仍在基質腔內分裂而間質成長；骨主要靠骨膜/內膜表面沉積的附加成長，不以間質成長為主。",
        "reasons": {
            "A": "透明軟骨可有間質成長，尤其在生長板與早期軟骨模型中重要。",
            "B": "纖維軟骨仍屬軟骨類型，可有一定間質成長能力。",
            "C": "彈性軟骨也可由軟骨細胞在基質中增生而間質成長。",
            "D": "硬骨基質礦化後細胞被限制於骨陷窩，主要靠表面附加成長，不是間質成長，故為答案。",
        },
        "core": "軟骨可間質成長；骨主要 appositional growth。",
    },
    40: {
        "analysis": "Purkinje cells 是小腦皮質的巨大梨形神經元，位於分子層與顆粒層之間的 Purkinje cell layer，是小腦皮質主要輸出神經元。",
        "reasons": {
            "A": "大腦皮質有錐體細胞等，不是 Purkinje cells 的典型位置。",
            "B": "Purkinje cells 位於小腦皮質，故正確。",
            "C": "丘腦是灰質核團，不含典型小腦 Purkinje cell layer。",
            "D": "脊髓灰質有前角運動神經元等，不是 Purkinje cells 所在。",
        },
        "core": "Purkinje cells = cerebellar cortex 的主要輸出神經元。",
    },
    41: {
        "analysis": "肌型動脈的中膜以平滑肌為主，內彈性膜明顯且常呈波浪狀；彈性動脈才以多層彈性板為特色。",
        "reasons": {
            "A": "外膜通常不是最薄層，且可含血管滋養血管與神經，描述不佳。",
            "B": "中膜主要是平滑肌；多層彈性板是彈性動脈特色，不是肌型動脈主描述。",
            "C": "內膜表面是單層扁平內皮，不是多層扁平內皮。",
            "D": "肌型動脈有明顯、波浪狀內彈性膜，是重要辨識點，故正確。",
        },
        "core": "肌型動脈：中膜平滑肌多、內彈性膜明顯；彈性動脈：彈性板多。",
    },
    42: {
        "analysis": "齒堊質覆蓋牙根表面，供牙周韌帶 Sharpey fibers 嵌入，協助牙齒固定於齒槽骨。它不是由成釉細胞形成，也不覆蓋牙冠。",
        "reasons": {
            "A": "牙周韌帶的 Sharpey fibers 會嵌入齒堊質與齒槽骨，是牙齒固定重點，故正確。",
            "B": "齒堊質外接牙周韌帶、內接牙本質；齒髓在更內部，琺瑯質覆蓋牙冠。",
            "C": "琺瑯質由成釉細胞形成；齒堊質由成齒堊質細胞形成。",
            "D": "齒堊質主要覆蓋牙根，不是牙根與牙冠均有。",
        },
        "core": "齒堊質在牙根表面，讓 periodontal ligament 的 Sharpey fibers 嵌入。",
    },
    43: {
        "analysis": "Brunner glands 是十二指腸特有的黏膜下層腺體，分泌鹼性黏液以中和胃酸並保護十二指腸黏膜。",
        "reasons": {
            "A": "腸腺位於黏膜，但 Brunner glands 的定位特色是黏膜下層。",
            "B": "十二指腸腺位於黏膜下層，是辨認十二指腸的組織學重點，故正確。",
            "C": "外肌層負責腸蠕動，不含 Brunner glands。",
            "D": "外膜/漿膜不是十二指腸腺位置。",
        },
        "core": "十二指腸辨識：submucosa 有 Brunner glands。",
    },
    44: {
        "analysis": "移形上皮（urothelium）覆蓋腎盂、輸尿管、膀胱與近端尿道，可耐受伸展與尿液環境；尿道外口接近皮膚/鱗狀上皮，不是移形上皮。",
        "reasons": {
            "A": "腎盂屬集尿通道，覆蓋移形上皮。",
            "B": "近端尿道仍可見移形上皮，尤其靠近膀胱處。",
            "C": "膀胱是移形上皮最典型器官之一。",
            "D": "尿道外口接近外界，以上皮轉變為鱗狀上皮為主，不是移形上皮，故為答案。",
        },
        "core": "Urothelium 從腎盂到膀胱與近端尿道；越靠外口越轉為鱗狀上皮。",
    },
    45: {
        "analysis": "子宮內膜增生期受雌激素影響，功能層由基底層再生，腺體上皮增生、腺體較直，基質細胞分裂；分泌期才有水腫、腺體分泌與螺旋動脈更彎曲延伸。",
        "reasons": {
            "A": "增生期基質細胞會分裂增生，不是不分裂並大量儲存膠原。",
            "B": "螺旋動脈延伸至表層、變得更彎曲是分泌期較明顯。",
            "C": "上皮肥大與內膜水腫較符合分泌期黃體素作用。",
            "D": "增生期由子宮腺基部上皮開始重建功能層與腺體，故正確。",
        },
        "core": "增生期 = estrogen 驅動腺體與基質增生重建；分泌期 = progesterone 驅動腺體分泌、水腫、螺旋動脈發育。",
    },
    46: {
        "analysis": "精子生成在細精管上皮由基底部往管腔逐步成熟。精原細胞貼近基底膜，精母細胞、精細胞逐漸靠近管腔；Leydig cells 在間質，不在細精管上皮內。",
        "reasons": {
            "A": "精原細胞位於基底膜附近，是最靠近管腔底部的生殖細胞，故正確。",
            "B": "精母細胞由精原細胞分化而來，位置較精原細胞靠近管腔。",
            "C": "精細胞更成熟，位於更靠近管腔處。",
            "D": "Leydig cell 位於細精管間質，負責分泌睪固酮，不在管腔底部排列中。",
        },
        "core": "細精管生殖細胞由基底到管腔：spermatogonia -> spermatocyte -> spermatid -> spermatozoa。",
    },
    47: {
        "analysis": "消化道上皮吸收需要極性與旁細胞通透性控制。緊密結合封閉細胞間隙並維持頂端/基底外側膜蛋白分布，是嚴格管控管腔物質通過的關鍵。",
        "reasons": {
            "A": "緊密結合控制旁細胞路徑與上皮極性，最能嚴格調控吸收，故正確。",
            "B": "間隙結合負責細胞間小分子訊息傳遞，不是管腔吸收屏障主角。",
            "C": "胞橋體提供機械連結，抗拉扯，不主要管控小分子吸收。",
            "D": "connexin 是 gap junction 的蛋白組成，不是嚴格吸收屏障。",
        },
        "core": "上皮屏障與極性靠 tight junction；機械連結靠 desmosome，溝通靠 gap junction。",
    },
    48: {
        "analysis": "沒有視野缺失代表初級視覺路徑大致保留；無法說出所見物體形狀屬視覺辨識/物體識別障礙，較涉及腹側視覺路徑與顳葉皮質。",
        "reasons": {
            "A": "兩側 optic radiation 上半部受損會造成視野缺損，不符合完全沒有視野缺失。",
            "B": "Meyer's loop 受損會造成上象限盲等視野缺損，不符合題幹。",
            "C": "顳葉皮質參與物體形狀與意義辨識，受損可有視覺失認而無初級視野缺損，故正確。",
            "D": "頂葉較偏空間定位、注意與背側視覺路徑，不是物體形狀命名辨識的最典型位置。",
        },
        "core": "視覺腹側路徑（temporal cortex）處理 what/物體辨識；背側 parietal 路徑處理 where/how。",
    },
    49: {
        "analysis": "腎上腺髓質可視為改造的交感神經節。支配髓質嗜鉻細胞的是交感節前纖維，節前交感神經末梢釋放 acetylcholine 作用於 nicotinic receptor。",
        "reasons": {
            "A": "epinephrine 是腎上腺髓質細胞分泌到血中的主要激素之一，不是支配髓質的交感神經末梢主要傳遞物。",
            "B": "分布到腎上腺髓質的交感節前纖維釋放 acetylcholine，故正確。",
            "C": "CGRP 是感覺神經相關胜肽，不是此處主要交感節前傳遞物。",
            "D": "GABA 是中樞抑制性神經傳遞物，不是腎上腺髓質交感末梢主要物質。",
        },
        "core": "腎上腺髓質接受交感節前纖維，節前釋放 ACh；髓質細胞再分泌 E/NE 入血。",
    },
    50: {
        "analysis": "丘腦特異核與皮質配對：LGN 對初級視覺皮質、VPL 對身體初級體感覺皮質、VPM 對臉部/味覺相關感覺皮質、VA/VL 對運動皮質。題目問錯誤配對，VPM 並非直接對所謂初級痛覺皮質。",
        "reasons": {
            "A": "外側膝狀核投射至初級視覺皮質，是正確配對。",
            "B": "VPL 接收身體感覺並投射至初級體感覺皮質，是正確配對。",
            "C": "VPM 主要處理臉部體感覺與味覺相關輸入，不是單一配對到初級痛覺皮質，故為錯誤答案。",
            "D": "腹前核與運動皮質、基底核迴路相關，配對可接受。",
        },
        "core": "丘腦配對：LGN-視覺、MGN-聽覺、VPL-身體感覺、VPM-臉部感覺/味覺、VA/VL-運動。",
    },
    51: {
        "analysis": "本題問 REM sleep 最不適當敘述。REM 腦波低振幅快波，反而類似清醒狀態；NREM 尤其深睡期與清醒腦波差異更大。",
        "reasons": {
            "A": "REM 腦波與清醒較相似，說 REM 與清醒差異大於 NREM 與清醒差異是錯誤，故為答案。",
            "B": "PGO spikes 是 REM 睡眠常見相關現象，敘述合理。",
            "C": "REM 期有肌張力抑制，頸部與多數骨骼肌張力低於清醒，敘述合理。",
            "D": "REM 期常伴快速眼動、局部抽動與較可回憶夢境，敘述合理。",
        },
        "core": "REM = 腦波像清醒、肌張力低、夢多、PGO spikes；深 NREM 才與清醒腦波差異大。",
    },
    52: {
        "analysis": "fentanyl 對病人具有止痛效果，也因按鈕後帶來疼痛緩解與酬賞而強化按壓行為。Nocebo 是負向期待造成症狀惡化，與 fentanyl 的角色相反。",
        "reasons": {
            "A": "fentanyl 是 opioid analgesic，作為止痛劑符合情境。",
            "B": "nocebo 指負向期待造成不良感受或症狀加重；fentanyl 在此帶來止痛與酬賞，最不可能是 nocebo，故為答案。",
            "C": "按壓後獲得止痛會增加未來按壓行為，是行為強化物。",
            "D": "疼痛緩解與 opioid 效果可形成酬賞與動機，因此可作為 reward。",
        },
        "core": "reinforcer/reward 會增加行為；nocebo 是負向期待造成症狀惡化，和止痛酬賞相反。",
    },
    53: {
        "analysis": "打開某離子通道時，膜電位會往該離子的平衡電位移動。靜止膜電位 -75 mV；Cl- 平衡電位 -70 mV 較正，打開後去極化；K+ 平衡電位 -80 mV 較負，打開後過極化。",
        "reasons": {
            "A": "Cl- 將膜電位拉向 -70 mV，K+ 拉向 -80 mV，因此分別去極化與過極化，故正確。",
            "B": "此選項把兩者方向顛倒。",
            "C": "K+ 平衡電位比靜止膜電位更負，打開 K+ 通道不會去極化。",
            "D": "Cl- 平衡電位比靜止膜電位更正，打開 Cl- 通道不會過極化。",
        },
        "core": "通道打開後，膜電位往該離子的 equilibrium potential 移動。",
    },
    54: {
        "analysis": "化學突觸傳遞需要動作電位使突觸前電壓依賴性 Ca2+ 通道開啟，Ca2+ 流入觸發囊泡融合與神經傳遞物釋放。",
        "reasons": {
            "A": "阻斷突觸前 Ca2+ 流入會阻止囊泡融合，因此可阻止傳遞物釋放，故正確。",
            "B": "典型突觸延遲約 0.5-1 ms，不是 50-100 ms。",
            "C": "glycine 受體多為 Cl- 通道，通常造成抑制性突觸後電位。",
            "D": "神經傳遞物多靠再回收、酵素分解或膠細胞清除，不是大多由微血管擴散回收。",
        },
        "core": "突觸前 Ca2+ influx 是 vesicle fusion 與 neurotransmitter release 的必要步驟。",
    },
    55: {
        "analysis": "骨骼肌收縮開始的前幾秒需要快速再生 ATP，最立即的來源是 phosphocreatine 將高能磷酸轉給 ADP，由 creatine kinase 催化。",
        "reasons": {
            "A": "磷酸肌酸可快速把磷酸轉給 ADP 形成 ATP，是最初數秒主要來源，故正確。",
            "B": "氧化磷酸化效率高但啟動與供氧較慢，不是最初幾秒主要來源。",
            "C": "糖解作用可在短時間提供 ATP，但通常接在磷酸肌酸系統之後成為重要來源。",
            "D": "脂肪酸不經 glycolysis 產生 ATP，而是經 beta-oxidation 與氧化磷酸化，速度更慢。",
        },
        "core": "肌肉立即能量系統：ATP-PCr 最快；接著無氧糖解，長時間靠氧化代謝。",
    },
    56: {
        "analysis": "SA node 的 pacemaker potential（phase 4）由 funny Na+ current、T-type Ca2+ 及後續 Ca2+ 流入共同促成，並伴隨 K+ 外流減少，使膜電位緩慢上升。",
        "reasons": {
            "A": "鈉離子與鈣離子流入是緩慢去極化的主要來源，故正確。",
            "B": "鈣離子流出不會造成 pacemaker 去極化，方向錯誤。",
            "C": "鈉離子流出會使膜電位較負，不符合緩慢上升。",
            "D": "鈉、鈣皆流出不會造成去極化。",
        },
        "core": "SA node phase 4：If Na+ inward、Ca2+ inward、K+ outward 減少。",
    },
    57: {
        "analysis": "短暫阻斷血流後移除阻斷，缺血期間累積的代謝物與低氧會使血管擴張，恢復血流時出現短暫血流增加，稱反應性充血。",
        "reasons": {
            "A": "主動性充血是組織代謝活動增加時血流上升，如運動肌肉，不是解除短暫阻斷後的現象。",
            "B": "阻斷血流後再放開造成過度血流，是反應性充血，故正確。",
            "C": "肌原反應是血管平滑肌對壓力伸展的自動調節，不是此題主因。",
            "D": "對傷害的反應太廣，不能解釋綁住手指後放開的典型局部血流機制。",
        },
        "core": "Reactive hyperemia = ischemia 後放開，代謝物累積造成短暫血流過多。",
    },
    58: {
        "analysis": "失血時維持平均動脈壓主要靠交感活化：心跳加快、收縮力增加、微動脈收縮、靜脈收縮與副交感下降。心房利鈉肽（ANP）在心房伸展增加時釋放，會促進排鈉利尿與血管擴張，失血時不應增加。",
        "reasons": {
            "A": "腎上腺素增加可刺激竇房結，提高心率，符合代償。",
            "B": "微動脈半徑減少代表血管收縮，可增加周邊阻力維持血壓。",
            "C": "副交感活性下降可使心率上升，是壓力感受器反射的一部分。",
            "D": "失血時心房充盈下降，不會增加 ANP；ANP 增加還會降低血容量與血壓，故最不可能。",
        },
        "core": "失血代償靠交感上升、血管收縮、心率上升；ANP 是容量過多時的利鈉降壓訊號。",
    },
    59: {
        "analysis": "心肌動作電位有長 plateau phase，使不反應期很長，接近收縮期間，避免強直收縮並確保心室舒張充盈。",
        "reasons": {
            "A": "正常每次心跳時心肌功能性合胞體幾乎同步活化，不是只有部分細胞收縮。",
            "B": "心肌不反應期大約與動作電位 plateau 持續時間相當，故正確。",
            "C": "心搏量主要與舒張末期肌肉長度/前負荷正相關，不是收縮末期容積越大越好。",
            "D": "等容舒張期心室正在放鬆，並非處於產生最大收縮力的最佳長度描述。",
        },
        "core": "心肌長 plateau -> 長 refractory period -> 防止 tetanus。",
    },
    60: {
        "analysis": "膈神經支配橫膈，吸氣時需要橫膈收縮，因此平靜吸氣與用力吸氣都會增加膈神經放電；呼氣平靜時多為被動。",
        "reasons": {
            "A": "用力吸氣時橫膈仍會更強收縮，膈神經放電不會不增加。",
            "B": "平靜呼氣多為被動，不是膈神經放電增加的時相。",
            "C": "平靜吸氣與用力吸氣均需橫膈收縮，膈神經放電頻率增加，故正確。",
            "D": "呼氣尤其平靜呼氣不以膈神經興奮為主。",
        },
        "core": "膈神經放電增加代表橫膈吸氣收縮；平靜與用力吸氣都會增加。",
    },
    61: {
        "analysis": "兩試管 PO2 都是 40 mmHg，但乙的 PCO2 較高。CO2 上升使 pH 下降並造成 Bohr effect，血紅素氧解離曲線右移，在相同 PO2 下氧飽和度較低。",
        "reasons": {
            "A": "乙的血氧飽和度較低，血液總氧含量不會與甲相同。",
            "B": "血漿溶解氧主要由 PO2 決定，兩者 PO2 相同時血漿溶解氧相近，不是甲更多的核心差異。",
            "C": "乙 PCO2 較高造成 Bohr effect，血紅素氧飽和度比甲低，故正確。",
            "D": "PCO2 較高會使 pH 較低，不是較高。",
        },
        "core": "CO2 上升/酸中毒 -> Bohr effect -> Hb-O2 affinity 下降，同 PO2 下 O2 saturation 降低。",
    },
    62: {
        "analysis": "脂肪酵素可由舌/口腔、胃、小腸與胰臟相關分泌參與脂肪消化；膽囊主要儲存與濃縮膽汁，本身不分泌 lipase。",
        "reasons": {
            "A": "口腔可有 lingual lipase 參與脂肪消化，尤其在早期消化中有角色。",
            "B": "小腸上皮與腸液可有少量脂解相關酵素或消化輔助作用，不是最少。",
            "C": "胰臟分泌 pancreatic lipase，是脂肪消化最主要來源。",
            "D": "膽囊儲存膽汁、排出膽鹽幫助乳化脂肪，但不分泌脂肪酵素，故最少。",
        },
        "core": "膽囊排膽汁不分泌 lipase；脂肪消化主要靠 pancreatic lipase。",
    },
    63: {
        "analysis": "脂溶性維生素 A、D、E、K 功能各有典型配對：A 視覺與上皮、D 鈣磷吸收、E 抗氧化、K 凝血因子 gamma-carboxylation。增加肌肉張力不是維生素 K 的主要功能。",
        "reasons": {
            "A": "維生素 K 主要參與凝血因子修飾，不是增加肌肉張力，故為最不恰當答案。",
            "B": "活化態維生素 D 可促進腸道鈣磷吸收，敘述正確。",
            "C": "維生素 E 是脂溶性抗氧化劑，保護細胞膜脂質，敘述正確。",
            "D": "維生素 A 參與視紫質等感光色素形成，敘述正確。",
        },
        "core": "脂溶性維生素：A vision，D calcium，E antioxidant，K coagulation。",
    },
    64: {
        "analysis": "遠曲小管管腔側 Na-Cl cotransporter 的鈉再吸收，最終仰賴基底外側 Na/K ATPase 維持低細胞內 Na+；基底外側 K+ channel 讓 K+ 回收並維持 Na/K ATPase 運作與膜電位。",
        "reasons": {
            "A": "基底外側 K+ channel 支持 K+ recycling、膜電位與 Na/K ATPase 功能，間接維持管腔側鈉再吸收驅動力，故正確。",
            "B": "氯離子通道可參與氯外流，但題目問最有賴於搭配的關鍵通道時，K+ recycling 更核心。",
            "C": "基底外側鈉通道不是維持低細胞內 Na+ 的主要機制；主要靠 Na/K ATPase。",
            "D": "遠曲小管早段對水通透性低，水通道不是 NCC 鈉再吸收的主要搭配。",
        },
        "core": "DCT NaCl reabsorption 靠 luminal NCC，加上 basolateral Na/K ATPase 與 K+ recycling 維持梯度。",
    },
    65: {
        "analysis": "菊糖可自由濾過，不被分泌、不被再吸收，因此清除率等於 GFR。用來估腎血漿流量的是 PAH，而不是 inulin。",
        "reasons": {
            "A": "菊糖可經腎絲球自由濾過，敘述正確。",
            "B": "菊糖不被腎小管分泌或再吸收，這正是測 GFR 的理由。",
            "C": "菊糖清除率接近 GFR，不接近腎血漿流量；腎血漿流量用 PAH 估算，故為錯誤答案。",
            "D": "菊糖清除率與腎小球濾過率接近，敘述正確。",
        },
        "core": "Inulin clearance = GFR；PAH clearance 估 renal plasma flow。",
    },
    66: {
        "analysis": "Mesangial cell 收縮會降低濾過表面積，常受 angiotensin II、endothelin、norepinephrine 等血管收縮物質促進。Dopamine 在腎臟多與血管舒張、利鈉相關，最不可能造成收縮。",
        "reasons": {
            "A": "多巴胺在低劑量腎臟作用偏血管舒張與利鈉，不是典型促進 mesangial contraction 因子，故為答案。",
            "B": "endothelin 是強力血管收縮物質，可促進 mesangial cell 收縮。",
            "C": "angiotensin II 可收縮出球小動脈，也可促進 mesangial cell 收縮。",
            "D": "norepinephrine 透過交感 alpha 作用促進血管與 mesangial 收縮。",
        },
        "core": "Mesangial contraction 常由 Ang II、endothelin、NE 促進；dopamine 腎臟作用偏舒張/利鈉。",
    },
    67: {
        "analysis": "ACTH 作用於腎上腺皮質 MC2 receptor，主要經 Gs-cAMP-PKA 路徑促進膽固醇運送與類固醇生成。原發性腎上腺不足時 cortisol 低，負回饋減少使 ACTH 上升。",
        "reasons": {
            "A": "ACTH 主要不是 PLC 路徑，而是 cAMP/PKA 路徑。",
            "B": "類固醇生成關鍵是膽固醇進入粒線體，非平滑內質網作為第一步。",
            "C": "皮質醇為脂溶性類固醇，合成後擴散釋放，不是預先儲於分泌囊泡。",
            "D": "原發性腎上腺不足 cortisol 下降，對下視丘/腦下垂體負回饋降低，使 ACTH 增加，故正確。",
        },
        "core": "ACTH = cAMP/PKA 促 steroidogenesis；primary adrenal insufficiency = cortisol 低、ACTH 高。",
    },
    68: {
        "analysis": "GH 受 GHRH 與 ghrelin 促進，受 somatostatin 抑制；飢餓、運動與慢波睡眠可增加 GH，老化 GH 分泌下降。多巴胺典型抑制 prolactin，不是 GH 的主要抑制因子。",
        "reasons": {
            "A": "下視丘 dopamine 主要抑制 prolactin，不是抑制 GH 的典型調控，故為最不適當答案。",
            "B": "飢餓狀態可促進 GH，以動員能源並維持血糖。",
            "C": "慢波睡眠，尤其深睡期，會促進 GH 脈衝分泌。",
            "D": "GH 分泌隨年齡增加而下降，50 歲通常低於 20 歲。",
        },
        "core": "GH regulation：GHRH/ghrelin 促進，somatostatin 抑制；dopamine 主要抑制 prolactin。",
    },
    69: {
        "analysis": "進食後腸道 enteroendocrine cells 分泌 incretin，特別是 GLP-1 與 GIP，可葡萄糖依賴性促進胰島素分泌。DPP-4 是分解 GLP-1 的酵素，不是促胰島素的腸泌素本身。",
        "reasons": {
            "A": "腎上腺素來自腎上腺髓質/交感系統，通常抑制胰島素並促升糖，不是進食腸泌素。",
            "B": "DPP-4 是分解 incretin 的酵素，不是促進胰島素分泌的腸道荷爾蒙。",
            "C": "GLP-1 是進食後由腸道 L cells 分泌的 incretin，可促進胰島素分泌，故正確。",
            "D": "GLUT-4 是胰島素敏感組織的葡萄糖運輸蛋白，不是腸道分泌物。",
        },
        "core": "Incretin effect：GLP-1/GIP 進食後促 insulin；DPP-4 分解 incretin。",
    },
    70: {
        "analysis": "類固醇生成的限速早期步驟是膽固醇由外粒線體膜運入內粒線體膜，StAR 蛋白負責此運送；缺陷可造成先天性脂質性腎上腺增生。",
        "reasons": {
            "A": "膽固醇酯酶可釋放游離膽固醇，但不是把膽固醇送入粒線體的關鍵蛋白。",
            "B": "LDL receptor 負責攝取膽固醇來源，不是粒線體內運送步驟。",
            "C": "HDL receptor 可參與膽固醇取得，但不是本題所問的 StAR 功能。",
            "D": "StAR 促進膽固醇進入粒線體以啟動 steroidogenesis，缺陷可造成 congenital lipoid adrenal hyperplasia，故正確。",
        },
        "core": "Steroidogenesis first key step：StAR moves cholesterol into mitochondria。",
    },
    71: {
        "analysis": "甲狀腺分泌入血的主要荷爾蒙量以 T4 最多；T3 生物活性較強，但許多 T3 由周邊組織將 T4 去碘轉換而來。",
        "reasons": {
            "A": "T4 是正常甲狀腺分泌量最多的甲狀腺荷爾蒙，故正確。",
            "B": "reverse T3 是 T4 的非活性代謝產物，不是分泌最多者。",
            "C": "DIT 是甲狀腺素合成中的碘化酪胺酸殘基，不是主要分泌荷爾蒙。",
            "D": "T3 活性較強，但分泌量少於 T4，多由周邊轉換產生。",
        },
        "core": "甲狀腺分泌量 T4 > T3；活性 T3 > T4。",
    },
    72: {
        "analysis": "LH receptor 在男性 Leydig cells 上，LH 刺激睪固酮生成；睪固酮對 Sertoli cell 支持精子生成非常重要。LH receptor 缺失導致睪固酮不足，精子生成能力低。",
        "reasons": {
            "A": "inhibin 由 Sertoli cells 分泌，主要回饋抑制 FSH，不是 LH receptor 缺失時最直接缺乏的調節物。",
            "B": "cortisol 與壓力及代謝相關，不是男性精子生成的主要局部調節因子。",
            "C": "estradiol 在男性也有少量作用，但不是 LH receptor 缺失造成精子生成低下的主軸。",
            "D": "LH 透過 Leydig cells 促進 testosterone，睪固酮是精子生成的重要支持，故正確。",
        },
        "core": "LH -> Leydig cell -> testosterone；FSH -> Sertoli cell；testosterone 與 FSH 共同支持 spermatogenesis。",
    },
    73: {
        "analysis": "FSH 促進卵巢顆粒細胞增生、芳香化酶活性與濾泡由早期走向竇狀濾泡。缺乏 FSH 會導致 antral follicles 缺乏、雌激素低，而 androgen 可相對正常。",
        "reasons": {
            "A": "LH 主要刺激卵泡膜細胞產生 androgen；題幹 androgen 正常，不最支持 LH 缺乏。",
            "B": "FSH 缺乏會使顆粒細胞功能與濾泡成熟受阻，antral follicles 少且 estrogen 低，故正確。",
            "C": "inhibin 是由顆粒細胞分泌、回饋抑制 FSH；缺乏 inhibin 不會造成 FSH 缺乏型表現。",
            "D": "GnRH 缺乏通常會同時降低 LH 與 FSH，使 androgen 也可能下降，不如單純 FSH 缺乏符合。",
        },
        "core": "FSH 支持 granulosa cell、aromatase 與 antral follicle development；LH 支持 theca androgen。",
    },
    74: {
        "analysis": "肌紅蛋白 heme 中的 O2 結合會由遠端 histidine（distal His）穩定，形成氫鍵並降低一氧化碳相對親和力。",
        "reasons": {
            "A": "serine 可形成氫鍵，但不是肌紅蛋白 heme 氧結合位點的典型遠端殘基。",
            "B": "histidine，特別是 distal histidine，可與 O2 形成氫鍵穩定結合，故正確。",
            "C": "proline 結構特殊，常造成二級結構轉折，不是此處穩定 O2 的殘基。",
            "D": "tyrosine 有酚基可形成氫鍵，但不是肌紅蛋白 O2 結合的經典答案。",
        },
        "core": "Myoglobin O2 binding 由 distal histidine 穩定；proximal histidine 則連接 heme iron。",
    },
    75: {
        "analysis": "酵素催化效率常用 kcat/KM 表示，結合 turnover number 與底物親和/所需濃度資訊；數值越大，低底物濃度下催化越有效。",
        "reasons": {
            "A": "1/kcat 越大代表 turnover 越慢，不代表效率越佳。",
            "B": "KM 越大通常表示達半最大速率所需底物濃度越高，不等同效率越好。",
            "C": "kcat/KM 是酵素催化效率指標，數值越大越佳，故正確。",
            "D": "KM/kcat 是催化效率的倒數方向，越大反而通常越差。",
        },
        "core": "Catalytic efficiency = kcat/KM。",
    },
    76: {
        "analysis": "酵素降低活化能、穩定過渡態、加速達到平衡，但不改變反應物與產物間的自由能差，也不改變平衡常數。",
        "reasons": {
            "A": "酵素不改變反應物與產物的自由能差 ΔG，只降低活化能，因此此敘述錯誤，故為答案。",
            "B": "酵素常藉由穩定 transition state 降低活化能，敘述正確。",
            "C": "許多酵素具有立體化學專一性，敘述正確。",
            "D": "酵素可加快正反反應，使系統更快達平衡，但不改變平衡位置，敘述正確。",
        },
        "core": "Enzyme lowers activation energy, not ΔG or Keq。",
    },
    77: {
        "analysis": "phenylalanine hydroxylase 將 phenylalanine 羥化為 tyrosine，需要 tetrahydrobiopterin（BH4）作為輔因子；BH4 缺乏也可造成高苯丙胺酸血症。",
        "reasons": {
            "A": "tetrahydrobiopterin 是 phenylalanine hydroxylase 必需輔因子，故正確。",
            "B": "biotin 是羧化反應常見輔酶，不是此羥化反應的輔因子。",
            "C": "thiamine pyrophosphate 參與氧化脫羧與轉酮醇反應，不是 PAH 輔因子。",
            "D": "pyridoxal phosphate 常參與胺基轉移與脫羧，不是 phenylalanine hydroxylase 的核心輔因子。",
        },
        "core": "Phenylalanine -> tyrosine by phenylalanine hydroxylase requires BH4。",
    },
    78: {
        "analysis": "羧化反應需要攜帶 CO2 的輔酶，典型為 biotin，例如 pyruvate carboxylase、acetyl-CoA carboxylase、propionyl-CoA carboxylase。",
        "reasons": {
            "A": "biotin 負責攜帶活化 CO2，是羧化反應輔酶，故正確。",
            "B": "NAD+ 主要參與氧化還原反應，接受 hydride，不攜帶 CO2。",
            "C": "FAD 也是氧化還原輔因子，不是羧化反應 CO2 carrier。",
            "D": "TPP 參與醛基轉移與脫羧反應，不是羧化反應攜帶 CO2 的輔酶。",
        },
        "core": "Carboxylation uses biotin as CO2 carrier。",
    },
    79: {
        "analysis": "迴文序列指雙股 DNA 以 5' 到 3' 方向讀取時，互補股呈對稱序列。選項 B 的 CCTTCCGGAAGG 互補反向仍可對應自身。",
        "reasons": {
            "A": "AGGTCCTCCAGG 的反向互補不等於自身，不是迴文序列。",
            "B": "CCTTCCGGAAGG 的兩半互補對稱，符合 DNA palindromic sequence，故正確。",
            "C": "GAATCCCTTAGG 反向互補後不與原序列相同。",
            "D": "GGATCCCCTAGG 雖含部分限制酶樣片段，但整段不呈完整迴文對稱。",
        },
        "core": "DNA palindrome 要看反向互補是否相同，不是單股正反讀一樣。",
    },
    80: {
        "analysis": "Lesch-Nyhan syndrome 由 HGPRT 缺乏造成嘌呤 salvage pathway 障礙，導致尿酸過多與神經行為症狀；de novo pathway 本身仍可運作且常因 PRPP 增加而上升。",
        "reasons": {
            "A": "HGPRT 缺乏是 Lesch-Nyhan syndrome 的病因，敘述正確。",
            "B": "此病是 salvage pathway 缺陷，不是無法用 de novo pathway 合成 guanine；de novo 反而可增加，故為錯誤答案。",
            "C": "HGPRT deficiency 為 X-linked recessive，敘述正確。",
            "D": "嘌呤分解增加造成尿酸過多，可導致痛風、腎結石與組織傷害，敘述正確。",
        },
        "core": "Lesch-Nyhan = HGPRT salvage defect, X-linked, hyperuricemia, self-mutilation；de novo purine synthesis not absent。",
    },
    81: {
        "analysis": "大腸桿菌染色體 DNA 複製的主要複製型聚合酶是 DNA polymerase III；DNA polymerase I 主要移除 RNA primer 並補缺口。",
        "reasons": {
            "A": "DNA polymerase I 參與 RNA primer 移除與 DNA 修補，不是主要複製聚合酶。",
            "B": "DNA polymerase II 多與 DNA 修復/壓力反應相關，不是染色體複製主力。",
            "C": "DNA polymerase III 是 E. coli 染色體複製的主要聚合酶，故正確。",
            "D": "DNA polymerase IV 屬 translesion synthesis 相關，不是主要複製酶。",
        },
        "core": "E. coli replication main polymerase = DNA pol III；primer removal = DNA pol I。",
    },
    82: {
        "analysis": "同源性重組中，RecA 會結合單股 DNA 形成核蛋白螺旋絲，促進同源序列搜尋與 strand invasion。",
        "reasons": {
            "A": "DNA polymerase 負責合成 DNA，不是包覆 ssDNA 形成重組螺旋絲的蛋白。",
            "B": "RuvC 是 Holliday junction resolvase，作用在後期切解結構。",
            "C": "RecA 包覆 ssDNA 形成 helical filament，是同源重組核心蛋白，故正確。",
            "D": "RecBCD 參與 DNA 末端處理與產生可供 RecA 裝載的 ssDNA，但不是題目所問包覆形成螺旋絲者。",
        },
        "core": "Homologous recombination：RecA coats ssDNA and mediates strand invasion。",
    },
    83: {
        "analysis": "UvrA、UvrB、UvrC 組成細菌 nucleotide excision repair 系統，可辨認 UV thymine dimer 等 bulky DNA lesion，切除受損寡核苷酸片段。",
        "reasons": {
            "A": "直接修復如 photolyase 直接修復 thymine dimer，不是 UvrABC excinuclease 主要分類。",
            "B": "重組修復處理複製後缺口等，核心不是 UvrABC。",
            "C": "錯誤配對修復以 MutS/MutL/MutH 等為典型，不是 UvrABC。",
            "D": "UvrABC excinuclease 是核苷酸切除修復的細菌系統，故正確。",
        },
        "core": "UvrABC = bacterial nucleotide excision repair for bulky lesions。",
    },
    84: {
        "analysis": "真核轉譯起始依賴 5' cap、eIFs、掃描至 AUG；某些情境可用 IRES。Shine-Dalgarno sequence 是原核 mRNA 與 16S rRNA 配對的起始訊號，不是真核一般起始所需。",
        "reasons": {
            "A": "5' cap 是真核 cap-dependent translation initiation 的重要結構。",
            "B": "IRES 可在部分病毒或特殊 mRNA 中促進真核核糖體進入，仍屬真核可用機制。",
            "C": "eIF2 攜帶 initiator Met-tRNA 至小次單元，是真核起始重要因子。",
            "D": "Shine-Dalgarno sequence 是原核轉譯起始序列，對真核細胞最不重要，故為答案。",
        },
        "core": "Eukaryotic initiation uses 5' cap/eIF/scanning; Shine-Dalgarno is prokaryotic。",
    },
    85: {
        "analysis": "chloramphenicol、cycloheximide、puromycin 都抑制蛋白質合成不同步驟；penicillin 抑制細菌細胞壁 peptidoglycan 交聯，不直接抑制蛋白質生合成。",
        "reasons": {
            "A": "chloramphenicol 抑制原核 50S peptidyl transferase，會抑制蛋白質合成。",
            "B": "cycloheximide 抑制真核 60S translocation，會抑制蛋白質合成。",
            "C": "penicillin 抑制細胞壁合成，不抑制蛋白質生合成，故為答案。",
            "D": "puromycin 類似 aminoacyl-tRNA，造成 premature chain termination，會抑制蛋白質合成。",
        },
        "core": "Penicillin targets cell wall transpeptidation, not protein synthesis。",
    },
    86: {
        "analysis": "拓樸異構酶透過暫時切斷 DNA 磷酸雙酯鍵、讓 DNA 旋轉或穿越後再接回，以解除複製與轉錄時的超螺旋張力。",
        "reasons": {
            "A": "暫時切斷並重新接合 DNA 以紓緩纏繞壓力，是 topoisomerase 核心功能，故正確。",
            "B": "保護染色體尾端是 telomere/telomere-binding proteins 的功能，不是 topoisomerase。",
            "C": "組蛋白修飾由 histone acetyltransferase、deacetylase、methyltransferase 等執行，不是 topoisomerase 主要功能。",
            "D": "致癌基因轉譯後修飾不是 topoisomerase 的典型作用。",
        },
        "core": "Topoisomerase cuts and rejoins DNA to relieve supercoiling。",
    },
    87: {
        "analysis": "核糖體由 rRNA 與蛋白質構成，大小次單元都含 rRNA；rRNA 不只是結構，也具催化功能，peptidyl transferase 活性由大次單元 rRNA 執行。",
        "reasons": {
            "A": "大小次單元都含 rRNA，不是只有大次單元。",
            "B": "rRNA 也有催化功能，尤其 peptidyl transferase，不只結構角色。",
            "C": "大次單元由多個 rRNA 與蛋白質組成，此描述最適當，故正確。",
            "D": "peptidyl transferase 的催化核心是 rRNA，核糖體是 ribozyme，不是蛋白質執行。",
        },
        "core": "Ribosome is a ribonucleoprotein; peptidyl transferase is rRNA-catalyzed。",
    },
    88: {
        "analysis": "PDH complex 將 pyruvate 氧化脫羧為 acetyl-CoA，整體產物包括 CO2、acetyl-CoA 與 NADH。反應先脫羧釋放 CO2，再轉移乙醯基形成 acetyl-CoA，最後再生輔因子產生 NADH。",
        "reasons": {
            "A": "CO2 來自初始脫羧，應先於 acetyl-CoA 釋放，此順序不對。",
            "B": "PDH 最終還原 NAD+ 產生 NADH，不釋放 FADH2 作為產物。",
            "C": "FAD 是酵素輔因子中間傳遞電子，最終不是釋放 FADH2。",
            "D": "依序可概念化為 CO2、acetyl-CoA、NADH，故正確。",
        },
        "core": "PDH: pyruvate + CoA + NAD+ -> acetyl-CoA + CO2 + NADH。",
    },
    89: {
        "analysis": "Amylopectin 是澱粉的分支成分，由 alpha-D-glucose 以 alpha-1,4 鍵形成主鏈，並以 alpha-1,6 鍵形成分支。",
        "reasons": {
            "A": "只有 alpha-1,4 長直鏈較像 amylose，不是 amylopectin 的分支特徵。",
            "B": "beta-1,4 長直鏈是 cellulose 的特色，不是 amylopectin。",
            "C": "alpha-1,4 主鏈加 alpha-1,6 分支符合 amylopectin，故正確。",
            "D": "beta 鍵結不符合澱粉 amylopectin；澱粉為 alpha glucose polymer。",
        },
        "core": "Amylose = alpha-1,4 mostly linear；amylopectin = alpha-1,4 with alpha-1,6 branches。",
    },
    90: {
        "analysis": "可直接合成 ATP 的高能化合物包括 1,3-BPG、PEP 與 phosphocreatine。3-phosphoglycerate 不是高能磷酸供體，需先轉成 2-PG 再成 PEP。",
        "reasons": {
            "A": "1,3-bisphosphoglycerate 可經 phosphoglycerate kinase 直接產生 ATP。",
            "B": "3-phosphoglycerate 不能直接把磷酸轉給 ADP 合成 ATP，故為答案。",
            "C": "phosphocreatine 可經 creatine kinase 直接再生 ATP。",
            "D": "phosphoenolpyruvate 可經 pyruvate kinase 直接產生 ATP。",
        },
        "core": "直接 substrate-level ATP donors：1,3-BPG、PEP、phosphocreatine；3-PG 不是。",
    },
    91: {
        "analysis": "氣喘小氣道收縮的重要介質包括 cysteinyl leukotrienes，作用於 leukotriene receptors 造成支氣管收縮、黏液分泌與發炎；拮抗其受器可抑制氣喘反應。",
        "reasons": {
            "A": "COX 抑制會影響 prostaglandins，且可能在部分氣喘患者惡化 leukotriene 偏向，不是最適合標的。",
            "B": "leukotriene receptor 直接介入支氣管收縮與氣喘發炎，作為抑制小氣道收縮藥物標的最合適，故正確。",
            "C": "PGH2 是前列腺素/血栓素前驅物，不是氣喘支氣管收縮最直接可用標的。",
            "D": "phospholipase A2 位於花生四烯酸路徑上游，抑制範圍太廣，不如 leukotriene receptor 具針對性。",
        },
        "core": "氣喘可用 leukotriene receptor antagonists 減少 leukotriene-mediated bronchoconstriction。",
    },
    92: {
        "analysis": "脂膜筏是富含 cholesterol 與 sphingolipids 的膜微區，常聚集 GPI-anchored proteins 與訊號蛋白。methylated proteins 不是脂膜筏的主要組成類別。",
        "reasons": {
            "A": "cholesterol 是 lipid raft 的核心組成之一。",
            "B": "sphingolipids 與 cholesterol 共同形成較有序膜微區，是 lipid raft 特色。",
            "C": "GPI-anchored proteins 常定位於 lipid rafts，參與訊號與膜蛋白分選。",
            "D": "methylated proteins 不是 lipid raft 的主要結構組成，故為答案。",
        },
        "core": "Lipid rafts are enriched in cholesterol, sphingolipids, and GPI-anchored proteins。",
    },
    93: {
        "analysis": "飽和脂肪酸 beta-oxidation 受能量狀態與脂肪酸進入粒線體調控：malonyl-CoA 抑制 CPT1，acetyl-CoA/NADH 反映產物累積，cAMP 反映荷爾蒙動員。NADPH 主要用於還原性生合成，不是 beta-oxidation 調控核心。",
        "reasons": {
            "A": "acetyl-CoA 是 beta-oxidation 產物，累積可反映 TCA/能量狀態而影響氧化。",
            "B": "cAMP 上升促進脂解，增加脂肪酸供應，與 beta-oxidation 調節有關。",
            "C": "malonyl-CoA 抑制 CPT1，是脂肪酸進入粒線體氧化的重要調控因子。",
            "D": "NADPH 主要供脂肪酸合成與抗氧化還原反應，與飽和脂肪酸 beta-oxidation 關聯最低，故為答案。",
        },
        "core": "Beta-oxidation regulation focuses on CPT1/malonyl-CoA, substrate supply, and energy/product state; NADPH is biosynthesis-oriented。",
    },
    94: {
        "analysis": "泛素通常接到待分解蛋白質的 lysine 殘基 epsilon-amino group，而不是 arginine。泛素-蛋白酶體系統需要 ATP；自噬與溶小體也參與蛋白質迴轉。",
        "reasons": {
            "A": "ubiquitin 典型接在 lysine 殘基，不是 arginine，故為錯誤答案。",
            "B": "自噬將胞器或蛋白送往溶小體分解，胺基酸可再利用，敘述正確。",
            "C": "細菌孢子形成需要大幅蛋白質重塑與分解，涉及 protein turnover，敘述合理。",
            "D": "泛素活化與連接過程需要 ATP，敘述正確。",
        },
        "core": "Ubiquitination usually modifies lysine residues and requires ATP-dependent E1 activation。",
    },
    95: {
        "analysis": "phenylalanine 與 tyrosine 分解可產生 fumarate 與 acetoacetate。fumarate 可進入 TCA/gluconeogenesis，acetoacetate 屬酮體相關，因此兩者兼具 glucogenic 與 ketogenic。",
        "reasons": {
            "A": "若只產生 fumarate 才可稱純 glucogenic，但它們也產生 acetoacetate。",
            "B": "若只產生 acetoacetate/acetyl-CoA 才偏純 ketogenic，但它們也產生 fumarate。",
            "C": "產物包含 fumarate 與 acetoacetate，因此兼具 glucogenic 與 ketogenic，故正確。",
            "D": "acetoacetate 代表具有生酮性，說不具生酮性錯誤。",
        },
        "core": "Phe/Tyr are both glucogenic and ketogenic: fumarate + acetoacetate。",
    },
    96: {
        "analysis": "UCP1 位於棕色脂肪粒線體內膜，提供 H+ 不經 ATP synthase 回流到基質的通道，使質子梯度能量以熱散失，達到非顫抖產熱。",
        "reasons": {
            "A": "UCP1 讓氫離子回到粒線體基質、繞過 ATP synthase，故正確。",
            "B": "電子傳遞鏈仍會把 H+ 打到膜間腔；UCP1 不是阻擋這一步。",
            "C": "UCP1 不直接異位抑制 complex I/NADH dehydrogenase。",
            "D": "UCP1 不直接抑制 ATP synthase，而是提供質子旁路降低 ATP 合成耦合。",
        },
        "core": "UCP1 dissipates proton gradient by allowing H+ re-entry into mitochondrial matrix, producing heat。",
    },
    97: {
        "analysis": "本題資料疑似有題幹與選項錯位：題幹前半談粒線體細胞凋亡與 apoptosome，但目前選項是 RIA 偵測荷爾蒙類型，且與第 98 題相同。在不更動題幹、選項與答案的前提下，以下依目前選項與官方答案 B 解釋 Rosalyn Yalow 的 RIA 概念，並建議人工回查原始題目分割。",
        "reasons": {
            "A": "steroid hormones 分子小且脂溶性，雖可用免疫分析設計偵測，但 Yalow 經典 RIA 貢獻最具代表性是胰島素等 peptide hormone。",
            "B": "RIA 最早以放射標記抗原與抗體競爭結合來測定血中胰島素，屬 peptide hormone，故依目前選項 B 為答案。",
            "C": "eicosanoid hormones 是花生四烯酸衍生物，不是 Yalow RIA 經典獲獎貢獻的主要類型。",
            "D": "retinoid hormones 與維生素 A 衍生訊號相關，並非 RIA 開發偵測的代表性賀爾蒙類別。",
        },
        "core": "本題需人工回查題目分割；若依目前選項，Yalow 的 RIA 經典應用是 insulin 等 peptide hormones。",
        "notes": ["題幹疑似混入細胞凋亡題與第98題文字，選項卻為RIA荷爾蒙類型；未改題幹與選項，建議回查原始PDF。"],
    },
    98: {
        "analysis": "Rosalyn Yalow 因 radioimmunoassay（RIA）發展獲諾貝爾獎，經典應用是以放射標記抗原與抗體競爭結合，定量血中胰島素等 peptide hormones。",
        "reasons": {
            "A": "steroid hormones 可用其他免疫或質譜方法測量，但不是 Yalow RIA 經典獲獎貢獻的主要代表。",
            "B": "RIA 的代表性突破是偵測 insulin 等 peptide hormones，故正確。",
            "C": "eicosanoids 是脂質介質，不是 Yalow RIA 經典題目所指的主要荷爾蒙類型。",
            "D": "retinoids 與核受體訊號相關，不是 RIA 開發獲獎貢獻的代表類別。",
        },
        "core": "Yalow 的 RIA 經典用途是定量 insulin 等 peptide hormones。",
    },
    99: {
        "analysis": "典型細胞內 second messengers 包括 cAMP、Ca2+、IP3、DAG、cGMP 等。17 beta-estradiol 是類固醇荷爾蒙，主要作為第一訊息分子與核受體/膜受體作用，不是主要細胞內 second messenger。",
        "reasons": {
            "A": "cAMP 是 Gs/Gi 路徑常見 second messenger。",
            "B": "Ca2+ 是重要 second messenger，可調節 calmodulin、分泌與收縮等。",
            "C": "IP3 是 PLC 路徑產物，可促進內質網釋放 Ca2+，是 second messenger。",
            "D": "17 beta-estradiol 是雌激素本身，不是細胞內主要 second messenger，故為答案。",
        },
        "core": "Second messengers include cAMP, Ca2+, IP3/DAG, cGMP; steroid hormones are first messengers/ligands。",
    },
    100: {
        "analysis": "第二型限制酶通常辨認短的特定雙股 DNA 序列，多為 4-6 bp 的迴文序列，並在序列內或附近切割。",
        "reasons": {
            "A": "type II restriction enzymes 常辨認 4-6 bp 短迴文序列，故正確。",
            "B": "10-12 bp 對多數典型 type II restriction enzymes 來說過長。",
            "C": "15-20 bp 更不像典型限制酶辨認長度。",
            "D": "20-30 bp 遠超過常見 type II 限制酶辨認序列大小。",
        },
        "core": "Type II restriction enzymes usually recognize short palindromic DNA sequences, often 4-6 bp。",
    },
}


def load_questions():
    data = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    return data["questions"]


def make_update(question):
    number = question["question_number"]
    spec = SPECS[number]
    correct = question.get("correct_answer") or ",".join(question.get("correct_answers", []))
    explanation = (
        f"【題幹解析】\n{spec['analysis']}本題官方答案為 {correct}。\n\n"
        "【選項詳解】\n"
        + "\n".join(f"- {letter}. {spec['reasons'][letter]}" for letter in ("A", "B", "C", "D"))
        + f"\n\n【核心考點】\n{spec['core']}"
    )
    front = question["question_text"].replace("\n", " ")
    if len(front) > 90:
        front = front[:87] + "..."
    return {
        "question_id": question["id"],
        "question_number": number,
        "explanation": explanation,
        "key_point": spec["core"],
        "flashcard_front": front,
        "flashcard_back": spec["core"],
        "flashcard_summary": spec["core"],
        "review_status": "ai_generated",
        "explanation_model": MODEL,
        "explanation_generated_at": GENERATED_AT,
        "manual_review_notes": spec.get("notes", []),
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    questions = load_questions()
    for start in range(1, 101, 10):
        end = start + 9
        batch_questions = [q for q in questions if start <= q["question_number"] <= end]
        updates = [make_update(q) for q in batch_questions]
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates,
        }
        out = OUT_DIR / f"q{start:03d}-q{end:03d}.json"
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(out)


if __name__ == "__main__":
    missing = sorted(set(range(1, 101)) - set(SPECS))
    if missing:
        raise SystemExit(f"missing specs: {missing}")
    main()
