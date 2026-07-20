import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/108-2/medicine-6.json"
DATASET_ID = "108-2_medicine-6"
GENERATED_AT = "2026-07-20T16:47:55+08:00"
MODEL = "codex-high-quality-rewrite"


def explanation(stem, options, core):
    return f"【題幹解析】\n{stem}\n\n【選項詳解】\n{options}\n\n【核心考點】\n{core}"


UPDATES = {
    3: {
        "explanation": explanation(
            "題目問 lidocaine 加入 epinephrine 做周邊臂神經叢浸潤時，哪個麻醉作用敘述錯誤。Epinephrine 在此主要靠局部血管收縮，讓 lidocaine 留在注射區較久、降低血中吸收並延長阻斷；它不是靠 alpha-2 receptor 產生直接止痛效果，所以官方答案選 D。",
            "- A. epinephrine可延長lidocaine麻醉的作用時間：血管收縮會減少局部麻醉藥被帶回血液循環，神經周圍有效濃度維持較久，因此作用時間延長，這是正確敘述。\n- B. epinephrine可增強lidocaine神經阻斷的作用：局部藥物被清除得較慢時，lidocaine 在神經附近的濃度較穩定，臨床上可讓阻斷較深或較持久，因此不是本題要找的錯誤項。\n- C. epinephrine可減低lidocaine藥物全身性的吸收：這正是加入血管收縮劑的重要目的，可降低血中濃度上升速度，也減少局部麻醉藥全身毒性的風險。\n- D. epinephrine因作用於α2-adrenergic receptor,有直接止痛效果：周邊局部麻醉中 epinephrine 的高考點是 alpha-1 為主的血管收縮；直接 alpha-2 止痛較常想到 clonidine 或 dexmedetomidine 等藥物，因此這句機轉錯置。",
            "局部麻醉藥加 epinephrine 的重點是血管收縮、減少吸收、延長作用；不要把它誤記成 alpha-2 直接止痛藥。",
        ),
        "key_point": "Epinephrine 加入 lidocaine 主要靠局部血管收縮延長麻醉、降低全身吸收，並非 alpha-2 直接止痛。",
        "flashcard_front": "lidocaine 加 epinephrine：作用與錯誤機轉？",
        "flashcard_back": "作用是血管收縮、減少 lidocaine 吸收並延長阻斷；錯誤機轉是說 epinephrine 透過 alpha-2 receptor 直接止痛。",
        "flashcard_summary": "Lidocaine + epinephrine -> 血管收縮延長作用、降低全身吸收；不是 alpha-2 直接止痛。",
    },
    5: {
        "explanation": explanation(
            "題幹要找非去極化肌肉鬆弛劑中，屬於 benzyl-isoquinolinium compounds、又幾乎不釋放 histamine、因此較不會造成給藥後低血壓的藥物。Cis-atracurium 符合這三個條件，官方答案選 B。",
            "- A. mivacurium：它屬於 benzylisoquinolinium 類，但可能造成 histamine 釋放，快速或較大劑量給藥時可出現潮紅、低血壓或支氣管痙攣，因此不符合「沒有 histamine 釋放」。\n- B. cis-atracurium：cis-atracurium 是 atracurium 的異構物，屬 benzylisoquinolinium 類，histamine 釋放很少，血流動力學相對穩定，是題幹描述的藥物。\n- C. d-tubocurarine：這是較早期的 benzylisoquinolinium 類非去極化肌鬆藥，但會釋放 histamine 並有神經節阻斷作用，低血壓風險較明顯。\n- D. pancuronium：pancuronium 屬 aminosteroid 類，不是 benzylisoquinolinium；它較常見的是迷走神經阻斷造成心搏過速，而不是題幹要考的低 histamine 釋放藥物。",
            "非去極化肌鬆藥分類要會配副作用：cis-atracurium 是 benzylisoquinolinium 類且 histamine 釋放少；mivacurium、d-tubocurarine較會釋放 histamine。",
        ),
        "key_point": "Cis-atracurium 屬 benzylisoquinolinium 類，histamine 釋放少，血壓較穩定。",
        "flashcard_front": "哪個 benzylisoquinolinium 肌鬆藥 histamine 釋放少？",
        "flashcard_back": "Cis-atracurium；mivacurium 與 d-tubocurarine 較會釋放 histamine，pancuronium 則是 aminosteroid 類。",
        "flashcard_summary": "肌鬆藥分類 -> cis-atracurium 是低 histamine 釋放的 benzylisoquinolinium。",
    },
    12: {
        "explanation": explanation(
            "上斜肌通過滑車後改變拉力方向，主要功能是內旋，另外可使眼球下轉與外轉。題目問「不會」造成哪種運動；內轉主要是內直肌負責，不是上斜肌作用，所以官方答案選 C。",
            "- A. 看下(depression)：上斜肌有下轉作用，尤其在眼球內轉位置時下轉效果更明顯，因此這個選項是上斜肌會做的動作。\n- B. 內旋(intorsion)：內旋是上斜肌最重要的主要作用，讓眼球上極向鼻側旋轉，所以不能選。\n- C. 內轉(adduction)：眼球內轉主要由內直肌完成；上斜肌的水平分力反而偏向外轉，因此「內轉」不是它本身的作用。\n- D. 外轉(abduction)：上斜肌有外轉的次要作用，這點常和內直肌的內轉混淆；因為題目問不會做的動作，所以 D 不是答案。",
            "上斜肌口訣可抓「內旋、下轉、外轉」；內轉是內直肌，不是上斜肌。",
        ),
        "key_point": "上斜肌作用為內旋、下轉、外轉；不負責眼球內轉。",
        "flashcard_front": "上斜肌 superior oblique 的眼球運動？",
        "flashcard_back": "主要內旋，另有下轉與外轉；不做內轉，內轉由內直肌負責。",
        "flashcard_summary": "Superior oblique -> intorsion、depression、abduction；非 adduction。",
    },
    14: {
        "explanation": explanation(
            "假性內斜視是外觀看似內斜，但真正眼位沒有內斜。常見原因是鼻側鞏膜被遮住、瞳孔距離過近或 kappa angle 造成視覺軸外觀偏差。早產兒網膜症造成黃斑部異位屬於視網膜牽拉後的視覺軸改變，較可能造成真性斜視或其他方向的假性偏斜，不是典型假性內斜視原因，官方答案選 D。",
            "- A. 兩眼瞳孔間距太短：瞳孔距離較短時，兩眼看起來較靠近鼻側，外觀可像內斜，但角膜反光與遮蓋檢查可顯示眼位正常。\n- B. 顯著的內眥上皮皺摺(epicanthal folds)：內眥贅皮遮住鼻側白眼球，是嬰幼兒假性內斜視最經典原因。\n- C. 高度近視伴隨negative kappa angle：negative kappa angle 會讓角膜反光位置呈現類似內斜的外觀，因此可造成假性內斜視。\n- D. 早產兒網膜症造成黃斑部異位(ectopic macula)：ROP 牽拉黃斑會改變視軸與注視位置，臨床問題已不只是單純外觀遮蔽，並非假性內斜視的典型機轉。",
            "假性內斜視的核心是「外觀看起來內斜、實際眼位正常」；內眥贅皮、短瞳距、negative kappa angle 常見，黃斑部異位不是典型原因。",
        ),
        "key_point": "假性內斜視多由內眥贅皮、短瞳距或 negative kappa angle 造成；黃斑部異位不是典型假性內斜視原因。",
        "flashcard_front": "假性內斜視常見原因與例外？",
        "flashcard_back": "常見：內眥贅皮、短瞳距、negative kappa angle；例外：ROP 造成黃斑部異位。",
        "flashcard_summary": "Pseudoesotropia -> 外觀假內斜但眼位正常；ROP ectopic macula 非典型原因。",
    },
    15: {
        "explanation": explanation(
            "隱斜視是平常靠融合功能維持眼位，一旦遮蓋破壞融合後才露出偏斜。依本題官方答案，診斷重點放在 cover-uncover test：遮住再放開時觀察眼球是否出現復位運動。要注意有些教材會把 alternate cover test 列為更容易顯露 phoria、並用 prism cover test 量化偏斜；本題仍須依官方鍵選 A。",
            "- A. cover-uncover test：遮蓋一眼後再移開遮蓋，若被遮眼解除遮蓋時需要移動回正，代表曾在遮蓋下失去融合而偏斜，符合本題官方所問的隱斜視確認方式。\n- B. alternate cover test：交替遮蓋會更徹底打斷融合，常用來顯露總偏斜量；但題目問「診斷一般須靠何種檢查」且官方答案列 A，因此 B 不能改選。\n- C. prism cover test：稜鏡遮蓋檢查主要用稜鏡中和偏斜，用來測量角度與追蹤變化，不是本題官方指定的初步診斷答案。\n- D. prism reflex test(krimsky)：Krimsky 法靠角膜反光搭配稜鏡估算斜視角，常用於無法配合遮蓋檢查者，較偏向估算顯性斜視而非典型隱斜視診斷。",
            "隱斜視來自融合被破壞後才出現的眼位偏斜；本題官方以 cover-uncover test 為答案，但臨床教材對 alternate cover test 的角色常需一起辨認。",
        ),
        "key_point": "隱斜視是破壞融合後才顯現的偏斜；本題官方答案為 cover-uncover test，另需知道 alternate cover 常用於顯露與量測總偏斜。",
        "flashcard_front": "隱斜視 heterophoria：官方答案與檢查陷阱？",
        "flashcard_back": "本題官方選 cover-uncover test；但 alternate cover test 也常用於打斷融合、顯露 phoria，需依題目與官方鍵判讀。",
        "flashcard_summary": "Heterophoria -> 融合被破壞後偏斜；本題官方 A，alternate cover 為常見教材陷阱。",
        "manual_review_notes": ["隱斜視的常見教材多強調 alternate cover test 可顯露 phoria；本題官方答案為 A，建議人工複核題目用語。"],
    },
    22: {
        "explanation": explanation(
            "Hereditary hemorrhagic telangiectasia（HHT）常因鼻腔黏膜 telangiectasia 反覆流鼻血，治療會依嚴重度從保濕照護、局部燒灼或雷射，到手術重建或血管介入。此題答案狀態為官方全給分，表示選項在「不恰當」判定上有爭議或需看臨床情境，不能硬套成單一錯誤選項。",
            "- A. regular nasal mucosal care with nasal saline：鼻腔鹽水、保濕與黏膜照護是 HHT 鼻出血的基礎保守治療，通常是合理起始處置。\n- B. endonasal lasering or bipolar diathermy：內視鏡雷射或雙極電燒可處理可見的 telangiectasia，適合反覆鼻出血者，但需注意黏膜傷害與復發。\n- C. septodermoplasty：對嚴重、反覆且保守治療失敗的鼻出血，可用鼻中隔皮膚移植減少脆弱黏膜出血，屬較侵入性的選擇。\n- D. vascular embolization：血管栓塞可在特定出血或血管畸形情境使用，但在鼻腔 HHT 反覆出血並非所有病人都適合，風險與適應症要仔細評估；因此本題可能因情境不足而全給分。",
            "HHT 鼻出血治療要按嚴重度分層；本題官方全給分時，詳解重點是說明每個處置的適應症與限制，而不是擅自改答案。",
        ),
        "key_point": "HHT 鼻出血治療從鼻腔保濕、雷射/電燒到 septodermoplasty 或血管介入皆需依嚴重度與適應症選擇；本題官方全給分。",
        "flashcard_front": "HHT 反覆鼻出血：治療分層與本題答案狀態？",
        "flashcard_back": "可由鼻腔保濕、雷射/電燒進展到 septodermoplasty 或血管栓塞；本題為官方全給分，不能硬判單一錯誤選項。",
        "flashcard_summary": "HHT epistaxis -> 分層治療；108-2 medicine-6 Q22 官方全給分。",
    },
    26: {
        "explanation": explanation(
            "題目問 HPV 與頭頸癌的相關敘述何者錯誤。HPV 相關頭頸癌最典型是口咽癌，尤其扁桃腺與舌根，常見亞型為 HPV-16；E6、E7 分別干擾 p53 與 Rb。HPV 陽性口咽癌通常治療反應與預後較好，不是較差，所以官方答案選 D。",
            "- A. 在各個頭頸次部位中,與HPV相關性最高的是口咽癌(oropharyngeal cancer)：口咽癌是 HPV 相關性最高的頭頸癌部位，特別是扁桃腺與舌根，這句正確。\n- B. 在所有的HPV亞型中,以第16型與頭頸癌的關係最為密切：HPV-16 是頭頸癌，尤其 HPV 陽性口咽癌最重要的高危險亞型。\n- C. HPV產生的E6蛋白質會抑制p53的功能,E7蛋白質則會抑制pRb的功能：E6 促進 p53 降解，E7 使 Rb 路徑失控，兩者共同推動細胞週期失調與癌化。\n- D. HPV陽性的口咽癌對化學治療及放射治療的反應及預後較差：這句方向相反；HPV 陽性口咽癌一般對放化療較敏感，預後優於 HPV 陰性、菸酒相關腫瘤。",
            "HPV 頭頸癌高考點：口咽癌、HPV-16、E6 抑 p53、E7 抑 Rb，且 HPV 陽性口咽癌預後通常較好。",
        ),
        "key_point": "HPV 陽性口咽癌通常對放化療反應較好、預後較佳；說預後較差是錯誤敘述。",
        "flashcard_front": "HPV 陽性口咽癌：亞型、分子機轉、預後？",
        "flashcard_back": "常見 HPV-16；E6 抑 p53，E7 抑 Rb；HPV 陽性口咽癌通常放化療反應與預後較好。",
        "flashcard_summary": "HPV HNSCC -> oropharynx、HPV-16、E6/p53、E7/Rb、預後較佳。",
    },
    30: {
        "explanation": explanation(
            "Trisomy 13（Patau syndrome）常見中樞與顏面中線缺陷、唇顎裂、眼部異常、多指，以及心臟、腹壁或泌尿生殖異常。它典型不是大頭畸形；相反地常見小頭或前腦發育異常，所以「macrocephaly」不符合，官方答案選 C。",
            "- A. 唇顎裂(cleft lip/palate)：Patau syndrome 常有中線發育異常，唇裂或顎裂是常見表現，不能選為不會合併。\n- B. 臍膨出(omphalocele)：染色體三倍體相關胎兒可出現腹壁缺損，Patau syndrome 也可能合併臍膨出或其他內臟畸形。\n- C. 大頭畸形(macrocephaly)：Patau syndrome 的中樞神經異常常見 holoprosencephaly、小頭畸形與嚴重發育缺陷；大頭畸形不是典型合併異常。\n- D. 橈骨發育不良(radial bone aplasia)：Patau syndrome 可有肢體與骨骼發育異常，考題將它列為可能合併項；作答時主要用 C 的「大頭」與典型「小頭/中線缺陷」相反來排除。",
            "Patau syndrome 記憶重點是中線缺陷、唇顎裂、多指、嚴重中樞異常；頭部典型偏小頭或前腦發育異常，不是 macrocephaly。",
        ),
        "key_point": "Trisomy 13 常見中線缺陷、唇顎裂、多指與小頭/前腦異常；macrocephaly 不是典型表現。",
        "flashcard_front": "Patau syndrome 不典型合併異常？",
        "flashcard_back": "Macrocephaly 不典型；Patau 常見唇顎裂、多指、中線缺陷與小頭/holoprosencephaly。",
        "flashcard_summary": "Trisomy 13 -> 中線缺陷、唇顎裂、多指、小頭；非大頭畸形。",
    },
    59: {
        "explanation": explanation(
            "「侍者小費」姿勢是 Erb-Duchenne palsy 的典型描述，來自臂神經叢上幹 C5-C6 受損。肩外展與外旋、肘屈曲等功能變差，手臂呈內收、內旋、前臂旋前的姿勢，因此官方答案選 A。",
            "- A. 臂神經叢：臂神經叢上幹受損會影響 deltoid、supraspinatus、infraspinatus、biceps 等 C5-C6 支配肌群，形成 waiter's tip 姿勢，是正確答案。\n- B. 正中神經：正中神經病變常見拇指對掌、前臂旋前或橈側手指感覺問題，經典姿勢不是整個上肢內收內旋的 waiter's tip。\n- C. 尺神經：尺神經受損會出現爪形手、骨間肌萎縮或小指無名指感覺異常，表現集中在手部尺側，不是 Erb palsy 的姿勢。\n- D. 橈神經：橈神經麻痺典型是垂腕，因伸腕伸指無力；雖然也會影響上肢外觀，但不是肩肘姿勢改變為主的侍者小費。",
            "Waiter's tip 指向臂神經叢上幹 C5-C6 受損；正中、尺、橈神經各有手部或垂腕表現，定位不同。",
        ),
        "key_point": "侍者小費姿勢是臂神經叢上幹 C5-C6 受損的 Erb-Duchenne palsy。",
        "flashcard_front": "Waiter's tip posture 對應哪個神經病變？",
        "flashcard_back": "臂神經叢上幹 C5-C6 受損，造成 Erb-Duchenne palsy。",
        "flashcard_summary": "Waiter's tip -> brachial plexus upper trunk C5-C6 lesion。",
    },
    61: {
        "explanation": explanation(
            "鎖入症候群多來自兩側腹側橋腦病變，皮質脊髓徑與皮質延髓徑受損，病人意識清楚但四肢癱瘓、不能說話。可用垂直眼動或眨眼溝通；水平共軛注視因橋腦眼動結構受損通常不正常，所以題目問明顯錯誤時，官方答案選 C。",
            "- A. 四肢無力：兩側皮質脊髓徑中斷會造成嚴重四肢無力或癱瘓，這是鎖入症候群核心表現之一。\n- B. 兩側橋腦(pons)病變引起：典型病灶在腹側橋腦，常見原因包括 basilar artery occlusion，因此這句符合病灶定位。\n- C. 眼球左右共軛注視(conjugate gaze)功能正常：水平共軛注視仰賴橋腦 PPRF 與外展神經核相關網路，鎖入症候群常保留垂直眼動而不是水平注視正常，這句錯誤。\n- D. 皮質延髓徑(corticobular tract)部分受損：皮質延髓徑受損可造成構音、吞嚥與臉部運動控制障礙，解釋病人無法說話但清醒的表現。",
            "Locked-in syndrome：意識清楚、四肢癱瘓、不能言語，病灶在腹側橋腦；保留的是垂直眼動/眨眼，不是水平共軛注視。",
        ),
        "key_point": "鎖入症候群保留垂直眼動與眨眼，水平共軛注視通常受損。",
        "flashcard_front": "Locked-in syndrome：保留哪種眼動？哪種不正常？",
        "flashcard_back": "保留垂直眼動與眨眼；水平共軛注視因橋腦病灶通常不正常。",
        "flashcard_summary": "Locked-in syndrome -> ventral pons lesion、quadriplegia、anarthria、vertical eye movement preserved。",
    },
    70: {
        "explanation": explanation(
            "兩側腹股溝疼痛提示 L1 皮節或第一腰神經根受到刺激。題幹又說兩側大腿前屈角度正常，較不像主要髖關節或 iliopsoas 動作受限，而是壓迫性骨折造成神經根相關痛；最可能是 L1 壓迫性骨折，官方答案選 C。",
            "- A. C7：C7 皮節常對應中指與上肢遠端，壓迫時不會以雙側腹股溝疼痛為主要定位線索。\n- B. T8：T8 約在胸腹部上段皮節，接近肋弓或上腹部感覺區，位置明顯高於腹股溝。\n- C. L1：L1 皮節包括腹股溝區，第一腰椎壓迫性骨折可刺激相關神經根而造成雙側腹股溝痛，正好對上題目給的疼痛位置。\n- D. L5：L5 常對應小腿外側、足背與大拇趾伸肌相關功能，典型疼痛放射不會只定位在兩側腹股溝。",
            "皮節定位：腹股溝區抓 L1；C7 看中指，T8 看上腹/肋弓附近，L5 看足背與大拇趾。",
        ),
        "key_point": "雙側腹股溝痛對應 L1 皮節，最支持第一腰椎壓迫性骨折。",
        "flashcard_front": "腹股溝疼痛的皮節定位？",
        "flashcard_back": "腹股溝區主要對應 L1；壓迫性骨折合併腹股溝痛要想到 L1。",
        "flashcard_summary": "Groin pain dermatome -> L1；第一腰椎壓迫可刺激 L1 神經根。",
    },
    75: {
        "explanation": explanation(
            "Blowout fracture 是眼眶受鈍傷後，壓力使較薄弱的眼眶壁破裂，最常見是眶底。眶底下方是 maxillary sinus，所以骨折後較容易看到上頜竇積血；說 frontal sinus 比 maxillary sinus 更容易積血方向錯誤，官方答案選 B。",
            "- A. Waters' view及Caldwell view檢查可助於評估眼底骨折：現在 CT 最精準，但傳統 X 光 Waters view、Caldwell view 可協助初步看眶底與鼻竇變化，因此不是錯誤敘述。\n- B. frontal sinus比maxillary sinus更容易積血：眶底骨折緊鄰上頜竇，血液與眼眶內容物更容易進入 maxillary sinus；frontal sinus 不是典型最容易積血的位置。\n- C. Blowout fracture主要因orbital floor太薄弱導致：眼眶底壁薄且下方接上頜竇，是 blowout fracture 的典型脆弱處，這句正確。\n- D. 常伴隨有複視現象(diplopia)：下直肌或眶內軟組織嵌頓會限制眼球上轉，病人常有複視，尤其向上看時明顯。",
            "Blowout fracture 常考眶底薄弱、上頜竇積血、下直肌/軟組織嵌頓與複視；不是 frontal sinus 最易積血。",
        ),
        "key_point": "眼眶爆裂骨折最常涉及眶底，易造成上頜竇積血與複視；frontal sinus 不是典型積血處。",
        "flashcard_front": "Blowout fracture：最常骨折處與錯誤敘述？",
        "flashcard_back": "常在 orbital floor，血液進 maxillary sinus 且可複視；錯誤是說 frontal sinus 比 maxillary sinus 更易積血。",
        "flashcard_summary": "Blowout fracture -> orbital floor、maxillary sinus hematoma、diplopia；非 frontal sinus。",
    },
    78: {
        "explanation": explanation(
            "知情同意的核心是病人在充分理解手術內容、效益、風險與替代方案後，能自行做出是否接受治療的決定。這直接保障醫療倫理中的尊重自主原則，所以官方答案選 A。",
            "- A. 病人自主：醫師說明資訊並確認病人理解，是為了讓病人依自己的價值觀做決定，正是 autonomy 的實踐。\n- B. 病人隱私：隱私重點在個資、病情與身體暴露的保密；知情同意可包含資訊揭露，但主要目的不是隱私保護。\n- C. 資源浪費：資源使用涉及效益、成本與分配，和簽署手術同意書的倫理核心不同。\n- D. 公平正義：公平正義關心資源與照護機會是否公平；本題描述的是單一病人對自己手術做決定，不是分配正義問題。",
            "Informed consent 最主要保障 autonomy：病人知道、理解並自願決定。",
        ),
        "key_point": "手術知情同意最主要是確保病人自主權，而非隱私、資源分配或公平正義。",
        "flashcard_front": "Informed consent 最主要保障哪個倫理原則？",
        "flashcard_back": "病人自主 autonomy：充分理解後自願決定是否接受治療。",
        "flashcard_summary": "Informed consent -> autonomy；不是 privacy、resource allocation 或 justice。",
    },
}


def make_update(q, source_questions):
    source = source_questions[q]
    item = {
        "question_id": source["id"],
        "question_number": q,
        "explanation": UPDATES[q]["explanation"],
        "key_point": UPDATES[q]["key_point"],
        "flashcard_front": UPDATES[q]["flashcard_front"],
        "flashcard_back": UPDATES[q]["flashcard_back"],
        "flashcard_summary": UPDATES[q]["flashcard_summary"],
        "review_status": "ai_generated",
        "explanation_model": MODEL,
        "explanation_generated_at": GENERATED_AT,
        "manual_review_notes": UPDATES[q].get("manual_review_notes", []),
    }
    return item


def write_batch(path, start, end, numbers, source_questions):
    data = {
        "source_file": SOURCE_FILE,
        "dataset_id": DATASET_ID,
        "range": {"start": start, "end": end},
        "updates": [make_update(q, source_questions) for q in numbers],
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    source = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    source_questions = {q["question_number"]: q for q in source["questions"]}
    out_dir = Path("scratch/rewrite_updates/108-2_medicine-6")
    out_dir.mkdir(parents=True, exist_ok=True)
    write_batch(out_dir / "q003-q061_selected01.json", 3, 61, [3, 5, 12, 14, 15, 22, 26, 30, 59, 61], source_questions)
    write_batch(out_dir / "q070-q078_selected02.json", 70, 78, [70, 75, 78], source_questions)


if __name__ == "__main__":
    main()
