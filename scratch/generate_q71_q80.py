# -*- coding: utf-8 -*-
import json
import os

source_file = "public/data/exams/110-1/medicine-6.json"
dataset_id = "110-1_medicine-6"
output_dir = "d:/Antigravity/med_exam_public/scratch/rewrite_updates/110-1_medicine-6"
output_file = os.path.join(output_dir, "q071-q080.json")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

updates = []

# Question 71
q71_explanation = """【題幹解析】
腋網症候群（axillary web syndrome, AWS）又稱條索化（cording），主要發生在腋下淋巴結被破壞或殘留淋巴管受到干擾後。本題旨在詢問哪種癌症手術後最常出現此疼痛與上肢活動受限的症狀。乳癌手術常合併腋下淋巴結清除術（ALND）或前哨淋巴結切片（SLNB），為 AWS 最典型的誘發手術。

【選項詳解】
- A. 錯誤。頭頸癌手術主要涉及頸部淋巴結清創（neck dissection），其手術區域位於頭頸部及鎖骨上方，並未觸及腋下淋巴系統，因此不會引發腋網症候群。
- B. 錯誤。肺癌手術一般進行開胸或胸腔鏡手術（VATS）以及縱隔腔淋巴結清除（mediastinal lymph node dissection），其清除範圍在胸腔及縱隔腔內部，並非腋下區域，因此不會造成腋網症候群。
- C. 正確。乳癌手術不論是乳房全切除或部分切除，只要涉及腋下淋巴結清創（ALND）或前哨淋巴結切片（SLNB），便可能因淋巴管與小血管發炎、纖維化與栓塞，在腋下及手臂內側形成可觸及的緊繃條索狀物，導致局部疼痛與肩膀活動受限。
- D. 錯誤。口腔癌手術主要進行原發病灶切除及頸部淋巴結清創，手術切口與淋巴清掃範圍局限於頸部以上，與腋下解剖區域無關，不會發生腋網症候群。

【核心考點】
腋網症候群（AWS）是乳癌手術（涉及腋下淋巴處理）特有的術後早期併發症，其病理機轉與腋下淋巴管及血管的血栓性靜脈炎或纖維化條索化有關，臨床上會限制上肢的伸展與外展活動。"""

updates.append({
    "question_id": "110-1_medicine-6_071",
    "question_number": 71,
    "explanation": q71_explanation,
    "key_point": "腋網症候群（AWS）是乳癌手術（涉及腋下淋巴處理）特有的術後早期併發症，其病理機轉與腋下淋巴管及血管的血栓性靜脈炎或纖維化條索化有關。",
    "flashcard_front": "乳癌手術 / 腋下淋巴結摘除 / 緊繃條索狀物 / 腋網症候群 (AWS)",
    "flashcard_back": "腋網症候群(AWS)是乳癌手術切除淋巴後常見的併發症，表現為腋下至手臂的纖維化條索緊繃與疼痛。",
    "flashcard_summary": "乳癌術後腋網症候群 -> 腋網症候群是乳癌手術切除淋巴後常見的腋下條索狀緊繃併發症。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 72
q72_explanation = """【題幹解析】
本題詢問骨盆腔囊狀病灶在 MRI 影像上的特徵性表現。當囊腫在 T1 加權影像（T1WI）呈高訊號（亮），且在 T2 加權影像（T2WI）呈現訊號衰減的稍低訊號時，此現象稱為 T2 陰影效應（T2 shading sign）。這是陳舊出血、含鐵血黃素（hemosiderin）及高濃度蛋白質蓄積的典型表徵，最符合巧克力囊腫（子宮內膜異位瘤）的影像特點。

【選項詳解】
- A. 正確。巧克力囊腫（chocolate cyst，子宮內膜異位瘤）內部充滿反覆出血累積的陳舊血液。血液隨時間分解，高濃度的鐵離子與蛋白質產生磁化率效應，使得病灶在 T1WI 呈現顯著的高訊號，並在 T2WI 呈現訊號衰減的低至稍低訊號（T2 shading sign），與題幹影像描述完全相符。
- B. 錯誤。卵巢癌（ovarian cancer）多呈現實質性或混合性囊實構造，其囊狀部分在 T2WI 通常呈現明顯的高訊號（亮），實質部分則常有早期不均勻顯影，極少表現為單純的 T2 shading 影像。
- C. 錯誤。輸卵管卵巢膿瘍（tubo-ovarian abscess, TOA）屬於急性發炎性積膿，囊內以發炎細胞及壞死組織液為主，在 T1WI 呈低訊號，T2WI 呈顯著高訊號，且常伴隨周邊囊壁的增厚及顯著強化。
- D. 錯誤。畸胎瘤（teratoma）內部含有大量脂肪與皮脂物質，在 T1WI 及 T2WI 雖然皆呈高訊號，但其高訊號來源為脂肪。在臨床診斷中，若使用脂肪抑制技術（fat saturation sequence）時，畸胎瘤的高訊號會被壓抑至低訊號，此與巧克力囊腫的 T2 shading 機轉截然不同。

【核心考點】
子宮內膜異位瘤（巧克力囊腫）在 MRI 上的診斷關鍵在於 T1 加權高訊號、T2 加權呈低訊號的「T2 shading sign」，其原理是囊內陳舊性出血中的鐵離子所致。"""

updates.append({
    "question_id": "110-1_medicine-6_072",
    "question_number": 72,
    "explanation": q72_explanation,
    "key_point": "子宮內膜異位瘤（巧克力囊腫）在 MRI 上的診斷關鍵在於 T1 加權高訊號、T2 加權呈低訊號的「T2 shading sign」。",
    "flashcard_front": "骨盆腔囊腫 / T1高訊號 / T2稍低訊號 (T2 shading) / 巧克力囊腫",
    "flashcard_back": "在MRI上呈現T1高訊號、T2低訊號(shading sign)的骨盆腔囊腫為巧克力囊腫，與陳舊出血有關。",
    "flashcard_summary": "巧克力囊腫MRI特徵 -> 巧克力囊腫在 T1 呈高訊號，在 T2 呈低訊號（T2 shading sign）。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 73 (Negative question: 何者診斷為錯誤)
q73_explanation = """【題幹解析】
本題為否定題，要求選出「錯誤」的診斷。當膝關節遭受強大外力扭傷時（如旋轉剪力），常引發前十字韌帶（ACL）斷裂。此種創傷機制在影像學上有其特徵性伴隨表現，包括股骨外側髁與脛骨後外側的撞擊骨挫傷（bone contusion），以及脛骨外側平台的撕裂性骨折（Segond fracture）。根據該病例的特定影像，患者並未合併外側半月板撕裂（lateral meniscal tear），故選項 C 為錯誤診斷，為本題之正確答案。

【選項詳解】
- A. 正確（描述符合病人實際情況，非本題答案）。病患的磁振造影（MRI）顯示前十字韌帶（ACL）的連續性中斷，呈明顯的 ACL 斷裂（anterior cruciate ligament tear）。
- B. 正確（描述符合病人實際情況，非本題答案）。由於關節受傷時骨頭發生瞬間撞擊（常為 pivot-shift 機制），在 MRI 的 T2/PD 訊號上可見股骨外側髁（lateral femoral condyle）與脛骨後外側（posterior lateral tibia）有高訊號的骨髓水腫，即骨挫傷（bone contusion）。
- C. 錯誤（描述與病人影像不符，為本題應選之錯誤診斷）。該患者的影像學表現並無外側半月板（lateral meniscus）游離緣中斷或異常高訊號，意即沒有外側半月板撕裂（lateral meniscal tear），故此診斷不正確。
- D. 正確（描述符合病人實際情況，非本題答案）。X 光片中可看見脛骨外側平台邊緣有微小的游離骨折碎片，即 Segond fracture。這是由外側副韌帶（LCL）的髂脛束（ITB）或前外側韌帶（ALL）扯落所致，是前十字韌帶斷裂的特徵性間接影像表徵。

【核心考點】
前十字韌帶（ACL）急性斷裂在影像上的關鍵伴隨表徵包括：X 光上的 Segond 骨折（對 ACL 斷裂的特異性極高）以及 MRI 上因撞擊造成的股骨外側髁與脛骨後外側骨挫傷（bone contusion）。"""

updates.append({
    "question_id": "110-1_medicine-6_073",
    "question_number": 73,
    "explanation": q73_explanation,
    "key_point": "前十字韌帶（ACL）急性斷裂在影像上的關鍵伴隨表徵包括：X 光上的 Segond 骨折以及 MRI 上因撞擊造成的股骨外側髁與脛骨後外側骨挫傷。",
    "flashcard_front": "膝部受傷 / ACL斷裂 / 骨挫傷 / Segond fracture / 半月板撕裂",
    "flashcard_back": "ACL斷裂常伴隨Segond骨折與骨挫傷，且半月板撕裂好發於內側而非外側半月板。",
    "flashcard_summary": "ACL斷裂伴隨損傷 -> 常合併Segond骨折與骨挫傷，半月板受損多為內側而非外側。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 74 (Negative question: 何者錯誤)
q74_explanation = """【題幹解析】
本題為否定題，要求選出關於頸動脈狹窄治療與診斷的「錯誤」敘述。頸動脈狹窄（carotid stenosis）的治療策略取決於患者「是否有症狀（如近期發生過 TIA 或缺血性中風）」以及「狹窄嚴重程度」。無症狀的重度頸動脈狹窄（通常為狹窄率大於 60% 至 70% 以上且預期壽命大於5年者），除了接受內科藥物治療外，適度給予血管重建手術或支架置放，能更有效預防未來中風的風險，並非「無論嚴重程度均僅用內科治療即可」。

【選項詳解】
- A. 正確（敘述符合醫學原則，非本題答案）。有症狀的頸動脈狹窄，若狹窄程度大於 50-60% 以上，為降低短期內再次中風的機率，臨床指引強烈建議考慮進行頸動脈內膜切除術（CEA）或頸動脈支架置放術（CAS）。
- B. 錯誤（敘述不符合醫學原則，為本題應選之錯誤敘述）。對於無症狀的頸動脈狹窄，若狹窄嚴重度大於 60%-70%，且病人的手術風險較低時，進行手術（CEA）或支架（CAS）介入治療比起單純內科藥物，能顯著降低同側缺血性中風的發生率，因此「無論嚴重度皆不需手術」是錯誤的。
- C. 正確（敘述符合醫學原則，非本題答案）。在血流動力學中，總頸動脈分支處（carotid bifurcation）因分流產生紊流（turbulent flow）與高剪力，是斑塊最好發的解剖位置。
- D. 正確（敘述符合醫學原則，非本題答案）。頸部磁振血管影像（MRA）為非侵入性檢查，能清晰呈現血管的三維結構，與頸動脈超音波、電腦斷層血管攝影（CTA）同為診斷頸動脈狹窄的關鍵影像工具。

【核心考點】
無症狀的重度頸動脈狹窄（>60%）且預期壽命大於5年者，進行頸動脈內膜切除術（CEA）或支架置放術（CAS）介入治療比單純藥物更有效降低中風風險。"""

updates.append({
    "question_id": "110-1_medicine-6_074",
    "question_number": 74,
    "explanation": q74_explanation,
    "key_point": "無症狀的重度頸動脈狹窄（>60%）且預期壽命大於5年者，可考慮手術（CEA）或支架（CAS）介入治療以預防中風。",
    "flashcard_front": "頸動脈狹窄 / 無症狀狹窄 / 外科手術 (CEA) / 內科藥物治療",
    "flashcard_back": "無症狀的頸動脈狹窄若程度嚴重（>60%），仍可考慮手術或支架治療，非一律僅用內科治療。",
    "flashcard_summary": "無症狀頸動脈狹窄處置 -> 嚴重度高於60-70%時，無症狀患者亦可考慮手術或支架預防中風。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 75
q75_explanation = """【題幹解析】
本題旨在評估產後出血（postpartum hemorrhage, PPH）的病因、臨床病理生理變化與藥物使用禁忌。產後出血的處置強調即時的生命徵象穩定（ABC）與針對病因的子宮收縮藥物選擇。麥角生物鹼（如 methylergonovine）由於會刺激血管收縮，對於本身已有血管內皮受損、血管收縮異常的高血壓或子癇前症孕婦，容易誘發嚴重高血壓危象或腦血管意外，為臨床禁忌。

【選項詳解】
- A. 錯誤。造成產後出血最常見的原因是子宮收縮無力（uterine atony），約佔所有產後出血原因的 70% 至 80%；子宮內翻（uterine inversion）屬於極罕見但危急的產科併發症，並非最常見原因。
- B. 錯誤。懷孕期間孕婦血容量顯著增加（代償性上升 30% 至 50%）。因此，當發生產後出血時，機體會維持代償狀態，血壓往往在失血量極大時才會突然崩潰；心搏過速（tachycardia）才是反映血容量不足、產後出血最早且最靈敏的代償性臨床徵兆。
- C. 錯誤。面對產後出血患者，急診處理的第一步驟應是建立靜脈通路、給予靜脈輸液、輸血並監測生命徵象以穩定血流動力學（即穩定 ABC），而非先會診。在穩定生命徵象的同時，即可同步由產科人員進行子宮按摩與藥物治療。
- D. 正確。麥角生物鹼（ergot alkaloids，如 Methergine）可刺激子宮平滑肌收縮以達到止血效果，但該藥會同時引發全身小動脈強烈收縮。這會使血壓顯著上升，因此在合併子癇前症（pre-eclampsia）或妊娠高血壓的產後出血病患中為禁用藥物。

【核心考點】
產後出血最常見原因為子宮收縮無力（atony）；早期失血之代償徵兆為心搏過速而非低血壓。子宮收縮劑 Methergine 具有強烈收縮血管及升壓作用，禁用於高血壓或子癇前症患者。"""

updates.append({
    "question_id": "110-1_medicine-6_075",
    "question_number": 75,
    "explanation": q75_explanation,
    "key_point": "產後出血最常見原因為子宮收縮無力，早期代償為心搏過速；Methergine 具升壓作用，禁用於高血壓或子癇前症者。",
    "flashcard_front": "產後出血 / 子癇前症 / 麥角生物鹼 (Methergine) / 心搏過速",
    "flashcard_back": "麥角生物鹼會升高血壓，子癇前症孕婦的產後出血禁用；早期出血徵兆是心搏過速而非低血壓。",
    "flashcard_summary": "產後出血與麥角生物鹼 -> 麥角生物鹼因會升壓，是子癇前症孕婦產後出血的絕對禁忌。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 76 (Negative question: 何者最不適當)
q76_explanation = """【題幹解析】
本題為否定題，要求選出外耳道異物沖洗時「最不適當」的處置。利用清水灌洗外耳道是移除小而無卡死異物的常用方法，但在進行沖洗前，必須嚴格評估耳膜完整性與異物性質。沖洗液的溫度必須與人體核心體溫相近，若溫度相差過大，會產生溫差刺激，誘發嚴重的不良生理反應。

【選項詳解】
- A. 適當（非本題答案）。若耳膜已有破裂，沖洗液會流入中耳腔，可能引發中耳炎、劇烈疼痛，或導致沖洗液及異物進一步往中耳及內耳方向位移，故沖洗前必須以耳鏡確認耳膜完整。
- B. 不適當（為本題應選之錯誤敘述）。沖洗外耳道所使用的水溫必須接近體溫（約 37°C）。若使用冰水或熱水沖洗，會使外耳道與內耳半規管之間產生溫差，引發內淋巴液對流，造成溫差試驗（caloric test）效應，導致患者產生嚴重的眩暈（vertigo）、眼球震顫（nystagmus）及嘔吐。
- C. 適當（非本題答案）。若外耳道異物為吸水性物質（如豆類、穀物等種子或棉花），沖洗會使其吸水膨脹，反而將外耳道卡得更緊，增加取出難度及壓迫組織風險，因此這類異物禁用清水沖洗。
- D. 適當（非本題答案）。異物移出後，必須再次使用耳鏡細心評估，確認外耳道上皮是否受損、耳膜有無穿孔，或聽小骨鏈有無在異物卡入或取出過程中受到機械性傷害，以做後續的預防治療。

【核心考點】
外耳道沖洗的水溫必須接近體溫（37°C），以防溫差效應引發眩暈與眼震；此外，耳膜破裂者、吸水性異物（如植物種子）或鈕扣電池皆為清水沖洗之禁忌症。"""

updates.append({
    "question_id": "110-1_medicine-6_076",
    "question_number": 76,
    "explanation": q76_explanation,
    "key_point": "外耳道沖洗水溫必須接近體溫（37°C），否則會因溫差效應引發嚴重眩暈；耳膜破裂與吸水性異物為沖洗禁忌。",
    "flashcard_front": "外耳道異物 / 清水沖洗 / 沖洗液溫度 / 眩暈與眼震",
    "flashcard_back": "沖洗外耳道須使用接近體溫(37°C)的溫水，若使用冰水會刺激前庭半規管引發嚴重眩暈與眼震。",
    "flashcard_summary": "外耳道沖洗溫度 -> 沖洗須用接近體溫的溫水，冰水會引發前庭刺激與眩暈。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 77
q77_explanation = """【題幹解析】
本題考查常用局部麻醉藥物 Lidocaine（利多卡因）在合併使用血管收縮劑（Epinephrine）時的最大安全劑量計算。Lidocaine 會使局部血管擴張，增加藥物全身吸收的速度與系統性毒性風險。加入 Epinephrine 能使局部血管收縮，延緩 Lidocaine 的吸收，進而延長麻醉時間、減少術中出血，並提升安全劑量上限。

【選項詳解】
- A. 錯誤。100 mg 遠低於該體重下 Lidocaine 的最大安全劑量，在臨床上無法為大範圍的臉部創傷提供充足的局部麻醉用藥額度。
- B. 錯誤。250 mg 接近單獨使用 Lidocaine 時的最大劑量，但未達到併用血管收縮劑時的上限值。
- C. 正確。單獨使用 Lidocaine 的安全劑量為 4.5 mg/kg（最大總劑量上限為 300 mg）；當併用 Epinephrine（通常為 1:200,000 比例）時，安全劑量可提高至 7 mg/kg（最大總劑量上限為 500 mg）。針對 72 公斤的患者，依體重計算為 72 * 7 = 504 mg，但由於設有 500 mg 的絕對總量上限，故其最高安全劑量為 500 mg。
- D. 錯誤。700 mg 已顯著超出 Lidocaine 併用血管收縮劑時的 500 mg 最大總量限制，極易誘發局麻藥全身性毒性（LAST），包括中樞神經系統興奮（如抽搐）及心血管抑制。

【核心考點】
局部麻醉劑 Lidocaine 單獨使用上限為 4.5 mg/kg（最大總量 300 mg）；併用 Epinephrine 的上限為 7 mg/kg（最大總量 500 mg）。"""

updates.append({
    "question_id": "110-1_medicine-6_077",
    "question_number": 77,
    "explanation": q77_explanation,
    "key_point": "局部麻醉劑 Lidocaine 單獨使用上限為 4.5 mg/kg（總量限 300 mg）；併用 Epinephrine 的上限為 7 mg/kg（總量限 500 mg）。",
    "flashcard_front": "Lidocaine / Epinephrine併用 / 72公斤 / 最高麻醉安全劑量",
    "flashcard_back": "Lidocaine併用血管收縮劑最大安全劑量為7 mg/kg，且總上限為500 mg，72公斤者最高安全劑量即為500 mg。",
    "flashcard_summary": "Lidocaine麻醉上限 -> 併用腎上腺素時最大安全劑量為7 mg/kg（總量上限500 mg）。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 78 (Negative question: 但不包括下列那一個)
q78_explanation = """【題幹解析】
本題為否定題，要求指出該案例中「沒有」違反的醫療倫理原則。醫師在為病人移除外耳道異物的過程中，發現「中耳積水」這一非立即致命且非緊急的狀況。在未獲得病人充分說明並同意的情況下，逕自執行中耳引流管置放手術，屬於侵入性醫療行為。這違反了與知情同意（informed consent）及尊重病人自主權（autonomy）相關的倫理規範，但此情境並未涉及患者隱私外洩。

【選項詳解】
- A. 錯誤（該原則已被違反，非本題答案）。醫師在執行侵入性的中耳引流管置放前，有責任先向病人解釋其病情、治療選項、潛在風險及利益，未作說明即直接動手，違反了「告知義務」。
- B. 錯誤（該原則已被違反，非本題答案）。知情同意（informed consent）要求病人在理解病情及治療計畫後，出於自主意志簽署或表達同意。醫師直接放引流管完全跳過了此一倫理與法律程序，違反了「知情同意」原則。
- C. 正確（該原則未被違反，為本題應選之正確答案）。守密義務（confidentiality）是指保護病人的醫療隱私資訊，不被未授權的第三方知悉。本案例中醫師雖然擅自做手術，但並未將病人的隱私或病歷洩漏給他人，因此沒有違反「守密」原則。
- D. 錯誤（該原則已被違反，非本題答案）。尊重病人自主決定權（respect for autonomy）是現代醫療倫理的核心，病人有權決定自己的身體接受何種醫療處置。醫師代替病人做決定並直接施作手術，公然違反了病人的「自主決定」權。

【核心考點】
非緊急的醫療處置必須在病患充分知情並表達同意後方可執行，否則將違反告知義務與自主決定權。守密義務（confidentiality）則關乎病患個人資訊與隱私的保護。"""

updates.append({
    "question_id": "110-1_medicine-6_078",
    "question_number": 78,
    "explanation": q78_explanation,
    "key_point": "非緊急的醫療處置必須在病患充分知情並獲得授權後方可執行，否則違反告知與自主原則；守密義務著重於隱私保護。",
    "flashcard_front": "中耳積水 / 未徵求同意 / 直接放置引流管 / 醫學倫理 / 守密",
    "flashcard_back": "未取得病人知情同意擅自進行非緊急處置，違反告知、知情同意與自主，未違反守密。",
    "flashcard_summary": "未授權醫療處置倫理 -> 違反告知與知情同意原則，但與守密義務無關。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 79
q79_explanation = """【題幹解析】
本題考查醫療專業邊界（professional boundaries）與醫學倫理的實際應用。醫師與其正在診治的病人發生情感或親密關係，會破壞客觀專業判斷，影響病人福祉與信任。當醫院發現此類違反邊界的事件時，首要考量是保護病人的醫療權益，避免專業邊界重疊造成的利害衝突，因此院方的最佳也是最迫切處置是轉移病人的照護權。

【選項詳解】
- A. 正確。醫師與現診病人建立親密或感情關係，會嚴重干擾醫療決策的客觀公正性。院方首要職責在於重建專業的醫療邊界，因此必須「應該立即中止這位醫師與病人間的醫療關係」，並安排病人轉診予其他醫師，以確保病人的醫療安全與權益。
- B. 錯誤。醫師的感情私生活或婚姻狀況雖有道德瑕疵，但醫院無權且沒有法律地位主動向其配偶披露相關隱私，若立即告知其配偶，反而違反了員工隱私保護及機構行政邊界。
- C. 錯誤。雖然情感關係涉及私人層面，但由於對象是該醫師「正在診治的病人」，此行為直接跨越了醫病關係的專業邊界，存在權力不對等與決策偏頗風險，並非「純屬個人隱私、醫院不必理會」的私人事務。
- D. 錯誤。立即中止該醫師的所有醫療職務（即停職或解僱）屬於嚴重的行政懲處，在未經院內倫理委員會或人事單位正式調查、釐清事實真相前，逕行採取此一極端處分並不符合比例原則與程序正義。

【核心考點】
維護醫病關係的「專業邊界（professional boundaries）」至關重要。當醫師與現有患者發生情感親密關係時，為防範利益衝突並維護決策客觀，院方必須立即中止其直接醫病關係並進行轉介。"""

updates.append({
    "question_id": "110-1_medicine-6_079",
    "question_number": 79,
    "explanation": q79_explanation,
    "key_point": "當醫師與現有患者發生情感或親密關係時，為維護專業邊界與決策客觀性，院方應立即中止該醫病關係並安排轉介。",
    "flashcard_front": "醫師與病人 / 婚外情 / 專業邊界 / 院方首要處置",
    "flashcard_back": "醫師與病人發生親密關係違反專業邊界，院方首要處置為立即中止其醫療關係並轉介病人。",
    "flashcard_summary": "醫病關係專業邊界 -> 醫師與患者有親密關係時，院方應立即中止其醫療關係並進行轉介。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Question 80
q80_explanation = """【題幹解析】
本題考查《赫爾辛基宣言》（Declaration of Helsinki）中關於臨床試驗與常規醫療照護結合時的倫理規範。當主治醫師同時擔任研究者時，容易產生治療者角色與研究者角色的利益衝突。宣言對此做出了明確的限制，旨在確保任何結合研究的照護方案，都必須建立在對病人有潛在臨床實質益處，且能將健康損害風險降至最低的前提下。

【選項詳解】
- A. 錯誤。該選項僅提到「不會對健康有不良影響」，漏掉了《赫爾辛基宣言》中規定的另一核心要素：該研究必須對病人具有「潛在的預防、診斷或治療價值」，醫師不能在對病人無任何潛在臨床益處的情況下，僅因其無害就將其納入研究。
- B. 錯誤。赫爾辛基宣言並不禁止將醫學研究與醫療照護相結合。在許多情況下（如新藥或新型療法的開發），將研究融入臨床照護中能為面臨現有療法瓶頸的病人帶來一線曙光，因此兩者是可以且在適當規範下應該結合的。
- C. 正確。根據赫爾辛基宣言第37條（或相關結合條款），醫師只有在此研究具有「潛在的預防、診斷或治療價值」，並且醫師有充足的理由相信參與該研究不會對病人的健康產生任何不良影響（不損害病人的最大福祉）時，才能將研究與醫療照護相結合。
- D. 錯誤。僅有行政或主管機關核准（如 IRB 審查、政府核可）是必要程序，但不能以此取代醫師的個人專業倫理判斷。醫師必須對病人的健康與福祉負起第一線責任，並確認研究符合宣言中的潛在利益與安全標準。

【核心考點】
《赫爾辛基宣言》規定，結合醫學研究與臨床照護的前提為：研究必須對病患具潛在預防、診斷或治療價值，且有充足理由確信參與不會對其健康造成不良影響。"""

updates.append({
    "question_id": "110-1_medicine-6_080",
    "question_number": 80,
    "explanation": q80_explanation,
    "key_point": "《赫爾辛基宣言》規定，結合醫學研究與臨床照護的前提為：研究必須對病患具潛在預防、診斷或治療價值，且有充足理由確信參與不會對其健康造成不良影響。",
    "flashcard_front": "赫爾辛基宣言 / 醫學研究與醫療照護結合 / 臨床價值 / 利益衝突",
    "flashcard_back": "結合研究與醫療照護，前提是研究具潛在臨床價值，且醫師確信參與不會危害病人健康。",
    "flashcard_summary": "赫爾辛基結合照護 -> 僅在研究具潛在價值且不損害病人健康時，方可結合研究與醫療照護。",
    "review_status": "ai_generated",
    "explanation_model": "antigravity-subagent",
    "explanation_generated_at": "2026-07-14T13:13:29+08:00",
    "manual_review_notes": []
})

# Compile final JSON
output_data = {
    "source_file": source_file,
    "dataset_id": dataset_id,
    "range": {
        "start": 71,
        "end": 80
    },
    "updates": updates
}

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Generated q071-q080.json at " + output_file)
