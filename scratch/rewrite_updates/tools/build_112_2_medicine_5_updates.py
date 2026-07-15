import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/112-2/medicine-5.json"
DATASET_ID = "112-2_medicine-5"
OUT_DIR = Path("scratch/rewrite_updates/112-2_medicine-5")
STAMP = "2026-07-15T00:00:00+08:00"


DATA = {
    1: {
        "topic": "大量輸血流程的血品比例",
        "analysis": "生命跡象不穩定且持續出血的外傷病人啟動 massive transfusion protocol 時，重點是用接近全血的平衡復甦，避免只補紅血球造成凝血因子與血小板稀釋。本題官方更正接受 C、D，代表 1:1:2 與 1:1:1 都被視為合理的高比例血漿與血小板策略。",
        "options": {
            "A": "血漿與血小板相對太少，紅血球比例過高，容易加重稀釋性凝血病變，臨床結果較差。",
            "B": "比 1:1:4 稍平衡，但仍偏向紅血球補充，不能充分反映大量出血時同步補凝血因子與血小板的原則。",
            "C": "1:1:2 是常用的平衡大量輸血比例，可降低凝血障礙與失血死亡風險，為官方接受答案之一。",
            "D": "1:1:1 最接近全血復甦，亦符合現代外傷大量輸血強調的血漿、血小板、紅血球平衡補充，為官方接受答案之一。",
        },
        "core": "大量輸血不是只補紅血球，而是要早期補血漿與血小板；常考比例為 1:1:1 或 1:1:2。",
        "key": "大量輸血流程應採平衡復甦，血漿、血小板與紅血球比例常以 1:1:1 或 1:1:2 為高分考點。",
    },
    2: {
        "topic": "術後肺水腫原因",
        "analysis": "術後肺水腫可分為靜水壓上升型與通透性增加型。體液過量、急性左心衰竭、胰臟炎造成的全身性發炎都可導致肺水腫；單純高血壓若未造成急性心衰竭，較不是典型直接原因。",
        "options": {
            "A": "胰臟炎可引發全身發炎反應與 ARDS，增加肺微血管通透性，可能造成非心因性肺水腫。",
            "B": "體液容積過量會提高肺微血管靜水壓，是術後肺水腫常見原因。",
            "C": "急性左心衰竭會使肺靜脈壓上升，造成心因性肺水腫。",
            "D": "高血壓本身不是術後肺水腫的典型直接原因，除非已造成急性心衰竭或容量負荷問題，因此最不容易造成肺水腫。",
        },
        "core": "肺水腫常見機轉是容量或左心壓力過高，或發炎造成微血管通透性增加；單純高血壓不是最典型原因。",
        "key": "術後肺水腫常見於體液過量、左心衰竭、ARDS/胰臟炎，單純高血壓較不典型。",
    },
    3: {
        "topic": "困難梭狀芽孢桿菌感染治療",
        "analysis": "CDI 常發生於抗生素使用後，因腸道菌叢被破壞而讓 C. difficile 增生並產生毒素。治療原則是停用誘發抗生素，並使用針對 CDI 的口服 vancomycin 或 fidaxomicin，不是再給廣效抗革蘭陰性菌抗生素。",
        "options": {
            "A": "CDI 可有水瀉、發燒，嚴重結腸炎時可有血便或白血球升高，描述可接受。",
            "B": "糞便毒素或核酸檢測可輔助診斷；嚴重或診斷不明時也可能以內視鏡看到偽膜性腸炎。",
            "C": "錯誤。應停用不必要的誘發抗生素，並給口服 vancomycin 或 fidaxomicin；廣效抗革蘭陰性菌藥物反而可能惡化菌叢失衡。",
            "D": "腹瀉會造成脫水、低鉀、酸鹼失衡等問題，補充水分與電解質是支持治療重點。",
        },
        "core": "CDI 的治療不是擴大抗生素涵蓋，而是停誘發藥並給針對 C. difficile 的治療。",
        "key": "CDI 治療首重停用誘發抗生素，並使用口服 vancomycin 或 fidaxomicin。",
    },
    4: {
        "topic": "傷口癒合延遲最常見原因",
        "analysis": "傷口癒合需要良好灌流、沒有過度張力、沒有血腫與感染。其中感染會延長發炎期、破壞新生組織並增加膠原分解，是最常見也最重要的可處理原因。",
        "options": {
            "A": "傷口感染會使發炎持續、膠原沉積與上皮化受阻，是傷口癒合延遲最常見原因。",
            "B": "縫合技巧不佳會造成張力過高或死腔，但整體而言不如感染常見。",
            "C": "傷口流血或血腫會增加感染風險並影響癒合，但不是最常見的直接原因。",
            "D": "糖尿病、營養不良、免疫抑制等合併症會延遲癒合，但題目問最常見原因時仍以感染為主。",
        },
        "core": "傷口癒合延遲的第一個要想到感染，因為感染會使發炎期延長並破壞修復環境。",
        "key": "傷口感染是傷口癒合延遲最常見原因。",
    },
    5: {
        "topic": "手術部位感染 SSI 定義",
        "analysis": "SSI 必須與手術切口、深部軟組織或器官腔室感染有關，並符合時間範圍。肺炎屬呼吸道感染，不是手術部位感染；切口膿瘍、人工物相關感染、吻合處膿瘍才符合 SSI 概念。",
        "options": {
            "A": "術後 21 天發生肺炎與敗血症，感染源在呼吸道，不在切口、深部切口或器官腔室，因此不符合 SSI 定義。",
            "B": "疝氣修補術後 28 天傷口癒合不良、有分泌物與膿瘍，符合表淺或深部切口 SSI。",
            "C": "關節置換屬植入物相關手術，11 個月後傷口紅腫且穿刺培養陽性，仍可符合植入物相關 SSI/人工關節感染範圍。",
            "D": "胃切除後吻合處膿瘍屬器官腔室感染，雖表面傷口正常，仍符合 organ/space SSI。",
        },
        "core": "SSI 看感染是否發生在切口、深部組織或手術相關器官腔室；術後肺炎不是 SSI。",
        "key": "術後肺炎不是 surgical site infection；吻合處膿瘍與切口膿瘍才是 SSI。",
    },
    6: {
        "topic": "MELD score 組成",
        "analysis": "MELD 用於估計末期肝病短期死亡風險與肝移植優先順序，核心參數為 bilirubin、INR、creatinine，現代 MELD-Na 另納入 sodium。白血球計數不屬 MELD。",
        "options": {
            "A": "總膽紅素反映肝臟排泄功能，是 MELD 的核心參數。",
            "B": "白血球計數可反映感染或發炎，但不是 MELD 分數公式的項目。",
            "C": "肌酐酸反映腎功能，肝硬化合併腎功能差預後差，因此是 MELD 參數。",
            "D": "INR 反映凝血合成功能，是 MELD 的核心參數。",
        },
        "core": "MELD 記 bilirubin、INR、creatinine；不要把 WBC 或 albumin 混進來。",
        "key": "MELD score 的基本參數為 bilirubin、INR、creatinine，非 WBC。",
    },
    7: {
        "topic": "燒傷淨體重損失併發症",
        "analysis": "嚴重燒傷後高代謝與蛋白質分解會造成 lean body mass 下降。臨床常以 10%、20%、30%、40% 對應不同嚴重後果：10% 免疫下降、20% 傷口癒合延遲、30% 肺炎與壓瘡、40% 死亡風險顯著上升。",
        "options": {
            "A": "10% 損失較早出現的是免疫功能下降，不是最典型的傷口癒合延遲門檻。",
            "B": "20% 損失更常對應傷口癒合延遲，而免疫功能下降在較早階段即可出現。",
            "C": "30% 淨體重損失會明顯增加肺炎與壓瘡風險，符合考點。",
            "D": "40% 損失常與死亡風險上升相關，不是主要用來描述脆弱性骨折。",
        },
        "core": "燒傷後 lean body mass loss 越高，從免疫下降、傷口癒合差，到肺炎壓瘡與死亡風險逐步增加。",
        "key": "燒傷病人 lean body mass loss 約 30% 時，肺炎與壓瘡風險明顯增加。",
    },
    8: {
        "topic": "腦下垂體腫瘤治療",
        "analysis": "多數功能性腦下垂體腺瘤，如 ACTH、GH、TSH 分泌腫瘤，首選經蝶竇手術切除。泌乳激素瘤對 dopamine agonist 反應佳，通常先以 cabergoline 或 bromocriptine 治療。",
        "options": {
            "A": "ACTH 分泌腫瘤造成 Cushing disease，通常首選經蝶竇手術。",
            "B": "GH 分泌腫瘤造成肢端肥大症，手術是主要初始治療之一。",
            "C": "TSH 分泌腫瘤少見，但通常也以手術為優先治療。",
            "D": "Prolactinoma 多先用 dopamine agonist，可縮小腫瘤並降低 prolactin，通常不是手術第一優先。",
        },
        "core": "垂體腺瘤中最愛考的例外是 prolactinoma：先用 dopamine agonist，不先開刀。",
        "key": "Prolactinoma 的第一線治療通常是 dopamine agonist，而非手術。",
    },
    9: {
        "topic": "出血性中風照護",
        "analysis": "出血性腦中風急性照護包含血壓、血糖、體位、吞嚥與壓瘡預防等。預防性抗癲癇藥不是所有病人都一定需要，通常用於癲癇發作、皮質出血或高風險情境。",
        "options": {
            "A": "避免高血糖是合理照護目標，常以小於 180 mg/dL 作為急性重症控制目標。",
            "B": "急性腦出血常需控制收縮壓，約 140 到 160 mmHg 是常見考試範圍。",
            "C": "意識障礙或臥床病人要注意翻身與皮膚照護，預防壓瘡是正確照護。",
            "D": "錯誤。沒有癲癇發作或特定高風險狀況時，不是所有出血性中風都一定要預防性抗癲癇藥。",
        },
        "core": "出血性中風可控制血壓與血糖並預防併發症，但抗癲癇藥不是每位病人常規必給。",
        "key": "腦出血照護不等於一定給預防性抗癲癇藥。",
    },
    10: {
        "topic": "顱內動脈瘤影像判讀",
        "analysis": "此題依附圖判讀，官方答案指出該影像位置屬顱內動脈瘤好發位置之一。缺少附圖時，作答重點是不要過度推論破裂或固定為中大腦動脈瘤；常見好發處包含 anterior communicating、posterior communicating、MCA bifurcation 等分叉處。",
        "options": {
            "A": "未破裂動脈瘤不是靠抗血小板藥物預防破裂或梗塞，治療需依大小、位置與破裂風險評估。",
            "B": "官方圖像位置被判定為顱內動脈瘤好發處，因此為正確。",
            "C": "若影像位置非 MCA bifurcation，不能單憑有動脈瘤就判為中大腦動脈瘤。",
            "D": "CTA 看見動脈瘤不代表已破裂；破裂需結合臨床蜘蛛膜下腔出血或影像出血證據。",
        },
        "core": "顱內動脈瘤常在 Willis circle 分叉處；影像題要避免把位置、破裂與處置混為一談。",
        "key": "CTA 動脈瘤影像需判斷位置；不能看到動脈瘤就推定破裂。",
    },
    11: {
        "topic": "腰椎椎間盤突出神經症狀",
        "analysis": "急性腰椎椎間盤突出常見於 L4-5、L5-S1，造成下背痛與神經根痛。疼痛減輕但麻木取代疼痛不一定代表神經恢復，可能是神經功能受損持續或進展，因此最不適當。",
        "options": {
            "A": "L4-5 與 L5-S1 是腰椎椎間盤突出最常見節段，正確。",
            "B": "長期姿勢、負重與退化會增加椎間盤損傷，描述合理。",
            "C": "典型症狀包含下背痛與沿神經根分布的下肢疼痛，正確。",
            "D": "疼痛減少而麻木增加不代表病變緩解；感覺缺失可能表示神經受壓仍存在，最不適當。",
        },
        "core": "神經根痛變麻不等於好轉；麻木、無力或進行性神經缺損要提高警覺。",
        "key": "腰椎椎間盤突出若疼痛變少但麻木增加，不可直接判定神經根病變緩解。",
    },
    12: {
        "topic": "Denis three-column middle column",
        "analysis": "Denis three-column model 中，middle column 包括椎體後半部、後半部椎間盤、後縱韌帶等結構。middle column 受損會影響胸腰椎骨折穩定性。",
        "options": {
            "A": "椎體全部不是 middle column；前半部屬 anterior column。",
            "B": "後半部椎體與後縱走韌帶符合 middle column 的核心組成。",
            "C": "椎莖屬 posterior elements，不屬 middle column 的典型定義。",
            "D": "椎關節與椎莖屬 posterior column，並非 middle column。",
        },
        "core": "three-column model：前柱是椎體前半，middle column 是椎體後半與 PLL，後柱是椎弓與後方韌帶複合體。",
        "key": "Middle column 包括後半部椎體與後縱韌帶。",
    },
    13: {
        "topic": "第二級腦震盪",
        "analysis": "腦震盪分級在不同教材略有差異，但第二級常見概念是意識未喪失，但症狀或意識混亂持續較久。只要有意識喪失通常會被歸在較嚴重等級，因此選項 A 錯。",
        "options": {
            "A": "錯誤。失去意識通常不是第二級腦震盪的定義，而代表較嚴重腦震盪或需更嚴格評估。",
            "B": "腦震盪後 1 到 2 週再受撞擊有 second impact 風險，應避免劇烈運動。",
            "C": "短暫失憶、混亂或注意力下降是腦震盪常見表現。",
            "D": "頭痛、記憶障礙與認知症狀可持續一段時間，描述合理。",
        },
        "core": "腦震盪若有意識喪失，通常不是輕中度分級可草率處理，需更謹慎評估與避免二次傷害。",
        "key": "第二級腦震盪不以失去意識為定義；有 LOC 通常代表較嚴重。",
    },
    14: {
        "topic": "血管腫瘤與血管畸形",
        "analysis": "血管腫瘤是內皮細胞增生，血管畸形是血管發育異常。嬰兒血管瘤多會自然退化，但不是一歲前半數完全消失；AVM 主要治療常需栓塞、手術或合併治療，硬化劑不是最好答案；微血管畸形通常不會隨年齡消失。",
        "options": {
            "A": "選 1、3 表示只認為 1 與 3 錯，但第 2 與第 4 也有問題，因此不完整。",
            "B": "選 2、3 把第 3 句也列為錯誤，但第 3 句區分血管腫瘤與畸形的本質是正確的。",
            "C": "第 1、2、4 句錯誤，第 3 句正確，符合題目。",
            "D": "選 1、3、4 錯在把第 3 句列為錯誤，且漏掉第 2 句。",
        },
        "core": "血管腫瘤是細胞增生，血管畸形是結構發育異常；血管畸形通常隨人長大，不會自行萎縮消失。",
        "key": "血管腫瘤與血管畸形要分清：hemangioma 可退化，vascular malformation 通常不會自然消失。",
    },
    15: {
        "topic": "Glomus tumor 好發位置",
        "analysis": "Glomus tumor 來自 glomus body，典型發生在手指遠端、特別是指甲下，表現為局部劇痛、冷敏感與點狀壓痛。",
        "options": {
            "A": "髖關節不是 glomus tumor 的典型好發位置。",
            "B": "手肘可有各種軟組織腫瘤，但不是 glomus tumor 最常見部位。",
            "C": "手指，尤其甲下區，是 glomus tumor 最常見位置。",
            "D": "頭頸部不是此題所問的典型最常見位置。",
        },
        "core": "看到 glomus tumor 要想到指甲下、點狀劇痛與冷敏感。",
        "key": "Glomus tumor 最常見於手指甲下區。",
    },
    16: {
        "topic": "Mathes-Nahai 肌肉皮瓣分類",
        "analysis": "Mathes-Nahai 依肌肉血供型態分類。官方更正接受 A、C；A 的中文與英文標示不一致，且若指 soleus 則不屬 type I；C 的 pectoralis major 常歸為 type V，而不是 type III。",
        "options": {
            "A": "官方接受為錯誤。題目中文寫比目魚肌但英文寫 gastrocnemius；若以比目魚肌理解，其血供型態不是 type I。",
            "B": "Gracilis 常為 type II，即一條主要血管加多條次要血管，配對正確。",
            "C": "官方接受為錯誤。Pectoralis major 常列為 type V，不是 type III。",
            "D": "Sartorius 常列為 type IV，即節段性血供，配對正確。",
        },
        "core": "Mathes-Nahai 要同時看血供型態與肌肉名稱；此題 A 有中英文不一致，C 的胸大肌分類也不對。",
        "key": "本題官方複數給分 A、C；pectoralis major 不是 type III，A 有 soleus/gastrocnemius 標示問題。",
    },
    17: {
        "topic": "消融式雷射與臉部細紋",
        "analysis": "消融式雷射用於皮膚 resurfacing，可改善皺紋、細紋與光老化。Fractional CO2 laser 是常用消融式雷射；pulsed dye、ruby 與 Nd:YAG 多有不同色素或血管適應症，非此題最佳。",
        "options": {
            "A": "Nd:YAG 常用於血管、除毛或深層病灶等，不是臉部細紋 resurfacing 的最佳消融式雷射。",
            "B": "Pulsed dye laser 主要針對血管性病灶，不是去除細紋的典型消融式雷射。",
            "C": "Fractional CO2 laser 可進行分段式汽化與膠原重塑，適合改善臉部細紋。",
            "D": "Ruby laser 主要針對色素或刺青等，非細紋 resurfacing 首選。",
        },
        "core": "臉部細紋與 resurfacing 常考 CO2 laser，尤其 fractional CO2。",
        "key": "Fractional CO2 laser 是改善臉部細紋的典型消融式雷射。",
    },
    18: {
        "topic": "男性女乳症與乳癌風險",
        "analysis": "男性女乳症可由生理時期、藥物或內分泌疾病引起。一般男性女乳症本身多為良性，但 Klinefelter syndrome 會顯著增加男性乳癌風險，因此說與乳癌風險無關是錯誤。",
        "options": {
            "A": "Spironolactone 可造成抗雄性素作用或荷爾蒙比例改變，誘發男性女乳症。",
            "B": "一般男性女乳症多是良性乳腺增生，本身不等同乳癌。",
            "C": "新生兒、青春期與老年期都可有生理性男性女乳症。",
            "D": "錯誤。Klinefelter syndrome 會增加男性乳癌風險，不能說與乳癌風險無關。",
        },
        "core": "一般 gynecomastia 多良性，但 Klinefelter syndrome 是男性乳癌風險因子。",
        "key": "Klinefelter syndrome 相關男性女乳症不可說與乳癌風險無關。",
    },
    19: {
        "topic": "吸入性灼傷處置",
        "analysis": "火災密閉空間、臉部燻黑、水泡與燒傷要高度懷疑吸入性灼傷。評估主要靠臨床與支氣管鏡，若有上呼吸道水腫風險要及早插管；胸部 X 光或 CT 早期可能正常，不能用來排除。",
        "options": {
            "A": "錯誤。吸入性灼傷不能靠胸部 X 光或 CT 來排除；懷疑時應重視臨床、氣道評估與支氣管鏡。",
            "B": "嚴重燒傷病人的死亡常與吸入性傷害、呼吸衰竭與感染有關，正確。",
            "C": "上呼吸道水腫可能快速惡化，意識清楚也可能需要預防性早期插管。",
            "D": "燒傷病人不建議常規預防性抗生素；有明確感染時再治療。",
        },
        "core": "吸入性灼傷是臨床診斷與氣道危機，早期 X 光正常不能放心。",
        "key": "疑似 inhalation injury 時，胸部 X 光/CT 不能排除，需重視早期氣道處理。",
    },
    20: {
        "topic": "Stanford 主動脈剝離分類",
        "analysis": "Stanford 分類不是依 intimal tear 位置，而是看剝離是否侵犯升主動脈。只要累及升主動脈就是 type A；未累及升主動脈、限於降主動脈則為 type B。",
        "options": {
            "A": "剝離若累及主動脈根部，可造成主動脈瓣閉鎖不全，正確。",
            "B": "錯誤。Stanford 分類依是否累及升主動脈，不是依 intimal tear 的破口位置。",
            "C": "急性 type A 需緊急手術，以避免破裂、心包填塞、急性 AR 等致命併發症。",
            "D": "無併發症的急性 type B 通常先以降壓、止痛與心率控制治療。",
        },
        "core": "Stanford A/B 的關鍵是升主動脈有沒有被剝離波及，不是破口在哪裡。",
        "key": "Stanford type A 是累及升主動脈；type B 是未累及升主動脈。",
    },
    21: {
        "topic": "EVAR endoleak 分類",
        "analysis": "EVAR 後 endoleak 依來源分類。Type I 是近端或遠端 sealing zone 漏；type II 是分支血管逆流；type III 是支架接合處分離或材質破損；type IV 是 graft porosity。",
        "options": {
            "A": "近端接觸區滲漏屬 type IA，正確。",
            "B": "腰動脈或下腸繫膜動脈逆流造成瘤囊灌流是 type II，正確。",
            "C": "錯誤。遠端接觸區滲漏是 type IB，不是 type III。",
            "D": "支架織物孔洞滲漏屬 type IV，正確。",
        },
        "core": "Endoleak type I 看 sealing zone，type II 看分支逆流，type III 看支架結構問題。",
        "key": "EVAR 遠端接觸區漏是 type I，不是 type III。",
    },
    22: {
        "topic": "再灌流後腔室症候群與橫紋肌溶解",
        "analysis": "急性下肢缺血再灌流後劇痛、小腿緊繃、被動牽拉痛，符合腔室症候群與橫紋肌溶解風險。常見高血鉀、CK 上升、myoglobinuria；高血鈣急性期最不典型，反而可見低血鈣。",
        "options": {
            "A": "肌肉壞死釋放鉀離子，可能造成高血鉀。",
            "B": "高血鈣最不可能；橫紋肌溶解急性期常見低血鈣，恢復期才可能反彈高血鈣。",
            "C": "肌肉壞死會使 creatine kinase 明顯上升。",
            "D": "肌紅蛋白釋放可造成 myoglobinuria 與急性腎損傷。",
        },
        "core": "再灌流後小腿劇痛要想到 compartment syndrome；橫紋肌溶解急性期是高鉀、CK 高、肌紅蛋白尿。",
        "key": "急性橫紋肌溶解較不會出現高血鈣。",
    },
    23: {
        "topic": "ASD 與 sinus venosus type",
        "analysis": "ASD 評估須注意肺血管阻力、年齡與缺損型態。Sinus venosus ASD 常合併部分肺靜脈回流異常，而不是典型合併二尖瓣逆流；二尖瓣裂隙與逆流較常見於 ostium primum ASD。",
        "options": {
            "A": "成人 ASD，特別是年紀較大或疑有肺高壓者，心導管可評估肺血管阻力，合理。",
            "B": "固定性肺血管阻力很高時關閉 ASD 可能惡化右心負荷與 Eisenmenger 生理，不可關閉。",
            "C": "錯誤。Inferior/sinus venosus ASD 常與異常肺靜脈回流相關，不是二尖瓣逆流。",
            "D": "青春期前女性用右前外側開胸可能影響乳房發育或美觀，需謹慎選擇。",
        },
        "core": "Sinus venosus ASD 要想到 anomalous pulmonary venous return；primum ASD 才常和 AV valve/mitral valve 問題相連。",
        "key": "Sinus venosus ASD 常合併異常肺靜脈回流，不是典型二尖瓣逆流。",
    },
    24: {
        "topic": "嬰兒主動脈瓣狹窄治療",
        "analysis": "8 個月大嬰兒主動脈瓣狹窄且壓差高，可考慮氣球瓣膜擴張或手術瓣膜切開。機械瓣膜置換在嬰幼兒因尺寸、成長與抗凝血問題最不適合；Ross procedure 可在特定情況考慮。",
        "options": {
            "A": "氣球瓣膜擴張可作為嬰兒先天性主動脈瓣狹窄的治療選項。",
            "B": "直視瓣膜切開可解除狹窄，也是一種可行選項。",
            "C": "機械瓣膜置換最不適合嬰兒，因瓣膜尺寸、成長問題與長期抗凝血風險高。",
            "D": "Ross procedure 在兒童可作為瓣膜替代策略之一，雖較複雜但不是本題最不適合。",
        },
        "core": "嬰兒主動脈瓣狹窄首重保留或修整瓣膜；機械瓣膜置換因成長與抗凝血問題最差。",
        "key": "嬰幼兒主動脈瓣狹窄最不適合直接機械瓣膜置換。",
    },
    25: {
        "topic": "食道憩室真假憩室",
        "analysis": "Zenker diverticulum 是咽食道交界處的 pulsion false diverticulum，通常只含黏膜與黏膜下層，不含完整肌肉層。Epiphrenic diverticulum 也多與動力異常相關，常為 pulsion false diverticulum。",
        "options": {
            "A": "Zenker、mid-esophageal/parabronchial 與 epiphrenic 是常見分類方式，描述可接受。",
            "B": "錯誤。Zenker diverticulum 是偽憩室，不含完整肌肉層。",
            "C": "Zenker 是最常見的食道憩室之一，描述正確。",
            "D": "Epiphrenic diverticulum 常為壓出型偽憩室，常與食道動力異常相關。",
        },
        "core": "Zenker diverticulum 是 pulsion false diverticulum，不是真憩室。",
        "key": "Zenker 憩室不含完整肌肉層，屬偽憩室。",
    },
    26: {
        "topic": "肺鱗狀上皮癌特徵",
        "analysis": "肺鱗狀上皮癌與抽菸關聯強，常位於中央或肺門附近，容易發生中央壞死與空洞化。相較之下，肺腺癌常位於周邊且較常見於非吸菸者。",
        "options": {
            "A": "錯誤。肺鱗狀上皮癌與抽菸高度相關。",
            "B": "錯誤。鱗狀上皮癌多為中央型，周邊較典型的是腺癌。",
            "C": "正確。鱗狀上皮癌可因中央壞死形成 cavitation。",
            "D": "錯誤。鱗狀上皮癌通常較局部生長，腺癌較常早期遠端轉移。",
        },
        "core": "肺鱗癌考點：吸菸、中央型、空洞化、高鈣血症；肺腺癌考周邊與早轉移。",
        "key": "肺鱗狀上皮癌較常中央壞死與空洞化。",
    },
    27: {
        "topic": "肺膿瘍來源與影像",
        "analysis": "肺膿瘍常由吸入造成厭氧菌感染，也可由血行播散如 Staphylococcus aureus bacteremia 造成。典型影像可見空洞與氣液平面，多數以抗生素為主治療。",
        "options": {
            "A": "膿瘍破裂到肋膜腔可能造成氣胸、膿胸或支氣管肋膜瘻，正確。",
            "B": "錯誤。肺膿瘍可由葡萄球菌菌血症或敗血性栓塞造成，不能說無關。",
            "C": "空洞中氣液平面是肺膿瘍的典型影像線索。",
            "D": "多數肺膿瘍可用抗生素治療，只有特定失敗或併發症才需引流或手術。",
        },
        "core": "肺膿瘍不只吸入，血行播散也可造成；影像常見 air-fluid level。",
        "key": "Staphylococcus bacteremia 可造成肺膿瘍，不能說無關。",
    },
    28: {
        "topic": "惡性肋膜積液常見原因",
        "analysis": "惡性肋膜積液常見原因包括肺癌、乳癌、淋巴瘤與間皮瘤等。黑色素瘤也可轉移到肋膜，但不是常見原因，因此在選項中最不典型。",
        "options": {
            "A": "肺腺癌是惡性肋膜積液最常見來源之一。",
            "B": "淋巴瘤可侵犯肋膜或造成惡性肋膜積液，屬常見鑑別。",
            "C": "Mesothelioma 原發於肋膜，是惡性肋膜積液重要原因。",
            "D": "黑色素瘤可轉移，但相較肺癌、淋巴瘤、間皮瘤，並非常見原因。",
        },
        "core": "惡性肋膜積液先想到肺癌、乳癌、淋巴瘤、間皮瘤。",
        "key": "黑色素瘤不是惡性肋膜積液的常見成因。",
    },
    29: {
        "topic": "胸部穿刺傷手術適應症",
        "analysis": "胸部穿刺傷需手術的情境包括心包填塞、食道破裂、大量血胸、持續出血、持續漏氣或肺無法擴張等。胸管一放即 500 mL 且生命徵象回穩，未達典型立即開胸標準。",
        "options": {
            "A": "心包填塞會快速致命，是手術或緊急處置適應症。",
            "B": "食道破裂污染縱膈與胸腔，通常需手術處理。",
            "C": "500 mL 初始引流且生命徵象回穩，不等於大量血胸立即開胸標準，因此較不適當。",
            "D": "氣胸合併持續漏氣、肺塌陷或通氣不足，可能需手術修補。",
        },
        "core": "胸部外傷開胸常見門檻是大量初始出血、持續出血或重大結構損傷；500 mL 且穩定通常不夠。",
        "key": "胸管初始 500 mL 且生命徵象回穩，不是典型立即開胸適應症。",
    },
    30: {
        "topic": "Zollinger-Ellison syndrome",
        "analysis": "ZES 是 gastrinoma 分泌 gastrin 造成胃酸過多與頑固性潰瘍。約 20% 到 25% 與 MEN1 相關，不是 MEN2；且 MEN1 相關 gastrinoma 常多發，不一定可單靠手術治癒。",
        "options": {
            "A": "Gastrinoma 分泌過多 gastrin 造成胃酸分泌增加與多發/頑固性潰瘍，正確。",
            "B": "錯誤。ZES 合併的是 MEN1，不是 MEN2；MEN1 病灶常多發，治療也較複雜。",
            "C": "多數 gastrinoma 位於 gastrinoma triangle，病灶小而定位困難，正確。",
            "D": "Gastrinoma 可為惡性並轉移至淋巴結或肝臟，描述正確。",
        },
        "core": "Zollinger-Ellison syndrome 要連到 gastrinoma、胃酸過多與 MEN1。",
        "key": "ZES 合併 MEN1，不是 MEN2。",
    },
    31: {
        "topic": "膽囊癌危險因子",
        "analysis": "膽囊癌預後差，常與膽結石、慢性發炎、瓷膽囊等相關。膽結石是最重要危險因子，多數膽囊癌病人可伴隨膽結石。",
        "options": {
            "A": "部分早期膽囊癌可在膽囊切除後偶然發現，但不能說大部分都如此診斷。",
            "B": "膽囊癌整體預後差，五年存活率不高，選項明顯錯誤。",
            "C": "膽結石與慢性膽囊發炎是膽囊癌最重要危險因子，描述正確。",
            "D": "T2 膽囊癌通常需擴大根除手術與肝床切除/淋巴清掃評估，不是單純追蹤。",
        },
        "core": "膽囊癌考點是膽結石與預後差；T2 以上通常需更積極手術。",
        "key": "膽結石是膽囊癌最重要危險因子之一。",
    },
    32: {
        "topic": "腸皮瘻管自然關閉",
        "analysis": "Enterocutaneous fistula 多為術後併發症，治療先控制敗血症、補液營養、保護皮膚並等待可能自然關閉。多數低風險瘻管可保守治療關閉，但輸出量、瘻管長度與阻塞感染會影響預後。",
        "options": {
            "A": "腸皮瘻管最常見原因是手術後併發症，不是惡性腫瘤侵犯。",
            "B": "輸出量分類各教材略有差異，常把高輸出定為大於 500 mL/day；但嚴格 low-output 常低於 200 mL/day，因此此句不是最佳考點。",
            "C": "瘻管短於 2 cm 較不容易自行關閉，長而窄且無阻塞感染者才較有機會關閉。",
            "D": "超過半數病人可先採保守治療並有自然關閉機會，符合官方答案。",
        },
        "core": "腸皮瘻管先穩定病人與營養支持；是否會關閉取決於輸出量、長度、阻塞、感染與腫瘤等因素。",
        "key": "Enterocutaneous fistula 多可先保守治療，部分病人可自行關閉。",
        "notes": ["Q32 瘻管輸出量 low/moderate/high 的切點不同教材可能有差異，已依官方答案解釋。"],
    },
    33: {
        "topic": "胰臟癌與術前膽道引流",
        "analysis": "胰臟頭部癌常以無痛性黃疸表現，Courvoisier sign 可見膽囊腫大。術前常規 ERCP 膽道減壓並不會降低術後傷口感染，反而可能增加膽道感染；通常只在膽管炎、嚴重黃疸或延遲手術等情況使用。",
        "options": {
            "A": "遺傳性胰臟癌與 PRSS1、STK11、CDKN2A、BRCA2 等基因相關，正確。",
            "B": "頭部癌常黃疸，體尾部癌常疼痛與體重減輕，正確。",
            "C": "胰頭癌造成膽道阻塞時可有可觸及且無痛性膽囊腫大，即 Courvoisier sign。",
            "D": "錯誤。常規術前 ERCP 減壓不會減少術後傷口感染，且可能增加感染風險。",
        },
        "core": "胰頭癌常黃疸；術前膽道減壓不是常規降感染手段，要有特定適應症。",
        "key": "胰臟癌術前常規 ERCP 膽道減壓不會降低術後傷口感染。",
    },
    34: {
        "topic": "Insulinoma 診斷",
        "analysis": "Insulinoma 典型為 Whipple triad：低血糖症狀、低血糖被證實、給糖後症狀改善。內生性胰島素過多會有 insulin 與 C-peptide 同時升高；外來胰島素則 C-peptide 低。",
        "options": {
            "A": "三徵稱 Whipple triad，不是 Charcot triad；且血糖單位應為 mg/dL，不是 mg/mL。",
            "B": "低血糖時 insulin 高且 C-peptide 高，支持內生性胰島素分泌，如 insulinoma。",
            "C": "Insulinoma 多為單發且良性，不是多發為主。",
            "D": "多數 insulinoma 為 sporadic；MEN1 相關者較可能多發，不是較多單發。",
        },
        "core": "低血糖合併 insulin 與 C-peptide 都高，才支持內生性 insulinoma。",
        "key": "Insulinoma 診斷可用低血糖時 C-peptide 上升來區分外來胰島素。",
    },
    35: {
        "topic": "肝腺瘤與 FNH",
        "analysis": "Hepatic adenoma 與口服避孕藥、代謝症候群等相關，可能出血或惡性轉化；FNH 是良性增生，常有中央疤痕，惡性轉化與出血風險低，多半觀察即可。",
        "options": {
            "A": "口服避孕藥與 hepatic adenoma 關聯較強，不是 FNH 較有關。",
            "B": "肝腺瘤較可能自發性出血，也有惡性轉化風險，正確。",
            "C": "影像上 FNH 常有典型中央疤痕，MRI/CT 常能區分兩者。",
            "D": "FNH 多數不需手術；肝腺瘤則依大小、症狀、性別與風險考慮切除。",
        },
        "core": "Hepatic adenoma 有出血與惡性風險；FNH 通常良性觀察。",
        "key": "肝腺瘤比 FNH 更需擔心出血與惡性轉化。",
    },
    36: {
        "topic": "Pringle maneuver",
        "analysis": "Pringle maneuver 是暫時夾住 hepatoduodenal ligament 內的 portal triad，也就是肝動脈、門脈與膽管，以控制肝臟流入血流。常採間歇性夾閉，例如夾 15 分鐘、放 5 分鐘，減少肝缺血傷害。",
        "options": {
            "A": "Pringle 夾的是肝動脈與門脈流入，不是肝靜脈流出。",
            "B": "間歇性夾 15 分鐘、放鬆 5 分鐘是常見考試描述，正確。",
            "C": "肝功能差者更需減少全肝缺血，選擇性或半肝血流控制可能較有利。",
            "D": "連續與間歇性、選擇性控制對缺血再灌流傷害可能不同，不能說無差異。",
        },
        "core": "Pringle maneuver 控制 portal triad 流入血流，不控制 hepatic vein 流出。",
        "key": "Pringle maneuver 常採間歇性 15 分鐘夾閉、5 分鐘放鬆。",
    },
    37: {
        "topic": "減重手術基本概念",
        "analysis": "近年 sleeve gastrectomy 因技術相對簡單、效果佳且避免腸道繞道，成為常見減重手術。代謝手術主要改善 type 2 diabetes；吸收不良型或繞道型較需長期營養補充；早期滲漏多需積極評估。",
        "options": {
            "A": "Sleeve gastrectomy 近年相當普遍，是正確敘述。",
            "B": "代謝手術主要治療 type 2 diabetes，不是 type 1 diabetes。",
            "C": "較需要長期補充維生素的是吸收不良或繞道成分較多的手術，不是單純限制性手術。",
            "D": "術後早期腸道滲漏可能危及生命，不能概括說多數保守治療即可。",
        },
        "core": "減重手術常考 sleeve gastrectomy 普及、type 2 diabetes 改善與營養缺乏風險。",
        "key": "近年減重手術常用 sleeve gastrectomy；代謝手術主要針對 type 2 diabetes。",
    },
    38: {
        "topic": "Bethesda nondiagnostic 甲狀腺結節",
        "analysis": "甲狀腺細針穿刺若為 Bethesda I nondiagnostic，下一步通常是超音波導引下重做 FNA，以取得足夠檢體。未有診斷前不應直接放射碘或手術，單純追蹤也可能延誤診斷。",
        "options": {
            "A": "重做細針穿刺是 Bethesda nondiagnostic 結節的標準下一步。",
            "B": "放射性碘不是 nondiagnostic solid nodule 的診斷處置。",
            "C": "尚未有惡性或可疑診斷，不宜直接甲狀腺葉切除作為第一步。",
            "D": "2 公分實心結節且 FNA nondiagnostic，單純 6 個月後追蹤不如重做 FNA 恰當。",
        },
        "core": "Bethesda I 的關鍵處置是重做 FNA，最好在超音波導引下取樣。",
        "key": "甲狀腺 FNA nondiagnostic 時，下一步通常是 repeat FNA。",
    },
    39: {
        "topic": "MEN2 與甲狀腺髓質癌追蹤",
        "analysis": "Pheochromocytoma 合併 medullary thyroid carcinoma 要想到 MEN2 與 RET 突變。MTC 追蹤用 calcitonin 與 CEA；MTC 不是濾泡細胞來源，不吸收放射碘，因此 131I whole body scan 不適合定位復發。",
        "options": {
            "A": "MEN2A 可合併副甲狀腺亢進，追蹤鈣、磷、PTH 合理。",
            "B": "Calcitonin 與 CEA 是 MTC 復發追蹤的重要腫瘤指標。",
            "C": "錯誤。MTC 來自 C cell，不攝取碘，131I whole body scan 不是定位復發的適當檢查。",
            "D": "Pheochromocytoma 可追蹤 catecholamine 代謝物與影像，描述合理。",
        },
        "core": "MTC 追蹤用 calcitonin/CEA，不用 radioiodine scan。",
        "key": "甲狀腺髓質癌不是濾泡細胞癌，不能用 131I whole body scan 追蹤定位。",
    },
    40: {
        "topic": "MEN2 家族篩檢",
        "analysis": "MEN2 是 RET proto-oncogene 的遺傳性疾病，家族成員應做 RET 基因檢測。兒童若有致病突變，需依突變風險決定預防性甲狀腺切除時機。",
        "options": {
            "A": "Thyroglobulin 用於分化型甲狀腺癌追蹤，不適合 MEN2/MTC 篩檢。",
            "B": "RET proto-oncogene 基因檢測可確認是否遺傳 MEN2 風險，最適宜。",
            "C": "超音波可找結節，但不能取代遺傳風險篩檢，且可能太晚。",
            "D": "Calcitonin/CEA 可追蹤 MTC，但家族幼兒風險評估首選 RET 檢測。",
        },
        "core": "MEN2 家族篩檢先做 RET，不是等 calcitonin 升高或超音波看到腫瘤。",
        "key": "MEN2 家族成員應以 RET proto-oncogene 檢測作為篩檢重點。",
    },
    41: {
        "topic": "乳房腫瘤切片方式",
        "analysis": "乳房病灶術前診斷以 core needle biopsy 較能提供組織架構與侵襲性判斷。FNA 只能提供細胞學，若惡性也不應直接以此決定全乳房切除，還需完整評估分期、病理與手術選項。",
        "options": {
            "A": "Core needle biopsy 取部分病灶組織，可視為 incisional biopsy 的概念，合理。",
            "B": "Vacuum-assisted biopsy 可取得更多檢體，降低取樣不足與偽陰性風險，合理。",
            "C": "Core biopsy 可分辨 in situ 與 invasive cancer，有助決定是否做腋下淋巴評估。",
            "D": "最不恰當。FNA 若為惡性仍不足以直接決定全乳房切除，需組織診斷與完整治療規劃。",
        },
        "core": "乳癌術前診斷偏好 core needle biopsy，因為能看組織架構與侵襲性。",
        "key": "FNA 細胞學惡性不能直接等同可立即全乳切除。",
    },
    42: {
        "topic": "乳房超音波惡性特徵",
        "analysis": "乳房超音波惡性特徵包括 taller-than-wide、不規則或角狀邊緣、低回音、後方陰影等。Posterior enhancement 較常見於囊性或部分良性病灶，不是典型惡性特徵。",
        "options": {
            "A": "Taller-than-wide 表示病灶垂直穿越組織平面，是惡性可疑徵象。",
            "B": "Angular 或 spiculated margin 是惡性可疑邊緣。",
            "C": "Posterior enhancement 較常與囊性或良性病灶相關，最不常作為惡性特徵。",
            "D": "Hypoechoic mass 是乳癌常見超音波表現之一。",
        },
        "core": "乳房超音波惡性特徵偏向不規則、taller-than-wide、低回音與後方陰影；後方增強較不典型。",
        "key": "Posterior wall enhancement 不是乳房腫瘤常見惡性超音波特徵。",
    },
    43: {
        "topic": "乳癌常用化療藥物",
        "analysis": "乳癌化療常用 anthracycline 類如 doxorubicin、epirubicin，以及 taxane 類如 docetaxel、paclitaxel。Etoposide 不是乳癌常規常用藥物。",
        "options": {
            "A": "Doxorubicin 是乳癌常用 anthracycline 類藥物。",
            "B": "Docetaxel 是乳癌常用 taxane 類藥物。",
            "C": "Etoposide 常用於小細胞肺癌、睪丸癌等，乳癌較不常使用。",
            "D": "Epirubicin 是乳癌常用 anthracycline 類藥物。",
        },
        "core": "乳癌化療常考 anthracycline 與 taxane；etoposide 不是典型乳癌常規藥。",
        "key": "Etoposide 最不常用於乳癌常規化療。",
    },
    44: {
        "topic": "小兒外科術式命名",
        "analysis": "Sistrunk operation 是甲狀舌管囊腫/竇道切除術式，不是鰓裂遺跡。Ladd 用於腸旋轉不良，Soave 用於 Hirschsprung disease，Peña 與 anorectal malformation 修補相關。",
        "options": {
            "A": "Malrotation 對應 Ladd procedure，正確。",
            "B": "錯誤。Sistrunk operation 用於 thyroglossal duct cyst，不是 branchial cleft remnant。",
            "C": "Hirschsprung disease 可用 Soave pull-through，正確。",
            "D": "Peña operation 與 anorectal malformation 後矢狀入路修補相關，正確。",
        },
        "core": "Sistrunk 對甲狀舌管囊腫；Ladd 對 malrotation；Soave 對 Hirschsprung。",
        "key": "Branchial cleft remnant 不對應 Sistrunk operation。",
    },
    45: {
        "topic": "食道閉鎖氣管食道瘻預後因子",
        "analysis": "食道閉鎖合併氣管食道瘻的預後主要受出生體重、重大先天異常尤其心臟病、肺部狀況與感染影響。單純手術矯正的時間本身，較不是傳統預後分類的核心因子。",
        "options": {
            "A": "出生體重低通常預後較差，是重要因子。",
            "B": "重大先天異常，特別心臟病，明顯影響預後。",
            "C": "手術時機會受病況影響，但不是經典預後評估中最相關的獨立因子。",
            "D": "肺部狀況與吸入、感染、呼吸窘迫有關，影響預後。",
        },
        "core": "EA/TEF 預後先看出生體重、心臟重大異常與肺部狀況。",
        "key": "食道閉鎖併 TEF 的預後較不直接由手術矯正時機決定。",
    },
    46: {
        "topic": "膀胱輸尿管逆流分級",
        "analysis": "VCUG 的 VUR 分級依逆流到輸尿管、腎盂腎盞及擴張扭曲程度。題目附圖官方答案為 bilateral grade V，代表嚴重逆流伴明顯輸尿管與集尿系統擴張、扭曲與腎盞鈍化。",
        "options": {
            "A": "Grade II 只有逆流到腎盂腎盞但無擴張，嚴重度不足。",
            "B": "Grade III 有輕中度擴張，但沒有 grade V 的嚴重扭曲與鈍化。",
            "C": "Grade IV 有中度擴張扭曲，但若附圖已有嚴重擴張與腎盞形態消失，仍不足。",
            "D": "Grade V 為最嚴重逆流，符合官方影像判讀。",
        },
        "core": "VUR grade V 是嚴重輸尿管擴張扭曲與腎盞鈍化；grade 越高腎損傷風險越高。",
        "key": "嚴重雙側 VUR 伴明顯擴張扭曲為 grade V。",
    },
    47: {
        "topic": "Gastroschisis 與 omphalocele 比較",
        "analysis": "Omphalocele 是中線臍部缺損，有囊膜覆蓋，常合併染色體與其他先天異常，缺口通常較大。Gastroschisis 多在臍旁、無囊膜覆蓋，腸道暴露造成液體與熱量流失較多，需要較多輸液。",
        "options": {
            "A": "臍膨出較常合併染色體異常，正確。",
            "B": "臍膨出缺口可較大，且常包含肝臟等器官，正確。",
            "C": "最不適當。通常腹裂畸形因腸道裸露，水分與熱量流失較多，較需要大量輸液。",
            "D": "臍膨出較常合併其他先天異常，正確。",
        },
        "core": "Gastroschisis 無囊膜，腸道暴露，輸液需求大；omphalocele 有囊膜且常合併染色體異常。",
        "key": "腹裂畸形通常比臍膨出更需要積極輸液。",
    },
    48: {
        "topic": "Hirschsprung disease 病理染色",
        "analysis": "Hirschsprung disease 診斷靠直腸切片顯示無神經節細胞，可用 H&E、calretinin 免疫染色與 acetylcholinesterase 染色輔助。PAS 主要看醣類、黴菌或特定沉積，不適合診斷無神經節。",
        "options": {
            "A": "PAS 染色不是 Hirschsprung disease 診斷無神經節細胞的適用染色，最不適用。",
            "B": "H&E 可直接評估是否有 ganglion cells。",
            "C": "Calretinin immunostaining 可輔助判斷神經節細胞與神經纖維。",
            "D": "AChE 染色可顯示黏膜下神經纖維增生，是經典輔助染色。",
        },
        "core": "Hirschsprung diagnosis 看無神經節；H&E、calretinin、AChE 有用，PAS 不適用。",
        "key": "PAS 不是先天性巨腸症直腸切片的診斷染色。",
    },
    49: {
        "topic": "Hirschsprung pull-through 術式",
        "analysis": "題幹描述切除無神經節腸段後，將有神經節腸段拉下與肛門端對端接合。這最符合 Swenson procedure；官方也接受 Soave，可能因附圖或改良拉下術式判讀而複數給分。Duhamel 是後方 retrorectal side-to-side，Sistrunk 與此無關。",
        "options": {
            "A": "Swenson procedure 是切除無神經節腸段並做 coloanal anastomosis，符合端對端接合描述。",
            "B": "Soave procedure 是 endorectal pull-through，官方也接受為正確答案之一。",
            "C": "Duhamel procedure 為 retrorectal pull-through 與側側吻合，不是題幹端對端接合的典型描述。",
            "D": "Sistrunk procedure 用於甲狀舌管囊腫，與 Hirschsprung disease 無關。",
        },
        "core": "Hirschsprung 常見 pull-through：Swenson、Soave、Duhamel；Sistrunk 不是腸道手術。",
        "key": "本題官方複數給分 Swenson 與 Soave；Duhamel 與 Sistrunk 不符。",
    },
    50: {
        "topic": "憩室炎破裂併膿瘍",
        "analysis": "老年人左下腹痛、發燒、白血球與 CRP 高、局部腹膜炎，加上既往大腸憩室炎，最符合乙狀結腸憩室炎併穿孔或局部膿瘍。CT 若見左下腹膿瘍與乙狀結腸發炎更支持。",
        "options": {
            "A": "缺血性腸壞死常有劇烈腹痛、血便或高風險血管病史，未最符合左下腹局部膿瘍情境。",
            "B": "乙狀結腸扭轉常有大量腹脹與咖啡豆樣影像，不是此題感染膿瘍表現。",
            "C": "乙狀結腸憩室炎破裂併膿瘍可造成左下腹痛、發燒、白血球升高與局部腹膜炎，最符合。",
            "D": "空腸腸繫膜膿瘍較少造成典型左下腹乙狀結腸區症狀。",
        },
        "core": "老年左下腹痛加發燒與局部腹膜炎，先想到 sigmoid diverticulitis with abscess。",
        "key": "乙狀結腸憩室炎破裂併膿瘍是老年左下腹痛發燒的重要診斷。",
    },
    51: {
        "topic": "下腸繫膜動脈分支",
        "analysis": "Inferior mesenteric artery 分支包括 left colic artery、sigmoid arteries、superior rectal artery。Middle rectal artery 通常來自 internal iliac artery，不是 IMA 分支。",
        "options": {
            "A": "Left colic artery 是 IMA 的分支。",
            "B": "Sigmoid artery 是 IMA 的分支。",
            "C": "Superior rectal artery 是 IMA 的終末分支。",
            "D": "Middle rectal artery 來自 internal iliac artery 系統，不是 IMA。",
        },
        "core": "IMA 分支：left colic、sigmoid、superior rectal；middle rectal 來自 internal iliac。",
        "key": "Middle rectal artery 不是 inferior mesenteric artery 的分支。",
    },
    52: {
        "topic": "Peutz-Jeghers syndrome",
        "analysis": "Hamartomatous polyps 加上口唇、口腔黏膜與手指末端黑色素沉著，是 Peutz-Jeghers syndrome 的典型組合，常與 STK11 突變及多種癌症風險增加相關。",
        "options": {
            "A": "Juvenile polyposis 也可有 hamartomatous polyps，但沒有典型口唇黏膜色素沉著。",
            "B": "Peutz-Jeghers syndrome 典型為 hamartomatous polyps 與 mucocutaneous pigmentation。",
            "C": "Lynch syndrome 是 DNA mismatch repair 相關大腸癌風險，非 hamartomatous polyposis 加色素沉著。",
            "D": "FAP 為 APC 突變造成大量 adenomatous polyps，不是此題表現。",
        },
        "core": "口唇黑斑加 hamartomatous polyps，就是 Peutz-Jeghers。",
        "key": "Peutz-Jeghers syndrome 典型為黏膜皮膚色素沉著與 hamartomatous polyps。",
    },
    53: {
        "topic": "減肥手術適應症",
        "analysis": "傳統考試常用減重手術適應症包括 BMI >40，或 BMI >35 且有肥胖相關合併症，並需嘗試保守治療失敗、心理狀態穩定、無活躍藥酒癮。家庭會議可協助支持，但不是正式適應症。",
        "options": {
            "A": "依傳統指引，BMI >40 或 BMI >35 合併肥胖相關疾病是適應症之一。",
            "B": "飲食與生活型態治療失敗是考量手術的重要條件。",
            "C": "錯誤。家庭會議決定不是減肥手術的醫學適應症。",
            "D": "心理穩定且無酒精依賴或非法藥物使用，有助降低術後風險，是重要評估項目。",
        },
        "core": "減重手術不是家屬開會決定，而是依 BMI、共病、保守治療失敗與心理/成癮評估。",
        "key": "家庭會議決定不是 bariatric surgery 的適應症。",
        "notes": ["Q53 近年 ASMBS/IFSO 適應症已更新；本題依考試常用傳統門檻與官方答案解釋。"],
    },
    54: {
        "topic": "微創手術模擬訓練",
        "analysis": "微創手術模擬訓練包含 box trainer、VR 與影像模型，可訓練深度感知、手眼協調、雙手操作與病人特定解剖理解。說模擬訓練仍無法做到這些訓練，是錯誤。",
        "options": {
            "A": "Box trainer 與 VR 可在安全環境練習基本技能，正確。",
            "B": "錯誤。深度感知、手眼協調與雙手敏捷性正是模擬訓練的重要目標。",
            "C": "病人特定術前模擬可幫助手術團隊理解解剖，符合模擬精神。",
            "D": "數位影像可建立三維模型與 VR 環境，正確。",
        },
        "core": "微創手術模擬就是用來練手眼協調、深度感與雙手操作。",
        "key": "Simulation training 可以訓練 depth perception、hand-eye coordination 與 bimanual dexterity。",
    },
    55: {
        "topic": "基本腹腔鏡手術",
        "analysis": "一般外科基本腹腔鏡手術常包含膽囊切除、闌尾切除、疝氣修補等。腹腔鏡子宮切除屬婦產科手術，不屬一般外科基本腹腔鏡術式範圍。",
        "options": {
            "A": "腹腔鏡膽囊切除是最典型基本腹腔鏡手術。",
            "B": "腹腔鏡子宮切除屬婦產科手術，非一般外科 basic laparoscopic procedures。",
            "C": "腹腔鏡疝氣修補是常見基本腹腔鏡術式。",
            "D": "腹腔鏡闌尾切除是常見基本腹腔鏡術式。",
        },
        "core": "一般外科基本腹腔鏡術式常考膽囊、闌尾、疝氣；子宮切除屬婦科。",
        "key": "腹腔鏡子宮切除不是一般外科基本腹腔鏡手術術式。",
    },
    56: {
        "topic": "Round cell tumor 與 Ewing sarcoma",
        "analysis": "Ewing sarcoma 典型染色體易位是 t(11;22)，形成 EWSR1-FLI1 融合基因。題目選項 A 寫 t(21;22)，染色體號碼錯誤，因此最不適當。",
        "options": {
            "A": "錯誤。Ewing sarcoma 最典型是 t(11;22)，不是 t(21;22)。",
            "B": "Ewing sarcoma 對放射線敏感，切緣不佳時可需術後局部放射治療。",
            "C": "原發性骨淋巴瘤常為 large B-cell 類型，單發病灶預後相對較好。",
            "D": "多藥化療可改善原發性骨淋巴瘤的治療成績。",
        },
        "core": "Ewing sarcoma 的高頻考點是 t(11;22) 與 EWSR1-FLI1。",
        "key": "Ewing sarcoma 典型易位是 t(11;22)，不是 t(21;22)。",
    },
    57: {
        "topic": "脂肪栓塞症候群",
        "analysis": "長骨骨折內固定後出現意識混亂、點狀出血與缺氧，典型為 fat embolism syndrome。治療以支持性照護、氧氣/呼吸支持為主；不應先假設頭部外傷腦壓升高而給 mannitol。",
        "options": {
            "A": "脂肪栓塞可在胸部 X 光呈 diffuse infiltrates，常形容為 snowstorm appearance。",
            "B": "低氧與血小板下降是脂肪栓塞常見表現。",
            "C": "最不適當。臨床三徵指向脂肪栓塞，不應優先以腦壓升高給 mannitol。",
            "D": "支持性治療是主軸，類固醇使用有爭議但在考試語境可作為必要時輔助。",
        },
        "core": "長骨骨折後低氧、神經症狀、點狀出血是 fat embolism syndrome。",
        "key": "脂肪栓塞症候群治療以支持性照護為主，不是先給 mannitol 降腦壓。",
    },
    58: {
        "topic": "Rolando fracture",
        "analysis": "大拇指掌骨基底的粉碎性關節內骨折是 Rolando fracture。Bennett fracture 則是第一掌骨基底的兩片式關節內骨折伴脫位。",
        "options": {
            "A": "Rolando fracture 是第一掌骨基底粉碎性關節內骨折，符合題幹。",
            "B": "Bennett fracture 是第一掌骨基底兩片式斜形關節內骨折，不是粉碎型。",
            "C": "Jones fracture 是第五蹠骨近端骨折，位置完全不同。",
            "D": "Boxer's fracture 是第五掌骨頸骨折，與拇指掌骨基底無關。",
        },
        "core": "第一掌骨基底骨折：Bennett 是兩片式，Rolando 是粉碎性關節內。",
        "key": "Comminuted intra-articular fracture of thumb metacarpal base 是 Rolando fracture。",
    },
    59: {
        "topic": "半月板破裂造成膝關節鎖住",
        "analysis": "年輕人運動後膝蓋疼痛、卡住、無法伸直或彎曲，X 光無骨折，最符合半月板破裂造成 mechanical locking。ACL 受傷常有快速腫脹與不穩，MCL 是內側疼痛，髕骨韌帶斷裂會無法主動伸膝。",
        "options": {
            "A": "MCL 斷裂主要是內側膝痛與外翻不穩，不典型造成膝關節卡住。",
            "B": "ACL injury 常見急性腫脹、pop sound 與不穩，非最典型 locked knee。",
            "C": "半月板破裂可造成膝關節卡住與伸直受限，最符合。",
            "D": "髕骨韌帶斷裂會影響伸膝機制，常有髕骨高位，不是此題最可能。",
        },
        "core": "運動後 locked knee 要想到 meniscal tear。",
        "key": "膝關節卡住且 X 光無骨折，最可能是半月板破裂。",
    },
    60: {
        "topic": "兒童近端肱骨骨折與 Salter-Harris II",
        "analysis": "兒童近端肱骨骨折常涉及生長板，常見 Salter-Harris type II 型態。鎖骨與肱骨髁上骨折多不以近端生長板 SH-II 為典型。",
        "options": {
            "A": "鎖骨骨折常見，但不屬典型 Salter-Harris II 生長板傷害。",
            "B": "近端肱骨骨折容易涉及近端肱骨生長板，常見 Salter-Harris II。",
            "C": "肱骨髁上骨折位於遠端肱骨髁上區，不是典型 SH-II 生長板傷害。",
            "D": "肱骨外髁骨折屬關節周邊骨折型態，非此題最容易造成 SH-II 的選項。",
        },
        "core": "兒童近端肱骨骨折常涉及生長板，Salter-Harris II 是常見型態。",
        "key": "近端肱骨骨折最容易造成 Salter-Harris type II 生長板傷害。",
    },
    61: {
        "topic": "舟狀骨骨折",
        "analysis": "跌倒手撐地後一個月腕部仍痛，且觸痛在 anatomical snuffbox 或舟狀骨區，要高度懷疑 scaphoid fracture。舟狀骨血供特殊，漏診可能導致 nonunion 或 avascular necrosis。",
        "options": {
            "A": "Pisiform 位於尺側掌側，與典型 snuffbox 壓痛不符。",
            "B": "Scaphoid 是 FOOSH 後最常見需警覺的腕骨骨折，符合題幹。",
            "C": "Lunate injury 可見月狀骨脫位或 Kienböck disease，但位置與題幹典型性較差。",
            "D": "Hamate hook fracture 常見於球拍或球棒運動，偏尺側掌側痛。",
        },
        "core": "FOOSH 後 snuffbox tenderness 先想到 scaphoid fracture。",
        "key": "跌倒撐地後持續腕痛，最典型腕骨骨折是舟狀骨。",
    },
    62: {
        "topic": "脊椎狹窄常見類型",
        "analysis": "脊椎狹窄最常見為退化性，尤其腰椎 L4-5。先天性椎管狹窄可發生但不是最常見。若有進行性神經缺損，手術減壓是重要治療選項。",
        "options": {
            "A": "最不適當。脊椎狹窄最常見是退化性，不是先天性。",
            "B": "狹窄可在 central canal、lateral recess、neuroforamen，pedicle 本身不是典型狹窄區。",
            "C": "腰椎狹窄常見於 L4-5，正確。",
            "D": "進行性神經缺損是手術減壓的重要適應症，療效可不錯。",
        },
        "core": "Spinal stenosis 最常見是退化性腰椎狹窄，常在 L4-5。",
        "key": "先天性椎管狹窄不是脊椎狹窄最常見類型。",
    },
    63: {
        "topic": "人工關節感染處置",
        "analysis": "Prosthetic joint infection 的診斷包括 sinus tract、培養、CRP/ESR、關節液白血球與臨床判斷。治療可依時間、菌種、植入物穩定度選擇 DAIR、一期或二期置換，不是一定都要拔除人工關節。",
        "options": {
            "A": "Sinus tract 連通到人工關節是 PJI 的強診斷線索。",
            "B": "少數病人 CRP 可不升高，不能只靠單一發炎指標排除。",
            "C": "關節液 WBC >3000 支持慢性 PJI，但診斷仍需整合其他標準。",
            "D": "最不適當。急性早期且植入物穩定者可考慮清創、保留植入物與抗生素治療，不一定都拔除。",
        },
        "core": "人工關節感染治療需分急慢性與植入物穩定度，不是所有病例都必須拔除。",
        "key": "PJI 不一定要拔除人工關節；部分可 DAIR 保留植入物。",
    },
    64: {
        "topic": "輸尿管阻塞與不可逆腎損傷",
        "analysis": "輸尿管結石造成持續尿路阻塞時，腎功能可隨時間逐漸不可逆受損。完全或高程度阻塞若持續數週，約一個月即可有明顯不可逆傷害風險。",
        "options": {
            "A": "一週可造成腎功能下降，但通常不是題目問最短導致不可逆傷害的常用答案。",
            "B": "約一個月的持續阻塞已可造成不可逆腎功能傷害，符合官方答案。",
            "C": "三個月過長，臨床上不應等到此時才處理持續阻塞。",
            "D": "六個月更晚，會嚴重低估阻塞性腎病變風險。",
        },
        "core": "尿路阻塞不能拖；持續約數週到一個月就可能造成不可逆腎損傷。",
        "key": "輸尿管阻塞持續約一個月可造成不可逆腎功能傷害。",
    },
    65: {
        "topic": "RCC 副腫瘤症候群",
        "analysis": "Renal cell carcinoma 可有多種副腫瘤症候群，如高血壓、紅血球增多症、高血鈣、肝功能異常（Stauffer syndrome）。低血鈣不是典型 RCC 副腫瘤表現。",
        "options": {
            "A": "RCC 可因 renin 或腎血流改變造成高血壓。",
            "B": "RCC 可有非轉移性肝功能異常，即 Stauffer syndrome。",
            "C": "低血鈣不是 RCC 典型副腫瘤症候群；相反常考高血鈣。",
            "D": "RCC 可分泌 EPO 或類似機轉造成紅血球增多症。",
        },
        "core": "RCC 副腫瘤常考高鈣、高血壓、紅血球增多、Stauffer syndrome。",
        "key": "RCC 常見高血鈣，不是低血鈣。",
    },
    66: {
        "topic": "Pheochromocytoma 10% rule",
        "analysis": "傳統 pheochromocytoma 常考 10% rule：約 10% extra-adrenal、10% bilateral、10% malignant、10% familial/MEN 等。多數發生在腎上腺，因此說約 10% 發生於腎上腺是錯的。",
        "options": {
            "A": "約 10% 與 MEN2 等遺傳症候群有關，是傳統記憶法之一。",
            "B": "錯誤。多數 pheochromocytoma 發生於腎上腺；約 10% 是腎上腺外 paraganglioma。",
            "C": "約 10% 雙側腎上腺是傳統考點。",
            "D": "尿中 catecholamine 或 metanephrine 相關檢測可輔助診斷。",
        },
        "core": "傳統 10% rule 中，10% 是腎上腺外，不是腎上腺內。",
        "key": "Pheochromocytoma 多數在腎上腺，約 10% 在腎上腺外。",
    },
    67: {
        "topic": "BPH 手術絕對適應症",
        "analysis": "BPH 手術絕對或強適應症包括反覆尿滯留、反覆尿路感染、膀胱結石、反覆肉眼血尿、腎功能受損等。前列腺體積大且 IPSS 高代表症狀嚴重，但不是絕對手術適應症。",
        "options": {
            "A": "BPH 造成反覆肉眼血尿是手術適應症。",
            "B": "前列腺體積 >50 mL 且 IPSS >20 分屬症狀嚴重，可考慮治療，但不是絕對手術適應症。",
            "C": "BPH 造成反覆尿路感染是手術適應症。",
            "D": "BPH 導致腎功能受損是重要手術適應症。",
        },
        "core": "BPH 絕對手術適應症看併發症，不只看體積與症狀分數。",
        "key": "IPSS 高與前列腺大不是 BPH 手術絕對適應症。",
    },
    68: {
        "topic": "TURP 效果與併發症",
        "analysis": "TURP 是 BPH 標準手術之一，對尿流速改善通常比多數微創療法持久且明顯。TUR syndrome 是經尿道手術吸收低張灌洗液造成低鈉與神經心血管症狀的併發症；尿失禁雖少見但仍可能發生。",
        "options": {
            "A": "TURP 對尿流速與症狀改善通常較微創療法更顯著且持久，正確。",
            "B": "TURP 住院與恢復通常比部分微創療法久，不能說相當。",
            "C": "尿失禁風險降低但不等於不會發生。",
            "D": "TUR syndrome 可造成噁心、嘔吐、意識混亂、低鈉與心血管症狀，官方接受為正確。",
        },
        "core": "TURP 效果佳，但仍有出血、低鈉 TUR syndrome、逆行射精與尿失禁等風險。",
        "key": "本題官方接受 A、D；TURP 改善尿流速佳，也可能有 TUR syndrome。",
    },
    69: {
        "topic": "尿路感染危險因子",
        "analysis": "尿路感染危險因子包括導尿管、尿滯留、出口阻塞、神經性膀胱、結石等。尿道下裂是尿道開口位置異常，並非典型最重要 UTI 危險因子。",
        "options": {
            "A": "尿路導管會破壞防禦並形成生物膜，是 UTI 重要危險因子。",
            "B": "膀胱出口阻塞造成尿滯留，增加感染風險。",
            "C": "神經性膀胱造成排空不全或需導尿，增加感染風險。",
            "D": "尿道下裂不如導尿管、阻塞與神經性膀胱典型，因此最不是危險因子。",
        },
        "core": "UTI 風險重點是尿滯留、導尿與排尿功能障礙。",
        "key": "尿道下裂不是典型引起尿路感染的主要危險因子。",
    },
    70: {
        "topic": "男性性功能神經支配",
        "analysis": "勃起主要由副交感骨盆神經促進；射精 emission 多由交感 hypogastric nerve；陰莖感覺與球海綿體肌收縮屬 pudendal nerve 的體神經功能。",
        "options": {
            "A": "儲精囊收縮屬交感神經，主要與 hypogastric nerve 相關，不是 obturator nerve。",
            "B": "陰莖背神經是 pudendal nerve 的感覺分支，不是造成勃起的副交感路徑。",
            "C": "球海綿體肌由 pudendal nerve 支配，屬體神經，正確。",
            "D": "膀胱頸收縮屬交感 hypogastric nerve，不是體神經。",
        },
        "core": "勃起靠副交感，射精 emission 靠交感，球海綿體肌靠 pudendal somatic nerve。",
        "key": "球海綿體肌收縮由 pudendal nerve 的體神經支配。",
    },
    71: {
        "topic": "腎移植接受者疾病復發",
        "analysis": "腎移植前需評估原腎病是否會復發。FSGS 可復發且影響預後；多囊腎不會在移植腎復發；oxalosis 常需肝腎合併處理。SLE 腎炎可在移植腎復發，不能說不會復發。",
        "options": {
            "A": "Primary hyperoxaluria/oxalosis 因肝臟代謝缺陷，可需肝腎合併移植。",
            "B": "多囊腎是遺傳性原腎疾病，移植腎通常不會復發多囊腎。",
            "C": "FSGS 在移植後可復發，復發會影響移植腎預後。",
            "D": "最不恰當。SLE 腎炎仍可能在移植腎復發，不能說不會復發。",
        },
        "core": "腎移植後會復發的病要記 FSGS、IgA、MPGN、SLE 等；多囊腎不會在移植腎復發。",
        "key": "SLE 腎炎移植後仍可能復發。",
    },
    72: {
        "topic": "肘部 X 光關節積液",
        "analysis": "肘部外傷側面 X 光若看見 fat pad sign 或關節囊膨出，表示關節積液，常提示隱性骨折。官方答案指出影像可明顯見關節積液，而非直接看見肱骨或橈骨骨折。",
        "options": {
            "A": "題目影像未必能直接看出肱骨骨折，不能選。",
            "B": "影像若無明顯橈骨骨折線，不能直接判斷。",
            "C": "題幹未以兒童生長板為主要線索，且官方影像重點不是 growth plate。",
            "D": "側面肘 X 光可藉 fat pad sign 判斷關節積液，為最恰當。",
        },
        "core": "肘外傷 X 光看不到骨折線時，fat pad sign/effusion 仍提示關節內傷害。",
        "key": "肘部側面 X 光明顯 fat pad sign 代表 joint effusion。",
    },
    73: {
        "topic": "Fournier gangrene",
        "analysis": "糖尿病病人會陰部紅腫脹痛、白血球上升，CT 若見會陰或陰囊軟組織氣體，最符合 Fournier's gangrene，也就是會陰部壞死性筋膜炎，需要立即抗生素與清創。",
        "options": {
            "A": "Inguinal hernia 可造成鼠蹊腫塊，但不會典型造成會陰壞死性感染與軟組織氣體。",
            "B": "Femoral hernia 多在股管區，不符合糖尿病會陰部感染表現。",
            "C": "Obturator hernia 常見腸阻塞與內收肌疼痛徵象，不是會陰感染。",
            "D": "Fournier's gangrene 是糖尿病會陰部壞死性筋膜炎，最符合。",
        },
        "core": "糖尿病加會陰紅腫痛與 CT 軟組織氣體，先想到 Fournier gangrene。",
        "key": "Fournier's gangrene 是會陰部壞死性筋膜炎，需緊急清創。",
    },
    74: {
        "topic": "膽結石腹部 X 光",
        "analysis": "飯後右上腹不適符合膽囊結石症狀，腹部影像若在右上腹膽囊區看到鈣化結石，最可能是 gallbladder stones。總膽管結石位置與臨床常伴黃疸或膽管炎；腎結石/腎結核位置與症狀不同。",
        "options": {
            "A": "膽結石可造成飯後右上腹不適，若影像鈣化位置在膽囊區最符合。",
            "B": "總膽管嵌塞結石常有黃疸、膽管炎或胰臟炎表現，不是此題最可能。",
            "C": "腎結核影像可見腎實質鈣化等，臨床不以飯後右上腹痛為主。",
            "D": "腎結石通常是側腹痛、血尿，位置也不同。",
        },
        "core": "飯後右上腹痛加膽囊區鈣化影像，最可能膽結石。",
        "key": "右上腹飯後不適與膽囊區結石影像支持 gallbladder stones。",
    },
    75: {
        "topic": "Dumping syndrome",
        "analysis": "Dumping syndrome 分早期與晚期。早期因高滲食物快速進入小腸造成腸液移動、腹瀉與血管舒縮症狀；晚期是餐後高血糖刺激過多胰島素，接著反應性低血糖，不是反應性高血糖。",
        "options": {
            "A": "依進食後發生時間分早期與晚期，正確。",
            "B": "最不適當。晚期 dumping 的核心是反應性低血糖，不是反應性高血糖。",
            "C": "早期 dumping 常有腹瀉；晚期以低血糖症狀為主，描述大致符合考點。",
            "D": "術後初期限制高糖飲料與簡單糖可減少 dumping，正確。",
        },
        "core": "早期 dumping 是高滲快速進腸，晚期 dumping 是胰島素過度反應造成低血糖。",
        "key": "晚期傾食症候群是反應性低血糖，不是高血糖。",
    },
    76: {
        "topic": "老人外傷特性",
        "analysis": "老人外傷最常見原因是跌倒，且因生理儲備差、用藥多，出血時生命徵象可能不典型。老人腦萎縮與抗凝血使用使硬腦膜下血腫常見；硬腦膜上血腫反而較不典型。",
        "options": {
            "A": "跌倒是 65 歲以上老人外傷最常見原因，正確。",
            "B": "老人可能因藥物或代償差，出血時生命徵象仍看似正常，正確。",
            "C": "最不適當。老人較常見硬腦膜下血腫，不是硬腦膜上血腫機率比一般人高。",
            "D": "使用抗凝血藥時，即使輕微頭部外傷也應低閾值安排 CT，正確。",
        },
        "core": "老人頭部外傷常擔心 subdural hematoma 與抗凝血相關遲發出血。",
        "key": "老人外傷較常見硬腦膜下血腫，不是硬腦膜上血腫。",
    },
    77: {
        "topic": "嵌頓疝氣造成小腸阻塞",
        "analysis": "無開刀史的高齡男性出現小腸阻塞，且左側鼠蹊部觸及硬塊，最可能是嵌頓或絞扼性疝氣造成腸阻塞。術後沾黏常見於有腹部手術史者。",
        "options": {
            "A": "腸套疊在成人較少見，通常需腫瘤或息肉作 lead point，與鼠蹊硬塊不符。",
            "B": "腸沾黏常見於腹部手術後，本題無開刀史，可能性較低。",
            "C": "直腸癌較常造成大腸阻塞與排便改變，不是小腸脹大加鼠蹊硬塊的最佳解釋。",
            "D": "疝氣可造成小腸阻塞，鼠蹊部硬塊是關鍵線索，最可能。",
        },
        "core": "小腸阻塞加鼠蹊部硬塊，先想到 incarcerated hernia。",
        "key": "無開刀史小腸阻塞合併鼠蹊硬塊，最可能疝氣。",
    },
    78: {
        "topic": "緊急手術同意與病人自主",
        "analysis": "病人先前只是暫不手術、日後再討論，並未明確拒絕破裂休克時的救命手術。現在病人無意識、無家屬可聯絡，若不手術將危及生命，醫師可依緊急避難與最佳利益原則立即處置。",
        "options": {
            "A": "不恰當。先前拒絕的是高風險選擇性手術，不等於拒絕破裂休克時的緊急救命手術。",
            "B": "不恰當。不能因年齡與資源理由直接拒絕可救命的緊急治療。",
            "C": "表述過度。緊急醫療可在無法取得同意時先救命，但不是籠統排除所有病人意願。",
            "D": "最適當。病人未聲明此緊急情境拒絕手術，且手術有救命機會，應立即安排緊急手術。",
        },
        "core": "無法取得同意且有立即生命危險時，可依病人最佳利益進行緊急救命處置。",
        "key": "選擇性手術暫拒不等於拒絕破裂休克時的緊急救命手術。",
    },
    79: {
        "topic": "活體肝臟捐贈配偶資格",
        "analysis": "台灣活體器官捐贈中，配偶原則上需生有子女或結婚二年以上；但若待移植者在結婚滿一年後才被診斷需要移植，則不受二年限制。本題結婚一年多後近日診斷需移植，妻子可捐贈。",
        "options": {
            "A": "錯誤。配偶屬法定可捐贈活體器官的關係範圍，不限血緣。",
            "B": "錯誤。雖有二年原則，但待移植者結婚滿一年後才診斷需移植者例外。",
            "C": "錯誤。配偶不一定要有婚生子女才可捐贈；法條另有二年或診斷時點例外。",
            "D": "正確。結婚已滿一年且近日才診斷需器官移植，符合例外，可捐贈。",
        },
        "core": "活體配偶捐贈記住：生有子女或結婚二年以上；但結婚滿一年後才診斷需移植者例外。",
        "key": "結婚滿一年後才診斷需移植，配偶可活體捐贈，不必等滿二年。",
    },
    80: {
        "topic": "器官移植倫理法律",
        "analysis": "讓等待移植病人自行接觸潛在捐贈者家屬並談價碼，會涉及捐贈者隱私、器官買賣與繞過公平分配制度。健保支付是醫療費用給付問題，不是此作法最直接的倫理法律問題。",
        "options": {
            "A": "病人接觸潛在捐贈者家屬會暴露捐贈者與家屬資訊，可能侵犯隱私。",
            "B": "直接談價碼明顯牽涉器官買賣或有償取得器官，違反無償原則。",
            "C": "自行媒合與談價會破壞器官分配的公正與制度化程序。",
            "D": "健保支付可能受醫療行為與給付規範影響，但不是此情境最直接包含的倫理法律問題。",
        },
        "core": "器官移植制度核心是自願、無償、隱私保護與公平分配；不可讓病人私下接觸家屬談價碼。",
        "key": "私下接觸捐贈者家屬談價碼涉及隱私、器官買賣與公平分配，不是健保支付問題。",
    },
}


def make_explanation(item):
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
    source = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    questions = {q["question_number"]: q for q in source["questions"]}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for start in range(1, 81, 10):
        end = start + 9
        updates = []
        for number in range(start, end + 1):
            q = questions[number]
            item = DATA[number]
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": number,
                    "explanation": make_explanation(item),
                    "key_point": item["key"],
                    "flashcard_front": item["topic"],
                    "flashcard_back": item["core"],
                    "flashcard_summary": f"{item['topic']}：{item['key']}",
                    "review_status": "ai_generated",
                    "explanation_model": "codex-high-quality-rewrite",
                    "explanation_generated_at": STAMP,
                    "manual_review_notes": item.get("notes", []),
                }
            )
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates,
        }
        (OUT_DIR / f"q{start:03d}-q{end:03d}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    missing = sorted(set(range(1, 81)) - set(DATA))
    if missing:
        raise SystemExit(f"missing DATA entries: {missing}")
    main()
