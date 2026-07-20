import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/108-1/medicine-2.json"
DATASET_ID = "108-1_medicine-2"
OUT_DIR = Path("scratch/rewrite_updates/108-1_medicine-2_selected")
GENERATED_AT = "2026-07-20T00:00:00+08:00"


BATCHES = [
    [41, 42, 43, 44, 45, 46, 47, 49, 50, 51],
    [52, 53, 54, 55, 56, 57, 58, 59, 60, 61],
    [62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
    [72, 73, 75, 76, 77, 78, 79, 80, 81, 82],
    [84, 85, 86, 88, 89, 91, 93, 94, 95, 98],
    [99, 100],
]


ENTRIES = {
    41: {
        "stem": "本題考研究設計。暴露與疾病資料都來自鄉鎮市區層級，缺少個人生活型態等個體資料，因此是在比較群體資料，而不是追蹤或回溯個別病人。",
        "core": "生態學研究（ecological study）以群體為分析單位，適合看地區差異與提出假說；缺點是不能直接推論到個人層級，容易有 ecological fallacy。",
        "reasons": {
            "A": "個案報告是描述單一或少數病例的臨床現象，本題沒有個別病例描述。",
            "B": "生態學研究使用地區空污與地區癌症發生率等群體資料，正符合題幹。",
            "C": "病例對照研究要先依是否罹病分組，再回溯個人暴露史；本題沒有個人層級病例與對照。",
            "D": "世代研究需依暴露狀態追蹤個人未來是否發病；本題不是個人追蹤。",
        },
    },
    42: {
        "stem": "本題問酸雨來源。酸雨主要由硫氧化物與氮氧化物在大氣中形成硫酸、硝酸後造成。",
        "core": "酸雨的高頻來源是 SOx 與 NOx；一氧化碳與臭氧雖是重要空污指標，但不是酸雨形成的主要前驅物。",
        "reasons": {
            "A": "一氧化碳與臭氧不屬酸雨主要前驅物，所以 1、2 不對。",
            "B": "此組包含一氧化碳與臭氧，混入非主要酸雨來源。",
            "C": "硫氧化物與氮氧化物會轉為強酸性物質，僅 3、4 正確。",
            "D": "臭氧不是酸雨效應的主要成因，因此 2 不應列入。",
        },
    },
    43: {
        "stem": "本題考致癌物與非致癌物風險評估的差別。非致癌毒性通常假設有閾值，低於某劑量時不會產生可觀察不良效應。",
        "core": "非致癌風險評估重點是閾值、NOAEL/LOAEL、參考劑量與危害商數；致癌風險才常用無閾值線性外推、斜率因子與 10^-6 風險比較。",
        "reasons": {
            "A": "非致癌物多採閾值假設，這是本題要選的描述。",
            "B": "斜率因子常用於致癌風險線性外推，不是非致癌物的典型做法。",
            "C": "10^-6 可接受風險比較屬致癌風險表達方式，非致癌通常看暴露是否超過參考劑量。",
            "D": "不確定性分析仍然需要，例如種間差異、個體敏感性與資料不足都要納入。",
        },
    },
    44: {
        "stem": "本題直接考登革熱病媒。登革病毒主要由斑蚊傳播，台灣常見考點是埃及斑蚊與白線斑蚊。",
        "core": "登革熱病媒記斑蚊：Aedes aegypti 與 Aedes albopictus；瘧蚊是瘧疾，家蚊常連到日本腦炎等，不要混淆。",
        "reasons": {
            "A": "熱帶家蚊與白腹叢蚊不是登革熱的標準病媒組合。",
            "B": "埃及斑蚊與白線斑蚊都是登革熱重要病媒，符合題幹。",
            "C": "小黑蚊造成叮咬困擾，白腹叢蚊也不是登革熱主要標準答案。",
            "D": "中華瘧蚊與瘧疾較相關，熱帶家蚊不是登革熱主要病媒。",
        },
    },
    45: {
        "stem": "本題考八小時時量平均濃度。每小時前 10 分鐘 60 ppm、後 50 分鐘 0 ppm，整體暴露比例是 10/60。",
        "core": "TWA = 總暴露量除以總時間。本題每小時平均為 60 x 10/60 = 10 ppm，八小時重複同樣模式仍是 10 ppm。",
        "reasons": {
            "A": "60 ppm 只暴露每小時 10 分鐘，平均後為 10 ppm，正確。",
            "B": "15 ppm 代表暴露比例或時間權重計算過高。",
            "C": "20 ppm 等於把暴露時間估為每小時 20 分鐘，與題幹不符。",
            "D": "60 ppm 是暴露時段的瞬間濃度，不是八小時平均濃度。",
        },
    },
    46: {
        "stem": "本題考職業暴露與癌症。苯是典型造血系統毒物，長期暴露與白血病風險增加相關。",
        "core": "苯暴露要想到骨髓抑制、再生不良性貧血與白血病，尤其急性骨髓性白血病風險。",
        "reasons": {
            "A": "苯會傷害骨髓與造血系統，最典型癌症是血癌。",
            "B": "肝癌常與病毒性肝炎、黃麴毒素、酒精等相關，不是苯的最典型考點。",
            "C": "腎癌可與部分化學或吸菸風險相關，但苯首要考造血癌症。",
            "D": "皮膚癌較常連到紫外線、砷或瀝青焦油等，不是苯長期暴露的代表癌症。",
        },
    },
    47: {
        "stem": "本題考台灣成人肥胖 BMI 切點。台灣常用過重為 BMI >= 24，肥胖為 BMI >= 27。",
        "core": "台灣成人 BMI 分類：24 以上為過重，27 以上為肥胖；這和部分國際資料以 30 為肥胖不同。",
        "reasons": {
            "A": "25 接近某些國際過重切點，但不是台灣成人肥胖切點。",
            "B": "BMI 27 是我國成人肥胖定義的切點。",
            "C": "29 高於台灣肥胖門檻，不是定義切點。",
            "D": "31 更接近較嚴重肥胖，不是本題問的成人肥胖起始點。",
        },
    },
    49: {
        "stem": "本題問醫療費用成長率的主要推力。人口結構、所得提高與醫療科技進步都會直接推升醫療需求或單價。",
        "core": "醫療支出成長常由人口老化、所得增加、科技進步與保險支付誘因推動；資訊不對稱重要，但較像醫療市場特性，不是支出成長率最直接因素。",
        "reasons": {
            "A": "人口老化增加慢性病與照護需求，與費用成長高度相關。",
            "B": "所得增加會提高醫療需求與願付能力，常推升支出。",
            "C": "新醫療科技通常帶來新檢查、新治療與較高成本，是費用成長主因之一。",
            "D": "醫病資訊不對稱會影響供需與代理決策，但相較前三者，與整體費用成長率的直接關聯較小。",
        },
    },
    50: {
        "stem": "本題考原廠新藥昂貴的成本結構。新藥上市前最大負擔通常是研發、臨床試驗與專利壟斷期間的定價能力。",
        "core": "原廠新藥貴主要因研發風險、臨床試驗成本與專利保護；單純生產製造成本通常不是最高或最關鍵的成本來源。",
        "reasons": {
            "A": "研究及發展費用包含大量失敗候選藥物成本，是新藥價格的重要來源。",
            "B": "專利保護減少競爭，使原廠能在保護期內維持較高價格。",
            "C": "臨床試驗需長時間、大規模受試者與法規審查，成本很高。",
            "D": "藥品量產製造成本相對研發與試驗通常較小，因此影響較小。",
        },
    },
    51: {
        "stem": "本題問 metronidazole 不適合治療哪一類感染。它主要涵蓋厭氧菌與部分原蟲，不是淋病球菌用藥。",
        "core": "Metronidazole 記厭氧菌、Trichomonas、Entamoeba、Giardia；淋病球菌是 Neisseria gonorrhoeae，治療以 ceftriaxone 等為主。",
        "reasons": {
            "A": "Metronidazole 對厭氧菌感染有用途，早期也常被列為 C. difficile 治療考點。",
            "B": "陰道滴蟲是 metronidazole 的典型適應症。",
            "C": "淋病球菌不是 metronidazole 的治療範圍，因此是本題答案。",
            "D": "阿米巴性結腸炎可使用 metronidazole 治療侵襲性病灶。",
        },
    },
    52: {
        "stem": "本題考 CMF 化療藥物分類。Methotrexate 與 5-fluorouracil 都干擾核酸合成，屬抗代謝藥物。",
        "core": "Cyclophosphamide 是烷化劑；methotrexate 抑制 dihydrofolate reductase；5-FU 抑制 thymidylate synthase，後兩者歸類為 anti-metabolites。",
        "reasons": {
            "A": "Topoisomerase II 抑制劑代表藥如 etoposide、doxorubicin，不是 cyclophosphamide 或 methotrexate 的主要機轉。",
            "B": "抑制有絲分裂是 vinca alkaloids 或 taxanes 類考點，不是 methotrexate 與 5-FU。",
            "C": "Methotrexate 與 5-FU 都抑制 DNA 合成所需代謝路徑，屬抗代謝藥物。",
            "D": "Cyclophosphamide 是 DNA alkylating agent，但 5-FU 是抗代謝藥，不是烷化劑。",
        },
    },
    53: {
        "stem": "本題問哪個不是抗血小板凝集藥。Heparin 主要增強 antithrombin，屬抗凝血藥，不是抗血小板藥。",
        "core": "抗血小板藥影響 platelet activation/aggregation；heparin 影響凝血因子，考試常用來區分 antiplatelet 與 anticoagulant。",
        "reasons": {
            "A": "Dipyridamole 會增加血小板內 cAMP，抑制血小板凝集。",
            "B": "Aspirin 抑制 COX、降低 TXA2，是典型抗血小板藥。",
            "C": "Heparin 作用在 antithrombin 與凝血因子，不是血小板凝集拮抗劑。",
            "D": "Ticlopidine 抑制 ADP 受體路徑，屬抗血小板藥。",
        },
    },
    54: {
        "stem": "本題問 bromocriptine 敘述何者錯誤。Bromocriptine 是 dopamine receptor agonist，可抑制 prolactin，也可用於巴金森氏症。",
        "core": "Bromocriptine 可治高泌乳素血症與部分巴金森症；肢端肥大症主要藥物是 somatostatin analog 如 octreotide，不能說 bromocriptine 透過增加 somatostatin 分泌而有效。",
        "reasons": {
            "A": "Dopamine 會抑制泌乳素分泌，所以 bromocriptine 可治高泌乳素血症。",
            "B": "作為 dopamine agonist，它可改善巴金森氏症的 dopaminergic 活性不足。",
            "C": "肢端肥大症主要靠 somatostatin analog 抑制 GH；此選項把機轉說成增加 somatostatin 分泌，並非 bromocriptine 的正確描述。",
            "D": "抑制 prolactin 可減少泌乳，故可改善產後乳房腫脹或泌乳過多。",
        },
    },
    55: {
        "stem": "本題問 vasopressin 何者錯誤。Vasopressin 又稱 ADH，重點是保水與血管收縮，不是促進利尿。",
        "core": "Vasopressin 經 V2 受體增加集合管水分再吸收，經 V1 受體收縮血管；它是抗利尿激素，錯誤敘述通常會把它講成利尿。",
        "reasons": {
            "A": "Vasopressin 由後葉釋放，具血管收縮作用，描述可接受。",
            "B": "胜肽類藥物在腸胃道易被分解，口服效果差。",
            "C": "垂體性尿崩症缺乏 ADH，可用 vasopressin 或 desmopressin 類藥治療。",
            "D": "Vasopressin 是抗利尿，會增加水分再吸收；說它利尿並造成水分流失是錯的。",
        },
    },
    56: {
        "stem": "本題考高血鈣治療。先用生理食鹽水擴充體液，再用 loop diuretic 促進鈣排泄。",
        "core": "高血鈣急性處理可用 normal saline 加 furosemide；thiazide 會增加鈣再吸收，反而不適合。",
        "reasons": {
            "A": "Furosemide 抑制 thick ascending limb 的 Na-K-2Cl，降低鈣再吸收，可增加尿鈣排出。",
            "B": "Hydrochlorothiazide 會增加遠端小管鈣再吸收，可能加重高血鈣。",
            "C": "Amiloride 是保鉀利尿劑，對急性降血鈣不是最佳選擇。",
            "D": "Conivaptan 是 vasopressin receptor antagonist，主要處理低鈉血症相關水分問題。",
        },
    },
    57: {
        "stem": "本題問哪個抗心律不整藥典型副作用是類狼瘡症狀。Procainamide 是高頻藥物性 lupus 考點。",
        "core": "Drug-induced lupus 常記 procainamide、hydralazine、isoniazid 等；抗心律不整藥中以 procainamide 最典型。",
        "reasons": {
            "A": "Sotalol 是 class III beta-blocking antiarrhythmic，主要擔心 QT 延長與 torsades。",
            "B": "Disopyramide 有抗膽鹼副作用與負性肌力，不是類狼瘡代表。",
            "C": "Amiodarone 典型毒性是肺纖維化、甲狀腺、肝毒性、角膜沉積與皮膚變色。",
            "D": "Procainamide 可造成 drug-induced lupus-like syndrome，是本題答案。",
        },
    },
    58: {
        "stem": "本題考受體與第二傳訊。M2 muscarinic receptor 是 Gi coupled，會抑制 adenylyl cyclase。",
        "core": "M2 走 Gi 抑制 adenylyl cyclase；M3 多走 Gq；beta 受體多走 Gs 活化 adenylyl cyclase。",
        "reasons": {
            "A": "M2 cholinoceptor 透過 Gi 降低 cAMP，會抑制 adenylyl cyclase。",
            "B": "M3 muscarinic receptor 主要透過 Gq 增加 IP3/DAG，不是抑制 adenylyl cyclase。",
            "C": "β1 adrenoceptor 走 Gs，會活化 adenylyl cyclase。",
            "D": "β3 adrenoceptor 也主要走 Gs，提高 cAMP，不是抑制。",
        },
    },
    59: {
        "stem": "本題問 PGI2 致效劑治療肺高壓。Treprostinil 是 prostacyclin analog，可擴張肺血管並抑制血小板凝集。",
        "core": "肺動脈高壓藥物常見三類：prostacyclin analog、endothelin antagonist、PDE5/sGC pathway；treprostinil 屬 PGI2 類。",
        "reasons": {
            "A": "Treprostinil 是 PGI2/prostacyclin 類致效劑，可用於 pulmonary hypertension。",
            "B": "Alprostadil 是 PGE1 類，常考維持 PDA 或勃起功能，不是肺高壓 PGI2 代表。",
            "C": "Misoprostol 是 PGE1 analog，常用於胃保護或產科用途。",
            "D": "Latanoprost 是 PGF2α analog，用於青光眼降低眼壓。",
        },
    },
    60: {
        "stem": "本題問作用於 dopaminergic D2 receptor 的帕金森氏症用藥。Bromocriptine 是 ergot 類 dopamine agonist。",
        "core": "Dopamine agonists 可直接刺激 dopamine receptors；bromocriptine 典型連 D2，pramipexole 常記 D3 偏好，selegiline 是 MAO-B inhibitor。",
        "reasons": {
            "A": "Pramipexole 是 dopamine agonist，但考點常偏 D3 receptor，不是本題指定 D2 的傳統答案。",
            "B": "Bromocriptine 是 D2 receptor agonist，可用於 Parkinsonism。",
            "C": "Flurazepam 是 benzodiazepine 類安眠藥，作用於 GABA_A receptor。",
            "D": "Selegiline 抑制 MAO-B，減少 dopamine 分解，不是直接 D2 receptor agonist。",
        },
    },
    61: {
        "stem": "本題考抗綠膿桿菌 penicillin。Ticarcillin 屬 antipseudomonal penicillins，可與 aminoglycoside 合併治療 Pseudomonas。",
        "core": "Antipseudomonal penicillins 包括 ticarcillin、piperacillin；一般 aminopenicillin 或抗葡萄球菌 penicillin 不等於抗綠膿桿菌。",
        "reasons": {
            "A": "Amoxicillin 是 aminopenicillin，常用呼吸道、腸球菌等，非抗綠膿桿菌代表。",
            "B": "Dicloxacillin 是抗 penicillinase 的抗葡萄球菌 penicillin，不主打 Pseudomonas。",
            "C": "Nafcillin 也屬抗葡萄球菌 penicillin，不是 antipseudomonal penicillin。",
            "D": "Ticarcillin 可涵蓋 P. aeruginosa，並可與 aminoglycoside 併用。",
        },
    },
    62: {
        "stem": "本題問 ceftriaxone 正確敘述。Ceftriaxone 是第三代 cephalosporin，常作淋病球菌感染首選。",
        "core": "Ceftriaxone：第三代 cephalosporin、淋病與腦膜炎常見用藥、部分由膽汁排泄，腎功能不全通常不需像純腎排藥物那樣大幅減量。",
        "reasons": {
            "A": "Ceftriaxone 是 N. gonorrhoeae 感染的標準首選用藥，正確。",
            "B": "它屬第三代 cephalosporin，不是第四代；第四代代表是 cefepime。",
            "C": "Clavulanate 常與 amoxicillin 等 beta-lactam 合併，不是 ceftriaxone 的典型固定併用。",
            "D": "Ceftriaxone 有膽道排泄比例，腎衰竭通常不需一律降到半量。",
        },
    },
    63: {
        "stem": "本題問何者無助於改善貧血。Deferoxamine 是鐵螯合劑，用於鐵過量，不是補鐵或造血治療。",
        "core": "缺鐵可補 oral iron 或 parenteral iron；B12/folate 用於巨球性貧血；deferoxamine 會移除鐵，不能拿來改善缺鐵性貧血。",
        "reasons": {
            "A": "Ferrous fumarate 是口服鐵劑，可治缺鐵性貧血。",
            "B": "Iron dextran 是注射鐵劑，可在特定情況補充鐵。",
            "C": "Deferoxamine 螯合鐵並促進排出，用於鐵中毒或鐵負荷過高，無助於改善貧血。",
            "D": "維生素 B12 與葉酸可治因缺乏造成的巨球性貧血。",
        },
    },
    64: {
        "stem": "本題考子宮內膜異位症藥物。抑制卵巢週期與內膜刺激可減少疼痛，medroxyprogesterone 是可用選項。",
        "core": "Endometriosis 可用 progestins、combined OCP、GnRH agonist 等；本題選肌肉注射 medroxyprogesterone。",
        "reasons": {
            "A": "Flutamide 是 androgen receptor antagonist，主要用於前列腺癌或高雄激素狀態，不是內膜異位常規治療。",
            "B": "Medroxyprogesterone 可抑制內膜增生與卵巢週期，適合治療 endometriosis 疼痛。",
            "C": "Oxandrolone 是 anabolic steroid，臨床用途與子宮內膜異位症不符。",
            "D": "Raloxifene 是 SERM，主要用於骨質疏鬆與乳癌風險議題，不適合作為本題治療。",
        },
    },
    65: {
        "stem": "本題問肢端肥大症除手術外的治療。肢端肥大症多因 GH-secreting pituitary adenoma，somatostatin analog 可抑制 GH 分泌。",
        "core": "Acromegaly 藥物記 octreotide/lanreotide、pegvisomant、部分 dopamine agonist；somatropin 是 GH，會使問題更糟。",
        "reasons": {
            "A": "Desmopressin 是 ADH 類藥，用於中樞性尿崩症或部分止血用途，不治 GH 過多。",
            "B": "Octreotide 是 somatostatin analog，可抑制 GH 分泌，符合肢端肥大症治療。",
            "C": "Leuprolide 是 GnRH agonist，主要用於性腺軸相關疾病，不是 GH 腫瘤治療。",
            "D": "Somatropin 是重組 GH，會增加 GH 作用，與肢端肥大症治療方向相反。",
        },
    },
    66: {
        "stem": "本題問立即停藥會造成反彈性高血壓的降壓藥。Clonidine 是中樞 alpha-2 agonist，突然停藥會交感活性反彈。",
        "core": "Clonidine 長期高劑量不可突然停藥，否則 norepinephrine 釋放反彈增加，可導致 severe rebound hypertension。",
        "reasons": {
            "A": "Clonidine 抑制中樞交感輸出；突然停用會交感活性暴增，可能致命性高血壓。",
            "B": "Nifedipine 是鈣離子通道阻斷劑，停藥不以強烈交感反彈為典型考點。",
            "C": "Hydralazine 是直接血管擴張劑，副作用可有反射性心搏過速與類狼瘡，但非本題立即停藥反彈代表。",
            "D": "Captopril 是 ACE inhibitor，停藥不會造成 clonidine 式交感反彈。",
        },
    },
    67: {
        "stem": "本題問直接作用型 muscarinic agonist 治療口乾。Cevimeline 可刺激 M3 受體，增加唾液分泌。",
        "core": "Sjögren 或放療後口乾可用 pilocarpine、cevimeline；atropine 是拮抗劑，neostigmine 是間接增加 ACh，succinylcholine 是 nicotinic blocker。",
        "reasons": {
            "A": "Atropine 是 muscarinic antagonist，會造成口乾，不是治療口乾。",
            "B": "Cevimeline 是 direct-acting muscarinic agonist，可改善 Sjögren 或放療後 xerostomia。",
            "C": "Neostigmine 是 acetylcholinesterase inhibitor，屬間接作用，不是題幹問的直接致效劑。",
            "D": "Succinylcholine 是 neuromuscular blocker，作用在 nicotinic receptor，不治口乾。",
        },
    },
    68: {
        "stem": "本題問偏頭痛合併噁心嘔吐時的最佳藥物。Sumatriptan 是 5-HT1B/1D agonist，可治療急性 migraine attack。",
        "core": "Migraine 急性治療常用 triptans；sumatriptan 可收縮顱內血管並抑制三叉神經胜肽釋放，較符合典型偏頭痛發作。",
        "reasons": {
            "A": "Acetaminophen 可止痛退燒，但對典型中重度偏頭痛伴噁心嘔吐不是最佳特異性藥物。",
            "B": "Allopurinol 用於高尿酸或痛風預防，與偏頭痛急性治療無關。",
            "C": "Sumatriptan 是 triptan 類，適合急性偏頭痛，故為最佳選擇。",
            "D": "Sulindac 是 NSAID，可止痛消炎，但不是本題偏頭痛特異性最佳選項。",
        },
    },
    69: {
        "stem": "本題問 NK1 receptor antagonist 預防化療或術後噁心嘔吐。Aprepitant 阻斷 substance P 的 NK1 receptor。",
        "core": "Aprepitant/fosaprepitant 是 NK1 antagonist，常與 5-HT3 antagonist、dexamethasone 合併預防化療噁心嘔吐。",
        "reasons": {
            "A": "Riociguat 刺激 soluble guanylate cyclase，用於肺高壓相關適應症，不是止吐 NK1 藥。",
            "B": "Fasudil 是 Rho kinase inhibitor，與化療止吐機轉不符。",
            "C": "Bosentan 是 endothelin receptor antagonist，用於肺動脈高壓。",
            "D": "Aprepitant 拮抗 NK1 receptor，可預防 chemotherapy-induced nausea and vomiting。",
        },
    },
    70: {
        "stem": "本題問作用在腸胃道、減少脂肪吸收的減肥藥。Orlistat 抑制胃腸與胰臟 lipase。",
        "core": "Orlistat 在腸腔內抑制脂肪分解吸收，副作用常是脂肪便與脂溶性維生素吸收下降。",
        "reasons": {
            "A": "Phentermine 是中樞交感促進食慾抑制藥，不是腸胃道脂肪吸收抑制。",
            "B": "Topiramate 用於癲癇、偏頭痛，減重多與中樞食慾相關，不是 lipase inhibitor。",
            "C": "Orlistat 抑制腸胃道 lipase，減少脂肪吸收，符合題幹。",
            "D": "Lorcaserin 是 5-HT2C agonist 類食慾抑制概念，不是腸道脂肪吸收抑制。",
        },
    },
    71: {
        "stem": "本題問 ketamine 的主要麻醉機轉。Ketamine 是 dissociative anesthetic，主要拮抗 NMDA receptor。",
        "core": "Ketamine 抑制 NMDA receptor，可造成解離性麻醉；和 propofol、benzodiazepines、barbiturates 的 GABA_A 作用不同。",
        "reasons": {
            "A": "活化 GABA_A receptor 比較像 propofol、benzodiazepine 或 barbiturate 類方向。",
            "B": "抑制 GABA_A receptor 會增加神經興奮，不是 ketamine 麻醉主機轉。",
            "C": "活化 NMDA receptor 會促進興奮性傳遞，與 ketamine 作用相反。",
            "D": "Ketamine 主要抑制 NMDA receptor，正確。",
        },
    },
    72: {
        "stem": "本題問 levetiracetam 何者錯誤。它結合 SV2A，口服可用，且主要以腎臟排除，不是主要肝代謝。",
        "core": "Levetiracetam：SV2A、影響神經傳遞物質釋放、部分癲癇可用、藥物交互作用少；主要腎排泄是考點。",
        "reasons": {
            "A": "Levetiracetam 有口服劑型，可經口服給藥。",
            "B": "它選擇性結合 synaptic vesicle protein SV2A，這是核心機轉。",
            "C": "透過 SV2A 可影響 glutamate、GABA 等神經傳遞物質釋放，描述可接受。",
            "D": "Levetiracetam 主要經腎臟排泄，並非主要經肝臟代謝，因此此項錯誤。",
        },
    },
    73: {
        "stem": "本題問哪些鎮靜物質可被 flumazenil 拮抗，何者為誤。Flumazenil 是 benzodiazepine receptor antagonist，不能逆轉酒精。",
        "core": "Flumazenil 可拮抗 benzodiazepines，也可對 Z-drugs 的 benzodiazepine receptor 作用有拮抗效果；alcohol 不是其解毒標的。",
        "reasons": {
            "A": "Zolpidem 作用於 GABA_A benzodiazepine receptor complex，可被 flumazenil 拮抗。",
            "B": "Lorazepam 是 benzodiazepine，flumazenil 可拮抗其鎮靜作用。",
            "C": "Alcohol 雖也影響 GABA 等系統，但不是 benzodiazepine receptor agonist，flumazenil 無法作為其拮抗解毒藥。",
            "D": "Alprazolam 是 benzodiazepine，屬 flumazenil 可拮抗的範圍。",
        },
    },
    75: {
        "stem": "本題問放射性銫與鉈中毒解毒。Prussian blue 可在腸道結合 cesium、thallium，阻斷再吸收並促進糞便排出。",
        "core": "Prussian blue 是 radioactive cesium 與 thallium 的重要解毒劑；重金屬螯合劑要依金屬種類分辨。",
        "reasons": {
            "A": "EDTA 常用於鉛等重金屬螯合，不是 137Cs 或 thallium 的標準答案。",
            "B": "Unithiol/DMPS 可用於砷、汞等部分金屬中毒，不是本題首選。",
            "C": "Deferasirox 是鐵螯合劑，用於慢性鐵負荷過高。",
            "D": "Prussian blue 能結合銫與鉈，減少腸肝循環與吸收，是正確答案。",
        },
    },
    76: {
        "stem": "本題描述肺部圓形病灶，內含中性球、壞死細胞與黏稠液，這是化膿性發炎形成的膿瘍。",
        "core": "Abscess 是局部化膿性壞死，內容物以 neutrophils、壞死碎屑與膿液為主；肺部可由細菌感染造成。",
        "reasons": {
            "A": "肥厚性瘢痕是修復後膠原過度沉積，不會以中性球與壞死膿液為主。",
            "B": "膿瘍正是局部含大量中性球、壞死細胞與膿液的病灶。",
            "C": "血腫主要是血液聚積，內容不會以化膿性中性球壞死液為主。",
            "D": "結核典型是乾酪性肉芽腫，細胞組成與題幹膿液描述不同。",
        },
    },
    77: {
        "stem": "本題問懷孕時乳房變化。懷孕受 estrogen、progesterone、prolactin 影響，乳腺小葉與腺泡增生，準備泌乳。",
        "core": "Pregnancy breast change 記 lobular hyperplasia、腺泡發達與分泌功能準備；不是纖維化、鱗狀化生或異生。",
        "reasons": {
            "A": "間質纖維化不是懷孕乳房的主要生理變化。",
            "B": "乳管上皮鱗狀化生屬病理性改變，不是正常妊娠反應。",
            "C": "腺泡細胞異生代表異常分化，不是懷孕下的生理性增生。",
            "D": "小葉增生是懷孕時乳房最典型的生理變化。",
        },
    },
    78: {
        "stem": "本題羊水細胞有兩群細胞：部分正常 46 條，部分多一條 21 號染色體，代表同一個體內有兩種細胞株。",
        "core": "Trisomy 21 是 Down syndrome；若檢體同時有正常細胞與 trisomy 21 細胞，診斷是 mosaic Down syndrome。",
        "reasons": {
            "A": "單純無分離型唐氏症通常所有細胞皆為 trisomy 21，不會同時有正常細胞株。",
            "B": "Edwards syndrome 是 trisomy 18，不是第 21 號染色體多一條。",
            "C": "轉位型愛德華氏症仍與第 18 號染色體相關，且題幹不是轉位描述。",
            "D": "正常細胞與 trisomy 21 細胞並存，最符合鑲嵌型唐氏症候群。",
        },
    },
    79: {
        "stem": "本題考類澱粉沉積的類型與染色。甲狀腺髓質癌可由腫瘤細胞分泌 calcitonin，形成局部 amyloid。",
        "core": "Amyloid 共同特徵是 beta-pleated sheet，Congo red 呈蘋果綠雙折射；medullary thyroid carcinoma 的 amyloid 來自 calcitonin。",
        "reasons": {
            "A": "Alzheimer disease 的 amyloid 主要是 Aβ，不是 AA amyloid。",
            "B": "甲狀腺髓質癌由 C cell 產生 calcitonin，可形成類澱粉沉積，正確。",
            "C": "Congo red 可染多種類澱粉，不限於 AL 輕鏈型。",
            "D": "Congo red 陽性與 beta-pleated sheet 相關，不是 crossed alpha-pleated 結構。",
        },
    },
    80: {
        "stem": "本題問癌症惡體質原因。TNF 又稱 cachectin，可由巨噬細胞與腫瘤細胞產生，促進食慾下降與蛋白脂肪分解。",
        "core": "Cancer cachexia 高頻介質是 TNF、IL-1、IL-6、IFN-gamma 等發炎細胞激素；本題選 TNF 由 macrophages 與 tumor cells 產生。",
        "reasons": {
            "A": "1 與 2 都是 TNF 來源，符合惡體質機轉。",
            "B": "此組包含 IL-10；IL-10 偏抗發炎調節，不是癌症惡體質主要原因。",
            "C": "1 正確，但 4 的 IL-10 produced by tumor cells 不是典型 cachexia 介質。",
            "D": "3、4 都是 IL-10，不是本題惡體質主因。",
        },
    },
    81: {
        "stem": "本題是老年男性心臟 amyloid，Congo red 蘋果綠，且沒有惡性腫瘤、慢性發炎、腎病或神經病變。最符合 senile systemic amyloidosis。",
        "core": "老年人以心臟為主的 amyloid，沒有 AL、AA 或透析相關線索時，常考 transthyretin（ATTR）沉積。",
        "reasons": {
            "A": "免疫球蛋白輕鏈沉積屬 AL amyloidosis，通常要想到 plasma cell dyscrasia；題幹沒有惡性腫瘤線索。",
            "B": "β2-microglobulin 常見於長期血液透析相關 amyloidosis；題幹沒有腎病或透析。",
            "C": "Transthyretin 可造成老年性心臟類澱粉沉積，與題幹排除腫瘤、慢性發炎、腎病與神經病變後的情境相符。",
            "D": "Calcitonin amyloid 典型見於甲狀腺髓質癌，不是本題心肌沉積。",
        },
    },
    82: {
        "stem": "本題問 microangiopathic hemolytic anemia 的組合。碎裂紅血球、血小板低下可見於 TTP、巨大血管瘤造成的 Kasabach-Merritt 現象與 DIC。",
        "core": "Schistocytes 代表紅血球在微血管內被剪切；TTP、DIC、巨大血管瘤可造成血小板消耗與溶血，ITP 通常是孤立血小板低下。",
        "reasons": {
            "A": "1、2 正確，但漏掉 DIC 也會造成微血管性溶血與碎裂紅血球。",
            "B": "1、3 正確，但巨大血管瘤也可造成血小板消耗與溶血。",
            "C": "TTP、巨大血管瘤與 DIC 都可有溶血性貧血、血小板低下與 schistocytes。",
            "D": "此組包含 ITP；ITP 主要是免疫破壞血小板，通常不會有 schistocytes 型溶血。",
        },
    },
    84: {
        "stem": "本題問成年人最常見惡性淋巴瘤。Diffuse large B-cell lymphoma 是成人 non-Hodgkin lymphoma 中最常見類型。",
        "core": "成人最常見惡性淋巴瘤記 DLBCL；它是侵襲性 B 細胞淋巴瘤，可原發或由低度惡性淋巴瘤轉化。",
        "reasons": {
            "A": "瀰漫大 B 細胞淋巴瘤是成人最常見惡性淋巴瘤，正確。",
            "B": "周邊 T 細胞淋巴瘤較少見，不是成人最常見。",
            "C": "退行性大細胞淋巴瘤屬特定 T/null cell lymphoma，發生率不及 DLBCL。",
            "D": "被套細胞淋巴瘤是 B 細胞淋巴瘤，但不是最常見成人惡性淋巴瘤。",
        },
    },
    85: {
        "stem": "本題小孩病毒感染後出現孤立血小板低下、瘀斑，其他血球正常，且類固醇有效，最符合急性免疫性血小板低下紫斑症。",
        "core": "兒童 ITP 常在病毒感染後出現，因抗血小板抗體造成血小板破壞；血紅素與白血球通常正常。",
        "reasons": {
            "A": "抗血小板抗體導致周邊血小板破壞，最符合病毒後 ITP。",
            "B": "骨髓造血不良通常會影響多條血球細胞系，不會只有血小板明顯降低。",
            "C": "GPIIb/IIIa 功能不全是 Glanzmann thrombasthenia，血小板數通常正常但功能異常。",
            "D": "vWF metalloprotease（ADAMTS13）缺乏造成 TTP，會有微血管溶血等表現，不符合本題。",
        },
    },
    86: {
        "stem": "本題用免疫染色判斷上呼吸道腫瘤。Synaptophysin 與 chromogranin 是神經內分泌分化標記，嗅母神經胚細胞癌最符合。",
        "core": "Olfactory neuroblastoma 發生於鼻腔嗅上皮區，具神經內分泌標記；上皮癌或 NUT carcinoma 不以 synaptophysin/chromogranin 作為核心診斷線索。",
        "reasons": {
            "A": "鼻咽上皮細胞癌常與 EBV、上皮性標記相關，不是神經內分泌標記陽性的典型答案。",
            "B": "嗅母神經胚細胞癌具神經分化，常表現 synaptophysin、chromogranin，正確。",
            "C": "喉頭上皮細胞癌多為 squamous cell carcinoma，重點不是神經內分泌抗原。",
            "D": "NUT 中線癌以 NUT rearrangement 與 NUT immunostain 為診斷重點，不是此組標記。",
        },
    },
    88: {
        "stem": "本題長骨複雜性骨折術後數日出現胸痛與呼吸困難，考栓塞併發症；選項中最符合的是肺栓塞。",
        "core": "骨折與術後臥床可造成 venous thromboembolism；長骨骨折也要想到 fat embolism，但本題選項以肺栓塞代表急性呼吸困難。",
        "reasons": {
            "A": "敗血症會有感染、休克或全身發炎線索，題幹重點是骨折術後突發胸痛呼吸困難。",
            "B": "肺栓塞可在手術或骨折後發生，造成胸痛、呼吸困難與低氧，最符合選項。",
            "C": "顱內出血主要造成意識、神經學症狀，不會以胸痛呼吸困難為主。",
            "D": "細菌性肺炎通常有發燒、咳痰、浸潤影等感染線索，題幹更指向栓塞。",
        },
    },
    89: {
        "stem": "本題問旅行者肝炎且孕婦感染死亡率高的病毒。HEV 經糞口傳染，常與污染水源及旅行相關，孕婦感染可很嚴重。",
        "core": "Hepatitis E：糞口傳染、旅行者肝炎、水源污染、孕婦高死亡率，是和 HAV 區分的關鍵。",
        "reasons": {
            "A": "A 型肝炎也經糞口傳染並可見於旅行，但孕婦高死亡率的經典考點是 E 型。",
            "B": "B 型肝炎主要經血液、性接觸與垂直傳染，不是典型旅行者糞口肝炎。",
            "C": "D 型肝炎需依附 HBV 感染，不是旅行者肝炎主因。",
            "D": "E 型肝炎符合旅行者肝炎，且孕婦感染死亡率可顯著升高。",
        },
    },
    91: {
        "stem": "本題是否定題，問哪一項不是潰瘍性結腸炎特徵。UC 可合併 PSC，但不是大部分患者都有 PSC。",
        "core": "UC 典型特徵：從直腸連續向近端延伸、侷限黏膜與表淺黏膜下層、pseudopolyps、toxic megacolon；PSC 是重要腸外表現但盛行率不會超過半數。",
        "reasons": {
            "A": "PSC 可與 UC 相關，但只有少數 UC 患者合併 PSC；說大部分超過 50% 都有是錯誤敘述，因此為答案。",
            "B": "Pseudopolyps 與 toxic megacolon 都是 UC 可見表現，屬正確特徵。",
            "C": "UC 常從直腸開始，連續性向近端延伸，這是典型分布。",
            "D": "UC 發炎通常限於黏膜及表淺黏膜下層，與 Crohn transmural inflammation 不同。",
        },
    },
    93: {
        "stem": "本題問 pituitary apoplexy 最常見原因。腦下垂體中風多指垂體腺瘤內急性出血或梗塞，其中出血是典型描述。",
        "core": "Pituitary apoplexy 常以突發頭痛、視覺症狀、眼肌麻痺與急性垂體功能不全表現，病理重點是腦下垂體腺瘤內出血。",
        "reasons": {
            "A": "嚴重腦下垂體出血是 pituitary apoplexy 的最常見與最典型原因。",
            "B": "缺血性壞死可參與 apoplexy，但考題問最常見原因時以出血為標準答案。",
            "C": "膿瘍屬感染性病灶，不是 pituitary apoplexy 的常見原因。",
            "D": "惡性腫瘤侵犯可造成垂體病變，但不是腦下垂體中風的典型主因。",
        },
    },
    94: {
        "stem": "本題有甲狀腺對稱性腫大與 antimicrosomal antibody，這是自體免疫甲狀腺炎線索，最符合橋本氏甲狀腺炎。",
        "core": "Hashimoto thyroiditis：女性、無痛性瀰漫或結節性甲狀腺腫、anti-TPO/antimicrosomal antibody，組織可見淋巴球浸潤與 Hurthle cell change。",
        "reasons": {
            "A": "橋本氏甲狀腺炎是自體免疫疾病，抗微粒體抗體陽性且甲狀腺對稱腫大，最符合。",
            "B": "亞急性甲狀腺炎通常有疼痛、病毒後病史與肉芽腫性發炎，不以 antimicrosomal antibody 為主。",
            "C": "雷得氏甲狀腺炎呈硬化纖維化，常與周圍組織沾黏，與題幹無沾黏不合。",
            "D": "慢性纖維性甲狀腺炎本質上接近 Riedel thyroiditis，重點是硬化與侵犯周圍組織，不符合抗體線索。",
        },
        "manual_review_notes": ["原題提到病理圖，已依文字線索與官方答案撰寫；若日後補圖，建議再核對影像。"],
    },
    95: {
        "stem": "本題是否定題，問 CIN/SIL 何者較不正確。LSIL 多數會自然回復，並非大部分持續存在。",
        "core": "LSIL 常可 regression，少部分進展到 HSIL；HSIL 較容易 persist，雖少數仍可 regression。否定題要選與自然病程相反的敘述。",
        "reasons": {
            "A": "LSIL 多數會回復而不是大部分持續存在；此敘述較不正確，因此為答案。",
            "B": "LSIL 有一部分會進展成 HSIL，約 10% 的量級可作考試記憶。",
            "C": "HSIL 雖風險較高，但仍有少數可能回復，此敘述可接受。",
            "D": "HSIL 多數會持續存在或進展，故需要積極追蹤處置，敘述可接受。",
        },
    },
    98: {
        "stem": "本題問狂犬病病理診斷依據。Rabies 典型可見 Negri bodies，為神經元內嗜酸性包涵體。",
        "core": "Rabies 病理關鍵字是 Negri body，常見於海馬迴 Purkinje cells 等神經元；Lewy body 則是巴金森病考點。",
        "reasons": {
            "A": "Lewy body 是 Parkinson disease、Lewy body dementia 的 alpha-synuclein 包涵體，不是狂犬病。",
            "B": "Kuru plaque 與 prion disease 相關，不是 rabies 診斷依據。",
            "C": "Negri body 是狂犬病典型神經元內包涵體，為本題答案。",
            "D": "Stress granules 是細胞壓力反應相關顆粒，不是狂犬病病理診斷重點。",
        },
    },
    99: {
        "stem": "本題問肉芽腫性葡萄膜炎常見於哪個疾病。Sarcoidosis 是非乾酪性肉芽腫性疾病，眼部可有 uveitis。",
        "core": "Sarcoidosis 常見肺門淋巴結、肺部病灶、皮膚與眼部侵犯；granulomatous uveitis 是重要併發症。",
        "reasons": {
            "A": "惡性黑色素瘤可侵犯眼部，但不是肉芽腫性葡萄膜炎的典型全身病因。",
            "B": "惡性淋巴瘤可有眼內侵犯或 masquerade syndrome，但不是本題常見肉芽腫性葡萄膜炎考點。",
            "C": "類肉瘤病會形成非乾酪性肉芽腫，常併發 granulomatous uveitis。",
            "D": "紅斑性狼瘡可有多種眼部表現，但肉芽腫性葡萄膜炎不是最典型連結。",
        },
    },
    100: {
        "stem": "本題病人嘔吐、記憶衰退與虛談，解剖見乳頭體及第三、第四腦室周圍出血壞死，符合 Wernicke-Korsakoff syndrome。",
        "core": "Wernicke-Korsakoff syndrome 與 thiamine（vitamin B1）缺乏相關，病灶常在 mammillary bodies 與 periventricular regions。",
        "reasons": {
            "A": "Vitamin A 缺乏主要造成夜盲、乾眼與上皮角化，不是乳頭體出血壞死。",
            "B": "Vitamin B1 缺乏會造成 Wernicke-Korsakoff syndrome，記憶障礙與 confabulation 正符合。",
            "C": "Vitamin B6 缺乏可造成周邊神經病變、癲癇或 sideroblastic anemia 等，不是此病理圖像。",
            "D": "Vitamin B12 缺乏造成巨球性貧血與脊髓後索側索病變，不以乳頭體壞死為主。",
        },
    },
}


def build_explanation(entry):
    option_lines = [f"- {letter}. {entry['reasons'][letter]}" for letter in ("A", "B", "C", "D")]
    return "\n\n".join(
        [
            f"【題幹解析】\n{entry['stem']}",
            "【選項詳解】\n" + "\n".join(option_lines),
            f"【核心考點】\n{entry['core']}",
        ]
    )


def compact_rule(entry, answer):
    return f"{entry['core']} 本題答案為 {answer}。"


def main():
    source = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    questions_by_number = {q["question_number"]: q for q in source["questions"]}

    missing = sorted(set().union(*[set(batch) for batch in BATCHES]) - set(ENTRIES))
    if missing:
        raise SystemExit(f"missing entries: {missing}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    paths = []
    for index, numbers in enumerate(BATCHES, start=1):
        updates = []
        for number in numbers:
            q = questions_by_number[number]
            entry = ENTRIES[number]
            answer = q.get("correct_answer", "")
            explanation = build_explanation(entry)
            rule = compact_rule(entry, answer)
            item = {
                "question_id": q["id"],
                "question_number": number,
                "explanation": explanation,
                "key_point": entry["core"],
                "flashcard_front": f"108-1 medicine-2 第 {number} 題：{answer} 的關鍵考點是什麼？",
                "flashcard_back": rule,
                "flashcard_summary": rule,
                "review_status": "ai_generated",
                "explanation_model": "codex-high-quality-rewrite",
                "explanation_generated_at": GENERATED_AT,
                "manual_review_notes": entry.get("manual_review_notes", []),
            }
            updates.append(item)

        update = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": min(numbers), "end": max(numbers)},
            "updates": updates,
        }
        path = OUT_DIR / f"q{min(numbers):03d}-q{max(numbers):03d}_sparse{index:02d}.json"
        path.write_text(json.dumps(update, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        paths.append(str(path))

    print(json.dumps({"update_files": paths, "question_count": sum(len(b) for b in BATCHES)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
