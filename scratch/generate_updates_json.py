import json
import os

source_file = "public/data/exams/109-1/medicine-5.json"
dataset_id = "109-1_medicine-5"

# 載入原始考卷對齊 ID
source_path = os.path.join("d:/Antigravity/med_exam_public", source_file)
with open(source_path, 'r', encoding='utf-8') as f:
    source_data = json.load(f)

source_q_map = {q['question_number']: q['id'] for q in source_data['questions']}

updates_data = []

# Q61
q61_explanation = """【題幹解析】
患者車禍撞擊儀表板導致股骨向後推擠，臨床呈現肢體變短且髖關節屈曲、內收、內旋轉的典型畸形，此為髖關節後脫位之特徵性表現。

【選項詳解】
- A. 錯誤。髖關節前位脫臼（anterior hip dislocation）通常是因為關節在極度外展（abduction）和外旋（external rotation）時受到衝擊，下肢畸形外觀呈現屈曲、外展及外旋，與題幹之內收、內旋不符。
- B. 正確。搭乘計程車前座車禍時膝關節撞擊儀表板（dashboard injury），股骨幹被迫向後推擠，最易引發髖關節後位脫臼。此時受損下肢會因髂股韌帶（iliofemoral ligament）與臀肌牽引，呈現肢體變短、屈曲、內收與內旋的典型畸形外觀。
- C. 錯誤。股骨頸骨折（femoral neck fracture）多發生於老年人，若發生骨折移位，患側下肢會因髂腰肌與臀肌的拉扯呈現肢體變短、外展及外旋（external rotation）的外觀，而非內收、內旋。
- D. 錯誤。股骨轉子間骨折（intertrochanteric fracture）同樣多見於骨質疏鬆患者，骨折移位時患側下肢亦會因肌肉收縮而呈現縮短、明顯外旋與外展的外觀，與題幹所述的內旋、內收表現相反。

【核心考點】
下肢創傷典型畸形鑑別：髖關節後脫位呈現屈曲/內收/內旋（F-AD-IR），前脫位與股骨頸/轉子間骨折則呈現外旋與外展。"""

updates_data.append({
    "question_number": 61,
    "explanation": q61_explanation,
    "key_point": "髖關節後脫位典型外觀呈肢體變短、屈曲、內收、內旋，前脫位或股骨頸/轉子間骨折移位則呈外旋。",
    "flashcard_front": "髖關節後脫位（posterior hip dislocation）典型下肢畸形外觀為何？",
    "flashcard_back": "肢體變短、髖關節屈曲（flexion）、內收（adduction）、內旋（internal rotation）。",
    "flashcard_summary": "髖關節後脫位 -> 畸形外觀：肢體變短、屈曲、內收、內旋。"
})

# Q62
q62_explanation = """【題幹解析】
兒童股骨頭缺血性壞死（Legg-Calvé-Perthes disease, LCPD）的預後與發病年齡及影像學變化密切相關。發病年紀愈輕（小於5歲），因骨骼仍有極佳的重塑（remodeling）潛力，通常預後良好，不屬於預後不佳的徵象。

【選項詳解】
- A. 錯誤。股骨頭部外側X光通透性增加（Gage's sign 或外側骨骺缺損）代表外側柱（lateral pillar）受累，會使股骨頭失去支撐而塌陷，屬於 Catterall 預後不良的「處於危險中的股骨頭（head at risk）」徵象之一。
- B. 錯誤。正常小兒股骨頭生長板為斜向，若生長板呈水平向（horizontal growth plate），顯示生物力學受力異常或骨骺滑脫風險增加，也是 Catterall 預後不良的指標之一。
- C. 正確。LCPD患者在發病時年紀小於 5 歲，由於股骨頭重塑能力強，病變自癒與恢復圓形的機會很高，此為預後「良好」的指標，不屬於預後不良的徵象。
- D. 錯誤。根據 Catterall 的分級，壞死範圍達 80% 屬於 Class III 或 IV，代表大範圍或全股骨頭壞死，受壓時極易發生塌陷與變形，屬於預後不佳的明確徵象。

【核心考點】
Legg-Calvé-Perthes disease (LCPD) 的預後因子：發病年齡小於5歲為重要良好指標；Catterall head-at-risk 徵象（如外側柱受累、生長板水平化、廣泛壞死及向外半脫位）代表預後不佳。"""

updates_data.append({
    "question_number": 62,
    "explanation": q62_explanation,
    "key_point": "Legg-Calvé-Perthes disease (LCPD) 預後與年齡極相關，發病小於5歲預後良好；Catterall head-at-risk 徵象（生長板水平化、外側柱受損、大範圍壞死）代表預後差。",
    "flashcard_front": "Legg-Calvé-Perthes disease (LCPD) 預後良好與不良的關鍵指標為何？",
    "flashcard_back": "發病年齡小於5歲為良好指標；Catterall head-at-risk 徵象（外側柱 X 光通透性增加、生長板水平向、壞死範圍大）為不良指標。",
    "flashcard_summary": "LCPD 預後因子 -> <5歲預後好；生長板水平、外側柱受累、壞死>80%預後差。"
})

# Q63
q63_explanation = """【題幹解析】
痛風急性發作時的處置應優先使用抗發炎藥物控制紅腫熱痛，第一線藥物包含NSAIDs與Colchicine。診斷上應注意急性期血尿酸值不一定上升，且關節液鏡檢應見陰性雙折射針狀結晶。

【選項詳解】
- A. 錯誤。在痛風急性發作時，高達30%以上的患者其血清尿酸（uric acid）濃度可能在正常範圍內，這是因為體內發炎反應刺激腎臟排出尿酸，或血中尿酸大量沉澱至關節腔內所致，故不能以尿酸正常排除診斷。
- B. 正確。急性痛風發作的治療目標是快速抗發炎與止痛。非類固團消炎藥（NSAIDs）、秋水仙素（colchicine）或全身性/局部類固醇均為臨床公認的第一線有效治療藥物。
- C. 錯誤。半月板或關節軟骨的軟骨鈣質沉著病（chondrocalcinosis）是焦磷酸鈣（CPPD）結晶沉積的典型X光表現，主要見於「假性痛風（pseudogout）」，而非長期高尿酸血症所致的痛風（gout，痛風多呈痛風石 tophi 沉積）。
- D. 錯誤。偏光顯微鏡下，痛風的尿酸鈉（MSU）結晶呈現強烈「陰性雙折射（negatively birefringent）」的針狀（needle-shaped）結晶。陽性雙折射（positively birefringent）且呈菱形或棒狀者，為焦磷酸鈣（CPPD）結晶的特徵。

【核心考點】
痛風與假性痛風鑑別：痛風（MSU）為陰性雙折射針狀結晶，急性期血尿酸不一定高，首選NSAIDs/秋水仙素；假性痛風（CPPD）為弱陽性雙折射菱形結晶，X光可見軟骨鈣化。"""

updates_data.append({
    "question_number": 63,
    "explanation": q63_explanation,
    "key_point": "痛風（MSU）急性期尿酸可能正常，治療首選 NSAIDs/秋水仙素，偏光鏡下呈強陰性雙折射針狀結晶；假性痛風（CPPD）則呈弱陽性雙折射菱形結晶。",
    "flashcard_front": "痛風（MSU）與假性痛風（CPPD）在偏光顯微鏡下的結晶特徵有何不同？",
    "flashcard_back": "痛風：尿酸鈉（MSU）呈現強陰性雙折射（negatively birefringent）針狀結晶；假性痛風：焦磷酸鈣（CPPD）呈現弱陽性雙折射（positively birefringent）菱形或棒狀結晶。",
    "flashcard_summary": "痛風 vs 假性痛風結晶 -> 痛風為陰性雙折射針狀結晶，假性痛風為弱陽性雙折射菱形結晶。"
})

# Q64
q64_explanation = """【題幹解析】
含鈣腎結石（主要為草酸鈣與磷酸鈣）的形成取決於促成因子與抑制因子的平衡。高尿鈣、高草酸尿及高尿酸尿皆會促進結晶飽和與沉澱；而尿中檸檬酸鹽則扮演螯合鈣離子的抑制保護角色。

【選項詳解】
- A. 正確。1（尿鈣增加）、2（尿酸上升，可作異質成核結晶核）、3（草酸鹽上升，易與鈣結合沉澱）皆是促使含鈣結石飽和度升高、形成結晶的常見原因。
- B. 錯誤。4（尿中檸檬酸鹽濃度上升）是防範結石的保護因子而非原因。檸檬酸根會與尿中鈣離子結合形成高度可溶的檸檬酸鈣，從而減少游離鈣與草酸根或磷酸根反應，因此檸檬酸鹽上升會抑制結石形成，不應包含在內。
- C. 錯誤。此組合漏掉了最關鍵的原發致病因子「1. 尿中鈣離子濃度增加」，且包含了具備預防結石效果的「4. 尿中檸檬酸鹽濃度上升」。
- D. 錯誤。此組合包含了抑制結石生成的保護因子「4. 尿中檸檬酸鹽濃度上升」，且漏掉了作為結晶核促進草酸鈣沉澱的「2. 尿中尿酸濃度上升」。

【核心考點】
尿路結石生成機制：高尿鈣（hypercalciuria）、高草酸尿（hyperoxaluria）及高尿酸尿（hyperuricosuria）為含鈣結石的三大促進物；而高檸檬酸尿（hypercitraturia）則能螯合鈣離子，屬於結石抑制劑。"""

updates_data.append({
    "question_number": 64,
    "explanation": q64_explanation,
    "key_point": "尿中鈣、尿酸及草酸濃度上升會促進含鈣結石形成，而尿中檸檬酸鹽則會螯合鈣離子、抑制含鈣結石生成。",
    "flashcard_front": "尿液中哪些成分是含鈣腎結石 of 腎臟結石 的促進物？哪種成分是防結石的保護因子？",
    "flashcard_back": "促進物：鈣離子、草酸鹽、尿酸；保護因子（抑制劑）：檸檬酸鹽（citrate，與鈣結合形成可溶性檸檬酸鈣）。",
    "flashcard_summary": "含鈣腎結石化學因子 -> 促進：高尿鈣、高草酸尿、高尿酸尿；抑制：高檸檬酸尿。"
})

# Q65
q65_explanation = """【題幹解析】
腎上腺意外瘤（incidentaloma）的處理原則取決於其是否具備內分泌功能，以及腫瘤的大小與影像學特徵。無功能性腫瘤若體積過大（通常大於4公分），惡性皮質癌風險增高，仍屬手術切除指徵。

【選項詳解】
- A. 正確。具有功能性（如分泌皮質醇、醛固酮或兒茶酚胺）會引發全身性疾病，而體積大於5公分（或臨床指引常用大於4公分）則惡性腎上腺皮質癌（adrenocortical carcinoma）風險顯著升高，兩者皆為明確的手術切除指徵。
- B. 正確。腹腔鏡腎上腺切除術（laparoscopic adrenalectomy）是目前切除良性或限制性腎上腺腫瘤的首選黃金術式，與傳統開腹手術相比，具有術後疼痛輕微、傷口小且恢復迅速等微創優勢。
- C. 正確。隨著電腦斷層（CT）與磁振造影（MRI）等影像檢查的普及與高解析度化，臨床上絕大多數的腎上腺腫瘤都是在進行非腎上腺相關檢查時意外被發現的，稱為腎上腺意外瘤（incidentaloma）。
- D. 錯誤。即使經內分泌篩檢確認不具內分泌功能，若腫瘤直徑大於4公分（或影像學呈現高CT值、沖刷率低等疑似惡性特徵），為排除惡性皮質癌的可能，仍強烈建議予以手術切除，而非一律不需手術。

【核心考點】
腎上腺意外瘤（adrenal incidentaloma）處置準則：大於 4 cm 或影像具惡性特徵（無功能性亦然），以及所有具功能性（功能分泌）之腫瘤，皆為手術切除適應症；手術首選腹腔鏡。"""

updates_data.append({
    "question_number": 65,
    "explanation": q65_explanation,
    "key_point": "腎上腺意外瘤若具功能性、直徑大於4公分或影像懷疑惡性，皆有手術切除指徵；良性或侷限性者手術首選腹腔鏡。",
    "flashcard_front": "無功能性腎上腺意外瘤（incidentaloma）何時具有手術切除指徵？",
    "flashcard_back": "直徑大於 4 cm，或影像特徵（如 unenhanced CT > 10 HU、沖刷率低）懷疑惡性（皮質癌）時。",
    "flashcard_summary": "腎上腺意外瘤手術指徵 -> 功能性、直徑 > 4 cm，或影像懷疑惡性。"
})

# Q66
q66_explanation = """【題幹解析】
睪丸腫瘤可分為原發性生殖細胞瘤與繼發性腫瘤。早期精原細胞瘤在根治性睪丸切除術後，首選處置通常是密切追蹤或選擇性單劑化療/放療，而非以全身性化學治療為主。

【選項詳解】
- A. 正確。原發性睪丸惡性腫瘤中，高達90%到95%以上屬於生殖細胞瘤（germ cell tumor），主要可細分為精原細胞瘤（seminoma）與非精原細胞瘤（non-seminomatous germ cell tumor, NSGCT）。
- B. 正確。在50歲以上的老年男性中，原發性睪丸癌極罕見，其睪丸腫瘤大多為繼發性（secondary）轉移而來，其中最常見的病理類型即為惡性淋巴瘤（lymphoma）。
- C. 正確。血清腫瘤標記 α-胎兒蛋白（AFP）在單純的精原細胞瘤（pure seminoma）中絕對不會升高。若臨床上病理報告為 seminoma 但 AFP 卻升高，代表該腫瘤混有非精原細胞瘤（如 yolk sac tumor）成分，必須按非精原細胞瘤原則治療。
- D. 錯誤。早期（Stage I）精原細胞瘤在接受根治性經腹股溝睪丸切除術後，其治癒率極高，首選的標準後續處置為「密切追蹤（surveillance）」；亦可選擇單劑 carboplatin 輔助化療或局部放射線治療以減低復發率。故「以化療為主」之敘述不符合早期治療實務（追蹤即可，放療亦是重要選項）。

【核心考點】
睪丸癌分類與治療原則：原發最常見生殖細胞瘤（seminoma 標記 HCG 可高但 AFP 必正常），老年續發最常見為淋巴瘤。Stage I seminoma 術後首選密切追蹤，非以化療為主。"""

updates_data.append({
    "question_number": 66,
    "explanation": q66_explanation,
    "key_point": "早期（Stage I）睪丸精原細胞瘤（seminoma）術後首選密切追蹤（surveillance），而非化療。精原細胞瘤 AFP 絕不升高。",
    "flashcard_front": "早期（Stage I）睪丸精原細胞瘤（seminoma）根治性切除術後，主要的輔助/追蹤策略為何？",
    "flashcard_back": "首選為「密切追蹤（surveillance）」，亦可選擇輔助性單劑 carboplatin 化療或局部放射線治療。",
    "flashcard_summary": "早期精原細胞瘤術後處置 -> 首選密切追蹤（surveillance），輔助化療或放療為可選方案。"
})

# Q67
q67_explanation = """【題幹解析】
繼發性膀胱腫瘤可經由鄰近器官直接浸潤或非鄰近器官的遠處血行轉移。在非鄰近器官引發遠處血行轉移至膀胱的癌症中，臨床以惡性黑色素瘤最為常見。

【選項詳解】
- A. 正確。根據泌尿科權威教科書（如 Campbell-Walsh Urology），在排除鄰近器官（如攝護腺、大腸直腸、子宮頸）直接侵犯的前提下，經由血行性或淋巴性遠處轉移至膀胱的惡性腫瘤中，原發源頭以「惡性黑色素瘤（melanoma）」的發生率最高。
- B. 錯誤。惡性淋巴瘤（lymphoma）侵犯膀胱多半屬於全身性淋巴瘤晚期的多器官侵犯，或極罕見的原發性膀胱結外淋巴瘤，並非遠處轉移至膀胱的最常見原發癌。
- C. 錯誤。胃癌（gastric cancer）屬於腹腔內消化道癌症，其遠處轉移多發生在肝臟、腹膜（如 Krukenberg 瘤）等部位，血行轉移至膀胱的病例在臨床上非常罕見。
- D. 錯誤。乳癌（breast cancer）雖有報告會引發膀胱轉移，多以瀰漫性黏膜下浸潤（疑似小葉癌 lobular carcinoma 轉移）呈現，但其膀胱轉移的整體發生率仍低於惡性黑色素瘤。

【核心考點】
繼發性膀胱癌來源鑑別：局部直接侵犯（攝護腺癌、大腸癌、子宮頸癌）是膀胱繼發腫瘤的主因；而發生遠處血行轉移至膀胱的非鄰近癌症中，原發最常見為惡性黑色素瘤（melanoma）。"""

updates_data.append({
    "question_number": 67,
    "explanation": q67_explanation,
    "key_point": "經血行/淋巴等遠處途徑轉移到膀胱的非鄰近器官癌症中，最常見的原發癌症是惡性黑色素瘤（melanoma）。",
    "flashcard_front": "發生非鄰近器官遠處血行轉移至膀胱的最常見原發癌症為何？",
    "flashcard_back": "惡性黑色素瘤（melanoma）。",
    "flashcard_summary": "膀胱遠處轉移癌 -> 最常見原發癌症為惡性黑色素瘤（melanoma）。"
})

# Q68
q68_explanation = """【題幹解析】
弛緩型神經性膀胱（flaccid neuropathic bladder）屬於下運動神經元（LMN）受損，主因是薦椎排尿反射弧（S2-S4）或其周邊傳出/傳入神經受損，使逼尿肌失去神經支配而無力。若為高位脊髓損傷（上運動神經元受損），排尿中樞反射弧完整，則會形成痙攣型神經性膀胱。

【選項詳解】
- A. 錯誤。S2-S4 脊髓（薦椎排尿中樞）受傷會直接破壞排尿反射弧的整合中樞，屬於典型的下運動神經元（LMN）受損，會導致逼尿肌無收縮力，引發弛緩型神經性膀胱。
- B. 正確。頸椎受傷伴隨四肢癱瘓（quadriplegia）屬於薦椎排尿中樞以上的高位脊髓損傷，即上運動神經元（UMN）受損。此時薦椎反射弧（S2-S4）依然完好，但失去大腦皮質的抑制控制，臨床上會表現為「痙攣型（spastic）」神經性膀胱，並常伴有逼尿肌-括約肌共濟失調（DSD），因此不會造成弛緩型膀胱。
- C. 錯誤。脊髓發育不良（myelodysplasia，如脊柱裂 spina bifida）會造成薦椎段的脊髓前角細胞（anterior horn cell）或前根發育不全，導致支配膀胱的下運動神經元受損，從而引起弛緩型神經性膀胱。
- D. 錯誤。小兒麻痺病毒（poliovirus）會選擇性感染並破壞脊髓前角細胞（anterior horn cells of spinal cord）。若波及控制膀胱逼尿肌的薦椎前角運動神經元，將中斷排尿反射弧，引發弛緩型神經性膀胱。

【核心考點】
神經性膀胱定位：高位脊髓損傷（薦椎 S2 以上，如頸、胸椎）導致上運動神經元受損，呈現痙攣型膀胱；薦椎排尿中樞（S2-S4）或周邊神經/前角細胞受損導致下運動神經元受損，呈現弛緩型膀胱。"""

updates_data.append({
    "question_number": 68,
    "explanation": q68_explanation,
    "key_point": "薦椎排尿中樞（S2-S4）以上受損（UMN，如頸椎受傷）會保留反射弧，造成痙攣型膀胱；S2-S4脊髓或前角細胞、周邊神經受損（LMN）則造成弛緩型膀胱。",
    "flashcard_front": "頸椎高位脊髓損傷與薦椎排尿中樞（S2-S4）受損所導致的神經性膀胱有何不同？",
    "flashcard_back": "頸椎損傷（S2以上）：上運動神經元（UMN）受損，導致痙攣型膀胱（伴 DSD）；S2-S4損傷：下運動神經元（LMN）受損，導致弛緩型（flaccid）膀胱。",
    "flashcard_summary": "神經性膀胱定位 -> 高位脊髓損傷為痙攣型膀胱，薦椎（S2-S4）/前角/周邊神經損傷為弛緩型膀胱。"
})

# Q69
q69_explanation = """【題幹解析】
間質性膀胱炎（interstitial cystitis, IC）是一種慢性非感染性膀胱發炎疾病。臨床診斷時必須先排除尿路感染與惡性病變，因此其特徵為尿液常規檢查與培養通常呈現正常。

【選項詳解】
- A. 正確。間質性膀胱炎具有顯著的性別與年齡傾向，好發於女性（男女比例約為 1:9），且多數患者在40歲以上的年齡段被首次診斷。
- B. 錯誤。間質性膀胱炎屬於無菌性、慢性非特異性發炎。患者的尿液常規檢查與尿液細菌培養通常是完全正常的（無明顯膿尿與血尿）。若尿中出現大量白血球（膿尿）或紅血球（血尿），應優先考慮急性細菌性膀胱炎、尿路結石或膀胱上皮癌等其他疾病，不可直接診斷為間質性膀胱炎。
- C. 正確。此病的核心臨床特徵為嚴重的下尿路刺激症狀，包括頻尿（部分患者一天可達數十次）、急尿、夜尿，以及特徵性的恥骨上骨盆腔脹痛或不適感。
- D. 正確。間質性膀胱炎的疼痛症狀與膀胱充盈（脹尿）密切相關，排尿後疼痛會隨之緩解。患者為避免脹尿的疼痛而頻繁排尿，長期下來會使膀胱肌肉適應性變差，導致膀胱功能性容積逐漸萎縮變小。

【核心考點】
間質性膀胱炎（IC/BPS）診斷與症狀：典型症狀為脹尿時恥骨上疼痛、排尿後緩解，伴隨頻尿與功能性膀胱縮小；診斷需排除感染，故尿常規與培養通常正常（無明顯膿尿或血尿）。"""

updates_data.append({
    "question_number": 69,
    "explanation": q69_explanation,
    "key_point": "間質性膀胱炎（IC/BPS）是一慢性非感染性膀胱炎，其診斷需排除感染與癌症，因此尿液常規檢查與尿液培養通常正常。",
    "flashcard_front": "間質性膀胱炎（IC/BPS）患者的尿液常規檢查（urinalysis）典型表現為何？",
    "flashcard_back": "通常是完全正常的（無明顯膿尿與血尿），診斷前必須先排除泌尿道感染或惡性腫瘤。",
    "flashcard_summary": "間質性膀胱炎尿常規 -> 典型表現為完全正常（排除細菌感染、膿尿或顯著血尿）。"
})

# Q70
q70_explanation = """【題幹解析】
小兒反覆性尿路感染常見於女孩，誘發原因可分為行為生理因子（如排尿排便障礙）及解剖結構異常（如膀胱輸尿管逆流）。無論有無發燒，一旦確診感染皆需使用抗生素治療以防腎臟受損。

【選項詳解】
- A. 錯誤。雖然反覆尿路感染需要排除結構異常，但大多數反覆性尿路感染的女孩在接受影像學檢查後，其尿路系統解剖構造完全正常，病因多為功能性排尿障礙或不良生活習慣。
- B. 正確。憋尿和少喝水會減少尿流沖刷尿道的次數，使細菌容易上行滋生；而慢性便秘時，直腸蓄積的糞便會直接壓迫膀胱頸與後尿道，干擾膀胱排空，增加餘尿量，這些行為與排便障礙是女孩反覆尿路感染最常見的非結構性誘因。
- C. 錯誤。沒有發燒症狀通常代表是下尿路感染（膀胱炎），但仍需要使用抗生素進行適當療程的治療。若不予治療，除了會持續產生解尿疼痛、頻尿等不適，細菌還極可能沿著輸尿管逆行上行，引發嚴重的急性腎盂腎炎與腎臟結疤。
- D. 錯誤。膀胱輸尿管尿液逆流（VUR）是導致小兒反覆性尿路感染（特別是發燒性上尿路感染）最常見的解剖學異常原因之一。尿液逆流會把膀胱內的細菌直接送往腎臟，造成反覆的腎盂腎炎。

【核心考點】
兒童反覆性尿路感染（UTI）病因與處置：最常見的功能性誘建立在排尿排便習慣障礙（憋尿、少喝水、慢性便秘）；最常見的解剖異常為膀胱輸尿管逆流（VUR）；確診後皆需給予抗生素治療，不可因無發燒而忽略。"""

updates_data.append({
    "question_number": 70,
    "explanation": q70_explanation,
    "key_point": "小兒反覆尿路感染女孩多數解剖構造正常，憋尿、少喝水及便秘是常見功能性誘因，而膀胱輸尿管逆流（VUR）是最常見的解剖異常。",
    "flashcard_front": "小兒（特別是女孩）反覆性尿路感染（UTI）最常見的非結構性（功能性）誘因為何？",
    "flashcard_back": "憋尿、飲水過少（減少尿流沖刷）以及慢性便秘（直腸糞便壓迫膀胱頸導致排尿不順、餘尿增加）。",
    "flashcard_summary": "兒童反覆尿路感染功能誘因 -> 憋尿、少喝水、慢性便秘（排尿排便障礙）。"
})


# 組合最終 JSON
final_updates = []
for upd in updates_data:
    q_num = upd["question_number"]
    q_id = source_q_map[q_num]
    
    final_updates.append({
        "question_id": q_id,
        "question_number": q_num,
        "explanation": upd["explanation"],
        "key_point": upd["key_point"],
        "flashcard_front": upd["flashcard_front"],
        "flashcard_back": upd["flashcard_back"],
        "flashcard_summary": upd["flashcard_summary"],
        "review_status": "ai_generated",
        "explanation_model": "codex-high-quality-rewrite",
        "explanation_generated_at": "2026-07-13T11:45:00+08:00",
        "manual_review_notes": []
    })

output_structure = {
    "source_file": source_file,
    "dataset_id": dataset_id,
    "range": { "start": 61, "end": 70 },
    "updates": final_updates
}

# 確保輸出目錄存在
output_path = "d:/Antigravity/med_exam_public/scratch/rewrite_updates/109-1_medicine-5/q061-q070.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# 寫入 JSON
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output_structure, f, indent=2, ensure_ascii=False)

print(f"Updates successfully generated and saved to: {output_path}")

# 校驗 JSON 格式
try:
    with open(output_path, 'r', encoding='utf-8') as f:
        loaded = json.load(f)
    print("Verification passed: JSON is valid.")
except Exception as e:
    print(f"Verification failed: {e}")
