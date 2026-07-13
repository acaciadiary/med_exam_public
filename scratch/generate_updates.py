# -*- coding: utf-8 -*-
import json
import os

updates = [
    {
        "question_id": "110-2_medicine-3_031",
        "question_number": 31,
        "explanation": "【題幹解析】\n病患為36歲女性，臨床表現有微燒、上眼瞼及臉頰部紅疹（提示 Heliotrope rash 或 Gottron's sign），且伴隨近端肢體無力（「必須側身以雙手扶持起床」代表近端大腿及軀幹肌群無力）。血清學檢查顯示 ANA 輕度陽性（1:40 speckled）且補體（C3、C4）正常，最有可能的診斷為皮肌炎（dermatomyositis）。\n\n【選項詳解】\n- A. 正確。皮肌炎（dermatomyositis）以對稱性近端肌肉無力（例如起床、起立、爬樓梯困難）為核心臨床表徵，並常伴隨特徵性皮膚病變，如上眼瞼的紫紅色斑（Heliotrope rash）與臉頰紅疹，與本病患的病史完全符合。\n- B. 錯誤。全身性紅斑性狼瘡（systemic lupus erythematosus, SLE）雖可有發燒、臉部紅疹及 ANA 陽性，但一般不會以如此典型且嚴重的急性近端骨骼肌無力為首發表現，且 SLE 活性期通常會伴隨補體（C3、C4）的明顯消耗下降。\n- C. 錯誤。濕疹（eczema）為單純的皮膚發炎反應，會造成局部皮膚紅腫、搔癢與脫屑，但絕不會合併全身性的骨骼肌病變與近端肌肉無力症狀。\n- D. 錯誤。光敏感（photosensitivity）是皮膚對紫外線產生的異常免疫反應，為多種風濕免疫疾病（如 SLE）或藥物引發的皮膚症狀，但不會造成近端肌肉無力與起立困難。\n\n【核心考點】\n皮肌炎（Dermatomyositis）的診斷關鍵在於「對稱性近端肌無力」合併特徵性皮膚表現（如上眼瞼紫紅斑 Heliotrope rash、關節伸側 Gottron 氏丘疹）。臨床上若出現起床或站立需要雙手扶持的近端肌病變，且伴隨臉部紅疹，應高度懷疑皮肌炎。",
        "key_point": "皮肌炎（Dermatomyositis）的診斷核心在於對稱性近端肌無力合併特徵性皮膚病變（Heliotrope rash、Gottron's papules）。",
        "flashcard_front": "皮肌炎 (Dermatomyositis) / 臨床診斷特徵",
        "flashcard_back": "典型表現為對稱性近端肌無力（如起立、起床困難），合併特徵性皮膚紅疹（如上眼瞼紫紅斑 Heliotrope rash 或關節伸側 Gottron 氏丘疹）。",
        "flashcard_summary": "皮肌炎診斷 -> 對稱性近端肌無力伴隨眼瞼/臉頰特徵性紅疹。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_032",
        "question_number": 32,
        "explanation": "【題幹解析】\n21歲男性自青少年期（15歲）起，反覆發生由流行性感冒嗜血桿菌（Haemophilus influenzae，一種有莢膜的細菌）引起的肺炎，並伴有慢性鼻竇炎與支氣管擴張，而全血球計數及分類大致在正常範圍。此病史高度提示「體液免疫缺陷（humoral immunodeficiency，即抗體缺乏）」，例如常見變異型免疫缺陷病（CVID）。為了評估體液免疫缺損，首要且最關鍵的檢查是檢測血清中免疫球蛋白（IgG, IgA, IgM）的定量。\n\n【選項詳解】\n- A. 錯誤。CD4 與 CD8 淋巴細胞計數主要用於評估細胞免疫（cellular immunity）缺陷，例如 HIV/AIDS 或重症聯合免疫缺陷病（SCID）。本例主要為反覆有莢膜細菌引起的局部竇肺部感染，主要是抗體調理作用不足的問題，而非細胞免疫缺損。\n- B. 正確。反覆的有莢膜細菌（如流感嗜血桿菌、肺炎鏈球菌）感染與支氣管擴張，是體液免疫（抗體）缺陷的典型表現。測量血清免疫球蛋白 G（serum IgG）及其他免疫球蛋白（IgA、IgM）濃度，是診斷原發性抗體缺陷病的第一步與最基礎評估。\n- C. 錯誤。血中免疫球蛋白 E（serum IgE）主要與過敏性疾病（如氣喘、異位性皮膚炎）或特定寄生蟲感染相關。雖然高 IgE 症候群也會有反覆感染，但其典型為冷膿瘍（cold abscess）及粗糙面容，檢測 IgE 對此病患的一般體液免疫篩檢幫助有限。\n- D. 錯誤。血中第三與第四補體（serum C3 and C4）缺乏雖會增加有莢膜細菌的感染機率，但原發性補體缺乏極為罕見且常伴隨自體免疫疾病（如 SLE）。相較之下，抗體缺乏症的盛行率遠高於補體缺乏，故首選篩檢仍為血清免疫球蛋白定量。\n\n【核心考點】\n反覆發生有莢膜細菌（如流感嗜血桿菌）引起的呼吸道感染與支氣管擴張，提示體液免疫（抗體）缺陷。篩檢的第一步是檢測血清免疫球蛋白定量（IgG, IgA, IgM）。",
        "key_point": "反覆發生有莢膜細菌引起的竇肺部感染提示體液免疫缺損，首選篩檢為檢測血清免疫球蛋白濃度。",
        "flashcard_front": "體液免疫缺損 (Humoral Immunodeficiency) / 首選篩檢項目",
        "flashcard_back": "反覆出現有莢膜細菌（如流感嗜血桿菌、肺炎鏈球菌）感染與支氣管擴張時，應首選檢測血清免疫球蛋白（IgG、IgA、IgM）定量。",
        "flashcard_summary": "體液免疫缺損篩檢 -> 反覆莢膜細菌感染者首選檢測血清免疫球蛋白（IgG）。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_033",
        "question_number": 33,
        "explanation": "【題幹解析】\n診斷全身性紅斑狼瘡（SLE）常參考 ACR/EULAR 的分類標準。在此標準中，抗核抗體（ANA）是進入診斷標準的必要入口條件（Entry criterion，敏感度 >95%）；第四補體（C4）降低反映補體系統活化消耗（免疫學標準）；全血球計數（CBC）可用於評估溶血性貧血、白血球減少或血小板減少（血液學標準）。抗 SSA 抗體雖然在部分 SLE 病患中呈陽性，但並未列入 SLE 診斷分類標準中，其主要與乾燥症或新生兒狼瘡相關，因此對確診 SLE 幫助最小。\n\n【選項詳解】\n- A. 錯誤。抗核抗體（ANA）是診斷 SLE 的入門篩檢指標，敏感度極高（>95-98%）。在 2019 EULAR/ACR 標準中，ANA 必須呈陽性（>= 1:80）才能繼續評估其餘分類項目，故對確診幫助極大。\n- B. 錯誤。第四補體（C4）的降低代表補體系統被活化消耗，在 SLE 分類標準中屬於重要的免疫學評分指標，且補體下降常反映疾病活性（特別是狼瘡腎炎），對確診與活性追蹤皆極具價值。\n- C. 錯誤。全血球計數與血球分類（CBC with DC）可評估病患是否具有 SLE 診斷標準中的血液學異常，包括自體免疫性溶血性貧血、白血球減少症（WBC < 4,000/μL）、淋巴球減少症（< 1,000/μL）或血小板減少症（< 100,000/μL）。\n- D. 正確。抗 SSA 抗體（anti-SSA/Ro）雖然在約 30% 的 SLE 病患中呈陽性，但其臨床特異性主要關聯於乾燥症（Sjögren's syndrome）及新生兒狼瘡。在現行的 SLE 分類診斷標準中，並未將 anti-SSA 列為主要的免疫學診斷抗體（主要採用 anti-dsDNA、anti-Sm 及抗磷脂抗體），因此對確診 SLE 的直接幫助最小。\n\n【核心考點】\n在 SLE 診斷標準中，ANA 是必備篩檢入口，低補體（C3/C4）與血球減少是核心指標；抗 SSA 抗體主要與乾燥症及新生兒狼瘡相關，在 SLE 分類標準中非主要診斷抗體，對確診 SLE 的直接診斷權重最小。",
        "key_point": "在 SLE 診斷標準中，ANA 是必備篩檢入口，低補體（C3/C4）與血球減少是核心指標；抗 SSA 抗體對確診 SLE 的直接特異性與診斷權重最低。",
        "flashcard_front": "全身性紅斑性狼瘡 (SLE) / 診斷標準中抗 SSA 抗體之角色",
        "flashcard_back": "抗 SSA (Ro) 抗體主要與乾燥症及新生兒狼瘡相關，在 SLE 分類標準中非主要診斷抗體，對確診 SLE 的直接診斷權重最小。",
        "flashcard_summary": "SLE診斷指標 -> ANA、低補體及血球低下為核心標準，抗SSA抗體診斷權重最小。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_034",
        "question_number": 34,
        "explanation": "【題幹解析】\n該40歲女性有顯著的多發癌症家族史（包含乳癌、淋巴癌、結腸癌），雖然其姑媽（父系）的 BRCA-1 和 BRCA-2 檢測為陰性，但這僅排除 BRCA-1/2 的突變。遺傳性乳癌及其他遺傳性癌症綜合症（如 Li-Fraumeni 症候群、Lynch 症候群）還可能與許多其他抑癌基因（如 TP53, PTEN, PALB2, CHEK2, ATM 等）突變相關，因此應考慮進行 BRCA-1 及 BRCA-2 以外的基因檢測。\n\n【選項詳解】\n- A. 錯誤。雖然兩位姑媽（父系親屬）的 BRCA-1/2 基因檢測為陰性，但相關的癌症易感基因突變仍有可能是從父親那邊遺傳過來（如父親患有淋巴癌，堂兄患有結腸癌，暗示可能存在其他抑癌基因的突變）。遺傳性癌症基因可經由父系或母系雙方遺傳。\n- B. 錯誤。即使是遺傳性乳癌高危險群，常規的乳癌篩檢推薦每年接受乳房磁振造影（MRI）與乳房攝影（mammography）檢查。正子攝影（PET scan）具有高輻射劑量且對無症狀早期乳癌的篩檢敏感度不足，不用於常規篩檢。\n- C. 正確。遺傳性乳癌與卵巢癌綜合症除了 BRCA-1 和 BRCA-2 之外，還與 TP53（Li-Fraumeni 症候群）、PTEN（Cowden 症候群）、PALB2、ATM、CHEK2 等多個基因突變相關。當家族中存在多發癌症且 BRCA1/2 為陰性時，應考慮使用多基因面板（multi-gene panel）進行更廣泛的篩檢。\n- D. 錯誤。預防乳癌的化學預防藥物，如選擇性雌激素受體調節劑（SERM，如 tamoxifen）或芳香環轉化酶抑制劑（AI，如 exemestane），雖可用於降低高風險女性的乳癌風險，但芳香環轉化酶抑制劑主要建議用於「停經後」女性。本病患僅 40 歲，仍處於停經前，不適合首選 AI。\n\n【核心考點】\n乳癌及其他遺傳性癌症的基因諮詢中，單純 BRCA-1/2 陰性不能完全排除其他抑癌基因突變（如 TP53, PTEN, PALB2 等）。對於多發癌症家族史者，應考慮擴展多基因面板（multi-gene panel）檢測。停經前女性預防乳癌化學預防藥物首選為 SERM (如 Tamoxifen)，而非 AI (Aromatase inhibitors)。",
        "key_point": "乳癌家族中 BRCA-1/2 陰性不能排除其他遺傳性癌症基因（如 TP53, PTEN, PALB2）突變，應考慮擴展多基因面板（multi-gene panel）檢測。",
        "flashcard_front": "遺傳性乳癌諮詢 / BRCA-1/2 陰性之意義",
        "flashcard_back": "家族中BRCA-1/2檢測陰性仍無法排除其他高/中外顯率抑癌基因（如TP53、PTEN、PALB2）突變，應考慮進行多基因面板檢測。",
        "flashcard_summary": "遺傳性乳癌篩檢 -> BRCA陰性且有顯著家族史者，應考慮多基因面板（multi-gene panel）檢測。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_035",
        "question_number": 35,
        "explanation": "【題幹解析】\nEGFR（HER1）與 HER2 皆屬於受體酪胺酸激酶 ErbB 家族，其過度表達或突變主要見於「上皮細胞」來源的惡性腫瘤（carcinoma）。例如肺腺癌常有 EGFR 突變，結腸癌可使用抗 EGFR 單株抗體，乳癌常有 HER2 擴增。然而，腸平滑肌惡性肉瘤（leiomyosarcoma）是來自「間葉組織（mesenchymal tissue）」的惡性肉瘤（sarcoma），其增殖機轉與 EGFR/HER2 通路無關，因此不適用此類標靶治療。\n\n【選項詳解】\n- A. 錯誤。大腸直腸癌（結腸癌）常使用抗 EGFR 單株抗體（如 Cetuximab、Panitumumab）進行標靶治療，前提是腫瘤基因檢測為 KRAS/NRAS/BRAF 野生型（wild-type）。\n- B. 錯誤。非小細胞肺癌（特別是肺腺癌）中，EGFR 突變是非常常見的驅動突變，第一線治療常使用小分子 EGFR 酪胺酸激酶抑制劑（EGFR TKI，如 Gefitinib、Afatinib、Osimertinib）。\n- C. 正確。腸平滑肌惡性肉瘤（intestinal leiomyosarcoma）屬於軟組織肉瘤（soft tissue sarcoma），源於間葉組織（非上皮組織），其增殖與轉移不依賴 EGFR 或 HER2 信號通路，臨床上 EGFR 相關標靶治療對其無療效。\n- D. 錯誤。乳癌中約有 15-20% 屬於 HER2 陽性（HER2 為 EGFR 家族成員，即 ErbB2），臨床上會使用抗 HER2 單株抗體（如 Trastuzumab, Pertuzumab）或抗體藥物複合體（ADC，如 T-DM1, T-DXd）進行標靶治療。\n\n【核心考點】\nEGFR (HER1) 與 HER2 標靶藥物主要應用於「上皮來源」的惡性腫瘤（如肺腺癌、結腸癌、乳癌）。間葉組織來源的肉瘤（如平滑肌肉瘤）不適用此類標靶治療。",
        "key_point": "EGFR (HER1) 與 HER2 標靶藥物主要應用於上皮細胞來源的惡性腫瘤，間葉組織來源的肉瘤（如平滑肌肉瘤）不適用此類治療。",
        "flashcard_front": "EGFR/HER2 標靶治療 / 肉瘤 (Sarcoma) 之適用性",
        "flashcard_back": "EGFR與HER2標靶主要用於上皮源性癌症（如肺癌、結腸癌、乳癌），間葉組織源的肉瘤（如平滑肌肉瘤）不依賴此通路，故不適用。",
        "flashcard_summary": "EGFR標靶適應症 -> 適用於上皮源性惡性腫瘤，間葉組織來源之肉瘤不適用。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_036",
        "question_number": 36,
        "explanation": "【題幹解析】\n標靶治療藥物 Imatinib（商品名 Gleevec）是歷史上第一個研發成功的小分子酪胺酸激酶抑制劑（TKI）。它主要作用於 Bcr-Abl 融合蛋白，該蛋白是由於第9號與第22號染色體易位（費城染色體，Philadelphia chromosome）所產生的異常融合激酶，為慢性骨髓性白血病（CML）的核心致病機轉。Imatinib 同時還能抑制 c-Kit 與 PDGFR。\n\n【選項詳解】\n- A. 正確。Imatinib 主要特異性抑制費城染色體產生的 Bcr-Abl 融合蛋白之酪胺酸激酶活性，阻斷下游的異常增殖信號，因此成為治療慢性骨髓性白血病（CML）的一線藥物。此外，它也能抑制 c-Kit，故常用於治療胃腸道基質瘤（GIST）。\n- B. 錯誤。PML-RARα 是第15號與第17號染色體易位產生的融合蛋白，見於急性前骨髓性白血病（APL，AML-M3）。其標靶治療藥物主要是全反式維甲酸（ATRA）與三氧化二砷（ATO），而非 imatinib。\n- C. 錯誤。NF-κB 是一種調控免疫與發炎反應的轉錄因子。雖然在多種癌症中異常活化，但 Imatinib 並不是 NF-κB 的抑制劑（臨床上有些蛋白酶體抑制劑如 Bortezomib 會間接影響 NF-κB 通路）。\n- D. 錯誤。EGFRα（或一般指 EGFR）的抑制劑包括 gefitinib、erlotinib、afatinib、osimertinib 等小分子 TKI，以及 cetuximab 等單株抗體。Imatinib 並不抑制 EGFR。\n\n【核心考點】\nImatinib (Gleevec) 是針對 Bcr-Abl 融合蛋白的酪胺酸激酶抑制劑，是費城染色體陽性 CML 的首選藥物；它同時也能抑制 c-Kit，可用於治療胃腸道基質瘤 (GIST)。",
        "key_point": "標靶藥物 Imatinib 是針對 Bcr-Abl 融合蛋白的酪胺酸激酶抑制劑，是治療 CML 的一線藥物，同時能抑制 c-Kit 用於治療 GIST。",
        "flashcard_front": "Imatinib (基利克) / 主要作用標靶",
        "flashcard_back": "Imatinib為酪胺酸激酶抑制劑，主要抑制費城染色體產生的Bcr-Abl融合蛋白（用於CML），以及c-Kit受體（用於GIST）。",
        "flashcard_summary": "Imatinib作用靶點 -> 抑制Bcr-Abl（治療CML）與c-Kit（治療GIST）。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_037",
        "question_number": 37,
        "explanation": "【題幹解析】\n狼瘡抗凝血因子（Lupus anticoagulant, LA）是一種抗磷脂抗體（antiphospholipid antibody）。雖然在試管內（in vitro）它會干擾磷脂質，導致以磷脂質為基礎的凝血時間（如 aPTT）延長；但在體內（in vivo），它實際上會促進血小板活化與凝血反應，引發高凝狀態（易造成動靜脈血栓、流產，而「非」出血傾向）。當病患的 aPTT 延長時，進行混合試驗（Mixing test，將患者血漿與正常血漿 1:1 混合）：若是凝血因子缺乏，補入正常血漿後 aPTT 會被矯正至正常；但因 LA 是一種「抗體/抑制物（inhibitor）」，它會繼續中和正常血漿中的磷脂質與因子，因此混合試驗中 aPTT「不會」變為正常（即無法被矯正）。此外，LA 也常見於非 SLE 患者（如原發性抗磷脂抗體症候群），並會與 VDRL 試劑中的心脂質（cardiolipin）發生交叉反應，導致梅毒血清試驗偽陽性。\n\n【選項詳解】\n- A. 錯誤。狼瘡抗凝血因子（LA）在體內的作用是促進血栓形成（Prothrombotic），因此病患臨床上主要表現為血管栓塞或習慣性流產，通常沒有出血傾向，此敘述正確。\n- B. 正確。LA 會與試劑中的磷脂結合而使體外 aPTT 延長。在混合試驗（Mixing study）中，由於 LA 是一種循環抑制物（circulating inhibitor/antibody），會中和混合進來的正常凝血因子/磷脂，因此 aPTT 仍會維持延長，無法被矯正（corrected）至正常範圍。故「會變為正常」的描述是錯誤的。\n- C. 錯誤。LA 不僅見於全身性紅斑性狼瘡（SLE）患者，也常見於「原發性抗磷脂抗體症候群（Primary Antiphospholipid Syndrome）」，或因藥物、感染所誘發的短暫陽性，因此非 SLE 患者也可能出現，此敘述正確。\n- D. 錯誤。抗磷脂抗體（包括 LA 與抗心脂抗體 anticardiolipin antibody）會與梅毒篩檢試劑（如 VDRL、RPR）中的心脂質抗原產生交叉反應，導致梅毒血清試驗呈現「生物性偽陽性」，此敘述正確。\n\n【核心考點】\n狼瘡抗凝血因子 (LA) 在體內會促進血栓，但在體外會導致 aPTT 延長。由於 LA 屬於循環抑制物 (inhibitor)，其引起的 aPTT 延長無法藉由混合試驗 (mixing study) 被矯正至正常。同時，它也常導致梅毒檢驗 (VDRL/RPR) 出現偽陽性。",
        "key_point": "狼瘡抗凝血因子（LA）是循環抑制物而非因子缺乏，故其引起的 aPTT 延長在混合試驗（mixing study）中無法被矯正至正常。",
        "flashcard_front": "狼瘡抗凝血因子 (LA) / 混合試驗 (Mixing Test) 反應",
        "flashcard_back": "LA屬於循環磷脂結合抗體（抑制物），在混合正常血漿的試驗中，無法被正常因子稀釋矯正，aPTT仍會維持延長。",
        "flashcard_summary": "狼瘡抗凝因子實驗室特徵 -> 體外aPTT延長且混合試驗無法矯正，體內則促血栓。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_038",
        "question_number": 38,
        "explanation": "【題幹解析】\n這名孕婦有月經量多、姐姐產後大出血的家族史，血液檢查顯示：血小板數量正常（275,000/μL），但出血時間（Bleeding time, BT）延長至 14 分（反映血小板黏附功能異常）；PT 正常（外在與共同路徑正常），但 aPTT 延長至 44 秒（內生性路徑異常）。臨床上，同時伴隨「血小板計數正常、出血時間延長、aPTT延長」的遺傳性出血疾病，最典型就是類血友病（von Willebrand disease, vWD）。這是因為 von Willebrand factor (vWF) 負責血小板與內皮細胞的黏附（vWF 缺乏導致 BT 延長），同時 vWF 也是第八因子（Factor VIII）的載體蛋白以穩定第八因子（vWF 缺乏導致第八因子濃度下降，進而使 aPTT 延長）。\n\n【選項詳解】\n- A. 錯誤。A 型血友病（Hemophilia A）是 X 染色體隱性遺傳疾病，主要發生在男性，其病原為第八凝血因子（Factor VIII）缺乏。血友病會導致 aPTT 延長，但其「出血時間（Bleeding time, BT）」與血小板功能正常，且典型臨床症狀為深部關節或肌肉出血，而非皮膚黏膜或月經出血。\n- B. 正確。類血友病（vWD）為最常見的遺傳性出血疾病，通常為體染色體顯性遺傳。vWF 的功能是協助血小板黏附至受損血管壁，並保護血中第八因子。缺乏 vWF 會同時導致血小板功能受損（表現為 bleeding time 延長、皮膚黏膜出血如月經量多）及第八因子減少（表現為 aPTT 延長），但血小板數量正常。\n- C. 錯誤。慢性肝炎（chronic hepatitis）若造成凝血功能異常，主要是因為肝臟合成凝血因子能力下降，通常會先引起「PT 延長」（因為第七因子半衰期最短，最先受影響），且常伴隨脾臟腫大導致的血小板低下，與本題 PT 正常、血小板正常的實驗室數據不符。\n- D. 錯誤。尿毒症（uremia）會因為尿毒素累積干擾血小板功能，導致出血時間（Bleeding time）延長，但尿毒症本身不會直接引起 aPTT 延長，且病患並無腎臟病病史，30 歲孕婦若有嚴重尿毒症，臨床上會有顯著的腎功能衰竭症狀，與本題情境不符。\n\n【核心考點】\n類血友病 (vWD) 是最常見的體染色體遺傳出血疾病，其特徵是血小板數量正常，但出血時間 (BT) 延長（vWF 媒介血小板黏附受阻）且 aPTT 延長（vWF 缺乏導致第八因子不穩定）。",
        "key_point": "類血友病（vWD）是因 vWF 缺乏導致血小板黏附功能異常（BT延長）及第八因子不穩定（aPTT延長），但血小板數量與 PT 正常。",
        "flashcard_front": "類血友病 (vWD) / 經典實驗室檢查特徵",
        "flashcard_back": "表現為血小板數量正常，但出血時間（BT）延長（反映血小板功能受損）以及aPTT延長（反映第八因子濃度低下），PT則維持正常。",
        "flashcard_summary": "類血友病實驗室診斷 -> 血小板數正常，出血時間(BT)與aPTT同時延長。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_039",
        "question_number": 39,
        "explanation": "【題幹解析】\n原發性肺癌（特別是位於肺尖的 Pancoast tumor）局部擴散時會侵犯周圍的神經結構。若侵犯「頸部交感神經節（星狀神經節 stellate ganglion）」，會導致 Horner 氏症候群；若侵犯「臂神經叢（C8、T1、T2）」，則會導致 Pancoast 症候群。而膈神經（phrenic nerve, C3-C5）受壓迫或侵犯會導致「橫膈膜麻痺（diaphragmatic paralysis）」，表現為患側橫膈上升及呼吸困難，與 Horner 氏症候群無關。\n\n【選項詳解】\n- A. 正確。Horner 氏症候群是由於「頸部交感神經鏈（特別是星狀神經節 stellate ganglion）」受到腫瘤侵犯或壓迫所致，並非由膈神經（phrenic nerve）麻痺引起。膈神經麻痺會導致同側橫膈上升及呼吸困難，兩者為完全不同的神經路徑。因此本敘述錯誤，為本題應選答案。\n- B. 錯誤。Horner 氏症候群的典型臨床四聯徵（tetrad）包括眼皮下垂（ptosis，瞼板肌無力）、瞳孔縮小（miosis，瞳孔放大肌無力）、無汗症（anhidrosis，交感泌汗受阻）及眼球陷沒（enophthalmos，因眼眶肌張力減退），此敘述正確。\n- C. 錯誤。Pancoast 症候群（又稱肺尖腫瘤症候群）是指肺癌長在肺尖（sulcus tumor）局部擴散，侵犯臂神經叢的下幹（主要是第8頸神經 C8、第1胸神經 T1 及第2胸神經 T2），此敘述正確。\n- D. 錯誤。由於 Pancoast 腫瘤壓迫 C8、T1 臂神經叢，此處神經支配手臂的尺側（ulnar side），因此典型症狀為同側肩膀劇烈疼痛，並向手臂內側（尺骨側）及無名指、小指放射，此敘述正確。\n\n【核心考點】\nHorner 氏症候群是因「交感神經鏈」受侵犯所致，表現為 miosis, ptosis, anhidrosis；Pancoast 症候群則是因肺尖癌壓迫「臂神經叢下幹 (C8-T2)」，導致肩痛並放射至手臂尺側。膈神經 (C3-C5) 麻痺則會造成橫膈提升而非 Horner 氏症候群。",
        "key_point": "肺癌局部擴散侵犯頸交感神經鏈會導致 Horner 氏症候群；侵犯臂神經叢下幹（C8-T2）會導致 Pancoast 症候群。膈神經麻痺則導致橫膈上升。",
        "flashcard_front": "肺癌局部擴散 / Horner 氏症候群 vs 膈神經麻痺",
        "flashcard_back": "Horner氏症候群是因腫瘤侵犯「交感神經鏈（星狀神經節）」所致。膈神經（phrenic nerve）受損會導致同側橫膈上升，兩者路徑不同。",
        "flashcard_summary": "肺部腫瘤神經壓迫 -> 交感神經鏈受損導致Horner氏症候群，膈神經受損導致橫膈上升。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    },
    {
        "question_id": "110-2_medicine-3_040",
        "question_number": 40,
        "explanation": "【題幹解析】\n膀胱癌（絕大多數為尿路上皮癌 urothelial carcinoma）的臨床特點是多發性與易復發。流行病學統計顯示，在初次診斷膀胱癌的病患中，約有 70% 到 80% 的患者屬於「非肌肉侵犯性膀胱癌（Non-muscle invasive bladder cancer, NMIBC）」，也就是臨床上所稱的表淺（superficial）型（包括 Ta, T1, Tis）。這類癌症通常可先經由尿道膀胱腫瘤切除術（TURBT）配合膀胱內藥物灌注治療，但極易復發。而初診斷即為肌肉侵犯型或轉移型者僅佔少數。\n\n【選項詳解】\n- A. 正確。初診斷膀胱癌時，約有 70-80% 的病例為表淺型（即非肌肉侵犯型，侷限在黏膜 Ta/Tis 或黏膜下層 T1）。這類腫瘤通常預後較佳，但復發率高。\n- B. 錯誤。平滑肌侵犯型（muscle-invasive，期別為 T2 以上）在初診斷時約佔 20-30%。此類型需要進行更具侵襲性的治療，例如根治性膀胱切除術（radical cystectomy）或全身性化學治療，並非最常見的初診斷期別。\n- C. 錯誤。轉移型（metastatic）膀胱癌在初診斷時非常罕見，比例通常小於 5-10%。雖然肺部是膀胱癌常見的遠端轉移部位之一，但絕非初次診斷時最常見的期別。\n- D. 錯誤。轉移至肝臟同樣屬於晚期轉移型（Stage IV），在初次確診膀胱癌的病患中僅佔極低比例，不符合最常見期別的流行病學分佈。\n\n【核心考點】\n初次診斷膀胱癌時，最常見的期別為非肌肉侵犯型 / 表淺型 (Non-muscle invasive / superficial bladder cancer，約佔 70-80%)，其預後較好但復發率高。",
        "key_point": "初次診斷膀胱癌時，最常見的期別為表淺型（非肌肉侵犯性膀胱癌，約佔 70-80%），其預後較佳但復發率高。",
        "flashcard_front": "膀胱癌 / 初次診斷最常見之臨床期別",
        "flashcard_back": "初診斷膀胱癌時最常見的是表淺型（非肌肉侵犯型，侷限於黏膜或黏膜下層），約占所有病例的 70-80%。",
        "flashcard_summary": "膀胱癌臨床期別 -> 初次診斷最常見為表淺型（非肌肉侵犯型，占70-80%）。",
        "review_status": "ai_generated",
        "explanation_model": "gemini-2.5-pro",
        "explanation_generated_at": "2026-07-13T19:20:47+08:00",
        "manual_review_notes": []
    }
]

output_data = {
    "source_file": "public/data/exams/110-2/medicine-3.json",
    "dataset_id": "110-2_medicine-3",
    "range": { "start": 31, "end": 40 },
    "updates": updates
}

output_path = r"d:\Antigravity\med_exam_public\scratch\rewrite_updates\110-2_medicine-3\q031-q040.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print("SUCCESS")
