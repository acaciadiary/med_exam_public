import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/108-1/medicine-1.json"
DATASET_ID = "108-1_medicine-1"
OUT_DIR = Path("scratch/rewrite_updates/108-1_medicine-1_selected")
STAMP = "2026-07-20T00:00:00+08:00"


BATCHES = [
    [1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
    [12, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    [24, 27, 29, 30, 31, 32, 33, 35, 36, 37],
    [38, 39, 41, 42, 43, 45, 46, 47, 48, 51],
    [52, 53, 54, 55, 56, 57, 60, 61, 62, 63],
    [64, 65, 66, 67, 68, 69, 70, 71, 72, 73],
    [74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
    [85, 86, 87, 88, 89, 90, 91, 92, 93, 94],
    [95, 97, 98, 99, 100],
]


ENTRIES = {
    1: {
        "stem": "本題是小腦傳入、傳出路徑的否定式題。背側脊髓小腦徑傳遞同側本體感覺，起自 Clarke's column，經下小腦腳進入小腦；它不是先左右交叉後再進入小腦，所以官方答案為 B。",
        "core": "背側脊髓小腦徑是同側、不交叉、經下小腦腳入小腦；中小腦腳主要是橋腦核到小腦的纖維，上小腦腳以輸出為主但也含部分傳入纖維。",
        "reasons": {
            "A": "Clarke's column（nucleus thoracicus）是背側脊髓小腦徑的重要起點，這句正確，不是本題要找的錯誤項。",
            "B": "背側脊髓小腦徑通常保持同側上行，經下小腦腳入小腦；「左右交叉後」是錯誤關鍵，因此選 B。",
            "C": "上小腦腳主要承載小腦輸出纖維，但也有腹側脊髓小腦徑等傳入纖維，說含進、出纖維可以成立。",
            "D": "中小腦腳由橋腦核發出的橋小腦纖維構成，是大腦皮質訊息進入小腦的重要通路，敘述正確。",
        },
    },
    2: {
        "stem": "喉外神經是上喉神經的外支，主要支配環甲肌。甲狀腺手術傷到它時，病人較會出現高音發聲或張力調節受損，因此答案是 A。",
        "core": "上喉神經外支支配環甲肌；多數喉內肌由迷走神經的返喉神經支配。",
        "reasons": {
            "A": "環甲肌由喉外神經支配，負責拉緊聲帶、調高音調，受傷時最直接受影響。",
            "B": "甲杓肌屬多數喉內肌，主要由返喉神經支配，不是喉外神經的代表肌肉。",
            "C": "後環杓肌是外展聲帶的重要肌肉，也由返喉神經支配，傷喉外神經不會以它為主。",
            "D": "外側環杓肌負責內收聲帶，支配來源仍是返喉神經，不是本題所問的喉外神經。",
        },
    },
    4: {
        "stem": "兩眼向正上方看主要靠上直肌與下斜肌共同作用，兩者皆由動眼神經支配。題目問同時上視的腦神經，答案是 C。",
        "core": "動眼神經支配上直肌、下直肌、內直肌、下斜肌與提上眼瞼肌；滑車神經支配上斜肌，外展神經支配外直肌。",
        "reasons": {
            "A": "眼神經是三叉神經第一支，主要負責眼眶、額部與鼻背感覺，不支配眼球運動肌。",
            "B": "滑車神經支配上斜肌，主要使眼球內轉時下視，不是雙眼正上視的主力。",
            "C": "動眼神經支配上直肌與下斜肌，兩眼正上方凝視需要這些肌肉協調，因此為答案。",
            "D": "外展神經只支配外直肌，功能是眼球外展，與正上視不符。",
        },
    },
    5: {
        "stem": "胸骨柄後方的上縱隔有主動脈弓及其分支。正中胸骨柄穿刺最容易傷及位在其後方的主動脈弓，答案為 A。",
        "core": "胸骨柄後方對應上縱隔，重要構造包括主動脈弓、頭臂靜脈與氣管等；心室與肺動脈幹位置較低。",
        "reasons": {
            "A": "主動脈弓位於上縱隔、胸骨柄後方，是胸骨柄正中穿刺最需擔心的血管。",
            "B": "左心室主要構成心臟左下外形，位置比胸骨柄低，較接近心尖區。",
            "C": "肺動脈幹位於胸骨體後方、較主動脈弓低，並非胸骨柄正中最可能傷及者。",
            "D": "上腔靜脈在右上縱隔，偏右側，正中胸骨柄後方最典型對應不是它。",
        },
    },
    6: {
        "stem": "胎兒臍靜脈閉鎖後形成肝圓韌帶，位於肝鐮韌帶游離緣內。題目問臍靜脈的殘跡，答案是 B。",
        "core": "臍靜脈殘跡是肝圓韌帶；臍動脈殘跡主要形成內側臍韌帶，尿膜管殘跡是正中臍韌帶。",
        "reasons": {
            "A": "肝鐮韌帶是腹膜皺襞，本身不是臍靜脈閉鎖後的索狀殘跡。",
            "B": "肝圓韌帶就是左臍靜脈出生後閉鎖形成的結構，最符合題意。",
            "C": "冠狀韌帶是肝臟與橫膈之間的腹膜反摺，與臍靜脈殘跡無關。",
            "D": "正中臍韌帶來自尿膜管（urachus），不是臍靜脈。",
        },
    },
    7: {
        "stem": "橫膈有三個常考開口：T8 下腔靜脈孔穿中央腱，T10 食道裂孔穿肌部，T12 主動脈裂孔在正中弓狀韌帶後方。答案是 B。",
        "core": "T8 IVC 穿中央腱；T10 esophagus；T12 aorta。",
        "reasons": {
            "A": "主動脈經 T12 主動脈裂孔通過，位於橫膈腳後方，不穿中央腱。",
            "B": "下腔靜脈穿過 T8 的腔靜脈孔，這個孔位於橫膈中央腱。",
            "C": "食道穿 T10 食道裂孔，位置在右膈腳肌纖維形成的開口，不是中央腱。",
            "D": "肝門靜脈進入肝門，不是典型穿越橫膈中央腱的構造。",
        },
    },
    8: {
        "stem": "陰部神經與內陰部血管在坐骨肛門窩外側壁的陰部管（Alcock canal）內行走，因此答案是 B。",
        "core": "坐骨肛門窩外側壁含閉孔內肌筋膜與陰部管，陰部神經位於其中。",
        "reasons": {
            "A": "內側壁主要由外肛門括約肌與提肛肌相關結構形成，不是陰部管所在處。",
            "B": "陰部神經在外側壁的陰部管內走行，伴隨內陰部動、靜脈。",
            "C": "上側壁接近骨盆底肌，不是陰部神經在坐骨肛門窩的典型位置。",
            "D": "後側壁不是陰部管的主要解剖定位，不能作為本題答案。",
        },
    },
    9: {
        "stem": "下肢表淺靜脈中，大隱靜脈沿足背內側、內踝前方與大腿內側上行；小隱靜脈偏後外側。答案是 A。",
        "core": "大隱靜脈走內側並注入股靜脈；小隱靜脈走後方注入膕靜脈。",
        "reasons": {
            "A": "大隱靜脈是下肢內側表淺靜脈，從內踝前方一路上行至股靜脈。",
            "B": "小隱靜脈主要在小腿後側上行，最後進入膕靜脈，不是內側主幹。",
            "C": "膕靜脈位於膕窩深部，屬深靜脈，不能用「走在下肢內側」來描述。",
            "D": "股靜脈位於大腿深部的股三角與內收肌管中，不是本題常考的內側表淺走向。",
        },
    },
    10: {
        "stem": "肱骨外科頸繞行腋神經與後旋肱動脈。此處骨折最容易傷及腋神經，造成三角肌、小圓肌功能與肩外側感覺受損，答案是 D。",
        "core": "肱骨外科頸骨折對應腋神經；肱骨幹橈神經溝對應橈神經；內上髁對應尺神經。",
        "reasons": {
            "A": "肌皮神經穿喙肱肌後支配前臂屈肌群，典型受傷點不是肱骨外科頸。",
            "B": "正中神經與肱動脈同行於手臂前內側，肱骨外科頸骨折不是最典型傷害位置。",
            "C": "尺神經較常在肱骨內上髁附近受傷，不是外科頸骨折首選。",
            "D": "腋神經穿四邊孔並繞肱骨外科頸，該處骨折最容易使它受損。",
        },
    },
    11: {
        "stem": "跗骨隧道位於內踝後方，內含 tibialis posterior、flexor digitorum longus、posterior tibial vessels、tibial nerve、flexor hallucis longus。若所有肌腱受傷，腳趾屈曲最受影響，答案是 A。",
        "core": "跗骨隧道記憶口訣 Tom, Dick, And Very Nervous Harry；其中 FDL 與 FHL 負責腳趾屈曲。",
        "reasons": {
            "A": "屈趾長肌與屈拇長肌都經跗骨隧道，切斷後腳趾屈曲明顯受損。",
            "B": "伸趾肌腱位於踝前方伸肌支持帶下，不走內踝跗骨隧道。",
            "C": "趾內收主要屬足底內在肌功能，不是跗骨隧道內所有肌腱受傷的主表現。",
            "D": "趾外展也主要由足底內在肌完成，和跗骨隧道內長肌腱不是最直接對應。",
        },
    },
    12: {
        "stem": "題目問與邊緣系統最不相關者，官方答案標示 D。不過杏仁核通常是邊緣系統核心構造之一，因此此題官方答案可能有爭議；仍依官方答案保留 D，並提醒讀者人工複核。",
        "core": "邊緣系統常包括海馬形成、穹窿、乳頭體、扣帶迴與杏仁核等；本題官方答案 D 建議人工複核。",
        "reasons": {
            "A": "齒狀迴屬海馬形成，與記憶迴路高度相關，通常屬邊緣系統範圍。",
            "B": "穹束連接海馬與乳頭體，是 Papez circuit 的重要纖維束，與邊緣系統相關。",
            "C": "乳頭體屬下視丘的一部分，也是 Papez circuit 的節點，與邊緣系統相關。",
            "D": "杏仁核在標準解剖學中通常是邊緣系統的重要成員；雖官方答案為 D，但此選項需人工複核。",
        },
    },
    15: {
        "stem": "前庭神經核與姿勢平衡、眼球反射及小腦絨球小結葉相關。它不是主要與齒狀核連繫，所以否定式答案是 C。",
        "core": "前庭神經核連到前庭脊髓徑、內側縱束與小腦前庭小腦區；齒狀核偏向小腦半球高階運動計畫輸出。",
        "reasons": {
            "A": "前庭脊髓徑來自前庭神經核，參與伸肌張力與姿勢反射，敘述正確。",
            "B": "部分前庭核纖維進入內側縱束，協調眼球運動與頭部姿勢，敘述正確。",
            "C": "前庭核主要連到絨球小結葉與 fastigial nucleus，不是小腦齒狀核，因此為錯誤項。",
            "D": "前庭眼球反射需要前庭核與眼球運動核協調，敘述正確。",
        },
    },
    16: {
        "stem": "海馬最主要皮質傳入來自內嗅皮質，經 perforant pathway 進入齒狀迴與海馬迴路。答案是 A。",
        "core": "海馬主要 afferent 來自 entorhinal cortex；海馬主要輸出經穹窿到乳頭體等結構。",
        "reasons": {
            "A": "內嗅皮質是海馬資訊輸入的主要門戶，尤其與記憶形成密切相關。",
            "B": "扣帶迴屬邊緣系統，但不是海馬最主要的直接傳入來源。",
            "C": "杏仁核與情緒記憶相關，可和海馬互動，但不是本題問的主要 afferent。",
            "D": "韁核與邊緣系統、獎賞厭惡路徑相關，並非海馬主要傳入。",
        },
    },
    17: {
        "stem": "淚腺副交感路徑來自顏面神經 greater petrosal nerve，於翼腭神經節突觸後，再經顴神經與淚腺神經到淚腺。節後纖維源自翼腭神經節，答案是 C。",
        "core": "淚腺副交感：CN VII greater petrosal nerve -> pterygopalatine ganglion -> V2/V1 分支到淚腺。",
        "reasons": {
            "A": "睫狀神經節負責瞳孔括約肌與睫狀肌副交感，不支配淚腺分泌。",
            "B": "膝神經節是顏面神經感覺神經節，不是副交感節後神經元所在處。",
            "C": "翼腭神經節是淚腺分泌副交感纖維突觸的位置，節後纖維由此發出。",
            "D": "耳神經節與腮腺分泌相關，不是淚腺的副交感節。",
        },
    },
    18: {
        "stem": "氣管前層深頸筋膜位於舌骨下肌後方，包覆甲狀腺、氣管與食道等頸部臟器。答案是 C。",
        "core": "深頸筋膜：包圍層包 SCM/trapezius；氣管前層包甲狀腺與氣管；椎前層包脊柱前肌群；頸動脈鞘包血管神經束。",
        "reasons": {
            "A": "包圍層主要包覆胸鎖乳突肌與斜方肌，不是覆蓋甲狀腺表面的筋膜層。",
            "B": "頸動脈鞘包總頸/內頸動脈、內頸靜脈與迷走神經，不包甲狀腺。",
            "C": "氣管前層位於舌骨下肌後方並包覆甲狀腺，正好對應題目描述的位置。",
            "D": "椎前層包覆椎前肌群與斜角肌，位於更深、更後方。",
        },
    },
    19: {
        "stem": "前、中顱窩硬腦膜及小腦天幕的感覺支配主要來自三叉神經分支，特別是 V1、V2、V3 的 meningeal branches。答案是 B。",
        "core": "顱內硬腦膜痛覺主要由三叉神經支配；後顱窩部分可有迷走、舌咽與上頸神經參與。",
        "reasons": {
            "A": "舌咽神經可參與部分後顱窩區域感覺，但不是前、中顱窩硬腦膜主支配。",
            "B": "三叉神經提供前、中顱窩硬腦膜與小腦天幕的重要感覺支配，最符合題意。",
            "C": "迷走神經可支配部分後顱窩硬腦膜，範圍不符合題幹前、中顱窩。",
            "D": "舌下神經是舌肌運動神經，不負責硬腦膜感覺。",
        },
    },
    20: {
        "stem": "胎兒卵圓孔位於心房中隔，讓血液由右心房進入左心房，以繞過未擴張的肺循環。答案是 C。",
        "core": "卵圓孔：右心房到左心房；動脈導管：肺動脈到主動脈。",
        "reasons": {
            "A": "主動脈與肺動脈之間的胎兒分流是動脈導管，不是卵圓孔。",
            "B": "右心房與右心室本來由三尖瓣相通，卵圓孔不在此處。",
            "C": "卵圓孔連通右心房與左心房，是胎兒循環重要分流。",
            "D": "右心室與左心室由室間隔分隔；胎兒正常分流不是靠兩心室相通。",
        },
    },
    21: {
        "stem": "縱隔胸膜與橫膈中央部壁層胸膜由膈神經感覺支配，疼痛可轉移到 C3-C5 皮節的肩頸區。答案是 C。",
        "core": "膈神經 C3-C5 支配橫膈中央與縱隔胸膜感覺；肋間神經支配胸壁與橫膈周邊胸膜。",
        "reasons": {
            "A": "肋間神經支配肋胸膜與橫膈周邊胸膜，轉移痛較在胸腹壁，不是頸部痛主因。",
            "B": "迷走神經不是壁層胸膜疼痛的主要傳入神經。",
            "C": "膈神經支配縱隔胸膜與橫膈中央，刺激時可造成肩頸部轉移痛。",
            "D": "交感神經幹不是此處壁層胸膜痛覺的典型傳入路徑。",
        },
    },
    22: {
        "stem": "乳房血液供應主要來自內胸動脈穿支、外胸動脈及肋間動脈分支。肋下動脈位於第 12 肋下，通常不列為乳腺主要血供，答案是 D。",
        "core": "乳房血供：internal thoracic、lateral thoracic、intercostal arteries；subcostal artery 不是主要來源。",
        "reasons": {
            "A": "肋間動脈分支供應乳房，尤其外側與深部區域，屬正確血供來源。",
            "B": "內胸動脈穿支是乳房內側重要血液來源。",
            "C": "外胸動脈供應乳房外側，是常見且重要的血供。",
            "D": "肋下動脈走在第 12 肋下，位置太低，不是乳腺典型血液供應來源。",
        },
    },
    23: {
        "stem": "心包膜穿刺常由劍突下、左肋下緣附近進針，朝左肩方向，可降低進入肋膜腔與傷肺的機會。答案是 C。",
        "core": "劍突下心包穿刺可避開肋膜反折與肺緣，是考題最常見安全進針點。",
        "reasons": {
            "A": "胸骨右側第六肋間較可能接近右胸膜反折與肺緣，不是標準安全點。",
            "B": "胸骨左側第三肋間位置偏高，較容易遇到肋膜與內胸血管風險。",
            "C": "劍突與左肋下緣交點是經劍突下心包穿刺的典型位置，能減少刺破肋膜腔。",
            "D": "胸骨右側第四肋間不如劍突下路徑安全，也不符合心包穿刺常用考點。",
        },
    },
    24: {
        "stem": "成人正常心尖搏動多位於左第五肋間、鎖骨中線附近且稍內側。答案是 D。",
        "core": "心尖體表定位：左第五肋間、鎖骨中線內側約 1 公分。",
        "reasons": {
            "A": "第四肋間偏高，且鎖骨中線外側不是正常心尖最典型位置。",
            "B": "左乳頭位置會因個體而異，且不是解剖定位的精確描述。",
            "C": "第六肋間前腋線外側太低且太外側，較像心臟擴大時才可能偏移。",
            "D": "第五肋間鎖骨中線內側最符合正常年輕男性直立時心尖投影。",
        },
    },
    27: {
        "stem": "子宮體兩側可連接卵巢韌帶、子宮圓韌帶與闊韌帶。主韌帶主要連接子宮頸與陰道上部到骨盆側壁，不是子宮體兩側，答案是 D。",
        "core": "子宮體兩側常接卵巢韌帶、子宮圓韌帶與闊韌帶；主韌帶支撐子宮頸。",
        "reasons": {
            "A": "卵巢韌帶連接卵巢內側端與子宮角附近，屬子宮體側方相關結構。",
            "B": "子宮圓韌帶由子宮角向前外側走行，與子宮體側方相連。",
            "C": "闊韌帶是覆蓋子宮與附件的腹膜皺襞，連於子宮兩側。",
            "D": "主韌帶位於子宮頸旁，連到骨盆側壁；題幹問子宮體兩側，因此它最不符合。",
        },
    },
    29: {
        "stem": "內側與外側迴旋股動脈通常皆源自深股動脈，是股骨頭、頸與大腿近端的重要血供。答案是 B。",
        "core": "Medial and lateral circumflex femoral arteries are usually branches of profunda femoris artery。",
        "reasons": {
            "A": "股動脈可有變異分支，但典型解剖中這兩條迴旋股動脈主要來自深股動脈。",
            "B": "深股動脈是內側與外側迴旋股動脈的典型直接來源。",
            "C": "把內側迴旋股動脈列為股動脈直接分支不符合常規考點。",
            "D": "外側迴旋股動脈典型也來自深股動脈，不是股動脈直接分支。",
        },
    },
    30: {
        "stem": "肩胛上神經通過肩胛上切迹後支配棘上肌，再到棘下窩支配棘下肌。受傷時直接影響這兩塊肌肉，答案是 C。",
        "core": "肩胛上神經支配 supraspinatus 與 infraspinatus；腋神經支配 deltoid 與 teres minor。",
        "reasons": {
            "A": "棘下肌受肩胛上神經支配，但小圓肌由腋神經支配，所以不完整。",
            "B": "三角肌與小圓肌皆由腋神經支配，對應肱骨外科頸或四邊孔，不是肩胛上切迹。",
            "C": "棘上肌與棘下肌都由肩胛上神經支配，正好對應肩胛上切迹受傷的位置。",
            "D": "棘上肌正確，但肩胛下肌由上、下肩胛下神經支配，不由肩胛上神經支配。",
        },
    },
    31: {
        "stem": "脊髓前動脈通常是單一中線血管；大腦前交通動脈也通常是單一連接兩側前大腦動脈的血管。答案是 A。",
        "core": "單一血管：anterior spinal artery、anterior communicating artery；成對血管：posterior spinal arteries、posterior communicating arteries。",
        "reasons": {
            "A": "脊髓前動脈與前交通動脈都通常為單一未成對構造，符合題意。",
            "B": "脊髓後動脈與後交通動脈多為左右成對，不符合單一構造。",
            "C": "脊髓前動脈單一，但後交通動脈成對，因此整組不符合。",
            "D": "前交通動脈單一，但脊髓後動脈成對，因此整組不符合。",
        },
    },
    32: {
        "stem": "人類絨毛膜促性腺激素 hCG 由胎盤的融合滋養層分泌，用來維持早期妊娠黃體功能。答案是 B。",
        "core": "hCG is produced by syncytiotrophoblast and maintains corpus luteum in early pregnancy。",
        "reasons": {
            "A": "腦下腺前葉分泌 LH、FSH、TSH、ACTH、GH、prolactin，不製造 hCG。",
            "B": "融合滋養層是 hCG 的主要來源，這是妊娠測試與胚胎學常考點。",
            "C": "黃體受到 hCG 刺激而維持 progesterone 分泌，但黃體本身不是 hCG 來源。",
            "D": "蛻膜是妊娠子宮內膜變化，並非 hCG 的主要製造細胞。",
        },
    },
    33: {
        "stem": "橫中隔早期位於頸部體節高度，之後隨胚胎摺疊與快速成長下降，並參與形成橫膈中央腱。答案是 B。",
        "core": "septum transversum begins near cervical somites and contributes to central tendon of diaphragm。",
        "reasons": {
            "A": "枕節與舌下肌群等發育較相關，不是橫中隔第四週的典型高度。",
            "B": "橫中隔在第四週約位於頸節高度，之後下降到胸腹交界，符合答案。",
            "C": "胸節高度是後來相對位置改變後的概念，不是第四週橫中隔起始高度。",
            "D": "腰節位置過低，與橫中隔早期位於頸部的胚胎學考點不符。",
        },
    },
    35: {
        "stem": "動脈韌帶是胎兒動脈導管閉鎖後的殘跡，連接主動脈弓與肺動脈幹/左肺動脈附近。答案是 A。",
        "core": "ligamentum arteriosum = ductus arteriosus remnant, between aortic arch and pulmonary trunk/left pulmonary artery。",
        "reasons": {
            "A": "動脈韌帶位在主動脈弓與肺動脈幹附近，正是動脈導管閉鎖後的位置。",
            "B": "臍動脈閉鎖形成內側臍韌帶，不會形成動脈韌帶。",
            "C": "胚胎時期動脈導管主要將肺動脈血分流至主動脈，血氧狀態不能簡化為只攜帶缺氧血。",
            "D": "動脈韌帶不連接肺動脈與肺靜脈，肺靜脈屬回流到左心房的血管。",
        },
    },
    36: {
        "stem": "脊索在椎間盤中殘留為髓核；椎體與椎弓多由硬節衍生，纖維環來自周圍間質。答案是 B。",
        "core": "notochord remnant becomes nucleus pulposus。",
        "reasons": {
            "A": "椎體主要由體節硬節細胞形成，不是脊索直接殘留。",
            "B": "髓核是脊索的胚胎殘跡，為本題答案。",
            "C": "纖維環是椎間盤外層纖維軟骨，來源不同於脊索殘跡。",
            "D": "椎弓同樣源自硬節形成的椎骨結構，不是脊索衍生物。",
        },
    },
    37: {
        "stem": "肌纖維膜 sarcolemma 就是骨骼肌纖維的細胞膜。其他選項是包覆肌肉不同層級的結締組織。答案是 A。",
        "core": "sarcolemma = skeletal muscle cell plasma membrane；epi-, peri-, endomysium are connective tissue sheaths。",
        "reasons": {
            "A": "肌纖維膜是肌細胞的 plasma membrane，正是題目要問的構造。",
            "B": "肌外膜包覆整條肌肉，是結締組織，不是細胞膜。",
            "C": "肌內膜包覆單條肌纖維外側，屬細緻結締組織層，不等於 plasma membrane。",
            "D": "肌束膜包覆肌束，是結締組織，不是肌細胞膜。",
        },
    },
    38: {
        "stem": "核仁是細胞核內 rRNA 轉錄與核糖體次單元組裝區，沒有由膜包圍。其他胞器都有膜性結構。答案是 A。",
        "core": "nucleolus is non-membrane-bound; endosome, peroxisome, and ER are membrane-bound organelles。",
        "reasons": {
            "A": "核仁沒有獨立膜包覆，是本題問的非膜性構造。",
            "B": "胞內體是膜性囊泡，參與內吞路徑分選。",
            "C": "過氧化質體是單層膜胞器，含氧化酶與 catalase 等。",
            "D": "內質網是典型膜性胞器，包括粗面與滑面內質網。",
        },
    },
    39: {
        "stem": "棕色脂肪富含粒線體與多小脂滴，在新生兒含量較多，用於非顫抖產熱，隨年齡增加而減少。答案是 D。",
        "core": "white adipose stores energy with one large lipid droplet; brown adipose generates heat, has many droplets and many mitochondria。",
        "reasons": {
            "A": "白色脂肪主要儲能，棕色脂肪主要產熱；選項把功能顛倒。",
            "B": "脂肪小滴不是由典型 plasma membrane 包裹，而是由磷脂單層與相關蛋白包覆。",
            "C": "白色脂肪細胞通常是一大脂滴，棕色脂肪細胞是多小脂滴；選項顛倒。",
            "D": "棕色脂肪在新生兒較多且分布較廣，成人逐漸減少，敘述正確。",
        },
    },
    41: {
        "stem": "胸腺是 T 細胞成熟器官，有皮質、髓質與 Hassall corpuscles，但正常胸腺不形成淋巴小結。答案是 A。",
        "core": "thymus lacks lymphatic nodules/follicles; spleen, intestine, and tonsil contain lymphoid follicles。",
        "reasons": {
            "A": "胸腺沒有淋巴小結，這是它與其他淋巴器官的常考差異。",
            "B": "脾臟白髓含淋巴小結與 periarteriolar lymphoid sheath，不符合題幹「不具有」。",
            "C": "小腸有 Peyer's patches 與孤立淋巴小結，屬黏膜相關淋巴組織。",
            "D": "扁桃體富含淋巴小結與生發中心，是典型淋巴組織。",
        },
    },
    42: {
        "stem": "肛門直腸交界上方仍可見直腸單層柱狀上皮與杯狀細胞；往下才逐漸轉為複層扁平上皮。答案是 A。",
        "core": "rectum has simple columnar epithelium with goblet cells; anal canal transitions to stratified squamous epithelium; internal sphincter is thickened circular muscle。",
        "reasons": {
            "A": "直腸上皮為含杯狀細胞的單層柱狀上皮，符合肛門直腸交界附近可觀察到的構造。",
            "B": "複層扁平上皮主要在肛管遠端，不是直腸本身的上皮。",
            "C": "Peyer's patch 是迴腸特徵，不屬肛門構造。",
            "D": "內括約肌來自內環肌加厚，不是外縱走肌加厚；選項機轉錯。",
        },
    },
    43: {
        "stem": "胃腺 proper gastric gland 主要有壁細胞、主細胞、黏液頸細胞與內分泌細胞等。壁細胞分泌鹽酸與 intrinsic factor，答案是 A。",
        "core": "gastric gland proper contains parietal cells and chief cells; M cells, Paneth cells, and goblet cells are intestinal-associated。",
        "reasons": {
            "A": "壁細胞是胃腺的典型細胞，分泌 HCl 與 intrinsic factor。",
            "B": "M cells 主要位於腸道 Peyer's patches 相關上皮，不是胃腺 proper 的細胞。",
            "C": "Paneth cells 位於小腸腺底部，分泌抗菌物質，不屬胃腺 proper。",
            "D": "杯狀細胞是腸道上皮常見細胞，正常胃腺 proper 不以杯狀細胞為代表。",
        },
    },
    45: {
        "stem": "透明帶在初級濾泡階段開始出現，之後次級與成熟濾泡皆有。原始濾泡尚未形成透明帶，答案是 D。",
        "core": "zona pellucida appears from primary follicle stage, not primordial follicle。",
        "reasons": {
            "A": "成熟濾泡中的卵母細胞已有明顯透明帶。",
            "B": "次級濾泡已形成透明帶，也有顆粒細胞與卵泡膜發展。",
            "C": "初級濾泡開始出現透明帶，因此不是答案。",
            "D": "原始濾泡只有初級卵母細胞與扁平濾泡細胞，尚無透明帶。",
        },
    },
    46: {
        "stem": "精液由精子與附屬腺體分泌物組成，包括精囊、前列腺與尿道球腺。陰莖海綿體是勃起組織，不是分泌腺。答案是 B。",
        "core": "semen contains secretions from seminal vesicles, prostate, and bulbourethral glands; corpus cavernosum is erectile tissue。",
        "reasons": {
            "A": "前列腺分泌液是精液的重要成分，含 PSA、酵素與檸檬酸等。",
            "B": "陰莖海綿體是血管性勃起組織，不分泌精液成分。",
            "C": "尿道球腺分泌黏液樣液體，參與潤滑與中和尿道酸性。",
            "D": "精囊分泌富含 fructose 的液體，是精液主要體積來源之一。",
        },
    },
    47: {
        "stem": "題目問由高濃度到低濃度的運輸。小腸鈉離子進入細胞與鉀離子經 leak channel 流出細胞，都是順電化學梯度；鈣幫浦與腎小管氫離子分泌較偏主動或次級主動運輸。答案是 C（2、4）。",
        "core": "順梯度運輸不耗直接能量；pump 與 exchanger/cotransporter 常利用 ATP 或離子梯度完成主動或次級主動運輸。",
        "reasons": {
            "A": "1 的 Ca2+ ATPase 將鈣回收到肌漿網，是 ATP 驅動的主動運輸，不是單純高到低。",
            "B": "2 正確，但 3 的 Na-H countertransport 是次級主動運輸概念，不能列為單純高到低。",
            "C": "2 中鈉進入小腸上皮細胞順鈉梯度，4 中鉀經 leak channel 外流也順梯度，因此正確。",
            "D": "1 不是順梯度運輸，所以含 1 的組合不對。",
        },
    },
    48: {
        "stem": "氣味受器位於嗅覺上皮的嗅覺感覺神經元纖毛上，接受 odorant 後訊號傳到嗅球。答案是 D。",
        "core": "odorant receptors are on olfactory sensory neurons in olfactory epithelium, not on mitral/tufted cells。",
        "reasons": {
            "A": "嗅球毛叢狀細胞接收嗅覺神經元輸入，但不是氣味受器所在處。",
            "B": "僧帽細胞是嗅球輸出神經元，不直接表現主要 odorant receptors。",
            "C": "嗅覺皮質處理氣味訊息，但氣味受器位在周邊嗅覺上皮。",
            "D": "嗅覺上皮內的嗅覺感覺神經元纖毛上有氣味受器，最符合題意。",
        },
    },
    51: {
        "stem": "平滑肌橫橋循環慢，myosin ATPase 活性低，能以較低耗能維持張力。與骨骼肌快縮纖維相比，ATPase 活性最低的是平滑肌，答案是 B。",
        "core": "smooth muscle has slow cross-bridge cycling and low myosin ATPase activity。",
        "reasons": {
            "A": "slow oxidative 骨骼肌纖維 ATPase 較慢，但仍屬骨骼肌收縮系統，不低於平滑肌。",
            "B": "平滑肌 myosin ATPase 活性最低，能長時間維持張力且耗能較少。",
            "C": "fast oxidative glycolytic fibers 屬快速纖維，ATPase 活性高於慢纖維與平滑肌。",
            "D": "fast glycolytic fibers 收縮速度最快、ATPase 活性高，不可能是最低。",
        },
    },
    52: {
        "stem": "骨骼肌中 Ca2+ 結合 troponin C 後，tropomyosin 移開 actin 上的 myosin-binding sites，允許橫橋形成與收縮。答案是 B。",
        "core": "Ca2+ binds troponin C -> tropomyosin moves -> myosin-binding sites on actin exposed。",
        "reasons": {
            "A": "Ca2+ 是結合 troponin 後啟動收縮，不是離開 troponin 後啟動。",
            "B": "tropomyosin 位移會暴露 actin 上 myosin 結合位點，這是骨骼肌收縮開始的關鍵。",
            "C": "ATP 水解提供橫橋循環能量，但題幹問 tropomyosin 結構變化的直接結果。",
            "D": "tropomyosin 不與 myosin 接合來啟動收縮；它的角色是遮蔽或移開 actin 結合位。",
        },
    },
    53: {
        "stem": "若只考慮 ABO 紅血球輸血，AB 型受血者血漿沒有抗 A、抗 B 抗體，可接受 A、B、O 型紅血球。三人皆可捐給 AB 型患者，答案是 C。",
        "core": "AB recipient is universal recipient for ABO red blood cells; O donor red cells can be given to any ABO type。",
        "reasons": {
            "A": "A 型與 B 型可以捐給 AB 型，但 O 型也可以，因此「只有小李及小吳」不完整。",
            "B": "O 型紅血球可捐給 AB 型，但 AB 型也可接受 A、B 型，不是只有 O 型。",
            "C": "AB 型受血者可接受 A、B、O 型紅血球，三人均可捐血符合題意。",
            "D": "三人均不可捐血與 ABO 相容性相反，明顯錯誤。",
        },
    },
    54: {
        "stem": "Protein C 是肝臟合成的維生素 K 依賴性抗凝蛋白。vWF 多由內皮細胞與巨核細胞製造；G-CSF 與 interferon gamma 主要由免疫相關細胞分泌。答案是 A。",
        "core": "liver synthesizes many coagulation and anticoagulation proteins, including protein C and protein S。",
        "reasons": {
            "A": "protein C 主要由肝臟合成，且為維生素 K 依賴性抗凝因子。",
            "B": "vWF 主要由內皮細胞與巨核細胞生成，不是肝臟主要血漿蛋白產物。",
            "C": "G-CSF 可由巨噬細胞、內皮細胞、纖維母細胞等分泌，主要功能是刺激嗜中性球生成。",
            "D": "interferon gamma 主要由活化 T 細胞與 NK 細胞分泌，不是肝臟製造的血漿蛋白。",
        },
    },
    55: {
        "stem": "舒張期雜音典型來自房室瓣狹窄（血液舒張期通過狹窄 AV valve）或半月瓣閉鎖不全（舒張期逆流）。答案是 C。",
        "core": "diastolic murmurs: AV valve stenosis and aortic/pulmonic regurgitation; systolic murmurs: AV regurgitation and semilunar stenosis。",
        "reasons": {
            "A": "房室瓣狹窄是舒張期，但主動脈瓣狹窄是收縮期射出性雜音，所以組合不對。",
            "B": "房室瓣閉鎖不全是收縮期逆流，只有主動脈瓣閉鎖不全屬舒張期。",
            "C": "房室瓣狹窄與主動脈瓣閉鎖不全都會造成舒張期雜音，最符合題意。",
            "D": "房室瓣閉鎖不全與主動脈瓣狹窄皆偏收縮期雜音，不符合舒張期。",
        },
    },
    56: {
        "stem": "抑制心肌 Na-K ATPase 會增加細胞內 Na+，降低 Na-Ca exchanger 排鈣效率，使細胞內 Ca2+ 增加並提升收縮力，類似 digoxin 作用。答案是 C。",
        "core": "Na-K ATPase inhibition -> intracellular Na rises -> NCX activity falls -> intracellular Ca rises -> positive inotropy。",
        "reasons": {
            "A": "促進 SR Ca2+ ATPase 會加速鈣回收，較偏促進舒張，不是最直接增加收縮力的選項。",
            "B": "抑制 ryanodine receptor 會減少 SR 釋放 Ca2+，反而降低收縮力。",
            "C": "抑制 Na-K ATPase 會間接增加心肌細胞內 Ca2+，因此增加 contractility。",
            "D": "增加 Na-Ca exchanger 活性會把 Ca2+ 排出細胞，通常降低可用於收縮的 Ca2+。",
        },
    },
    57: {
        "stem": "心房顫動的 ECG 特徵是沒有規則 P 波，QRS 多數正常狹窄，但 R-R 間隔 irregularly irregular。答案是 B。",
        "core": "atrial fibrillation: absent organized P waves, irregularly irregular R-R intervals, usually normal QRS if conduction system intact。",
        "reasons": {
            "A": "AF 沒有明顯正常 P 波，而是 fibrillatory waves 或基線不規則。",
            "B": "心室傳導若未合併束支阻滯，QRS 可正常；AV node 不規則傳導造成 R-R 間隔不規則。",
            "C": "心房收縮對 ventricular filling 的貢獻通常約 10-20%，靜息時不一定下降 30-40% 或更多。",
            "D": "AF 常使心室速率不規則且可偏快，不是因 AV node 延遲而明顯下降。",
        },
    },
    60: {
        "stem": "本題資料庫標示全給分。若依生理學，高海拔低氧最主要刺激周邊化學受器，使通氣量增加；A、B、C 的生理方向較不典型，應以官方全給分狀態理解。",
        "core": "高海拔低氧會刺激頸動脈體/主動脈體，增加通氣並造成呼吸性鹼血症；此題為全給分題，需保留官方狀態。",
        "reasons": {
            "A": "高海拔低氧通常造成過度換氣與呼吸性鹼血症，不是呼吸性酸血症；但資料庫此題標示全給分。",
            "B": "慢性高海拔適應通常增加 2,3-BPG，降低 Hb 對氧親和力以利釋氧；選項方向不典型。",
            "C": "低氧會刺激而非抑制主動脈體與頸動脈體傳入訊號；選項方向不典型。",
            "D": "低氧刺激周邊化學受器後增加每分鐘通氣量，這是生理上最直接的反應。",
        },
    },
    61: {
        "stem": "呼出氣體是肺泡氣與解剖死腔氣的混合。死腔氣接近吸入空氣，氧分壓較高，因此混合後的呼出氣氧分壓可高於肺泡氣與動脈血。答案是 D。",
        "core": "expired air contains dead-space air, so its PO2 is higher than alveolar gas PO2。",
        "reasons": {
            "A": "肺泡氧分壓約 100 mmHg，低於含死腔氣混合後的呼出氣氧分壓。",
            "B": "肺泡微血管內血液氧分壓逐漸接近肺泡氣，但不會高於呼出混合氣。",
            "C": "體動脈血氧分壓約 95 mmHg，低於含吸入空氣成分的呼出氣。",
            "D": "呼出氣含有未參與氣體交換的死腔氣，因此平均氧分壓最高。",
        },
    },
    62: {
        "stem": "胃泌素除了刺激胃酸分泌，也有促進胃黏膜生長的 trophic effect。答案是 B。",
        "core": "gastrin stimulates acid secretion and growth of gastric mucosa。",
        "reasons": {
            "A": "膽囊收縮素主要刺激膽囊收縮與胰酵素分泌，不是胃黏膜增生主因。",
            "B": "胃泌素對胃黏膜有 trophic effect，最能刺激胃黏膜增生。",
            "C": "運動素主要調控消化道移行性運動複合波，和胃黏膜增生關聯較小。",
            "D": "胰泌素主要刺激胰臟與膽道分泌重碳酸鹽，並抑制胃酸，不是胃黏膜生長主因。",
        },
    },
    63: {
        "stem": "食道遲緩不能症來自食道肌間神經叢抑制性神經元退化，造成下食道括約肌放鬆不良與蠕動異常。答案是 B。",
        "core": "achalasia is due to loss/defect of myenteric plexus inhibitory neurons, especially NO/VIP signaling。",
        "reasons": {
            "A": "NO 與 VIP 是促進 LES 放鬆的抑制性神經傳遞物；分泌過多不會造成典型 achalasia。",
            "B": "肌間神經叢缺損使 LES 無法正常放鬆，是 achalasia 的核心病理。",
            "C": "會厭功能缺陷會造成吞嚥保護與誤吸問題，不是下食道括約肌放鬆不良。",
            "D": "幽門狹窄影響胃排空，位置在胃出口，不會造成食道遲緩不能症。",
        },
    },
    64: {
        "stem": "唾液澱粉酶與舌脂肪酶缺少時，胰臟與小腸酵素仍可消化醣類、脂肪與蛋白質。答案是 D。",
        "core": "沒有唾液仍可靠胰澱粉酶、胰脂肪酶與蛋白酶完成三大營養素消化。",
        "reasons": {
            "A": "醣類與脂肪仍可被消化，但蛋白質也能由胃蛋白酶與胰蛋白酶系統消化，所以不只 1、2。",
            "B": "脂肪與蛋白質可消化，但醣類也可由胰澱粉酶與小腸刷狀緣酵素消化。",
            "C": "醣類與蛋白質可消化，脂肪也可靠胰脂肪酶與膽鹽乳化後消化。",
            "D": "即使沒有唾液，醣類、脂肪、蛋白質都仍有其他消化酵素與機制可處理。",
        },
    },
    65: {
        "stem": "Aquaporin 2 位於集尿管 principal cells，受 vasopressin/ADH 調控轉位到頂膜，增加水再吸收。答案是 A。",
        "core": "ADH causes AQP2 insertion into collecting duct apical membrane; water movement is passive along osmotic gradient。",
        "reasons": {
            "A": "vasopressin 經 V2 receptor 促使 AQP2 轉位至頂膜，是本題正確重點。",
            "B": "亨利氏環下降枝水通透性高，但主要不是由受 ADH 調控的 AQP2 表現來描述。",
            "C": "水分移動方向是由低張向高張環境，選項把滲透方向說反。",
            "D": "水通道只提供被動擴散通路，不做 ATP 驅動的主動運輸。",
        },
    },
    66: {
        "stem": "腎小管腔內氫離子常由 HCO3-、HPO4 2- 與 NH3/NH4+ 系統緩衝。丁酸根 C3H7COO- 不是常見尿液酸鹼緩衝物，答案是 D。",
        "core": "urinary buffers include bicarbonate, phosphate, and ammonia; organic anions such as butyrate are not standard major buffers。",
        "reasons": {
            "A": "HCO3- 可在近端腎小管參與氫離子處理與重吸收，不是最不常見者。",
            "B": "磷酸鹽 HPO4 2- 是尿液 titratable acid 的重要緩衝系統。",
            "C": "NH3 可結合 H+ 形成 NH4+，是排酸的重要機制。",
            "D": "C3H7COO- 不是腎小管常用的主要酸鹼緩衝物質，最符合題意。",
        },
    },
    67: {
        "stem": "腎小管葡萄糖主要在近端小管再吸收；早段近端小管頂膜以 SGLT2 為主，基底外側再經 GLUT2 離開細胞。答案是 C。",
        "core": "proximal tubule apical SGLT2 reabsorbs most filtered glucose; basolateral GLUT2 returns glucose to blood。",
        "reasons": {
            "A": "GLUT1 不是遠端腎小管頂膜再吸收葡萄糖的主要運輸蛋白；位置與蛋白都不對。",
            "B": "SGLT1 是頂膜鈉依賴共同運輸蛋白，不在基底外側膜負責再吸收。",
            "C": "近端腎小管頂膜主要使用 SGLT2 再吸收大部分葡萄糖，敘述正確。",
            "D": "近端小管基底外側以 GLUT2 較典型，不是主要 GLUT1。",
        },
    },
    68: {
        "stem": "體溫、cortisol 與 melatonin 都有明顯晝夜節律；胰島素分泌受進食與血糖影響最大，晝夜生物時鐘不是最主要決定因素。答案是 D。",
        "core": "circadian rhythm strongly affects body temperature, cortisol, and melatonin; insulin is primarily meal/glucose-driven。",
        "reasons": {
            "A": "體溫有晝夜變化，通常清晨較低、傍晚較高。",
            "B": "cortisol 有明顯日夜節律，清晨較高。",
            "C": "melatonin 與光暗週期密切相關，夜間分泌上升。",
            "D": "胰島素主要隨進食與血糖變動，雖可受節律調節，但最不屬典型晝夜指標。",
        },
    },
    69: {
        "stem": "StAR protein 的主要功能是把膽固醇從粒線體外膜運送到內膜，讓 CYP11A1 將膽固醇轉成 pregnenolone。答案是 C。",
        "core": "StAR mediates cholesterol transport into mitochondria, the rate-limiting step of steroidogenesis。",
        "reasons": {
            "A": "膽固醇轉成 pregnenolone 是 CYP11A1/desmolase 的酵素反應，不是 StAR 直接催化。",
            "B": "StAR 不負責膽固醇進入細胞內；它重點在粒線體內外膜間運送。",
            "C": "StAR 將膽固醇送入粒線體內膜側，是類固醇生成的限速步驟。",
            "D": "LDL 是運送膽固醇的脂蛋白，StAR 不會把膽固醇轉成 LDL。",
        },
    },
    70: {
        "stem": "甲狀腺素是脂溶性激素，進入細胞後與核內受器結合，調控基因轉錄。答案是 A。",
        "core": "thyroid hormone and steroid hormones act mainly through intracellular/nuclear receptors。",
        "reasons": {
            "A": "thyroid hormone 可進入細胞並與核內受器結合，改變基因表現。",
            "B": "insulin 是胜肽激素，作用於細胞膜 receptor tyrosine kinase。",
            "C": "growth hormone 作用於細胞膜 JAK-STAT 相關受器，不是細胞內受器。",
            "D": "ANP 作用於膜上 guanylyl cyclase receptor，增加 cGMP，不是進入細胞核受器。",
        },
    },
    71: {
        "stem": "腦下垂體前葉功能全面降低時，ACTH 缺乏造成次發性腎上腺皮質功能不足；壓力狀態需額外補充 cortisol。答案是 D。",
        "core": "panhypopituitarism needs physiologic hormone replacement, and stress-dose glucocorticoid is required during illness or surgery。",
        "reasons": {
            "A": "只補充 androgen 不能恢復完整精子製造，還需要 FSH/LH 軸功能或相應治療。",
            "B": "TSH 缺乏會造成中樞性甲狀腺低下，通常需要補充甲狀腺素。",
            "C": "前葉功能降低不等於後葉 ADH 缺乏；是否補 ADH 取決於有無尿崩症。",
            "D": "壓力狀態下 cortisol 需求增加，ACTH 軸不足者需額外 glucocorticoid。",
        },
    },
    72: {
        "stem": "血睪屏障由 Sertoli cells 間 tight junction 形成，隔離免疫系統以保護減數分裂後較晚出現抗原的生殖細胞，尤其 primary spermatocytes 之後的細胞。答案是 D。",
        "core": "blood-testis barrier protects developing germ cells such as primary spermatocytes and later stages。",
        "reasons": {
            "A": "Leydig cells 位於間質，負責 testosterone 生成，不在血睪屏障後方保護區內。",
            "B": "myoid cells 位於生精小管周圍，協助收縮與支撐，不是屏障主要保護目標。",
            "C": "fibroblasts 屬間質細胞，不是血睪屏障保護的生殖細胞。",
            "D": "primary spermatocytes 位於屏障腔側，需免於免疫辨識，是血睪屏障保護重點。",
        },
    },
    73: {
        "stem": "乳汁合成主要由 prolactin 促進；oxytocin 主要促進乳汁排出。答案是 B。",
        "core": "prolactin makes milk; oxytocin ejects milk。",
        "reasons": {
            "A": "oxytocin 讓肌上皮細胞收縮，負責 let-down reflex，不是乳汁合成主因。",
            "B": "prolactin 作用於乳腺上皮細胞，促進乳汁生成，是本題答案。",
            "C": "progesterone 在妊娠中促進乳腺發育，但高濃度會抑制產後乳汁大量分泌。",
            "D": "prostaglandins 不是乳汁生成的主要內分泌調控激素。",
        },
    },
    74: {
        "stem": "等電點是分子淨電荷為零的 pH；多胜肽仍可能同時帶有正、負局部電荷，但總和為零。答案是 C。",
        "core": "at isoelectric pH, net charge equals zero, not necessarily no charged groups。",
        "reasons": {
            "A": "胺基端與羧基端不會在等電點皆帶正電，羧基端常為負電或依環境解離。",
            "B": "等電點不是所有可解離基團都不帶電，而是正負電總和抵消。",
            "C": "淨電荷為零正是等電點的定義。",
            "D": "帶有四個淨電荷與等電點定義相反。",
        },
    },
    75: {
        "stem": "蛋白質身分鑑定需要特異抗體、質量資訊或序列資訊。分子篩層析主要依分子大小分離，不能直接確認蛋白質身分。答案是 C。",
        "core": "Western blot, mass spectrometry, and N-terminal sequencing can identify proteins; size-exclusion chromatography mainly separates by size。",
        "reasons": {
            "A": "Western blot 利用特異抗體辨識蛋白，可用於身分鑑定。",
            "B": "質譜可提供蛋白質或胜肽質量與序列片段資訊，常用於蛋白鑑定。",
            "C": "分子篩層析只能依大小分離或估計分子量，不能直接證明蛋白身分。",
            "D": "胺基端序列分析提供序列資訊，可直接協助辨認蛋白質。",
        },
    },
    76: {
        "stem": "凝膠過濾色層分析法中，大分子先被沖提出來，小分子較晚。四者分子量由大到小為 RNA polymerase、IgG、RNase A、cytochrome c，因此第二順位是 IgG，答案是 B。",
        "core": "gel filtration separates by size: largest elutes first。",
        "reasons": {
            "A": "cytochrome c 約 13 kDa，接近最小，會較晚沖出，不是第二順位。",
            "B": "IgG 約 145 kDa，小於 RNA polymerase 但大於 RNase A 與 cytochrome c，因此第二個沖出。",
            "C": "RNase A 約 13.7 kDa，只比 cytochrome c 稍大，仍屬後段沖出。",
            "D": "RNA polymerase 約 450 kDa 最大，會第一個沖出，不是第二順位。",
        },
    },
    77: {
        "stem": "維生素 B12 又稱 cobalamin，結構中含鈷離子。答案是 D。",
        "core": "vitamin B12 = cobalamin, contains cobalt。",
        "reasons": {
            "A": "vitamin K 與凝血因子 gamma-carboxylation 相關，不含鈷為結構特徵。",
            "B": "vitamin E 是脂溶性抗氧化維生素，不含鈷離子。",
            "C": "vitamin B6 是 pyridoxine/pyridoxal phosphate 系列，不以鈷為結構核心。",
            "D": "vitamin B12 的 cobalamin 名稱即反映其含 cobalt，為本題答案。",
        },
    },
    78: {
        "stem": "維生素 A 的活性型 retinoic acid 會與核內 retinoid receptors（RAR/RXR）結合，調控基因表達。答案是 C。",
        "core": "vitamin A regulates transcription through nuclear retinoid receptors。",
        "reasons": {
            "A": "calcitriol receptor 是維生素 D 受器，不是維生素 A 直接結合的主要受器。",
            "B": "receptor tyrosine kinases 是 insulin、growth factor 等膜受器路徑，不是維生素 A 的核內作用方式。",
            "C": "nuclear retinoid receptors 是維生素 A/retinoic acid 調控轉錄的直接受器。",
            "D": "GPCR 是許多胜肽或小分子訊號路徑，不是維生素 A 調控基因表達的主要受器。",
        },
    },
    79: {
        "stem": "霍亂毒素 ADP-ribosylates Gs alpha，抑制其 GTPase，使 Gs 持續活化 adenylyl cyclase，cAMP 上升並造成分泌性腹瀉。題目問錯誤敘述，答案是 A。",
        "core": "cholera toxin locks Gs alpha in active GTP-bound state -> adenylyl cyclase stays active -> cAMP increases。",
        "reasons": {
            "A": "Gs alpha 不是無法活化下游效應物，而是持續活化 adenylyl cyclase；這句錯誤，故為答案。",
            "B": "Gs alpha 維持 GTP-bound 活化態時較不易重新與 beta-gamma 次單元結合，敘述可成立。",
            "C": "adenylyl cyclase 持續活化是霍亂毒素造成高 cAMP 的核心機轉。",
            "D": "cAMP 增加會促進腸上皮氯離子與水分分泌，造成大量水瀉。",
        },
    },
    80: {
        "stem": "HGPRT 活性降低會減少 purine salvage，使 PRPP 與 de novo purine synthesis 增加，尿酸生成上升，可導致痛風。答案是 C。",
        "core": "HGPRT deficiency impairs purine salvage and increases uric acid; severe form is Lesch-Nyhan syndrome。",
        "reasons": {
            "A": "citrate synthase 是 TCA cycle 酵素，缺乏不會典型造成尿酸過多。",
            "B": "PRPP synthetase 活性降低會減少 purine 合成基質，方向不符合痛風；活性過高才可能增加尿酸。",
            "C": "HGPRT 活性降低使 hypoxanthine/guanine salvage 下降，purine 分解成尿酸增加。",
            "D": "glucose 6-phosphatase 表現上升不是痛風的典型酵素異常機轉。",
        },
    },
    81: {
        "stem": "大腸桿菌 Dam methylase 會甲基化親代 DNA 的 GATC 序列，讓錯配修復系統辨認舊模板股與新合成未甲基化股。答案是 B。",
        "core": "Dam methylation marks the parental/template strand for bacterial mismatch repair。",
        "reasons": {
            "A": "Dam methylase 不是把 uracil 甲基化成 thymine；那不是錯配修復的辨識機制。",
            "B": "模板股被 Dam methylation 標記後，修復系統可切除新股上的錯誤配對。",
            "C": "去除錯誤配對的是錯配修復蛋白群，不是 Dam methylase 本身直接執行。",
            "D": "修復目標通常是新合成未甲基化股，不是任意稱為 coding strand 的那一股。",
        },
    },
    82: {
        "stem": "E. coli DNA polymerase I 具有 5' to 3' polymerase、3' to 5' exonuclease proofreading、5' to 3' exonuclease 去除 primer 等活性，但沒有 DNA gyrase 活性。答案是 B。",
        "core": "DNA polymerase I has polymerase plus 3'->5' and 5'->3' exonuclease activities; DNA gyrase is a topoisomerase。",
        "reasons": {
            "A": "3' to 5' exonuclease 是 proofreading 活性，DNA polymerase I 具有此功能。",
            "B": "DNA gyrase 是拓樸異構酶，處理 DNA 超螺旋，不是 DNA polymerase I 活性。",
            "C": "5' to 3' DNA polymerase 活性是 DNA polymerase I 的基本合成功能。",
            "D": "5' to 3' exonuclease 可移除 RNA primer，是 DNA polymerase I 的特色之一。",
        },
    },
    83: {
        "stem": "Histone deacetylase 移除組蛋白乙醯基，使染色質較緊密，通常降低或調節轉錄活性。最主要功能是調節基因轉錄，答案是 A。",
        "core": "histone acetylation opens chromatin; deacetylation condenses chromatin and regulates transcription。",
        "reasons": {
            "A": "去乙醯化改變染色質開放程度，直接影響基因轉錄，是本題答案。",
            "B": "HDAC 不會增加組蛋白濃度，而是改變組蛋白修飾狀態。",
            "C": "它主要作用在染色質與轉錄層級，不是直接減少 mRNA translation。",
            "D": "eIF2 穩定性屬轉譯調控議題，與 HDAC 的主要功能不符。",
        },
    },
    85: {
        "stem": "Trp operon 弱化作用利用 leader peptide 上連續 Trp codons 感測色胺酸充足與否，藉由轉錄、轉譯偶聯改變 RNA hairpin 結構。答案是 C。",
        "core": "attenuation senses charged tRNA-Trp through ribosome stalling at Trp codons in the leader peptide。",
        "reasons": {
            "A": "Trp operon 還有 repressor/operator 調控，弱化作用不是唯一機制。",
            "B": "leader peptide 不是直接作用於 RNA polymerase，而是透過 ribosome 停滯改變 mRNA 二級結構。",
            "C": "leader peptide 上的 Trp codons 可反映細胞內 charged tRNA-Trp 供應，是弱化作用核心設計。",
            "D": "色胺酸低時 ribosome 停在 Trp codons，會形成 anti-terminator，使 operon 繼續表現，不是引發終止性的弱化。",
        },
    },
    86: {
        "stem": "細菌錯配修復利用 Dam methylation 標記舊股；新合成股暫時未甲基化，因此修復系統知道要切除新股錯誤。答案是 C。",
        "core": "bacterial mismatch repair distinguishes strands by methylation status。",
        "reasons": {
            "A": "乙醯化常見於蛋白質或組蛋白調控，不是細菌錯配修復辨識模板股的主要 DNA 標記。",
            "B": "磷酸化不是細菌 DNA mismatch repair 用來分辨新舊股的標誌。",
            "C": "Dam methylase 造成的甲基化可標記親代模板股，是本題關鍵。",
            "D": "醣化不是 DNA 錯配修復辨認模板股的標準機制。",
        },
    },
    87: {
        "stem": "肝醣合成酶將 UDP-glucose 提供的葡萄糖殘基接到肝醣非還原端，形成 alpha-1,4 鍵結；分支酶才形成 alpha-1,6。答案是 D。",
        "core": "glycogen synthase extends glycogen at nonreducing ends by alpha-1,4 linkages using UDP-glucose。",
        "reasons": {
            "A": "肝醣合成酶被去磷酸化時活化；磷酸化通常使其活性降低。",
            "B": "此酵素不只存在於肝臟，骨骼肌等組織也有肝醣合成。",
            "C": "葡萄糖單元供給者是 UDP-glucose，不是 glucose-6-phosphate。",
            "D": "將葡萄糖殘基接到非還原端並形成 alpha-1,4 鍵結，正是肝醣合成酶功能。",
        },
    },
    88: {
        "stem": "Thiamine pyrophosphate 是 pyruvate dehydrogenase complex 的輔因子。缺乏維生素 B1 時 pyruvate 不能順利轉成 acetyl-CoA，轉向 lactate，造成乳酸中毒。答案是 D。",
        "core": "thiamine deficiency impairs pyruvate dehydrogenase and alpha-ketoglutarate dehydrogenase, causing lactate accumulation。",
        "reasons": {
            "A": "異檸檬酸脫氫酶屬 TCA cycle，但不是 B1 缺乏造成乳酸中毒的典型關鍵。",
            "B": "乳酸脫氫酶會把 pyruvate 轉為 lactate，但 B1 缺乏的上游問題是 PDH 受損。",
            "C": "蘋果酸脫氫酶不是 thiamine 依賴酵素，和此題機轉不符。",
            "D": "PDH complex 需 thiamine 作輔因子，受損時 pyruvate 累積並轉成 lactate。",
        },
    },
    89: {
        "stem": "胰島素促進骨骼肌與脂肪等肝外組織 GLUT4 轉位到細胞膜，增加葡萄糖攝取；若注射後未進食，容易造成低血糖。答案是 B。",
        "core": "insulin lowers blood glucose mainly by increasing GLUT4-mediated uptake in muscle and adipose tissue and suppressing hepatic glucose output。",
        "reasons": {
            "A": "肝臟主要使用 GLUT2，GLUT1 不是胰島素降低血糖的主軸。",
            "B": "GLUT4 在肝外胰島素敏感組織增加葡萄糖攝取，是低血糖最主要因素。",
            "C": "肝臟以 glucokinase 為主，不是 hexokinase；且本題最直接是肝外 GLUT4 攝糖。",
            "D": "肝外 hexokinase 可磷酸化葡萄糖，但胰島素急性降低血糖的核心是 GLUT4 攝入增加。",
        },
    },
    90: {
        "stem": "Acetyl-CoA 主要來自脂肪酸 beta-oxidation、ketogenic amino acids 及 pyruvate oxidative decarboxylation。Pyrimidine 分解不屬主要來源，答案是 C。",
        "core": "major acetyl-CoA sources: pyruvate, fatty acids, ketogenic amino acids; pyrimidines are not a major source。",
        "reasons": {
            "A": "fatty acids 經 beta-oxidation 產生 acetyl-CoA，是主要來源之一。",
            "B": "ketogenic amino acids 分解可形成 acetyl-CoA 或 acetoacetate，屬主要來源。",
            "C": "pyrimidine 分解產物通常進入 beta-alanine、beta-aminoisobutyrate 等路徑，不是 acetyl-CoA 主要來源。",
            "D": "pyruvate 經 PDH complex 轉成 acetyl-CoA，是醣類代謝的重要來源。",
        },
    },
    91: {
        "stem": "GSH 被氧化成 GSSG 後，glutathione reductase 使用 NADPH 將 GSSG 還原回 2 個 GSH，不是使用 ATP。否定式答案是 D。",
        "core": "glutathione reductase uses NADPH, while GSH contains Glu-Cys-Gly and forms GSSG via disulfide bond。",
        "reasons": {
            "A": "GSH 是 glutamate、cysteine、glycine 三胜肽，敘述正確。",
            "B": "某些 leukotriene，如 LTC4，合成時會接上 glutathione，敘述正確。",
            "C": "兩個 GSH 氧化時以雙硫鍵形成 GSSG，敘述正確。",
            "D": "glutathione reductase 需要 NADPH 還原 GSSG，不是直接利用 ATP；此句錯誤。",
        },
    },
    92: {
        "stem": "Epinephrine 屬 catecholamine，生合成從 tyrosine 開始，經 DOPA、dopamine、norepinephrine 到 epinephrine。答案是 D。",
        "core": "catecholamines are synthesized from tyrosine。",
        "reasons": {
            "A": "glycine 是 heme、purine 等路徑常見前驅物，不是 catecholamine 主前驅物。",
            "B": "tryptophan 是 serotonin、melatonin 與 niacin 的前驅物，不是 epinephrine。",
            "C": "histidine 可形成 histamine，不是 epinephrine 的前驅物。",
            "D": "tyrosine 是 dopamine、norepinephrine、epinephrine 的共同起始胺基酸。",
        },
    },
    93: {
        "stem": "轉氨基作用可把胺基轉到 alpha-ketoglutarate 上，直接生成 glutamate。答案是 A。",
        "core": "alpha-ketoglutarate accepts an amino group in transamination to become glutamate。",
        "reasons": {
            "A": "alpha-ketoglutarate 接受胺基後即形成 glutamic acid，是本題答案。",
            "B": "pyruvate 接受胺基會形成 alanine，不是 glutamate。",
            "C": "acetoacetate 是 ketone body 相關分子，不是轉氨基直接形成 glutamate 的受體。",
            "D": "oxaloacetate 接受胺基會形成 aspartate，不是 glutamate。",
        },
    },
    94: {
        "stem": "Serotonin 由 tryptophan 經 hydroxylation 與 decarboxylation 形成；之後可再轉為 melatonin。答案是 C。",
        "core": "tryptophan is the precursor of serotonin and melatonin。",
        "reasons": {
            "A": "arginine 可生成 nitric oxide、urea cycle 相關產物，不是 serotonin 前驅物。",
            "B": "glutamic acid 可形成 GABA 或參與氮代謝，不是 serotonin 前驅物。",
            "C": "tryptophan 是 serotonin 生合成的直接前驅胺基酸。",
            "D": "tyrosine 是 catecholamine 與 thyroid hormone 前驅物，不是 serotonin。",
        },
    },
    95: {
        "stem": "ATP synthase 位於粒線體內膜，利用跨內膜質子梯度在基質側合成 ATP。ATP 不是在內膜與外膜間隙形成，所以否定式答案是 C。",
        "core": "ATP synthase makes ATP on the mitochondrial matrix side using the proton gradient across the inner membrane。",
        "reasons": {
            "A": "ATP synthase 嵌在粒線體內膜，敘述正確。",
            "B": "它利用內膜兩側的 H+ 電化學梯度驅動 ATP 合成，敘述正確。",
            "C": "ATP 合成的催化頭部朝向 matrix，ATP 在基質側生成，不是在膜間腔；此句錯誤。",
            "D": "旋轉催化與構型改變是 ATP synthase 產生 ATP 的重要機制，敘述正確。",
        },
    },
    97: {
        "stem": "G1 進入 S 期需要 E2F 釋放以啟動 DNA 合成相關基因。Cyclin E-CDK2 磷酸化 pRb 後，pRb 放開 E2F，細胞週期往 S 期推進。答案是 C。",
        "core": "CDK2 phosphorylation of pRb releases E2F and promotes G1/S transition。",
        "reasons": {
            "A": "p53 活化通常誘導 cell-cycle arrest 或 apoptosis，不會刺激進入 S 期。",
            "B": "p21 是 CDK inhibitor，會抑制 CDK 活性，使細胞週期停下。",
            "C": "CDK2 磷酸化 pRb 可解除 E2F 抑制，誘導 DNA synthesis enzymes 表現。",
            "D": "pRb-E2F 複合體會抑制 E2F 作用；形成此複合體不是進入 S 期訊號。",
        },
    },
    98: {
        "stem": "類固醇受體是細胞內/核內受器，與 G protein 訊息傳遞無關。Adenylyl cyclase、PLC 與 Ras 都可出現在膜受器下游訊號網絡，答案是 A。",
        "core": "steroid receptors are intracellular transcription factors, not GPCR pathway proteins。",
        "reasons": {
            "A": "類固醇受體直接結合脂溶性激素並調控轉錄，不屬 G protein 訊息傳遞路徑。",
            "B": "adenylyl cyclase 是 Gs/Gi 常見下游效應酶，與 G protein 路徑相關。",
            "C": "phospholipase C 可由 Gq 活化，產生 IP3 與 DAG，與 G protein 路徑相關。",
            "D": "Ras 是小 GTP-binding protein，常見於受器訊號傳遞網絡，與 GTPase 訊號概念相關。",
        },
    },
    99: {
        "stem": "Calmodulin 以 EF-hand 的 helix-loop-helix motif 結合 Ca2+，構型改變後調節多種標靶蛋白與激酶。它不是靠 amphipathic beta-sheet 結合標靶，所以否定式答案是 B。",
        "core": "calmodulin contains EF-hand helix-loop-helix Ca2+-binding motifs and regulates target enzymes after Ca2+ binding。",
        "reasons": {
            "A": "calmodulin 與 Ca2+ 結合後會構型改變，暴露標靶蛋白結合面，敘述正確。",
            "B": "calmodulin 的標靶結合不是靠一個 amphipathic beta-sheet；此結構描述錯誤。",
            "C": "Ca2+-calmodulin 可調節 CaM kinases、MLCK 等多種 protein kinases，敘述正確。",
            "D": "EF-hand 是 helix-loop-helix 型 Ca2+ 結合 motif，符合 calmodulin 特性。",
        },
    },
    100: {
        "stem": "實驗室讓質體直接進入細菌最常見方法是製備 competent cells，使用 CaCl2 處理後熱休克，使質體 DNA 進入細菌。答案是 D。",
        "core": "common bacterial plasmid transformation: CaCl2-treated competent cells plus heat shock; electroporation is another method but not low-voltage electrophoresis。",
        "reasons": {
            "A": "低電壓電泳不是常用轉形方法；電穿孔是高電場短脈衝，概念不同。",
            "B": "帶質體的噬菌體屬 transduction 或 phage-mediated delivery，不是質體直接轉形最常用方法。",
            "C": "微注射常用於較大型細胞或胚胎操作，不適合當作細菌質體轉形常規方法。",
            "D": "CaCl2 處理加熱休克是經典 bacterial transformation 方法，正是題目所問的常用方式。",
        },
    },
}


def make_explanation(entry):
    return (
        "【題幹解析】\n"
        + entry["stem"]
        + "\n\n【選項詳解】\n"
        + "\n".join(f"- {letter}. {entry['reasons'][letter]}" for letter in ("A", "B", "C", "D"))
        + "\n\n【核心考點】\n"
        + entry["core"]
    )


def make_update(question, entry):
    front = question.get("flashcard_front") or question["question_text"].strip()
    return {
        "question_id": question["id"],
        "question_number": question["question_number"],
        "explanation": make_explanation(entry),
        "key_point": entry["core"],
        "flashcard_front": front,
        "flashcard_back": entry["core"],
        "flashcard_summary": f"{front} -> {entry['core']}",
        "review_status": "ai_generated",
        "explanation_model": "codex-high-quality-rewrite",
        "explanation_generated_at": STAMP,
        "manual_review_notes": [],
    }


def main():
    data = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    by_number = {q["question_number"]: q for q in data["questions"]}
    targets = [number for batch in BATCHES for number in batch]
    if len(targets) != 85 or len(set(targets)) != 85:
        raise SystemExit("target question count must be exactly 85")
    if sorted(targets) != sorted(ENTRIES):
        missing = sorted(set(targets) - set(ENTRIES))
        extra = sorted(set(ENTRIES) - set(targets))
        raise SystemExit(f"entry mismatch missing={missing} extra={extra}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_file in OUT_DIR.glob("q*.json"):
        old_file.unlink()

    for index, numbers in enumerate(BATCHES, start=1):
        updates = [make_update(by_number[number], ENTRIES[number]) for number in numbers]
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": min(numbers), "end": max(numbers)},
            "updates": updates,
        }
        out_path = OUT_DIR / f"q{min(numbers):03d}-q{max(numbers):03d}_selected{index:02d}.json"
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {len(BATCHES)} update files for {len(targets)} selected questions")


if __name__ == "__main__":
    main()
