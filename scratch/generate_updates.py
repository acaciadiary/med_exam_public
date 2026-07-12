# -*- coding: utf-8 -*-
import json
import os

updates = [
  {
    "question_id": "109-1_medicine-4_061",
    "question_number": 61,
    "explanation": "【題幹解析】\n思覺失調症（schizophrenia）患者的自殺風險顯著高於一般族群。流行病學與長期追蹤研究指出，約有 10% 至 13% 的思覺失調症病人最終死於自殺，此自殺死亡率比一般人群高出數十倍。\n\n【選項詳解】\n- A. 錯誤。1~3% 顯著低估了思覺失調症患者的自殺死亡率。一般大眾的自殺率遠低於此，但對於重度精神疾病如思覺失調症，其終生自殺死亡率要高得多。\n- B. 正確。根據長期追蹤的流行病學研究，思覺失調症患者中約有 10% 至 13% 會因自殺而死亡，特別是在疾病早期、功能退化明顯、或剛出院的時期。\n- C. 錯誤。25~30% 雖然是思覺失調症病人曾有過「自殺企圖（suicide attempts）」或嚴重自殺意念的估計比例，但並非「自殺死亡（completed suicide）」的長期追蹤比例。\n- D. 錯誤。40~50% 遠高於思覺失調症的實際自殺死亡率，此比例在臨床上並不符合流行病學數據。\n\n【核心考點】\n思覺失調症（schizophrenia）的自殺流行病學特徵：長期追蹤下的終生自殺死亡率約為 10-13%。高風險因子包括年輕、男性、疾病早期、病前功能良好、伴隨重度憂鬱症狀以及對疾病具有高度病識感（insight）而產生的絕望感。",
    "key_point": "思覺失調症（schizophrenia）患者在長期追蹤中，最終約有 10% 至 13% 死於自殺，高風險期多在疾病早期或剛出院時。",
    "flashcard_front": "思覺失調症（schizophrenia）的病人長期追蹤下，約有多少比例最終會死於自殺？",
    "flashcard_back": "約 10% 到 13%（通常臨床文獻指出約為 10%）。",
    "flashcard_summary": "思覺失調症 -> 長期追蹤自殺死亡率約為 10~13%。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_062",
    "question_id": "109-1_medicine-4_062",
    "question_number": 62,
    "explanation": "【題幹解析】\n本題詢問關於譫妄（delirium）的敘述何者錯誤。標準答案為 A。譫妄是一種因生理病因導致的急性認知與意識狀態改變，其症狀起伏大，治療應以找出並處理根本的身體病因為首要。當精神症狀或躁動嚴重危害安全時，可考慮短期且低劑量使用口服或靜脈/肌肉注射之抗精神病藥物，但長效針劑因作用時間長、代謝慢且無法調整劑量，絕對不可用於急性譫妄的治療。\n\n【選項詳解】\n- A. 錯誤（本題答案）。抗精神病長效針劑（long-acting injection, LAI）在體內釋放緩慢、半衰期極長，一旦發生副作用（如錐體外症候群 EPS）無法立即停藥移除，且譫妄症狀呈波動性（fluctuating course），需要動態調整藥量，因此長效針劑絕對不可用於治療譫妄。\n- B. 正確。高齡（尤其是大於 70 歲）是譫妄的獨立高危險因子，因其腦部代償能力（brain reserve）較差，在面對感染、手術或藥物變動時更容易誘發譫妄。\n- C. 正確。譫妄的發生通常意味著患者身體狀況嚴重失衡，臨床上與死亡率上升、住院天數延長、認知功能加速退化及出院後安置困難等不良預後密切相關。\n- D. 正確。譫妄的核心症狀為急性發作且起伏的注意力缺失、意識清明度下降，並常伴隨認知功能受損（如記憶、定向力障礙）及知覺異常（如視幻覺）。\n\n【核心考點】\n譫妄（delirium）的診斷核心在於急性發作、症狀波動、意識及注意力障礙；處置原則是找出並根除潛在的身體病因（如電解質不平衡、感染、藥物中毒或戒斷）。若需藥物控制躁動，僅可使用短效口服或針劑，禁用長效針劑。",
    "key_point": "譫妄首要治療為處置根本病因，若需藥物控制躁動可用短效抗精神病藥，長效針劑因無法隨病況調整劑量而禁用。",
    "flashcard_front": "關於譫妄（delirium）的臨床特徵與治療原則，下列敘述何者錯誤？",
    "flashcard_back": "抗精神病長效針劑是治療首選之一。譫妄病情起伏大，禁用長效針劑，應優先找出病因，必要時給予低劑量短效藥物。",
    "flashcard_summary": "譫妄 -> 禁用長效針劑，核心為意識與注意力障礙，治療以清除根本病因為主。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_063",
    "question_id": "109-1_medicine-4_063",
    "question_number": 63,
    "explanation": "【題幹解析】\n選擇性血清素再吸收抑制劑（SSRI）是臨床上最常用的抗憂鬱藥物。本題詢問何者不是 SSRI 的常見副作用。標準答案為 A。SSRI 的常見副作用與血清素受體在全身的分布有關，包括腸胃道反應、性功能障礙及中樞神經興奮引起的睡眠障礙。SSRI 並不會引起急性血糖急速上升；在精神科藥物中，引發血糖上升、高血脂及體重增加等代謝副作用的，主要是第二代（非典型）抗精神病藥物（如 olanzapine、clozapine）。\n\n【選項詳解】\n- A. 正確（非 SSRI 的副作用）。SSRI 藥物不具備直接引發急性高血糖或血糖急速上升的藥理作用。相反地，某些非典型抗精神病藥因拮抗 H1 和 5-HT2C 受體，才會導致嚴重的體重增加與胰島素阻抗。\n- B. 錯誤（是常見副作用）。SSRI 剛開始使用時，會刺激腸胃道的 5-HT3 受體，常引起噁心、嘔吐、腹瀉或消化不良等胃腸道症狀，通常在用藥 1-2 週後會逐漸適應。\n- C. 錯誤（是常見副作用）。長期服用 SSRI 的患者中，高達 50-70% 會出現性功能障礙，包含性慾減退、勃起障礙、或射精延遲（anorgasmia），此與血清素活性上升抑制多巴胺路徑有關。\n- D. 錯誤（是常見副作用）。SSRI 具有輕微的中樞活化作用，特別是在早晨服用或剛開始用藥時，容易造成失眠、淺眠或多夢等睡眠障礙。\n\n【核心考點】\nSSRI 類藥物的藥理學與副作用：常見副作用包括噁心（刺激胃腸道 5-HT3）、性功能障礙（抑制多巴胺）、睡眠障礙（中樞興奮）。引發代謝異常（血糖上升、體重增加）的代表性精神科藥物為非典型抗精神病藥物（尤其是 olanzapine 與 clozapine）。",
    "key_point": "SSRI 常見副作用有噁心、性功能障礙及失眠；高血糖與代謝異常則主要出現在第二代抗精神病藥（如 olanzapine）。",
    "flashcard_front": "下列何者不是選擇性血清素再吸收抑制劑（SSRI）的常見副作用？",
    "flashcard_back": "血糖急速上升。SSRI常見副作用為噁心、性功能障礙及睡眠障礙，急性血糖上升主要是部分非典型抗精神病藥物的副作用。",
    "flashcard_summary": "SSRI副作用 -> 噁心、性功能障礙、睡眠障礙。血糖急速上升為非典型抗精神病藥副作用。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_064",
    "question_id": "109-1_medicine-4_064",
    "question_number": 64,
    "explanation": "【題幹解析】\n本題詢問關於身體形象畏懼症（BDD）的敘述何者錯誤。標準答案為 A。身體形象畏懼症患者對自身外觀存在主觀想像的缺陷或極度誇大微小的瑕疵，導致嚴重的焦慮與功能受損。這是一種精神障礙（在 DSM-5 中歸類於強迫症相關障礙症），患者尋求手術或醫美介入後，通常非但無法解決心理上的扭曲認知，反而容易對治療結果更加不滿，引發醫療糾紛，因此非手術適應症。首選治療為高劑量抗憂鬱劑（如 SSRI）配合認知行為治療（CBT）。\n\n【選項詳解】\n- A. 錯誤（本題答案）。外科手術或整形醫美介入無法解決患者大腦對身體形象的病態認知，術後患者往往會轉移關注部位或認為手術失敗，導致病情惡化，因此手術為治療禁忌。\n- B. 正確。統計顯示，BDD 患者最常感到不滿意的身體部位通常是面部特徵（如鼻子的形狀或大小）以及頭髮（如髮線、禿頭恐懼），其他也包括皮膚 and 生殖器。\n- C. 正確。身體形象畏懼症患者常伴隨嚴重的社交退縮與自我否定，共病率極高，其中最常見的共病為重鬱症（major depressive disorder）與強迫症（obsessive-compulsive disorder）。\n- D. 正確。藥物治療方面，第一線藥物為選擇性血清素再吸收抑制劑（SSRI），且臨床上通常需要比治療一般憂鬱症更高的劑量，並需維持數週以上才能見效。\n\n【核心考點】\n身體形象畏懼症（BDD）的臨床特點：患者對外觀有扭曲的缺陷感受，整形手術是禁忌（無效且會惡化）；藥物治療以高劑量 SSRI 為主，常與重鬱症及強迫症共病。",
    "key_point": "身體形象畏懼症（BDD）患者對外貌有妄想般的扭曲認知，醫美或整形手術為禁忌，應使用高劑量 SSRI 與認知行為治療。",
    "flashcard_front": "關於身體形象畏懼症（body dysmorphic disorder）的臨床表現與治療，下列敘述何者錯誤？",
    "flashcard_back": "以手術或醫學美容介入可有效減緩病情。手術是禁忌，無法改善認知扭曲，首選治療為高劑量SSRI與心理治療。",
    "flashcard_summary": "身體形象畏懼症 -> 禁用手術/醫美介入，共病強迫/憂鬱，治療首選高劑量SSRI。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_065",
    "question_id": "109-1_medicine-4_065",
    "question_number": 65,
    "explanation": "【題幹解析】\n本題詢問關於急性壓力疾患（ASD）與創傷後壓力症候群（PTSD）的比較何者錯誤。標準答案為 C。兩者皆是經歷重大創傷事件後引發的壓力反應，核心症狀相似，包括侵入性症狀、迴避行為、認知與情緒的負面改變、以及警覺性增高。主要區別在於時間跨度：ASD 的病程為創傷後 3 天至 1 個月；超過 1 個月則診斷為 PTSD。解離症狀（如失去現實感、自我解離）不但在 ASD 中非常常見，且在 DSM-5 中亦是重要症狀群之一。\n\n【選項詳解】\n- A. 正確。根據 DSM-5 診斷標準，急性壓力疾患（ASD）的時間定義為創傷事件後 3 天至 1 個月內。如果相關症狀持續超過 1 個月，則必須評估並考慮改診斷為創傷後壓力症候群（PTSD）。\n- B. 正確。PTSD 的黃金治療組合為藥物治療（如首選之 SSRI，包括 sertraline, paroxetine）配合針對創傷的心理治療（如認知行為治療 CBT、眼動減敏與歷程更新治療 EMDR），兩者合併療效最佳。\n- C. 錯誤（本題答案）。解離症狀（dissociative symptoms，如麻木、失去現實感 derealization、自我感喪失 depersonalization 或解離性遺忘）是急性壓力反應的常見特徵，常會出像在急性壓力疾患（ASD）中。\n- D. 正確。神經內分泌研究證實，PTSD 患者常存有下視丘-腦垂體-腎上腺軸（HPA axis）的功能失調，表現為皮質醇（cortisol）的負回饋抑制異常敏感，導致體內皮質醇水平異常偏低，而促腎上腺皮質激素釋放激素（CRH）上升。\n\n【核心考點】\nASD 與 PTSD 的鑑別診斷與病理：\n1. 時間定義：ASD（3天至1個月）；PTSD（持續超過1個月）。\n2. 兩者皆可出現解離症狀。\n3. 生理機轉：與 HPA axis 失調（皮質醇過低、負回饋過度敏感）有關。",
    "key_point": "ASD 與 PTSD 皆可有解離症狀；ASD 症狀持續時間為 3 天至 1 個月，若超過 1 個月則需診斷為 PTSD。",
    "flashcard_front": "關於急性壓力疾患（ASD）與創傷後壓力症候群（PTSD）的敘述，下列敘述何者錯誤？",
    "flashcard_back": "急性壓力疾患之症狀中不會出現解離症狀。解離症狀（如現實感喪失）在ASD和PTSD中都相當常見。",
    "flashcard_summary": "ASD與PTSD -> 區分在於病程（ASD限1個月內，超時為PTSD），兩者皆可有解離症狀，PTSD與HPA軸功能失調有關。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_066",
    "question_id": "109-1_medicine-4_066",
    "question_number": 66,
    "explanation": "【題幹解析】\n本題描述一位因長期吸食安非他命（amphetamine）而誘發精神病症狀（聽幻覺、被害妄想、易怒躁動）的個案，詢問何者處置錯誤。標準答案為 D。安非他命為中樞神經興奮劑，濫用會導致突觸間隙多巴胺濃度暴增，進而引發類似思覺失調症的幻覺與妄想。首要處置是立即停用毒品，並在急性躁動或暴力期短期給予多巴胺受體拮抗劑（如 haloperidol）控制精神病症，必要時可採取保護性約束。在安非他命戒斷期，患者常會因多巴胺耗竭出現「崩潰（crash）」現象，表現為嚴重憂鬱、疲倦、嗜睡，此種戒斷憂鬱通常是暫時且自限性的，不需要使用情緒穩定劑（如 carbamazepine）治療。\n\n【選項詳解】\n- A. 正確。個案的精神病症狀是由安非他命引起的，因此治療的第一步與最根本處置是立即停止使用安非他命，以切斷外源性刺激。\n- B. 正確。由於安非他命會促進多巴胺大量釋放，短期使用第一代（如 haloperidol）或第二代抗精神病藥阻斷多巴胺受體，能有效控制幻覺、妄想與嚴重躁動。\n- C. 正確. 患者出現打傷同事的暴力行為，若在急診或病房難以照顧且有自傷傷人危險時，可進行保護性肢體約束，但必須密切觀察其呼吸及生命徵象，以防發生橫紋肌溶解症。\n- D. 錯誤（本題答案）。安非他命戒斷引起的憂鬱症狀，主因是多巴胺受體敏感度降低及神經傳導物質耗竭，一般以支持性治療為主；情緒穩定劑（如 carbamazepine）主要用於雙極性障礙症或癲癇，在此處並無療效，且 carbamazepine 具有嚴重的藥物交互作用與嚴重的皮膚副作用（如史蒂芬強生症候群 SJS），不應給予。\n\n【核心考點】\n安非他命誘發之精神病態（amphetamine-induced psychosis）的處置：\n1. 根本治療：停用安非他命。\n2. 急性精神症狀與躁動：短期使用抗精神病藥物（D2 antagonist）控制。\n3. 戒斷期憂鬱：支持療法為主，而非使用情緒穩定劑（如 carbamazepine）。",
    "key_point": "安非他命誘發之精神症狀應以停藥和短期抗精神病藥治療；戒斷憂鬱是多巴胺耗竭引起，不使用情緒穩定劑（如 carbamazepine）治療。",
    "flashcard_front": "對於安非他命濫用引發聽幻覺、被害妄想與易怒躁動的患者，下列處置敘述何者錯誤？",
    "flashcard_back": "若有憂鬱症狀可給予情緒穩定劑（如 carbamazepine）。安非他命戒斷憂鬱通常是支持治療或用抗憂鬱藥，不需使用情緒穩定劑。",
    "flashcard_summary": "安非他命精神病態 -> 處置為停藥、短期使用D2拮抗劑，約束需防橫紋肌溶解；戒斷憂鬱不給carbamazepine。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_067",
    "question_id": "109-1_medicine-4_067",
    "question_number": 67,
    "explanation": "【題幹解析】\n本題詢問「虛談（confabulation）」最可能代表何種精神障礙。標準答案為 C。虛談是指患者在意識清楚的狀態下，為了填補記憶中的空白（如順向或逆向遺忘），而在無意中編造出虛構的故事、情節或經歷，且患者本身深信其為真實。這是典型的「記憶障礙（memory impairment）」，最經典的臨床例子是因長期酗酒導致維生素 B1（thiamine）缺乏所引起的科薩科夫症候群（Korsakoff's syndrome）。\n\n【選項詳解】\n- A. 錯誤。思考障礙常見的表現是妄想（delusion）、思考流程鬆散（looseness of association） or 思考中斷（thought blocking），而虛談是因記憶缺損而填補內容的產物，本質上不屬於思考障礙。\n- B. 錯誤。情緒障礙表現為憂鬱、焦慮、躁狂或情感平淡等，與編造記憶填補空白的虛談症狀無關。\n- C. 正確。虛談是記憶障礙（遺忘症）的代償性表現。患者大腦無法形成或提取真實記憶，為了應對外界提問，便自動抓取過去的片段或虛構內容來「填補」記憶漏洞，常見於 Korsakoff's syndrome 或額葉受損。\n- D. 錯誤。語言障礙（如失語症 aphasia）表現為表達或理解語言困難、發音不清等。虛談症患者通常說話流暢、語法正確，只是說出的內容是虛構的記憶，因此非語言障礙。\n\n【核心考點】\n虛談（confabulation）的定義與機轉：它是為了填補嚴重「記憶缺失」而產生的無意編造行為，屬於「記憶障礙」。常見於維生素 B1 缺乏導致的 Wernicke-Korsakoff syndrome，病理位置主要在乳頭體（mammillary bodies）及視丘內側核心。",
    "key_point": "虛談（confabulation）是個案為了填補嚴重的記憶缺失而無意中編造的故事，屬於記憶障礙，經典病因為科薩科夫症候群。",
    "flashcard_front": "精神醫學中，患者因記憶缺失而在意識清醒時編造故事填補空白的「虛談（confabulation）」症狀，最主要屬於何種障礙？",
    "flashcard_back": "記憶（memory）障礙。常見於酗酒引發維生素B1缺乏的科薩科夫症候群。",
    "flashcard_summary": "虛談 -> 記憶障礙，代償性填補遺忘，常見於Korsakoff's syndrome（維生素B1缺乏）。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_068",
    "question_id": "109-1_medicine-4_068",
    "question_number": 68,
    "explanation": "【題幹解析】\n本題考查咖啡因（caffeine）戒斷症狀的臨床特點。標準答案為 B。當習慣每日攝取咖啡因的個案突然停止或顯著減量時，會引發戒斷反應。此反應通常在停用後的 12 至 24 小時內即開始發作，並在 20-51 小時達到高峰，持續約 2-9 天。其最常見且特徵性的症狀是血管舒縮性頭痛（因失去咖啡因的血管收縮作用而導致腦血管擴張）以及顯著的倦怠與疲勞。戒斷症狀的嚴重程度與先前咖啡因的每日攝取量成正比。\n\n【選項詳解】\n- A. 錯誤。咖啡因的半衰期較短，戒斷症狀通常在停用或減量後 12 至 24 小時內就迅速出現，而非一星期後才發生。\n- B. 正確。頭痛（headache）與倦怠/疲勞（fatigue/drowsiness）是咖啡因戒斷最典型且出現率最高的兩大臨床表現，其他症狀包括易怒、注意力無法集中與輕微抑鬱。\n- C. 錯誤。咖啡因戒斷不會導致幻聽、被害妄想等精神病性症狀（psychotic symptoms）；幻覺妄想主要是中樞興奮劑（如安非他命）中毒，或酒精、鎮靜安眠藥嚴重戒斷（如譫妄）的表現。\n- D. 錯誤。研究與臨床觀察顯示，咖啡因戒斷症狀的嚴重程度及發生率，與個案平時每日的咖啡因攝取量（使用量）呈明顯的正相關。\n\n【核心考點】\n咖啡因戒斷症候群（Caffeine withdrawal）：\n1. 發作時間：停藥後 12-24 小時。\n2. 典型症狀：頭痛（最典型）、倦怠、易怒。\n3. 嚴重度：與平時每日攝取總量呈正相關。",
    "key_point": "咖啡因戒斷症狀通常在停藥後 12-24 小時內發生，最常見為頭痛與倦怠，嚴重度與平時使用量呈比。",
    "flashcard_front": "關於咖啡因（caffeine）的戒斷症狀，下列敘述何者正確？",
    "flashcard_back": "最常見症狀包括頭痛、倦怠。症狀通常在停用後 12-24 小時內發生，且嚴重度與平時攝取量呈正相關。",
    "flashcard_summary": "咖啡因戒斷 -> 停藥12-24小時內發作，最典型為頭痛與倦怠，嚴重度與使用量呈正相關。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_069",
    "question_id": "109-1_medicine-4_069",
    "question_number": 69,
    "explanation": "【題幹解析】\n本題詢問注意力不足過動症（ADHD）的診斷標準何者錯誤。官方最後更正為多重答案，選 A 或 B 均給分（即 A、B 均為錯誤敘述）。\n在 DSM-5 診斷標準中，部分過動-衝動或注意力不足的症狀必須在「12歲之前」（舊版 DSM-IV 為 7 歲之前）即已出現，因此 A 選項在現行 DSM-5 標準下是錯誤的。此外，ADHD 診斷要求症狀必須在「兩個或更多情境」（如學校和家裡）中出現，因此 B 選項「只要在一個情境中出現就算」亦是錯誤的。\n\n【選項詳解】\n- A. 正確（本選項敘述錯誤，符合題意）。根據 DSM-5 診斷標準，部分過動-衝動或注意力不足的症狀必須在「12 歲之前」就已出現。DSM-IV 的舊標準才是「7 歲之前」。因此，本敘述以現行標準而言是錯誤的。\n- B. 正確（本選項敘述錯誤，符合題意）。ADHD 診斷的關鍵條件之一是跨情境性，症狀必須在「兩個或兩個以上的情境」（如家裡、學校、工作、與朋友或親戚相處時）中顯現並造成影響。單一情境出現的症狀多與環境適應或特定關係有關，不符合 ADHD 診斷。\n- C. 錯誤（本選項敘述正確，不符題意）。診斷 ADHD 的必要條件是這些症狀必須有明確證據顯示其干擾了社交、學業或職業功能，或降低了上述功能的品質。\n- D. 錯誤（本選項敘述正確，不符題意）。ADHD 必須與其他可能導致注意力不集中或衝動的精神疾病進行鑑別診斷（排他條款），包括廣泛性發展障礙（自閉症譜系）、思覺失調症、焦慮症或雙極性障礙等。\n\n【核心考點】\nDSM-5 中注意力不足過動症（ADHD）的診斷準則要點：\n1. 年齡限制：部分症狀必須在 12 歲以前出現（舊版 DSM-IV 為 7 歲）。\n2. 情境要求：必須在兩個或更多情境中表現（如學校與家庭）。\n3. 功能損害：必須造成社交、學業或職業功能損害。",
    "key_point": "ADHD的診斷標準要求症狀在12歲前（非7歲）即出現，且必須在兩個或以上的情境中發生，並造成功能損害。",
    "flashcard_front": "關於注意力不足過動症（ADHD）在DSM-5中的診斷標準，下列敘述何者錯誤？（提示：本題官方公告多重給分）",
    "flashcard_back": "「在7歲前出現」與「在單一情境中出現即可」均為錯誤。現行標準為症狀需在12歲前出現，且必須在至少兩個情境（如家庭與學校）中顯現。",
    "flashcard_summary": "ADHD診斷標準 -> 症狀發病於12歲前，必須跨越兩個以上情境，且造成社交/學業/工作功能損害。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  },
  {
    "id": "109-1_medicine-4_070",
    "question_id": "109-1_medicine-4_070",
    "question_number": 70,
    "explanation": "【題幹解析】\n本題詢問關於妥瑞氏症（Tourette's disorder）的敘述何者正確。標準答案為 D。妥瑞氏症是一種神經發育障礙，其病生理學與基底核多巴胺通路過度活躍密切相關。因此，多巴胺受體拮抗劑（例如 haloperidol、aripiprazole、pimozide）能有效減少 tics 的發生。在診斷上，必須同時具有「多種動作抽動」及「一種或多種聲帶抽動」（不需同時出現，但病程中皆曾出現過），且持續一年以上。\n\n【選項詳解】\n- A. 錯誤。妥瑞氏症的診斷標準要求在病程中必須「動作抽動（motor tics）」與「聲帶/發聲抽動（vocal tics）」兩者皆曾出現過（不一定要同時發生），若只出現單一種，則僅能診斷為持續性動作或聲帶抽動症。\n- B. 錯誤。雖然多數妥瑞氏症患者的症狀在青春期後會逐漸減輕或消退，但並非「所有」患者成年後都會痊癒，部分病人（約 10-20%）的症狀會持續到成年，甚至造成終身障礙。\n- C. 錯誤。妥瑞氏症具有強烈的遺傳傾向，同卵雙胞胎（monozygotic twins）的一致率（約 50-70%）顯著高於異卵雙胞胎（dizygotic twins，約 10%），兩者罹病機會不同。\n- D. 正確。妥瑞氏症的發生與大腦基底核（basal ganglia）的多巴胺過度敏感或活性過高有關，臨床上使用多巴胺受體拮抗劑（D2 antagonist，如 haloperidol、pimozide 或較新型的 aripiprazole）阻斷多巴胺活性，具有顯著改善抽動症狀的療效。\n\n【核心考點】\n妥瑞氏症（Tourette's disorder）的診斷與治療：\n1. 診斷條件：多種動作 tic + 至少一種聲帶 tic，持續 > 1年，18歲前發病。\n2. 遺傳學：高度遺傳性，同卵雙胞胎一致率高於異卵。\n3. 藥物治療：以多巴胺受體拮抗劑（D2 blockers）或 alpha-2 腎上腺素受體阻斷劑為主要藥物選擇。",
    "key_point": "妥瑞氏症的診斷需同時具備動作與聲帶抽動，其機轉與多巴胺過度活躍有關，故多巴胺拮抗劑具明確療效。",
    "flashcard_front": "關於妥瑞氏症（Tourette's disorder）的診斷標準與治療，下列敘述何者正確？",
    "flashcard_back": "作用在多巴胺受體拮抗作用的抗精神病藥物具有療效。診斷需同時包含動作與聲帶抽動，且同卵一致率顯著高於異卵。",
    "flashcard_summary": "妥瑞氏症 -> 診斷需動作+聲帶tic均曾出現，高度遺傳性，多巴胺拮抗劑（D2 antagonist）為有效藥物。",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-12T21:26:00+08:00",
    "manual_review_notes": []
  }
]

output_dir = 'scratch/rewrite_updates/109-1_medicine-4'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'q061-q070.json')

output_data = {
  "source_file": "public/data/exams/109-1/medicine-4.json",
  "dataset_id": "109-1_medicine-4",
  "range": {
    "start": 61,
    "end": 70
  },
  "updates": updates
}

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("Successfully written to", output_path)
