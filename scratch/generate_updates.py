import json
import os

updates = [
  {
    "question_id": "114-2_medicine-3_051",
    "question_number": 51,
    "explanation": "【題幹解析】\n本題詢問關於乳糜胸（chylothorax）特徵與診斷的正確敘述。乳糜胸是由於胸管（thoracic duct）受損或阻塞，導致含有高濃度三酸甘油酯與乳糜微粒的淋巴液蓄積於胸膜腔中。\n\n【選項詳解】\n- A. 錯誤。乳糜胸胸水最具特徵性的生化檢測值是三酸甘油酯（triglyceride）大於 110 mg/dL，而非膽固醇（cholesterol）數值高於 110 mg/dL。膽固醇數值極高（通常大於 250 mg/dL）而三酸甘油酯低下，是「假性乳糜胸（pseudochylothorax）」的表現。\n- B. 正確。胸管受損（thoracic duct injury）是乳糜胸最常見的病因，臨床上主要以心胸外科手術或外傷等醫源性創傷（iatrogenic trauma）佔最大多數，其次則為淋巴瘤等非創傷性腫瘤壓迫。\n- C. 錯誤。乳糜液內富含乳糜微粒、甘油三酯、蛋白質及大量淋巴球，因此乳糜胸的胸水化學與細胞分析符合「滲出液（exudate）」的標準，而非濾出液（transudate）。\n- D. 錯誤。乳糜胸的治療初期應優先採取保守療法（如禁食、改用中鏈三酸甘油酯飲食、給予 octreotide 以減少淋巴液產生）及肋膜腔引流。若長期放置豬尾巴導管（pig-tail）引流，會造成淋巴液、蛋白質與免疫球蛋白大量流失，引發嚴重營養不良及免疫抑制。\n\n【核心考點】\n乳糜胸（Chylothorax）的診斷以胸水三酸甘油酯（TG）> 110 mg/dL 為金標準，本質上為滲出液。最常見原因為胸管受損（多見於胸腔手術等醫源性創傷）。治療首重減少淋巴回流，避免長期引流導致嚴重營養流失。",
    "key_point": "乳糜胸的診斷標準為胸水三酸甘油酯 (TG) > 110 mg/dL，本質為滲出液，最常見於胸管手術或外傷等醫源性創傷。",
    "flashcard_front": "乳糜胸 (chylothorax) 的診斷標準、胸水性質及最常見原因為何？",
    "flashcard_back": "診斷標準：胸水三酸甘油酯 (TG) > 110 mg/dL；胸水性質：滲出液 (exudate)；最常見原因：胸管創傷 (thoracic duct trauma，多為手術等醫源性傷害)。",
    "flashcard_summary": "乳糜胸 -> 診斷為 TG > 110 mg/dL，屬滲出液，最常見於胸管手術或創傷。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "114-2_medicine-3_052",
    "question_number": 52,
    "explanation": "【題幹解析】\n本題描述一位 70 歲男性有長期重度吸菸史，發現左下肺葉 2 公分腫瘤及左腎上腺 2 公分腫瘤。病患同時合併高血壓（約 160/95 mmHg）。對於這顆意外發現的腎上腺腫瘤（adrenal incidentaloma），首先必須評估其荷爾蒙分泌功能，特別是在進行任何侵入性處置前，必須先排除嗜鉻細胞瘤。\n\n【選項詳解】\n- A. 正確。在評估腎上腺意外瘤時，首要步驟為篩檢是否為功能性腫瘤。由於此病患有高血壓表現，必須先測量 24 小時尿液兒茶酚胺（catecholamine）、香草扁桃酸（VMA）或甲氧基腎上腺素類（metanephrines），以排除嗜鉻細胞瘤。\n- B. 錯誤。在未明確腎上腺腫瘤是否具有內分泌功能（特別是未排除嗜鉻細胞瘤）以及未釐清病理診斷前，直接安排手術切除是極具風險的，若為嗜鉻細胞瘤，可能在手術觸碰腫瘤時誘發嚴重的兒茶酚胺風暴。\n- C. 錯誤。細針穿刺細胞學檢查（FNA）常用於懷疑惡性腫瘤轉移的病人，但在進行任何腎上腺穿刺活檢之前，必須「絕對排除」嗜鉻細胞瘤。若對未經藥物準備的嗜鉻細胞瘤進行穿刺，會誘發大量兒茶酚胺釋放，引發致死性的高血壓危象。\n- D. 錯誤。病患左下肺葉有疑似惡性腫瘤，其腎上腺腫瘤有高度可能是轉移灶，若僅安排 3~6 個月後電腦斷層追蹤，會延誤癌症的分期診斷與治療時機，且無法評估該腫瘤是否有內分泌功能。\n\n【核心考點】\n面對新發現的腎上腺意外瘤（Adrenal incidentaloma），在進行細針穿刺（FNA）或手術切除前，必須優先通過 24 小時尿液 catecholamine、VMA 或 metanephrines 檢測來排除嗜鉻細胞瘤（Pheochromocytoma），以避免誘發致命性高血壓危象。",
    "key_point": "評估腎上腺意外瘤時，手術或細針穿刺前必須優先檢測兒茶酚胺或 VMA 以排除嗜鉻細胞瘤，避免高血壓危象。",
    "flashcard_front": "評估腎上腺意外瘤 (adrenal incidentaloma) 時，在手術或細針穿刺前，最重要的生化篩檢為何？",
    "flashcard_back": "必須先測量 24hr 尿液兒茶酚胺 (catecholamine)、VMA 或 metanephrines 以排除嗜鉻細胞瘤 (pheochromocytoma)，防止穿刺或手術誘發致死性高血壓危象。",
    "flashcard_summary": "腎上腺意外瘤 -> 手術/穿刺前必先排除嗜鉻細胞瘤 (測 24hr 尿液 catecholamine/VMA)。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "114-2_medicine-3_053",
    "question_number": 53,
    "explanation": "【題幹解析】\n本題詢問治療肢端肥大症（acromegaly）時，能最有效同時降低生長素（GH）和類胰島素生長因子-I（IGF-I）的藥物。肢端肥大症多因垂體腺瘤過度分泌生長激素所致，藥物治療首選能直接作用於垂體受體並抑制其分泌的藥物。\n\n【選項詳解】\n- A. 錯誤。Cabergoline 是多巴胺受體促效劑（dopamine agonist），在肢端肥大症患者中，只有少數人（約 20-30%）能達到 GH 和 IGF-I 的正常化，通常僅用於病情較輕、手術後殘餘腫瘤或合併分泌泌乳素的個案，療效不如體抑素類似物。\n- B. 錯誤。Pegvisomant 是生長激素受體拮抗劑（GH receptor antagonist），能非常有效地阻斷周邊的 GH 受體，從而顯著降低肝臟產生的 IGF-I。然而，它不會降低血中的生長素（GH）濃度，反而會因為阻斷負回饋機制而導致血中 GH 反饋性升高。\n- C. 正確。體抑素類似物（somatostatin analogues，如 octreotide、lanreotide）能結合垂體生長激素瘤上的 SSTR-2 與 SSTR-5 受體，直接且強力抑制生長素（GH）的合成與分泌，進而降低血中生長素與周邊 IGF-I 的濃度，是臨床上最有效降低這兩者的一線藥物。\n- D. 錯誤。Bromocriptine 亦為多巴胺受體促效劑，但其對於降低 GH 和 IGF-I 的臨床療效與耐受性皆劣於 cabergoline，目前在肢端肥大症的治療中已非首選。\n\n【核心考點】\n肢端肥大症（Acromegaly）藥物治療中，Somatostatin analogues (如 octreotide) 可直接抑制垂體腫瘤，同時降低 GH 與 IGF-I。GH 受體拮抗劑 (Pegvisomant) 雖能顯著降低 IGF-I，但不會降低（甚至會代償性升高）血中 GH 濃度。",
    "key_point": "Somatostatin analogues (如 octreotide) 能直接抑制垂體腫瘤，同時降低 GH 與 IGF-I；而 GH 受體拮抗劑 (Pegvisomant) 僅能降低 IGF-I，無法降低 GH 濃度。",
    "flashcard_front": "治療肢端肥大症，Somatostatin analogues 與 Pegvisomant 對於 GH 與 IGF-I 的降低效果有何主要差異？",
    "flashcard_back": "Somatostatin analogues (如 octreotide) 可直接抑制垂體分泌，同時有效降低 GH 與 IGF-I；Pegvisomant 為 GH 受體拮抗劑，僅能降低 IGF-I，但血中 GH 濃度不會下降 (反而可能代償性升高)。",
    "flashcard_summary": "肢端肥大症治療 -> 體抑素類似物同時降低 GH 與 IGF-I；Pegvisomant 只降 IGF-I (GH 不降)。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "114-2_medicine-3_054",
    "question_number": 54,
    "explanation": "【題幹解析】\n本題詢問通常在甲狀腺危象（thyrotoxic crisis / thyroid storm）時才會使用的藥物。甲狀腺危象是嚴重的甲狀腺機能亢進急症，臨床上需使用多種藥物（包括抗甲狀腺藥物、乙型阻斷劑、碘劑及皮質類固醇等）進行多靶點治療。本題經官方更正為全體給分（原標準答案為 D）。\n\n【選項詳解】\n- A. 正確（全體給分）。Propranolol 是非選擇性 $\\beta$ 受體阻斷劑，在甲狀腺危象中常用於控制嚴重心搏過速與交感神經亢進症狀，且高劑量時能抑制外周 T4 轉化為 T3。然而，Propranolol 也被極廣泛用於治療一般甲狀腺機能亢進的心悸症狀，並非僅在危象時才使用。\n- B. 正確（全體給分）。Propylthiouracil (PTU) 是硫醯胺類（thionamides）抗甲狀腺藥物，在甲狀腺危象中因能額外抑制外周 T4 轉換成 T3 而被列為首選。但它也是日常口服治療一般甲狀腺機能亢進（特別是妊娠早期）的常規一線用藥。\n- C. 正確（全體給分）。Carbimazole 為抗甲狀腺藥物前驅藥，在體內轉化為 methimazole 起效，主要用於日常甲亢的維持治療。由於它不能抑制周邊 T4 轉化為 T3，在甲狀腺危象中一般不作為首選，亦非危象專用。\n- D. 正確（全體給分，原標準答案）。Lugol's solution（盧戈氏溶液 / 碘液）富含無機碘，可利用 Wolff-Chaikoff 效應暫時性阻斷甲狀腺素的釋放。由於長期使用會產生逸脫效應（escape phenomenon）導致甲亢反彈惡化，故在臨床上通常僅限於甲狀腺危象的緊急控制，或是甲狀腺切除術前 7-10 天的短期術前準備以減少腺體充血，平時一般甲亢的維持治療中絕不長期使用。\n\n【核心考點】\n無機碘劑（如 Lugol's solution、SSKI）因具備暫時性抑制甲狀腺素釋放的作用，且長期使用會發生逸脫效應，因此臨床應用嚴格受限，通常僅在甲狀腺危象或 Graves' disease 術前準備等特殊緊急時機才會使用。一般甲亢則以 thionamides (如 methimazole, PTU) 及 $\\beta$-blockers 為主。",
    "key_point": "無機碘劑 (如 Lugol's solution) 因具備 Wolff-Chaikoff 效應但有逸脫效應，臨床上僅限於甲狀腺危象與甲狀腺切除術前準備短期使用。",
    "flashcard_front": "為什麼無機碘劑 (如 Lugol's solution) 通常僅在甲狀腺危象或術前準備時使用，而不做為一般甲亢的長期維持治療？",
    "flashcard_back": "因為長期使用無機碘劑會產生逸脫效應 (escape phenomenon)，使抑制甲狀腺素合成與釋放的作用失效，導致甲亢反彈惡化。因此臨床僅限於危象緊急阻斷或術前減少腺體血管增生。",
    "flashcard_summary": "無機碘劑 -> 因逸脫效應限於甲狀腺危象及術前準備短期使用，不可做為一般甲亢之長期藥物。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": [
      "官方更正全體給分題（原標準答案為 D）。已在解析中詳細補充爭議原因與各選項臨床時機。"
    ]
  },
  {
    "id": "114-2_medicine-3_055",
    "question_number": 55,
    "explanation": "【題幹解析】\n本題評估關於糖尿病慢性併發症分類與病因敘述的適當性。糖尿病的慢性併發症主要分為微血管病變與大血管病變。本題經官方更正，答 C 或 D 或 CD 者均給分。\n\n【選項詳解】\n- A. 錯誤（非最不適當敘述，屬於正確描述）。糖尿病視網膜病變（diabetic retinopathy）是由於視網膜毛細血管周皮細胞流失與基底膜增厚，屬於非常典型的微血管病變（microvascular complication）。\n- B. 錯誤（非最不適當敘述，屬於正確描述）。冠狀動脈心臟病（coronary heart disease）涉及冠狀動脈等中大型動脈的粥狀硬化與阻塞，屬於典型的大血管病變（macrovascular complication）。\n- C. 正確（為不適當敘述）。糖尿病足病變（diabetic foot）的成因是多因素的，包含周邊神經病變（diabetic neuropathy，與微血管病變高度相關）、血管病變（特別是周邊動脈大血管病變 PAD）以及局部免疫下降易受感染。大血管病變造成的下肢缺血是糖尿病足難以癒合的主因，故說「不是大血管病變」顯然是錯誤的。\n- D. 正確（為不適當敘述）。慢性高血糖（chronic hyperglycemia）是否為大血管病變的「直接」原因，在臨床研究上曾有爭議。雖然高血糖會透過形成糖化終產物（AGEs）與阻礙內皮一氧化氮合成等途徑損害血管，但多個大型隨機臨床試驗（如 UKPDS、ACCORD、ADVANCE 等）顯示，嚴格控制血糖對降低大血管事件（如心肌梗塞、中風）的短期保護效果，遠不如對微血管病變顯著，且大血管病變深受高血壓、高血脂、抽菸等多重因子影響。因此「是否直接造成較無定論」在字義上具備學術爭議，亦被判定為可給分的選項。\n\n【核心考點】\n糖尿病足（Diabetic foot）的病因結合了微血管相關的神經病變與大血管相關的周邊動脈阻塞病變（PAD），缺血是大血管阻塞的直接後果。此外，嚴格控制血糖能顯著預防微血管病變，但對大血管併發症的預防則需結合血壓與血脂等多因子控制，單純控糖效果在臨床試驗中較具學術爭議。",
    "key_point": "糖尿病足病變的成因包含周邊神經病變及大血管相關的周邊動脈病變 (PAD)；而血糖控制對於微血管併發症效果顯著，對大血管事件的直接預防則具爭議。",
    "flashcard_front": "糖尿病足 (diabetic foot) 的病因結構為何？高血糖控制與微/大血管併發症的關係有何不同？",
    "flashcard_back": "糖尿病足成因包含神經病變 (微血管相關) 與下肢血管阻塞 (大血管相關 PAD)。控制高血糖能顯著降低微血管病變 (如視網膜、腎病變) 的風險，但對大血管病變 (如心肌梗塞、周邊血管病變) 的預防則需合併控制血壓與血脂，單純控糖效果在大型試驗中較無定論。",
    "flashcard_summary": "糖尿病併發症 -> 糖尿病足兼具神經與大血管病變；嚴格控糖對微血管預防極明確，對大血管則需多因子控制。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": [
      "官方更正答 C 或 D 或 CD 均給分。已在解析中詳細拆解糖尿病足的多因子成因及血糖對大/微血管併發症的試驗爭議。"
    ]
  },
  {
    "id": "114-2_medicine-3_056",
    "question_number": 56,
    "explanation": "【題幹解析】\n本題詢問根據 NCEP: ATP III 的診斷標準，下列哪位男性成人符合代謝症候群（metabolic syndrome）個案。NCEP: ATP III 診斷標準規定，若符合定義的 5 項指標中的 3 項或以上，即可確診為代謝症候群。\n\n【選項詳解】\n- A. 錯誤。該男性僅符合 2 項指標：血壓偏高（$\ge$ 130/85 mmHg，此處為 132/78 mmHg）與三酸甘油酯過高（$\ge$ 150 mg/dL，此處為 190 mg/dL）。其腰圍為 89 cm（未達男性 > 102 cm 標準）、HDL-C 為 46 mg/dL（未低於男性 < 40 mg/dL 標準），而白蛋白尿並非 ATP III 診斷項目。\n- B. 錯誤。該男性僅符合 2 項指標：空腹血糖偏高（$\ge$ 100 mg/dL，此處為 109 mg/dL）與三酸甘油酯過高（$\ge$ 150 mg/dL，此處為 242 mg/dL）。其血壓未達標，且 BMI 與白蛋白尿均不是 ATP III 代謝症候群的診斷指標（診斷指標為腰圍而非 BMI）。\n- C. 正確。該男性共符合 4 項指標：(1) 腰圍 105 cm（達男性 > 102 cm 標準）；(2) 血壓 142/86 mmHg（達 $\ge$ 130/85 mmHg 標準）；(3) 空腹血糖 116 mg/dL（達 $\ge$ 100 mg/dL 標準）；(4) 三酸甘油酯 216 mg/dL（達 $\ge$ 150 mg/dL 標準）。因符合項目達 4 項（$\ge$ 3 項），診斷成立。其 HDL-C 42 mg/dL 則在男性正常範圍內（未低於 40 mg/dL）。\n- D. 錯誤。該男性僅符合 2 項指標：血壓偏高（$\ge$ 130/85 mmHg，此處為 146/88 mmHg）與空腹血糖偏高（$\ge$ 100 mg/dL，此處為 123 mg/dL）。其總膽固醇與 BMI 非診斷指標，HDL-C 46 mg/dL 亦未低於 40 mg/dL。\n\n【核心考點】\nNCEP: ATP III 代謝症候群診斷標準（男性）為以下 5 項中符合至少 3 項：(1) 腹部肥胖（腰圍 > 102 cm）；(2) 三酸甘油酯 $\ge$ 150 mg/dL；(3) HDL-C < 40 mg/dL；(4) 血壓 $\ge$ 130/85 mmHg；(5) 空腹血糖 $\ge$ 100 mg/dL。需注意 BMI、總膽固醇及白蛋白尿均非診斷指標。",
    "key_point": "NCEP: ATP III 代謝症候群診斷標準規定，男性腰圍 > 102 cm、TG $\ge$ 150、HDL < 40、BP $\ge$ 130/85、空腹血糖 $\ge$ 100 mg/dL，符合三項以上即可診斷。",
    "flashcard_front": "NCEP: ATP III 代謝症候群診斷標準中，男性的 5 項診斷指標與界限值分別 homes？",
    "flashcard_back": "男性代謝症候群需符合以下 5 項中至少 3 項：\n1. 腰圍 (Waist circumference) > 102 cm (台灣國健署為 $\ge$ 90 cm)\n2. 三酸甘油酯 (TG) $\ge$ 150 mg/dL\n3. 高密度膽固醇 (HDL-C) < 40 mg/dL\n4. 血壓 $\ge$ 130/85 mmHg\n5. 空腹血糖 (Fasting glucose) $\ge$ 100 mg/dL\n(註：總膽固醇、BMI、白蛋白尿皆非診斷項目)",
    "flashcard_summary": "代謝症候群診斷 (ATP III) -> 男腰 > 102cm, TG $\ge$ 150, HDL < 40, BP $\ge$ 130/85, 血糖 $\ge$ 100，符合三項診斷。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "114-2_medicine-3_057",
    "question_number": 57,
    "explanation": "【題幹解析】\n本題詢問下列何者最不可能導致低血糖（hypoglycemia）。解答時應先了解各個選項在生理病理或藥理機制上對血糖的影響。\n\n【選項詳解】\n- A. 正確（最不可能導致低血糖，其副作用為高血糖）。Thiazide 類利尿劑在臨床上的常見副作用是「高血糖」而非低血糖。其主要機制是利尿導致低血鉀，低血鉀會抑制胰臟 $\\beta$ 細胞釋放胰島素，並使周邊組織對胰島素的敏感性下降。\n- B. 錯誤。胰島素瘤（insulinoma）是分泌胰島素的胰臟神經內分泌腫瘤，腫瘤會不受調控地自主釋放大量內源性胰島素，是引發反覆空腹低血糖（Whipple's triad）的經典原因。\n- C. 錯誤。Glimepiride 是一種磺醯脲類（sulfonylurea）口服降血糖藥，主要是透過促進胰臟 $\\beta$ 細胞的胰島素分泌來降血糖。若服用過量，會造成胰島素過剩並引起嚴重且持續性的低血糖。\n- D. 錯誤。敗血症（sepsis）等重症患者中，由於全身性發炎反應導致葡萄糖消耗急劇增加，且常合併肝功能受損導致肝糖分解與糖質新生（gluconeogenesis）受阻，臨床上常會誘發非糖尿病性的重症低血糖。\n\n【核心考點】\n自發性低血糖的常見病因包括胰島素瘤、磺醯脲類藥物過量及重症（如敗血症導致糖質新生受阻與消耗增加）。而 Thiazide 類利尿劑的代謝副作用則為高血糖（機制與低血鉀抑制胰島素釋放相關）、高尿酸、高鈣以及低鈉、低鉀。",
    "key_point": "Thiazide 類利尿劑的副作用為高血糖，其藉由低血鉀抑制胰島素分泌；而胰島素瘤、磺醯脲類過量及敗血症均會引發低血糖。",
    "flashcard_front": "Thiazide 類利尿劑、胰島素瘤、Glimepiride 過量與敗血症對血糖的影響及機制有何不同？",
    "flashcard_back": "1. Thiazide 類利尿劑：會導致高血糖。機制為低血鉀干擾胰島素釋放，並降低胰島素敏感性。\n2. 胰島素瘤 (insulinoma)：自主分泌大量胰島素導致空腹低血糖。\n3. Glimepiride (Sulfonylurea)：刺激胰島素分泌，過量會造成嚴重低血糖。\n4. 敗血症 (sepsis)：因發炎因子造成糖消耗量大增且抑制肝臟糖質新生，可引發重症低血糖。",
    "flashcard_summary": "血糖影響因素 -> Thiazide 引起高血糖；胰島素瘤、磺醯脲類過量及敗血症則會引發低血糖。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "114-2_medicine-3_058",
    "question_number": 58,
    "explanation": "【題幹解析】\n本題描述一位 25 歲年輕男性（患有糖尿病數年，需靠注射胰島素控制血糖）因熬夜、壓力大且飲用含糖飲料，出現心悸、氣喘、噁心、嘔吐、腹痛與體重減輕。急診理學檢查顯示心跳 100 次/分、血壓 110/70 mmHg，隨機血糖為 560 mg/dL。此病史與臨床表現高度提示為糖尿病酮酸中毒（Diabetic Ketoacidosis, DKA）發作，這是一種因胰島素絕對或相對缺乏所致的內科急症。\n\n【選項詳解】\n- A. 錯誤（非不適當處置，屬於正確步驟）。懷疑 DKA 時，必須立即抽血檢測靜脈或動脈血氣分析（確認 pH 值與 $\\text{HCO}_3^-$ 以評估酸中毒程度）、血中電解質（特別是鉀離子，因胰島素治療會使鉀離子進入細胞內，需監測以防致命性低血鉀）及血糖。\n- B. 錯誤（非不適當處置，屬於正確步驟）。DKA 治療的兩大核心為：(1) 靜脈輸注大量生理食鹽水以矯正嚴重脫水與恢復血容量；(2) 靜脈點滴注射速效型胰島素以降低血糖並逆轉酮酸生成。\n- C. 正確（為不適當處置）。患者高血糖的原因是體內胰島素絕對或相對不足（常因熬夜壓力、喝含糖飲料、擅自停藥或感染誘發），**胰島素是治療 DKA 唯一能救命的降血糖藥物**，絕非「胰島素無效」，此時絕對不可停用胰島素或改用口服降糖藥，否則會使病情迅速惡化致死。\n- D. 錯誤（非不適當處置，屬於正確步驟）。DKA 屬於臨床重症，容易合併嚴重電解質紊亂、心律不整、腦水腫或休克，治療期間需要每 1 至 2 小時追蹤生化數值並精密調整輸液與藥物，因此必須安排病人住院密切治療與監測。\n\n【核心考點】\n糖尿病酮酸中毒 (DKA) 的發病機轉為胰島素絕對或相對不足，首要治療為大量靜脈輸液（補水）與靜脈點滴注射速效胰島素。胰島素是逆轉 DKA 的唯一關鍵藥物，不可改用口服降糖藥，且須密切追蹤血鉀以防止治療中發生致命低血鉀。",
    "key_point": "糖尿病酮酸中毒 (DKA) 的治療首重大量靜脈補水與靜脈注射速效胰島素以逆轉酮酸生成，切不可改用口服降糖藥，且需嚴密監測並補充足夠的血鉀。",
    "flashcard_front": "針對懷疑糖尿病酮酸中毒 (DKA) 的急診患者，其病因機轉與三大治療原則為何？",
    "flashcard_back": "病因機轉：胰島素絕對或相對缺乏。\n治療原則：\n1. 大量靜脈點滴生理食鹽水，矯正嚴重脫水。\n2. 靜脈點滴速效胰島素，逆轉酮體生成 (絕不可改用口服藥)。\n3. 密切監測並補充電解質，特別是當血鉀低於 5.2 mEq/L 時需及時補鉀，以防胰島素使用後引發致命低血鉀。",
    "flashcard_summary": "DKA 處理 -> 機轉為胰島素缺乏，治療為大量補水、靜脈點滴胰島素，以及密切監測/補充鉀離子。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "114-2_medicine-3_059",
    "question_number": 59,
    "explanation": "【題幹解析】\n本題詢問病毒性腦炎（viral encephalitis）病人的腦脊髓液（CSF）檢查報告中最不可能出現的結果。解答本題需將病毒性、細菌性、結核性或真菌性腦膜炎的 CSF 化學與細胞特徵進行鑑別。\n\n【選項詳解】\n- A. 錯誤（非最不可能出現，屬於可能出現的描述）。雖然多數病毒性腦膜炎的腦脊髓液中無紅血球，但某些會引起局部腦組織出血壞死的病毒性腦炎（最典型為單純皰疹病毒腦炎 HSV encephalitis，常造成雙側顳葉出血壞死），其腦脊髓液中常見紅血球數目增加。\n- B. 錯誤（非最不可能出現，屬於可能出現的描述）。病毒感染引起的腦膜發炎反應會導致血腦障壁通透性增加與發炎反應，使腦脊髓液中的蛋白質濃度輕度至中度增加（通常在 50 至 150 mg/dL 之間，但極少像細菌性腦膜炎那般高達數百 mg/dL）。\n- C. 錯誤（非最不可能出現，屬於可能出現的描述）。病毒性腦炎的典型 CSF 細胞反應為白血球數目中度增加（通常 < 1000 cells/$\mu$L），且分類上以單核球或淋巴球（lymphocytes）為主（雖然在感染極早期 24 小時內，可能短暫以嗜中性球為主，但隨後會迅速轉為淋巴球）。\n- D. 正確（為最不可能出現之結果）。在單純病毒性腦炎中，病毒通常不消耗葡萄糖，因此腦脊髓液的葡萄糖濃度大多正常，其與血液葡萄糖濃度的比值（CSF/serum glucose ratio）通常大於 0.6。若該比值顯著下降至小於 0.4，是細菌性、結核性或真菌性腦膜炎的特徵（因為這些病原體與大量嗜中性球會消耗葡萄糖）。\n\n【核心考點】\n腦脊髓液 (CSF) 鑑別診斷中，病毒性腦炎/腦膜炎的特徵為葡萄糖濃度正常 (CSF/serum ratio > 0.6) 且白血球以淋巴球為主。若比值小於 0.4 (葡萄糖顯著降低)，則強烈指向細菌、結核或真菌性腦膜炎。此外，HSV 腦炎因侵犯顳葉出血壞死，CSF 可見紅血球增加。",
    "key_point": "病毒性腦炎的腦脊髓液 (CSF) 特徵為葡萄糖濃度正常 (CSF/serum ratio > 0.6)；若比值 < 0.4，則強烈提示為細菌性、結核性或真菌性腦膜炎。",
    "flashcard_front": "如何從腦脊髓液 (CSF) 的葡萄糖比值 (CSF/serum ratio) 與細胞分類鑑別病毒性與細菌性腦膜炎/腦炎？",
    "flashcard_back": "1. 病毒性腦炎/腦膜炎：CSF 葡萄糖正常 (CSF/serum ratio > 0.5-0.6)；白血球以淋巴球 (lymphocytes) 為主。\n2. 細菌性腦膜炎：CSF 葡萄糖顯著下降 (CSF/serum ratio < 0.4)；白血球顯著增加且以嗜中性球 (neutrophils) 為主。\n(註：HSV 腦炎可因顳葉壞死而使 CSF 出現紅血球。)",
    "flashcard_summary": "CSF 鑑別 -> 病毒性：葡萄糖正常、以淋巴球為主；細菌/結核/真菌性：葡萄糖顯著降低 (<0.4)。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "114-2_medicine-3_060",
    "question_number": 60,
    "explanation": "【題幹解析】\n本題詢問下列何者最不可能傳播人類免疫不全病毒（HIV）。解答本題需理解 HIV 病毒在不同體液中的濃度分佈，以及其主要的生理傳播途徑。\n\n【選項詳解】\n- A. 錯誤。陰道性交（vaginal sex）是全球最普遍的 HIV 傳播途徑之一。體液（如精液、陰道分泌物）中的病毒能透過陰道或子宮頸黏膜的微小破損進入人體，若同時合併其他性傳染病（如梅毒、疱疹等造成黏膜潰瘍）會使風險倍增。\n- B. 錯誤。共用針頭（needle sharing）是效率極高的血液傳播途徑。靜脈注射毒品者共用針頭或針筒時，微量的殘留血液會直接進入下一個人的循環系統中，造成高機率的感染。\n- C. 正確。親吻（kissing）最不可能傳播 HIV。唾液中的 HIV 病毒量極低，不足以造成感染，且唾液中含有天然的抗病毒蛋白。除非雙方皆有嚴重的口腔黏膜大面積開放性出血傷口，否則一般的社交性接觸或親吻不具備傳播風險。\n- D. 錯誤。肛交（anal sex）是性行為中傳播 HIV 風險最高者，特別是對接受方（receptive partner）而言。直腸黏膜僅由單層柱狀上皮組成，且缺乏潤滑分泌，在摩擦中極易產生微小撕裂傷，使病毒輕易接觸黏膜下的毛細血管而造成感染。\n\n【核心考點】\n人類免疫不全病毒（HIV）的主要傳播途徑包括不安全行為（肛交風險最高，特別是接受方；其次為陰道性交）、血液接觸（共用針頭、輸入污染血品）及母子垂直感染。一般的日常社交接觸、共用餐具或親吻（因唾液中病毒載量極低且有抑制物質）在臨床上最不可能導致感染。",
    "key_point": "HIV 的主要傳播途徑為不安全性行為 (其中肛交風險最高)、血液接觸 (如共用針頭) 與母子垂直傳播；親吻等唾液接觸在臨床上最不可能傳播。",
    "flashcard_front": "HIV 的三大主要傳播途徑為何？為什麼親吻和一般的社交接觸不會傳播 HIV？",
    "flashcard_back": "三大傳播途徑：不安全性行為 (肛交、陰道性交)、血液接觸 (共用針頭、針扎、污染血品)、母子垂直傳播。\n不透過親吻傳播原因：唾液中的 HIV 病毒量極低，且唾液含有可抑制病毒活性的酶。一般社交接觸或無出血傷口的親吻皆不具備臨床感染風險。",
    "flashcard_summary": "HIV 傳播 -> 性行為 (肛交風險高)、血液與母子傳播為主；唾液中病毒量低，親吻不具傳播風險。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-14T13:30:00+08:00",
    "manual_review_notes": []
  }
]

# Write to the destination JSON
output_data = {
  "source_file": "public/data/exams/114-2/medicine-3.json",
  "dataset_id": "114-2_medicine-3",
  "range": { "start": 51, "end": 60 },
  "updates": updates
}

target_file = "scratch/rewrite_updates/114-2_medicine-3/q051-q060.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {target_file}")
