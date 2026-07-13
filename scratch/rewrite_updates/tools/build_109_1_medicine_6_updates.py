import json
from datetime import datetime, timezone, timedelta
from pathlib import Path


SOURCE_FILE = "public/data/exams/109-1/medicine-6.json"
DATASET_ID = "109-1_medicine-6"
OUT_DIR = Path("scratch/rewrite_updates/109-1_medicine-6")
MODEL = "codex-high-quality-rewrite"
TS = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")


def explanation(stem, options, core):
    return f"【題幹解析】\n{stem}\n\n【選項詳解】\n" + "\n".join(
        f"- {label}. {text}" for label, text in options
    ) + f"\n\n【核心考點】\n{core}"


def load_source():
    return json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8"))


def make_update(q, stem, options, core, key_point, front, back, summary, notes=None):
    return {
        "question_id": q["id"],
        "question_number": q["question_number"],
        "explanation": explanation(stem, options, core),
        "key_point": key_point,
        "flashcard_front": front,
        "flashcard_back": back,
        "flashcard_summary": summary,
        "review_status": "ai_generated",
        "explanation_model": MODEL,
        "explanation_generated_at": TS,
        "manual_review_notes": notes or [],
    }


DATA = {
    1: {
        "stem": "本題考的是全身麻醉誘導前對困難通氣或困難氣道的預測。題幹問「最不可能」，因此官方答案 A 是指風濕性心臟病本身不是典型困難通氣預測因子；其餘選項都可能因上呼吸道、頸椎或睡眠呼吸障礙增加通氣或插管難度。",
        "options": [
            ("A", "正確。風濕性心臟病主要影響心臟瓣膜、肺高壓或心衰竭風險，會影響麻醉風險評估，但不是典型的困難面罩通氣或困難插管解剖預測因子。"),
            ("B", "錯誤。唐氏症常有巨舌、上呼吸道狹窄、低張力與頸椎不穩定，麻醉前應預期可能通氣或插管較困難。"),
            ("C", "錯誤。類風濕性關節炎可能造成顳顎關節活動受限、環杓關節或頸椎受累，特別是寰樞椎不穩定，會增加氣道處置風險。"),
            ("D", "錯誤。阻塞性睡眠呼吸中止症常與肥胖、上呼吸道塌陷及困難面罩通氣相關，是麻醉氣道評估的重要警訊。"),
        ],
        "core": "困難氣道評估重點是口咽構造、頸椎活動度、睡眠呼吸障礙與顳顎關節等因素；單純風濕性心臟病不是典型困難通氣預測因子。",
        "key": "困難通氣常見風險包括 Down syndrome、類風濕頸椎或顳顎關節受限、OSA；風濕性心臟病本身不是典型氣道因子。",
        "front": "困難通氣預測因子：Down syndrome / RA / OSA / 風濕性心臟病",
        "back": "最不典型的是風濕性心臟病；它影響麻醉心血管風險，但不是主要困難氣道解剖因子。",
        "summary": "困難氣道評估 -> 看上呼吸道與頸椎等解剖風險；風濕性心臟病非典型氣道風險。",
    },
    2: {
        "stem": "Pulse oximetry 以紅光與紅外光吸收差異估算動脈血氧飽和度，最核心的物理基礎是 oxyhemoglobin 與 deoxyhemoglobin 在 660 nm 與 940 nm 的吸收不同。",
        "options": [
            ("A", "錯誤。SpO2 是連續、非侵入性監測，但指甲油、低灌流、動作、環境光與異常血紅素都可能干擾讀值。"),
            ("B", "正確。O2Hb 與 deO2Hb 對紅光 660 nm 與紅外光 940 nm 的吸收比例不同，儀器利用脈動性動脈血訊號計算 SpO2。"),
            ("C", "錯誤。一氧化碳血紅素會被傳統 pulse oximeter 誤判為氧合血紅素，使 SpO2 假性偏高，而不是低於 SaO2。"),
            ("D", "錯誤。SpO2 大於 90% 不保證組織一定無缺氧；貧血、休克、CO 中毒或局部灌流不良仍可能造成組織缺氧。"),
        ],
        "core": "Pulse oximetry 反映的是脈動動脈血中 O2Hb/deO2Hb 的光吸收估算值，會受 COHb、低灌流與外界干擾影響，不能等同於完整組織氧合評估。",
        "key": "Pulse oximetry 使用 660 nm 紅光與 940 nm 紅外光區分 O2Hb 與 deO2Hb。",
        "front": "Pulse oximetry 原理與限制",
        "back": "正確原理是 O2Hb/deO2Hb 對 660 nm 與 940 nm 光吸收不同；COHb 會讓傳統 SpO2 假性偏高。",
        "summary": "SpO2 -> 光吸收估算血氧；COHb、低灌流、指甲油與動作會造成誤差。",
    },
    3: {
        "stem": "本題問 pacemaker 病人麻醉前與術中處置何者錯誤。電燒可能造成電磁干擾，磁鐵能否改變 pacing 模式取決於裝置種類與設定，不能保證完全避免干擾或危害。",
        "options": [
            ("A", "正確。非心臟手術前應確認 pacemaker 類型、適應症、電池、依賴程度與最近檢查結果，必要時請心臟電生理團隊評估。"),
            ("B", "錯誤。磁鐵通常可能使部分 pacemaker 進入非同步 pacing，但反應依廠牌與設定不同，也不能完全消除電燒干擾，因此不能說「即可完全避免」。"),
            ("C", "正確。心電圖濾波可能讓 pacing spike 不明顯；術中應確保監測能辨識 pacing 與實際脈搏反應。"),
            ("D", "正確。除 ECG 外，還要用 pulse oximetry 或動脈壓波形確認機械性心搏，避免只看到電訊號卻沒有有效灌流。"),
        ],
        "core": "Pacemaker 麻醉管理的陷阱是不能把磁鐵當成萬能保護；術前裝置評估、電燒策略與機械性脈搏監測都很重要。",
        "key": "磁鐵不能保證完全避免 pacemaker 術中電燒干擾，反應取決於裝置設定。",
        "front": "Pacemaker + 電燒 + 磁鐵",
        "back": "磁鐵反應不固定，不能保證完全避免 EMI；需術前查裝置並監測有效脈搏。",
        "summary": "Pacemaker 麻醉 -> 磁鐵不是萬能；術前裝置確認與術中有效灌流監測是重點。",
    },
    4: {
        "stem": "Midazolam 是 benzodiazepine，過量造成鎮靜與呼吸抑制時，特異性拮抗劑是 flumazenil，作用在 GABA-A receptor 的 benzodiazepine binding site。",
        "options": [
            ("A", "正確。Flumazenil 是 benzodiazepine receptor antagonist，可逆轉 midazolam 等 benzodiazepine 的鎮靜與呼吸抑制，但使用時要注意癲癇或長期使用者戒斷風險。"),
            ("B", "錯誤。Dexmedetomidine 是 alpha-2 agonist，用於鎮靜與止痛輔助，不是 benzodiazepine 拮抗劑。"),
            ("C", "錯誤。Ketamine 主要是 NMDA receptor antagonist，具有解離性麻醉與止痛效果，不會拮抗 midazolam。"),
            ("D", "錯誤。Naloxone 是 opioid receptor antagonist，用於嗎啡、fentanyl 等 opioid 過量，不是 midazolam 的解毒劑。"),
        ],
        "core": "解毒劑配對要記牢：benzodiazepine 對 flumazenil；opioid 對 naloxone。",
        "key": "Midazolam 過量的特異性拮抗劑是 flumazenil。",
        "front": "Midazolam overdose antidote",
        "back": "Flumazenil 拮抗 benzodiazepine 受體；naloxone 是 opioid 拮抗劑。",
        "summary": "麻醉解毒劑 -> benzodiazepine: flumazenil；opioid: naloxone。",
    },
    5: {
        "stem": "本題問 opioids 何者錯誤。嗎啡造成呼吸抑制主要與 mu receptor 作用相關，不是 kappa receptor。",
        "options": [
            ("A", "正確。傳統分類可提到 mu、kappa、delta 等 opioid receptors；sigma 現代多不再視為典型 opioid receptor，但舊式考題常列入歷史分類。"),
            ("B", "正確。典型 opioid receptors 屬於 G protein-coupled receptors，活化後抑制 adenylate cyclase、減少鈣離子流入並增加鉀離子外流。"),
            ("C", "錯誤。嗎啡的鎮痛、欣快與呼吸抑制主要經由 mu receptor，kappa receptor 較與脊髓鎮痛、鎮靜與 dysphoria 相關。"),
            ("D", "正確。Naloxone 是 opioid receptor antagonist，可快速逆轉 opioid 引起的呼吸抑制。"),
        ],
        "core": "Opioid 高頻考點：mu receptor 負責主要鎮痛與呼吸抑制；naloxone 是拮抗劑；opioid receptors 是 GPCR。",
        "key": "嗎啡呼吸抑制主要經 mu receptor，不是 kappa receptor。",
        "front": "Opioid receptor：morphine respiratory depression",
        "back": "Morphine 的呼吸抑制主要是 mu receptor；naloxone 可逆轉 opioid 作用。",
        "summary": "Opioid pharmacology -> mu: 鎮痛與呼吸抑制；naloxone: antagonist。",
    },
    6: {
        "stem": "本題問 ASA 預防術中周邊神經損傷建議何者不是。Lithotomy 過度牽拉腿後肌群主要可能牽涉坐骨神經或腓總神經張力，股神經較常與髖過度屈曲、外展、外旋或腹股溝壓迫相關。",
        "options": [
            ("A", "正確。術前確認病人能否忍受預期擺位，可提早發現關節活動受限、神經病變或疼痛風險。"),
            ("B", "正確。側臥時適當 chest roll 可減少腋窩與臂叢壓迫，降低上肢神經受損風險。"),
            ("C", "錯誤。Lithotomy 過度拉扯 hamstring 更容易牽涉坐骨神經張力；股神經傷害通常與髖部過度屈曲、外展、外旋或腹股溝區壓迫有關。"),
            ("D", "正確。手肘屈曲會增加 cubital tunnel 壓力，可能增加尺神經受壓風險。"),
        ],
        "core": "手術擺位神經傷害要把神經與姿勢配對：手肘屈曲傷尺神經、側臥腋窩壓迫傷臂叢、lithotomy 牽拉常牽涉坐骨或腓總神經。",
        "key": "Lithotomy 過度拉扯 hamstring 不是典型股神經損傷機轉。",
        "front": "ASA positioning nerve injury：lithotomy / ulnar / brachial plexus",
        "back": "Lithotomy hamstring traction 較牽涉坐骨神經；股神經多與髖屈曲外展外旋或腹股溝壓迫有關。",
        "summary": "術中擺位 -> 神經損傷取決於壓迫或牽拉位置；C 的股神經配對不當。",
    },
    7: {
        "stem": "本題問 preeclampsia 何者錯誤。Methylergonovine 會造成血管收縮、升高血壓，子癲前症或高血壓病人產後促進子宮收縮時不應照一般常規使用。",
        "options": [
            ("A", "正確。妊娠 20 週後新發高血壓合併蛋白尿，是典型子癲前症診斷框架。"),
            ("B", "正確。嚴重高血壓會增加腦出血、肺水腫、凝血異常等風險；收縮壓達 160 mmHg 屬 severe range，需積極控制。"),
            ("C", "正確。Magnesium sulfate 用於預防或治療子癲抽搐，並會增強非去極化肌肉鬆弛劑作用，插管麻醉時需調整劑量與監測。"),
            ("D", "錯誤。Methylergonovine 具血管收縮與升壓作用，子癲前症或高血壓患者應避免常規使用，以免血壓惡化。"),
        ],
        "core": "子癲前症產婦要避免會升高血壓的 uterotonic；methylergonovine 是常考禁忌，magnesium sulfate 會增強肌鬆作用。",
        "key": "Preeclampsia 產後不宜常規使用 methylergonovine，因其可升高血壓。",
        "front": "Preeclampsia：uterotonic 禁忌與 magnesium sulfate",
        "back": "Methylergonovine 會血管收縮升壓，preeclampsia 應避免；MgSO4 會增強非去極化肌鬆。",
        "summary": "Preeclampsia -> severe BP 要治療；MgSO4 防抽搐；methylergonovine 會升壓不適合。",
    },
    8: {
        "stem": "Pregabalin 是 gabapentinoid，主要結合電壓依賴性鈣離子通道的 alpha-2-delta subunit，減少興奮性神經傳遞物質釋放而止痛。",
        "options": [
            ("A", "錯誤。Sodium channel blocker 是局部麻醉藥、部分抗癲癇藥等常見機轉，不是 pregabalin 的主要靶點。"),
            ("B", "正確。Pregabalin 作用於 voltage-gated calcium channel 的 alpha-2-delta subunit，常用於神經病變痛。"),
            ("C", "錯誤。Chloride channel 與 GABA-A receptor 相關藥物較有關，pregabalin 雖名稱類似 GABA，但不直接活化 GABA receptor 或 chloride channel。"),
            ("D", "錯誤。Potassium channel opener 不是 pregabalin 的主要止痛機轉。"),
        ],
        "core": "Pregabalin/gabapentin 的考點是 alpha-2-delta calcium channel subunit，不是 sodium channel 或 GABA receptor。",
        "key": "Pregabalin 作用於 voltage-gated calcium channel 的 alpha-2-delta subunit。",
        "front": "Pregabalin analgesic mechanism",
        "back": "Pregabalin 結合鈣離子通道 alpha-2-delta subunit，減少神經傳遞物質釋放。",
        "summary": "Pregabalin -> calcium channel alpha-2-delta -> neuropathic pain。",
    },
    9: {
        "stem": "本題問最不適合拔管的 weaning 指標。RSBI = 呼吸頻率/潮氣容積，數值越高代表淺快呼吸、脫離呼吸器失敗風險越高；大於 105 通常不適合拔管。",
        "options": [
            ("A", "錯誤。Tidal volume >5 mL/kg、vital capacity >10 mL/kg 是可接受的呼吸力學條件，支持嘗試拔管。"),
            ("B", "正確。RSBI >105 表示呼吸淺快，預測 weaning failure，最不適合考慮拔管。"),
            ("C", "錯誤。最大吸氣壓力小於 -25 cmH2O 代表吸氣肌力足夠，是較有利的拔管條件。"),
            ("D", "錯誤。在 FiO2 40-50%、PEEP <5 cmH2O 下 SaO2 >90%，代表氧合條件大致可接受。"),
        ],
        "core": "拔管前要看氧合、通氣、呼吸肌力與 RSBI；RSBI >105 是常考的拔管失敗指標。",
        "key": "RSBI >105 代表淺快呼吸，預測脫離呼吸器失敗。",
        "front": "Weaning/extubation：RSBI cutoff",
        "back": "RSBI >105 最不適合拔管；MIP < -25、TV >5 mL/kg、低 FiO2/PEEP 下氧合可接受較有利。",
        "summary": "Weaning criteria -> RSBI 高代表失敗風險；>105 不適合拔管。",
    },
    10: {
        "stem": "Retinitis pigmentosa 的典型三徵是 bone-spicule pigmentation、waxy pallor of optic disc、retinal arteriole attenuation；macular edema 可見但不是 classical triad。",
        "options": [
            ("A", "錯誤。骨刺狀黑色素沉積是 retinitis pigmentosa 的典型眼底表現之一。"),
            ("B", "錯誤。視神經盤蠟樣蒼白也是典型三徵之一。"),
            ("C", "錯誤。視網膜小動脈變細是典型三徵之一。"),
            ("D", "正確。黃斑部水腫可作為併發表現影響中央視力，但不屬於 classical triad。"),
        ],
        "core": "RP classical triad：bone-spicule pigmentation、waxy disc pallor、arteriolar attenuation；不要把 macular edema 放進三徵。",
        "key": "Retinitis pigmentosa 典型三徵不包含 macular edema。",
        "front": "Retinitis pigmentosa classical triad",
        "back": "Bone-spicule pigmentation、waxy optic disc pallor、arteriolar attenuation；不含 macular edema。",
        "summary": "RP -> 三徵是骨刺色素、視神經蒼白、小動脈變細。",
    },
    11: {
        "stem": "角膜鹼性灼傷比酸性灼傷更容易穿透組織、造成深層破壞，預後判斷的重要因素之一是 limbal ischemia 程度，因輪部含角膜上皮幹細胞。",
        "options": [
            ("A", "錯誤。鹼性物質會皂化脂肪、快速穿透角膜與前房，通常比酸性灼傷預後更差。"),
            ("B", "錯誤。急救是大量、持續以生理食鹽水或清水沖洗至 pH 接近中性，不應刻意用酸性溶液中和，避免放熱或二次傷害。"),
            ("C", "錯誤。急性期可在眼科監測下使用 topical steroid 減少發炎與角膜溶解風險，並非前 10 天絕對禁止。"),
            ("D", "正確。Limbal ischemia 代表角膜輪部幹細胞與血流受損，與上皮修復能力及視力預後密切相關。"),
        ],
        "core": "眼化學灼傷第一步是立即大量沖洗；鹼傷重於酸傷；limbal ischemia 是預後關鍵。",
        "key": "角膜鹼傷預後與 limbal ischemia 程度高度相關。",
        "front": "Alkali corneal burn prognosis",
        "back": "立即大量沖洗；鹼傷比酸傷嚴重；limbal ischemia 越重預後越差。",
        "summary": "Corneal alkali burn -> urgent irrigation + limbal ischemia predicts prognosis。",
    },
    12: {
        "stem": "Carotid cavernous fistula 造成海綿竇與眼靜脈壓上升，典型可見眼球突出、結膜充血水腫與 corkscrew-like episcleral vessels。",
        "options": [
            ("A", "錯誤。Salmon patch 常用來描述結膜淋巴瘤等粉紅色病灶，不是 CCF 的典型血管表徵。"),
            ("B", "錯誤。Kaposi sarcoma 是血管性腫瘤，可見於免疫低下病人，不是 CCF 的典型結膜表現。"),
            ("C", "正確。CCF 造成上眼靜脈回流壓升高，結膜與上鞏膜血管可呈扭曲擴張的 corkscrew-like vessels。"),
            ("D", "錯誤。微小動脈瘤常見於糖尿病視網膜病變的視網膜表現，不是 CCF 的主要結膜表徵。"),
        ],
        "core": "CCF 的眼部關鍵字是 pulsatile proptosis、bruit、chemosis、上鞏膜 corkscrew vessels。",
        "key": "Carotid cavernous fistula 可造成 corkscrew-like conjunctival/episcleral vessels。",
        "front": "Carotid cavernous fistula conjunctival sign",
        "back": "CCF 使眼靜脈壓升高，出現結膜與上鞏膜 corkscrew-like vessels。",
        "summary": "CCF -> venous congestion -> corkscrew episcleral vessels。",
    },
    13: {
        "stem": "白內障術後 posterior capsular opacity 是人工水晶體後方囊袋混濁，標準治療是 Nd:YAG laser posterior capsulotomy。",
        "options": [
            ("A", "正確。Nd:YAG laser 可在後囊造成開口，使視軸恢復透明，是 PCO 的常用治療。"),
            ("B", "錯誤。Phacoemulsification 是移除原本白內障水晶體的手術，不是術後後囊混濁的主要治療。"),
            ("C", "錯誤。人工水晶體是在白內障手術時植入，不能直接治療後囊混濁。"),
            ("D", "錯誤。人工玻璃體不是 PCO 的治療方式。"),
        ],
        "core": "白內障術後看不清若是 posterior capsular opacity，考 Nd:YAG laser capsulotomy。",
        "key": "Posterior capsular opacity 的治療是 Nd:YAG laser capsulotomy。",
        "front": "PCO after cataract surgery treatment",
        "back": "用 Nd:YAG laser posterior capsulotomy，不是再做 phacoemulsification。",
        "summary": "白內障術後 PCO -> Nd:YAG laser。",
    },
    14: {
        "stem": "眼球往外上方看是 abduction 加 elevation。在外轉位置時，上直肌是主要上轉肌，因此需 lateral rectus 加 superior rectus。",
        "options": [
            ("A", "正確。外直肌使眼球外轉，上直肌在外轉位置負責上轉，兩者共同讓眼球看向 temporal upper。"),
            ("B", "錯誤。上斜肌主要功能是內旋，並在內轉位置使眼球下轉，不是外上看的主要肌肉。"),
            ("C", "錯誤。下直肌主要下轉，與外上方運動方向相反。"),
            ("D", "錯誤。下斜肌在內轉位置主要上轉，但題目已指定外直肌共同作用，外上方主要配上直肌。"),
        ],
        "core": "垂直直肌在外轉眼位作用最純；上直肌負責外轉位上轉，下直肌負責外轉位下轉。",
        "key": "眼球外上看需要 lateral rectus 加 superior rectus。",
        "front": "Eye movement：temporal upper gaze",
        "back": "外上方 = lateral rectus 外轉 + superior rectus 上轉。",
        "summary": "眼外肌 -> 外轉位上轉靠 superior rectus。",
    },
    15: {
        "stem": "本題問眼球運動敘述何者錯誤。Accommodative convergence 是因調節反射誘發的會聚，不屬於 tonic convergence。",
        "options": [
            ("A", "正確。Duction 是單眼運動，可描述 adduction、abduction、elevation、depression、intorsion、extorsion。"),
            ("B", "正確。Version 是雙眼同向運動，例如雙眼一起看右上或左下。"),
            ("C", "正確。Vergence 是雙眼反向運動，包括 convergence 與 divergence。"),
            ("D", "錯誤。Accommodative convergence 來自近距離調節反射；tonic convergence 是基礎眼位張力，兩者分類不同。"),
        ],
        "core": "Duction 單眼、version 雙眼同向、vergence 雙眼異向；accommodative convergence 不等於 tonic convergence。",
        "key": "Accommodative convergence 是調節誘發的會聚，不是 tonic convergence。",
        "front": "Duction / version / vergence / accommodative convergence",
        "back": "Duction 單眼；version 同向；vergence 異向；accommodative convergence 不是 tonic convergence。",
        "summary": "眼球運動分類 -> D 錯在把調節性會聚歸為強直性會聚。",
    },
    16: {
        "stem": "Uveal coloboma 多因 embryonic fissure 閉合不全，典型位於眼球下方或 inferonasal 區域，鐘點位置常以 6 點鐘表示。",
        "options": [
            ("A", "錯誤。3 點鐘不是典型胚裂閉合不全的位置。"),
            ("B", "正確。先天性脈絡膜或葡萄膜缺損典型在 6 點鐘方向，反映胚裂位置。"),
            ("C", "錯誤。9 點鐘不是典型位置。"),
            ("D", "錯誤。12 點鐘位於上方，不符合典型 embryonic fissure 位置。"),
        ],
        "core": "Coloboma 的高頻字眼是 embryonic fissure failure，典型在 inferonasal/6 o'clock。",
        "key": "Uveal coloboma 通常位於 6 點鐘方向。",
        "front": "Uveal tract coloboma location",
        "back": "胚裂閉合不全造成，典型在眼球下方 6 點鐘。",
        "summary": "Coloboma -> embryonic fissure -> 6 o'clock。",
    },
    17: {
        "stem": "砂眼由 Chlamydia trachomatis 造成，包涵體位於細胞質內，不是細胞核內；題目問錯誤敘述，因此答案是 C。",
        "options": [
            ("A", "正確。砂眼病原是 Chlamydia trachomatis，慢性感染可造成結膜瘢痕與倒睫。"),
            ("B", "正確。Cicatricial trachoma 可在上眼瞼結膜看到 Arlt line，代表結膜瘢痕。"),
            ("C", "錯誤。Chlamydia 的包涵體位於細胞質內，典型不是細胞核內嗜伊紅性包涵體；核內包涵體較會想到病毒感染。"),
            ("D", "正確。治療可用 azithromycin 或 tetracycline 類藥物；舊式考題常列口服與局部四環黴素治療。"),
        ],
        "core": "Trachoma：Chlamydia、上瞼結膜濾泡與瘢痕、Arlt line、Herbert pits；包涵體在細胞質。",
        "key": "砂眼披衣菌包涵體在細胞質內，不在細胞核內。",
        "front": "Trachoma inclusion body location",
        "back": "Chlamydia trachomatis 造成砂眼；包涵體在細胞質，非細胞核。",
        "summary": "Trachoma -> Chlamydia -> cytoplasmic inclusion body。",
    },
    18: {
        "stem": "Neonatal gonococcal conjunctivitis 多在出生後 2-5 天發生大量膿性分泌物，進展快且可傷害角膜；第三至第四週較像披衣菌性結膜炎時間。",
        "options": [
            ("A", "正確。新生兒常經產道接觸母親淋病雙球菌而感染。"),
            ("B", "正確。淋病性結膜炎具侵襲性，需全身抗生素治療，常合併局部清潔或局部治療。"),
            ("C", "錯誤。淋病性結膜炎通常出生後數天內出現；第三至第四週才開始較不符合，反而應考慮披衣菌等病因。"),
            ("D", "正確。應做 Gram stain 與培養以確認病原並導引治療。"),
        ],
        "core": "新生兒眼炎時間軸：淋病通常 2-5 天、披衣菌約 5-14 天或較晚；淋病需快速全身治療以保護角膜。",
        "key": "新生兒淋病性結膜炎通常出生後數天內出現，不是第三至第四週。",
        "front": "Neonatal gonococcal conjunctivitis onset",
        "back": "通常出生後 2-5 天大量膿性分泌物，需全身抗生素與培養確認。",
        "summary": "Neonatal conjunctivitis -> gonococcus early and aggressive。",
    },
    19: {
        "stem": "Scala media 的 endolymph 與 +80 mV endocochlear potential 由 stria vascularis 維持，與鉀離子分泌及內耳電化學梯度有關。",
        "options": [
            ("A", "正確。血管紋負責產生並維持 endolymph 的高鉀濃度與正電位，是 endocochlear potential 來源。"),
            ("B", "錯誤。Reissner membrane 分隔 scala vestibuli 與 scala media，不是主要電位來源。"),
            ("C", "錯誤。Basilar membrane 支撐 Corti organ 並參與頻率分析，不產生 +80 mV 電位。"),
            ("D", "錯誤。Organ of Corti 含毛細胞，負責機械轉電訊號，但 endocochlear potential 主要由 stria vascularis 產生。"),
        ],
        "core": "內耳高頻配對：scala media 裝 endolymph；stria vascularis 產生 endocochlear potential。",
        "key": "Endocochlear potential 來自 stria vascularis。",
        "front": "Endocochlear potential source",
        "back": "Scala media 的 +80 mV 電位由 stria vascularis 維持。",
        "summary": "Cochlea -> stria vascularis -> endolymph high K+ and +80 mV。",
    },
    20: {
        "stem": "圖像題官方答案為原發性後天性膽脂瘤。此型通常與咽鼓管功能不良造成 pars flaccida retraction pocket 相關，角化上皮堆積後形成膽脂瘤。",
        "options": [
            ("A", "錯誤。先天性膽脂瘤常見於完整鼓膜後方的白色腫塊，沒有典型後天性退縮袋病史。"),
            ("B", "正確。原發性後天性膽脂瘤多由鼓膜鬆弛部退縮袋形成，逐漸堆積角化物並侵蝕中耳或乳突骨質。"),
            ("C", "錯誤。繼發性後天性膽脂瘤常與鼓膜穿孔後鱗狀上皮向中耳移入相關，機轉不同。"),
            ("D", "錯誤。耳道膽脂瘤發生在外耳道，與中耳 pars flaccida retraction pocket 的典型表現不同。"),
        ],
        "core": "膽脂瘤分類要看位置與鼓膜狀態：pars flaccida 退縮袋是原發性後天性膽脂瘤的典型線索。",
        "key": "原發性後天性膽脂瘤常由 pars flaccida retraction pocket 形成。",
        "front": "Primary acquired cholesteatoma",
        "back": "多與咽鼓管功能不良造成鼓膜鬆弛部退縮袋與角化物堆積有關。",
        "summary": "Cholesteatoma -> primary acquired = pars flaccida retraction pocket。",
        "notes": ["圖像題：說明依官方答案與典型耳鏡表現撰寫，建議人工確認原圖位置。"],
    },
}


DATA.update({
    21: {
        "stem": "急性周邊型顏面神經麻痺最常見原因是 idiopathic Bell palsy。其他原因如 Ramsay Hunt、顳骨骨折或顱底感染需依病史與體徵辨識，但盛行率較低。",
        "options": [("A", "錯誤。Ramsay Hunt syndrome 由帶狀疱疹侵犯膝狀神經節造成，常有耳痛、水泡與較差預後，但不是最常見原因。"), ("B", "正確。Bell palsy 是最常見急性周邊顏面神經麻痺原因，屬排除其他病因後的特發性診斷。"), ("C", "錯誤。顱底骨髓炎多見於糖尿病或免疫低下者的惡性外耳炎延伸，遠較少見。"), ("D", "錯誤。顳骨骨折可造成外傷性顏面神經麻痺，但需有外傷史，不是最常見原因。")],
        "core": "急性單側周邊顏面麻痺最常見是 Bell palsy；有耳疱疹、外傷、感染或漸進惡化時才要優先想其他病因。",
        "key": "急性顏面神經麻痺最常見原因是 Bell palsy。",
        "front": "Most common acute facial palsy",
        "back": "Bell palsy 是最常見的急性周邊型顏面神經麻痺。",
        "summary": "Facial palsy -> most common = Bell palsy。",
    },
    22: {
        "stem": "過敏原皮膚測試的優點包括敏感度高、快速、相對便宜；但抗組織胺等藥物會抑制皮膚反應而影響結果。",
        "options": [("A", "錯誤。皮膚點刺測試敏感度高，是其優點之一。"), ("B", "錯誤。測試後短時間即可判讀 wheal-and-flare 反應，結果快速。"), ("C", "錯誤。相較許多血液檢查，皮膚測試費用較低。"), ("D", "正確。抗組織胺、部分抗憂鬱藥或類固醇使用狀況可能影響皮膚反應，因此「藥物不影響」不是優點。")],
        "core": "皮膚過敏原測試會被抗組織胺等藥物干擾，檢查前用藥史很重要。",
        "key": "過敏原皮膚測試會受藥物影響，尤其抗組織胺。",
        "front": "Allergy skin test limitations",
        "back": "優點是快、便宜、敏感度高；缺點是會受抗組織胺等藥物影響。",
        "summary": "Allergy skin test -> rapid and sensitive, but medication affects result。",
    },
    23: {
        "stem": "阻塞性睡眠呼吸中止症的標準診斷檢查是 polysomnography，治療上大多數成人的一線標準治療為 nasal CPAP。",
        "options": [("A", "錯誤。成人睡眠呼吸中止通常以 apnea/hypopnea 持續至少 10 秒並計算 AHI；題目所列每次超過 5 秒不符合典型標準。"), ("B", "錯誤。阻塞位置常在軟顎、口咽側壁、舌根等多層次，不能簡化為最常在舌根。"), ("C", "正確。Nasal CPAP 可維持上呼吸道正壓、避免睡眠中塌陷，是多數成人 OSA 的標準治療。"), ("D", "錯誤。Adenotonsillectomy 是兒童扁桃腺或腺樣體肥大 OSA 的常見首選，成人通常先考慮 CPAP 與風險因子處理。")],
        "core": "成人 OSA 治療首選常是 CPAP；兒童腺扁桃體肥大才常以 adenotonsillectomy 為首選。",
        "key": "成人 OSA 多數病人的標準治療是 nasal CPAP。",
        "front": "OSA diagnosis/treatment",
        "back": "成人 OSA：PSG 診斷，CPAP 標準治療；兒童腺扁桃肥大常手術。",
        "summary": "OSA -> adult standard treatment = nasal CPAP。",
    },
    24: {
        "stem": "聲音沙啞合併喉部腫塊，若切片為鱗狀上皮癌，早期或可切除病灶常可依分期選擇手術或放射線治療。此題重點是喉癌治療選項與圖中位置判讀。",
        "options": [("A", "錯誤。喉癌與吸菸、飲酒關聯最強；檳榔與口腔癌關係更密切，不能說本圖喉部腫瘤與長期嚼檳榔密切相關。"), ("B", "錯誤。官方答案不支持箭頭位於 supraglottis；聲音沙啞常提示聲門區病灶較早出現症狀。"), ("C", "錯誤。聲門癌因淋巴引流較少，早期頸部淋巴結轉移相對少見；supraglottic cancer 才較常頸轉移。"), ("D", "正確。喉部 squamous cell carcinoma 的治療依分期與部位，可考慮手術切除或放射線治療，並兼顧發聲與吞嚥功能。")],
        "core": "喉癌症狀與轉移風險依部位不同：聲門癌早期沙啞、淋巴轉移較少；治療可手術或放療。",
        "key": "喉部鱗狀上皮癌可依分期考慮手術切除或放射線治療。",
        "front": "Laryngeal SCC treatment and glottic cancer clues",
        "back": "聲門癌常早期沙啞且頸轉移較少；SCC 可依分期手術或放療。",
        "summary": "Laryngeal cancer -> biopsy SCC -> surgery or radiotherapy depending on stage。",
        "notes": ["圖像題：說明依官方答案與常見喉癌部位特徵撰寫，建議人工確認原圖箭頭。"],
    },
    25: {
        "stem": "晚飯後喉痛吞嚥困難合併頸部 X 光，多考慮食道異物。食道鏡若發現疑似穿孔，重點是立即停止經口進食、引流或減壓並進一步處理；放置鼻胃管可協助減壓與營養路徑規劃。",
        "options": [("A", "錯誤。此類魚刺或食道異物常卡在食道入口或頸段食道，不是會厭軟骨本身。"), ("B", "錯誤。硬式食道鏡移除異物通常需全身麻醉與良好氣道保護，局部麻醉下處理並非標準。"), ("C", "錯誤。硬式與軟式食道鏡併發症風險不完全相同，硬式操作對穿孔等風險較需注意。"), ("D", "正確。若疑似食道破裂，應禁食、減少污染與壓力，放置鼻胃管並安排後續影像、抗生素或外科處置。")],
        "core": "食道異物最怕穿孔；一旦懷疑破裂，禁食、減壓、抗生素與外科評估是處置主軸。",
        "key": "食道鏡發現疑似食道破裂時，應禁食並放置鼻胃管等減壓處置。",
        "front": "Esophageal foreign body complication management",
        "back": "疑似食道破裂：NPO、鼻胃管減壓、抗生素與後續外科/影像評估。",
        "summary": "Esophageal foreign body -> perforation suspected -> NPO + NG tube + urgent management。",
        "notes": ["圖像題：未直接檢視原始頸部 X 光，已依題幹與官方答案撰寫。"],
    },
    26: {
        "stem": "舌癌 4.5 cm 且未侵犯鄰近構造屬 T3；同側單一 4 cm 淋巴結、無明顯 extranodal extension，依 AJCC 第 7 版為 N2a，第 8 版口腔癌若無 ENE 仍符合 N2a；整體為 stage IVA。",
        "options": [("A", "錯誤。腫瘤最大徑大於 4 cm，不能分為 T2；且 4 cm 單一同側淋巴結也不是 N1。"), ("B", "錯誤。N2a 正確，但原發腫瘤 4.5 cm 應為 T3，不是 T2。"), ("C", "錯誤。T3 正確，但 N1 是單一同側淋巴結小於等於 3 cm；本題淋巴結 4 cm，應為 N2a。"), ("D", "正確。T3 加 N2a 的口腔舌癌臨床分期為 stage IVA。")],
        "core": "口腔癌分期先看腫瘤大小與淋巴結大小：>4 cm 是 T3；單一同側 3-6 cm 是 N2a；組合為 stage IVA。",
        "key": "舌癌 4.5 cm 為 T3；同側單一 4 cm 淋巴結為 N2a，stage IVA。",
        "front": "Tongue cancer AJCC staging: 4.5 cm tumor + 4 cm ipsilateral node",
        "back": "T3N2a, stage IVA。",
        "summary": "Tongue SCC staging -> >4 cm T3; ipsilateral single 3-6 cm node N2a。",
    },
    27: {
        "stem": "耳部檢查正常但有間歇性耳痛，要想到 referred otalgia。扁桃腺與口咽區可經舌咽神經轉移痛到耳部，且此人有菸酒檳榔頭頸癌風險。",
        "options": [("A", "錯誤。舌癌也可造成轉移痛，但典型耳痛牽涉舌咽神經時，扁桃腺/口咽癌更常被考。"), ("B", "錯誤。聲門癌常以聲音沙啞表現，耳痛不是最典型早期線索。"), ("C", "正確。扁桃腺癌屬口咽癌，常可經舌咽神經造成 referred otalgia，而耳鏡檢查可正常。"), ("D", "錯誤。頰黏膜癌與檳榔關係密切，但相較扁桃腺癌較不是正常耳檢下耳痛的典型來源。")],
        "core": "正常耳鏡但耳痛，尤其有頭頸癌風險，要檢查口咽、下咽與喉部；扁桃腺癌可造成轉移性耳痛。",
        "key": "正常耳檢的轉移性耳痛需想到扁桃腺/口咽癌。",
        "front": "Referred otalgia + normal ear exam + head and neck cancer",
        "back": "最典型要想到扁桃腺癌，經舌咽神經造成耳痛。",
        "summary": "Referred otalgia -> normal ear exam -> oropharyngeal/tonsillar cancer。",
    },
    28: {
        "stem": "Gravida 指曾懷孕次數，para 指達可存活週數後分娩次數。此女性曾懷孕兩次但都自然流產，未曾分娩可存活胎兒，因此是 nullipara，而不是 nulligravida。",
        "options": [("A", "錯誤。Multipara 指已分娩達可存活週數至少兩次，與兩次流產不符。"), ("B", "錯誤。Nulligravida 是從未懷孕；本題曾懷孕兩次。"), ("C", "正確。Nullipara 指未曾有達可存活週數的分娩，即使曾懷孕或流產仍可屬 nullipara。"), ("D", "錯誤。Primipara 指有一次達可存活週數的分娩，本題沒有。")],
        "core": "產科名詞要分清：gravida 看懷孕次數，para 看達可存活週數的分娩次數；流產不等於 para。",
        "key": "曾懷孕但均流產、無可存活週數分娩者為 nullipara。",
        "front": "Gravida vs para：兩次自然流產",
        "back": "曾懷孕所以不是 nulligravida；未曾分娩可存活胎兒所以是 nullipara。",
        "summary": "Obstetric history -> pregnancies count gravida; viable deliveries count para。",
    },
    29: {
        "stem": "羊水通常偏中性至弱鹼性，pH 約 7.0-7.5；這也是臨床上用 nitrazine test 協助判斷破水的基礎之一。",
        "options": [("A", "錯誤。pH 4.5-5.5 較接近正常陰道酸性環境，不是羊水。"), ("B", "錯誤。pH 5.6-6.5 仍偏低，較不符合羊水常見範圍。"), ("C", "正確。羊水 pH 最常約 7.0-7.5，較陰道分泌物鹼性。"), ("D", "錯誤。pH 8.0-8.5 過高，不是最常見羊水範圍。")],
        "core": "破水判讀常考：陰道分泌物偏酸，羊水偏鹼，常約 pH 7.0-7.5。",
        "key": "羊水 pH 最常介於 7.0-7.5。",
        "front": "Amniotic fluid pH",
        "back": "羊水偏鹼，常約 pH 7.0-7.5；陰道環境較酸。",
        "summary": "Amniotic fluid -> pH 7.0-7.5。",
    },
    30: {
        "stem": "肩難產處理避免 fundal pressure，因會使肩膀更卡在恥骨後方並增加子宮破裂或胎兒傷害風險；應用 McRoberts、suprapubic pressure、旋轉手法或取後肩。",
        "options": [("A", "錯誤。Woods corkscrew maneuver 是旋轉胎肩解除肩難產的標準手法之一。"), ("B", "正確。Fundal pressure 不是肩難產處理方法，且可能加重嵌頓與傷害。"), ("C", "錯誤。McRoberts maneuver 是第一線處置，透過屈髖改變骨盆角度。"), ("D", "錯誤。Delivery of posterior shoulder 可減少肩徑，是肩難產處理方式之一。")],
        "core": "肩難產禁忌是 fundal pressure；可用 McRoberts、suprapubic pressure、Woods corkscrew、取後肩。",
        "key": "肩難產處置不應使用 fundal pressure。",
        "front": "Shoulder dystocia management contraindication",
        "back": "Fundal pressure 會加重嵌頓；正確處置包括 McRoberts、旋轉手法、取後肩。",
        "summary": "Shoulder dystocia -> never fundal pressure。",
    },
})


DATA.update({
    41: {"stem": "雙胞胎 A 羊水過多且較大、雙胞胎 B 羊水過少且較小，典型符合 twin-twin transfusion syndrome。捐贈者常羊水少、貧血與生長受限；受贈者常羊水多、紅血球增多或心衰竭風險。", "options": [("A", "錯誤。羊水過多通常發生在受贈者，捐贈者因尿量少常羊水過少。"), ("B", "錯誤。捐贈者可有貧血，但不是典型溶血性貧血；機轉是胎盤血管吻合造成血流轉移。"), ("C", "錯誤。紅血球增多較常見於受贈者，捐贈者較可能貧血。"), ("D", "正確。超音波可見 donor 與 recipient 體重、羊水量、膀胱大小等 phenotype 差異。")], "core": "TTTS：donor 小、貧血、羊水少；recipient 大、polycythemia、羊水多與心臟負荷。", "key": "TTTS 可由超音波觀察 donor/recipient phenotype 差異。", "front": "TTTS donor vs recipient", "back": "Donor：oligohydramnios、貧血、生長受限；recipient：polyhydramnios、polycythemia。", "summary": "Twin-twin transfusion -> ultrasound phenotype discordance。"},
    42: {"stem": "35 週子癲前症且血壓 172/116 mmHg、尿蛋白 3+、體重快速增加，屬 severe features，需要住院評估與治療，不能只門診追蹤。", "options": [("A", "錯誤。嚴重高血壓不能只治療後門診追蹤，需要住院監測母胎狀況。"), ("B", "錯誤。只評估胎兒而門診追蹤會忽略母體 severe preeclampsia 風險。"), ("C", "錯誤。雖然需同時處理血壓與胎兒評估，但 severe range blood pressure 應住院，不適合門診追蹤。"), ("D", "正確。立即住院可控制血壓、給予 magnesium sulfate 評估、監測胎兒並規劃分娩時機。")], "core": "Preeclampsia with severe-range BP 是住院處理警訊，需母胎監測與治療。", "key": "子癲前症合併 172/116 mmHg 應立即住院治療。", "front": "Severe preeclampsia management", "back": "Severe-range BP 或症狀需住院控制血壓、預防抽搐並評估分娩。", "summary": "Preeclampsia severe features -> inpatient management。"},
    43: {"stem": "Burch colposuspension 會將陰道旁筋膜懸吊到 iliopectineal ligament，也就是 Cooper's ligament。官方圖中標示 C 為 Cooper's ligament。", "options": [("A", "錯誤。標示 A 不是官方答案所指 Cooper's ligament。"), ("B", "錯誤。標示 B 不是 iliopectineal ligament 的位置。"), ("C", "正確。Cooper's ligament 位於恥骨上支後方的堅韌骨膜韌帶，是 Burch colposuspension 懸吊縫合固定點。"), ("D", "錯誤。標示 D 不是本題所問 Cooper's ligament。")], "core": "Burch 手術的固定點是 Cooper's ligament；圖像題需辨識恥骨後空間的解剖標示。", "key": "Laparoscopic Burch colposuspension 中 Cooper's ligament 為圖中 C。", "front": "Burch colposuspension Cooper's ligament", "back": "固定於 iliopectineal/Cooper's ligament；本圖標示 C。", "summary": "Burch colposuspension -> Cooper ligament fixation point = C。", "notes": ["圖像題：未直接檢視原圖，依官方答案與手術解剖撰寫。"]},
    44: {"stem": "本題問早期懷孕何者錯誤。MTX 治療與 salpingostomy 都有再次外孕風險，但不能說 MTX 比 salpingostomy 尤高；治療選擇取決於穩定度、hCG、腫塊大小與生育考量。", "options": [("A", "正確。骨盆腔發炎會傷害輸卵管，是子宮外孕重要危險因子。"), ("B", "錯誤。MTX 並不會比 salpingostomy 特別造成更高再次外孕風險；輸卵管原本病變才是復發風險重點。"), ("C", "正確。早期正常子宮內懷孕 hCG 約每 48 小時明顯上升，傳統常用至少增加約 66% 作為參考。"), ("D", "正確。hCG 高於 discriminatory zone 且 48 小時上升不足，胚胎存活或正常子宮內懷孕機會降低，需要警覺。")], "core": "子宮外孕危險因子是輸卵管受損；hCG 趨勢可協助判斷早期懷孕是否正常。", "key": "MTX 治療子宮外孕不代表再次外孕風險必然高於 salpingostomy。", "front": "Ectopic pregnancy risk and hCG trend", "back": "PID 是危險因子；正常早孕 hCG 48 小時應明顯上升；B 敘述過度武斷。", "summary": "Early pregnancy -> PID risk; hCG trend; MTX does not inherently raise recurrent ectopic more than salpingostomy。"},
    45: {"stem": "子宮內膜異位症可由症狀、內診、超音波或 CA-125 懷疑，但確定診斷需腹腔鏡直接觀察病灶並切片病理確認。", "options": [("A", "錯誤。超音波可偵測 endometrioma 等病灶，但不能作為所有內膜異位症的確診。"), ("B", "錯誤。內診壓痛、子宮後傾或結節只能支持診斷。"), ("C", "錯誤。CA-125 可升高但特異性不足，也可受月經、發炎或其他腫瘤影響。"), ("D", "正確。腹腔鏡下病灶切片病理是確定診斷方式。")], "core": "Endometriosis 的 gold standard 是 laparoscopic visualization with biopsy。", "key": "子宮內膜異位症確診需腹腔鏡下切片。", "front": "Definitive diagnosis of endometriosis", "back": "腹腔鏡直接觀察並切片病理確認。", "summary": "Endometriosis -> definitive diagnosis = laparoscopy + biopsy。"},
    46: {"stem": "卵巢上皮癌病理中，clear cell 與 endometrioid 常和 endometriosis 相關；endometrioid 可合併子宮內膜癌。大量 psammoma bodies 典型見於漿液性腫瘤，不能代表預後極差。", "options": [("A", "正確。Endometriosis 相關卵巢癌常見 clear cell 與 endometrioid subtype。"), ("B", "正確。Endometrioid ovarian carcinoma 較可能與同步子宮內膜癌相關。"), ("C", "正確。卵巢 clear cell carcinoma 在分級系統中常視為高級別或不再細分低級別。"), ("D", "錯誤。Psammoma body 是漿液性腫瘤常見鈣化結構，不能以大量存在就推論預後極差。")], "core": "Psammoma bodies 是 serous tumor 常見病理線索，不等於預後極差；endometriosis 關聯 clear cell/endometrioid。", "key": "漿液性卵巢癌的 psammoma body 不代表預後極差。", "front": "Epithelial ovarian cancer pathology: psammoma body", "back": "Psammoma body 常見於 serous tumor，是診斷線索而非極差預後指標。", "summary": "Ovarian epithelial cancer -> endometriosis linked clear cell/endometrioid; psammoma body not poor prognosis。"},
    47: {"stem": "題幹描述 large round/ovoid/polygonal cells、clear pale cytoplasm、large irregular nuclei、prominent nucleoli，是 dysgerminoma 的典型病理形態。", "options": [("A", "錯誤。Sertoli-Leydig cell tumor 屬 sex cord-stromal tumor，常有男性化表現與不同組織型態。"), ("B", "正確。Dysgerminoma 細胞大、胞質清亮、核仁明顯，類似 seminoma。"), ("C", "錯誤。Adult granulosa cell tumor 常見 Call-Exner bodies 與 coffee-bean nuclei。"), ("D", "錯誤。Endodermal sinus tumor 常見 Schiller-Duval bodies，AFP 升高。")], "core": "Dysgerminoma 病理像 seminoma：大細胞、清亮胞質、明顯核仁；yolk sac tumor 看 Schiller-Duval bodies。", "key": "大圓形清亮胞質且核仁明顯的卵巢生殖細胞腫瘤是 dysgerminoma。", "front": "Dysgerminoma histology", "back": "Large polygonal cells, clear cytoplasm, prominent nucleoli。", "summary": "Ovarian germ cell tumor -> dysgerminoma histology。"},
    48: {"stem": "卵巢濾泡期對應子宮內膜增生期；排卵後黃體期因黃體素作用，對應子宮內膜分泌期。因此把黃體期說成增生期是錯誤。", "options": [("A", "正確。濾泡期雌激素上升，促進子宮內膜增生。"), ("B", "錯誤。黃體期對應分泌期，不是增生期。"), ("C", "正確。黃體期由 progesterone 主導，使內膜進入 secretory phase。"), ("D", "正確。排卵後顆粒細胞黃體化，製造並分泌 progesterone。")], "core": "月經週期配對：follicular = proliferative；luteal = secretory。", "key": "卵巢黃體期對應子宮內膜分泌期，不是增生期。", "front": "Ovarian cycle vs endometrial cycle", "back": "Follicular-proliferative；luteal-secretory。", "summary": "Menstrual cycle -> follicular/proliferative; luteal/secretory。"},
    49: {"stem": "兩細胞兩性腺激素理論：LH 刺激 theca cells 製造 androgen，FSH 刺激 granulosa cells 的 aromatase 將 androgen 轉成 estrogen。", "options": [("A", "正確。主要性類固醇皆由 cholesterol 合成。"), ("B", "錯誤。Theca cells 製造 androgen 主要受 LH 刺激，不是 FSH。"), ("C", "正確。Granulosa cells 在 FSH 刺激下表現 aromatase，把 androgen 轉為 estrogen。"), ("D", "正確。Progesterone 為 C21、androgen 為 C19、estrogen 為 C18 steroid。")], "core": "Two-cell two-gonadotropin：LH-theca-androgen；FSH-granulosa-aromatase-estrogen。", "key": "Theca cell 製造 androgen 受 LH 刺激，不是 FSH。", "front": "Steroidogenesis two-cell theory", "back": "LH 刺激 theca 做 androgen；FSH 刺激 granulosa aromatase 做 estrogen。", "summary": "Steroidogenesis -> B wrong: theca androgen is LH-driven。"},
    50: {"stem": "hCG 是 glycoprotein/peptide hormone，作用於細胞膜上的 LH/hCG receptor，屬 G protein-coupled receptor；不是細胞核受體。", "options": [("A", "正確。多數 steroid hormones 可穿過細胞膜，受體位於細胞質或細胞核並調控基因表現。"), ("B", "正確。Peptide hormones 通常不能穿過脂質膜，受體在細胞膜。"), ("C", "錯誤。hCG 受體在細胞膜上，不在細胞核中。"), ("D", "正確。Thyroid hormone 進入細胞後作用於核內受體，調控基因轉錄。")], "core": "Peptide/glycoprotein hormone 用細胞膜受體；steroid 與 thyroid hormone 多用細胞內或核內受體。", "key": "hCG receptor 位於細胞膜，不在細胞核。", "front": "Hormone receptor location: hCG", "back": "hCG 是 glycoprotein hormone，受體在細胞膜 LH/hCG receptor。", "summary": "Hormone receptors -> hCG membrane receptor; thyroid/steroid nuclear/intracellular。"},
    51: {"stem": "GnRH 由下視丘脈衝式分泌，刺激腦下垂體分泌 LH 與 FSH；因此說 GnRH 只能刺激 LH、不能刺激 FSH 是錯誤。", "options": [("A", "錯誤。GnRH 可刺激 anterior pituitary 分泌 LH 與 FSH，脈衝頻率會影響相對分泌比例。"), ("B", "正確。GnRH 需 pulsatile secretion 才能維持 gonadotropin 分泌；持續給藥反而抑制軸線。"), ("C", "正確。GnRH 是十胜肽，也就是含 10 個胺基酸的 peptide。"), ("D", "正確。GnRH 半衰期短，約數分鐘。")], "core": "GnRH 是 pulsatile decapeptide，刺激 LH 與 FSH；連續刺激會 downregulation。", "key": "GnRH 可刺激 LH 與 FSH，不是只刺激 LH。", "front": "GnRH function", "back": "GnRH 是短半衰期十胜肽，脈衝式刺激 LH 和 FSH。", "summary": "GnRH -> pulsatile -> LH + FSH。"},
    52: {"stem": "不孕症常見原因包括排卵障礙、輸卵管因素與男性因素。子宮肌瘤雖可影響生育，尤其是黏膜下或扭曲腔室者，但整體相對不是最常見主因。", "options": [("A", "錯誤。排卵障礙是常見女性不孕原因。"), ("B", "錯誤。輸卵管阻塞是常見原因，常與骨盆感染或手術相關。"), ("C", "正確。子宮肌瘤相對較少直接造成不孕，需看位置是否影響子宮腔。"), ("D", "錯誤。男性因素約占相當比例，是不孕評估必須同步檢查的常見原因。")], "core": "不孕症評估不要只看女性；排卵、輸卵管與男性因素常見，肌瘤是否影響生育取決於位置。", "key": "相較排卵障礙、輸卵管阻塞與男性因素，子宮肌瘤造成不孕比例較少。", "front": "Common infertility causes", "back": "常見：排卵障礙、輸卵管因素、男性因素；肌瘤相對較少且看位置。", "summary": "Infertility -> fibroid less common cause than ovulatory/tubal/male factors。"},
    53: {"stem": "此 22 歲女性肥胖、月經稀發、AFC 20，符合 PCOS 方向；目前未有生育考量，重點是減重、代謝篩檢與用黃體素或荷爾蒙保護內膜，不適合給排卵藥。", "options": [("A", "正確。排卵藥用於有懷孕需求的排卵誘導；此人目前沒有生育需求，給排卵藥最不合適。"), ("B", "錯誤。長期無排卵會造成內膜持續受雌激素刺激，可用黃體素使內膜週期性剝落。"), ("C", "錯誤。減重與生活型態調整是 PCOS 與肥胖治療核心。"), ("D", "錯誤。PCOS 常伴胰島素阻抗與糖尿病風險，應篩檢代謝問題。")], "core": "PCOS 沒有生育需求時，不以排卵藥為優先；要保護子宮內膜並處理體重與代謝風險。", "key": "PCOS 無生育需求者不適合給排卵藥作為建議。", "front": "PCOS without fertility desire management", "back": "減重、代謝篩檢、黃體素/荷爾蒙保護內膜；不需排卵藥。", "summary": "PCOS -> no fertility desire -> avoid ovulation induction。"},
    54: {"stem": "濾泡期抑制 FSH 的 hormone X 可為 estradiol 的負回饋；持續高濃度 hormone Y 誘發 LH surge 也是 estradiol 的正回饋。因此 X 即 Y。Hormone Z 促使 primary oocyte 完成第一次減數分裂是 LH surge。", "options": [("A", "正確。X 與 Y 都可指 estradiol：低至中等濃度負回饋抑制 FSH，持續高濃度則正回饋誘發 LH surge。"), ("B", "錯誤。Y 是 estradiol，Z 是 LH，兩者不同。"), ("C", "錯誤。X 是 estradiol，Z 是 LH。"), ("D", "錯誤。濾泡期抑制 FSH 較重要的是 estradiol 與 inhibin B；inhibin A 主要與黃體期較相關。")], "core": "Estradiol 依濃度與時間可負回饋或正回饋；LH surge 促成卵母細胞成熟。", "key": "Hormone X 與 Y 都是 estradiol；Z 是 LH。", "front": "Follicular hormones: estradiol feedback and LH surge", "back": "Estradiol 可抑制 FSH，也可在持續高濃度誘發 LH surge；LH 促進 oocyte maturation。", "summary": "Follicular cycle -> estradiol negative/positive feedback; LH triggers maturation。"},
    55: {"stem": "人工授精 IUI 是將處理後精液置入子宮腔，不需要取卵；IVF、ICSI 與 PGD 都需要先取得卵子或胚胎。", "options": [("A", "正確。IUI 不需取卵，適用部分輕度男性因素、不明原因不孕或排卵誘導搭配。"), ("B", "錯誤。IVF 需要取卵後在體外受精。"), ("C", "錯誤。ICSI 是把單一精子注入卵細胞質，必須先取卵。"), ("D", "錯誤。PGD 需有胚胎可供切片檢測，通常建立在 IVF 流程上。")], "core": "輔助生殖中 IUI 不需取卵；IVF/ICSI/PGD 都涉及取卵與胚胎實驗室操作。", "key": "不需取卵的人工輔助生殖技術是 intrauterine insemination。", "front": "ART that does not require oocyte retrieval", "back": "IUI 不需取卵；IVF、ICSI、PGD 需要。", "summary": "ART -> IUI no oocyte retrieval。"},
    56: {"stem": "官方圖像答案為臍動脈血流速度波形。胎兒 Doppler 中臍動脈波形用於評估胎盤阻力，常看收縮期與舒張末期血流。", "options": [("A", "正確。臍動脈 Doppler 呈動脈性脈衝波形，可評估 placental resistance。"), ("B", "錯誤。臍靜脈通常較連續、非動脈性脈衝波形。"), ("C", "錯誤。中大腦動脈波形用於評估 brain-sparing 或胎兒貧血等，位置與波形判讀不同。"), ("D", "錯誤。下行主動脈不是本題官方圖示所指血管。")], "core": "胎兒 Doppler 要分血管：臍動脈看胎盤阻力與舒張末期血流；MCA 看腦循環與貧血。", "key": "本題圖示為臍動脈血流速度波形。", "front": "Fetal Doppler: umbilical artery waveform", "back": "臍動脈 Doppler 用於評估胎盤阻力，重點看 end-diastolic flow。", "summary": "Fetal Doppler -> umbilical artery waveform。", "notes": ["圖像題：未直接檢視原圖，依官方答案撰寫。"]},
    57: {"stem": "承上題，官方圖像判讀為 reversed end-diastolic velocity，表示臍動脈舒張末期血流反向，是胎盤阻力嚴重升高的警訊。", "options": [("A", "錯誤。Absence of end-diastolic velocity 是舒張末期血流消失；本題官方答案為反向而非消失。"), ("B", "正確。Reversed end-diastolic velocity 代表舒張末期血流逆轉，較 absent 更嚴重。"), ("C", "錯誤。Positive 不是臍動脈 Doppler 此處的標準具體判讀。"), ("D", "錯誤。Negative 也不是本題所問波形結果的恰當描述。")], "core": "臍動脈 Doppler 嚴重異常順序：舒張末期血流降低、消失、反向；反向代表高風險。", "key": "臍動脈 reversed end-diastolic velocity 是嚴重胎盤阻力升高表現。", "front": "Umbilical artery Doppler reversed end-diastolic flow", "back": "舒張末期血流反向，比 absent end-diastolic flow 更嚴重。", "summary": "Umbilical artery Doppler -> reversed EDF indicates severe placental resistance。", "notes": ["圖像題：未直接檢視原圖，依官方答案撰寫。"]},
    58: {"stem": "中風後 CRPS type 1 常影響肩、手腕、手指，形成 shoulder-hand syndrome；肘部相對較少是主要受影響部位。", "options": [("A", "錯誤。肩膀常受影響，肩痛與活動受限常見。"), ("B", "正確。肘部相對較少是 post-stroke CRPS type 1 的主要受累部位。"), ("C", "錯誤。手腕常有疼痛、腫脹與活動受限。"), ("D", "錯誤。手指常見水腫、疼痛與僵硬。")], "core": "Post-stroke CRPS type 1 又稱 shoulder-hand syndrome，重點在肩與遠端手部，肘較少。", "key": "中風後 CRPS type 1 相對較少影響肘部。", "front": "Post-stroke CRPS type 1 affected parts", "back": "常影響肩、手腕、手指；肘部相對少。", "summary": "Post-stroke CRPS -> shoulder-hand syndrome, elbow less involved。"},
    59: {"stem": "Autonomic dysreflexia 多發生於 T6 以上脊髓損傷，通常在 spinal shock 結束後較常見，最常見誘因是膀胱脹尿；不是受傷後一個月內最常發生。", "options": [("A", "錯誤。自主神經反射異常通常在損傷後數週至數月、spinal shock 期後較常見，不是最常在一個月內。"), ("B", "正確。T6 以上完全脊髓損傷失去上位調控，最容易發生嚴重高血壓反射。"), ("C", "正確。膀胱膨脹、導尿管阻塞是最常見誘因。"), ("D", "正確。初步處置包括讓病人坐起、鬆開束縛並立即尋找及移除刺激來源。")], "core": "Autonomic dysreflexia：T6 以上、劇烈高血壓、膀胱脹尿常見；處置先坐起並移除刺激。", "key": "Autonomic dysreflexia 不常在脊髓損傷後一個月內發生，常在 spinal shock 後。", "front": "Autonomic dysreflexia timing and trigger", "back": "T6 以上 SCI；膀胱脹尿最常見；先坐起並移除刺激。", "summary": "SCI autonomic dysreflexia -> T6 above + bladder distension + remove stimulus。"},
    60: {"stem": "Reflexogenic erection 由外陰部觸覺刺激引發，反射中樞位於 S2-4，主要經副交感骨盆神經控制。", "options": [("A", "錯誤。T11-12 下腹神經屬交感路徑，較與 psychogenic erection 或射精相關。"), ("B", "正確。S2-4 副交感 pelvic nerve 介導反射性勃起。"), ("C", "錯誤。S2-4 pelvic nerve 是副交感，不是交感。"), ("D", "錯誤。T11-12 hypogastric nerve 是交感，不是副交感 S2-4 路徑。")], "core": "勃起神經控制：reflexogenic erection = S2-4 parasympathetic pelvic nerve；psychogenic 多涉 T11-L2 sympathetic。", "key": "男性反射性勃起由 S2-4 副交感骨盆神經控制。", "front": "Reflexogenic erection nerve pathway", "back": "S2-4 parasympathetic pelvic nerve。", "summary": "Erection physiology -> reflexogenic = S2-4 parasympathetic。"},
})


DATA.update({
    61: {"stem": "鷹爪手典型來自尺神經病變，因第四、五指蚓狀肌與骨間肌無力，造成 MCP 過伸、IP 屈曲，尤其在慢性病變後明顯。", "options": [("A", "正確。尺神經支配多數手內在肌，損傷會造成 claw hand、骨間肌萎縮與夾紙試驗異常。"), ("B", "錯誤。橈神經病變典型是 wrist drop，不是鷹爪手。"), ("C", "錯誤。正中神經病變可造成猿手、魚際萎縮或前三指感覺異常，不是典型鷹爪手。"), ("D", "錯誤。肌皮神經支配肱二頭肌等，病變影響肘屈曲與前臂外側感覺，不造成鷹爪手。")], "core": "神經病變手形：尺神經 claw hand、橈神經 wrist drop、正中神經 ape hand。", "key": "鷹爪手最典型是尺神經病變。", "front": "Claw hand nerve lesion", "back": "Ulnar nerve lesion；第四、五指 clawing 與手內在肌無力。", "summary": "Peripheral nerve hand signs -> claw hand = ulnar nerve。"},
    62: {"stem": "下背痛 red flags 包括夜間痛、持續惡化、不明體重減輕、癌症史、發燒、重大外傷、神經缺損等；夜間疼痛且愈來愈嚴重須警覺腫瘤或感染。", "options": [("A", "正確。夜間痛且逐漸惡化是 red flag，需進一步檢查。"), ("B", "錯誤。BMI 高是機械性下背痛風險因素，但本身不是嚴重病變 red flag。"), ("C", "錯誤。合併下肢疼痛可見於坐骨神經痛，需評估但不一定代表嚴重病變。"), ("D", "錯誤。曾有腰椎手術史會影響鑑別，但不如夜間惡化痛典型代表惡性或感染警訊。")], "core": "下背痛 red flag 指向癌症、感染、骨折或嚴重神經壓迫；夜間惡化痛是重要警訊。", "key": "夜間疼痛且愈來愈嚴重是下背痛 red flag。", "front": "Low back pain red flag", "back": "夜間痛、持續惡化、癌症史、發燒、體重減輕、嚴重神經缺損需轉介檢查。", "summary": "Low back pain -> worsening night pain is red flag。"},
    63: {"stem": "Osgood-Schlatter disease 是青少年脛骨粗隆牽引性骨軟骨炎，X 光可見 tibial tubercle fragmentation，通常保守治療。", "options": [("A", "正確。病變在脛骨粗隆，可見骨頭碎裂或不規則。"), ("B", "錯誤。病灶位於髕骨肌腱附著的 tibial tubercle，不是髕骨與髕骨肌腱交接處。"), ("C", "錯誤。可使用休息、冰敷、伸展與 NSAIDs 緩解症狀，並非不可使用。"), ("D", "錯誤。多數會隨骨骼成熟改善，通常不需手術。")], "core": "Osgood-Schlatter = tibial tubercle traction apophysitis，青少年運動疼痛，保守治療。", "key": "Osgood-Schlatter 可見 tibial tubercle fragmentation。", "front": "Osgood-Schlatter disease location and treatment", "back": "Tibial tubercle 牽引性骨軟骨炎；可 fragmentation；多保守治療。", "summary": "Osgood-Schlatter -> tibial tubercle fragmentation, conservative care。"},
    64: {"stem": "類風濕性關節炎主要侵犯滑膜關節，常見手腕、MCP、PIP、足部，也可肩、踝；腰椎不是典型好發部位，脊椎受累較重要是頸椎。", "options": [("A", "錯誤。腕關節是 RA 常見受累部位。"), ("B", "錯誤。肩關節可受 RA 侵犯。"), ("C", "正確。腰椎關節不是 RA 好發部位；若脊椎受累較常考頸椎寰樞關節不穩。"), ("D", "錯誤。踝關節可受 RA 侵犯。")], "core": "RA 好發周邊滑膜關節，脊椎例外重點是頸椎，不是腰椎。", "key": "RA 不好發腰椎關節。", "front": "Rheumatoid arthritis common joints", "back": "常見腕、MCP/PIP、肩、踝；脊椎重點是頸椎，非腰椎。", "summary": "RA -> peripheral synovial joints, cervical spine; lumbar spine uncommon。"},
    65: {"stem": "心臟復健絕對禁忌包括急性心肌炎、急性心包膜炎、不穩定心絞痛、失代償心衰竭、嚴重未控制心律不整等；CABG 後與移植後反而常是復健適應症。", "options": [("A", "錯誤。急性心肌梗塞穩定後是心臟復健重要適應症；急性未穩定期才需暫緩。"), ("B", "錯誤。冠狀動脈繞道手術後通常需要心臟復健。"), ("C", "正確。急性心包膜炎或心肌炎運動可能惡化發炎與心律風險，屬絕對禁忌。"), ("D", "錯誤。心臟或心肺移植後常需復健以恢復功能，非絕對禁忌。")], "core": "心臟復健禁忌是急性未穩定或發炎狀態；術後穩定病人多是復健對象。", "key": "急性心包膜炎或心肌炎是心臟復健絕對禁忌。", "front": "Absolute contraindication to cardiac rehabilitation", "back": "急性心包膜炎/心肌炎；CABG 或移植後穩定者通常是復健適應症。", "summary": "Cardiac rehab -> acute myocarditis/pericarditis contraindication。"},
    66: {"stem": "Rate-pressure product = heart rate x systolic blood pressure，與 myocardial oxygen consumption 最具相關性，常用於運動測試與心臟復健強度評估。", "options": [("A", "錯誤。平均血壓可反映灌流壓，但心肌耗氧量常用 HR x SBP 估算。"), ("B", "正確。心跳數乘以收縮壓是 rate-pressure product，和心肌耗氧量高度相關。"), ("C", "錯誤。舒張壓較與冠狀動脈灌流相關，不是 RPP 的標準組成。"), ("D", "錯誤。收縮壓乘舒張壓沒有 RPP 的臨床意義。")], "core": "心肌耗氧量估算看 double product/rate-pressure product：HR x SBP。", "key": "Myocardial oxygen consumption 與 HR x SBP 最相關。", "front": "Rate-pressure product formula", "back": "Heart rate x systolic blood pressure。", "summary": "MVO2 estimate -> HR x SBP。"},
    67: {"stem": "孕前與懷孕早期補充葉酸可降低胎兒神經管缺損風險；葉酸屬維生素 B9。", "options": [("A", "錯誤。Thiamine 是 B1，與神經管缺損預防不是主要配對。"), ("B", "錯誤。Pyridoxine 是 B6，常與孕吐或代謝相關，不是 NTD 預防主角。"), ("C", "正確。Folic acid 是 B9，已證實可降低 neural tube defects。"), ("D", "錯誤。Cobalamin 是 B12，缺乏可造成貧血與神經症狀，但 NTD 預防主角是 B9。")], "core": "預防 NTD：懷孕前後補充 folic acid (B9)。", "key": "孕婦補充 folic acid 可降低神經管缺損。", "front": "Vitamin preventing neural tube defects", "back": "Vitamin B9, folic acid。", "summary": "Pregnancy supplement -> folic acid prevents NTD。"},
    68: {"stem": "神經管缺損最常發生在腰薦椎區，臨床常見 myelomeningocele 也多位於 lumbosacral region。", "options": [("A", "錯誤。頸椎可發生但不是最常見。"), ("B", "錯誤。胸椎不是最常見位置。"), ("C", "錯誤。胸腰椎可見，但較典型最常見為腰薦椎。"), ("D", "正確。腰薦椎是兒童 neural tube defect 最常受影響部位。")], "core": "Neural tube defect 最常見部位是 lumbosacral spine。", "key": "神經管缺損最常影響腰薦椎。", "front": "Most common NTD spinal level", "back": "Lumbar-sacral level。", "summary": "Neural tube defect -> lumbosacral most common。"},
    69: {"stem": "全舌切除後主要問題是口腔期食團後送不足。Chin-up posture 可利用重力協助食物由口腔往咽部移動。", "options": [("A", "錯誤。Mendelsohn maneuver 主要延長喉部上提與上食道括約肌開啟，適用咽期問題。"), ("B", "錯誤。Shaker exercise 強化 suprahyoid muscles，改善 UES 開啟，不是立即補償舌頭後送不足。"), ("C", "正確。抬下巴可利用重力協助口中食物後送，適合舌切除後口腔傳送不足。"), ("D", "錯誤。Masako exercise 針對舌根與咽壁接觸訓練，不是全舌切除後進食當下最恰當補償。")], "core": "吞嚥姿勢要配問題：舌推送不足用 chin-up；咽期殘留或 UES 問題才考其他手法。", "key": "全舌切除後食團後送不足可用 chin-up posture。", "front": "Post-glossectomy swallowing compensation", "back": "Chin-up 利用重力協助食團由口腔後送。", "summary": "Total glossectomy dysphagia -> chin-up for oral propulsion。"},
    70: {"stem": "圖中物理治療後病變官方答案為熱敷包造成，最可能是局部熱傷害或燙傷。Hot pack 若溫度過高、包覆不足或感覺障礙者使用過久，容易造成皮膚灼傷。", "options": [("A", "錯誤。短波治療也可能造成深部熱傷害，但本題圖像與官方答案指向熱敷包。"), ("B", "正確。熱敷包直接傳導熱，使用不當可造成局部燙傷，常見於感覺差或循環差病人。"), ("C", "錯誤。干擾波主要是電刺激治療，不是此圖最可能熱傷害來源。"), ("D", "錯誤。低能量雷射一般不會造成典型熱敷包樣燙傷。")], "core": "物理治療熱療安全要注意溫度、時間、墊布與感覺功能；hot pack 可造成接觸性燙傷。", "key": "物理治療後局部燙傷最可能來自 hot packs。", "front": "PT modality causing burn lesion",
        "back": "Hot packs 使用不當可造成接觸性熱傷害。", "summary": "Physical therapy burn -> hot pack。", "notes": ["圖像題：未直接檢視原圖，依官方答案撰寫。"]},
    71: {"stem": "Spastic dysarthria 是上運動神經元系統，特別是雙側 corticobulbar tract 受損造成，表現為聲音緊繃、費力、速度慢與痙攣性音質。", "options": [("A", "錯誤。單側上運動神經元病灶較常造成 unilateral UMN dysarthria，通常較輕。"), ("B", "錯誤。單側下運動神經元病灶較會造成 flaccid 成分或局部肌肉無力。"), ("C", "正確。雙側上運動神經元受損最容易造成 spastic dysarthria。"), ("D", "錯誤。雙側下運動神經元受損較造成 flaccid dysarthria。")], "core": "構音障礙定位：spastic = bilateral UMN；flaccid = LMN；ataxic = cerebellar。", "key": "Spastic dysarthria 最典型來自雙側上運動神經元受損。", "front": "Spastic dysarthria lesion", "back": "Bilateral upper motor neuron / corticobulbar tract lesion。", "summary": "Dysarthria localization -> spastic = bilateral UMN。"},
    72: {"stem": "急性鼻竇炎若合併意識不清，要擔心眼眶或顱內併發症，必須以 CT 等進一步影像評估；Water's view X 光不足以判斷影響範圍。", "options": [("A", "正確。CT 比 plain film 清楚，但輻射劑量較高。"), ("B", "正確。慢性鼻竇炎對數週抗生素無效時，CT 可評估解剖與手術需求。"), ("C", "錯誤。急性鼻竇炎合併意識不清是嚴重警訊，Water's view 不足，需 CT 評估顱內或眼眶併發症。"), ("D", "正確。增強 CT 有助於評估腫瘤、膿瘍或併發症。")], "core": "鼻竇炎出現意識改變、眼眶症狀或神經症狀時，要用 CT/MRI 評估併發症，不能只靠 X 光。", "key": "急性鼻竇炎合併意識不清不能只用 Water's view，需 CT 評估。", "front": "Sinusitis imaging red flag", "back": "意識不清或疑併發症需 CT，不可只靠 X 光 Water's view。", "summary": "Sinusitis imaging -> neurologic symptoms require CT。"},
    73: {"stem": "肩痛 X 光若見旋轉肌袖附著處鈣化，最可能是 calcific tendinosis。官方答案為 calcified tendinosis，常見於 supraspinatus tendon。", "options": [("A", "正確。Calcific tendinosis 可在肩袖肌腱看到鈣化沉積，造成急性或慢性肩痛。"), ("B", "錯誤。Greater tuberosity avulsion fracture 會有骨皮質中斷或撕脫骨片，與單純肌腱鈣化不同。"), ("C", "錯誤。骨轉移通常呈破壞性或硬化性骨病灶，臨床與影像分布不同。"), ("D", "錯誤。原發性 osteoblastic bone tumor 不符合跌倒後肩痛與典型肩袖鈣化表現。")], "core": "肩部 X 光看到肩袖區鈣化，要想到 calcific tendinitis/tendinosis，而非骨腫瘤或撕脫骨折。", "key": "肩袖鈣化造成肩痛最可能是 calcific tendinosis。", "front": "Shoulder X-ray calcification diagnosis", "back": "Calcific tendinosis, often supraspinatus tendon calcification。", "summary": "Shoulder pain X-ray -> calcific tendinosis。", "notes": ["圖像題：未直接檢視原圖，依官方答案撰寫。"]},
    74: {"stem": "80 歲女性下腹部 T2WI 圖像官方答案為子宮內膜癌。高齡女性若影像顯示子宮腔或內膜區病灶，需優先考慮 endometrial carcinoma。", "options": [("A", "錯誤。子宮頸癌病灶位於 cervix，影像位置與官方箭號不符。"), ("B", "錯誤。卵巢癌源於附件區卵巢腫塊，不是箭號所示子宮內膜病灶。"), ("C", "錯誤。陰道癌位於陰道壁，與子宮腔內膜病灶不同。"), ("D", "正確。停經後高齡女性子宮內膜區腫瘤最符合子宮內膜癌。")], "core": "停經後女性子宮腔內膜病灶或異常出血，要高度懷疑 endometrial cancer。", "key": "本題 MRI 箭號所指最符合子宮內膜癌。", "front": "Pelvic MRI elderly woman endometrial lesion", "back": "高齡女性子宮內膜區病灶最符合 endometrial cancer。", "summary": "Pelvic MRI -> endometrial lesion in elderly woman = endometrial cancer。", "notes": ["圖像題：未直接檢視原圖，依官方答案撰寫。"]},
    75: {"stem": "兒童 VF defibrillation 傳統考點為第一次 2 J/kg，第二次與後續可 4 J/kg；題目選項中第三次 4 J/kg 符合官方答案。", "options": [("A", "錯誤。起初 defibrillation 傳統建議為 2 J/kg，不是 4 J/kg。"), ("B", "錯誤。再次 shock 不以 6 J/kg 作為此題標準答案。"), ("C", "錯誤。再次 shock 不以 8 J/kg 作為此題標準答案。"), ("D", "正確。依本題採用的 PALS 傳統劑量邏輯，第三次 defibrillation 可為 4 J/kg。")], "core": "兒童 VF shock 劑量常考 2 J/kg 起始、後續 4 J/kg；新版流程可允許後續升高，但本題依官方答案採 4 J/kg。",
        "key": "兒童 VF defibrillation 傳統劑量：初次 2 J/kg，後續 4 J/kg。",
        "front": "Pediatric VF defibrillation dose",
        "back": "傳統考點：first 2 J/kg, subsequent 4 J/kg；本題第三次選 4 J/kg。",
        "summary": "Pediatric VF -> defibrillation 2 then 4 J/kg in traditional exam logic。",
        "notes": ["PALS 劑量曾有版本差異；本說明保留官方答案，建議若作臨床使用需依最新 PALS 指引。"]},
    76: {"stem": "年輕成人急性視力下降合併眼球疼痛，尤其眼球轉動痛，最典型是 optic neuritis。其他血管阻塞通常以無痛視力喪失為主。", "options": [("A", "正確。視神經炎常見於年輕成人，急性單眼視力下降、色覺下降與眼球轉動痛。"), ("B", "錯誤。中央視網膜動脈阻塞通常是突發無痛性嚴重視力喪失。"), ("C", "錯誤。中央視網膜靜脈阻塞多為無痛視力下降，常見於高血壓、糖尿病或青光眼風險者。"), ("D", "錯誤。顳動脈炎多見於 50 歲以上，伴頭痛、顳部壓痛、咀嚼跛行，不符合 30 歲男性最典型診斷。")], "core": "Painful acute visual loss in young adult 要想到 optic neuritis；血管阻塞多無痛。", "key": "急性視力下降合併眼痛最可能是視神經炎。", "front": "Painful acute visual loss young adult", "back": "Optic neuritis；常有眼球轉動痛與色覺下降。", "summary": "Acute visual loss + pain -> optic neuritis。"},
    77: {"stem": "Preeclampsia 典型徵候包括妊娠高血壓、蛋白尿，過去也常提水腫；血糖上升不是典型臨床徵候，較屬妊娠糖尿病考點。", "options": [("A", "錯誤。妊娠高血壓是子癲前症核心表現。"), ("B", "錯誤。蛋白尿是傳統診斷重點之一。"), ("C", "正確。血糖上升不是 preeclampsia 典型臨床徵候。"), ("D", "錯誤。下肢水腫過去常列為相關表現，雖現代診斷不以水腫為必要條件，但仍比血糖上升更符合典型表現。")], "core": "Preeclampsia 看高血壓、蛋白尿與器官受損；血糖上升屬妊娠糖尿病，不是典型徵候。", "key": "子癲前症典型徵候不包含血糖上升。", "front": "Preeclampsia typical signs",
        "back": "妊娠高血壓、蛋白尿、器官受損；血糖上升不是典型表現。", "summary": "Preeclampsia -> hypertension/proteinuria, not hyperglycemia。"},
    78: {"stem": "兒童、孕婦、囚犯、精神病患等在研究倫理中屬 vulnerable populations，需要更嚴格保護，以避免自主性不足、權力不對等或額外傷害風險造成剝削。", "options": [("A", "錯誤。人數有限不是主要倫理理由。"), ("B", "錯誤。代理同意確實需把關，但它只是保護 vulnerable subjects 的一部分，不是總原則本身。"), ("C", "正確。嚴格規範的主要目的在保護易受傷害受試族群。"), ("D", "錯誤。這些族群不一定所有研究風險都過高；重點是脆弱性與自主/權力不對等。")], "core": "研究倫理對 vulnerable subjects 加強保護，核心是尊重自主、避免剝削與公平承擔研究風險利益。", "key": "兒童、孕婦、囚犯、精神病患研究規範較嚴格，是為保護易受傷害族群。", "front": "Research ethics vulnerable populations", "back": "嚴格規範基於保護 vulnerable subjects，避免剝削與同意不充分。", "summary": "Research ethics -> protect vulnerable populations。"},
    79: {"stem": "病人只是意識不清、急性心衰與 CO2 堆積，不能直接由家屬簽安寧緩和醫療同意書視為末期病人。急性可逆狀況下，醫師應以病人最大利益與緊急救治為優先。", "options": [("A", "錯誤。題幹未證明病人為末期病人；家屬不能因此直接合法替代簽署安寧同意。"), ("B", "正確。急性危急且病人意識不清時，醫師應以病人最大利益為先，先給予必要急救與穩定處置。"), ("C", "錯誤。家屬意願重要，但不能取代病人最大利益與法律要件，尤其在可逆急症中。"), ("D", "錯誤。倫理委員會可協助爭議，但急救情境不能等待其決議才處理。")], "core": "急救倫理先看病人最大利益與可逆性；安寧緩和醫療需符合法定條件，不能把急性意識不清直接當末期。", "key": "急性可逆危急狀況且病人意識不清時，醫師應以病人最大利益先急救。",
        "front": "Emergency ethics: unconscious patient family requests hospice", "back": "未證明末期且急性可逆時，先依病人最大利益急救；家屬不能直接替代所有決策。", "summary": "Medical ethics -> acute emergency -> patient's best interest and urgent care first。"},
    80: {"stem": "精神疾病診斷不等於喪失同意能力。若精神科評估病人能理解手術內容、風險、替代方案並能表達選擇，就具有簽署同意書能力，應由本人簽署。", "options": [("A", "錯誤。不能因思覺失調症診斷就認定無能力，更不會由朋友代簽。"), ("B", "錯誤。家屬代簽只在病人無同意能力且符合法定代理條件時考慮；本題病人可理解。"), ("C", "錯誤。精神科醫師可評估能力，但不是代簽同意書的人。"), ("D", "正確。病人具有決策能力時，應尊重自主，由病人自己簽署同意書。")], "core": "醫療同意能力是功能性判斷，不是診斷標籤；能理解、評估、表達選擇者可自行同意。", "key": "思覺失調症患者若具決策能力，手術同意書由本人簽署。", "front": "Informed consent capacity in schizophrenia", "back": "診斷不等於無能力；若能理解並表達選擇，病人自己簽。", "summary": "Consent capacity -> functional assessment; schizophrenia alone does not remove autonomy。"},
})


def main():
    exam = load_source()
    questions = {q["question_number"]: q for q in exam["questions"]}
    missing = sorted(set(questions) - set(DATA))
    extra = sorted(set(DATA) - set(questions))
    if missing or extra:
        raise SystemExit(f"question coverage mismatch missing={missing} extra={extra}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for start in range(1, 81, 10):
        end = start + 9
        updates = []
        for num in range(start, end + 1):
            item = DATA[num]
            updates.append(
                make_update(
                    questions[num],
                    item["stem"],
                    item["options"],
                    item["core"],
                    item["key"],
                    item["front"],
                    item["back"],
                    item["summary"],
                    item.get("notes"),
                )
            )
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates,
        }
        out = OUT_DIR / f"q{start:03d}-q{end:03d}.json"
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(out)


DATA.update({
    31: {"stem": "噴乳反射是嬰兒吸吮刺激造成後葉腦下垂體釋放 oxytocin，使乳腺周圍 myoepithelial cells 收縮，把乳汁推出乳管。", "options": [("A", "錯誤。Prolactin 主要促進乳汁製造，不是立即噴乳反射的收縮激素。"), ("B", "正確。Oxytocin 使乳腺肌上皮細胞收縮，造成 milk ejection 或 let-down reflex。"), ("C", "錯誤。Prostaglandin 與子宮收縮、發炎等相關，不是噴乳反射主因。"), ("D", "錯誤。Dopamine 會抑制 prolactin 分泌，不會引起噴乳反射。")], "core": "泌乳兩激素：prolactin 產奶，oxytocin 噴奶。", "key": "Milk ejection reflex 由 oxytocin 引起。", "front": "Milk production vs milk ejection", "back": "Prolactin 產奶；oxytocin 使肌上皮細胞收縮而噴乳。", "summary": "Lactation -> prolactin production, oxytocin ejection。"},
    32: {"stem": "NST 判讀看胎心率是否隨胎動出現足夠 acceleration。官方答案為 nonreactive，表示圖中胎動後未出現符合週數標準的足夠加速。", "options": [("A", "錯誤。Early deceleration 是子宮收縮時胎心率下降且與收縮同步，常與頭部受壓相關，不是 NST 胎動反應判讀。"), ("B", "錯誤。Late deceleration 是收縮後延遲下降，提示 uteroplacental insufficiency，題幹提示 FM 胎動，重點是 reactive/nonreactive。"), ("C", "錯誤。Reactive NST 需在一定時間內有足夠 fetal movement-associated acceleration；圖中未達標準。"), ("D", "正確。Nonreactive 表示未觀察到足夠胎心加速，需延長監測或進一步評估。")], "core": "NST 的重點是胎動後胎心加速；未達 acceleration 標準即 nonreactive。", "key": "NST 若胎動後無足夠 fetal heart rate acceleration，判讀為 nonreactive。", "front": "NST reactive vs nonreactive", "back": "Reactive 要有符合標準的胎心加速；沒有足夠 acceleration 是 nonreactive。", "summary": "NST -> fetal movement + acceleration; absent = nonreactive。", "notes": ["圖像題：說明依官方答案與 NST 判讀原則撰寫，建議人工確認圖中胎心加速幅度。"]},
    33: {"stem": "Biophysical profile 的 fetal breathing movement 項目：30 分鐘內至少一次持續 30 秒以上的胎兒呼吸運動即可得 2 分；本題有五次且每次 30 秒以上。", "options": [("A", "錯誤。0 分是未達一次 30 秒以上胎兒呼吸運動。"), ("B", "錯誤。BPP 各項通常以 0 或 2 分計，不給 1 分。"), ("C", "正確。30 分鐘內至少一次持續 30 秒以上即可得 2 分，本題明顯符合。"), ("D", "錯誤。BPP 單項最高為 2 分，不是 3 分。")], "core": "BPP 單項多為 0 或 2 分；胎兒呼吸在 30 分鐘內有一次持續 30 秒以上即 2 分。", "key": "BPP fetal breathing：30 分鐘內至少一次 >=30 秒，得 2 分。", "front": "BPP fetal breathing score", "back": "30 分鐘內至少一次持續 30 秒以上胎兒呼吸運動 = 2 分。", "summary": "BPP breathing -> >=1 episode lasting >=30 sec = 2 points。"},
    34: {"stem": "女性尿失禁最常見類型通常是 stress urinary incontinence，因腹壓增加時尿道支持不足或括約肌功能不足而漏尿。", "options": [("A", "錯誤。Urge incontinence 與逼尿肌過動相關，常見但不是女性整體最常見類型。"), ("B", "正確。Stress incontinence 是女性最常見尿失禁，咳嗽、打噴嚏、運動等腹壓增加時漏尿。"), ("C", "錯誤。Mixed incontinence 同時有 stress 與 urge 成分，但不是題目所問最常見單一類型。"), ("D", "錯誤。Overflow incontinence 多與尿滯留、神經病變或阻塞相關，在女性較少見。")], "core": "女性尿失禁最常見是 stress incontinence；關鍵字是腹壓增加時漏尿。", "key": "女性最常見 urinary incontinence 是 stress urinary incontinence。", "front": "Most common female urinary incontinence", "back": "Stress incontinence：咳嗽、打噴嚏、運動等腹壓增加時漏尿。", "summary": "Female UI -> most common stress incontinence。"},
    35: {"stem": "敗血症造成 alveolar-capillary membrane 通透性增加，引起非心因性肺水腫與嚴重低氧，典型稱為 acute respiratory distress syndrome (ARDS)。", "options": [("A", "錯誤。Pulmonary edema 是廣義肺水腫，未指出敗血症造成的瀰漫性肺泡微血管損傷症候群。"), ("B", "錯誤。Pulmonary hypertension 是肺血管壓力升高，不是本題描述的通透性肺損傷。"), ("C", "錯誤。Respiratory permeability defect 不是標準臨床診斷名稱。"), ("D", "正確。ARDS 可由敗血症、吸入、創傷等引起，核心是肺泡微血管屏障受損、通透性增加與低氧。")], "core": "敗血症後微血管通透性增加造成非心因性肺水腫，要想到 ARDS。", "key": "敗血症造成 alveolar-capillary membrane injury 與通透性增加是 ARDS。", "front": "Sepsis + alveolar-capillary permeability lung complication", "back": "Acute respiratory distress syndrome (ARDS)。", "summary": "Sepsis lung complication -> increased permeability -> ARDS。"},
    36: {"stem": "精液檢查發現無精蟲症時，需先確認結果，因檢體、禁慾時間或暫時性因素會影響判讀；因此最佳初步做法是說明原因並重複精液檢查或搭配抽血評估。", "options": [("A", "正確。無精蟲症應至少重複精液分析確認，並依情況做 FSH、LH、testosterone 等評估。"), ("B", "錯誤。睪丸切片可用於後續鑑別阻塞性或非阻塞性，但不是第一次發現後立即最佳做法。"), ("C", "錯誤。ICSI 是治療選項之一，需先釐清是否有可取得精子與病因。"), ("D", "錯誤。領養不是唯一選擇；阻塞性或部分非阻塞性無精蟲症仍可能透過取精與輔助生殖。")], "core": "男性不孕看到 azoospermia 要先重複確認與內分泌評估，再談侵入性檢查或治療。", "key": "無精蟲症初步應重複精液檢查並評估可能原因。", "front": "Initial management of azoospermia", "back": "先重複精液分析與抽血評估，不是直接睪丸切片或 ICSI。", "summary": "Azoospermia -> confirm with repeat semen analysis + hormonal workup。"},
    37: {"stem": "無月經不是 2 個月沒來即可定義。臨床常以原發性或次發性無月經定義，次發性常為原本規則月經停止至少 3 個月，或不規則月經停止至少 6 個月。", "options": [("A", "錯誤。2 個月未來不足以作為標準 amenorrhea 定義。"), ("B", "正確。評估無月經第一步必須先排除懷孕。"), ("C", "正確。解剖結構異常可造成無月經，但相對於懷孕、下視丘-腦下垂體-卵巢軸與內分泌原因比例較少。"), ("D", "正確。高泌乳血症會抑制 GnRH，造成排卵障礙與無月經。")], "core": "無月經評估第一步是驗孕；定義不是單純 2 個月沒來。", "key": "Amenorrhea 不定義為 2 個月月經沒來；需先排除懷孕。", "front": "Amenorrhea definition and first step",
        "back": "不是 2 個月沒來；評估第一步先驗孕，高泌乳血症可造成無月經。", "summary": "Amenorrhea -> rule out pregnancy first; 2 months is not standard definition。"},
    38: {"stem": "Clomiphene citrate 透過抗雌激素作用增加 GnRH/FSH/LH，前提是下視丘-腦下垂體仍能反應；若是 hypothalamic-pituitary failure，缺乏可被刺激的軸線，因此一定無效。", "options": [("A", "錯誤。Hypothalamic-pituitary dysfunction 若仍有部分功能，可能對排卵誘導有反應。"), ("B", "正確。Hypothalamic-pituitary failure 代表軸線衰竭，clomiphene 無法刺激足夠 gonadotropin 分泌。"), ("C", "錯誤。PCOS 是 clomiphene 常見適應症之一，可誘導排卵。"), ("D", "錯誤。子宮內膜異位症造成不孕機轉不同，但 clomiphene 並非「一定無效」；仍取決於是否需誘導排卵。")], "core": "Clomiphene 需要完整可反應的 HPO axis；軸線 failure 時無效。", "key": "Clomiphene 對 hypothalamic-pituitary failure 一定無效。", "front": "Clomiphene citrate ineffective condition", "back": "需要 HPO axis 能反應；hypothalamic-pituitary failure 無效。", "summary": "Clomiphene -> stimulates endogenous gonadotropins; pituitary failure no response。"},
    39: {"stem": "子宮頸癌侵犯下 1/3 陰道但無子宮旁組織侵犯、無腎盂輸尿管水腫，符合 FIGO IIIA。IIA 是上 2/3 陰道侵犯；IIB 是子宮旁侵犯；IIIB 才有骨盆壁或腎水腫。",
        "options": [("A", "錯誤。IB3 是侷限於子宮頸且腫瘤大於 4 cm，本題已侵犯下 1/3 陰道。"), ("B", "錯誤。IIA2 可侵犯上 2/3 陰道且腫瘤大於 4 cm，但不能到下 1/3 陰道。"), ("C", "錯誤。IIB 需要子宮旁組織侵犯；題幹說子宮旁組織柔軟無侵犯。"), ("D", "正確。侵犯下 1/3 陰道且未達骨盆壁、無腎水腫，為 FIGO IIIA。")],
        "core": "子宮頸癌分期：下 1/3 陰道侵犯是 IIIA；子宮旁侵犯是 IIB；腎水腫或骨盆壁是 IIIB。",
        "key": "子宮頸癌侵犯下 1/3 陰道為 FIGO IIIA。",
        "front": "Cervical cancer FIGO: lower third vagina",
        "back": "下 1/3 陰道侵犯 = IIIA；parametrium = IIB；hydronephrosis/pelvic wall = IIIB。",
        "summary": "Cervical cancer staging -> lower 1/3 vagina = IIIA。"},
    40: {"stem": "第一孕期唐氏症篩檢包含 NT、free beta-hCG 或 hCG、PAPP-A。Unconjugated estriol 是第二孕期 triple/quad screen 的項目。", "options": [("A", "錯誤。hCG 或 free beta-hCG 是第一孕期篩檢項目。"), ("B", "錯誤。Nuchal translucency 是第一孕期超音波重要項目。"), ("C", "正確。Unconjugated estriol 屬第二孕期母血篩檢項目，不是第一孕期標準項目。"), ("D", "錯誤。PAPP-A 是第一孕期母血篩檢項目。")], "core": "第一孕期 Down screen：NT + PAPP-A + free beta-hCG；uE3 是第二孕期項目。", "key": "第一孕期唐氏症篩檢不包含 unconjugated estriol。", "front": "First trimester Down screen components", "back": "包含 NT、PAPP-A、free beta-hCG/hCG；不含 uE3。", "summary": "Down screen -> first trimester excludes uE3。"},
})


if __name__ == "__main__":
    main()
