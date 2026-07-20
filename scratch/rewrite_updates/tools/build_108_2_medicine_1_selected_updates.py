import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/108-2/medicine-1.json"
DATASET_ID = "108-2_medicine-1"
OUT_DIR = Path("scratch/rewrite_updates/108-2_medicine-1_selected")
GENERATED_AT = "2026-07-20T00:00:00+08:00"


TARGETS = [
    1, 3, 5, 7, 8, 9, 11, 12, 13, 14,
    15, 16, 17, 19, 20, 21, 22, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    39, 40, 42, 44, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 57, 59, 60, 61, 62, 63, 64,
    65, 66, 67, 69, 70, 71, 72, 73, 75, 76,
    77, 79, 80, 81, 82, 83, 85, 86, 87, 88,
    89, 91, 92, 93, 94, 95, 96, 98, 99,
]

BATCHES = [
    TARGETS[0:10],
    TARGETS[10:20],
    TARGETS[20:30],
    TARGETS[30:40],
    TARGETS[40:50],
    TARGETS[50:60],
    TARGETS[60:70],
    TARGETS[70:79],
]


ENTRIES = {
    1: {
        "stem": "此資料列的題幹前段混入新小腦題，正式選項與官方答案則是在考總腱環(common tendinous ring)：哪些神經不從總腱環內通過。總腱環內通過的是動眼神經、外旋神經與鼻睫神經；額神經、淚神經與滑車神經在環外走行。",
        "key": "眼眶總腱環內有 CN III、CN VI 與 nasociliary nerve；frontal、lacrimal、trochlear nerves 走在總腱環外。",
        "reasons": {
            "A": "①額神經與⑤滑車神經在總腱環外，但③動眼神經穿過總腱環內，因此 135 混入一條環內神經。",
            "B": "②鼻睫神經、③動眼神經、⑥外旋神經都是總腱環內的重要內容物，236 方向完全相反。",
            "C": "④淚神經在環外，但②鼻睫神經與⑥外旋神經在環內，所以 246 不是完整的環外組合。",
            "D": "①額神經、④淚神經、⑤滑車神經均經上眼眶裂但不通過總腱環內，符合官方答案。題幹混排需人工回頭校對來源題文。",
        },
        "notes": ["Q1 題幹混入另一題文字，已依正式選項與官方答案 D 撰寫，建議人工校對來源題文。"],
    },
    3: {
        "stem": "翼腭窩的交通孔道是本題重點。後上方主要經圓孔(foramen rotundum)連到中顱窩，讓上頜神經 V2 進入翼腭窩。",
        "key": "翼腭窩後上方經圓孔通中顱窩；內側通鼻腔，外側通顳下窩，下方通口腔。",
        "reasons": {
            "A": "鼻腔是翼腭窩內側經蝶腭孔(sphenopalatine foramen)相通的位置，不是後上方。",
            "B": "顳下窩經翼上頜裂(pterygomaxillary fissure)與翼腭窩外側相通，方向不是後上。",
            "C": "中顱窩經圓孔連到翼腭窩後上方，這正是 V2 的入口路徑。",
            "D": "口腔主要經大、小腭管往下連通硬腭與軟腭，屬下方通道。",
        },
    },
    5: {
        "stem": "迷走神經進入腹腔時與食道一起形成前、後迷走神經幹，穿過橫膈的食道裂孔，位置約 T10。",
        "key": "迷走神經進腹腔走食道裂孔；主動脈孔給主動脈與胸管，腔靜脈孔給下腔靜脈。",
        "reasons": {
            "A": "食道裂孔容納食道與前、後迷走神經幹，是迷走神經進入腹腔的通道。",
            "B": "主動脈孔主要通過主動脈、胸管與奇靜脈相關構造，不是迷走神經的典型路徑。",
            "C": "腔靜脈孔位於 T8，供下腔靜脈穿過，也可有右膈神經分支，不是迷走神經。",
            "D": "正中弓狀韌帶跨過主動脈前方，描述的是主動脈裂孔邊界，不是神經進腹腔孔道。",
        },
    },
    7: {
        "stem": "梨狀肌是大坐骨孔內分隔上下通道的地標。臀上神經與臀上血管從梨狀肌上方進入臀部，其餘多由梨狀肌下方通過。",
        "key": "梨狀肌上方是 superior gluteal nerve/vessels；梨狀肌下方有 sciatic、inferior gluteal、pudendal 等構造。",
        "reasons": {
            "A": "臀上動脈與臀上神經一起由梨狀肌上方通過，是本題指定的構造。",
            "B": "臀下動脈由梨狀肌下方離開骨盆，供應臀部深層與附近肌群。",
            "C": "坐骨神經通常從梨狀肌下方進入臀區，臨床上也常以此解釋梨狀肌症候群。",
            "D": "陰部神經先由梨狀肌下方出骨盆，再繞坐骨棘進入會陰，不走梨狀肌上方。",
        },
    },
    8: {
        "stem": "腓深神經支配小腿前區肌群，負責踝背屈與伸趾。受傷時最典型會影響脛前肌，造成 foot drop 類表現。",
        "key": "Deep fibular nerve 支配 anterior compartment；tibialis anterior 是踝背屈關鍵肌。",
        "reasons": {
            "A": "腓長肌屬小腿外側區，主要由腓淺神經支配，功能偏足外翻。",
            "B": "腓短肌同樣屬腓淺神經支配，受腓深神經傷害時不是最直接受影響者。",
            "C": "脛前肌位於前區，由腓深神經支配，是踝背屈最重要的肌肉之一。",
            "D": "脛後肌位於小腿後深層，主要由脛神經支配，功能偏足內翻與蹠屈輔助。",
        },
    },
    9: {
        "stem": "肱骨內上髁後方的淺溝是尺神經通過處，俗稱 funny bone。撞擊內上髁後方會產生尺側手部麻痛。",
        "key": "尺神經走在肱骨內上髁後方；正中神經在肘前方，橈神經繞肱骨橈神經溝。",
        "reasons": {
            "A": "肌皮神經穿喙肱肌後走在上臂前區，不貼著內上髁後方。",
            "B": "正中神經經肘窩前方進入前臂，與肱動脈相關，不在內上髁後溝。",
            "C": "尺神經由內上髁後方通過，位置表淺且容易受壓或撞擊。",
            "D": "橈神經在上臂後方的橈神經溝走行，遠端偏向肱骨外上髁附近。",
        },
    },
    11: {
        "stem": "齒狀核輸出纖維是小腦主要離心路徑，經上小腦腳離開小腦，交叉後到紅核與丘腦。",
        "key": "Dentato-rubro-thalamic tract 是小腦輸出路徑，主要走 superior cerebellar peduncle。",
        "reasons": {
            "A": "上小腦腳承載齒狀核到紅核、丘腦的主要離心纖維，是本題答案。",
            "B": "中小腦腳主要是橋腦核到小腦的傳入纖維，代表 pontocerebellar input。",
            "C": "下小腦腳多為脊髓、前庭、橄欖等來源的傳入纖維，不是齒狀核主要輸出。",
            "D": "繩狀體是下小腦腳的重要組成，仍屬下小腦腳範圍，不是此徑路。",
        },
    },
    12: {
        "stem": "脊髓白質外側束含外側皮質脊髓徑，負責隨意運動控制。不同傳導徑在白質內有固定分布，是常考定位。",
        "key": "Lateral funiculus 內有 lateral corticospinal tract；背柱內側蹄系在後索。",
        "reasons": {
            "A": "背柱內側蹄系在脊髓階段走後索，傳精細觸覺、震動覺與本體覺。",
            "B": "外側皮質脊髓徑位於外側束，是下行運動徑的核心考點。",
            "C": "前庭脊髓徑多走前索或前外側區，主要調控姿勢與伸肌張力。",
            "D": "四疊體脊髓徑主要走前索，與頭頸反射性轉向較相關。",
        },
    },
    13: {
        "stem": "精細觸覺與震動覺、意識本體覺同屬背柱內側蹄系傳導，先在同側後索上行，再於延髓交叉。",
        "key": "Fine touch 走 dorsal column-medial lemniscus system；痛溫覺才偏前外側系統。",
        "reasons": {
            "A": "脊髓網狀徑與較瀰漫的痛覺、覺醒反應相關，不是精細定位觸覺的主路徑。",
            "B": "背側脊髓小腦徑傳無意識本體覺到小腦，用於運動協調。",
            "C": "背柱內側蹄系負責精細觸覺、震動覺與意識本體覺，符合題目。",
            "D": "前外側系統以痛覺、溫度覺與粗略觸覺為主，不是精細觸覺首選。",
        },
    },
    14: {
        "stem": "腳間窩(interpeduncular fossa)位於中腦腹側兩大腦腳之間，第三腦神經從此區域出腦。",
        "key": "Oculomotor nerve emerges from the interpeduncular fossa；trochlear nerve 從背側出腦。",
        "reasons": {
            "A": "滑車神經是唯一從腦幹背側離開的腦神經，不出現在腳間窩。",
            "B": "動眼神經自中腦腹側腳間窩出腦，正符合題目位置。",
            "C": "基底動脈位於橋腦腹側的基底溝附近，不是腳間窩內的典型構造。",
            "D": "腦下垂體位於蝶鞍內，與中腦腳間窩不是同一解剖空間。",
        },
    },
    15: {
        "stem": "Brodmann area 4 是初級運動皮質，位於中央前迴(precentral gyrus)。題目問錯誤敘述，因此把它放在中央後迴就是錯誤。",
        "key": "Area 4 = primary motor cortex at precentral gyrus；postcentral gyrus 是初級體感皮質。",
        "reasons": {
            "A": "Area 4 可發出皮質脊髓徑，是隨意運動輸出的主要來源之一。",
            "B": "Betz cells 是初級運動皮質第五層的大型錐體細胞，與 area 4 相符。",
            "C": "丘腦腹外側核接收小腦與基底核相關訊息後投射到運動皮質，此敘述可成立。",
            "D": "後中央迴是 Brodmann areas 3, 1, 2 的初級體感區，不是 area 4。",
        },
    },
    16: {
        "stem": "下頜神經(V3)除了感覺，也支配第一咽弓來源肌肉；腭帆張肌是其中之一。其餘多由迷走神經咽叢支配。",
        "key": "Tensor veli palatini 由 V3 支配；多數軟顎肌由 vagus nerve 支配。",
        "reasons": {
            "A": "腭帆張肌由 V3 的內側翼肌神經分支支配，V3 受損會影響其收縮。",
            "B": "腭帆提肌主要由迷走神經經咽叢支配，不是下頜神經。",
            "C": "腭咽肌屬咽喉部肌群，主要接受迷走神經咽叢支配。",
            "D": "腭舌肌雖在口咽交界，但運動支配仍以迷走神經為主。",
        },
    },
    17: {
        "stem": "喉外神經是上喉神經的外支，支配環甲肌。環甲肌可拉緊聲帶、調高音調；其他喉內肌多由返喉神經支配。",
        "key": "External laryngeal nerve innervates cricothyroid muscle；recurrent laryngeal nerve 支配多數其他喉內肌。",
        "reasons": {
            "A": "後環杓肌是唯一主要外展聲帶的肌肉，支配來自返喉神經。",
            "B": "外側環杓肌負責內收聲帶，也由返喉神經支配。",
            "C": "環甲肌由喉外神經支配，是上喉神經外支的經典考點。",
            "D": "甲杓肌調整聲帶張力，主要由返喉神經支配。",
        },
    },
    19: {
        "stem": "甲狀頸幹的典型分支包括甲狀腺下動脈、肩胛上動脈、橫頸動脈與升頸動脈。深頸動脈多來自肋頸幹。",
        "key": "Deep cervical artery 不是 thyrocervical trunk 分支，通常來自 costocervical trunk。",
        "reasons": {
            "A": "深頸動脈屬肋頸幹系統，供應頸後深層肌群，因此是本題的例外。",
            "B": "肩胛上動脈是甲狀頸幹常見分支，走向肩胛上切跡附近。",
            "C": "橫頸動脈通常由甲狀頸幹發出，供應頸肩背部相關區域。",
            "D": "甲狀腺下動脈是甲狀頸幹重要分支，供應甲狀腺下部。",
        },
    },
    20: {
        "stem": "房室結位於右心房 Koch triangle 內，靠近冠狀竇開口、三尖瓣隔瓣與 Todaro tendon 所圍區域。",
        "key": "AV node 最靠近 coronary sinus opening，是 Koch triangle 的重要地標。",
        "reasons": {
            "A": "節制帶位於右心室，與右束支傳導較相關，距 AV node 的解剖定位較遠。",
            "B": "下腔靜脈與右心房交界靠近竇房結相關區域，不是 AV node 最典型地標。",
            "C": "冠狀竇開口位於 Koch triangle 邊界附近，是判定 AV node 位置的關鍵。",
            "D": "界脊是右心房平滑部與梳狀肌區的分界，與竇房結區域較相關。",
        },
    },
    21: {
        "stem": "肺淋巴回流通常沿支氣管與肺門方向前進，下葉淋巴常先到下氣管支氣管淋巴結，也就是 carinal/subcarinal 區域。",
        "key": "肺下葉淋巴常匯入 inferior tracheobronchial nodes；肺淋巴多沿支氣管樹而非肺動脈主軸。",
        "reasons": {
            "A": "氣管分叉下方是下氣管支氣管淋巴結，不稱主動脈弓淋巴結。",
            "B": "右上肺葉淋巴主要走右側支氣管縱隔幹，通常不是直接匯入胸管。",
            "C": "肺淋巴管與支氣管、肺門淋巴結路徑更密切，不是主要與肺動脈伴行。",
            "D": "左下肺葉可回流至下氣管支氣管淋巴結，符合下葉往隆突附近回流的概念。",
        },
    },
    22: {
        "stem": "奇靜脈系統收集多數胸壁肋間靜脈，但左側第一肋間靜脈常直接或經左上肋間靜脈匯入左頭臂靜脈，不算典型奇靜脈系統。",
        "key": "左第一肋間靜脈多入左頭臂靜脈；多數後肋間靜脈才進 azygos/hemiazygos/accessory hemiazygos 系統。",
        "reasons": {
            "A": "左第八肋間靜脈通常可經半奇靜脈或副半奇靜脈系統回流，仍屬奇靜脈相關系統。",
            "B": "左第一肋間靜脈常走向左頭臂靜脈，通常不匯入奇靜脈系統。",
            "C": "右第三肋間靜脈可經右上肋間靜脈或奇靜脈系統回流，屬典型胸壁回流路徑。",
            "D": "右第十肋間靜脈直接或間接進入奇靜脈，是奇靜脈系統常見收集範圍。",
        },
    },
    25: {
        "stem": "近幽門十二指腸潰瘍常位於十二指腸球部後壁，臨床出血多與胃十二指腸動脈相關。選項沒有胃十二指腸動脈時，上游的肝總動脈是可結紮控制來源的選項。",
        "key": "十二指腸近幽門潰瘍出血考 gastroduodenal artery；選項中以 common hepatic artery 最接近其上游來源。",
        "reasons": {
            "A": "肝總動脈發出胃十二指腸動脈，能涵蓋近幽門十二指腸後壁出血的主要上游供血。",
            "B": "下胰十二指腸動脈主要供應十二指腸遠端與胰頭下部，來自上腸繫膜動脈。",
            "C": "左胃動脈供應胃小彎與腹段食道附近，與十二指腸球部後壁出血不相符。",
            "D": "左胃網膜動脈沿胃大彎左側走行，主要來自脾動脈系統，不是此處潰瘍重點。",
        },
    },
    26: {
        "stem": "腹股溝管深環是腹橫筋膜上的開口，男性通過精索，女性通過子宮圓韌帶。直接疝與間接疝的差異在是否經深環進入管內。",
        "key": "Deep inguinal ring 是 transversalis fascia 的開口；女性腹股溝管通過 round ligament。",
        "reasons": {
            "A": "女性通過的是子宮圓韌帶(round ligament of uterus)，不是卵巢韌帶。",
            "B": "鞘突是腹膜向腹股溝管的胚胎性突出，女性也可有對應結構，不只男性。",
            "C": "管內疝氣通常指經深環進入的間接型腹股溝疝，直接疝從 Hesselbach triangle 突出。",
            "D": "腹橫筋膜形成腹股溝管深環，是深環與其附近管壁的基本構造來源。",
        },
    },
    27: {
        "stem": "男性射精前的 emission 主要由交感神經促使輸精管、精囊與前列腺收縮，把精液送入尿道。外尿道括約肌屬骨骼肌控制，並非此階段典型會發生的腺體或輸精管收縮。",
        "key": "Emission 以交感神經促進輸精管與附屬腺收縮；外尿道括約肌不是準備射精時的主要收縮事件。",
        "reasons": {
            "A": "外尿道括約肌受陰部神經支配，題目問準備射精時的內臟反應，官方將其列為不會發生的現象。",
            "B": "前列腺收縮可把前列腺液排入尿道，是 emission 的一部分。",
            "C": "輸精管平滑肌收縮會推送精子，是射精準備階段的典型反應。",
            "D": "球尿道腺分泌與會陰部肌肉活動可參與性交與射精前後過程，不是本題的例外。",
        },
    },
    28: {
        "stem": "會陰體是多條會陰肌附著的中央纖維肌性結構，受傷後最會影響附著其上的球海綿體肌與會陰橫肌。坐骨海綿體肌主要附著於坐骨恥骨支，尿道外括約肌不是以會陰體為主要功能支點。",
        "key": "Perineal body 受傷主要影響 bulbospongiosus、superficial/deep transverse perineal 等附著肌；ischiocavernosus 較不受影響。",
        "reasons": {
            "A": "1 球海綿體肌與 3 會陰淺橫肌都與會陰體相關，受傷後容易受影響。",
            "B": "2 會陰深橫肌和會陰體有關，雖然 4 坐骨海綿體肌較少受影響，但此組合不是最佳。",
            "C": "1 球海綿體肌附著會陰體，受傷時功能容易改變，所以 15 不能說最不受影響。",
            "D": "4 坐骨海綿體肌主要固定於坐骨恥骨支，5 尿道外括約肌也不是典型以會陰體為主要附著點，最符合不受影響的組合。",
        },
    },
    29: {
        "stem": "內收長肌屬大腿內收肌群，主要由閉孔神經支配。股薄肌同屬內收群，也由閉孔神經支配。",
        "key": "Adductor longus 與 gracilis 主要都由 obturator nerve 支配。",
        "reasons": {
            "A": "股薄肌是大腿內側肌群，主要由閉孔神經支配，與內收長肌相同。",
            "B": "股方肌由 sacral plexus 的 nerve to quadratus femoris 支配，不是閉孔神經。",
            "C": "恥骨肌常以股神經支配為主，可有閉孔神經變異，但考題常不列為與內收長肌相同的最佳答案。",
            "D": "閉孔內肌由 nerve to obturator internus 支配，名稱相近但不是閉孔神經本幹。",
        },
    },
    30: {
        "stem": "腕隧道內含正中神經及多條屈肌肌腱，包含屈拇指長肌腱。伸拇長肌與外展拇長肌走背側伸肌腱鞘，不在腕隧道內。",
        "key": "Carpal tunnel contains flexor pollicis longus tendon and flexor digitorum tendons with median nerve。",
        "reasons": {
            "A": "伸拇指長肌腱走手腕背側的伸肌區，不是腕隧道內容物。",
            "B": "屈拇指長肌腱穿過腕隧道，腕隧道症候群或狹窄會影響其滑動空間。",
            "C": "外展拇指長肌腱走背外側第一伸肌腱鞘，與腕隧道不同。",
            "D": "內收拇指肌由尺神經深支支配，肌腹位於手掌深部，不是腕隧道內肌腱。",
        },
    },
    31: {
        "stem": "背部肌肉層次由淺入深可分夾肌、豎脊肌、橫突棘肌與枕下肌群。大後頭直肌屬枕下肌群，位置比前面幾個更深。",
        "key": "Rectus capitis posterior major 屬 suboccipital muscles，是列舉肌肉中最深層。",
        "reasons": {
            "A": "頭夾肌屬較淺層的 splenius group，覆蓋在深層肌群外側。",
            "B": "頭最長肌屬豎脊肌群，比枕下小肌群表淺。",
            "C": "頭半棘肌屬橫突棘肌群，雖深於夾肌與豎脊肌部分，但仍覆蓋枕下肌。",
            "D": "大後頭直肌位在枕下三角附近，屬最深層的枕下肌群。",
        },
    },
    32: {
        "stem": "精子生成中，初級精母細胞完成第一次減數分裂後會形成兩個次級精母細胞；第二次減數分裂後才形成精細胞。",
        "key": "Meiosis I: primary spermatocyte -> secondary spermatocytes；meiosis II -> spermatids。",
        "reasons": {
            "A": "精原細胞是起始的有絲分裂細胞，位於減數分裂之前。",
            "B": "初級精母細胞是進入第一次減數分裂的細胞，不是 meiosis I 完成後的產物。",
            "C": "次級精母細胞正是第一次減數分裂完成後產生的細胞。",
            "D": "精細胞是在次級精母細胞完成第二次減數分裂後才出現。",
        },
    },
    33: {
        "stem": "橫膈胚胎來源包括橫中隔、胸腹膜、食道背側繫膜與體壁肌肉。胸心包膜主要形成纖維心包與胸膜心包膜，不構成橫膈。",
        "key": "Diaphragm 來源不包括 pleuropericardial membrane。",
        "reasons": {
            "A": "橫中隔形成橫膈中央腱的重要來源，是橫膈組成之一。",
            "B": "胸腹膜參與關閉胸腹腔間通道，是橫膈胚胎來源。",
            "C": "食道背側繫膜形成橫膈腳(crura)相關構造，與橫膈有關。",
            "D": "胸心包膜用來分隔心包腔與胸膜腔，不是橫膈的胚胎組成。",
        },
    },
    34: {
        "stem": "十二指腸由前腸末端與中腸起始部共同形成，隨胃旋轉而向右形成 C-loop。上皮增生會暫時阻塞腔道，之後再通化。",
        "key": "Duodenum 發育會經歷上皮增生造成暫時閉鎖，再 recanalization。",
        "reasons": {
            "A": "十二指腸並非全部來自前腸，遠端還有中腸來源。",
            "B": "卵黃柄連接的是中腸環頂端，不是十二指腸環的典型連接。",
            "C": "胃旋轉後十二指腸環通常移向右側並成為次級腹膜後構造，不是左側。",
            "D": "十二指腸上皮增生會使腔道一度閉鎖，隨後再通化，這是正確敘述。",
        },
    },
    35: {
        "stem": "未分化性腺中的原始性腺索在男性會持續發育成睪丸索，最後形成細精管。女性則由皮質索形成原始濾泡。",
        "key": "男性 gonadal cords -> seminiferous tubules；女性 cortical cords -> primordial follicles。",
        "reasons": {
            "A": "女性原始濾泡主要來自皮質索，不是原始性腺索直接形成的男性化路徑。",
            "B": "副睪由中腎管(mesonephric duct)衍生，不是男性皮質索。",
            "C": "男性性腺索會形成睪丸索並發育為細精管，符合題目。",
            "D": "輸卵管來自副中腎管(paramesonephric duct)，不是女性皮質索。",
        },
    },
    36: {
        "stem": "眼發育中，視網膜中央動脈與靜脈來自玻璃體血管近端保留下來的部分；遠端玻璃體血管會退化。因此題目問錯誤時選 B。",
        "key": "Central retinal vessels 來自 hyaloid vessels 的近端，不是遠端。",
        "reasons": {
            "A": "眼裂位於眼杯與視柄腹側，容納玻璃體血管進入，描述正確。",
            "B": "中央視網膜血管由近側玻璃體血管形成，遠側部分退化，所以遠側端衍生物的說法錯誤。",
            "C": "視網膜色素上皮源自眼杯外層，神經視網膜源自內層。",
            "D": "視神經由視網膜神經節細胞軸突沿視柄形成，敘述正確。",
        },
    },
    37: {
        "stem": "平滑肌細胞呈梭形，細胞外常有外板包圍，細胞間以 gap junction 促進同步收縮；沒有骨骼肌那種 T 小管系統。",
        "key": "Smooth muscle cell 外有 external lamina；dense bodies 主要錨定 actin，不用 T tubules。",
        "reasons": {
            "A": "緻密體主要作為肌動蛋白絲與中間絲的錨定點，不是肌球蛋白絲直接附著處。",
            "B": "平滑肌細胞外有外板包圍，是組織學上的正確特徵。",
            "C": "平滑肌沒有典型 T 小管，鈣離子訊號多靠 caveolae 與胞內外鈣來源調節。",
            "D": "平滑肌細胞間常以 gap junction 溝通，不是以橋粒作為收縮同步的核心。",
        },
    },
    39: {
        "stem": "長骨軟骨內骨化先在骨幹形成初級骨化中心，出生前後才在骨骺形成次級骨化中心。",
        "key": "Primary ossification center 位於 diaphysis；secondary ossification centers 位於 epiphyses。",
        "reasons": {
            "A": "骨幹是初級骨化中心所在位置，先形成骨套與骨化區。",
            "B": "骨骺主要出現次級骨化中心，不是初級骨化中心。",
            "C": "骨幹骺端是生長板附近區域，負責長度增加，但不是初級中心命名位置。",
            "D": "骨內膜是骨內表面的細胞層，與骨化中心的解剖位置不同。",
        },
    },
    40: {
        "stem": "中樞神經膠細胞各有分工：寡突膠細胞形成 CNS 髓鞘，星狀膠細胞支持血腦障壁與離子環境，微小膠細胞負責免疫吞噬，室管膜細胞襯腦室與中央管。",
        "key": "Oligodendrocyte 是 CNS 的 myelin-forming cell，功能類似 PNS 的 Schwann cell。",
        "reasons": {
            "A": "寡突膠細胞在中樞形成髓鞘，功能上對應周邊的許旺細胞。",
            "B": "立方上皮樣、襯腦室與中央管的是室管膜細胞，不是星狀膠細胞。",
            "C": "灰質中數量最多、分支接觸血管的是星狀膠細胞；微小膠細胞以免疫吞噬為主。",
            "D": "室管膜細胞主要襯腦室與參與腦脊髓液環境，吞噬免疫功能屬微小膠細胞。",
        },
    },
    42: {
        "stem": "胰臟內分泌部是蘭氏小島，分泌 insulin、glucagon 等荷爾蒙。腺泡與泡心細胞屬外分泌部。",
        "key": "Endocrine pancreas = islets of Langerhans；exocrine pancreas = serous acini and ducts。",
        "reasons": {
            "A": "漿液腺泡是外分泌胰臟，負責消化酵素，不是內分泌部。",
            "B": "蘭氏小島是胰臟內分泌部，由多種內分泌細胞組成。",
            "C": "泡心細胞位於腺泡中心並連接導管系統，屬外分泌導管相關細胞。",
            "D": "嗜酸性酶原顆粒是外分泌腺泡細胞富含消化酵素的特徵。",
        },
    },
    44: {
        "stem": "緻密斑屬遠端小管在血管極附近的特化上皮，負責感受 tubular NaCl。題目問錯誤，近直小管來源的說法不對。",
        "key": "Macula densa 是 distal tubule/thick ascending limb 末端特化，不是 proximal straight tubule。",
        "reasons": {
            "A": "腎絲球微血管內皮為有窗型，利於濾過，是正確敘述。",
            "B": "緻密斑來自遠端小管相關上皮，不是近直小管，因此為錯誤敘述。",
            "C": "近腎絲球細胞由入球小動脈平滑肌樣細胞特化，可分泌 renin。",
            "D": "弓形動脈位於皮質與髓質交界附近，是腎血管走行的重要地標。",
        },
    },
    46: {
        "stem": "細精管內的生精上皮含不同階段生殖細胞與 Sertoli cell，屬複合型複層上皮。睪固酮主要由間質 Leydig cell 分泌。",
        "key": "Seminiferous tubule lining 是 complex stratified seminiferous epithelium。",
        "reasons": {
            "A": "Sertoli cell 位於細精管上皮內，支持生殖細胞，不是在管外。",
            "B": "類肌細胞可收縮幫助推動管內容物；睪固酮由 Leydig cell 分泌。",
            "C": "細精管上皮包含多層不同分化階段的細胞，稱複合型複層上皮。",
            "D": "靠近基底部的是精原細胞，較成熟的精細胞位於靠近管腔處。",
        },
    },
    47: {
        "stem": "Guanylyl cyclase 催化 GTP 形成 cGMP。可溶性 guanylyl cyclase 受 nitric oxide 活化，cGMP 進一步活化 PKG 並造成平滑肌鬆弛。",
        "key": "NO activates soluble guanylyl cyclase -> cGMP -> PKG -> vasodilation。",
        "reasons": {
            "A": "cAMP 由 adenylyl cyclase 生成，不是 guanylyl cyclase 的產物。",
            "B": "一氧化氮可活化可溶性 guanylyl cyclase，是血管舒張訊號的核心。",
            "C": "guanylyl cyclase 的產物 cGMP 主要活化 protein kinase G，不是直接活化 PKC。",
            "D": "NO-cGMP 訊號通常使血管平滑肌鬆弛，方向是血管舒張而非收縮。",
        },
    },
    48: {
        "stem": "Astrocyte 參與血腦障壁、離子與神經傳遞物環境調控，並提供代謝支持；形成中樞髓鞘是寡突膠細胞的工作。",
        "key": "Astrocyte 不形成 myelin；CNS myelin 由 oligodendrocyte 形成。",
        "reasons": {
            "A": "星狀膠細胞足突包覆血管，誘導與維持血腦障壁功能。",
            "B": "髓鞘形成由寡突膠細胞負責，這不是 astrocyte 的正常功能。",
            "C": "星狀膠細胞可調節細胞外鉀離子與神經傳遞物濃度，維持神經元環境。",
            "D": "星狀膠細胞可儲存肝醣並以 lactate 等方式支持神經元代謝。",
        },
    },
    49: {
        "stem": "瞳孔對光反射路徑是 retina/optic nerve 到 pretectal area，再到雙側 Edinger-Westphal nucleus，經動眼神經至 ciliary ganglion 和瞳孔括約肌。三叉神經不在此反射弧。",
        "key": "Pupillary light reflex uses CN II afferent and CN III parasympathetic efferent；trigeminal nerve 不參與。",
        "reasons": {
            "A": "中腦的 pretectal area 與 Edinger-Westphal nucleus 是光反射中樞。",
            "B": "睫狀神經節是副交感節後神經元所在，會支配瞳孔括約肌。",
            "C": "Edinger-Westphal nucleus 提供動眼神經副交感節前纖維，屬反射弧一部分。",
            "D": "三叉神經負責臉部感覺與角膜反射傳入等，並不參與瞳孔對光反射。",
        },
    },
    50: {
        "stem": "純感覺腦神經包括嗅、視、前庭蝸神經。題目列出的選項中，只有第二腦神經 optic nerve 是純感覺纖維。",
        "key": "CN II 是純感覺；CN V、VII、X 都含運動或副交感成分。",
        "reasons": {
            "A": "視神經傳遞視覺特殊感覺，不含一般體運動纖維，是純感覺腦神經。",
            "B": "三叉神經含臉部感覺，也含咀嚼肌運動纖維，因此不是只含 sensory fibers。",
            "C": "顏面神經含臉部表情肌運動、副交感與味覺纖維，成分混合。",
            "D": "迷走神經含內臟運動、副交感、感覺與味覺等纖維，不是純感覺。",
        },
    },
    51: {
        "stem": "投籃百發百中屬反覆練習後的運動學習、校正與時序控制，小腦在誤差修正與精細協調中最重要。",
        "key": "Cerebellum 負責 motor learning、timing、coordination 與誤差校正。",
        "reasons": {
            "A": "海馬迴偏陳述性記憶與空間記憶，不是精準投籃動作校正的主角。",
            "B": "基底核參與習慣、動作選擇與啟動，但投籃精準誤差修正更偏小腦。",
            "C": "黑質屬基底核迴路，與多巴胺和帕金森病相關，不是此題最佳腦區。",
            "D": "小腦負責動作協調與運動學習，可讓反覆練習的動作更精準。",
        },
    },
    52: {
        "stem": "動態顫抖、測距障礙與姿勢不穩是小腦病變典型三聯考點，反映協調與誤差修正受損。",
        "key": "Intention tremor、dysmetria、ataxia 指向 cerebellar lesion。",
        "reasons": {
            "A": "大腦運動皮質損傷偏上運動神經元徵象，如痙攣、無力與反射亢進。",
            "B": "小腦受損會造成 intention tremor、dysmetria、步態或姿勢不穩。",
            "C": "基底核病變常見靜止顫抖、舞蹈症、動作遲緩等動作調節問題。",
            "D": "中腦病灶可影響眼動、意識或傳導徑，但題目這組症狀最典型是小腦。",
        },
    },
    53: {
        "stem": "下運動神經元損傷會有肌萎縮、肌束顫動與反射降低。選項中 ALS 會同時侵犯上、下運動神經元，最能連到 lower motor neuron degeneration。",
        "key": "ALS involves degeneration of upper and lower motor neurons；LMN signs include atrophy and fasciculations。",
        "reasons": {
            "A": "Parkinson disease 主要是黑質多巴胺神經元退化，屬基底核迴路疾病。",
            "B": "Huntington disease 是紋狀體相關退化，表現舞蹈症與認知精神症狀。",
            "C": "ALS 侵犯脊髓前角細胞等下運動神經元，也侵犯上運動神經元，是本題答案。",
            "D": "Myasthenia gravis 是神經肌肉接合處 acetylcholine receptor 自體免疫疾病，不是運動神經元退化。",
        },
    },
    54: {
        "stem": "骨骼肌 DHPR 是 T-tubule 膜上的 L-type voltage sensor/Ca2+ channel，感受去極化後機械性連動 ryanodine receptor 釋放肌漿網鈣離子。",
        "key": "Skeletal muscle DHPR 位於 T tubule membrane，是 voltage-gated Ca2+ channel/voltage sensor。",
        "reasons": {
            "A": "DHPR 不是 ligand-gated；骨骼肌興奮收縮耦合由膜電位改變啟動。",
            "B": "肌漿網上的主要鈣釋放通道是 ryanodine receptor，不是 DHPR。",
            "C": "DHPR 位於橫管膜並感受電壓變化，符合骨骼肌興奮收縮耦合。",
            "D": "肌漿網 ligand-gated 的描述放錯位置，也不是 DHPR 的主要定義。",
        },
    },
    57: {
        "stem": "大量失血使動脈壓下降，感壓受器被拉伸減少，放電頻率下降；代償反應是交感上升、副交感下降、周邊阻力增加。",
        "key": "Acute hemorrhage decreases baroreceptor firing, increases sympathetic tone, and raises TPR。",
        "reasons": {
            "A": "失血使動脈壓與血管壁伸展下降，感壓受器放電不會增加，因此最不可能。",
            "B": "交感神經活性上升會收縮靜脈、增加靜脈回流，是代償反應。",
            "C": "副交感對心臟活性下降，讓心跳加快以維持心輸出量。",
            "D": "周邊小動脈收縮使總周邊阻力上升，有助於維持血壓。",
        },
    },
    59: {
        "stem": "微血管前小動脈收縮會降低下游微血管靜水壓，使 Starling 濾過壓下降，因此液體濾出速率減少。",
        "key": "Precapillary arteriolar constriction lowers capillary hydrostatic pressure and filtration。",
        "reasons": {
            "A": "前小動脈收縮會讓進入微血管的壓力下降，不會增加微血管靜水壓。",
            "B": "微血管靜水壓降低會使濾過速率下降，符合 Starling forces。",
            "C": "血漿膠體滲透壓主要由血漿蛋白決定，前小動脈短暫收縮不會使其顯著增加。",
            "D": "組織間液膠體滲透壓取決於間質蛋白，並非前小動脈收縮的直接顯著變化。",
        },
    },
    60: {
        "stem": "氣道從傳導部進入呼吸部後才有氣體交換。肺泡與呼吸性細支氣管有肺泡結構可交換氣體；支氣管與末端細支氣管屬傳導部。",
        "key": "Gas exchange occurs in alveoli and respiratory bronchioles, not bronchi or terminal bronchioles。",
        "reasons": {
            "A": "支氣管只傳導空氣，不能進行有效氣體交換，所以 12 包含錯誤項目。",
            "B": "肺泡與呼吸性細支氣管都屬呼吸部，可進行氣體交換。",
            "C": "末端細支氣管仍屬傳導部，沒有肺泡開口進行交換，所以 234 不正確。",
            "D": "支氣管與末端細支氣管都不是交換部，134 排除肺泡也不合理。",
        },
    },
    61: {
        "stem": "在相同 PCO2 下，氧合程度會影響血紅素攜帶 CO2 的能力。去氧血紅素較能形成 carbaminohemoglobin，這是 Haldane effect。",
        "key": "Haldane effect: deoxygenated Hb carries more CO2; high PO2 blood has less carbaminohemoglobin。",
        "reasons": {
            "A": "即使 PCO2 相同，低氧血因 Haldane effect 可攜帶較多 CO2，總含量不一定相同。",
            "B": "甲管 PO2 100 mmHg、血紅素較氧合，carbaminohemoglobin 比例會低於 PO2 40 mmHg 的乙管。",
            "C": "乙管 PO2 40 mmHg 較接近混合靜脈血，不是體動脈血。",
            "D": "此題差異主要是 Haldane effect；Bohr effect 是 CO2/H+ 影響血紅素對氧親和力。",
        },
    },
    62: {
        "stem": "總肺容量(TLC)包含所有肺容積，扣掉肺餘容積(RV)後，就是最大呼氣可吐出的肺活量(VC)。",
        "key": "Vital capacity = total lung capacity - residual volume。",
        "reasons": {
            "A": "TLC 與 RV 的差值等於肺活量，也就是最大吸氣後可呼出的總量。",
            "B": "吸氣儲備容積只是平靜吸氣後還可再吸入的量，不包含全部可呼出量。",
            "C": "潮氣容積是平靜呼吸每次進出的量，遠小於 TLC-RV。",
            "D": "功能性肺餘容量是平靜呼氣後肺內剩餘量，等於 ERV+RV。",
        },
    },
    63: {
        "stem": "排便反射涉及直腸擴張感受、腸神經叢與薦髓副交感傳出。官方答案採副交感膽鹼性傳出參與內肛括約肌與直腸反射調控的概念。",
        "key": "排便反射由直腸伸展、腸神經與 pelvic parasympathetic reflex 共同調控；外肛括約肌為隨意骨骼肌。",
        "reasons": {
            "A": "直腸壓力訊息主要進入腸肌神經叢與薦髓反射路徑，不是只傳到黏膜下神經叢。",
            "B": "直腸平滑肌的排便反射以副交感與腸神經調控為主，不是腰椎神經釋放 epinephrine 促動。",
            "C": "外肛括約肌是骨骼肌，受陰部神經隨意控制，不能和內肛括約肌一起用腸神經 NO 解釋。",
            "D": "副交感膽鹼性活動參與排便反射，促進直腸收縮並調整內肛括約肌反應，是官方接受的選項。",
        },
    },
    64: {
        "stem": "Trypsin 是胰酵素活化串聯的核心，可活化多種胰蛋白酶原類酵素與 procolipase；但 deoxyribonuclease 通常不靠 trypsin 活化。",
        "key": "Trypsin activates procolipase, procarboxypeptidases, proelastase 等；DNase 不屬此活化串聯重點。",
        "reasons": {
            "A": "Procolipase 可由 trypsin 活化成 colipase，協助 pancreatic lipase 作用。",
            "B": "Procarboxypeptidase B 可由 trypsin 活化成 carboxypeptidase B。",
            "C": "Proelastase 是 trypsin 活化的胰蛋白水解酵素前驅物之一。",
            "D": "Deoxyribonuclease 為核酸分解酵素，不是 trypsin 典型活化的酵素原。",
        },
    },
    65: {
        "stem": "逆流倍增靠亨利氏環上升段粗枝主動再吸收 NaCl，特別是 NKCC2 與 Na-K ATPase，建立髓質滲透壓梯度。題目問錯誤，C 把運輸蛋白與方向都寫錯。",
        "key": "Thick ascending limb reabsorbs NaCl via NKCC2; it does not secrete NaCl into the tubular lumen via NCC。",
        "reasons": {
            "A": "逆流機制的目的正是建立並維持髓質垂直滲透壓梯度，利於濃縮尿液。",
            "B": "上升段粗枝以基底外側 Na-K ATPase 提供能量，驅動 NaCl 再吸收。",
            "C": "上升段粗枝使用 Na-K-2Cl cotransporter 將離子由管腔再吸收，不是用 Na-Cl cotransporter 分泌到管腔。",
            "D": "直管以逆流交換保存髓質梯度，避免血流把梯度洗掉。",
        },
    },
    66: {
        "stem": "鈉再吸收在各段腎小管有固定 transporter：近端以 SGLT 等共同運輸，上升段粗枝用 NKCC2，遠曲小管用 NCC，ENaC 主要在晚遠曲與集尿管。",
        "key": "Thin ascending limb 不是 ENaC 主要作用處；ENaC 在 late distal tubule/collecting duct。",
        "reasons": {
            "A": "近端小管大量鈉再吸收，包含鈉-葡萄糖共同轉運蛋白，是正確方向。",
            "B": "亨利氏環上升段粗枝使用 Na-K-2Cl cotransporter，對袢利尿劑敏感。",
            "C": "上升段細枝不是上皮鈉通道的典型位置，因此此敘述錯誤。",
            "D": "遠曲小管使用 Na-Cl cotransporter，對 thiazide 類利尿劑敏感。",
        },
    },
    67: {
        "stem": "Aldosterone 與 testosterone 是類固醇，1,25-dihydroxycholecalciferol 是維生素 D 衍生的 secosteroid；thyroxine 是碘化酪胺酸衍生物，化學屬性不同。",
        "key": "Thyroxine is an iodinated tyrosine derivative; the others are steroid/secosteroid hormones。",
        "reasons": {
            "A": "Aldosterone 是腎上腺皮質製造的礦物皮質類固醇。",
            "B": "1,25-dihydroxycholecalciferol 由維生素 D 轉化，屬 secosteroid 類訊號分子。",
            "C": "Thyroxine 是含碘酪胺酸衍生物，不屬類固醇骨架，因此與其他三者不同。",
            "D": "Testosterone 是性腺製造的類固醇荷爾蒙。",
        },
    },
    69: {
        "stem": "血鉀升高會直接刺激腎上腺皮質球狀帶分泌 aldosterone，促進遠端腎元排鉀並保鈉。",
        "key": "Hyperkalemia directly increases aldosterone secretion from zona glomerulosa。",
        "reasons": {
            "A": "ADH 主要受血漿滲透壓與有效循環量調控，核心作用是水分再吸收。",
            "B": "Angiotensinogen 由肝臟製造，是 RAAS 前驅蛋白，不是高血鉀最直接上升的激素。",
            "C": "Aldosterone 對高血鉀反應明顯，可增加集尿管主細胞鉀分泌。",
            "D": "ANP 主要因心房伸展增加而分泌，促進排鈉，與高血鉀直接調控不如 aldosterone。",
        },
    },
    70: {
        "stem": "甲狀腺激素脂溶性高，血中多與結合蛋白運送，游離型進入細胞後主要結合核內受器調控基因轉錄。題目問錯誤，細胞膜受器說法不對。",
        "key": "Free thyroid hormone binds intracellular/nuclear receptors, not primarily cell membrane receptors。",
        "reasons": {
            "A": "T3/T4 在血中多與 TBG、transthyretin、albumin 等蛋白結合運送。",
            "B": "游離型甲狀腺激素進入細胞後作用於核內受器，不是主要結合細胞膜受器。",
            "C": "甲狀腺激素半衰期較多數胜肽荷爾蒙長，尤其 T4 更明顯。",
            "D": "甲狀腺激素受器作為轉錄調節因子，可改變標的基因轉錄。",
        },
    },
    71: {
        "stem": "催產素由下視丘製造、後葉釋放，主要促進子宮收縮與乳腺肌上皮細胞收縮，造成排乳反射。",
        "key": "Oxytocin causes milk ejection and uterine contraction。",
        "reasons": {
            "A": "催產素促進子宮平滑肌收縮，不是促進子宮鬆弛。",
            "B": "催產素使乳腺肌上皮細胞收縮，把乳汁推出乳腺管，是主要作用之一。",
            "C": "抑制黃體分解不是人類催產素的主要生理考點。",
            "D": "抑制 PGF2α 分泌不是催產素在此題要考的核心作用。",
        },
    },
    72: {
        "stem": "Klinefelter syndrome 多為 47,XXY，睪丸發育不全造成低 testosterone 與精子稀少；因性腺功能低下，LH/FSH 會代償性升高。",
        "key": "Klinefelter syndrome 是 hypergonadotropic hypogonadism：low testosterone with high LH/FSH。",
        "reasons": {
            "A": "47,XXY 是最常見核型，符合 Klinefelter syndrome。",
            "B": "曲細精管功能不良常導致寡精或無精，造成不孕。",
            "C": "睪固酮分泌偏低是性腺功能低下的結果。",
            "D": "LH 與 FSH 通常因負回饋不足而升高，不是降低，因此為錯誤敘述。",
        },
    },
    73: {
        "stem": "高 prolactin 會抑制 GnRH，進而降低 LH/FSH 與 testosterone，造成性功能障礙。藥物、腦下垂體腫瘤或下視丘-垂體柄病灶都可造成高泌乳素；隱睪症不會解釋 prolactin 150 ng/mL。",
        "key": "Hyperprolactinemia suppresses GnRH; cryptorchidism causes testicular problems but not marked prolactin elevation。",
        "reasons": {
            "A": "抑制 dopamine 會移除對 prolactin 的抑制，使 prolactin 上升並降低性腺軸功能。",
            "B": "腦下垂體 prolactinoma 可直接造成高 prolactin 與低 testosterone。",
            "C": "靠近腦下垂體的下視丘或垂體柄病灶會阻斷 dopamine 抑制，也可使 prolactin 上升。",
            "D": "隱睪症可影響睪丸生精或功能，但不能解釋明顯高 prolactin，因此最不可能。",
        },
    },
    75: {
        "stem": "雙硫鍵由兩個 cysteine 側鏈的 thiol 氧化形成 cystine。Methionine 雖含硫，但其硫是 thioether，不形成典型蛋白質雙硫鍵。",
        "key": "Disulfide bonds form between cysteine residues, not methionine residues。",
        "reasons": {
            "A": "甲硫胺酸側鏈硫原子不具形成雙硫鍵所需的 thiol，因此此敘述錯誤。",
            "B": "強還原劑可把雙硫鍵還原成兩個 thiol，使鍵結斷裂。",
            "C": "雙硫鍵可限制蛋白質構形，提高許多蛋白質的穩定性。",
            "D": "雙硫鍵異構酶可協助錯配雙硫鍵重排，是蛋白質摺疊的重要酵素。",
        },
    },
    76: {
        "stem": "Glycine 在高 pH 強鹼環境下，羧基去質子化為 COO-，胺基也失去質子成 NH2，因此 pH 12 時主要型態是 NH2-CH2-COO-。",
        "key": "At strongly basic pH, glycine is mainly NH2-CH2-COO-。",
        "reasons": {
            "A": "NH3+-CH2-COOH 是強酸環境下較質子化的型態，不符合 pH 12。",
            "B": "NH2-CH2-COO- 同時呈去質子化羧酸鹽與中性胺基，符合強鹼完成滴定後主要型態。",
            "C": "NH2-CH3+-COO- 結構本身把主鏈寫錯，glycine 中間應為 CH2。",
            "D": "NH3+-CH2-COO- 是接近等電點附近的 zwitterion，高 pH 下胺基會去質子化。",
        },
    },
    77: {
        "stem": "素食合併惡性貧血指向維生素 B12 缺乏。B12 又稱 cobalamin，核心金屬離子是鈷；吸收需要胃壁細胞分泌的 intrinsic factor。",
        "key": "Vitamin B12 contains cobalt and requires gastric intrinsic factor for ileal absorption。",
        "reasons": {
            "A": "Cyanocobalamin 是補充劑或儲存形式之一，活性輔酶型主要是 methylcobalamin 與 adenosylcobalamin，不是必須含氰基才活化。",
            "B": "B12 的金屬不是鐵；含鐵的代表是 heme 類分子。",
            "C": "Cobalamin 名稱即來自其含鈷離子，符合題目問的含金屬水溶性維生素。",
            "D": "促進 B12 吸收的 intrinsic factor 由胃壁細胞分泌，吸收位置在末端迴腸，不是小腸壁細胞分泌。",
        },
    },
    79: {
        "stem": "雙股 DNA 加熱到高溫會變性，主要破壞鹼基間氫鍵與鹼基堆疊，使雙股解旋並產生 260 nm 吸光度上升的 hyperchromic effect；一般不會斷裂 N-glycosidic covalent bond。",
        "key": "DNA heat denaturation disrupts hydrogen bonds/base stacking, not N-glycosidic covalent bonds。",
        "reasons": {
            "A": "雙股解開後鹼基暴露，UV 260 nm 吸光度會增加，稱 hyperchromicity。",
            "B": "N-醣苷共價鍵連接鹼基與去氧核糖，單純加熱變性不會把此共價鍵當作主要斷裂目標。",
            "C": "高溫會使雙股螺旋解開，這正是 DNA denaturation 的表現。",
            "D": "在中性水溶液中加熱變性通常仍維持溶解，不等於 DNA 沉澱。",
        },
    },
    80: {
        "stem": "DNA polymerase 只能從既有核酸鏈的 3'-OH 端延長，不能從零開始合成。因此複製需要 RNA primer 提供可延伸的 3'-OH。",
        "key": "DNA polymerase requires a free 3'-OH supplied by RNA primer。",
        "reasons": {
            "A": "聚合反應需要的是 3'-OH 攻擊 incoming dNTP 的磷酸，不是 3'-端磷酸基。",
            "B": "RNA 引子提供自由 3'-OH，讓 DNA polymerase 可以開始延長。",
            "C": "5'-OH 不是 DNA polymerase 延長反應的攻擊端。",
            "D": "5'-磷酸基可參與後續連接或鏈方向性描述，但不是啟動聚合所需端點。",
        },
    },
    81: {
        "stem": "人類染色體很長，若每條只有一個複製原點會來不及完成 S phase。真核染色體有多個 replication origins 同步或分時啟動。",
        "key": "Each human chromosome has many replication origins, far more than three。",
        "reasons": {
            "A": "單一複製原點是細菌環狀染色體常見概念，不適用人類每條染色體。",
            "B": "兩個複製原點仍遠低於真核大型染色體所需數量。",
            "C": "三個複製原點不足以支撐人類染色體在 S phase 完成複製。",
            "D": "人類每條染色體有多個複製原點，數量明顯大於三個。",
        },
    },
    82: {
        "stem": "Ras 是小 GTPase，活化時結合 GTP，失活時水解成 GDP。Ras 的膜定位靠 C 端 CAAX motif 的 cysteine 被 farnesylation，不是 N 端胺基與 farnesyl 結合。",
        "key": "Ras farnesylation occurs on a C-terminal cysteine in the CAAX motif, not the N-terminal amino group。",
        "reasons": {
            "A": "Ras 突變若使 GTP 水解受阻，會持續傳遞增生訊號，常見於癌症。",
            "B": "Ras 經 prenylation 等修飾後可附著於細胞膜內側，利於訊號傳遞。",
            "C": "Farnesyl 接在 Ras C 端 CAAX motif 的 cysteine，不是 N 端氨基，因此此敘述錯誤。",
            "D": "Farnesyl 屬 isoprenoid，和膽固醇合成都使用 mevalonate pathway 相關前驅物。",
        },
    },
    83: {
        "stem": "α-amanitin 對真核 RNA polymerase 的抑制以 RNA polymerase II 最敏感；Pol III 需較高濃度，Pol I 相對不敏感。",
        "key": "RNA polymerase II is most sensitive to alpha-amanitin。",
        "reasons": {
            "A": "RNA polymerase I 主要合成大型 rRNA 前驅物，對 α-amanitin 相對不敏感。",
            "B": "RNA polymerase II 合成 mRNA 前驅物，對 α-amanitin 最敏感。",
            "C": "RNA polymerase III 合成 tRNA 與 5S rRNA 等，抑制敏感度低於 Pol II。",
            "D": "Reverse transcriptase 是 RNA-dependent DNA polymerase，不是此毒素敏感性分類中的真核 RNA polymerase。",
        },
    },
    85: {
        "stem": "Hyaluronic acid 是非硫酸化 glycosaminoglycan，重複雙醣單位為 D-glucuronic acid 與 N-acetylglucosamine。",
        "key": "Hyaluronic acid repeats D-glucuronic acid + N-acetylglucosamine。",
        "reasons": {
            "A": "Galactose 加 N-acetylgalactosamine 較像某些其他醣胺聚醣組合，不是透明質酸。",
            "B": "Glucose 與 fructose 是一般單醣組合，不能構成 hyaluronic acid 的典型重複單位。",
            "C": "D-glucuronic acid 與 N-acetylglucosamine 正是 hyaluronic acid 的重複雙醣。",
            "D": "N-acetylgalactosamine 出現在 chondroitin sulfate 等分子中，透明質酸用的是 N-acetylglucosamine。",
        },
    },
    86: {
        "stem": "胰島素是進食後促進儲存與利用葡萄糖的荷爾蒙，會促進骨骼肌與脂肪細胞 GLUT4 轉位，增加葡萄糖攝取。",
        "key": "Insulin stimulates GLUT4-mediated glucose uptake in muscle and adipose tissue。",
        "reasons": {
            "A": "胰島素傾向活化 phosphodiesterase、降低 cAMP；抑制 PDE 比較像升高 cAMP 的方向。",
            "B": "胰島素會增加肝細胞 fructose-2,6-bisphosphate，促進糖解並抑制糖質新生。",
            "C": "胰島素促進糖解、肝醣合成與脂肪合成，不是抑制肝細胞糖解。",
            "D": "胰島素刺激 GLUT4 移到肌肉細胞膜，增加葡萄糖進入細胞。",
        },
    },
    87: {
        "stem": "紅血球糖解支路產生 2,3-BPG，它結合去氧血紅素並降低血紅素對氧的親和力，使氧解離曲線右移。",
        "key": "2,3-BPG decreases hemoglobin O2 affinity and promotes oxygen unloading。",
        "reasons": {
            "A": "1,3-bisphosphoglycerate 是糖解中間物，可產 ATP，但不是調節 Hb 氧親和力的主要分子。",
            "B": "2,3-bisphosphoglycerate 會結合 Hb，降低氧親和力，是本題答案。",
            "C": "Fructose 1,6-bisphosphate 是糖解早期中間物，不直接調節血紅素帶氧能力。",
            "D": "Fructose 2,6-bisphosphate 調節 PFK-1 與糖質新生，與 Hb 氧親和力無直接關係。",
        },
    },
    88: {
        "stem": "受質階層磷酸化是高能中間物直接把磷酸轉給 ADP/GDP。PEP、1,3-BPG 與 succinyl-CoA 可直接產生 ATP/GTP；2-phosphoglycerate 不能直接做到。",
        "key": "2-phosphoglycerate is not a direct substrate-level phosphorylation donor。",
        "reasons": {
            "A": "2-phosphoglycerate 需先轉成 phosphoenolpyruvate，自己不能直接生成 ATP。",
            "B": "Phosphoenolpyruvate 經 pyruvate kinase 可直接產生 ATP。",
            "C": "Succinyl-CoA 經 succinyl-CoA synthetase 可產生 GTP，屬 TCA 的受質階層磷酸化。",
            "D": "1,3-bisphosphoglycerate 經 phosphoglycerate kinase 可直接產生 ATP。",
        },
    },
    89: {
        "stem": "奇數碳脂肪酸 beta-oxidation 最後形成 propionyl-CoA，經 carboxylation 與重排後變成 succinyl-CoA 進入 TCA cycle。",
        "key": "Odd-chain fatty acids enter the TCA cycle as succinyl-CoA after propionyl-CoA conversion。",
        "reasons": {
            "A": "Alpha-ketoglutarate 是 TCA 中間物，但不是 propionyl-CoA 轉入循環的直接入口。",
            "B": "Succinyl-CoA 是奇數碳脂肪酸三碳產物轉換後進入 TCA 的形式。",
            "C": "Oxaloacetate 可由某些胺基酸或丙酮酸羧化形成，不是此路徑的直接產物。",
            "D": "Propionyl-CoA 是 beta-oxidation 最後三碳片段，但需先轉成 succinyl-CoA 才進入 TCA。",
        },
    },
    91: {
        "stem": "Glycophorin 是紅血球膜上的穿膜糖蛋白，其醣鏈位於細胞外側，參與紅血球表面負電荷與血型抗原呈現。醣鏈不會接在細胞質面的胺基酸殘基上。",
        "key": "Glycophorin oligosaccharides are exposed on the extracellular surface, not the cytoplasmic face。",
        "reasons": {
            "A": "Glycophorin 是紅血球膜 integral membrane protein，具有穿膜區段。",
            "B": "醣鏈位在細胞外面，因為糖基化發生在 ER/Golgi 腔側；細胞質面連醣的說法錯誤。",
            "C": "穿膜區通常由非極性胺基酸形成 alpha helix，讓蛋白跨越脂質雙層。",
            "D": "紅血球表面寡糖決定 ABO 等血型抗原，糖蛋白與糖脂都可承載相關醣鏈。",
        },
    },
    92: {
        "stem": "小腸腔側葡萄糖進入上皮細胞主要靠 SGLT1，利用鈉離子順電化學梯度共同運輸葡萄糖，屬次級主動運輸。",
        "key": "Apical intestinal glucose uptake uses Na+-glucose symport via SGLT1。",
        "reasons": {
            "A": "促進性擴散主要是 GLUT 介導，常見於基底側葡萄糖離開腸上皮細胞。",
            "B": "葡萄糖與鈉離子同向進入細胞，不是反向交換運輸。",
            "C": "SGLT1 讓 Na+ 與 glucose 共同運輸進入小腸上皮細胞，是正確機制。",
            "D": "葡萄糖本身不是由 ATPase 直接泵入細胞；能量間接來自 Na-K ATPase 維持鈉梯度。",
        },
    },
    93: {
        "stem": "Glucogenic amino acids 可轉成 TCA 中間物。Histidine 代謝最後進入 glutamate，再成 alpha-ketoglutarate，不是 succinyl-CoA。",
        "key": "Histidine is converted to glutamate and then alpha-ketoglutarate, not succinyl-CoA。",
        "reasons": {
            "A": "Glutamate 可經轉胺或氧化脫胺成 alpha-ketoglutarate，配對正確。",
            "B": "Histidine 的 glucogenic 入口是 glutamate/alpha-ketoglutarate，配 succinyl-CoA 錯誤。",
            "C": "Aspartate 可轉成 oxaloacetate，是典型 glucogenic 路徑。",
            "D": "Tyrosine 可分解產生 fumarate，同時也有 ketogenic 成分，這個配對可成立。",
        },
    },
    94: {
        "stem": "長期高蛋白但低澱粉攝取會使胰島素低、脂肪酸氧化與肝臟 ketogenesis 增加，血中酮體上升。",
        "key": "Very low carbohydrate intake promotes fatty acid oxidation and ketone body production。",
        "reasons": {
            "A": "高蛋白攝取會增加胺基酸氮負荷，尿素生成與尿中尿素通常增加，不會顯著減少。",
            "B": "極少澱粉使身體偏動員脂肪作能量，不是單純大量累積脂肪。",
            "C": "低醣狀態促進脂肪酸 beta-oxidation 與酮體生成，血中酮體會升高。",
            "D": "酮體增加偏向代謝性酸負荷，不是典型代謝性鹼中毒。",
        },
    },
    95: {
        "stem": "電子傳遞鏈最後階段是 complex IV 將電子傳給氧氣並還原成水。Complex IV 又稱 cytochrome c oxidase。",
        "key": "Cytochrome c oxidase = complex IV, the terminal enzyme reducing O2 to H2O。",
        "reasons": {
            "A": "Cytochrome oxidase 位於電子傳遞鏈末端，負責把電子交給氧氣。",
            "B": "Succinate dehydrogenase 是 complex II，負責把 FADH2 電子送入 ubiquinone，不是最後階段。",
            "C": "Ubiquinone:cytochrome c oxidoreductase 是 complex III，位在 complex IV 之前。",
            "D": "NADH dehydrogenase 是 complex I，是 NADH 電子進入傳遞鏈的起點之一。",
        },
    },
    96: {
        "stem": "被荷爾蒙活化的 phospholipase C 會切 PIP2，產生 DAG 與 IP3。DAG 活化 PKC，IP3 促進內質網釋放鈣離子，使細胞質鈣上升；題目問錯誤故選 D。",
        "key": "PLC cleaves PIP2 into DAG and IP3; IP3 increases cytosolic Ca2+。",
        "reasons": {
            "A": "PLC 的典型受質是 phosphatidylinositol 4,5-bisphosphate，也就是 PIP2。",
            "B": "DAG 留在膜上並活化 protein kinase C，是 PLC 訊號的重要分支。",
            "C": "許多 Gq-coupled receptors 可活化 PLC-beta，屬 G protein 連結受器路徑。",
            "D": "IP3 會促進內質網釋放 Ca2+，使細胞質鈣濃度增加，不是減少。",
        },
    },
    98: {
        "stem": "Ras 活化狀態取決於是否結合 GTP。致癌性 Ras 突變常使 GTP 水解失效，尤其無法被 GAP 有效促進水解，因此長時間停留在 GTP-bound 活化狀態。",
        "key": "Oncogenic Ras remains active because GAP-stimulated GTP hydrolysis is impaired。",
        "reasons": {
            "A": "若只是增加 GDP 親和力，Ras 會偏失活狀態，不能解釋持續活化。",
            "B": "突變 Ras 不受 GAP 正常促進 GTP 水解調控，會維持活化訊號。",
            "C": "膜受體與激素結合能力下降會減少上游刺激，並非 Ras 自身持續活化原因。",
            "D": "Ras 是小 GTPase，不是典型異三聚體 G protein；增加受體與 G protein 結合不是主要機轉。",
        },
    },
    99: {
        "stem": "Genomic library 是把基因組 DNA 切割後接入載體保存，因此需要 restriction enzymes、DNA ligase 與載體如 lambda phage。Reverse transcriptase 是製作 cDNA library 時由 mRNA 反轉錄才需要。",
        "key": "Genomic library uses genomic DNA fragments; reverse transcriptase is for cDNA library construction。",
        "reasons": {
            "A": "DNA ligase 用於把基因組 DNA 片段接入載體，是建立 genomic library 會用到的材料。",
            "B": "Bacteriophage lambda 可作為容納 DNA 片段的載體，適合 library 建構。",
            "C": "Reverse transcriptase 用於由 RNA 製作 cDNA，不是建立 genomic library 的必要材料。",
            "D": "Restriction enzymes 可切割 genomic DNA 與載體，產生可連接的片段。",
        },
    },
}


def make_explanation(entry):
    reasons = entry["reasons"]
    return (
        f"【題幹解析】{entry['stem']}\n\n"
        "【選項詳解】\n"
        f"- A. {reasons['A']}\n"
        f"- B. {reasons['B']}\n"
        f"- C. {reasons['C']}\n"
        f"- D. {reasons['D']}\n\n"
        f"【核心考點】{entry['key']}"
    )


def main():
    if len(TARGETS) != 79:
        raise SystemExit(f"target count mismatch: {len(TARGETS)}")
    missing = sorted(set(TARGETS) - set(ENTRIES))
    extra = sorted(set(ENTRIES) - set(TARGETS))
    if missing or extra:
        raise SystemExit(f"entry mismatch missing={missing} extra={extra}")

    data = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    by_number = {q["question_number"]: q for q in data["questions"]}
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for index, batch in enumerate(BATCHES, start=1):
        updates = []
        for number in batch:
            q = by_number[number]
            entry = ENTRIES[number]
            key = entry["key"]
            front = q.get("flashcard_front") or q["question_text"].strip()
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": number,
                    "explanation": make_explanation(entry),
                    "key_point": key,
                    "flashcard_front": front,
                    "flashcard_back": key,
                    "flashcard_summary": f"{front} -> {key}",
                    "review_status": "ai_generated",
                    "explanation_model": "codex-high-quality-rewrite",
                    "explanation_generated_at": GENERATED_AT,
                    "manual_review_notes": entry.get("notes", []),
                }
            )

        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": min(batch), "end": max(batch)},
            "updates": updates,
        }
        out_path = OUT_DIR / f"q{min(batch):03d}-q{max(batch):03d}_sparse{index:02d}.json"
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {len(BATCHES)} sparse update files for {len(TARGETS)} questions to {OUT_DIR}")


if __name__ == "__main__":
    main()
