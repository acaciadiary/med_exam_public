import json
from datetime import datetime, timezone, timedelta
from pathlib import Path


SOURCE_FILE = "public/data/exams/114-2/medicine-1.json"
DATASET_ID = "114-2_medicine-1"
OUT_DIR = Path("scratch/rewrite_updates/114-2_medicine-1")
MODEL = "codex-high-quality-rewrite"


def make_exp(topic, stem, answer, reasons, core):
    lines = [
        "【題幹解析】",
        f"本題考點是{topic}。題目官方答案為 {answer}；判斷時要先確認題目是在問正確敘述、錯誤敘述或最不可能的選項，再把選項對回解剖位置、生理機轉或分子功能。",
        stem,
        "",
        "【選項詳解】",
    ]
    for key in ("A", "B", "C", "D"):
        lines.append(f"- {key}. {reasons[key]}")
    lines += ["", "【核心考點】", core]
    return "\n".join(lines)


R = {
    1: {
        "topic": "小腦與腦幹神經核的直接連結",
        "stem": "小腦，特別是前庭小腦，與前庭神經核有大量雙向纖維，參與平衡、眼球運動與姿勢調節。",
        "core": "前庭神經核是腦幹中與小腦連結最直接、最密切的神經核，經下小腦腳與絨球小結葉形成前庭小腦迴路。",
        "front": "哪個腦幹神經核與小腦直接大量連結？",
        "back": "前庭神經核；它與前庭小腦形成平衡與眼球運動控制迴路。",
        "reasons": {
            "A": "動眼神經核主要支配眼外肌，雖會受小腦調控，但不是與小腦大量直接連結的主要神經核。",
            "B": "三叉神經脊髓核處理臉部痛溫覺，功能屬感覺傳入，不是前庭小腦迴路的核心。",
            "C": "三叉神經橋腦核處理臉部觸壓覺，與小腦的直接連結不如前庭神經核典型。",
            "D": "前庭神經核與絨球小結葉、下小腦腳有大量連結，是本題最符合的答案。",
        },
    },
    2: {
        "topic": "初級視覺皮質的血液供應",
        "stem": "初級視覺皮質位於枕葉距狀溝周圍，主要由後大腦動脈供血。",
        "core": "primary visual cortex 位於枕葉，血液供應以 posterior cerebral artery 為主。",
        "front": "primary visual cortex 主要由哪條動脈供血？",
        "back": "後大腦動脈 posterior cerebral artery。",
        "reasons": {
            "A": "上小腦動脈供應小腦上部與部分腦幹，並非枕葉視覺皮質主要血管。",
            "B": "前大腦動脈主要供應額葉與頂葉內側面，不是初級視覺皮質主供血來源。",
            "C": "中大腦動脈主要供應大腦半球外側面；視覺皮質主區不在其典型供血範圍。",
            "D": "後大腦動脈供應枕葉與距狀溝周圍皮質，因此是正確答案。",
        },
    },
    3: {
        "topic": "基底核輸出到丘腦的投射",
        "stem": "基底核經 GPi/SNr 輸出至丘腦，再影響運動皮質；高頻考點是 VA/VL nuclei。",
        "core": "基底核主要投射到丘腦 ventral anterior 與 ventral lateral nuclei，協助調節運動計畫。",
        "front": "basal ganglia 輸出主要進入哪個丘腦核？",
        "back": "腹前側核 VA，常與腹外側核 VL 一起記。",
        "reasons": {
            "A": "腹前側核接受基底核輸出並回投運動相關皮質，是本題答案。",
            "B": "前側核屬邊緣系統/Papez circuit，與記憶情緒較相關，不是基底核主要輸出站。",
            "C": "腹後外側核接受身體軀幹四肢感覺傳入，不是基底核運動迴路核心。",
            "D": "腹後內側核接受臉部感覺與味覺傳入，不是基底核主要投射核。",
        },
    },
    4: {
        "topic": "皮質脊髓徑路徑",
        "stem": "皮質脊髓徑由運動皮質下行，經內囊後肢、中腦大腦腳、橋腦基底部、延腦錐體至脊髓。",
        "core": "corticospinal tract 通過內囊後肢，不通過內囊前肢。",
        "front": "corticospinal tract 不通過哪裡？",
        "back": "內囊前肢；它走內囊後肢。",
        "reasons": {
            "A": "延腦錐體是皮質脊髓徑下行的重要通道，故不是例外。",
            "B": "中腦基底腳含皮質脊髓徑纖維，故不是例外。",
            "C": "橋腦基底部有下行皮質脊髓徑通過，故不是例外。",
            "D": "內囊前肢主要為額橋纖維等；皮質脊髓徑走內囊後肢，所以此項正確。",
        },
    },
    5: {
        "topic": "肌腱器官傳入纖維",
        "stem": "Golgi tendon organ 偵測肌腱張力，傳入纖維是 Ib；肌梭主要是 Ia 與 II。",
        "core": "Golgi tendon organ 使用 group Ib afferent；muscle spindle primary ending 使用 group Ia。",
        "front": "Golgi tendon organ 的傳入纖維？",
        "back": "group Ib。",
        "reasons": {
            "A": "group Ia 是肌梭 primary ending 的典型傳入，不是 Golgi tendon organ。",
            "B": "group Ib 傳遞 Golgi tendon organ 的張力訊號，是正確答案。",
            "C": "Aδ 多與快痛、冷覺相關，不是肌腱器官張力傳入。",
            "D": "C fiber 多傳遞慢痛、自律神經或溫度訊號，不是此反射的主要纖維。",
        },
    },
    6: {
        "topic": "大腦皮質功能定位",
        "stem": "Broca's area 位於優勢半球額下回，屬額葉；其他選項分別在頂葉、顳葉或枕葉。",
        "core": "Broca area 在 frontal lobe；Wernicke area 多在 temporal/parietal junction。",
        "front": "哪個構造位於額葉？",
        "back": "Broca's area。",
        "reasons": {
            "A": "angular gyrus 位於頂葉下部，與閱讀、語意整合相關，非額葉。",
            "B": "Broca's area 位於額下回，是額葉語言表達區，正確。",
            "C": "Heschl transverse gyri 是初級聽覺皮質，位於顳葉。",
            "D": "cuneus 位於枕葉內側，與視覺皮質相關。",
        },
    },
    7: {
        "topic": "內耳淋巴液分布",
        "stem": "膜迷路含內淋巴液；鼓室階屬骨迷路的外淋巴液空間。",
        "core": "saccule、utricle、cochlear duct 含 endolymph；scala tympani 含 perilymph。",
        "front": "哪個內耳構造不含內淋巴液？",
        "back": "鼓室階 scala tympani。",
        "reasons": {
            "A": "球囊屬膜迷路，含內淋巴液。",
            "B": "橢圓囊屬膜迷路，含內淋巴液。",
            "C": "耳蝸管屬膜迷路，含內淋巴液。",
            "D": "鼓室階屬外淋巴液空間，所以是不含內淋巴液的選項。",
        },
    },
    8: {
        "topic": "眼外肌神經支配",
        "stem": "眼外肌記憶口訣是 LR6 SO4, others III；外直肌由外旋神經支配，不是動眼神經。",
        "core": "lateral rectus 由 CN VI；superior oblique 由 CN IV；其餘多由 CN III。",
        "front": "眼外肌神經支配的錯誤配對？",
        "back": "動眼神經支配外直肌是錯的；外直肌由 CN VI。",
        "reasons": {
            "A": "上斜肌由滑車神經支配，配對正確。",
            "B": "下斜肌由動眼神經支配，配對正確。",
            "C": "外直肌由外旋神經支配，不是動眼神經，所以此項錯誤且為答案。",
            "D": "提上眼瞼肌由動眼神經上支支配，配對正確。",
        },
    },
    9: {
        "topic": "顏面神經支配表情肌",
        "stem": "頰肌與口輪匝肌皆為表情肌，由顏面神經支配；眼外肌由第三、四、六對腦神經支配。",
        "core": "buccinator 與 orbicularis oris 都是 facial nerve 支配的表情肌。",
        "front": "頰肌與哪個肌肉同神經支配？",
        "back": "口輪匝肌，兩者皆由顏面神經支配。",
        "reasons": {
            "A": "上直肌是眼外肌，由動眼神經支配，不同於頰肌。",
            "B": "上斜肌由滑車神經支配，不同於頰肌。",
            "C": "外直肌由外旋神經支配，不同於頰肌。",
            "D": "口輪匝肌是表情肌，與頰肌同由顏面神經支配，正確。",
        },
    },
    10: {
        "topic": "骨傳導聽覺路徑",
        "stem": "骨傳導繞過外耳與部分中耳傳音構造，但仍需耳蝸、柯蒂氏器與第八腦神經完成聽覺轉換與傳導。",
        "core": "bone conduction 主要省略外聽道與鼓膜/聽小骨的空氣傳導步驟；內耳與 CN VIII 仍需正常。",
        "front": "骨傳導耳機省去的聲音傳遞構造？",
        "back": "外聽道。",
        "reasons": {
            "A": "前庭耳蝸神經仍需將聽覺訊號傳入腦幹，不能省略。",
            "B": "柯蒂氏器仍負責機械能轉換成神經訊號，不能省略。",
            "C": "耳蝸仍是骨傳導刺激的目標內耳構造，不能省略。",
            "D": "骨傳導可繞過外聽道的空氣傳導，所以此項最符合。",
        },
    },
}


MORE = {
    11: ("舌乳突一般感覺", "舌前 2/3 一般感覺由 lingual nerve；輪廓狀乳突位於舌後部，其一般感覺主要由 glossopharyngeal nerve。", "vallate papillae 最不受 lingual nerve 受損影響。", "lingual nerve 受損最不影響哪種舌乳突？", "輪廓狀乳突；主要歸 CN IX。", {"A": "輪廓狀乳突屬舌後部，主要由舌咽神經處理，因此最不受舌神經受損影響。", "B": "葉狀乳突位於舌側緣，舌前部一般感覺可受舌神經影響。", "C": "絲狀乳突多在舌前 2/3，舌神經受損會影響其一般感覺。", "D": "蕈狀乳突位於舌前部，舌神經受損會影響其一般感覺。"}),
    12: ("下頷角皮膚感覺", "耳大神經來自頸神經叢 C2-C3，支配耳下、腮腺區與下頷角附近皮膚。", "angle of mandible 附近皮膚感覺常考 great auricular nerve。", "下頷角皮膚痛覺喪失是哪條神經？", "耳大神經 great auricular nerve。", {"A": "頰神經是 V3 分支，支配頰部皮膚與黏膜感覺，不是下頷角最典型神經。", "B": "耳大神經供應下頷角與腮腺附近皮膚，正確。", "C": "枕小神經供應耳後與枕外側皮膚，不是下頷角主神經。", "D": "頦神經供應下唇與頦部皮膚，不是下頷角。"}),
    13: ("翼腭窩邊界", "翼腭窩主要與蝶骨、腭骨、上頷骨相關；顳骨不參與形成其典型邊界。", "pterygopalatine fossa 由 maxilla、palatine bone、sphenoid 等構成，不含 temporal bone。", "哪個骨不形成翼腭窩？", "顳骨 temporal bone。", {"A": "蝶骨翼突參與翼腭窩後方邊界，故不是答案。", "B": "顳骨位於顱側與中耳區，不是翼腭窩邊界，正確。", "C": "腭骨垂直板參與翼腭窩內側邊界，故不是答案。", "D": "上頷骨後面參與翼腭窩前方邊界，故不是答案。"}),
    14: ("頸前三角的肌三角內容物", "肌三角含舌骨下肌、甲狀腺、氣管等；外頸動脈位在頸動脈三角較典型。", "muscular triangle 內容物偏中線內臟與 infrahyoid muscles；external carotid artery 不在其中。", "哪個不在肌三角？", "外頸動脈。", {"A": "胸骨甲狀肌是舌骨下肌群，位於肌三角內。", "B": "甲狀腺位於頸前中線附近，屬肌三角內容物。", "C": "氣管位於頸前中線，屬肌三角相關內容。", "D": "外頸動脈位於頸動脈三角，不是肌三角內容物。"}),
    15: ("肋骨與胸椎關節", "第 11、12 肋為浮肋，通常只以肋頭與同序胸椎體關節，缺乏橫肋關節面。", "第 11 胸椎通常無 transverse costal facet，第 11 肋不與橫突形成關節。", "胸廓連接何者最恰當？", "第十一肋只以肋頭與 T11 相接。", {"A": "第一肋通常與 T1 相關，不會一般性與 C7 相接。", "B": "第九肋屬假肋，通常不直接接胸骨。", "C": "典型肋頭多與同序及上一節胸椎體關節，不是與同序胸椎下肋關節面單獨相接。", "D": "第 11 胸椎通常沒有橫肋關節面，第 11 肋以肋頭與椎體相接，正確。"}),
    16: ("心血管反射傳入", "主動脈弓壓力與化學受器訊號主要經迷走神經傳入；頸動脈竇則經舌咽神經。", "cardiac reflex 的重要 visceral afferent 可經 vagus nerve 進入中樞。", "血壓與血液化學變化傳入心臟反射的神經？", "迷走神經 vagus nerve。", {"A": "迷走神經可傳遞主動脈弓壓受器與化學受器訊號，正確。", "B": "頸部交感神經主要是交感傳出路徑，不是此反射的主要感覺傳入。", "C": "胸部交感神經偏向交感傳出，不是血壓化學感受器主要傳入。", "D": "胸部內臟神經多與交感內臟傳出/痛覺傳入相關，不是此處最佳答案。"}),
    17: ("心包橫竇位置", "心包橫竇位於升主動脈、肺動脈幹後方，上腔靜脈前方；外科上可用手指通過此處夾住大動脈。", "transverse pericardial sinus 在 arterial outflow 後方、SVC 前方。", "心包橫竇最恰當位置？", "位在上腔靜脈前方。", {"A": "心包橫竇在上腔靜脈前方，且在主動脈與肺動脈幹後方，正確。", "B": "肺靜脈後方較接近斜竇相關位置，不是橫竇。", "C": "左心房下方不是橫竇的典型描述。", "D": "橫竇不是夾在肺動脈幹與主動脈之間，而是在兩者後方。"}),
    18: ("冠狀動脈供血區", "題目問最不可能造成左心房、左心室前側壁、心尖與室間隔缺氧者；右邊緣支主要供應右心室。", "right marginal branch 供應右心室，與左室前壁、側壁、心尖和中隔較不相干。", "哪條栓塞最不可能造成題述左心缺氧？", "右邊緣支。", {"A": "前室間支供應左室前壁、心尖與前 2/3 室間隔，可能造成題述缺氧。", "B": "後室間支可供應室間隔後部與鄰近心室壁，仍可能影響部分區域。", "C": "右邊緣支主要供應右心室游離壁，最不符合題述左心區域，正確。", "D": "左迴旋支供應左心房與左室側壁，可能造成題述區域缺氧。"}),
    19: ("腸繫膜與腹膜關係", "下降部十二指腸多為次級後腹膜構造，無典型腸繫膜；闌尾、乙狀結腸、橫結腸都有繫膜。", "descending duodenum 是 retroperitoneal，通常沒有 mesentery。", "哪個不具備腸繫膜？", "十二指腸下降段。", {"A": "十二指腸下降段多固定於後腹壁，屬次級後腹膜，沒有自由腸繫膜，正確。", "B": "闌尾有闌尾繫膜 mesoappendix。", "C": "乙狀結腸有 sigmoid mesocolon。", "D": "橫結腸有 transverse mesocolon。"}),
    20: ("胃大彎動脈來源", "左胃網膜動脈沿胃大彎走行，來自脾動脈；右胃網膜動脈來自胃十二指腸動脈。", "left gastroepiploic artery 是 splenic artery 的分支。", "左胃網膜動脈來自哪條？", "脾動脈。", {"A": "總肝動脈會經胃十二指腸動脈供應右胃網膜動脈，不是左胃網膜動脈直接來源。", "B": "左胃動脈主要沿小彎走行，不是左胃網膜動脈來源。", "C": "後胃動脈可來自脾動脈供應胃後壁，但不是左胃網膜動脈。", "D": "左胃網膜動脈來自脾動脈，正確。"}),
    21: ("臍皺襞內容物", "medial umbilical fold 由閉鎖後的臍動脈形成；median umbilical fold 是 urachus。", "medial umbilical fold = obliterated umbilical artery。", "臍內側韌帶包覆何結構？", "臍動脈遺跡。", {"A": "輸精管在腹股溝管與骨盆內走行，不形成臍內側皺襞。", "B": "閉鎖的臍動脈被腹膜覆蓋形成臍內側皺襞，正確。", "C": "上腹壁動脈形成外側臍皺襞，不是內側臍皺襞。", "D": "肝靜脈不在前腹壁形成此皺襞。"}),
    22: ("前腹壁淺筋膜", "前下腹壁淺筋膜分兩層：淺層脂肪性 Camper fascia、深層膜性 Scarpa fascia。", "皮下脂肪主要在 Camper's fascia。", "前下腹壁皮下脂肪在哪層？", "Camper's fascia。", {"A": "Camper's fascia 是脂肪層，正確。", "B": "Scarpa's fascia 是膜性層，脂肪較少。", "C": "腹橫筋膜在腹肌深面，不是皮下脂肪層。", "D": "闊筋膜是大腿深筋膜，不是前下腹壁皮下層。"}),
    23: ("前列腺血供與解剖", "前列腺主要由下膀胱動脈等內髂系統分支供血；上膀胱動脈不是最主要來源。", "prostate 主要血供不是 superior vesical artery。", "前列腺何者錯誤？", "主要來自上膀胱動脈是錯的。", {"A": "前列腺含腺體與纖維肌肉基質，敘述正確。", "B": "前列腺後方鄰近直腸，可經直腸指診觸診，正確。", "C": "主要血供通常來自下膀胱動脈等分支，不是上膀胱動脈，此項錯誤。", "D": "前列腺靜脈叢與膀胱靜脈叢相通，敘述正確。"}),
    24: ("陰莖深背靜脈回流", "陰莖深背靜脈走在 Buck fascia 深層，進入骨盆後回流至前列腺靜脈叢。", "deep dorsal vein of penis drains to prostatic venous plexus。", "陰莖深背靜脈何者正確？", "進入骨盆後注入前列腺靜脈叢。", {"A": "陰莖皮膚主要由淺背靜脈收集，不是深背靜脈主要工作。", "B": "深背靜脈位於 Buck fascia 深層，不是淺層。", "C": "其通過深會陰筋膜/恥骨弓下方進入骨盆，選項所述 fundiform ligament 不是最佳描述。", "D": "深背靜脈回流到前列腺靜脈叢，正確。"}),
    25: ("男性會陰肌肉功能", "球海綿體肌可壓迫尿道球，協助射精與排尿後排出殘尿；坐骨海綿體肌壓迫陰莖腳以維持勃起。", "bulbospongiosus helps empty residual urine from spongy urethra。", "男性會陰肌何者正確？", "球海綿體肌排尿後協助排出尿道殘尿。", {"A": "壓迫陰莖球主要是球海綿體肌；坐骨海綿體肌作用在陰莖腳以維持勃起。", "B": "球海綿體肌收縮可擠壓海綿體尿道，排出殘尿，正確。", "C": "坐骨海綿體肌附著於坐骨支與陰莖腳，不是會陰體。", "D": "會陰淺橫肌附著於坐骨支與會陰體，不是坐骨棘。"}),
    26: ("膀胱自律神經", "膀胱副交感來自 pelvic splanchnic nerves S2-S4；sacral splanchnic nerves 是交感性質。", "pelvic splanchnic 是副交感；sacral splanchnic 是交感。", "膀胱神經支配何者錯誤？", "薦內臟神經含副交感纖維是錯的。", {"A": "下腹神經含交感纖維，參與儲尿功能，正確。", "B": "薦內臟神經為交感纖維；副交感是骨盆內臟神經，此項錯誤。", "C": "交感刺激內尿道括約肌收縮，有助儲尿，正確。", "D": "副交感促進逼尿肌收縮以排尿，正確。"}),
    27: ("鎖骨下動脈分支", "內胸動脈是鎖骨下動脈第一段的直接分支；其他多屬腋動脈分支。", "internal thoracic artery directly branches from subclavian artery。", "哪個是鎖骨下動脈直接分支？", "內胸動脈。", {"A": "上胸動脈通常來自腋動脈第一段，不是鎖骨下動脈直接分支。", "B": "外胸動脈來自腋動脈第二段，不是直接分支。", "C": "內胸動脈直接來自鎖骨下動脈，正確。", "D": "胸肩峰動脈來自腋動脈第二段，不是鎖骨下動脈直接分支。"}),
    28: ("大腿前肌群作用", "大腿前肌群主要屈髖、伸膝，部分肌肉可外旋；伸髖主要由臀大肌與後肌群負責。", "anterior thigh muscles do not primarily extend hip。", "哪個不是大腿前肌群作用？", "伸直髖關節。", {"A": "髂腰肌與股直肌等可屈曲髖關節，是前肌群功能。", "B": "縫匠肌可屈曲、外展、外旋大腿，仍屬前內側相關功能。", "C": "股四頭肌伸直膝關節，是大腿前肌群核心功能。", "D": "伸髖主要靠臀大肌與腘旁肌群，不是大腿前肌群功能。"}),
    29: ("上肢皮節/皮神經圖像判讀", "題目依圖中黑色陰影判定表皮感覺來源，官方答案為橈神經；常見陰影可能在手背橈側或前臂後外側。", "radial nerve supplies dorsal radial hand and posterior arm/forearm skin areas。", "圖中陰影區皮膚感覺神經？", "橈神經。", {"A": "正中神經主要支配掌側橈側三指半與指端背側，不符合官方圖示判讀。", "B": "肌皮神經末梢為外側前臂皮神經，範圍較侷限，不是官方答案。", "C": "橈神經支配手背橈側與上肢後側多處皮膚，符合官方答案。", "D": "尺神經支配手掌/手背尺側一指半，與官方圖示不符。"}, ["題目依圖片陰影判讀；本資料未含圖片，已依官方答案與常見橈神經皮區重寫。"]),
    30: ("股骨內收結節位置", "adductor tubercle 位於股骨內上髁上方，是大收肌附著的重要標誌。", "adductor tubercle is superior to medial epicondyle。", "股骨內收結節位於何處？", "內上髁上方。", {"A": "大轉子位於股骨近端外側，不是內收結節位置。", "B": "內收結節位於內上髁上方，正確。", "C": "外上髁在膝外側，不是內收肌群附著標誌。", "D": "小轉子位於股骨近端後內側，不是內收結節。"}),
}


MORE.update({
    31: ("膕動脈分支", "膕動脈分出上、中、下膝動脈；降膝動脈通常來自股動脈。", "descending genicular artery is from femoral artery, not popliteal artery。", "哪個不是膕動脈分支？", "降膝動脈。", {"A": "降膝動脈來自股動脈遠端，不是膕動脈分支，正確。", "B": "上膝動脈是膕動脈膝關節吻合分支之一。", "C": "中膝動脈是膕動脈分支，供應膝關節內部。", "D": "下膝動脈也是膕動脈分支。"}),
    32: ("神經嵴衍生物", "神經嵴衍生黑色素細胞、周邊自律神經元、腎上腺髓質嗜鉻細胞；甲狀腺濾泡細胞來自內胚層。", "thyroid follicular cells are endoderm-derived, not neural crest。", "何者不是 neural crest 衍生？", "甲狀腺濾泡細胞。", {"A": "黑色素細胞為神經嵴衍生，故不是答案。", "B": "交感節後神經元為神經嵴衍生，故不是答案。", "C": "甲狀腺濾泡細胞來自咽底內胚層，不是神經嵴，正確。", "D": "腎上腺髓質嗜鉻細胞為神經嵴衍生，故不是答案。"}),
    33: ("舌發育與咽弓", "第二咽弓形成 copula，但後來被第三咽弓形成的 hypopharyngeal eminence 覆蓋而消失。", "copula 來自第二咽弓，最後被第三咽弓衍生構造取代。", "哪個咽弓形成 copula？", "第二咽弓。", {"A": "第一咽弓形成舌前 2/3 的 lateral lingual swellings 與 tuberculum impar，不是 copula。", "B": "第二咽弓形成 copula，之後被擠壓消失，正確。", "C": "第三咽弓形成舌後 1/3 主要部分，不是 copula。", "D": "第四咽弓與會厭附近/舌根後部相關，不是 copula。"}),
    34: ("陰道發育來源", "陰道上部與副中腎管相關，下部由尿殖竇形成的 sinovaginal bulbs 參與。", "vagina develops from paramesonephric duct and sinovaginal bulb。", "陰道由哪兩構造形成？", "副中腎管與竇陰道球泡。", {"A": "中腎管是男性生殖管道來源，不是陰道主要來源。", "B": "中腎管不構成女性陰道主要來源。", "C": "副中腎管與竇陰道球泡共同形成陰道，正確。", "D": "生殖結節形成陰蒂/陰莖等外生殖器，不是陰道。"}),
    35: ("臍韌帶胚胎遺跡", "medial umbilical ligament 是閉鎖臍動脈；round ligament of liver 才是臍靜脈遺跡。", "medial umbilical ligament = obliterated umbilical artery。", "內側臍韌帶是何遺跡？", "臍動脈。", {"A": "內側臍韌帶由臍動脈閉鎖形成，正確。", "B": "臍靜脈遺跡是肝圓韌帶。", "C": "靜脈導管遺跡是靜脈韌帶。", "D": "動脈導管遺跡是動脈韌帶。"}),
    36: ("神經垂體胚胎來源", "神經垂體是下視丘向下延伸，屬間腦神經外胚層；腺垂體來自 Rathke pouch。", "neurohypophysis derives from diencephalon。", "神經垂體衍生自哪裡？", "間腦。", {"A": "端腦形成大腦半球等，不是神經垂體來源。", "B": "神經垂體由間腦下視丘延伸而來，正確。", "C": "中腦不形成神經垂體。", "D": "髓腦形成延腦相關構造，不是神經垂體。"}),
    37: ("上皮細胞側面接合", "tight junction、adherens junction、gap junction 在側面；hemidesmosome 位於基底面連接基底膜。", "hemidesmosome is basal domain, not lateral domain。", "哪個不在上皮側面？", "半橋粒。", {"A": "間隙接合位於細胞側面，允許細胞間溝通。", "B": "黏連接合位於側面，連接 actin cytoskeleton。", "C": "半橋粒位於基底面，連接基底膜，正確。", "D": "緊密接合位於頂端側面，形成屏障。"}),
    38: ("骨骼肌 triad", "骨骼肌 triad 由一條 T 小管與兩個 terminal cisternae 組成，位於 A-I junction。", "skeletal muscle triad is at A-I junction。", "成熟骨骼肌何者正確？", "triad 分布於 A-I junction。", {"A": "骨骼肌細胞不是靠 gap junction 同步收縮；心肌才有 intercalated disc 與 gap junction。", "B": "終池是肌漿網膨大，不是細胞膜內凹；T 小管才是肌膜內凹。", "C": "triad 是一條 T 小管加兩個終池，不是一個終池加兩條 T 小管。", "D": "骨骼肌 triad 位於 A-I junction，正確。"}),
    39: ("關節軟骨特性", "關節面軟骨為透明軟骨，但缺乏軟骨膜，靠滑液與下方骨供應。", "articular cartilage lacks perichondrium。", "關節面軟骨不存在何者？", "軟骨膜。", {"A": "關節軟骨沒有軟骨膜，正確。", "B": "玻尿酸存在於基質與滑液中，與關節潤滑相關。", "C": "關節面軟骨為透明軟骨。", "D": "透明軟骨可見同源細胞群。"}),
    40: ("骨化方式", "長骨主要經軟骨內骨化，會有初級與次級骨化中心；扁平骨多為膜內骨化。", "long bones have primary and secondary ossification centers in endochondral ossification。", "骨生成何者正確？", "長骨軟骨內骨化有初級與次級骨化中心。", {"A": "扁平骨主要經膜內骨化，不是軟骨內骨化。", "B": "骨小樑增厚屬 appositional growth，不是間質性生長。", "C": "長骨軟骨內骨化出現初級與次級骨化中心，正確。", "D": "肥大軟骨區被礦化並由細胞作用重塑；選項說 osteoclast 在肥大區分解骨質不精確。"}),
    41: ("神經元形態", "自主神經節內節後神經元多為 multipolar neuron；感覺神經節多為 pseudounipolar。", "sympathetic ganglion neurons are multipolar。", "交感神經節神經元形態？", "多極型神經元。", {"A": "交感神經節內的節後神經元多為多極型，正確。", "B": "雙極型神經元多見於特殊感覺如嗅覺、視網膜與前庭耳蝸系統。", "C": "偽單極神經元典型在背根神經節與部分腦神經感覺節。", "D": "交感神經節不是偽單極與雙極混合為主。"}),
    42: ("嗅覺上皮細胞", "嗅覺上皮含嗅覺受器神經元、支持細胞、基底細胞與刷狀細胞；杯狀細胞是呼吸上皮常見。", "olfactory epithelium lacks goblet cells。", "哪種細胞最不可能在嗅覺上皮？", "杯狀細胞。", {"A": "支持細胞是嗅覺上皮成分。", "B": "基底細胞是嗅覺上皮幹/再生細胞。", "C": "刷狀細胞可出現在嗅覺上皮。", "D": "杯狀細胞典型屬呼吸上皮，不是嗅覺上皮成分，正確。"}),
    43: ("小腸與結腸組織特徵", "villi、lacteal、plicae circulares 是小腸特徵；teniae coli 是大腸特徵。", "teniae coli belongs to colon, not small intestine。", "何者不與其他三者同器官？", "結腸帶。", {"A": "絨毛是小腸吸收構造。", "B": "乳糜管位於小腸絨毛內，吸收脂質。", "C": "環皺襞是小腸增加表面積的構造。", "D": "結腸帶是大腸縱走肌束，與前三者不在同一器官。"}),
    44: ("表皮蘭氏細胞", "Langerhans cell 是表皮樹突狀抗原呈現細胞，多在 stratum spinosum。", "Langerhans cells are antigen-presenting dendritic cells in epidermis。", "蘭氏細胞何者正確？", "抗原呈現細胞。", {"A": "蘭氏細胞不是均勻分布於五層表皮。", "B": "較常見於棘狀層，不是基底層。", "C": "蘭氏細胞是抗原呈現細胞，正確。", "D": "機械受器是 Merkel cell 等概念，不是 Langerhans cell。"}),
    45: ("甲狀腺濾泡", "甲狀腺濾泡由濾泡細胞圍繞膠體構成，是合成與儲存甲狀腺素的基本單位。", "thyroid follicle = follicular cells surrounding colloid。", "甲狀腺濾泡何者正確？", "濾泡細胞圍繞膠體形成基本構造單位。", {"A": "濾泡大小會隨功能狀態而變，不是大小相似且直徑約 2 mm。", "B": "濾泡細胞圍繞膠體形成甲狀腺基本構造單位，正確。", "C": "thyroglobulin 在膠體側碘化，不是在細胞內完成後才送入膠體。", "D": "降鈣素由濾泡旁 C cells 分泌，不是濾泡細胞主要功能。"}),
    46: ("前列腺組織學", "前列腺是 tubuloalveolar gland；前列腺癌多在 peripheral zone，BPH 常在 transitional zone。", "prostate gland is a tubuloalveolar gland。", "前列腺何者正確？", "屬管泡腺。", {"A": "前列腺凝結體多隨年齡增加，男嬰不會常見大量鈣化凝結體。", "B": "前列腺癌最常發生於 peripheral zone，不是 transitional zone。", "C": "peripheral zone 通常是最大腺體區，central zone 不是最大。", "D": "前列腺腺體屬 tubuloalveolar gland，正確。"}),
    47: ("滲透壓與尿素穿透性", "紅血球在含可穿透溶質尿素的低有效滲透壓溶液中最易脹大；尿素進入細胞後水跟著進入。", "urea is permeant, so 100 mM NaCl + urea has low tonicity and swells RBC。", "紅血球在哪種溶液最易脹大？", "100 mM NaCl + 200 mM 尿素。", {"A": "NaCl 與 KCl 多為有效滲透粒子，總張力偏高，不易脹大。", "B": "尿素可穿透紅血球膜，外液有效張力主要剩 100 mM NaCl，細胞易吸水脹大。", "C": "葡萄糖相對較能維持有效滲透壓，較不如尿素造成脹大。", "D": "100 mM NaCl + 100 mM 葡萄糖有效張力也偏低，但不如尿素穿透後造成的脹大典型。"}),
    48: ("終板電位與肉毒毒素", "EPP 由 ACh 作用於 nicotinic receptor 造成局部去極化；botulinum toxin 抑制 ACh 釋放使 EPP 變小。", "botulinum toxin blocks ACh release, reducing EPP and causing flaccid paralysis。", "EPP 何者最適當？", "肉毒毒素使 ACh 釋放下降，EPP 變小。", {"A": "骨骼肌神經肌肉接合處是 nicotinic receptor，不是 muscarinic receptor。", "B": "EPP 是局部終板電位，主要來自 Na+ 內流，不是 K+ 大量流入造成的動作電位。", "C": "沿 T 小管傳遞的是肌膜動作電位，不是 EPP 本身。", "D": "肉毒毒素抑制運動神經末梢釋放 ACh，使 EPP 變小並造成無力，正確。"}),
    49: ("語言區病灶", "講話流利但理解/閱讀困難偏向 Wernicke aphasia；Broca 病灶則語言不流利。", "fluent speech with impaired comprehension/reading suggests Wernicke area lesion。", "流利但閱讀困難病灶？", "Wernicke's area。", {"A": "Wernicke 區病灶可造成流利但理解與閱讀障礙，最符合。", "B": "Broca 區病灶造成非流利型失語。", "C": "angular gyrus 可造成失讀失寫，但題幹強調流利語言與理解障礙時 Wernicke 較典型。", "D": "arcuate fasciculus 病灶典型為傳導性失語，複誦障礙突出。"}),
    50: ("恐懼情緒神經迴路", "杏仁核與恐懼制約、威脅評估與情緒反應最直接相關。", "amygdala is the key structure for fear emotion。", "哪個腦區最直接相關恐懼？", "杏仁核。", {"A": "視上核主要與 ADH/oxytocin 神經分泌相關。", "B": "視叉上核是生理時鐘核心，不是恐懼中樞。", "C": "杏仁核負責恐懼與威脅相關情緒處理，正確。", "D": "海馬迴主要與記憶形成與空間記憶相關。"}),
})


MORE.update({
    51: ("自主神經系統分部", "交感是胸腰部 thoracolumbar；副交感是頭薦部 craniosacral。", "sympathetic is thoracolumbar, not craniosacral。", "自主神經何者最不適當？", "交感稱為頭薦部門是錯的。", {"A": "頭薦部門是副交感，不是交感，此項錯誤。", "B": "交感節前神經元釋放 ACh，正確。", "C": "多數副交感節後神經元釋放 ACh，正確。", "D": "副交感神經節通常靠近或位於標的器官，正確。"}),
    52: ("代謝型受體", "α1 adrenergic receptor 是 norepinephrine 的 Gq 型代謝型受體；nicotinic 與 AMPA 是離子型受體。", "norepinephrine paired with alpha-1 receptor is metabotropic。", "神經傳導物質與代謝型受體正確配對？", "norepinephrine -> alpha-1 receptor。", {"A": "norepinephrine 可作用於 α1 receptor，屬 GPCR，正確。", "B": "5-HT1 是 serotonin 受體，不是 histamine 受體。", "C": "nicotinic receptor 是配體閘門離子通道，不是代謝型受體。", "D": "AMPA receptor 是離子型 glutamate receptor，不是代謝型受體。"}),
    53: ("前庭直線加速度", "球囊主要感受垂直方向線性加速度；橢圓囊偏水平線性加速度；半規管感受角加速度。", "saccule senses vertical linear acceleration。", "垂直加速主要靠哪個構造？", "球囊。", {"A": "半規管偵測旋轉角加速度，不是垂直線性加速度。", "B": "橢圓囊偏水平線性加速度。", "C": "球囊對垂直線性加速度最重要，正確。", "D": "柯蒂氏器是聽覺受器，不是前庭加速度受器。"}),
    54: ("副交感與調視", "副交感使瞳孔縮小、睫狀肌收縮、懸韌帶放鬆、水晶體變圓變厚以看近物。", "parasympathetic accommodation makes lens thicker, not thinner/longer。", "副交感興奮眼球何者最不可能？", "水晶體變薄變長。", {"A": "睫狀體環肌收縮是副交感調視反應。", "B": "睫狀肌收縮使懸韌帶張力下降。", "C": "水晶體會變圓變厚，不會變薄變長，此項最不可能。", "D": "副交感使瞳孔括約肌收縮，瞳孔變小。"}),
    55: ("運動初期 ATP 來源", "開始運動最初數秒主要靠肌肉內 creatine phosphate 快速再生 ATP。", "first seconds of exercise use creatine phosphate。", "運動最初數秒 ATP 來源？", "磷酸肌酸。", {"A": "脂肪酸氧化供能慢，較適合長時間運動。", "B": "葡萄糖分解可供短中期能量，但不是最初幾秒最快來源。", "C": "蛋白質不是正常短時間運動主要能量來源。", "D": "磷酸肌酸可快速把磷酸轉給 ADP，是最初幾秒主要 ATP 來源。"}),
    56: ("骨骼肌纖維型態", "2X 型是快速糖解型，收縮快但粒線體、肌紅蛋白、微血管較少，容易疲勞。", "type 2X fibers fatigue faster than type I fibers。", "2X 與第 1 型相比何者不同？", "2X 較容易疲勞。", {"A": "2X 粒線體較少；第 1 型氧化能力較強。", "B": "2X 型快速但較易疲勞，正確。", "C": "第 1 型肌紅蛋白較多，不是 2X。", "D": "第 1 型微血管較豐富，不是 2X。"}),
    57: ("纖維蛋白溶解", "溶栓是 plasminogen 轉為 plasmin 後分解 fibrin；可溶性 fibrin fragments 是分解產物，不會聚集成 fibrin。", "fibrin fragments are breakdown products, not building blocks of fibrin。", "血栓溶解何者錯誤？", "可溶性纖維蛋白片段聚集成 fibrin 是錯的。", {"A": "內皮細胞分泌 tPA，正確。", "B": "plasminogen 需活化成 plasmin 才能分解 fibrin，正確。", "C": "可溶性 fibrin fragments 是 fibrin 被分解後產物，不是聚集成 fibrin，此項錯誤。", "D": "fibrin 可促進 tPA 對 plasminogen 的活化效率，正確。"}),
    58: ("ECG 判讀", "高血鉀典型可見 tall peaked T waves；一度 AV block 是 PR 延長，不是縮短。", "hyperkalemia commonly causes tall T waves in lead II when calcium is normal。", "ECG 描述何者最適當？", "高血鉀 lead II 常見高 T 波。", {"A": "高血鉀可造成高尖 T 波，正確。", "B": "一度房室傳導阻斷為 PR interval 延長，不是縮短。", "C": "aVR 通常與 lead II 方向相反，QRS 多不相似向上。", "D": "胸前導程 T 波不會全部正常向下；多數左胸導程 T 波應向上。"}),
    59: ("心室肌動作電位 phase 1", "phase 1 初期快速再極化來自 fast Na+ channel 關閉與 transient outward K+ current 開啟。", "initial rapid repolarization: Na channels close, K channels open。", "去極化與平原期之間快速再極化機制？", "關閉鈉通道、打開鉀通道。", {"A": "Na+ 通道關閉、K+ 外流增加造成 phase 1，正確。", "B": "Cl- 通道不是心室肌 phase 1 的主要機制。", "C": "L-type Ca2+ 打開與 plateau 相關，不是關閉後打開 T-type。", "D": "T-type/L-type 轉換不是此階段主要機制。"}),
    60: ("心室肌與竇房結動作電位", "兩者再極化都依賴 K+ 外流；但 SA node 無穩定 -90 mV 靜止電位，去極化主要為 Ca2+。", "repolarization in both ventricular myocytes and SA node cells is mainly K+ efflux。", "心室肌與 SA node 比較何者適當？", "再極化主要都是 K+ 通道開啟。", {"A": "SA node 沒有穩定 -90 mV resting potential。", "B": "SA node 動作電位沒有典型心室肌 plateau。", "C": "SA node phase 0 主要靠 Ca2+ influx，不是 fast Na+。", "D": "兩者再極化皆主要靠 K+ 外流，正確。"}),
    61: ("Cushing reflex", "顱內壓上升可造成 Cushing response：血壓上升、反射性心跳下降，常合併呼吸異常。", "increased ICP -> hypertension with bradycardia。", "顱內壓上升最易見何變化？", "血壓上升、心跳下降。", {"A": "血壓下降不符合典型 Cushing response。", "B": "血壓上升且心跳速率下降最符合 Cushing reflex。", "C": "心跳上升不是典型反射結果。", "D": "血壓下降、心跳上升較像休克代償，不是顱壓上升典型。"}),
    62: ("Fick principle 氧含量", "全身耗氧 250 mL/min、心輸出 5 L/min，動靜脈氧差為 50 mL/L；動脈 200 mL/L，靜脈約 150 mL/L。", "CvO2 = CaO2 - VO2/CO = 200 - 250/5 = 150 mL/L。", "體靜脈血氧濃度最接近？", "150 mL/L。", {"A": "150 mL/L 符合 Fick 計算，正確。", "B": "146 mL/L 可能混入血紅素結合量計算，但題目可直接用總氧含量與耗氧量。", "C": "143 mL/L 低估靜脈氧含量。", "D": "47 mL/L 過低，不符合正常心輸出下耗氧差。"}),
    63: ("通氣量調控", "高 CO2 是強烈通氣刺激，低 O2 也刺激周邊化學受器；兩者合併時 minute ventilation 最大。", "5% O2 + 5% CO2 gives strongest ventilatory drive。", "哪種吸入氣使總通氣量最大？", "5% O2 + 5% CO2。", {"A": "接近正常氧且 CO2 很低，通氣刺激小。", "B": "低氧可增加通氣，但 CO2 低時刺激不如合併高 CO2。", "C": "高 CO2 可明顯刺激通氣，但氧氣正常。", "D": "低氧加高 CO2 同時刺激周邊與中樞化學受器，通氣量最大。"}),
    64: ("膽固醇吸收", "游離膽固醇為脂溶性分子，小腸吸收以被動擴散/載體輔助擴散概念為主，考題答案取 diffusion。", "free cholesterol absorption is mainly diffusion from micelles into enterocytes。", "游離膽固醇如何吸收？", "擴散作用。", {"A": "不是以 ATP 驅動的初級主動運輸為主。", "B": "不是典型鈉梯度次級主動運輸。", "C": "游離膽固醇由微膠粒到小腸上皮主要靠擴散進入，正確。", "D": "內吞不是本題主要機制。"}),
    65: ("secretin 作用", "secretin 由十二指腸 S cells 分泌，促進胰臟與膽道 HCO3- 分泌，並抑制胃酸/胃泌素相關分泌。", "secretin stimulates pancreatic bicarbonate and inhibits gastric secretion/gastrin。", "secretin 最主要直接作用？", "促胰臟碳酸氫根分泌並抑制 gastrin。", {"A": "膽囊收縮主要是 CCK 功能，不是 secretin 最主要作用。", "B": "促膽囊收縮仍偏 CCK。", "C": "刺激胰臟 HCO3- 分泌並抑制胃腺 gastrin，最符合 secretin。", "D": "促胃酸 HCl 分泌不是 secretin 作用。"}),
    66: ("腎臟滲透壓調節", "正常尿液可被稀釋至約 50 mOsm/L，也可濃縮至約 1200 mOsm/L；ADH 作用在集合管。", "urine osmolality can range roughly 50 to 1200 mOsm/L。", "腎滲透壓調節何者適當？", "尿液可低至 50、高至 1200 mOsm/L。", {"A": "血漿滲透壓升高才刺激 ADH，低於 280 不會刺激。", "B": "口渴閾值通常高於 ADH 分泌閾值。", "C": "ADH 主要增加集合管水通透性，不是近端小管。", "D": "正常腎臟可大幅稀釋與濃縮尿液，範圍約 50 到 1200 mOsm/L，正確。"}),
    67: ("亨氏環水分再吸收", "厚上行支是稀釋段，不透水，主要靠 NKCC2 再吸收 Na-K-2Cl，不是 Na-Cl cotransporter 且不再吸水。", "thick ascending limb is water-impermeable and uses NKCC2。", "腎小管水分再吸收何者錯誤？", "厚上行支因 Na-Cl cotransporter 再吸收水分是錯的。", {"A": "下降支有 AQP1，對水高度通透，正確。", "B": "厚上行支不透水，且主要 transporter 是 NKCC2，不是 NCC，此項錯誤。", "C": "基底外側 Na-K ATPase 提供鈉再吸收驅動力；但水不跟隨厚上行支通過。", "D": "離開厚上行支進入遠端小管的管液呈低張，正確。"}),
    68: ("胰島素代謝作用", "胰島素促進葡萄糖利用、肝醣與脂肪合成，抑制糖質新生、脂解與生酮。", "insulin promotes lipogenesis in adipose tissue。", "胰島素何者最適當？", "促進脂肪組織脂肪合成。", {"A": "高血鉀較會刺激胰島素分泌，低血鉀不是促進因子。", "B": "胰島素抑制肝臟葡萄糖產生。", "C": "胰島素促進脂肪組織脂肪合成，正確。", "D": "胰島素抑制 ketogenesis，不是促進。"}),
    69: ("醣蛋白荷爾蒙 alpha 次單元", "TSH、LH、FSH、hCG 共享 alpha subunit，差異在 beta subunit。", "TSH shares alpha subunit with LH, FSH, and hCG。", "哪兩個與 TSH 有相同 alpha subunit？", "LH 與 hCG。", {"A": "GH 與 prolactin 不是與 TSH 同族的醣蛋白荷爾蒙。", "B": "FSH 是同族，但 ACTH 不是；配對不全對。", "C": "ADH 與 oxytocin 是神經垂體胜肽，不是此 alpha subunit 家族。", "D": "LH 與 hCG 都與 TSH 共享 alpha subunit，正確。"}),
    70: ("壓力軸荷爾蒙", "壓力刺激下視丘分泌 CRH，再刺激腦下垂體分泌 ACTH；下視丘不直接分泌 ACTH。", "hypothalamus secretes CRH, not ACTH。", "荷爾蒙分泌何者最不適當？", "壓力使下視丘分泌 ACTH 是錯的。", {"A": "嚴重低血糖可刺激腎上腺素分泌，正確。", "B": "壓力使 HPA axis 活化，cortisol 增加，正確。", "C": "ACTH 由腦下垂體前葉分泌；下視丘分泌 CRH，此項錯誤。", "D": "ACTH 分泌受晝夜節律調控，正確。"}),
})


MORE.update({
    71: ("beta 細胞葡萄糖感應", "胰臟 beta 細胞以 GLUT-2 與 glucokinase 感應血糖，啟動 ATP/KATP/Ca2+ 路徑分泌 insulin。", "GLUT-2 is key for beta-cell glucose sensing。", "beta 細胞無法感應血糖最可能缺失？", "GLUT-2。", {"A": "GLUT-2 是 beta 細胞葡萄糖進入與感應的重要分子，缺失會降低 insulin 分泌。", "B": "葡萄糖-鈣反向運輸不是 beta 細胞感糖的標準分子。", "C": "葡萄糖-氯反向運輸不是此路徑核心。", "D": "葡萄糖-胺基酸共同運輸不是 beta 細胞主要血糖感應機制。"}),
    72: ("副甲狀腺切除後低鈣", "PTH 缺乏造成低血鈣、高血磷、腸鈣吸收下降；低鈣會增加神經肌肉興奮性，不會下降。", "hypocalcemia increases neuromuscular excitability。", "副甲狀腺切除後最不可能？", "神經肌肉興奮性下降。", {"A": "PTH 下降使腎臟排磷下降，血磷上升可能發生。", "B": "低血鈣會使神經肌肉興奮性上升，不是下降，因此最不可能。", "C": "PTH 缺乏使活性維生素 D 減少，腸鈣吸收下降。", "D": "PTH 缺乏造成血鈣下降。"}),
    73: ("卵巢濾泡發育", "primordial follicle 在出生前已形成，青春期後是在 FSH 影響下開始週期性募集，而非青春期才形成初級濾泡的起點。", "primordial follicles are present before puberty; recruitment occurs cyclically after puberty。", "濾泡生長何者最不適當？", "原始濾泡至青春期才開始發育形成初級濾泡的說法過度簡化。", {"A": "原始濾泡在胎兒/出生前已存在，並非到青春期才有最早期濾泡發育概念，此項最不適當。", "B": "初級濾泡形成 zona pellucida，是正確特徵。", "C": "月經週期中會募集多個濾泡並選出 dominant follicle，正確。", "D": "atresia 可發生於各發育階段，正確。"}),
    74: ("胜肽鍵數量", "n 個胺基酸形成一條線性多肽時有 n-1 個胜肽鍵；12 個胺基酸有 11 個。", "peptide bonds = amino acids - 1。", "12 胺基酸多肽有幾個胜肽鍵？", "11 個。", {"A": "9 少算了三個鍵。", "B": "10 少算了一個鍵。", "C": "12 個胺基酸形成線性多肽有 11 個胜肽鍵，正確。", "D": "12 是胺基酸數，不是胜肽鍵數。"}),
    75: ("固有無序蛋白", "intrinsically disordered proteins 缺乏單一固定三維構形，但常有調控與訊號功能，並可與多種伙伴作用。", "intrinsically disordered proteins lack a fixed 3D structure。", "固有無序蛋白特性？", "缺乏確定三維結構。", {"A": "固有無序蛋白常有重要功能，不是大多無功能。", "B": "缺乏穩定單一三維結構是其核心特性。", "C": "其組成常富含帶電/極性胺基酸，不是主要由芳香族胺基酸組成。", "D": "它們常透過結構彈性與其他蛋白互動。"}),
    76: ("血紅蛋白 2,3-BPG", "2,3-BPG 結合去氧血紅蛋白，穩定 T state，降低氧親和力，幫助周邊釋氧。", "2,3-BPG stabilizes T state of hemoglobin。", "2,3-BPG 使 Hb 形成哪種四級結構？", "T state。", {"A": "R state 是高氧親和狀態，2,3-BPG 不穩定它。", "B": "2,3-BPG 穩定低氧親和的 T state，正確。", "C": "A form 是 DNA/RNA helix 用語，不是 Hb 四級結構。", "D": "Z form 也是核酸構形用語，不是 Hb 狀態。"}),
    77: ("脂溶性維生素吸收", "膽汁幫助脂質與脂溶性維生素 A、D、E、K 形成微膠粒吸收。", "vitamin A is fat-soluble and needs bile for absorption。", "哪種維生素需要膽汁吸收？", "vitamin A。", {"A": "vitamin A 為脂溶性，需膽汁協助吸收，正確。", "B": "vitamin B6 為水溶性。", "C": "vitamin B12 為水溶性，吸收需 intrinsic factor，不是膽汁。", "D": "vitamin C 為水溶性。"}),
    78: ("人類基因組", "人類蛋白質編碼序列只占基因組少數，約 1-2%；說超過 40% 編碼蛋白質明顯錯誤。", "protein-coding DNA is a small fraction, not over 40%。", "人類基因組何者錯誤？", "超過 40% DNA 編碼蛋白質。", {"A": "真核基因常由 introns 打斷，呈不連續，正確。", "B": "蛋白質編碼區只占很小比例，非超過 40%，此項錯誤。", "C": "轉座子/重複序列約占相當大比例，接近半數的說法可接受。", "D": "centromere 與 telomere 為具特殊功能的重複 DNA，正確。"}),
    79: ("5-FU 作用機轉", "5-FU 代謝成 FdUMP 後抑制 thymidylate synthase，使 dTMP 合成受阻。", "FdUMP inhibits thymidylate synthase。", "5-FU 抑制哪個酵素？", "胸苷酸合成酶。", {"A": "xanthine oxidase 與嘌呤分解及 allopurinol 相關，不是 5-FU 主要標靶。", "B": "CPS II 參與嘧啶合成早期步驟，不是 FdUMP 直接抑制標靶。", "C": "adenosine deaminase 與嘌呤代謝/SCID 相關。", "D": "FdUMP 抑制 thymidylate synthase，阻斷 dTMP 合成，正確。"}),
    80: ("免疫球蛋白輕鏈重組", "V-J 重組是 DNA 層級的基因重排；J-C 連接是在 RNA splicing 層級完成。", "light chain V-J recombination occurs in DNA; J-C joining occurs in RNA processing。", "輕鏈 V-J 與 J-C 分別在哪層面？", "DNA；RNA。", {"A": "J-C 不是 DNA 重組，而是轉錄後 RNA splicing。", "B": "V-J 在 DNA 重排，J-C 在 RNA splicing，正確。", "C": "J-C 不是蛋白質層級。", "D": "V-J 不是 RNA 層級。"}),
    81: ("HIV 高變異原因", "HIV reverse transcriptase 缺乏校讀能力，複製錯誤率高，造成基因體快速變異。", "low fidelity reverse transcriptase drives HIV mutation。", "HIV 快速變異主因？", "反轉錄酶精準度不佳。", {"A": "隨機插入可影響宿主基因，但不是快速變異主因。", "B": "特殊 DNA 水解酵素不是 HIV 高突變率核心。", "C": "反轉錄酶 fidelity 差、缺乏校讀，正確。", "D": "蛋白酶切割影響病毒成熟，不是基因體高變異主因。"}),
    82: ("大腸桿菌 mismatch repair", "E. coli 以 Dam methylase 甲基化 GATC 序列 adenine，舊股甲基化、新股暫未甲基化以供辨識。", "E. coli marks template strand by adenine methylation。", "MMR 如何標記模板股？", "腺嘌呤甲基化。", {"A": "不是移除 thymine 甲基。", "B": "uracil methylation 成 thymine 不是模板股標記機制。", "C": "腺嘌呤甲基化標記舊股 DNA，正確。", "D": "胞嘧啶甲基化不是 E. coli mismatch repair 的典型模板辨識。"}),
    83: ("aminoacyl-tRNA synthetase 專一性", "若酵素催化仍在但辨識 tRNA 專一性下降，錯誤胺基酸/錯誤 tRNA 配對增加，造成蛋白質序列錯誤。", "loss of tRNA recognition specificity increases translational decoding errors。", "aaRS 專一性降低後果？", "產生功能異常蛋白。", {"A": "攜帶多種胺基酸不會提高正確合成效率，反而降低 fidelity。", "B": "錯誤 charging 會使轉譯解碼錯誤增加，產生異常蛋白，正確。", "C": "題目說催化活性不受影響，故不會完全無法連接胺基酸。", "D": "問題在 charging specificity，不是核糖體無法識別 tRNA。"}),
    84: ("TFIIH 功能", "TFIIH 有 helicase、ATPase 與 kinase 活性，協助 promoter opening 與 RNA Pol II CTD phosphorylation；不是負責終止。", "TFIIH is for initiation/promoter opening, not transcription termination。", "TFIIH 不具何功能？", "轉錄終止。", {"A": "TFIIH helicase 活性需 ATP hydrolysis，正確功能。", "B": "TFIIH 參與轉錄前起始複合體形成，正確。", "C": "TFIIH 具有 helicase 與 kinase 活性，正確。", "D": "轉錄終止不是 TFIIH 的主要生理功能，故為答案。"}),
    85: ("operon operator", "operator 是 repressor binding site；repressor 結合後阻止 RNA polymerase 有效轉錄。", "operator sequence is bound by repressor。", "operator 主要由何分子結合？", "repressor。", {"A": "suppressor tRNA 參與轉譯讀穿突變，不是 operator 結合蛋白。", "B": "miRNA 是真核轉錄後調控小 RNA，不是原核 operator 結合者。", "C": "inducer 通常結合 repressor 改變其活性，不直接作為 operator 結合分子。", "D": "repressor 直接結合 operator，正確。"}),
    86: ("trp operon attenuation", "trp operon 前導序列含連續 tryptophan codons，核糖體停滯與否反映 tryptophan 濃度並決定 attenuation。", "leader peptide tryptophan codons allow attenuation to sense tryptophan level。", "trp operon 何者最適當？", "前導胜肽序列中的 Trp codons 調控轉錄活性。", {"A": "前導胜肽不是催化 attenuation 的酵素。", "B": "tryptophan 低時核糖體停在 Trp codons，通常允許轉錄繼續，不是提前衰減。", "C": "前導胜肽不直接結合 RNA polymerase 限制其移動。", "D": "leader peptide 中的 Trp codons 使 attenuation 能感測細胞 tryptophan，正確。"}),
    87: ("substrate-level phosphorylation", "1,3-BPG 在 phosphoglycerate kinase 反應中把高能磷酸轉給 ADP，直接生成 ATP。", "1,3-bisphosphoglycerate can generate ATP in one step via phosphoglycerate kinase。", "哪個一個反應可直接製造 ATP？", "1,3-bisphosphoglycerate。", {"A": "glycerol-3-phosphate 不能一步直接生成 ATP。", "B": "6-phosphogluconolactone 在 PPP 中，不直接產生 ATP。", "C": "fructose 1,6-bisphosphate 需後續多步糖解，不直接生成 ATP。", "D": "1,3-BPG 經 phosphoglycerate kinase 可直接生成 ATP，正確。"}),
    88: ("多醣分類", "cellulose 是植物細胞壁結構多醣；amylose、amylopectin 與 glycogen 是儲存多醣。", "cellulose is structural polysaccharide。", "哪個是結構型多醣？", "cellulose。", {"A": "cellulose 是植物細胞壁結構多醣，正確。", "B": "amylose 是澱粉儲存多醣成分。", "C": "amylopectin 是澱粉儲存多醣成分。", "D": "glycogen 是動物儲存多醣。"}),
    89: ("膜脂骨架", "phosphatidylcholine 是 glycerophospholipid，以 glycerol 為骨架；sphingolipids 以 sphingosine/ceramide 為骨架。", "phosphatidylcholine has glycerol backbone。", "哪個複合脂質含 glycerol 架構？", "phosphatidylcholine。", {"A": "cholesterol 是 sterol，不以 glycerol 為骨架。", "B": "phosphatidylcholine 是 glycerophospholipid，含 glycerol backbone，正確。", "C": "ceramide 是 sphingolipid 核心，以 sphingosine 為骨架。", "D": "sphingomyelin 是 sphingolipid，不是 glycerol backbone。"}),
    90: ("palmitate 合成 NADPH", "脂肪酸合成每次延長循環需 2 NADPH，palmitate 需 7 輪，共 14 NADPH。", "palmitate synthesis consumes 14 NADPH。", "合成 1 mol palmitate 需幾 mol NADPH？", "14。", {"A": "7 是延長循環次數，不是 NADPH 數。", "B": "7 輪每輪 2 個 NADPH，共 14，正確。", "C": "16 接近碳數，不是 NADPH 數。", "D": "21 過多。"}),
    91: ("胰島素與脂肪酸氧化", "血糖高時 insulin 上升，促進 acetyl-CoA carboxylase 產生 malonyl-CoA，抑制 CPT1，使脂肪酸進入粒線體氧化下降。", "high glucose -> insulin -> malonyl-CoA inhibits CPT1 -> less fatty acid oxidation。", "血糖與脂質氧化何者正確？", "血糖高時 insulin 上升，減少脂肪酸入粒線體氧化。", {"A": "血糖低時 glucagon 上升會促進脂肪酸氧化，不是減少。", "B": "血糖高時 glucagon 不會上升。", "C": "血糖高時 insulin 上升，抑制脂肪酸進入粒線體氧化，正確。", "D": "血糖低時 insulin 不會上升。"}),
    92: ("尿素循環區室", "glutamate oxidative deamination 產生 NH4+ 在肝臟粒線體；尿素循環前兩步在線粒體，後續在細胞質完成尿素生成。", "ammonia generation is mitochondrial; urea cycle spans mitochondria and cytosol with urea formed in cytosol。", "尿素循環何者最適切？", "NH4+ 釋放在粒線體，尿素產生後段在細胞質。", {"A": "glutamate 釋放 NH4+ 在肝粒線體，尿素生成後段在細胞質，最符合。", "B": "過氧化體不是主要場所。", "C": "尿素循環不全在線粒體，也不靠囊泡運送尿素。", "D": "過氧化體、內質網與囊泡運送說法錯誤。"}),
    93: ("生酮胺基酸", "leucine 與 lysine 是純生酮胺基酸；arginine、proline、glutamate 主要為生糖性。", "leucine is ketogenic amino acid。", "哪個生酮胺基酸可供能？", "白胺酸 leucine。", {"A": "白胺酸為純生酮胺基酸，可轉成 acetyl-CoA/acetoacetate，正確。", "B": "精胺酸主要為生糖性。", "C": "脯胺酸主要為生糖性。", "D": "麩胺酸主要為生糖性，進入 TCA 中間產物。"}),
    94: ("電子傳遞鏈質子幫浦", "Complex I、III、IV 將質子由 matrix 泵至 intermembrane space；Complex III 每對電子約泵 4 H+。", "complex III pumps 4 protons to intermembrane space。", "呼吸鏈何者正確？", "complex III 將 4 H+ 移至膜間腔。", {"A": "Complex I 將 H+ 泵到膜間腔，不是 matrix。", "B": "Complex III 也將 H+ 泵到膜間腔，不是 matrix。", "C": "Complex III 經 Q cycle 將約 4 H+ 移至膜間腔，正確。", "D": "Complex IV 通常泵約 2 H+，不是 4 H+。"}),
    95: ("胰島素活化 glycogen synthase", "insulin 經 Akt 使 GSK3 磷酸化而被抑制；GSK3 不再抑制 glycogen synthase，GS 活性上升。", "insulin phosphorylates/inhibits GSK3, activating glycogen synthase。", "insulin 如何活化 GS？", "使 GSK3 磷酸化並抑制其活性。", {"A": "GSK3 去磷酸化會較活化，且會抑制 GS，不會活化 GS。", "B": "磷酸化 GSK3 是抑制其活性，不是提高活性。", "C": "去磷酸化 GSK3 不會抑制其活性。", "D": "insulin 使 GSK3 磷酸化而抑制它，解除對 GS 的抑制，正確。"}),
    96: ("PKA 活化", "PKA holoenzyme 的 regulatory subunits 結合 cAMP 後釋放 catalytic subunits。", "cAMP binds the regulatory subunits of PKA。", "PKA 活化需要什麼？", "cAMP 結合 R 次單元。", {"A": "cAMP 結合 PKA regulatory subunit，使 catalytic subunit 釋放，正確。", "B": "cAMP 不是主要結合 catalytic subunit。", "C": "Ca2+ 不是 PKA 的主要活化配體。", "D": "Ca2+ 結合 catalytic subunit 不是 PKA 活化機制。"}),
    97: ("PI3K 訊息傳遞", "PI3K 將 PIP2 磷酸化成 PIP3，招募 Akt/PKB 等 PH-domain 蛋白到細胞膜。", "PI3K phosphorylates PIP2 to PIP3。", "PI3K 磷酸化哪個膜分子？", "PIP2。", {"A": "Ras 是小 GTPase，不是 PI3K 的主要膜脂質受質。", "B": "PKC 是下游訊號蛋白，不是 PI3K 磷酸化的膜脂。", "C": "PI3K 磷酸化 PIP2 形成 PIP3，正確。", "D": "PKB/Akt 是被 PIP3 招募活化的蛋白，不是 PI3K 的受質膜脂。"}),
    98: ("cloning vector 容量", "YAC 可承載非常大片段 DNA，容量通常大於 BAC、phage vector 與 plasmid。", "YAC carries the largest DNA inserts among listed vectors。", "哪個載體可承載最大 DNA 片段？", "YAC。", {"A": "pBR322 plasmid 容量小。", "B": "YAC 可承載最大 DNA 片段，正確。", "C": "phage vector 容量中等，小於人工染色體。", "D": "BAC 容量大，但通常小於 YAC。"}),
    99: ("siRNA 長度", "mammalian RNAi 中 siRNA 通常約 21-23 nucleotides，導入 RISC 後進行序列專一性沉默。", "siRNA is usually about 21-23 nucleotides。", "siRNA 一般幾個核苷酸？", "21-23。", {"A": "11-13 太短。", "B": "21-23 nucleotides 是典型 siRNA 長度，正確。", "C": "31-33 過長。", "D": "41-43 過長。"}),
    100: ("蛋白質交互作用分析", "co-IP、yeast two-hybrid、tandem affinity purification 都常用於蛋白交互作用；IHC 主要看組織定位/表現。官方答案標 A，但依一般生化實驗概念較可能有爭議。", "protein-protein interaction assays commonly include co-IP, yeast two-hybrid, and tandem affinity purification; IHC is mainly localization.", "哪種一般不適用於蛋白質交互作用？", "官方答案為 A；此題建議人工複核。", {"A": "官方答案為串接親和共純化；但 TAP 常用於純化蛋白複合體與交互作用研究，故此官方答案值得複核。", "B": "免疫共沉澱是典型蛋白質交互作用分析方法。", "C": "免疫組織化學主要看組織定位與表現，通常不是直接證明交互作用的方法。", "D": "酵母菌雙雜交是典型蛋白質交互作用篩選方法。"}, ["官方答案 A 與常見實驗方法認知可能不一致；IHC 通常更不像直接蛋白交互作用分析，建議人工複核。"]),
})


for num, item in MORE.items():
    topic, stem, core, front, back, reasons, *notes = item
    R[num] = {
        "topic": topic,
        "stem": stem,
        "core": core,
        "front": front,
        "back": back,
        "reasons": reasons,
        "manual_review_notes": notes[0] if notes else [],
    }


def main():
    exam = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    questions = {q["question_number"]: q for q in exam["questions"]}
    if sorted(R) != list(range(1, 101)):
        missing = sorted(set(range(1, 101)) - set(R))
        extra = sorted(set(R) - set(range(1, 101)))
        raise SystemExit(f"record coverage mismatch missing={missing} extra={extra}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
    updates = []
    for number in range(1, 101):
        q = questions[number]
        rec = R[number]
        answer = q.get("correct_answer")
        explanation = make_exp(rec["topic"], rec["stem"], answer, rec["reasons"], rec["core"])
        updates.append(
            {
                "question_id": q["id"],
                "question_number": number,
                "explanation": explanation,
                "key_point": rec["core"],
                "flashcard_front": rec["front"],
                "flashcard_back": rec["back"],
                "flashcard_summary": f"{rec['topic']} -> {rec['back']}",
                "review_status": "ai_generated",
                "explanation_model": MODEL,
                "explanation_generated_at": stamp,
                "manual_review_notes": rec.get("manual_review_notes", []),
            }
        )

    for start in range(1, 101, 10):
        end = start + 9
        shard = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates[start - 1 : end],
        }
        path = OUT_DIR / f"q{start:03d}-q{end:03d}.json"
        path.write_text(json.dumps(shard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote 10 update files to {OUT_DIR}")


if __name__ == "__main__":
    main()
