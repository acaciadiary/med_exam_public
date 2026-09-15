const fs = require("fs");
const path = require("path");

const sourceFile = "public/data/exams/115-2/medicine-5.json";
const datasetId = "115-2_medicine-5";
const outDir = "scratch/rewrite_updates/115-2_medicine-5";
const timestamp = "2026-09-16T00:10:00+08:00";

const source = JSON.parse(fs.readFileSync(sourceFile, "utf8"));
const questionsByNumber = new Map(source.questions.map((q) => [q.question_number, q]));

function clean(text) {
  return text.trim().replace(/\n{3,}/g, "\n\n");
}

function update(questionNumber, explanation, keyPoint, flashcardSummary, manualReviewNotes = []) {
  const question = questionsByNumber.get(questionNumber);
  if (!question) throw new Error(`Missing source question ${questionNumber}`);
  const flashcardFront = flashcardSummary.split(/[：:]/)[0].trim() || keyPoint.slice(0, 80);
  return {
    question_id: question.id,
    question_number: question.question_number,
    explanation: clean(explanation),
    key_point: keyPoint,
    flashcard_front: flashcardFront,
    flashcard_back: keyPoint,
    flashcard_summary: flashcardSummary,
    review_status: "ai_generated",
    explanation_model: "codex-high-quality-rewrite",
    explanation_generated_at: timestamp,
    manual_review_notes: manualReviewNotes,
  };
}

const updates = [
  update(
    1,
    `
【題幹解析】
術後第一天傷口劇痛、發紅並有分泌物，題目要從 Gram stain 推回可能病原。Clostridium 屬是產芽孢的厭氧革蘭氏陽性桿菌，手術傷口若快速惡化、疼痛明顯，需想到 clostridial wound infection 或 gas gangrene。

【選項詳解】
- A. 正確。Clostridium 為革蘭氏陽性桿菌，且多為厭氧、產芽孢菌；在污染傷口或缺氧組織中可造成嚴重軟組織感染。
- B. 錯誤。革蘭氏陽性球菌較常想到 Staphylococcus 或 Streptococcus，不是 Clostridium 的形態。
- C. 錯誤。革蘭氏陰性桿菌包括 E. coli、Klebsiella、Pseudomonas 等，形態與染色特性都不符合梭狀芽孢菌。
- D. 錯誤。革蘭氏陰性球菌典型代表是 Neisseria，與術後 clostridial wound infection 的病原特徵不符。

【核心考點】
Clostridium 的關鍵辨識是「厭氧、產芽孢、革蘭氏陽性桿菌」。術後傷口快速疼痛惡化或壞死性軟組織感染時，要把 Gram stain 的形態先對上病原大類。
`,
    "Clostridium 屬是厭氧產芽孢的革蘭氏陽性桿菌。",
    "術後傷口感染：Clostridium -> Gram-positive rods"
  ),
  update(
    2,
    `
【題幹解析】
外傷氣胸的處置取決於氣胸大小、症狀與是否為張力性氣胸。少量皮下氣腫常代表空氣已從胸膜腔或肺實質傷口漏到皮下，因此在外傷情境下要懷疑氣胸。

【選項詳解】
- A. 錯誤。開放性氣胸若傷口形成單向瓣膜或通氣處理不當，仍可能演變成張力性氣胸。
- B. 錯誤。張力性氣胸先以針刺減壓搶救，但針刺只是暫時解除壓力，之後通常仍需放置胸管做確定處置。
- C. 正確。胸部 X 光看到少量皮下氣腫，在胸部外傷時常來自氣胸、肺裂傷或胸壁傷口漏氣，需進一步評估胸膜腔空氣。
- D. 錯誤。不是所有 X 光可見氣胸都一定要胸管；少量、穩定且無明顯症狀的氣胸可依情境觀察與追蹤。

【核心考點】
張力性氣胸是臨床診斷與立即減壓的急症，針刺後通常接胸管；單純小量氣胸則看症狀、大小與外傷風險決定觀察或引流。
`,
    "外傷氣胸看到皮下氣腫時要懷疑胸膜腔漏氣；張力性氣胸針刺減壓後通常仍需胸管。",
    "外傷氣胸：皮下氣腫提示漏氣，張力性氣胸需立即減壓並後續胸管"
  ),
  update(
    3,
    `
【題幹解析】
本題問甲狀腺手術併發症何者錯誤。單側喉返神經受損多造成聲音沙啞、嗆咳或聲帶麻痺；明顯呼吸困難較常見於雙側喉返神經受損、術後頸部血腫或氣道傷害。

【選項詳解】
- A. 錯誤，因此為本題要選的敘述。單側喉返神經損傷通常以聲音沙啞與單側聲帶麻痺為主，呼吸道阻塞風險不像雙側損傷那麼高。
- B. 正確。若發生氣管或喉部相關氣道損傷，可能需要暫時或永久性氣管切開以維持呼吸道。
- C. 正確。甲狀腺術後暫時性副甲狀腺功能低下常與腺體牽拉、缺血或暫時受損有關，多數會在數週到數月內恢復，6 個月內改善是合理描述。
- D. 正確。術後頸部血腫可能快速壓迫氣管，是甲狀腺手術後需立即辨識的急症，必要時要立刻打開傷口減壓。

【核心考點】
甲狀腺術後立即危及呼吸的重點是頸部血腫、氣道損傷與雙側喉返神經麻痺；單側喉返神經損傷主要表現為聲音問題。
`,
    "單側喉返神經損傷多造成聲音沙啞；雙側損傷或頸部血腫才較易造成急性呼吸困難。",
    "甲狀腺術後併發症：單側 RLN -> hoarseness；頸部血腫 -> airway emergency"
  ),
  update(
    4,
    `
【題幹解析】
腹腔內 desmoid fibromatosis 屬局部侵襲性纖維母細胞腫瘤，轉移極少見，但局部復發是臨床管理重點。題目問錯誤敘述，關鍵在於「不轉移」不能推論為「切除後不復發」。

【選項詳解】
- A. 正確。傳統治療曾以廣泛切除、取得陰性邊緣為主要策略，雖然近年也重視觀察與個別化治療。
- B. 錯誤，因此為本題要選的敘述。Desmoid tumor 幾乎不轉移，但局部侵犯與局部復發常見，尤其腹腔內或與 FAP 相關病灶更需謹慎追蹤。
- C. 正確。放射治療可用於無法完整切除、切除後殘存或局部控制困難的情境，但需考量部位與長期副作用。
- D. 正確。全身治療可包括 NSAID、抗荷爾蒙、低劑量化療、TKI 或較強的化療，常用於不可切除、進展或症狀明顯病灶。

【核心考點】
Desmoid fibromatosis 的考點是「低轉移、高局部復發」。治療需依症狀、位置、進展速度與可切除性選擇觀察、手術、放療或全身治療。
`,
    "Desmoid tumor 幾乎不轉移，但局部復發與局部侵犯是主要問題。",
    "Desmoid fibromatosis：low metastatic potential but locally recurrent"
  ),
  update(
    5,
    `
【題幹解析】
本題問 selenium 何者錯誤。Selenium 是 glutathione peroxidase 等 selenoprotein 的成分，作用是協助還原過氧化物、減少氧化傷害，不是增加細胞內過氧化氫。

【選項詳解】
- A. 錯誤，因此為本題要選的敘述。Selenium 透過 glutathione peroxidase 幫助將 hydrogen peroxide 與 lipid hydroperoxides 還原，保護細胞膜脂質；「增加過氧化氫」方向相反。
- B. 正確。缺硒可造成生長遲緩、肌肉疼痛無力、肌病變與心肌病變，典型例子包括 Keshan disease 的心肌病變。
- C. 正確。Selenium 參與免疫與甲狀腺激素代謝；缺乏可影響 selenoenzyme 活性與氧化還原平衡，進而影響 glutathione 系統。
- D. 正確。Glutathione peroxidase 含 selenium，功能是將 peroxide 還原為水或相對較不具反應性的產物。

【核心考點】
Selenium 的高頻考點是抗氧化酵素與甲狀腺代謝。遇到「增加過氧化氫來保護細胞」要立刻判斷方向錯誤。
`,
    "Selenium 是 glutathione peroxidase 的重要成分，功能是清除而不是增加 peroxide。",
    "Selenium：glutathione peroxidase cofactor -> antioxidant protection"
  ),
  update(
    6,
    `
【題幹解析】
創傷性腦損傷要區分 primary injury 與 secondary injury。短暫昏迷後出現 lucid interval，再惡化，是硬腦膜上血腫的經典考點，常與中硬腦膜動脈受傷有關。

【選項詳解】
- A. 錯誤。Primary brain injury 是撞擊當下造成的結構損傷，治療主要在預防 secondary injury，如低氧、低血壓、腦壓上升，不能靠藥物逆轉原始破壞。
- B. 錯誤。Epidural hematoma 常與顳骨骨折及 middle meningeal artery 出血有關；bridging veins 撕裂較典型造成 subdural hematoma。
- C. 正確。頭部外傷後先昏迷、短暫清醒再惡化的 lucid interval，是 epidural hematoma 的重要臨床線索。
- D. 錯誤。Corticosteroids 在 TBI 中未證實改善預後，且可能增加不良結果，不能作為例行治療。

【核心考點】
Epidural hematoma：middle meningeal artery、lucid interval、可能快速惡化。Subdural hematoma：bridging veins，常見於老人、酒精使用或腦萎縮族群。
`,
    "Epidural hematoma 常見 lucid interval，典型血管是 middle meningeal artery；bridging veins 屬 subdural hematoma。",
    "TBI：epidural hematoma -> lucid interval; subdural -> bridging veins"
  ),
  update(
    7,
    `
【題幹解析】
不穩定心絞痛的重點是症狀變得更頻繁、更嚴重、更持久，或在休息、低強度活動時發生。若只在固定運動量時出現，反而較像穩定心絞痛。

【選項詳解】
- A. 正確。發作頻率增加是 crescendo angina 的表現，屬不穩定心絞痛警訊。
- B. 正確。疼痛強度變大代表缺血門檻降低或病灶不穩定，符合不穩定心絞痛。
- C. 錯誤，因此為本題要選的敘述。僅在運動時發生、且模式固定，較符合穩定心絞痛；不穩定心絞痛可在休息或輕微活動時發作。
- D. 正確。疼痛持續時間變長，代表缺血負荷增加，是不穩定型表現。

【核心考點】
穩定心絞痛是可預測、活動誘發、休息或硝酸鹽緩解；不穩定心絞痛是新發、惡化、休息時發作或持續更久。
`,
    "不穩定心絞痛常有頻率、強度、持續時間增加或休息時發作；固定運動誘發較像穩定心絞痛。",
    "Angina：unstable = crescendo/rest/new-onset pattern"
  ),
  update(
    8,
    `
【題幹解析】
Stanford type B 主動脈剝離位於左鎖骨下動脈以遠。若沒有破裂、持續疼痛、器官缺血、下肢缺血或神經學併發症，屬 uncomplicated type B，主要先以內科降壓與降低剪力治療。

【選項詳解】
- A. 錯誤。緊急開放手術主要用於 type A 或 complicated type B；本題明確沒有缺血或神經學併發症。
- B. 錯誤。主動脈支架 TEVAR 常用於 complicated type B，例如破裂、持續疼痛、灌流不良或快速擴大； uncomplicated 病人不一定立即置放。
- C. 正確。積極控制血壓與心跳、降低 aortic wall shear stress，是 uncomplicated type B dissection 的初始核心治療。
- D. 錯誤。心包膜穿刺處理的是心包填塞，較與 ascending aorta/type A 破裂入心包相關；本題是 type B 且未描述心包填塞。

【核心考點】
主動脈剝離先分 type A 與 type B，再分 complicated 與 uncomplicated。Uncomplicated type B 以藥物控制血壓心跳為主；type A 或 complicated type B 才需侵入性處置。
`,
    "無併發症的 Stanford type B 主動脈剝離以降壓、降心跳、降低剪力為初始治療。",
    "Aortic dissection：uncomplicated type B -> medical blood pressure control"
  ),
  update(
    9,
    `
【題幹解析】
本題官方公告接受 B、D 或 BD。ASD 合併 Eisenmenger syndrome 代表長期左到右分流已造成嚴重肺高壓並反轉或雙向分流，此時關閉缺損可能使右心壓力無出口而惡化，通常禁忌。

【選項詳解】
- A. 錯誤。Eisenmenger physiology 已形成固定性肺血管阻力上升，外科關閉 ASD 可能造成右心衰竭，不能當作一般 ASD 修補。
- B. 可接受。官方公告將心內膜炎預防列為可給分答案之一；臨床上預防性抗生素需依是否有高風險心臟病灶、手術類型與當地規範判斷，不是所有 ASD 都例行使用。
- C. 錯誤。導管關閉 ASD 與手術關閉同樣會移除分流出口，對 Eisenmenger syndrome 通常不適合。
- D. 可接受。若病人有低血氧，氧氣治療可作支持性處置；但它不是逆轉肺血管病變的根本治療，現代照護還會評估肺高壓標靶治療與移植可能性。

【核心考點】
ASD 一旦進展到 Eisenmenger syndrome，重點是避免關閉分流、支持性照護並評估肺高壓治療。遇到公告多答案題時要保留可接受答案，同時理解原本生理邏輯。
`,
    "Eisenmenger syndrome 通常不應關閉 ASD；官方本題接受 B、D 或 BD。",
    "ASD + Eisenmenger：avoid closure; accepted answers B/D per official correction",
    ["官方公告本題答 B、D 或 BD 均給分；B 的適用情境與現代 infective endocarditis prophylaxis 規範需人工留意。"]
  ),
  update(
    10,
    `
【題幹解析】
本題問 tension pneumothorax 何者最不適當。張力性氣胸是會造成阻塞性休克的臨床急症，不能因一開始血氧看起來尚可就延誤減壓。

【選項詳解】
- A. 正確。呼吸窘迫與低血壓是張力性氣胸的重要表徵，因胸腔壓力上升會壓迫靜脈回流並降低心輸出。
- B. 正確。患側呼吸音減弱或消失是典型理學檢查線索。
- C. 正確。嚴重時可見氣管偏移、頸靜脈怒張或皮下氣腫，但氣管偏移不一定早期出現。
- D. 錯誤，因此為本題要選的敘述。張力性氣胸不能等待完整排除其他低血壓原因；若臨床懷疑，應立即針刺或指胸減壓。

【核心考點】
Tension pneumothorax 是先治療再確認的創傷急症。血氧暫時可接受不代表安全，低血壓加單側呼吸音下降時要立即減壓。
`,
    "疑似張力性氣胸合併休克時不可等待檢查或排除其他原因，需立即減壓。",
    "Tension pneumothorax：clinical emergency requiring immediate decompression"
  ),
  update(
    11,
    `
【題幹解析】
本題為高解析度食道壓力圖形判讀，官方答案為 A，但目前 JSON 只保留圖形選項標籤，沒有實際壓力圖。依題目主軸，胃食道逆流病人常見的壓力檢查重點是下食道括約肌壓力低、食道胃交界屏障較弱或蠕動清除能力不足。

【選項詳解】
- A. 正確。官方圖形答案為 A；若圖中呈現較低 LES pressure、EGJ barrier 較弱或蠕動清除不佳，會較符合胃食道逆流的生理基礎。
- B. 錯誤。未見圖形內容時不能精確判讀；若為 achalasia 典型圖會呈現 LES relaxation 異常與食道體部蠕動缺失，和一般 GERD 不同。
- C. 錯誤。若圖形顯示強烈收縮或 spastic pattern，通常會偏向 motility disorder，而不是單純逆流。
- D. 錯誤。若圖形代表正常 LES 與正常蠕動，不能解釋逆流病人的抗逆流屏障不足。

【核心考點】
HRM 判讀 GERD 時要看 EGJ/LES 抗逆流屏障與食道清除能力；但圖形題必須回到官方 PDF 圖像確認，不能只靠文字標籤判斷。
`,
    "GERD 的 HRM 線索常與 LES/EGJ 抗逆流屏障較弱或清除能力不足有關；本題仍需看官方圖。",
    "GERD HRM：weak EGJ barrier or ineffective clearance; image option required",
    ["本題 A-D 為圖形選項，JSON 未含圖像內容；已保留官方答案 A，建議人工對照官方 PDF 圖。"]
  ),
  update(
    12,
    `
【題幹解析】
本題問橫膈肌損傷修補何者錯誤。急性外傷性橫膈膜破裂常合併腹內臟器損傷，因此穩定性、受傷機轉與是否需探查腹腔會決定手術路徑。

【選項詳解】
- A. 正確。鈍性橫膈肌損傷常經腹部切開或腹腔鏡探查，因為需同時評估脾、肝、腸胃道等腹內臟器傷害。
- B. 正確。橫膈膜撕裂可用粗的不可吸收縫線修補，以承受呼吸運動造成的張力。
- C. 錯誤，因此為本題要選的敘述。胸腔鏡不是所有橫膈肌損傷的首選；急性創傷若疑有腹內傷，經腹探查常更適合。
- D. 正確。大範圍缺損或組織不足以直接關閉時，可使用人工或生物 mesh 加強修補。

【核心考點】
急性橫膈膜外傷的路徑選擇取決於合併傷與病人穩定度。不能把胸腔鏡視為所有橫膈膜損傷的固定首選。
`,
    "急性橫膈膜損傷常需經腹探查合併腹內傷；胸腔鏡不是所有類型的首選。",
    "Diaphragm injury：approach depends on associated injuries, not always thoracoscopy"
  ),
  update(
    13,
    `
【題幹解析】
本題問腹股溝疝氣危險因子何者最不適當。腹內壓增加、結締組織較弱或腹壁缺陷會增加疝氣風險；出生體重大於 3000 克本身不是典型危險因子。

【選項詳解】
- A. 正確。COPD 病人慢性咳嗽會反覆增加腹內壓，促進腹股溝疝氣形成或惡化。
- B. 正確。肥胖可增加腹壁負荷與腹內壓，與疝氣風險增加相關。
- C. 正確。腹水會長期提高腹內壓，使疝氣更容易出現或復發。
- D. 錯誤，因此為本題要選的敘述。疝氣的兒科風險較常與早產、低出生體重、鞘狀突未閉等相關，出生體重大於 3000 克不是典型危險因子。

【核心考點】
腹股溝疝氣危險因子可用「腹內壓上升」與「腹壁或鞘狀突問題」思考；早產與低出生體重比高出生體重更有考試價值。
`,
    "腹股溝疝氣風險常來自腹內壓上升或腹壁缺陷；高出生體重不是典型危險因子。",
    "Inguinal hernia：COPD, obesity, ascites increase pressure; prematurity/low birth weight in children"
  ),
  update(
    14,
    `
【題幹解析】
Dumping syndrome 分早期與晚期。早期是高滲食糜快速進入小腸造成體液移動與血管運動症狀；晚期是餐後胰島素過度反應造成低血糖。治療先從飲食調整開始。

【選項詳解】
- A. 錯誤。Early dumping 主要不是低血糖，而是高滲內容物快速進入小腸造成腹部絞痛、腹瀉、心悸、頭暈等。
- B. 錯誤。Late dumping 才是餐後反應性低血糖；高滲食物造成的體液移動屬 early dumping。
- C. 正確。少量多餐、減少單醣、增加蛋白質與纖維、餐中少喝水等飲食調整，是 dumping syndrome 的第一線處理。
- D. 錯誤。全胃切除可能造成或加重 dumping，不是治療 dumping syndrome 的常規手術。

【核心考點】
Early dumping 是滲透壓與血管運動症狀；late dumping 是反應性低血糖。處理先用飲食治療，藥物或手術只在少數頑固個案考慮。
`,
    "Dumping syndrome 先以飲食治療；early 是高滲食糜快速進入小腸，late 是反應性低血糖。",
    "Dumping syndrome：early osmotic symptoms, late hypoglycemia, diet first"
  ),
  update(
    15,
    `
【題幹解析】
Pneumatosis intestinalis 是影像徵象，不等於單一疾病。成人可見於良性、藥物、肺部疾病、腸缺血或惡性腫瘤相關狀況；但嬰兒出現時，尤其早產兒，需高度懷疑 necrotizing enterocolitis。

【選項詳解】
- A. 錯誤。腸壁積氣不一定要手術；要看有無腹膜炎、腸缺血、敗血症、門靜脈氣體、乳酸升高或穿孔。
- B. 正確。嬰兒，尤其早產兒若有腸壁積氣，NEC 是最重要診斷之一。
- C. 錯誤。許多腸壁積氣沒有腹膜炎；腹膜炎代表嚴重或需手術的警訊，但不是大多數個案都有。
- D. 錯誤。腸壁積氣可與癌症、化療、免疫抑制或腸阻塞等情境相關，不能說與癌症沒有關聯。

【核心考點】
Pneumatosis intestinalis 先判斷病人族群與危險徵象。嬰兒想到 NEC；成人則需用臨床穩定度判斷保守或手術。
`,
    "嬰兒腸壁積氣要懷疑 NEC；成人腸壁積氣不一定都需要手術。",
    "Pneumatosis intestinalis：infant -> consider NEC; surgery depends on danger signs"
  ),
  update(
    16,
    `
【題幹解析】
本題官方公告一律給分，因此系統接受 A、B、C、D。從生理學來看，CO2 氣腹的重點是 CO2 容易由腹膜吸收，可能造成 hypercarbia 與 respiratory acidosis，通常靠增加分鐘通氣量來矯正。

【選項詳解】
- A. 可接受但有疑義。官方一律給分；醫學概念上 CO2 其實容易被腹膜吸收，這也是腹腔鏡可能造成高碳酸血症的原因。
- B. 可接受。肺功能正常時，增加呼吸速率或潮氣量可提高 CO2 排出，改善呼吸性酸中毒。
- C. 可接受。肌肉等組織可作為 CO2 的重要緩衝與儲存空間，這是長時間氣腹時 CO2 負荷的概念之一。
- D. 可接受但有疑義。高碳酸血症常可引起交感活化、心跳與血壓變化；嚴重或迷走刺激時也可能有心搏過緩，因此本選項需依題目原公告處理。

【核心考點】
CO2 氣腹會被吸收並增加 CO2 負荷；一般先靠通氣調整處理 hypercarbia。公告一律給分的題目要保留官方給分範圍，不自行改答案。
`,
    "CO2 氣腹可造成 hypercarbia，肺功能正常時以增加通氣排出 CO2；本題官方一律給分。",
    "CO2 pneumoperitoneum：absorbed CO2 -> hypercarbia; increase ventilation; all-credit item",
    ["官方公告本題一律給分；A 與 D 依一般生理概念有疑義，建議人工留意。"]
  ),
  update(
    17,
    `
【題幹解析】
本題官方公告接受 C、D 或 CD，問的是術後腸麻痺何者錯誤。術後 ileus 常受電解質異常、感染發炎、opioid、手術刺激與活動不足影響，治療重點是矯正誘因與支持療法。

【選項詳解】
- A. 正確。低鉀、低鈉、低鎂都會影響腸道平滑肌與神經肌肉功能，矯正電解質是基本處置。
- B. 正確。肺炎、腹膜炎、敗血症等感染與全身發炎會加重 ileus，控制感染是重要治療。
- C. 錯誤，因此為官方可接受答案之一。咀嚼口香糖可縮短術後腸功能恢復時間的證據較支持輔助角色；erythromycin 對術後 ileus 並非穩定證實有效的標準治療。
- D. 官方也接受。NSAID 可減少 opioid 使用，理論上降低 opioid-induced ileus，但題目文字把 NSAID 寫成「類固醇類消炎止痛藥」並不精確，可能是公告接受 D 的原因。

【核心考點】
術後 ileus 的處理是找誘因：電解質、感染、opioid、活動與手術壓力。藥物或口香糖不能取代基礎矯正與支持治療。
`,
    "術後 ileus 要矯正電解質與感染並減少 opioid；本題官方接受 C、D 或 CD。",
    "Postoperative ileus：correct triggers; gum/erythromycin not definitive therapy; accepted C/D",
    ["官方公告本題答 C、D 或 CD 均給分；D 的 NSAID 中文描述可能造成判讀疑義。"]
  ),
  update(
    18,
    `
【題幹解析】
器官移植後晚期感染多與長期免疫抑制、潛伏病毒再活化與環境黴菌暴露有關。經常輸血本身不是典型的晚期感染主要危險因子。

【選項詳解】
- A. 正確。長期免疫抑制會削弱細胞免疫與體液免疫，增加 opportunistic infection 與一般感染風險。
- B. 正確。受贈者既存 CMV、HBV、HCV、EBV 等感染或潛伏病毒，可在免疫抑制下再活化。
- C. 正確。裝修環境可增加 Aspergillus 等黴菌孢子暴露，對移植病人是重要風險。
- D. 錯誤，因此為本題要選的敘述。輸血可有輸血相關感染或免疫影響，但不是移植後晚期感染的典型核心危險因子。

【核心考點】
移植後晚期感染要想到免疫抑制強度、病毒再活化與環境黴菌暴露。時間軸與免疫狀態比單一住院處置更重要。
`,
    "移植後晚期感染風險主要來自長期免疫抑制、既存病毒與環境黴菌暴露。",
    "Transplant late infection：immunosuppression, latent viruses, construction mold exposure"
  ),
  update(
    19,
    `
【題幹解析】
移植排斥的免疫學重點是 HLA/MHC 與 T 細胞活化。人類 HLA 基因位於第 6 對染色體短臂；class I 主要呈現給 CD8 T 細胞，class II 主要呈現給 CD4 T 細胞。

【選項詳解】
- A. 正確。HLA 編碼人類 MHC，位於 chromosome 6p，對抗原呈現與移植相容性很重要。
- B. 錯誤。Class I HLA 主要與 CD8 T 細胞互動；class II HLA 才主要與 CD4 T 細胞互動。
- C. 錯誤。T 細胞活化的關鍵 cytokine 常考 IL-2；calcineurin-NFAT 路徑促進 IL-2 transcription，而不是以 IL-6 為主要記憶點。
- D. 錯誤。Calcineurin inhibitor 抑制的是 T 細胞內 calcineurin 訊息傳遞與 IL-2 生成，不是阻斷 allorecognition 本身。

【核心考點】
HLA 在 6p；MHC I 對 CD8，MHC II 對 CD4。Tacrolimus/cyclosporine 抑制 calcineurin，降低 IL-2 與 T 細胞活化。
`,
    "HLA 基因位於第 6 對染色體短臂；MHC I 對 CD8，MHC II 對 CD4。",
    "Transplant immunology：HLA 6p; class I-CD8; class II-CD4; CNI blocks IL-2 signaling"
  ),
  update(
    20,
    `
【題幹解析】
脾臟外傷或手術處置要先看病人血流動力學。穩定病人可用 CT 分級並考慮非手術治療或血管栓塞；不穩定病人需優先手術止血。

【選項詳解】
- A. 錯誤。脾切除後確實有 overwhelming postsplenectomy infection 風險，重點是疫苗、衛教與特定情境抗生素；不一定所有成人都需長期抗生素。
- B. 錯誤。兒童脾臟外傷非手術治療成功率通常高於成人，因保脾策略更常成功。
- C. 錯誤。血壓不穩定且嚴重脾破裂時，不能先依賴栓塞拖延；應以手術或損傷控制優先。
- D. 正確。血流動力學穩定時，電腦斷層可評估脾臟損傷程度、血管外滲與是否適合非手術治療。

【核心考點】
脾臟外傷處置先問穩不穩定。穩定者 CT 分級並可保守或栓塞；不穩定者優先手術止血。
`,
    "脾臟外傷以血流動力學穩定度決定處置；穩定者 CT 評估，休克者優先手術。",
    "Splenic trauma：stable -> CT/nonoperative; unstable -> operative control"
  ),
  update(
    21,
    `
【題幹解析】
急性脊髓損傷的處理重點是固定脊椎、維持灌流與氧合、影像確認、並在有壓迫或不穩定時評估早期減壓。高劑量 steroid 已不再是無爭議的標準治療。

【選項詳解】
- A. 錯誤。Corticosteroids 對 acute SCI 的長期功能改善證據有限且有感染、出血等風險，不能說已被證實明顯改善並應列為標準治療。
- B. 錯誤。疑似頸椎損傷在未排除骨折或不穩定前不能為了壓瘡風險就早早移除頸圈，需先安全固定與評估。
- C. 正確。不完全脊髓損傷合併壓迫時，24 小時內早期手術減壓可能改善神經恢復，是重要處置方向。
- D. 錯誤。疑似 acute SCI 初始評估骨折與排列常先用 CT；MRI 對脊髓、韌帶、椎間盤與血腫較敏感，但不是所有疑似病例的第一個影像。

【核心考點】
Acute SCI：固定、維持灌流、CT 評估骨傷，必要時 MRI 看神經軟組織；不完全損傷合併壓迫可考慮 24 小時內減壓。
`,
    "不完全急性脊髓損傷合併壓迫時，早期減壓可能改善神經功能；steroid 不是常規標準答案。",
    "Acute SCI：immobilize, CT first for bone, early decompression when compressed"
  ),
  update(
    22,
    `
【題幹解析】
Cervical myelopathy 是頸髓受壓或病變造成的上運動神經元表現。典型線索包括步態不穩、手部精細動作變差、反射亢進、spasticity、clonus 或 Babinski sign。

【選項詳解】
- A. 錯誤。頸椎脊髓病變常可在 MRI 看到椎管狹窄、脊髓受壓或訊號改變；若完全沒有狹窄，診斷需重新評估。
- B. 錯誤。Myelopathy 屬上運動神經元病變，深部肌腱反射常上升；反射下降較像周邊神經或神經根問題。
- C. 正確。肌肉痙攣、clonus、反射亢進等是頸髓病變常見的上運動神經元徵象。
- D. 錯誤。感覺異常可出現，包含麻木、本體感覺差或感覺層次變化，不能說感覺一定正常。

【核心考點】
頸椎 myelopathy 是脊髓病變，考點是上運動神經元徵象：hyperreflexia、spasticity、clonus、步態不穩。
`,
    "Cervical myelopathy 常有 hyperreflexia、spasticity、clonus 等上運動神經元徵象。",
    "Cervical myelopathy：upper motor neuron signs, not decreased reflexes"
  ),
  update(
    23,
    `
【題幹解析】
Glioma 常具浸潤性，會沿白質束擴散，這正是完全切除困難的原因。手術多追求最大安全切除，而不是保證完整根除。

【選項詳解】
- A. 正確。許多原發性腦腫瘤源自神經膠質細胞或支持細胞，統稱 glioma。
- B. 錯誤，因此為本題要選的敘述。膠質瘤沿白質束浸潤代表邊界不清，常無法完全切除；功能區附近更需保留神經功能。
- C. 正確。放療、化療與標靶策略會依腫瘤級別、組織型、分子標記與病人狀態調整。
- D. 正確。兒童 diffuse pontine glioma 可侵犯腦幹，表現為多發腦神經麻痺、長束徵象與小腦症狀。

【核心考點】
Glioma 的浸潤性使完整切除困難；治療目標是最大安全切除加上依病理與分子特徵安排後續治療。
`,
    "Glioma 常沿白質束浸潤，因此多難以完全手術切除。",
    "Glioma：infiltrative along white matter tracts -> complete resection difficult"
  ),
  update(
    24,
    `
【題幹解析】
Dural arteriovenous fistula 是硬腦膜動脈與靜脈竇或皮質靜脈的異常連通。其危險性取決於靜脈回流型態；若有 cortical venous reflux，可能出血或神經缺損。

【選項詳解】
- A. 錯誤，因此為本題要選的敘述。DAVF 可出現頭痛、耳鳴、眼症狀或神經缺損，也可能破裂出血；不能說不會出血。
- B. 不作為本題最不適當的敘述。DAVF 與 AVM 都是動靜脈短路性病灶，臨床上需鑑別；嚴格說 DAVF 不一定會直接「變成」典型腦實質 AVM，因此本句也有用語不精準處。
- C. 正確。Carotid-cavernous fistula 可被歸在硬腦膜動靜脈瘻管相關分類中，特別是間接型。
- D. 正確。靜脈竇栓塞或靜脈高壓被認為與部分 DAVF 形成有關。

【核心考點】
DAVF 不是單純頭痛疾病；有皮質靜脈逆流時出血風險升高。判斷危險性要看靜脈引流型態，且需留意 DAVF 與 AVM 名詞不宜混用。
`,
    "Dural AV fistula 可因皮質靜脈逆流造成出血，不能說不會破裂出血。",
    "Dural AVF：risk depends on venous drainage; cortical venous reflux can bleed",
    ["B 選項把 DAVF 與 AVM 的關係寫得不夠標準；已保留官方答案 A，建議人工留意。"]
  ),
  update(
    25,
    `
【題幹解析】
NF1 是常見神經皮膚症候群，為 autosomal dominant，基因位於 17q11.2。NF1 可有 neurofibroma、optic pathway glioma，並增加 malignant peripheral nerve sheath tumor 風險。

【選項詳解】
- A. 正確。NF1 多為體染色體顯性遺傳，但也可見新發突變。
- B. 正確。NF1 gene 位於 chromosome 17q11.2，編碼 neurofibromin。
- C. 正確。NF1 病人有發展成 MPNST 的風險，常考約 8% 到 13% 的量級，10% 是常見考試描述。
- D. 錯誤，因此為本題要選的敘述。NF1 與 glioma，尤其 optic pathway glioma 有關；schwannoma 更典型與 NF2 相關，但說 NF1 與 glioma 無關不正確。

【核心考點】
NF1：17q11.2、neurofibromin、cafe-au-lait、neurofibroma、optic glioma、MPNST 風險。NF2 才特別想到 bilateral vestibular schwannoma。
`,
    "NF1 位於 17q11.2，與 optic glioma 及 MPNST 風險相關；雙側 vestibular schwannoma 較屬 NF2。",
    "NF1：17q11.2, optic glioma, MPNST risk; NF2 -> vestibular schwannoma"
  ),
  update(
    26,
    `
【題幹解析】
Congenital melanocytic nevi 的惡性轉化風險與大小相關，巨型 CMN 風險最高。常用分類中成人預估直徑超過 20 cm 屬 giant CMN。

【選項詳解】
- A. 錯誤。小於 1.5 cm 屬小型 CMN，黑色素瘤風險最低。
- B. 錯誤。1.5 到 10 cm 風險較小型高一些，但不是最高風險群。
- C. 錯誤。11 到 20 cm 屬中大型範圍，仍低於 giant CMN 的典型風險。
- D. 正確。直徑大於 20 cm 的 giant CMN 惡性變化風險最高，也需注意 neurocutaneous melanosis。

【核心考點】
CMN 越大，黑色素瘤與神經皮膚黑色素增生風險越高；考試常把 giant CMN 的切點放在成人預估直徑大於 20 cm。
`,
    "Giant congenital melanocytic nevus 通常以直徑大於 20 cm 為高風險切點。",
    "CMN：giant >20 cm -> highest melanoma risk"
  ),
  update(
    27,
    `
【題幹解析】
Guyon canal syndrome 是尺神經在腕部 Guyon canal 受壓造成的症候群。它會影響 ulnar nerve 的感覺或手內在肌，不會造成正中神經壓迫。

【選項詳解】
- A. 正確。Guyon canal 的邊界包含 pisiform、hook of hamate、piso-hamate ligament 與 palmar carpal ligament 等結構。
- B. 錯誤，因此為本題要選的敘述。Guyon canal 內主要通過 ulnar nerve 與 ulnar artery；median nerve 壓迫是 carpal tunnel syndrome 的考點。
- C. 正確。局部敲擊引發麻電感的 Tinel sign 可出現在 Guyon canal 處。
- D. 正確。Ganglion、giant cell tumor、ulnar artery thrombosis 或職業性壓迫都可能造成尺神經在 Guyon canal 受壓。

【核心考點】
Guyon canal 壓迫的是 ulnar nerve；carpal tunnel 壓迫的是 median nerve。腕部神經壓迫題先定位通道與神經。
`,
    "Guyon canal syndrome 是腕部尺神經壓迫，不是正中神經壓迫。",
    "Guyon canal：ulnar nerve compression; carpal tunnel：median nerve"
  ),
  update(
    28,
    `
【題幹解析】
Hydrofluoric acid 燒傷會讓 fluoride ion 深入組織並結合鈣鎂，造成劇烈疼痛與低鈣風險。表淺皮膚暴露常先反覆塗抹 calcium gluconate gel，直到疼痛緩解。

【選項詳解】
- A. 正確。2.5% calcium gluconate gel 常建議約每 15 分鐘反覆塗抹並按摩，直到疼痛明顯緩解；疼痛持續代表 fluoride 仍在作用。
- B. 錯誤。30 分鐘間隔太長，可能延誤 fluoride ion 的局部中和。
- C. 錯誤。60 分鐘不符合一般表淺 HF 皮膚暴露的初始處理頻率。
- D. 錯誤。90 分鐘更不適合急性疼痛與組織毒性控制。

【核心考點】
HF 燒傷不是一般酸灼傷；fluoride 會結合鈣鎂並造成深部傷害。表淺傷口可用 calcium gluconate gel 頻繁塗抹，疼痛不退要升級治療。
`,
    "Hydrofluoric acid 皮膚暴露使用 2.5% calcium gluconate gel 時，常約每 15 分鐘重複塗抹至疼痛緩解。",
    "HF burn：calcium gluconate gel q15 min until pain relief"
  ),
  update(
    29,
    `
【題幹解析】
疤痕品質與張力、方向、感染、異物、膠原沉積及縫合層次有關。縫合時最重要的是讓真皮層精準對合並降低張力，表皮只是最後對齊外觀。

【選項詳解】
- A. 正確。肥厚性疤痕與蟹足腫都與膠原過度堆積、傷口張力與個人體質有關。
- B. 正確。肥厚性疤痕通常侷限於原傷口範圍並可能逐漸成熟；蟹足腫會超出原傷口且較不會自然退縮。六個月停止生長是簡化但可用的區分概念。
- C. 錯誤，因此為本題要選的敘述。傷口強度主要來自真皮層，精準對合 dermis、減少 dead space 與張力比單純對齊 epidermis 更重要。
- D. 正確。可吸收縫線因材料分解與組織反應，通常比不可吸收縫線引起較多局部發炎。

【核心考點】
美容縫合的重點是 dermal approximation 與 tension control。表皮對齊影響外觀，但真皮層才是傷口強度與疤痕品質的關鍵。
`,
    "縫合時最重要的是精準對合真皮層並降低張力，而不是只對齊表皮。",
    "Scar formation：dermal approximation and low tension matter most"
  ),
  update(
    30,
    `
【題幹解析】
ABI 0.3 加上休息痛或組織缺血外觀，代表嚴重周邊動脈阻塞或 critical limb-threatening ischemia。下一步要抗血小板、評估血管影像並討論再血管化；warfarin 不是此情境的常規第一線處置。

【選項詳解】
- A. 正確。動脈攝影或 CTA/MRA 可用來規劃 endovascular therapy 或 bypass。
- B. 正確。Aspirin 屬抗血小板治療，可降低動脈粥樣硬化相關血栓事件，是 PAD 常用藥物。
- C. 錯誤，因此為本題要選的處置。Warfarin 抗凝血不是穩定周邊動脈阻塞或慢性肢體缺血的標準初始治療，除非有其他適應症如心房顫動或栓塞來源。
- D. 正確。ABI 0.3 且疼痛不能走路，需評估血管再通策略，包含腔內治療或繞道手術。

【核心考點】
嚴重 PAD/CLTI 的處理是抗血小板、風險因子控制、血管影像與再血管化評估；不要把動脈粥樣硬化缺血直接等同於 warfarin 適應症。
`,
    "ABI 0.3 代表嚴重缺血，應評估再血管化；warfarin 不是 PAD 的常規第一線治療。",
    "Severe PAD：antiplatelet + vascular imaging/revascularization, not routine warfarin"
  ),
  update(
    31,
    `
【題幹解析】
慢性下肢潰瘍常分動脈性、靜脈性與神經病變性。靜脈潰瘍典型位在內踝附近的小腿下段；足部潰瘍較常見於糖尿病神經病變或動脈缺血。

【選項詳解】
- A. 錯誤。動脈潰瘍常疼痛明顯；靜脈潰瘍可酸脹不適但不一定非常痛，糖尿病神經病變潰瘍甚至可疼痛不明顯。
- B. 正確。靜脈潰瘍多在 gaiter area，尤其內踝周圍；足部不是典型位置。
- C. 錯誤。動脈潰瘍可發生在足趾、足部壓力點，也可在小腿遠端或受壓處，不能說很少發生在腿部。
- D. 錯誤。糖尿病會增加周邊動脈疾病、神經病變與感染風險，腿足潰瘍影響通常更高而非更低。

【核心考點】
靜脈潰瘍看內踝周圍與水腫色素沉著；動脈潰瘍看足趾遠端、缺血痛、脈搏差；糖尿病潰瘍常有神經病變與感染風險。
`,
    "靜脈潰瘍典型位於內踝周圍小腿下段，足部潰瘍較常見於動脈缺血或糖尿病神經病變。",
    "Leg ulcer：venous medial gaiter area; arterial/diabetic often foot or pressure points"
  ),
  update(
    32,
    `
【題幹解析】
CABG 使用 radial artery 的優點是長期通暢率常優於大隱靜脈，但橈動脈屬肌性動脈，較容易痙攣，因此需使用血管擴張策略並選擇高度狹窄的目標血管以避免 competitive flow。

【選項詳解】
- A. 錯誤。Radial artery 通暢率通常不比大隱靜脈差；痙攣是需管理的問題，但不是讓其 5 年通暢率較差的理由。
- B. 錯誤。Radial artery 對 competitive flow 較敏感，較適合接到高度狹窄的冠狀動脈；小於 60% 狹窄不理想。
- C. 錯誤。Radial artery 可改善 graft patency，但不能說所有研究都顯示長期存活率優於大隱靜脈。
- D. 正確。使用 radial artery 時常搭配 calcium channel blocker 或 nitrate 等血管擴張策略，以降低痙攣。

【核心考點】
Radial artery graft 是肌性動脈，優點是通暢率佳，缺點是痙攣與 competitive flow 敏感；要接高度狹窄目標並用血管擴張劑。
`,
    "Radial artery graft 需預防血管痙攣，且較適合接高度狹窄的冠狀動脈。",
    "CABG radial artery：good patency but spasm-prone and competitive-flow sensitive"
  ),
  update(
    33,
    `
【題幹解析】
乳糜胸是胸管或淋巴系統受損造成 chyle 進入胸腔。成人常見原因包括手術或外傷，惡性腫瘤也是重要原因；若題目問最不適當，說「最常見原因為腫瘤侵犯」過於絕對，尤其在外科情境下術後損傷更常考。

【選項詳解】
- A. 正確。乳糜富含 triglyceride、chylomicron 與淋巴球，外觀常呈乳白色，主要成分與脂肪吸收有關。
- B. 錯誤，因此為本題要選的敘述。乳糜胸原因包含胸管手術損傷、外傷與惡性腫瘤；在許多臨床分類中，術後或外傷性原因非常重要，不能一概說腫瘤侵犯最常見。
- C. 正確。初始可禁食、低脂或中鏈三酸甘油酯飲食、TPN、胸腔引流與 octreotide；高流量或保守失敗時需手術或介入治療。
- D. 正確。手術常見方式是經胸結紮 thoracic duct，依漏出位置與病人狀態決定路徑。

【核心考點】
乳糜胸先確認高 triglyceride/chylomicron，再看流量與原因。初始支持治療，持續高流量或失敗要及早結紮胸管或介入處理。
`,
    "乳糜胸可由手術損傷、外傷或腫瘤造成；不能把腫瘤侵犯一概說成最常見原因。",
    "Chylothorax：chyle high triglyceride; conservative first, thoracic duct ligation if persistent"
  ),
  update(
    34,
    `
【題幹解析】
縱膈腔神經源性腫瘤多位於後縱膈。成人多為良性 schwannoma 或 neurofibroma；兒童相對較常見神經母細胞瘤等惡性或未成熟腫瘤。

【選項詳解】
- A. 錯誤，因此為本題要選的敘述。兒童縱膈神經源性腫瘤的惡性比例較成人高，不是較低。
- B. 正確。神經源性腫瘤典型位置是 posterior mediastinum，沿交感鏈、肋間神經或神經根生長。
- C. 正確。成人最常見的縱膈神經源性腫瘤常是 schwannoma，多為良性。
- D. 正確。Schwannoma 可來自胸腔內多種周邊神經，包括肋間神經、交感鏈或神經根。

【核心考點】
後縱膈腫瘤先想到 neurogenic tumor。成人多良性 schwannoma；兒童要更注意 neuroblastoma 等惡性腫瘤。
`,
    "縱膈神經源性腫瘤常在後縱膈；兒童惡性比例比成人高。",
    "Posterior mediastinum：neurogenic tumors; children higher malignant risk"
  ),
  update(
    35,
    `
【題幹解析】
本題官方公告一律給分。脾切除後最典型增加的是莢膜菌感染，尤其 Streptococcus pneumoniae、Haemophilus influenzae type b、Neisseria meningitidis；Cryptococcus neoformans 不是 asplenia 最典型的莢膜菌考點。

【選項詳解】
- A. 公告給分但有疑義。醫學概念上肺炎鏈球菌是脾切除後最重要且常見的風險菌之一，並不屬於「比較不常見」。
- B. 因公告一律給分而可被系統接受；但 Hib 也是脾切除後需預防的莢膜菌，通常會納入疫苗防護。
- C. 可接受。Cryptococcus neoformans 有莢膜，但脾切除後經典重點不是它；若以 asplenia 常見感染來看，C 較接近題目原意。
- D. 公告給分範圍包含此項；但 Neisseria meningitidis 是脾切除後需接種疫苗預防的重要莢膜菌，學理上並不適合當作不常見答案。

【核心考點】
Asplenia 先背三大莢膜菌：S. pneumoniae、Hib、N. meningitidis。遇到公告一律給分，答題系統接受所有選項，但學理上仍要記住經典高風險菌。
`,
    "脾切除後最重要的莢膜菌是 S. pneumoniae、Hib、N. meningitidis；本題官方一律給分。",
    "Asplenia：encapsulated bacteria SPN, Hib, meningococcus; all-credit item",
    ["官方公告本題一律給分；依 asplenia 經典感染風險，A/B/D 皆屬重要莢膜菌，C 較像原題想選的不常見項。"]
  ),
  update(
    36,
    `
【題幹解析】
胃腸道內分泌的 universal off switch 指 somatostatin。它可抑制胃酸、胰臟外分泌、腸道分泌與多種荷爾蒙釋放。

【選項詳解】
- A. 錯誤。Secretin 主要由十二指腸 S cells 分泌，促進胰臟 bicarbonate 分泌並抑制胃酸，但不是廣泛抑制多種內分泌激素的 universal off switch。
- B. 錯誤。Motilin 促進 migrating motor complex，與禁食期腸胃蠕動相關。
- C. 錯誤。VIP 會增加腸道水分與電解質分泌、放鬆平滑肌，VIPoma 可造成水樣腹瀉、低血鉀、胃酸低下。
- D. 正確。Somatostatin 廣泛抑制胃酸、胰泌素、胰島素、升糖素、腸道分泌與多種 GI hormone，是典型 off switch。

【核心考點】
Somatostatin 是 GI endocrine brake；VIP 是 secretory diarrhea，motilin 是 MMC，secretin 是 bicarbonate。
`,
    "Somatostatin 是胃腸道內分泌的 universal off switch，可抑制胃酸、腸液與多種荷爾蒙。",
    "GI hormones：somatostatin = universal off switch"
  ),
  update(
    37,
    `
【題幹解析】
Caroli disease 是肝內膽管先天性 ductal plate malformation，造成肝內膽管囊狀擴張。題目問最適當，需避開把它說成肝硬化後天疾病或一律切肝治療的選項。

【選項詳解】
- A. 有部分正確但不是官方所選。Caroli disease 的病因確實是 ductal plate malformation；選項若強調「連續性」囊性擴張，和典型可呈節段性、囊狀或梭狀擴張的描述不完全精準。
- B. 錯誤。Caroli disease 是先天性膽管異常，不是通常發生於肝硬化病人；它可與先天性肝纖維化與囊性腎病相關。
- C. 正確。Caroli disease 多在兒童或年輕成人被發現，性別差異不明顯。
- D. 錯誤。治療依分布與症狀決定；局部病灶可切除，瀰漫型或反覆膽管炎可能需肝移植，不能說一律以肝切除為主。

【核心考點】
Caroli disease 是先天性肝內膽管囊狀擴張，可反覆膽管炎與結石。治療看局部或瀰漫，不是所有病人都切肝。
`,
    "Caroli disease 是先天性肝內膽管囊狀擴張，多見於年輕人，治療依分布範圍決定。",
    "Caroli disease：ductal plate malformation with intrahepatic bile duct dilatation"
  ),
  update(
    38,
    `
【題幹解析】
胰臟惡性腫瘤手術要分 pancreatic adenocarcinoma 與 pancreatic neuroendocrine tumor。胰腺癌若有肝轉移通常不是根治性 Whipple 適應症；邊緣可切除胰癌多先做 neoadjuvant therapy。

【選項詳解】
- A. 錯誤。胰腺癌術中發現肝轉移通常代表全身性疾病，不宜硬做根治性切除。
- B. 錯誤。Whipple procedure 常見重大併發症包括胰漏、胃排空延遲、出血等；膽汁滲漏不是最典型最常見併發症。
- C. 正確。部分胰臟神經內分泌腫瘤若轉移侷限於肝臟、腫瘤生物學較合適且符合嚴格條件，可考慮肝臟移植或肝導向治療。
- D. 錯誤。Borderline resectable pancreatic cancer 現代策略多傾向先 neoadjuvant chemotherapy 或 chemoradiation，再評估切除，以提高 R0 切除率。

【核心考點】
胰腺癌有遠端轉移通常不做根治切除；borderline resectable 多先新輔助治療。Pancreatic NET 的肝轉移管理與胰腺癌不同。
`,
    "Borderline resectable pancreatic cancer 多先新輔助治療；pancreatic NET 肝轉移在嚴格條件下可考慮肝移植。",
    "Pancreatic malignancy：adenocarcinoma metastasis no curative Whipple; NET liver-limited may be treated aggressively"
  ),
  update(
    39,
    `
【題幹解析】
肝硬化病人接受肝癌切除，術前準備重點是評估肝功能、營養、凝血、感染預防與體液狀態。PTBD 主要用於膽道阻塞或需減黃疸情境，不是肝癌切除的必要常規準備。

【選項詳解】
- A. 正確。肝切除屬重大手術，依手術規範給予術前預防性抗生素可降低手術部位感染。
- B. 錯誤，因此為本題要選的敘述。沒有膽道阻塞或黃疸需要處理時，PTBD 不是肝硬化肝癌切除前必要準備。
- C. 正確。適當輸液與血流動力學管理可降低腎損傷與循環不穩風險，但需避免過度輸液。
- D. 正確。肝硬化病人常有營養不良，術前營養優化可降低併發症。

【核心考點】
肝硬化肝切除術前要優化肝功能、營養、感染預防與循環狀態；PTBD 是膽道阻塞工具，不是常規必做。
`,
    "PTBD 用於膽道阻塞或減黃疸需求，不是肝硬化肝癌切除的必要術前準備。",
    "HCC resection prep：nutrition, fluids, antibiotics; PTBD only when biliary indication"
  ),
  update(
    40,
    `
【題幹解析】
Tertiary hyperparathyroidism 是長期 secondary hyperparathyroidism 後，副甲狀腺變成自主分泌 PTH。最典型情境是慢性腎衰竭病人腎移植後，低鈣刺激解除但 PTH 仍過高。

【選項詳解】
- A. 錯誤。原發性副甲狀腺亢進成功治療後不會導致三級副甲狀腺亢進。
- B. 錯誤。單純低血鈣可刺激 secondary hyperparathyroidism，但 tertiary 需要長期刺激後形成自主分泌。
- C. 正確。慢性腎衰竭長期造成 secondary hyperparathyroidism，腎移植後若副甲狀腺仍自主分泌 PTH，即為 tertiary hyperparathyroidism 的經典情境。
- D. 錯誤。甲狀腺切除後較擔心副甲狀腺低下造成低血鈣，不是 tertiary hyperparathyroidism。

【核心考點】
Primary 是腺體自主；secondary 是低鈣或 CKD 代償；tertiary 是長期 secondary 後腺體自主，常在腎移植後看到。
`,
    "Tertiary hyperparathyroidism 常見於 CKD 長期 secondary HPT 後，腎移植後仍自主分泌 PTH。",
    "Hyperparathyroidism：tertiary = autonomous PTH after long secondary HPT, classically post-transplant"
  ),
  update(
    41,
    `
【題幹解析】
甲狀腺乳突癌手術範圍取決於腫瘤大小、雙側性、甲狀腺外侵犯、淋巴結狀態與是否需要後續 RAI。若計畫做 RAI，通常需要全甲狀腺或近全切除，單葉切除不足以達到 RAI 目的。

【選項詳解】
- A. 正確。高風險或雙側腫瘤常需 total 或 near-total thyroidectomy，以利疾病控制與後續追蹤。
- B. 錯誤，因此為本題要選的敘述。RAI 需要足夠移除正常甲狀腺組織與腫瘤負荷，單葉切除不利於 RAI 治療與 thyroglobulin 追蹤。
- C. 正確。1 到 4 cm、無甲狀腺外侵犯且 cN0 的 PTC，可依風險與病人條件選擇單葉切除或全甲狀腺切除。
- D. 正確。低風險 papillary thyroid microcarcinoma 可考慮 active surveillance，尤其無侵犯或淋巴結轉移時。

【核心考點】
PTC 手術不是一律全切或一律單葉；需看風險分層與 RAI 需求。需要 RAI 時通常不能只做腫瘤側單葉切除。
`,
    "PTC 若需 RAI，通常需全甲狀腺或近全切除；低風險 1-4 cm 可在單葉與全切間個別化。",
    "Papillary thyroid cancer：RAI planned -> total/near-total thyroidectomy"
  ),
  update(
    42,
    `
【題幹解析】
病人有 3.23 cm 甲狀腺結節、不規則、顯微鈣化，屬惡性風險高的超音波特徵。能提供良惡性確定資訊的下一步是 ultrasound-guided FNA cytology。

【選項詳解】
- A. 錯誤。血中 thyroglobulin 不能可靠鑑別甲狀腺結節良惡性，較常用於甲狀腺癌術後追蹤。
- B. 正確。細針抽吸細胞學是評估高風險甲狀腺結節良惡性的關鍵檢查。
- C. 錯誤。核醫掃描主要評估功能性 hot nodule；多數甲狀腺癌為 cold nodule，但掃描不能排除惡性。
- D. 錯誤。MRI 可看局部侵犯或解剖關係，但不是鑑別甲狀腺結節良惡性的第一線確診工具。

【核心考點】
甲狀腺結節有不規則邊緣、microcalcification、低回音或高度可疑特徵時，依大小門檻安排 FNA；thyroglobulin 不是初診鑑別工具。
`,
    "高風險超音波特徵的甲狀腺結節應做 FNA cytology；thyroglobulin 主要用於術後追蹤。",
    "Thyroid nodule：suspicious US features -> FNA, not serum thyroglobulin"
  ),
  update(
    43,
    `
【題幹解析】
30 到 39 歲女性有可觸及乳房硬塊，影像評估通常先以乳房超音波為主，必要時搭配診斷性 mammogram。不能直接跳到手術或 MRI。

【選項詳解】
- A. 錯誤。FNA 可在特定情境使用，但對可疑實體病灶，影像分級後常以 core needle biopsy 取得組織診斷更完整；不宜未影像評估就直接 FNA。
- B. 錯誤。懷疑惡性不代表直接手術切除；應先完成影像與切片診斷，以利分期與治療規劃。
- C. 正確。30 歲以上未滿 40 歲的可觸及病灶，乳房超音波是重要初始檢查，必要時加做診斷性乳房攝影。
- D. 錯誤。MRI 對高風險篩檢或問題解決有角色，但不是一般可觸及乳房硬塊的第一線初始檢查。

【核心考點】
年輕女性可觸及乳房腫塊先做目標超音波；30 歲以上可依情況加診斷性 mammogram。可疑影像再用 core needle biopsy 確診。
`,
    "30-39 歲可觸及乳房病灶先做乳房超音波，必要時搭配診斷性乳房攝影。",
    "Palpable breast mass age 30-39：targeted ultrasound +/- diagnostic mammography"
  ),
  update(
    44,
    `
【題幹解析】
乳房 MRI 出現快速增強後 washout pattern 是惡性可疑動態增強特徵。下一步應取得組織診斷，通常用 core needle biopsy。

【選項詳解】
- A. 正確。可疑影像病灶需以粗針切片取得組織，確認病理與受體狀態後才能規劃治療。
- B. 錯誤。PET-CT 不是 1.5 cm 可疑乳房病灶的初始確診工具，不能取代切片。
- C. 錯誤。未有組織診斷前直接手術切除不利於完整治療規劃，尤其若需 neoadjuvant therapy。
- D. 錯誤。MRI 已顯示 washout 可疑病灶，不能因 mammogram 陰性就只追蹤半年；緻密乳房或 MRI-only lesion 仍需處理。

【核心考點】
BI-RADS 可疑病灶的下一步是 tissue diagnosis。MRI washout pattern 提高惡性疑慮，應安排影像導引切片。
`,
    "乳房 MRI washout pattern 屬可疑惡性特徵，下一步是 core needle biopsy。",
    "Breast MRI washout lesion：needs tissue diagnosis with core needle biopsy"
  ),
  update(
    45,
    `
【題幹解析】
Invasive lobular carcinoma 常以單列細胞浸潤，影像上可呈現不明顯、擴散性、邊界模糊或 architectural distortion，不一定形成清楚腫塊。

【選項詳解】
- A. 錯誤。清楚邊緣、單一腫塊比較不像 invasive lobular carcinoma 的典型影像陷阱。
- B. 正確。小葉癌常呈擴散性分布、邊界不清，容易低估病灶範圍。
- C. 錯誤。高回聲且血流增加不是小葉癌最典型的特殊影像描述。
- D. 錯誤。均勻鈣化不是 invasive lobular carcinoma 的常見重點；ductal carcinoma in situ 更常考微鈣化。

【核心考點】
Invasive lobular carcinoma 影像常不形成清楚腫塊，可能多中心、多發或擴散性浸潤，範圍容易被 mammogram 或 ultrasound 低估。
`,
    "Invasive lobular carcinoma 常呈擴散性、邊界模糊或結構扭曲，不一定形成清楚腫塊。",
    "Invasive lobular carcinoma：diffuse, ill-defined, often underestimated"
  ),
  update(
    46,
    `
【題幹解析】
極低出生體重早產兒開始餵食後出現腹脹、血便、體溫不穩、呼吸暫停、心搏過慢與 pneumatosis intestinalis，典型是 NEC。初始處置是禁食、胃腸減壓、輸液、廣效抗生素與嚴密監測。

【選項詳解】
- A. 錯誤。NEC 需要腸道休息與靜脈抗生素，不能用口服抗生素處理。
- B. 錯誤。腸道狹窄是 NEC 後期併發症評估；急性疑似 NEC 時不先做上消化道攝影確認狹窄。
- C. 錯誤。沒有穿孔、腹膜炎或臨床惡化時，不是所有 NEC 都立即手術切除。
- D. 正確。禁食、口胃管減壓、靜脈輸液、廣效抗生素與支持治療，是疑似 NEC 的初始處置。

【核心考點】
NEC 初始先 NPO、NG/OG decompression、IV fluids、broad-spectrum antibiotics。手術留給穿孔、腹膜炎、壞死或保守失敗。
`,
    "疑似 NEC 的初始處置是禁食、胃腸減壓、輸液與廣效靜脈抗生素。",
    "NEC：NPO + gastric decompression + IV broad-spectrum antibiotics first"
  ),
  update(
    47,
    `
【題幹解析】
承上題，早產兒 NEC 若出現 portal venous gas、free air 與生命徵象不穩，代表穿孔與重症。題目強調「床邊」治療，極低體重且不穩定嬰兒可先做腹膜引流作為減壓與感染控制。

【選項詳解】
- A. 錯誤。正中開腹切除吻合對生命徵象不穩的極低體重新生兒負荷大，且急性污染環境下直接吻合風險高。
- B. 錯誤。開腹與造口可用於可耐受手術者，但題目指定床邊處置與不穩定病況，較適合先腹膜引流。
- C. 正確。床邊放置腹膜引流管可減壓、排出污染腹水，作為極低體重或不穩定 NEC 穿孔病人的緊急處置。
- D. 錯誤。中央靜脈導管可作支持治療，但不能處理腸穿孔造成的腹腔污染與壓力問題。

【核心考點】
NEC 穿孔需外科處理；極低體重或不穩定的新生兒，床邊 peritoneal drainage 是重要選項，可作暫時或有時決定性處置。
`,
    "不穩定極低體重 NEC 穿孔病人可先床邊腹膜引流，減壓並控制感染。",
    "NEC perforation unstable VLBW infant：bedside peritoneal drainage"
  ),
  update(
    48,
    `
【題幹解析】
疑似睪丸惡性腫瘤的處理重點是陰囊超音波、腫瘤指標、分期影像與 radical inguinal orchiectomy。追蹤最重要指標是 AFP、beta-hCG、LDH，不是 CEA 或 PSA。

【選項詳解】
- A. 正確。陰囊腫大需排除外傷、陰囊水腫、疝氣、附睪炎、扭轉等鑑別診斷。
- B. 正確。惡性睪丸腫瘤標準手術是經鼠蹊部根除性睪丸切除，包含高位精索控制，避免經陰囊切開造成腫瘤播散。
- C. 錯誤，因此為本題要選的敘述。睪丸腫瘤追蹤指標主要是 AFP、beta-hCG 與 LDH；CEA 與 PSA 不是最重要指標。
- D. 正確。術前或治療前完成適當影像分期，有助於後續治療與追蹤規劃。

【核心考點】
睪丸癌標準術式是 radical inguinal orchiectomy；腫瘤指標背 AFP、beta-hCG、LDH。
`,
    "睪丸腫瘤指標是 AFP、beta-hCG、LDH；標準手術為 radical inguinal orchiectomy。",
    "Testicular tumor：AFP, beta-hCG, LDH; radical inguinal orchiectomy"
  ),
  update(
    49,
    `
【題幹解析】
幼兒黃綠色嘔吐代表膽汁性嘔吐，需懷疑腸旋轉不良併 midgut volvulus。都卜勒超音波若出現腸繫膜血管旋轉的 whirlpool sign，最支持 volvulus。

【選項詳解】
- A. 錯誤。Malrotation 是造成 volvulus 的基礎異常，但題目圖像若呈 whirlpool sign 與急性膽汁性嘔吐，最直接診斷是 volvulus。
- B. 正確。Volvulus 會使腸繫膜與血管扭轉，造成膽汁性嘔吐並可能快速進展為腸缺血，是小兒外科急症。
- C. 錯誤。Intussusception 常見陣發腹痛、果醬樣血便，超音波是 target sign 或 doughnut sign，不是腸繫膜血管旋轉。
- D. 錯誤。腹腔內腫瘤可造成腹部腫塊或阻塞，但不解釋典型膽汁性嘔吐合併 whirlpool 型血管扭轉。

【核心考點】
小兒膽汁性嘔吐是 volvulus 警訊；超音波 whirlpool sign 支持 midgut volvulus，需要緊急處置。
`,
    "小兒膽汁性嘔吐合併超音波 whirlpool sign，優先想到 midgut volvulus。",
    "Bilious vomiting infant/child：whirlpool sign -> volvulus"
  ),
  update(
    50,
    `
【題幹解析】
尿道下裂是尿道開口位於陰莖腹側近端位置，常合併腹側包皮不足與 chordee。外觀重點是 dorsal hooded foreskin，也就是腹側包皮缺損。

【選項詳解】
- A. 錯誤。尿道下裂可合併陰莖腹側彎曲 ventral chordee，不是背面纖維黏連。
- B. 正確。陰莖腹面包皮缺損、背側包皮帽狀堆積，是尿道下裂常見外觀特徵。
- C. 錯誤。大多數單純尿道下裂不需要例行荷爾蒙與染色體核型分析；若合併雙側隱睪、嚴重近端尿道下裂或性別發育差異疑慮才需評估。
- D. 錯誤。手術重點是矯正彎曲、重建尿道與外觀，不是重建尿道海綿體作為固定必要步驟。

【核心考點】
Hypospadias 看腹側尿道開口、ventral chordee、ventral foreskin deficiency/dorsal hood。不要在未評估前做割包皮，因包皮可能用於修補。
`,
    "尿道下裂典型外觀是腹側包皮缺損與背側帽狀包皮，常合併 ventral chordee。",
    "Hypospadias：ventral meatus, ventral foreskin deficiency, dorsal hood"
  ),
  update(
    51,
    `
【題幹解析】
Wilms tumor 是兒童腎母細胞瘤，與 WT1、WT2 區域異常最相關。其他選項分別連到神經母細胞瘤、Li-Fraumeni 或 MEN2/甲狀腺髓質癌等考點。

【選項詳解】
- A. 正確。WT1 位於 11p13，WT2 區域位於 11p15，與 Wilms tumor 及 WAGR、Denys-Drash、Beckwith-Wiedemann 等症候群相關。
- B. 錯誤。N-MYC amplification 是 neuroblastoma 的重要預後因子。
- C. 錯誤。p53 突變與 Li-Fraumeni syndrome、多種癌症風險相關，不是 Wilms tumor 最典型基因。
- D. 錯誤。RET 突變常見於 MEN2、甲狀腺髓質癌與部分 Hirschsprung disease。

【核心考點】
Wilms tumor 背 WT1/WT2；neuroblastoma 背 N-MYC；MEN2 背 RET。兒科腫瘤基因要成組記憶。
`,
    "Wilms tumor 最相關基因區域是 WT1、WT2。",
    "Pediatric tumor genes：Wilms -> WT1/WT2; neuroblastoma -> N-MYC; MEN2 -> RET"
  ),
  update(
    52,
    `
【題幹解析】
左側結腸癌 cT3N0M0 代表腫瘤侵出肌層到腸周組織但無淋巴或遠端轉移。可切除結腸癌的標準治療是 oncologic colectomy 加區域淋巴結清除。

【選項詳解】
- A. 錯誤。新輔助化療可在特定局部晚期或研究情境考慮，但一般可切除 cT3N0 結腸癌不以它作為最標準下一步。
- B. 錯誤。ESD 適合侷限於黏膜或極淺層、低風險的早期病灶；T3 已侵及腸壁外組織，不能局部內視鏡切除。
- C. 正確。部分結腸切除合併根治性淋巴結清除，是可切除非轉移性結腸癌的主要治療。
- D. 錯誤。術前同步化放療是直腸癌常見策略；結腸癌 cT3N0M0 通常不以 neoadjuvant CCRT 為標準。

【核心考點】
結腸癌和直腸癌治療不同。可切除 T3N0M0 結腸癌以 oncologic colectomy + lymph node dissection 為主；直腸癌才常考術前 CCRT。
`,
    "可切除 cT3N0M0 結腸癌標準治療是部分結腸切除加區域淋巴結清除。",
    "Colon cancer cT3N0M0：oncologic colectomy with lymph node dissection"
  ),
  update(
    53,
    `
【題幹解析】
乙狀結腸扭轉若沒有腹膜炎或壞死，常可先大腸鏡減壓復位。但本題已有發燒、心跳快、反彈痛，代表可能缺血、壞死、穿孔或腹膜炎，不適合先做大腸鏡復位。

【選項詳解】
- A. 正確。腸阻塞或扭轉常有脫水與電解質異常，靜脈輸液與矯正是基本處置。
- B. 錯誤，因此為本題要選的處置。有腹膜炎或敗血症徵象時，大腸鏡減壓可能延誤手術且增加穿孔風險。
- C. 正確。發燒心跳快需懷疑敗血症，應抽血培養並給予抗生素。
- D. 正確。局部反彈痛提示腹膜刺激，應安排緊急剖腹探查或手術處理。

【核心考點】
Sigmoid volvulus：穩定且無腹膜炎可內視鏡減壓；有腹膜炎、缺血、穿孔或敗血症時直接手術。
`,
    "乙狀結腸扭轉若有腹膜炎或敗血症徵象，不應先做大腸鏡復位，需手術。",
    "Sigmoid volvulus：endoscopic detorsion only if no peritonitis/ischemia"
  ),
  update(
    54,
    `
【題幹解析】
腹腔鏡氣腹最常用 CO2，因不易燃、血中溶解度高且相對容易由肺排出。CO2 吸收後造成高碳酸血症與呼吸性酸中毒時，主要靠肺部通氣排出，不是靠腎臟直接排出碳酸來快速矯正。

【選項詳解】
- A. 正確。CO2 是目前最常用氣腹氣體。
- B. 正確。臨床常用 12 到 15 mmHg 左右壓力取得視野，同時避免過高壓力造成靜脈回流下降與呼吸循環影響。
- C. 錯誤，因此為本題要選的敘述。CO2 進入血液後主要透過肺部增加通氣排出；腎臟對酸鹼有慢性調節角色，但不是術中快速清除 CO2 的主要途徑。
- D. 正確。充氣太快或腹膜牽拉可刺激迷走神經，造成心搏過緩或低血壓，處理包括暫停充氣、放氣、給 atropine 等。

【核心考點】
CO2 氣腹造成 hypercarbia 時調呼吸器，不是靠腎臟即時排出。氣腹壓力與充氣速度都會影響循環。
`,
    "CO2 氣腹造成的 hypercarbia 主要靠肺通氣排出；腎臟不是術中快速矯正的主要器官。",
    "Pneumoperitoneum：CO2 absorbed -> ventilatory elimination; pressure 12-15 mmHg"
  ),
  update(
    55,
    `
【題幹解析】
遠端胃癌部分胃切除加 D2 淋巴結清除會處理胃周與主要供血血管旁淋巴結，但不會把上腸繫膜動脈當作需結紮血管。SMA 是供應中腸的重要大血管，結紮會造成災難性腸缺血。

【選項詳解】
- A. 錯誤，因此為本題要選的敘述。右胃、右胃網膜、左胃等血管可依手術範圍處理；但 superior mesenteric artery 不屬遠端胃切除需結紮的血管。
- B. 正確。遠端胃切除包含幽門、胃竇與安全切緣，實際範圍依腫瘤位置決定。
- C. 正確。重建可採 Billroth I 胃十二指腸吻合或 Billroth II/Roux-en-Y 胃空腸吻合。
- D. 正確。D2 清除涵蓋胃周與主要血管旁淋巴結；胃癌手術也要求足夠淋巴結數，常以至少 15 顆作分期品質門檻。

【核心考點】
胃癌 D2 清除是清淋巴結，不是任意結紮大血管。遠端胃切除不會結紮 SMA。
`,
    "遠端胃癌 D2 手術不會結紮上腸繫膜動脈；SMA 供應中腸，結紮會造成嚴重缺血。",
    "Distal gastrectomy D2：lymphadenectomy around named vessels, not SMA ligation"
  ),
  update(
    56,
    `
【題幹解析】
本題問骨代謝疾病何者最適當。Gaucher disease 是 lysosomal storage disease，可造成肝脾腫大、貧血血小板低下與骨痛、骨梗塞或骨壞死。

【選項詳解】
- A. 錯誤。Brown tumor 是副甲狀腺亢進造成骨吸收後的反應性病灶，診斷需結合血鈣、PTH、影像與臨床，不能靠局部腫瘤採樣單獨確認。
- B. 正確。Gaucher disease 為家族性 glucocerebrosidase 缺陷疾病，可造成肝脾腫大與骨梗塞、骨痛、骨壞死。
- C. 錯誤。Paget disease 的 viral inclusion 概念較與 osteoclast 異常有關，不是 osteoblast 出現包涵體。
- D. 錯誤。Paget disease 好發於中老年人，X 光可見 osteolytic 與 osteoblastic 混合變化，不是年輕族群好發。

【核心考點】
Gaucher disease：glucocerebrosidase deficiency、hepatosplenomegaly、bone crisis/infarct。Paget disease 好發老人且以 osteoclast 活性異常起始。
`,
    "Gaucher disease 可造成肝脾腫大與骨梗塞；Paget disease 好發中老年人。",
    "Gaucher disease：hepatosplenomegaly and bone infarct"
  ),
  update(
    57,
    `
【題幹解析】
髖臼 AP view 的線條包含 iliopectineal line、ilioischial line、acetabular roof、anterior/posterior wall 等。官方答案指出選項 C 不適當，代表圖中編號 5 並非髖臼頂。

【選項詳解】
- A. 正確。Iliopectineal line 代表 anterior column/anterior wall 相關輪廓，沿髂骨至恥骨上支方向延伸，是骨盆 AP 片重要標記。
- B. 正確。Ilioischial line 代表 posterior column 內側輪廓，與髖臼後柱判讀有關。
- C. 錯誤，因此為本題要選的敘述。依官方圖示，編號 5 的實線不是 acetabular roof；髖臼頂通常是負重區上方的 sourcil/roof 輪廓。
- D. 正確。Posterior lip 的邊緣在 AP view 上常呈較外側或特定輪廓線，可用於判讀後壁位置與骨折。

【核心考點】
骨盆 AP 片判讀髖臼要分 anterior column、posterior column、roof、前後壁。圖形題應以官方標號為準，不能只靠文字名稱硬背。
`,
    "髖臼 AP view 要能區分 iliopectineal line、ilioischial line、acetabular roof 與前後壁。",
    "Acetabular AP landmarks：iliopectineal, ilioischial, roof, anterior/posterior wall"
  ),
  update(
    58,
    `
【題幹解析】
Dupuytren contracture 是掌腱膜纖維增生與攣縮，常見於男性、年長者、北歐或歐洲血統者，常侵犯無名指與小指的 MCP/PIP 關節。

【選項詳解】
- A. 正確。男性較常見，且常有家族與族群差異。
- B. 錯誤，因此為本題要選的敘述。Dupuytren contracture 在歐洲人，特別北歐血統，比亞洲人常見。
- C. 正確。早期無明顯功能受限可觀察、復健或保守處理；進展到攣縮影響功能才考慮注射或手術。
- D. 正確。常侵犯掌指關節，也可影響近端指間關節，造成手指屈曲攣縮。

【核心考點】
Dupuytren contracture：男性、歐洲血統、掌腱膜結節與攣縮、MCP/PIP flexion contracture。
`,
    "Dupuytren contracture 在歐洲血統較常見，常侵犯 MCP/PIP 關節造成屈曲攣縮。",
    "Dupuytren contracture：European ancestry, male, MCP/PIP flexion contracture"
  ),
  update(
    59,
    `
【題幹解析】
肩關節複合體的穩定性來自骨性結構、盂唇、韌帶、關節囊與肌肉。上肢與中軸骨骼唯一真正骨性連接是胸鎖關節，透過鎖骨連到胸骨。

【選項詳解】
- A. 錯誤。Glenohumeral ligaments 是關節囊增厚形成的韌帶樣結構，不是界線非常清楚、平行排列的獨立帶狀韌帶。
- B. 錯誤。Scapulothoracic articulation 是功能性關節，不是真正具有關節囊與滑液腔的 synovial joint。
- C. 正確。鎖骨透過 sternoclavicular joint 連接上肢帶與 axial skeleton，是唯一骨性連接。
- D. 錯誤。Glenoid 關節面積遠小於 humeral head，約只涵蓋一部分，因此肩關節活動度高但骨性穩定度低，需盂唇與軟組織補強。

【核心考點】
肩帶唯一骨性連接是 clavicle-sternum 的胸鎖關節；scapulothoracic 是功能性滑動面，不是真正滑液關節。
`,
    "鎖骨是上肢與中軸骨骼唯一骨性連接；scapulothoracic articulation 是功能性關節。",
    "Shoulder anatomy：clavicle via SC joint is only bony link to axial skeleton"
  ),
  update(
    60,
    `
【題幹解析】
先天性脊柱側彎的進展風險取決於畸形型態與生長潛力。Unilateral unsegmented bar 合併對側 hemivertebra 是高風險組合，會因一側無法生長、對側持續生長而快速惡化。

【選項詳解】
- A. 錯誤。年齡小代表剩餘生長多，對高風險畸形反而更容易進展，單純觀察不適合。
- B. 錯誤。先天性骨性畸形對背架反應有限，背架難以阻止 unilateral bar + hemivertebra 的進展。
- C. 錯誤。牽引可用於特定僵硬或術前矯正情境，但不是此高風險先天畸形的主要治療判斷。
- D. 正確。Unilateral bar 加對側 hemivertebra 常快速惡化，需早期手術如 hemiepiphysiodesis、切除或融合策略以阻止進展。

【核心考點】
先天性 scoliosis 最怕 unilateral unsegmented bar with contralateral hemivertebra。年紀越小剩餘生長越多，進展風險越高。
`,
    "Unilateral bar 合併對側 hemivertebra 是快速惡化的先天性脊柱側彎型態，常需早期手術。",
    "Congenital scoliosis：unilateral bar + contralateral hemivertebra = high progression"
  ),
  update(
    61,
    `
【題幹解析】
年輕運動員 ACL 完全斷裂合併外側半月板破裂，若有不穩定與運動需求，通常進行 ACL reconstruction 並同時處理可修補的半月板。半月板能修就盡量保留，以降低退化風險。

【選項詳解】
- A. 錯誤。ACL reconstruction 不必固定延遲 6 個月；急性期先消腫、恢復關節活動度後即可安排，過久延遲可能增加半月板與軟骨傷害。
- B. 錯誤。年輕運動員的標準多為 ACL reconstruction；primary repair 只適用少數近端撕裂且條件合適者。
- C. 錯誤。術後復健會早期活動，但若同時做半月板修補，活動角度與負重常需保護，不能一概立即全範圍活動。
- D. 正確。合併可修補半月板破裂時，常與 ACL reconstruction 同時處理，恢復穩定並保留半月板。

【核心考點】
ACL 完全斷裂的年輕運動員常需重建；合併半月板破裂時，能修補就同步修補以保護膝關節長期功能。
`,
    "年輕運動員 ACL 完全斷裂合併半月板破裂，常同時做 ACL 重建與半月板修補。",
    "ACL tear athlete：reconstruction plus meniscus repair when repairable"
  ),
  update(
    62,
    `
【題幹解析】
Spinal shock 是脊髓損傷後損傷節段以下反射、運動與感覺暫時消失。判定完全或不完全損傷需等 spinal shock 解除；其結束常以 bulbocavernosus reflex 回復作為重要線索。

【選項詳解】
- A. 正確。Spinal shock 期間反射消失會干擾神經學分級，需等反射回復後更能判斷 complete 或 incomplete injury。
- B. 正確。脊髓休克會使損傷節段以下反射、肌張力、運動與感覺暫時消失。
- C. 錯誤，因此為本題要選的敘述。最常用來代表 spinal shock 結束的早期反射是 bulbocavernosus reflex，不是 cremasteric reflex。
- D. 正確。Spinal shock 本身沒有特異治療，處理重點是支持、固定、維持灌流與治療脊髓損傷原因。

【核心考點】
Spinal shock 期間不能急著判定完全損傷；bulbocavernosus reflex 回復常用來表示 spinal shock 結束。
`,
    "Spinal shock 結束常以 bulbocavernosus reflex 回復判斷，不是 cremasteric reflex。",
    "Spinal shock：loss of reflexes below lesion; bulbocavernosus return marks resolution"
  ),
  update(
    63,
    `
【題幹解析】
股骨頭缺血性壞死早期可在尚未塌陷時考慮保留股骨頭治療；一旦出現 crescent sign，代表軟骨下骨折與即將或已開始塌陷，保守治療效果差。

【選項詳解】
- A. 錯誤。早期病變主要在股骨頭前外上方的軟骨下骨，而不是先發生在關節軟骨。
- B. 錯誤。塌陷前早期病變可考慮核心減壓、藥物或其他保頭治療；不一定直接人工關節置換。
- C. 正確。Crescent sign 代表 subchondral fracture，顯示結構已失穩，單純保守治療如雙磷酸鹽、高壓氧或震波較不適合。
- D. 錯誤。股骨頭塌陷後，核心減壓與結構性骨移植的效果下降；嚴重塌陷或關節炎常需人工髖關節置換。

【核心考點】
ONFH 治療看是否塌陷。Pre-collapse 可保頭；crescent sign 或 collapse 後保守與核心減壓效果差，常往重建或置換思考。
`,
    "股骨頭壞死出現 crescent sign 代表軟骨下骨折，通常不適合單純保守治療。",
    "Femoral head osteonecrosis：crescent sign = subchondral fracture/collapse risk"
  ),
  update(
    64,
    `
【題幹解析】
發燒、低血壓、膿尿、腎功能損傷，加上輸尿管結石與水腎，是阻塞合併感染造成的泌尿敗血症風險。急性處置是先引流減壓，不能在感染未控制時直接做 definitive stone surgery。

【選項詳解】
- A. 正確。1 cm 輸尿管結石自行排出機率低，需告知家屬後續大多需要介入處理。
- B. 正確。感染性阻塞需立即解除阻塞，可用 PCN 或 ureteral stent，並搭配抗生素與支持治療。
- C. 錯誤，因此為本題要選的處置。敗血症與阻塞尚未控制時，不宜急做軟式輸尿管鏡同時處理腎與輸尿管結石，會增加菌血症與休克風險。
- D. 正確。ESWL 不是感染性阻塞急症的當下處理，且有敗血症風險時應先引流與抗生素。

【核心考點】
Obstructive pyelonephritis/sepsis：先抗生素加緊急 drainage，再延後處理結石。不要在感染未控制時做 definitive stone manipulation。
`,
    "感染性阻塞性輸尿管結石需先 PCN 或雙 J 導管引流，感染控制後再處理結石。",
    "Obstructed infected stone：urgent decompression first, definitive stone treatment later"
  ),
  update(
    65,
    `
【題幹解析】
腎上腺 incidentaloma 要評估是否分泌荷爾蒙與是否惡性。年輕女性有高血壓與低血鉀，需篩檢 primary aldosteronism，通常以 aldosterone-renin ratio 作為初步檢查。

【選項詳解】
- A. 錯誤。1.5 cm 腎上腺結節不能未完成荷爾蒙與影像風險評估就直接切除。
- B. 正確。高血壓合併低血鉀是原發性醛固酮增多症的重要線索，應安排篩檢。
- C. 錯誤。腎上腺切片很少作為初始處置，且在未排除 pheochromocytoma 前切片有危險；對分泌性病灶診斷幫助也有限。
- D. 錯誤。單純 6 個月後追蹤會漏掉可治療的分泌性高血壓原因；本題已有低血鉀與高血壓。

【核心考點】
Adrenal incidentaloma 不是只看大小；要篩功能。高血壓加低血鉀優先篩 primary aldosteronism。
`,
    "腎上腺 incidentaloma 合併高血壓與低血鉀，應篩檢 primary aldosteronism。",
    "Adrenal incidentaloma：hypertension + hypokalemia -> screen primary aldosteronism"
  ),
  update(
    66,
    `
【題幹解析】
Bosniak 分類用來評估腎囊腫惡性風險。若囊腫有不規則邊緣與 enhancing solid nodules，屬高度惡性疑慮的 Bosniak IV。

【選項詳解】
- A. 錯誤。Bosniak I 是單純囊腫，薄壁、無 septa、無 enhancement。
- B. 錯誤。Bosniak II 只有少量薄隔或細小鈣化，惡性風險低，不會有實心結節。
- C. 錯誤。Bosniak III 有厚壁或厚隔、可增強，屬不確定但高風險；若出現明確 enhancing solid nodule，分類再升到 IV。
- D. 正確。Bosniak IV 的關鍵是囊性病灶中有 enhancing soft tissue/solid nodular component，惡性風險最高。

【核心考點】
腎囊腫只要看到增強實心結節，就要想到 Bosniak IV。Bosniak III 是厚壁厚隔但未達明確實心結節。
`,
    "腎囊腫有增強實心結節屬 Bosniak IV，惡性風險最高。",
    "Bosniak cyst：enhancing solid nodule -> category IV"
  ),
  update(
    67,
    `
【題幹解析】
5α-reductase inhibitor 適合攝護腺較大、DHT 驅動增生明顯的 BPH，可縮小腺體並降低尿滯留或手術風險。若攝護腺不大，症狀改善效果有限，不能說無論大小都有效。

【選項詳解】
- A. 正確。5α-reductase inhibitor 抑制 testosterone 轉成 DHT，代表藥物包括 finasteride、dutasteride。
- B. 正確。DHT 下降會讓攝護腺上皮與間質增生減少，腺體縮小，症狀逐漸改善。
- C. 正確。藥效起效慢，常需 6 個月左右達到明顯體積縮小與症狀改善，約可使攝護腺體積下降 20% 到 30%。
- D. 錯誤，因此為本題要選的敘述。5ARI 對攝護腺較大者效果較好；小攝護腺或以動態平滑肌張力為主的 LUTS，alpha blocker 通常較快。

【核心考點】
5ARI 適合 enlarged prostate，起效慢但可縮小腺體；alpha blocker 改善症狀較快且不依賴腺體縮小。
`,
    "5α-reductase inhibitors 對攝護腺較大的 BPH 較有效，通常需數月才見最大效果。",
    "BPH 5ARI：large prostate, slow onset, shrinks gland; not regardless of size"
  ),
  update(
    68,
    `
【題幹解析】
男性外陰部與睪丸的血流來源需區分內外髂與主動脈分支。Cremaster 主要由 inferior epigastric artery 的 cremasteric branch 供應；inferior epigastric artery 來自 external iliac artery。

【選項詳解】
- A. 正確。Vas deferens 可由 superior vesical artery 分支的 deferential artery 供應，而 superior vesical 來自 internal iliac 系統。
- B. 錯誤，因此為本題要選的敘述。Umbilical artery 的近端可發出 superior vesical artery 供應膀胱上部，不是供應 cremaster 的主要來源。
- C. 正確。Cremasteric artery 來自 inferior epigastric artery，而 inferior epigastric artery 來自 external iliac artery。
- D. 正確。Testicular artery 直接由 abdominal aorta 發出，供應睪丸。

【核心考點】
睪丸血管來自主動脈；輸精管動脈多來自內髂系統；提睪肌血流來自外髂系統的 inferior epigastric artery 分支。
`,
    "Cremasteric artery 來自 inferior epigastric artery；testicular artery 直接來自主動脈。",
    "Male genital blood supply：cremasteric from inferior epigastric, testicular from aorta"
  ),
  update(
    69,
    `
【題幹解析】
本題官方公告接受 C、D 或 CD，問尿床敘述何者錯誤。夜尿症常與夜間尿量、膀胱容量與睡眠喚醒能力不匹配有關；通常 5 歲以前不急著診斷，約 6 歲後若困擾才積極治療。

【選項詳解】
- A. 正確。夜間多尿、夜間膀胱容量不足與喚醒困難，是單一症狀夜尿症的核心三角。
- B. 正確。4 歲仍尿床多可先衛教與觀察；到學齡後仍困擾，再考慮積極治療。
- C. 錯誤，因此為官方可接受答案之一。Desmopressin 與夜尿警鈴是常用第一線治療，但「第一週無反應就沒有證據支持長期使用」過於武斷；治療反應需看使用方式、劑量、依從性與追蹤時間。
- D. 官方也接受。夜尿症有遺傳傾向且曾報告多個基因座，但把第 6 與第 11 號染色體兩個基因座說成明確風險基因並直接連到睡眠、尿量與膀胱功能，證據表述過度簡化。

【核心考點】
夜尿症治療先看年齡與困擾程度。Desmopressin 對夜間多尿較快，夜尿警鈴對長期乾床訓練較有幫助；基因描述不要背得過度絕對。
`,
    "夜尿症常由夜間尿量、膀胱容量與喚醒能力不匹配造成；官方本題接受 C、D 或 CD。",
    "Enuresis：nocturnal urine, bladder capacity, arousal; alarm/desmopressin first-line when age appropriate",
    ["官方公告本題答 C、D 或 CD 均給分；C 的第一週無效即不續用與 D 的基因表述都需人工留意。"]
  ),
  update(
    70,
    `
【題幹解析】
移植腎動態核醫檢查可看灌流、攝取與排泄，協助追蹤急性排斥、ATN 或 delayed graft function，但確診區分仍常需腎臟切片。核醫也能偵測尿液外漏等泌尿併發症。

【選項詳解】
- A. 正確。急性排斥常可呈現灌流下降、攝取與排泄異常，但影像並非完全特異。
- B. 正確。腎臟切片仍是鑑別急性排斥與 delayed graft function 的關鍵標準。
- C. 正確。Delayed graft function 若恢復，serial imaging 可看到灌流或排泄逐漸改善。
- D. 錯誤，因此為本題要選的敘述。動態腎臟閃爍攝影可顯示放射性尿液在移植腎外聚集，能用於偵測尿液外漏或吻合口漏。

【核心考點】
移植腎核醫檢查可追蹤灌流、功能與尿漏；排斥與 DGF 的確診鑑別仍仰賴臨床、實驗室與常常需要切片。
`,
    "移植腎動態閃爍攝影可偵測尿液外漏；排斥與 DGF 的最佳鑑別仍常需腎切片。",
    "Renal transplant scan：perfusion/function and urine leak; biopsy best for rejection vs DGF"
  ),
  update(
    71,
    `
【題幹解析】
睪丸靜脈回流左右不同：右睪丸靜脈直接回流到下腔靜脈，左睪丸靜脈回流到左腎靜脈。右側新發精索靜脈曲張要注意下腔靜脈或腹膜後病灶。

【選項詳解】
- A. 正確。右側 testicular vein 通常直接注入 inferior vena cava。
- B. 錯誤。右腎靜脈不是右睪丸靜脈正常回流處；左側才典型回流到左腎靜脈。
- C. 錯誤。右外髂靜脈接收下肢與骨盆部分回流，不是睪丸靜脈正常終點。
- D. 錯誤。右下腹壁靜脈屬腹壁回流，不是右睪丸靜脈主回流血管。

【核心考點】
右 testicular vein -> IVC；左 testicular vein -> left renal vein。突然右側 varicocele 要警覺腹膜後或 IVC 受壓。
`,
    "右睪丸靜脈回流至下腔靜脈，左睪丸靜脈回流至左腎靜脈。",
    "Testicular vein drainage：right to IVC, left to left renal vein"
  ),
  update(
    72,
    `
【題幹解析】
肩部 CT 圖形題官方答案為 C，臨床線索指向 posterior shoulder dislocation。後脫臼時肱骨頭卡在肩盂後方，手臂常固定在內轉，病人無法做外轉。

【選項詳解】
- A. 錯誤。肩盂肱關節最常見脫臼是 anterior dislocation；本題影像與無法外轉較符合 posterior dislocation。
- B. 錯誤。後脫臼較會傷及後側肩盂或造成 reverse Hill-Sachs lesion；不是前側肩盂比後側更容易受損。
- C. 正確。Posterior shoulder dislocation 的典型姿勢是內轉、內收，未復位前外轉受限或無法外轉。
- D. 錯誤。多數急性肩脫臼先嘗試閉合復位；開刀用於閉合復位失敗、大骨折、反覆不穩或大型骨缺損等情境。

【核心考點】
Posterior shoulder dislocation 常在 seizure、電擊或跌倒後被漏診；臨床記住固定內轉、外轉受限，影像可見 posterior displacement。
`,
    "Posterior shoulder dislocation 常使手臂固定內轉，復位前外轉受限。",
    "Posterior shoulder dislocation：locked internal rotation and inability to externally rotate"
  ),
  update(
    73,
    `
【題幹解析】
KUB 圖形題官方答案為 medullary nephrocalcinosis。此診斷常見腎髓質或腎錐體區鈣化，可與高鈣尿、高副甲狀腺功能、遠端腎小管酸中毒、海綿腎等相關。

【選項詳解】
- A. 正確。腎髓質鈣化症在 KUB 可見雙側或髓質分布鈣化，病人可有血尿、結石或反覆泌尿症狀。
- B. 錯誤。Hydronephrosis 是集合系統擴張，KUB 不會以髓質鈣化作為主要表現，需超音波或 CT 看腎盂腎盞擴張。
- C. 錯誤。腎結核可有腎盞破壞、鈣化或自體腎切除樣改變，但「急性腎結核」不是典型 KUB 髓質鈣化診斷。
- D. 錯誤。泌尿上皮癌可能造成血尿與充盈缺損，但 KUB 髓質鈣化分布不支持其為最主要診斷。

【核心考點】
Medullary nephrocalcinosis 看腎髓質鈣化，常聯想到高鈣狀態、遠端 RTA、medullary sponge kidney 與反覆結石。
`,
    "腎髓質鈣化症在 KUB 可見髓質分布鈣化，常與高鈣尿、遠端 RTA 或海綿腎相關。",
    "Medullary nephrocalcinosis：medullary/pyramidal calcifications on KUB"
  ),
  update(
    74,
    `
【題幹解析】
年輕女性胸部 X 光異常，CT 圖形題官方答案為 teratoma。畸胎瘤常位於前縱膈，影像可含脂肪、鈣化、牙齒或囊實混合成分。

【選項詳解】
- A. 錯誤。主動脈剝離通常是急性胸背痛與主動脈內膜瓣影像，不會以含脂肪鈣化的前縱膈腫塊為主要表現。
- B. 正確。前縱膈畸胎瘤在 CT 可見脂肪、鈣化與囊性成分，年輕病人胸部影像異常時要列入鑑別。
- C. 錯誤。肺癌多為肺實質腫塊或支氣管相關病灶，年輕女性且影像呈典型前縱膈囊實混合時較不像。
- D. 錯誤。神經源性腫瘤最常位於後縱膈，不是典型前縱膈含脂肪鈣化腫塊。

【核心考點】
前縱膈腫瘤背 4T：thymoma、teratoma、thyroid、terrible lymphoma。Teratoma 的影像線索是脂肪加鈣化或牙齒樣成分。
`,
    "前縱膈畸胎瘤常見脂肪、鈣化與囊實混合成分；神經源性腫瘤多在後縱膈。",
    "Anterior mediastinal mass：teratoma may contain fat and calcification"
  ),
  update(
    75,
    `
【題幹解析】
本題問外傷敘述何者最不適當。外傷機轉最常見是鈍傷；傷口感染風險受污染程度、部位血流、下肢位置、延遲處理與異物影響。臉部與頭皮血流豐富，感染率通常不高。

【選項詳解】
- A. 正確。整體外傷最常見機轉是 blunt trauma，例如車禍、跌倒、撞擊。
- B. 錯誤，因此為本題要選的敘述。頭皮與臉部雖有皮膚菌叢，但血流豐富，清創縫合後感染風險通常低於下肢或污染傷口。
- C. 正確。金屬鐵片多為 radiopaque，大多可在 X 光看到；木頭、塑膠等異物則可能看不清楚。
- D. 正確。下肢血流相對較差、污染機會高、張力與水腫較多，傷口感染風險常高於上肢。

【核心考點】
傷口感染風險不是只看皮膚菌量；血流、污染、異物、位置與延遲處理更重要。臉與頭皮血流佳，感染率相對低。
`,
    "頭皮與臉部血流豐富，外傷傷口感染風險通常不因表皮菌多而最高。",
    "Wound infection risk：lower extremity/contamination worse; face and scalp vascular supply lowers risk"
  ),
  update(
    76,
    `
【題幹解析】
安全帶傷加 Chance fracture 是屈曲牽張傷，常合併腹內臟器傷害，尤其十二指腸、胰臟或小腸繫膜損傷。第一腰椎附近與後腹膜十二指腸位置相符。

【選項詳解】
- A. 錯誤。降主動脈可在高速鈍傷受損，但與 seatbelt sign 加 Chance fracture 的典型配對不如十二指腸。
- B. 錯誤。胃較前方且活動性較高，不是 Chance fracture 最典型連帶受傷器官。
- C. 錯誤。脾臟可因左上腹鈍傷受損，但安全帶屈曲牽張傷的經典腹內傷較偏腸道、腸繫膜、胰十二指腸。
- D. 正確。十二指腸位於後腹膜，容易在安全帶造成的壓迫與脊椎牽張傷中受傷。

【核心考點】
Seatbelt sign + Chance fracture 要找 hollow viscus、mesenteric、pancreaticoduodenal injury。不能只因生命徵象穩定就忽略腹內傷。
`,
    "安全帶傷合併 Chance fracture 要高度懷疑十二指腸、胰臟或腸繫膜損傷。",
    "Chance fracture with seatbelt sign：think duodenal/mesenteric injury"
  ),
  update(
    77,
    `
【題幹解析】
ACL 受傷的理學檢查包括 Lachman test、anterior drawer test 與 pivot shift test。其中 Lachman test 對急性 ACL 斷裂最常用且敏感。

【選項詳解】
- A. 錯誤。Varus stress test 評估外側副韌帶 LCL，而不是 ACL。
- B. 正確。Lachman test 陽性代表脛骨相對股骨前移增加、終點鬆軟，是 ACL 斷裂的重要檢查。
- C. 錯誤。Thomas test 評估髖屈肌攣縮。
- D. 錯誤。FABER test 常用於髖關節或薦髂關節病灶評估，不是 ACL 診斷檢查。

【核心考點】
ACL：Lachman、anterior drawer、pivot shift。LCL：varus stress；MCL：valgus stress；髖關節：FABER/Thomas。
`,
    "Lachman test 是評估 ACL 斷裂的重要理學檢查。",
    "ACL exam：Lachman test"
  ),
  update(
    78,
    `
【題幹解析】
告知癌症、死亡風險等壞消息，是讓病人理解病情並參與決策的過程，核心是尊重病人的自主權與知情同意。

【選項詳解】
- A. 錯誤。行善原則強調促進病人利益，但告知壞消息的倫理基礎不只是醫師認為對病人好，而是讓病人有能力自主決策。
- B. 錯誤。不傷害原則提醒告知方式要避免不必要傷害，但不能因此隱瞞重大診斷。
- C. 錯誤。正義原則重點是公平分配醫療資源與公平對待，與壞消息告知的核心較不直接。
- D. 正確。尊重自主原則要求醫師誠實告知重要資訊，讓病人依自己的價值做醫療選擇。

【核心考點】
壞消息告知不是單純資訊傳遞，而是知情同意與 shared decision-making 的基礎；倫理核心是 respect for autonomy。
`,
    "告知壞消息體現尊重自主原則，讓病人能知情並參與決策。",
    "Medical ethics：breaking bad news -> respect for autonomy"
  ),
  update(
    79,
    `
【題幹解析】
病人已經由專科醫師評估為腦死狀態，但家屬無法接受且要求繼續 ICU 治療。最合適作法是持續溝通、解釋醫學事實與治療界線，並將病人轉出加護病房，而不是單方面停藥或無限期占用 ICU。

【選項詳解】
- A. 錯誤。即使醫學上判定腦死，實務仍需符合程序、法律與院內倫理規範；題目情境重點不是醫師直接宣告後結束討論。
- B. 錯誤。完全接受家屬要求而無限期留 ICU，會造成不符合比例原則的治療與資源使用問題。
- C. 正確。向母親清楚且反覆解釋病情，提供情緒支持與翻譯文化協助，並轉出 ICU，是兼顧溝通、比例原則與醫療資源的作法。
- D. 錯誤。醫師自行停止升壓劑，未經適當溝通、程序與團隊共識，容易違反倫理與法律風險。

【核心考點】
腦死或治療無效情境要重視程序正義、家屬溝通與比例原則。不能單方面停治療，也不等於必須無限期維持 ICU 治療。
`,
    "腦死且家屬難以接受時，應持續解釋並依程序轉出 ICU；不可單方面停藥或無限期 ICU 治療。",
    "Brain death ethics：communicate, follow procedure, avoid unilateral withdrawal or indefinite ICU"
  ),
  update(
    80,
    `
【題幹解析】
成年男性要求結紮，但理學檢查摸不到兩側輸精管，需懷疑 congenital bilateral absence of vas deferens。醫師應誠實告知，並用精液分析確認是否無精症，同時可考慮 CFTR 相關諮詢。

【選項詳解】
- A. 錯誤。若沒有輸精管，照常做輸精管結紮既無必要也可能造成不當醫療；不能為了避免麻煩而隱瞞。
- B. 正確。應如實告知發現，安排精液分析確認，並視情況提供遺傳與生育相關諮詢。
- C. 錯誤。轉介可作為後續選項，但不能取代當下誠實告知與初步確認。
- D. 錯誤。找理由拒絕手術違反誠實與尊重病人自主，也未處理可能的先天異常與生育資訊需求。

【核心考點】
CBAVD 常與 CFTR mutation 相關，可能造成阻塞性無精症。發現異常時要誠實告知、確認診斷並提供適當諮詢。
`,
    "摸不到兩側輸精管時應懷疑 CBAVD，誠實告知並安排精液分析確認。",
    "CBAVD：tell patient, semen analysis, consider CFTR counseling"
  ),
];

function validateUpdates() {
  if (updates.length !== 80) throw new Error(`Expected 80 updates, got ${updates.length}`);
  const seen = new Set();
  for (const item of updates) {
    const sourceQuestion = questionsByNumber.get(item.question_number);
    if (!sourceQuestion) throw new Error(`No source question for ${item.question_number}`);
    if (sourceQuestion.id !== item.question_id) {
      throw new Error(`Question ${item.question_number} id mismatch: ${item.question_id} !== ${sourceQuestion.id}`);
    }
    if (seen.has(item.question_number)) throw new Error(`Duplicate question ${item.question_number}`);
    seen.add(item.question_number);
    for (const heading of ["【題幹解析】", "【選項詳解】", "【核心考點】"]) {
      if (!item.explanation.includes(heading)) {
        throw new Error(`Question ${item.question_number} missing heading ${heading}`);
      }
    }
    for (const label of ["- A.", "- B.", "- C.", "- D."]) {
      if (!item.explanation.includes(label)) {
        throw new Error(`Question ${item.question_number} missing option ${label}`);
      }
    }
  }
}

function writeUpdateFiles() {
  validateUpdates();
  fs.mkdirSync(outDir, { recursive: true });
  for (let start = 1; start <= 80; start += 10) {
    const end = start + 9;
    const batch = updates.filter((item) => item.question_number >= start && item.question_number <= end);
    const payload = {
      source_file: sourceFile,
      dataset_id: datasetId,
      range: { start, end },
      updates: batch,
    };
    const fileName = `q${String(start).padStart(3, "0")}-q${String(end).padStart(3, "0")}.json`;
    fs.writeFileSync(path.join(outDir, fileName), `${JSON.stringify(payload, null, 2)}\n`, "utf8");
  }
}

function mergeUpdates() {
  validateUpdates();
  const allowedFields = [
    "explanation",
    "key_point",
    "flashcard_front",
    "flashcard_back",
    "flashcard_summary",
    "review_status",
    "explanation_model",
    "explanation_generated_at",
  ];
  for (const item of updates) {
    const question = questionsByNumber.get(item.question_number);
    for (const field of allowedFields) {
      question[field] = item[field];
    }
    if (item.manual_review_notes.length > 0 || Object.prototype.hasOwnProperty.call(question, "manual_review_notes")) {
      question.manual_review_notes = item.manual_review_notes;
    }
  }
  fs.writeFileSync(sourceFile, `${JSON.stringify(source, null, 2)}\n`, "utf8");
}

const command = process.argv[2] || "updates";
if (command === "updates") {
  writeUpdateFiles();
  console.log(`Wrote ${updates.length} updates to ${outDir}`);
} else if (command === "merge") {
  mergeUpdates();
  console.log(`Merged ${updates.length} updates into ${sourceFile}`);
} else {
  throw new Error(`Unknown command: ${command}`);
}
