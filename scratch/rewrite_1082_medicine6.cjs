const fs = require("node:fs");
const path = require("node:path");
const cp = require("node:child_process");

const SOURCE_FILE = "public/data/exams/108-2/medicine-6.json";
const DATASET_ID = "108-2_medicine-6";
const UPDATE_DIR = "scratch/rewrite_updates/108-2_medicine-6";
const MODEL = "codex-high-quality-rewrite";
const GENERATED_AT = "2026-08-31T21:45:54+08:00";

const TARGETS = [
  1, 2, 4, 6, 7, 8, 9, 10, 11, 13,
  16, 17, 18, 19, 20, 21, 23, 24, 25, 27,
  28, 29, 31, 32, 33, 34, 35, 36, 37, 38,
  39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
  49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
  60, 62, 63, 64, 65, 66, 67, 68, 69, 71,
  72, 73, 74, 76, 77, 79, 80,
];

const BATCHES = [
  { file: "q001-q013_selected.json", range: { start: 1, end: 13 }, nums: [1, 2, 4, 6, 7, 8, 9, 10, 11, 13] },
  { file: "q016-q027_selected.json", range: { start: 16, end: 27 }, nums: [16, 17, 18, 19, 20, 21, 23, 24, 25, 27] },
  { file: "q028-q038_selected.json", range: { start: 28, end: 38 }, nums: [28, 29, 31, 32, 33, 34, 35, 36, 37, 38] },
  { file: "q039-q048_selected.json", range: { start: 39, end: 48 }, nums: [39, 40, 41, 42, 43, 44, 45, 46, 47, 48] },
  { file: "q049-q058_selected.json", range: { start: 49, end: 58 }, nums: [49, 50, 51, 52, 53, 54, 55, 56, 57, 58] },
  { file: "q060-q071_selected.json", range: { start: 60, end: 71 }, nums: [60, 62, 63, 64, 65, 66, 67, 68, 69, 71] },
  { file: "q072-q080_selected.json", range: { start: 72, end: 80 }, nums: [72, 73, 74, 76, 77, 79, 80] },
];

const ALLOWED_UPDATE_FIELDS = new Set([
  "question_id",
  "question_number",
  "explanation",
  "key_point",
  "flashcard_front",
  "flashcard_back",
  "flashcard_summary",
  "review_status",
  "explanation_model",
  "explanation_generated_at",
  "manual_review_notes",
]);

const ALLOWED_CHANGED_FIELDS = new Set([
  "explanation",
  "key_point",
  "flashcard_summary",
  "review_status",
  "flashcard_front",
  "flashcard_back",
  "explanation_model",
  "explanation_generated_at",
  "manual_review_notes",
]);

const REQUIRED_HEADINGS = ["【題幹解析】", "【選項詳解】", "【核心考點】"];
const BANNED_PHRASES = [
  "非本題答案",
  "不是本題標準答案",
  "回到題幹線索",
  "請用題幹線索連回",
  "題目中選項 A 所代表的鑑別或處置",
  "不能最精準回答本題",
  "最符合題幹",
  "核心記憶點",
  "定義、機轉、典型表現或處置原則",
  "標準答案所接受的判斷",
  "雖然與題目主題相關",
  "與標準答案的關鍵判斷不一致",
  "對照本題核心解析",
  "此選項不是最佳答案",
  "與正確答案的關鍵判斷點不一致",
  "原始解析重點指出",
  "原有解析重點",
  "作答時應回到",
  "熟悉疾病機轉",
  "本題測試",
];

const updates = {};

function explanation(stem, optionLines, core) {
  return `【題幹解析】\n${stem}\n\n【選項詳解】\n- ${optionLines.join("\n- ")}\n\n【核心考點】\n${core}`;
}

function add(questionNumber, item) {
  updates[questionNumber] = item;
}

function summary(front, back) {
  return `${front} -> ${back}`;
}

add(1, {
  stem: "麻醉中體溫監測的陷阱，是把區域麻醉誤認為不用監測。麻醉會抑制體溫調節、造成周邊血管擴張，區域麻醉也可能使阻斷區域散熱增加，因此不能把區域麻醉一概視為不需監測體溫。",
  options: [
    "A. 正確。核心溫度較能反映中樞器官溫度；鼻咽、食道下段、肺動脈等位置常用於核心溫度監測，鼻咽溫度在全身麻醉時尤其實用。",
    "B. 正確。手術室低溫、麻醉抑制寒顫與血管收縮，加上輸液與暴露，讓低體溫比高體溫常見得多。",
    "C. 正確。直腸溫度受局部血流與糞便影響，對快速溫度變化反應較慢；體外循環降溫或復溫時，會落後於較即時的核心監測部位。",
    "D. 錯誤。否定題的正答是這個例外敘述；區域麻醉同樣可干擾體溫調節，長時間手術、大範圍阻斷或高風險病人仍應監測體溫。"
  ],
  core: "麻醉體溫監測不能只看全身麻醉；凡可能發生臨床顯著體溫變化的麻醉，都要選擇合適部位監測。直腸溫度可用，但在快速升降溫時反應較慢。",
  key_point: "區域麻醉也可能造成低體溫，長時間或高風險手術需監測體溫；直腸溫度在快速變溫時會落後核心溫度。",
  flashcard_front: "麻醉體溫監測 / 區域麻醉 / 直腸溫度",
  flashcard_back: "區域麻醉不是一律免體溫監測；直腸溫度反應慢，體外循環等快速變溫時不如鼻咽、食道或肺動脈即時。",
});

add(2, {
  stem: "手術室外麻醉場所仍要達到可安全處理麻醉與急救的基本條件。題組中的 1、2、3 都是必要條件，4 說不需準備電擊器，正好違反急救設備要求。",
  options: [
    "A. 正確。足夠空間、可靠氧氣供應與合適監測儀器都是手術室外麻醉的基本配備；不包含「不需電擊器」才是正確組合。",
    "B. 錯誤。把第 4 項也納入會出問題；手術室外麻醉地點仍須具備或可立即取得急救車、急救藥物與電擊器。",
    "C. 錯誤。第 1 項空間需求正確，但第 4 項不需電擊器錯誤，而且漏掉氧氣與監測。",
    "D. 錯誤。第 2、3 項正確，但第 4 項錯誤，也漏掉足夠的麻醉照護空間。"
  ],
  core: "手術室外麻醉不是降低標準，而是把氧氣、抽吸、監測、空間、照明、急救藥物與電擊器帶到非手術室場域。遇到組合題時，含有「不用急救設備」的選項通常要排除。",
  key_point: "手術室外麻醉場所需有足夠空間、氧氣供應與監測儀器，且急救設備與電擊器不可省略。",
  flashcard_front: "手術室外麻醉 NORA / 基本設備",
  flashcard_back: "NORA 地點需氧氣、抽吸、監測、足夠空間與急救設備；電擊器是安全配備，不是可省略項目。",
});

add(4, {
  stem: "具有支氣管擴張效果的靜脈麻醉藥，官方更正接受 B、C。Ketamine 以交感活性與抑制支氣管收縮著稱，propofol 也可降低氣道阻力；原始單選答案 B 需依更正視為多重答案。",
  options: [
    "A. 錯誤。Thiopental 屬巴比妥類，可能造成組織胺釋放或氣道反應，對氣喘或支氣管痙攣病人不是支氣管擴張代表藥。",
    "B. 正確。Ketamine 會保留交感張力、增加兒茶酚胺作用，常被用在氣喘或支氣管痙攣風險病人的誘導選擇。",
    "C. 正確。Propofol 可抑制氣道反射並降低氣道阻力，官方更正將其列入可給分答案。",
    "D. 錯誤。Midazolam 主要提供鎮靜、抗焦慮與順行性失憶，並不是用來達成支氣管擴張的靜脈麻醉藥。"
  ],
  core: "支氣管痙攣風險題要先想到 ketamine；若題目承認更正，propofol 也可因降低氣道阻力而列為答案。Thiopental 與 midazolam 不具代表性支氣管擴張效果。",
  key_point: "官方更正接受 ketamine 與 propofol 具支氣管擴張或降低氣道阻力效果。",
  flashcard_front: "靜脈麻醉藥 / 支氣管擴張 / 官方更正",
  flashcard_back: "Ketamine 是典型支氣管擴張選擇；propofol 可降低氣道阻力，本題官方更正接受 B、C。",
});

add(6, {
  stem: "肥胖病人生理變化的錯誤點，在於把呼吸需求寫成不變。肥胖會增加耗氧與二氧化碳生成，為了維持氣體交換，每分鐘通氣量通常上升。",
  options: [
    "A. 正確。肥胖病人血容量、心輸出量與心肌耗氧增加，合併高血壓、睡眠呼吸中止或冠心病時，麻醉中缺血風險更高。",
    "B. 錯誤。肥胖會增加代謝需求與二氧化碳產生，每分鐘通氣量常需增加；同時功能餘氣量下降，誘導後容易快速去飽和。",
    "C. 正確。肥胖與胃食道逆流、胃排空延遲及腹壓升高相關，麻醉誘導時要留意誤吸風險。",
    "D. 正確。短頸、頸圍增加、舌咽軟組織多與睡眠呼吸中止，使面罩通氣與插管困難機率上升。"
  ],
  core: "肥胖麻醉的呼吸重點是耗氧增加、每分鐘通氣量需求上升、FRC 下降與去飽和快。看到「通氣量不變」要特別警覺。",
  key_point: "肥胖病人每分鐘通氣量與耗氧量通常增加，FRC 下降使麻醉誘導後更易缺氧。",
  flashcard_front: "肥胖麻醉 / 呼吸生理 / FRC",
  flashcard_back: "肥胖會增加耗氧與 CO2 生成，通氣需求上升；FRC 下降導致誘導後去飽和更快。",
});

add(7, {
  stem: "糖尿病患麻醉考量的錯誤點在血糖控制目標。手術壓力確實會升高血糖，但 250 mg/dL 不是理想控制目標，過高血糖會增加感染、滲透性利尿與電解質問題。",
  options: [
    "A. 正確。糖尿病腎病變、神經病變與冠心病可能在症狀不明顯時已存在，術前評估不能只靠病人主訴。",
    "B. 正確。自主神經病變可造成無痛性心肌缺血或梗塞、姿態性低血壓，也常與高血壓及心血管風險並存。",
    "C. 錯誤。壓力性高血糖不是放任高血糖的理由；圍手術期通常以約 140-180 mg/dL 為常用目標範圍，250 mg/dL 偏高。",
    "D. 正確。禁食且沒有葡萄糖輸注時，手術當天胰島素常需暫停或調整以避免低血糖；若為第 1 型糖尿病，仍需個別保留基礎胰島素。"
  ],
  core: "糖尿病麻醉要同時防低血糖與高血糖併發症；壓力反應會升糖，但不代表 250 mg/dL 可以當作合格控制。胰島素處置需看禁食、葡萄糖輸注與糖尿病型態。",
  key_point: "糖尿病圍手術期血糖不應放任到約 250 mg/dL；常用控制目標約 140-180 mg/dL，胰島素需依禁食與輸液調整。",
  flashcard_front: "糖尿病麻醉 / 圍手術期血糖",
  flashcard_back: "手術壓力會升糖，但 250 mg/dL 偏高；圍手術期常抓 140-180 mg/dL，並依禁食與葡萄糖輸注調整胰島素。",
});

add(8, {
  stem: "止痛藥物的關鍵辨識，是肌肉鬆弛不等於止痛。神經肌肉阻斷劑只能造成骨骼肌鬆弛與不動，沒有止痛、鎮靜或失憶作用，不能拿來當止痛治療。",
  options: [
    "A. 正確。類鴉片藥物可用於術後急性疼痛，也可在癌症疼痛或特定慢性疼痛情境中使用。",
    "B. 正確。類固醇可透過抗發炎、減少神經根水腫或腫瘤周邊水腫，作為某些疼痛治療的輔助藥。",
    "C. 錯誤。神經肌肉阻斷劑阻斷神經肌肉接合處傳導，只讓病人不能動；清醒者仍會感到疼痛與焦慮。",
    "D. 正確。Gabapentin、pregabalin、carbamazepine 等抗癲癇藥常用於神經病變疼痛。"
  ],
  core: "鎮痛、鎮靜、失憶與肌肉鬆弛是不同藥理效果。肌肉鬆弛劑不能取代止痛藥或麻醉深度。",
  key_point: "神經肌肉阻斷劑沒有止痛或鎮靜作用，只造成肌肉麻痺，不能單獨作為止痛治療。",
  flashcard_front: "止痛藥物 / 神經肌肉阻斷劑",
  flashcard_back: "肌肉鬆弛不等於止痛；neuromuscular blocker 只阻斷運動，病人仍可能有疼痛與意識。",
});

add(9, {
  stem: "急性肝衰竭重症照護的錯誤敘述，是把高血鈉當成換肝禁忌。急性肝衰竭最怕腦水腫與顱內壓上升；高正常到輕度高鈉常是控制腦水腫策略之一。",
  options: [
    "A. 正確。歐美急性肝衰竭常見原因之一是 acetaminophen 中毒，需早期辨識並給予 N-acetylcysteine 等處置。",
    "B. 大致正確但需看情境。急性肝衰竭感染風險高，早期文獻支持某些預防性抗菌策略可降低感染；現代照護更強調監測培養與有感染或高風險時及早治療。",
    "C. 正確。腦水腫與顱內壓升高會造成腦疝，是急性肝衰竭死亡與預後不良的重要指標。",
    "D. 錯誤。血鈉維持在約 145-155 mmol/L 常用於降低腦水腫風險；單純高血鈉超過 150 mmol/L 不是肝移植禁忌。"
  ],
  core: "急性肝衰竭照護的考點是腦水腫、感染監測與移植評估。高正常或輕度高鈉可作為顱內壓管理工具，不能誤當換肝禁忌。",
  key_point: "急性肝衰竭可用高正常至輕度高鈉策略降低腦水腫風險；高血鈉本身不是肝移植禁忌。",
  flashcard_front: "急性肝衰竭 / 腦水腫 / 高血鈉",
  flashcard_back: "ALF 的腦水腫可用高張鹽水維持血鈉約 145-155 mmol/L；這是顱內壓管理策略，不是換肝禁忌。",
  manual_review_notes: ["B 選項關於預防性抗生素的現代建議較保守，已在詳解中保留考題語境並加註情境差異。"],
});

add(10, {
  stem: "周邊潰瘍性角膜炎常反映周邊角膜免疫性發炎與血管炎，較常連到 RA、SLE、GPA 等系統性免疫病。多發性硬化症的典型眼部表現是視神經炎，和 PUK 的關聯較弱。",
  options: [
    "A. 錯誤。類風濕性關節炎是 PUK 的重要系統性相關疾病，可因免疫複合物與血管炎造成周邊角膜溶解。",
    "B. 錯誤。SLE 可有血管炎與免疫性眼表病變，雖不如 RA 典型，仍可能與 PUK 相關。",
    "C. 錯誤。韋格納肉芽腫即肉芽腫併多血管炎，會造成壞死性鞏膜炎與 PUK，是高風險關聯疾病。",
    "D. 正確。多發性硬化症典型眼部問題是視神經炎，不是周邊角膜潰瘍性溶解，因此較不易併發 PUK。"
  ],
  core: "PUK 要聯想到系統性血管炎與結締組織病，尤其 RA 與 GPA。MS 的高頻眼科考點是 optic neuritis，不是 PUK。",
  key_point: "周邊潰瘍性角膜炎常與 RA、SLE、GPA 等免疫血管炎相關；多發性硬化症較典型是視神經炎。",
  flashcard_front: "PUK / 系統性免疫疾病 / MS",
  flashcard_back: "PUK 連到 RA、SLE、GPA；MS 主要連到 optic neuritis，所以較不易併發 PUK。",
});

add(11, {
  stem: "砂眼最具診斷意義的病徵，是輪部濾泡與癒合後留下的 Herbert pits。砂眼由 Chlamydia trachomatis 反覆感染造成結膜濾泡與瘢痕，這組病徵比一般結膜刺激更具特異性。",
  options: [
    "A. 正確。Limbal follicles 與 Herbert pits 是砂眼的代表性病徵，尤其 Herbert pits 可視為過去輪部濾泡留下的凹陷瘢痕。",
    "B. 錯誤。巨大乳頭較常見於春季角結膜炎、過敏性結膜炎或隱形眼鏡相關反應，不是砂眼最具診斷性的病徵。",
    "C. 錯誤。Horner-Trantas dots 是春季角結膜炎的角膜緣嗜酸性球堆積，不是砂眼的典型診斷標誌。",
    "D. 錯誤。結膜結石是慢性結膜炎或老化可見的非特異性沉積，診斷砂眼的特異性不足。"
  ],
  core: "砂眼的高鑑別病徵是輪部濾泡與 Herbert pits；巨型乳頭、Horner-Trantas dots 和結膜結石都指向其他眼表疾病或非特異變化。",
  key_point: "砂眼最具診斷意義的病徵是輪部濾泡與 Herbert pits。",
  flashcard_front: "砂眼 trachoma / Herbert pits",
  flashcard_back: "Trachoma 由反覆披衣菌感染造成；limbal follicles 與 Herbert pits 是最具診斷意義的病徵。",
});

add(13, {
  stem: "急性隅角閉鎖性青光眼較不可能立即看到視神經盤凹陷擴大。急性發作的重點是眼壓急升造成疼痛、紅眼、角膜水腫與半散大固定瞳孔；視神經盤凹陷擴大屬慢性青光眼性視神經病變。",
  options: [
    "A. 錯誤。結膜與上鞏膜充血是急性眼壓升高時常見的紅眼表現。",
    "B. 錯誤。眼壓急升會讓角膜內皮幫浦失衡，造成角膜霧狀水腫與視力下降。",
    "C. 錯誤。虹膜括約肌缺血可造成半放大、反應差的瞳孔，是急性隅角閉鎖典型體徵。",
    "D. 正確。視神經盤凹陷擴大通常需要較長時間的青光眼性視神經損傷，急性發作當下較不可能是主要可見表現。"
  ],
  core: "急性 angle-closure 要記紅、痛、霧、吐、眼壓高、角膜水腫與 mid-dilated pupil。Cup/disc ratio 擴大偏向慢性視神經損傷。",
  key_point: "急性隅角閉鎖以角膜水腫、結膜充血與半散大瞳孔為主；視神經盤凹陷擴大是慢性青光眼表現。",
  flashcard_front: "急性隅角閉鎖 / 慢性青光眼凹陷",
  flashcard_back: "急性發作常見紅眼、角膜水腫、半散大瞳孔；C/D ratio 擴大多屬慢性青光眼性視神經病變。",
});

add(16, {
  stem: "本態性眼瞼痙攣的錯誤敘述，是說大多數為單眼發作。Essential blepharospasm 是局部肌張力不全，多為雙眼、對稱或近似對稱發作。",
  options: [
    "A. 錯誤。多數病人是雙側眼輪匝肌不自主收縮；單眼抽動較要考慮 hemifacial spasm、局部刺激或其他病因。",
    "B. 正確。此病好發於中老年女性，常因畏光、眨眼增加或功能性閉眼影響生活。",
    "C. 正確。乾眼、眼表刺激與畏光都可讓眨眼增加，臨床上需要和乾眼症等眼表疾病鑑別。",
    "D. 正確。局部注射 botulinum toxin 可抑制眼輪匝肌過度收縮，是常用且有效的症狀治療。"
  ],
  core: "Essential blepharospasm 的考點是中老年女性、雙側眼輪匝肌痙攣、需排除眼表刺激，治療首選肉毒桿菌素注射。",
  key_point: "本態性眼瞼痙攣多為雙側發作，好發中老年女性，常用肉毒桿菌素改善症狀。",
  flashcard_front: "Essential blepharospasm / 雙側 / Botox",
  flashcard_back: "本態性眼瞼痙攣多為雙側眼輪匝肌痙攣；單眼為主時要另想 hemifacial spasm，治療常用 botulinum toxin。",
});

add(17, {
  stem: "眼底照片的重點是判斷視網膜剝離型態。最可能是裂孔型視網膜剝離，關鍵是視網膜裂孔讓液化玻璃體進入感覺神經視網膜下方，造成隆起剝離。",
  options: [
    "A. 正確。Rhegmatogenous retinal detachment 由視網膜裂孔或裂隙引起，是臨床最常見的視網膜剝離型態。",
    "B. 錯誤。牽引型剝離多由糖尿病增殖性視網膜病變等纖維血管膜拉扯造成，影像常呈牽拉性、帳篷狀改變，不以裂孔為主。",
    "C. 錯誤。出血型剝離不是常規分類的典型答案；若有大量出血，診斷重點會放在出血來源與脈絡膜或視網膜下積血。",
    "D. 錯誤。滲漏型剝離是血管或脈絡膜病變造成液體滲出，通常沒有視網膜裂孔，積液可隨姿勢改變。"
  ],
  core: "視網膜剝離常分裂孔型、牽引型與滲漏型。裂孔型的核心機轉是液化玻璃體經裂孔進入視網膜下腔。",
  key_point: "裂孔型視網膜剝離由視網膜裂孔讓液化玻璃體進入視網膜下腔造成，是常見剝離型態。",
  flashcard_front: "視網膜剝離 / 裂孔型 RRD",
  flashcard_back: "RRD 的關鍵是 retinal break；牽引型靠膜牽拉，滲漏型靠液體滲出且無裂孔。",
});

add(18, {
  stem: "承上題已是視網膜剝離，處置要讓視網膜復位並封閉裂孔。單純在門診做雷射光凝只適合尚未剝離或很局限的裂孔，對已剝離視網膜通常不夠。",
  options: [
    "A. 適當。Cryopexy 可用來在裂孔周圍造成脈絡膜視網膜沾黏，常作為手術封孔的一部分。",
    "B. 適當。Scleral buckling 由外部頂住裂孔區域，減少玻璃體牽拉，是裂孔型視網膜剝離的手術方式之一。",
    "C. 較不適當。雷射光凝需要視網膜貼近色素上皮才能形成有效沾黏；已發生明顯剝離時，門診雷射不能單獨完成復位。",
    "D. 適當。Vitrectomy 可移除牽拉玻璃體、處理裂孔並搭配氣體或矽油填塞，常用於複雜或後段裂孔型剝離。"
  ],
  core: "已剝離的視網膜要先復位，再封閉裂孔。雷射常用於裂孔預防或術中輔助，不是明顯剝離後的單獨門診處置。",
  key_point: "視網膜已剝離時，單純門診雷射光凝不足；常需鞏膜扣環、冷凍固定或玻璃體切除等復位手術。",
  flashcard_front: "裂孔型視網膜剝離 / 處置",
  flashcard_back: "Retinal detachment 要復位加封孔；門診雷射適合未剝離裂孔，明顯剝離須考慮 buckle、cryopexy 或 vitrectomy。",
});

add(19, {
  stem: "前庭神經下分支傳入的代表構造是後半規管與球囊，這是內耳平衡解剖常考的分支對照。上半規管、側半規管與橢圓囊多由上分支負責，不能把三個半規管全歸到同一分支。",
  options: [
    "A. 錯誤。上半規管屬前庭神經上分支支配，常和側半規管、橢圓囊歸在同一組。",
    "B. 錯誤。側半規管由前庭神經上分支傳入，不是下分支的代表構造。",
    "C. 正確。後半規管由前庭神經下分支支配，是本題要選的構造。",
    "D. 錯誤。橢圓囊主要由前庭神經上分支支配；球囊才是下分支的耳石器代表。"
  ],
  core: "前庭神經分支可記成上分支管上、側與橢圓囊；下分支管後半規管與球囊。BPPV、前庭神經炎與前庭誘發肌電位題，都可能用這組解剖來定位病灶。",
  key_point: "前庭神經下分支支配後半規管與球囊；上分支支配上、側半規管與橢圓囊。",
  flashcard_front: "前庭神經上/下分支 / 半規管支配",
  flashcard_back: "Inferior vestibular nerve：posterior semicircular canal + saccule；superior division：superior/lateral canals + utricle。",
});

add(20, {
  stem: "Schwartze 徵象是鼓膜後方透出粉紅色或紅暈，代表耳硬化症活動期耳囊血管增生。耳鏡看見這個徵象時，最典型連到耳硬化症。",
  options: [
    "A. 錯誤。聽神經瘤是前庭神經鞘瘤，典型表現為單側感音神經性聽損與耳鳴，耳鏡通常正常。",
    "B. 錯誤。膽固醇肉芽腫可在中耳或岩尖造成藍黑色鼓膜或導音障礙，但不是 Schwartze 徵象的代表疾病。",
    "C. 錯誤。膽脂瘤耳鏡常見上鼓室或鼓膜鬆弛部凹陷袋、白色角化物堆積與惡臭耳漏，不是粉紅岬角紅暈。",
    "D. 正確。耳硬化症侵犯鐙骨足板時造成漸進性導音性聽損，活動期可見 Schwartze sign。"
  ],
  core: "Schwartze sign 看到粉紅色 promontory 要連到 otosclerosis。聽神經瘤通常耳鏡正常；膽脂瘤則看凹陷袋與角化物。",
  key_point: "Schwartze 徵象是耳硬化症活動期可見的鼓膜後粉紅色紅暈。",
  flashcard_front: "Schwartze sign / otosclerosis",
  flashcard_back: "耳硬化症可見鼓膜後粉紅色 promontory flush；膽脂瘤看白色角化物與凹陷袋，聽神經瘤耳鏡多正常。",
});

add(21, {
  stem: "眶上裂題的核心是眼窩入口的孔裂解剖。眶上裂連接中顱窩與眼窩，通過 III、IV、V1、VI 與眼上靜脈；三叉神經上頜支 V2 經圓孔離開顱腔，不走眶上裂。",
  options: [
    "A. 錯誤。滑車神經 CN IV 經眶上裂進入眼窩，支配上斜肌。",
    "B. 錯誤。外展神經 CN VI 經眶上裂進入眼窩，支配外直肌。",
    "C. 錯誤。眼上靜脈經眶上裂與海綿竇相通，是眼窩靜脈回流的重要通道。",
    "D. 正確。三叉神經上頜支 V2 經圓孔到翼腭窩，不經眶上裂；經眶上裂的是眼神經 V1。"
  ],
  core: "眶上裂記 III、IV、V1、VI 與眼上靜脈；圓孔是 V2，卵圓孔是 V3。作答時不要只背三叉神經三支，要把每一支對應到眼窩或顱底孔道，問不經眶上裂時常考 V2。",
  key_point: "V2 上頜神經走圓孔，不走眶上裂；眶上裂通過 CN III、IV、V1、VI 與眼上靜脈。",
  flashcard_front: "Superior orbital fissure / V2",
  flashcard_back: "SOF：III、IV、V1、VI、superior ophthalmic vein；foramen rotundum：V2。",
});

add(23, {
  stem: "發燒、咽喉痛、吞嚥困難與呼吸急促，加上咽喉內視鏡箭頭指向腫脹會厭，最符合急性會厭炎。這是可能迅速造成上呼吸道阻塞的急症。",
  options: [
    "A. 錯誤。箭頭所指應是發炎腫脹的會厭，不是甲狀軟骨；甲狀軟骨是喉部軟骨外框，非內視鏡腫脹黏膜結構。",
    "B. 錯誤。急性會厭炎常見病原為細菌，包含 Haemophilus influenzae、Streptococcus 等；不能概括成病毒感染為主。",
    "C. 正確。會厭水腫位於聲門上方，可在短時間內造成急性呼吸道阻塞，評估與保護 airway 是優先重點。",
    "D. 錯誤。側頸 X 光急性會厭炎典型為拇指徵象；尖塔徵象較典型見於哮吼的聲門下狹窄。"
  ],
  core: "急性會厭炎的考點是高熱、吞嚥痛、流口水或呼吸困難，以及 airway 風險。影像記 thumb sign；steeple sign 是 croup。",
  key_point: "急性會厭炎可快速造成上呼吸道阻塞；側頸 X 光為拇指徵象，不是尖塔徵象。",
  flashcard_front: "急性會厭炎 / airway / thumb sign",
  flashcard_back: "Epiglottitis 是 airway emergency；病原多細菌，側頸片 thumb sign。Steeple sign 屬 croup。",
});

add(24, {
  stem: "聲帶麻痺的正確敘述，是單側麻痺以左側較常見。聲帶麻痺多源自喉返神經病變，左喉返神經繞主動脈弓、路徑較長，因此較容易受胸頸部病變影響。",
  options: [
    "A. 錯誤。主要受損神經通常是喉返神經；上喉神經外支受損較影響環甲肌與高音控制，不是聲帶麻痺主因。",
    "B. 錯誤。呼吸困難較常見於雙側聲帶麻痺，因兩側聲帶停在近中線位置會讓聲門狹窄。",
    "C. 正確。左喉返神經行程較長，胸腔、縱膈與甲狀腺相關病變較易影響它，所以單側聲帶麻痺左側較多。",
    "D. 錯誤。發聲障礙、沙啞與嗆咳較常見於單側聲帶麻痺；雙側麻痺反而以呼吸道狹窄為大問題。"
  ],
  core: "聲帶麻痺要分單側與雙側：單側多沙啞、嗆咳，左側常見；雙側多呼吸困難。主神經是 recurrent laryngeal nerve。",
  key_point: "單側聲帶麻痺以左側較常見，主因多為喉返神經受損；雙側麻痺較容易呼吸困難。",
  flashcard_front: "聲帶麻痺 / 左喉返神經 / 單側雙側",
  flashcard_back: "Unilateral vocal fold paralysis：左側多、沙啞多；bilateral：airway obstruction 多。主因是 recurrent laryngeal nerve。",
});

add(25, {
  stem: "甲狀舌管囊腫的錯誤敘述，是把最常見惡性型態寫成鱗狀上皮癌。此囊腫的惡性化很少見，但一旦發生，最常見組織型是甲狀腺乳突癌。",
  options: [
    "A. 正確。甲狀舌管囊腫通常位於頸部中線，會隨吞嚥或伸舌上下移動，是常見先天性頸部腫塊。",
    "B. 錯誤。惡性轉化率確實低，但最常見惡性型態是 papillary thyroid carcinoma；鱗狀上皮癌不是最常見。",
    "C. 正確。標準治療是 Sistrunk 手術，包含囊腫、管道與舌骨中央部位切除，以降低復發。",
    "D. 正確。先前感染會造成沾黏與殘留管道風險上升，術後復發機率較高。"
  ],
  core: "甲狀舌管囊腫記中線、隨吞嚥或伸舌移動、Sistrunk 手術。惡性化少見，但以乳突癌最常見。",
  key_point: "甲狀舌管囊腫惡性化最常見為乳突癌；標準手術是 Sistrunk。",
  flashcard_front: "甲狀舌管囊腫 / 惡性化 / Sistrunk",
  flashcard_back: "TGDC 是中線先天性頸部腫塊；惡性化少見且以 papillary thyroid carcinoma 最多，治療用 Sistrunk。",
});

add(27, {
  stem: "口腔黏膜變化中正確的是扁平苔蘚具有惡性轉化可能。扁平苔蘚是慢性免疫相關病灶，雖多為良性，但仍被視為有惡性轉化潛能的口腔病變。",
  options: [
    "A. 錯誤。口腔白斑是不能被其他疾病解釋的白色斑塊，常見病理為過度角化、棘層增生或上皮異生，不是以上皮萎縮為主。",
    "B. 錯誤。口腔紅斑雖較少見，但異生或癌化比例通常高於白斑；說白斑惡性變化可能性較高不對。",
    "C. 正確。口腔扁平苔蘚可呈網狀白紋或糜爛型變化，屬免疫媒介疾病，也有低度但確實存在的癌化風險。",
    "D. 錯誤。口腔黏膜下纖維化和檳榔等刺激相關，屬口腔潛在惡性病變，不能說不會惡性變化。"
  ],
  core: "口腔癌前病變要比較白斑、紅斑、扁平苔蘚與黏膜下纖維化。紅斑癌化風險高，黏膜下纖維化與扁平苔蘚也不能當作完全良性。",
  key_point: "口腔扁平苔蘚與黏膜下纖維化都有惡性轉化可能；紅斑癌化風險通常高於白斑。",
  flashcard_front: "口腔黏膜病變 / 惡性轉化",
  flashcard_back: "白斑不等於萎縮；紅斑惡變率高。Lichen planus 與 oral submucous fibrosis 都有惡性潛能。",
});

add(28, {
  stem: "嚴格全素孕婦最可能缺乏維生素 B12。維生素 B12 主要來自動物性食物，嚴格全素且未補充時最容易不足，孕期不足會影響造血與胎兒神經發育。",
  options: [
    "A. 錯誤。維生素 A 可由植物性 beta-carotene 轉換取得，均衡全素飲食不一定最先缺乏它。",
    "B. 正確。維生素 B12 主要存在於肉類、乳蛋與其他動物性食品，嚴格全素孕婦需靠強化食品或補充劑。",
    "C. 錯誤。維生素 C 在蔬果中豐富，通常不是全素飲食最具代表性的缺乏項目。",
    "D. 錯誤。維生素 K 可由深綠色蔬菜與腸道菌提供，並非嚴格全素孕婦最典型缺乏。"
  ],
  core: "看到 strict vegetarian 或 vegan 孕婦，優先想到 B12 補充。B12 不足可造成巨球性貧血，也會影響胎兒與嬰兒神經發育。",
  key_point: "嚴格全素孕婦最需注意維生素 B12 缺乏，應由強化食品或補充劑取得。",
  flashcard_front: "全素孕婦 / 維生素 B12",
  flashcard_back: "B12 主要來自動物性食物；strict vegan pregnancy 要主動補充，避免貧血與神經發育問題。",
});

add(29, {
  stem: "真空吸引助產的適當負壓約 0.6 kg/cm2。這個壓力足以讓吸杯附著胎頭，又避免過高負壓增加頭皮與顱內傷害。",
  options: [
    "A. 錯誤。0.2 kg/cm2 通常吸附力不足，容易滑脫，不能有效協助牽引。",
    "B. 正確。約 0.6 kg/cm2 是真空吸引助產常用的目標負壓範圍。",
    "C. 錯誤。1.0 kg/cm2 偏高，會增加頭皮血腫、帽狀腱膜下出血等風險。",
    "D. 錯誤。2.0 kg/cm2 明顯過高，安全性不適合產科真空吸引。"
  ],
  core: "真空吸引不是壓力越大越好；考試常抓約 0.6 kg/cm2。負壓過低易滑脫，過高會增加胎兒頭皮與出血併發症。",
  key_point: "真空吸引助產適當負壓約 0.6 kg/cm2。",
  flashcard_front: "真空吸引助產 / 負壓",
  flashcard_back: "Vacuum extraction 常用負壓約 0.6 kg/cm2；過低吸不住，過高增加胎兒頭皮與出血傷害。",
});

add(31, {
  stem: "母乳維生素題的官方答案為維生素 K。新生兒腸道菌尚未建立、胎盤運輸與母乳含量都有限，因此出生後常規給予維生素 K 預防出血。",
  options: [
    "A. 錯誤。維生素 A 雖受母親營養影響，但不是本題考新生兒常規預防注射的核心缺乏項目。",
    "B. 錯誤。母乳中維生素 D 也常不足，現代嬰兒照護會重視補充；但本題官方考點是維生素 K 與新生兒出血預防。",
    "C. 錯誤。維生素 E 不是母乳餵養後立即以常規注射預防出血的代表答案。",
    "D. 正確。母乳維生素 K 含量低，新生兒凝血因子活化需要維生素 K，因此出生後常規給予 vitamin K1。"
  ],
  core: "國考問母乳缺乏與新生兒出血，標準連結是 vitamin K。補充提醒：母乳維生素 D 也常不足，但與本題官方答案的出血預防考點不同。",
  key_point: "母乳維生素 K 含量低，新生兒出生後需補充 vitamin K1 以預防出血。",
  flashcard_front: "母乳 / 維生素 K / 新生兒出血",
  flashcard_back: "母乳 vitamin K 低，新生兒腸道菌少，出生後常規給 vitamin K1 預防 hemorrhagic disease of newborn。",
  manual_review_notes: ["B 選項維生素 D 在現代嬰兒營養也常被視為不足；本題依官方答案保留 vitamin K 考點。"],
});

add(32, {
  stem: "產科超音波雙十字之間若標在長骨兩端，最符合股骨長度 FL。FL 常和其他生長參數一起用於估算胎齡與胎兒體重。",
  options: [
    "A. 錯誤。BPD 是胎兒頭部兩側頂骨間的橫徑，影像切面會是頭顱橫切面，不是長條骨性結構。",
    "B. 錯誤。AC 是腹圍，需要在胎兒腹部橫切面沿腹壁量周徑，不是兩端點距離。",
    "C. 正確。FL 是測量股骨骨幹兩端的長度，超音波上常以兩個十字卡尺標示骨端。",
    "D. 錯誤。NT 是第一孕期胎兒頸後透明帶厚度，測量位置在頸背皮下，不是股骨長度。"
  ],
  core: "產科超音波生長參數要分清 BPD、AC、FL、NT。看到長骨兩端點距離，最直覺是 femur length。",
  key_point: "超音波以雙卡尺量長骨兩端通常是胎兒股骨長度 FL。",
  flashcard_front: "產科超音波 / FL / BPD AC NT",
  flashcard_back: "FL 量股骨長度；BPD 量頭顱橫徑，AC 量腹圍，NT 量第一孕期頸後透明帶。",
});

add(33, {
  stem: "年輕女性有附件區 7-8 公分腫塊、姿勢改變可影響疼痛，急性加劇並有噁心嘔吐，最符合卵巢腫瘤合併扭轉。扭轉會造成靜脈回流受阻、腫脹與缺血，腹腔鏡常見暗紫或發紺附件。",
  options: [
    "A. 正確。附件腫塊合併急性單側下腹痛、噁心嘔吐與壓痛，是 ovarian torsion 的典型組合。",
    "B. 錯誤。輸卵管外孕需有懷孕相關線索、停經與 hCG 陽性；題幹重點是大型卵巢附件腫塊與扭轉疼痛。",
    "C. 錯誤。急性盲腸炎可造成右下腹痛與反彈痛，但無法解釋右側附件鵝蛋大小腫塊與腹腔鏡卵巢扭轉外觀。",
    "D. 錯誤。子宮肌瘤紅色變性多見於妊娠期肌瘤疼痛，題幹子宮大小正常且病灶位於卵巢附件區。"
  ],
  core: "卵巢扭轉常考附件腫塊大於 5 cm、急性單側下腹痛、噁心嘔吐與壓痛。診斷懷疑高時要及早腹腔鏡處理以保留卵巢功能。",
  key_point: "附件區大腫塊合併急性單側下腹痛與噁心嘔吐，優先懷疑卵巢腫瘤扭轉。",
  flashcard_front: "卵巢扭轉 / 附件腫塊 / 急性腹痛",
  flashcard_back: "Ovarian torsion：大附件腫塊、單側急痛、噁心嘔吐，腹腔鏡可見發紺腫大扭轉卵巢。",
});

add(34, {
  stem: "年輕女性卵巢實質腫瘤內含骨頭與牙齒，典型是成熟囊性畸胎瘤，也就是 dermoid cyst。成熟畸胎瘤可由多胚層組織構成，臨床多為良性，但仍要留意扭轉與雙側病灶；常見考試數字約 10-15%。",
  options: [
    "A. 錯誤。小於 1% 低估成熟畸胎瘤雙側性，與常考比例不符。",
    "B. 錯誤。2-3% 仍偏低，不是成熟畸胎瘤的典型雙側發生率。",
    "C. 正確。成熟囊性畸胎瘤約 10-15% 可為雙側，這個比例足以讓手術與追蹤時需要檢查對側卵巢。",
    "D. 錯誤。50% 過高，較不像成熟畸胎瘤的實際雙側比例。"
  ],
  core: "卵巢腫瘤看到牙齒、骨頭、毛髮要想到 mature cystic teratoma。它是常見良性生殖細胞腫瘤，雙側率約 10-15%，比 1-3% 高，但遠不到 50%。",
  key_point: "成熟囊性畸胎瘤含外胚層組織如牙齒或骨頭，雙側發生率約 10-15%。",
  flashcard_front: "成熟囊性畸胎瘤 / 雙側率",
  flashcard_back: "Dermoid cyst 可含牙齒、骨頭、毛髮；雙側性約 10-15%。",
});

add(35, {
  stem: "連續多次第一孕期自然流產，夫妻染色體檢查若有異常，最典型是其中一方帶有平衡性染色體易位。帶因者本身表型可正常，但配子可能不平衡，導致胚胎早期流產。",
  options: [
    "A. 錯誤。Trisomy 18 胚胎多造成胎兒嚴重異常或流產，但活著的成人父母不會以完整 trisomy 18 作為常見帶因狀態。",
    "B. 正確。Balanced translocation 帶因者染色體總量不增不減，自己可正常；減數分裂後形成不平衡配子，造成反覆流產。",
    "C. 錯誤。Turner syndrome 患者常有性腺發育不全與不孕，不是夫妻一方表型正常且造成反覆流產的最常見染色體異常。",
    "D. 錯誤。Klinefelter syndrome 常見男性不孕與睪丸功能低下，不是反覆第一孕期流產夫妻染色體檢查最典型答案。"
  ],
  core: "習慣性流產若追到父母染色體，最常考平衡易位。關鍵是父母表型正常，但胚胎染色體不平衡而早期流產。",
  key_point: "反覆第一孕期流產的父母染色體異常最典型是 balanced translocation。",
  flashcard_front: "習慣性流產 / 夫妻染色體 / balanced translocation",
  flashcard_back: "Balanced translocation 帶因者可正常，但配子不平衡會造成胚胎染色體異常與反覆流產。",
});

add(36, {
  stem: "晚期上皮性卵巢癌標準第一線化療以 platinum 加 taxane 為核心，常用組合是 carboplatin 加 paclitaxel。題目其他組合不是現代標準一線。",
  options: [
    "A. 錯誤。Cisplatin + 5FU 不是晚期上皮性卵巢癌的一線標準組合，5FU 更常見於其他腸胃道或頭頸癌情境。",
    "B. 正確。Carboplatin + paclitaxel 是晚期上皮性卵巢癌常用的一線化療組合，療效與耐受性較符合標準。",
    "C. 錯誤。Cisplatin + cyclophosphamide 是較早期的鉑類組合，已被 taxane/platinum 組合取代。",
    "D. 錯誤。Carboplatin + cyclophosphamide 不如 carboplatin + paclitaxel 典型，不是目前首選一線答案。"
  ],
  core: "上皮性卵巢癌化療抓 platinum-taxane。國考看到 advanced epithelial ovarian cancer，一線先想 carboplatin + paclitaxel。",
  key_point: "晚期上皮性卵巢癌第一線化療常用 carboplatin + paclitaxel。",
  flashcard_front: "上皮性卵巢癌 / 一線化療",
  flashcard_back: "Advanced epithelial ovarian cancer first-line chemotherapy：carboplatin + paclitaxel。",
});

add(37, {
  stem: "Yolk sac tumor 是惡性卵巢生殖細胞腫瘤，好發年輕女性，對鉑類化療敏感。即使術中囊腫破裂，也應優先保留生育功能並術後化療，而不是立即做根除性切除。",
  options: [
    "A. 錯誤。卵黃囊瘤屬惡性腫瘤，術中破裂後不能等坐月子後再觀察，需安排完整分期與術後化療。",
    "B. 錯誤。骨盆腔放射線治療會傷害生育功能，也不是卵黃囊瘤的主要術後治療；化學治療才是關鍵。",
    "C. 正確。年輕病人可保留子宮與對側正常卵巢，術後給予含鉑聯合化療，兼顧治療與生育功能。",
    "D. 錯誤。卵巢生殖細胞癌多對化療敏感，預後並非一律差；不需因診斷就立即切除子宮與雙側附件。"
  ],
  core: "年輕女性惡性卵巢生殖細胞腫瘤常可做 fertility-sparing surgery，再給術後化療。Yolk sac tumor 不靠放療，也不必常規切除子宮與對側正常卵巢。",
  key_point: "卵巢卵黃囊瘤可保留生育功能手術，術後給予含鉑聯合化療。",
  flashcard_front: "Yolk sac tumor / fertility-sparing / chemo",
  flashcard_back: "惡性卵巢生殖細胞腫瘤年輕病人常保留子宮與對側卵巢；yolk sac tumor 術後需含鉑化療。",
});

add(38, {
  stem: "病人已在外院開腹，見高度懷疑晚期卵巢癌與 omental cake，但無橫膈下或肝臟轉移且生命徵象穩定。此時處置重點是轉至可處理的醫院後完成主要減積手術，而不是只先做一次化療或放化療。",
  options: [
    "A. 正確。晚期卵巢癌若可切除，主要減積手術目標是盡量達到無肉眼殘餘病灶；此例已開腹未處理且有傷口問題，應立即接手手術。",
    "B. 錯誤。先給一次化療不能處理已開腹後的診斷、分期、減積與傷口問題；neoadjuvant chemotherapy 需在評估不可切除或不適合手術時才考慮。",
    "C. 錯誤。CT 可用於術前評估，但題幹已描述腹腔擴散範圍、無上腹明顯轉移且剛轉院，先急做 CT 會延誤可行的減積處理。",
    "D. 錯誤。同步化放療不是上皮性卵巢癌標準初始策略，放射線也不是 omental cake 晚期卵巢癌的主要治療。"
  ],
  core: "晚期卵巢癌治療核心是由有經驗團隊做 cytoreductive surgery，目標無肉眼殘餘，再接續系統性治療。只有在不可切除或手術風險過高時才偏向先化療。",
  key_point: "可切除晚期卵巢癌以主要減積手術為核心，目標是最大程度移除肉眼病灶。",
  flashcard_front: "晚期卵巢癌 / debulking surgery",
  flashcard_back: "Advanced ovarian cancer 若可切除，優先做 cytoreductive/debulking surgery，之後接續系統性化療。",
});

add(39, {
  stem: "邊緣惡性卵巢腫瘤的診斷界線，是沒有破壞性基質侵犯。Borderline tumor 可有上皮增生、乳突結構、核異型與有絲分裂增加，但一旦侵犯基質就屬浸潤性癌。",
  options: [
    "A. 錯誤。乳突狀構造與偽多層反映上皮增生，是邊緣性腫瘤可見特徵。",
    "B. 錯誤。細胞核異常可出現在 borderline tumor，表示比良性囊腺瘤更活躍。",
    "C. 錯誤。有絲分裂增加也是邊緣性腫瘤相對良性腫瘤更活躍的表現。",
    "D. 正確。可見基質侵犯代表已進入浸潤性癌診斷範圍，不符合 borderline tumor 的基本定義。"
  ],
  core: "卵巢 borderline tumor 的分界點是沒有 stromal invasion。只要看到破壞性基質侵犯，就不能再稱為單純邊緣性腫瘤。",
  key_point: "邊緣性卵巢腫瘤可有異型與分裂增加，但不能有基質侵犯。",
  flashcard_front: "Borderline ovarian tumor / stromal invasion",
  flashcard_back: "Borderline tumor = epithelial proliferation/atypia without destructive stromal invasion；有 invasion 就是 carcinoma。",
});

add(40, {
  stem: "懷孕 10 週胎兒發育最不符合的是 CRL 7 公分。10 週胎兒 CRL 大約 3-4 公分，7 公分較接近更晚週數。",
  options: [
    "A. 符合。10 週左右四肢與主要關節已形成，手肘可彎曲屬合理描述。",
    "B. 不符合。懷孕 10 週 CRL 約 3-4 公分；7 公分偏大，較接近 13 週左右的大小。",
    "C. 符合。橫膈膜在胚胎早期已逐步形成，10 週時說已形成大致合理。",
    "D. 符合。心臟基本分隔與主要結構在胚胎期已完成，10 週時心臟結構已可辨識。"
  ],
  core: "胎兒週數題要把 10 週和 CRL 數字連起來：10 週約 3-4 cm，12-13 週才接近 6-7 cm。器官形成多在第一孕期早段完成。",
  key_point: "懷孕 10 週 CRL 約 3-4 cm，7 cm 對 10 週而言過大。",
  flashcard_front: "懷孕 10 週 / CRL / 胎兒發育",
  flashcard_back: "10 週 CRL 約 3-4 cm；CRL 7 cm 較像 13 週。四肢關節、橫膈膜與心臟基本結構已形成。",
});

add(41, {
  stem: "圖示若為產婦雙腿高度屈曲貼近腹部，用來處理肩難產，最符合 McRoberts maneuver。此法可使薦骨變平、旋轉恥骨聯合，幫助前肩脫困。",
  options: [
    "A. 錯誤。Rubin maneuver 是以手伸入陰道對胎兒肩部施壓，使肩帶內收或旋轉，不是單純屈曲產婦大腿。",
    "B. 正確。McRoberts maneuver 是肩難產第一線手法之一，將產婦髖關節過度屈曲，使大腿貼近腹部。",
    "C. 錯誤。Fundal pressure 會把胎兒肩部壓得更卡，處理肩難產時通常避免使用。",
    "D. 錯誤。Woods corkscrew maneuver 是內旋胎兒肩膀的手法，不是圖中腿部姿勢調整。"
  ],
  core: "肩難產先做 McRoberts 加恥骨上壓，避免 fundal pressure。內轉手法如 Rubin、Woods 是下一層處置。",
  key_point: "McRoberts maneuver 是將產婦大腿屈曲貼腹以處理肩難產的第一線手法。",
  flashcard_front: "肩難產 / McRoberts maneuver",
  flashcard_back: "McRoberts = maternal hips hyperflexed onto abdomen；肩難產避免 fundal pressure，可加 suprapubic pressure。",
});

add(42, {
  stem: "會陰裂傷分級取決於傷及深度，臨床上和修補方式、抗生素與後續追蹤都有關。第四度裂傷最嚴重，已穿過肛門括約肌複合體並延伸到直腸黏膜。",
  options: [
    "A. 錯誤。只到陰道黏膜或會陰皮膚屬第一度裂傷，深度最淺。",
    "B. 錯誤。傷及外肛門括約肌屬第三度裂傷的一部分，尚未達第四度定義。",
    "C. 錯誤。傷及內肛門括約肌也仍在第三度裂傷範圍；第四度需再延伸到直腸黏膜。",
    "D. 正確。第四度會陰裂傷是肛門括約肌受損且累及直腸黏膜，等於產道與直腸腔之間的黏膜屏障也被破壞。"
  ],
  core: "會陰裂傷分級：一度皮膚/黏膜，二度會陰肌肉，三度肛門括約肌，四度直腸黏膜。三度和四度的分水嶺不是有沒有括約肌受傷，而是有沒有傷到 rectal mucosa。",
  key_point: "第四度會陰裂傷代表傷及肛門括約肌並延伸到直腸黏膜。",
  flashcard_front: "會陰裂傷分級 / 第四度",
  flashcard_back: "1 度皮膚黏膜，2 度會陰肌肉，3 度肛門括約肌，4 度直腸黏膜。",
});

add(43, {
  stem: "孕婦只超過預產期 2 天，胎心監測 reactive、無規則宮縮、MVP 3.6 cm 屬可接受羊水量，破水陰性且胎兒估重未達明確剖腹指徵。最適當是門診追蹤觀察。",
  options: [
    "A. 正確。胎兒監測與羊水量目前 reassuring，尚未達 42 週或其他立即生產指徵，可安排產檢追蹤與警示症狀回診。",
    "B. 錯誤。住院引產可在更晚週數、胎兒監測異常、羊水過少或母胎適應症時考慮；本題目前資料不足以支持立即引產。",
    "C. 錯誤。剖腹產需有產科適應症，例如胎兒窘迫、產程問題、胎位異常或估重極高；題幹沒有這些條件。",
    "D. 錯誤。破水測試陰性、無感染徵象，沒有給抗生素的理由。"
  ],
  core: "過預產期少數天不等於必須立即引產或剖腹。NST reactive 且羊水垂直最大池大於 2 cm 時，可密切追蹤。",
  key_point: "預產期後 2 天且 NST reactive、羊水量可接受時，最適當為門診追蹤觀察。",
  flashcard_front: "預產期後追蹤 / NST reactive / MVP",
  flashcard_back: "Post-date 但未 post-term，NST reactive、MVP 3.6 cm、未破水，可先門診密切追蹤。",
});

add(44, {
  stem: "孕期不建議接種的預防性疫苗是水痘疫苗。水痘疫苗屬活性減毒疫苗，孕期禁用；流感不活化疫苗、破傷風/Tdap 與暴露後狂犬病疫苗則可依適應症施打。",
  options: [
    "A. 錯誤。孕婦建議接種不活化流感疫苗，以降低母體重症與新生兒感染風險；禁用的是鼻噴活性減毒流感疫苗。",
    "B. 錯誤。狂犬病暴露後風險極高，孕期不是接種禁忌，需依暴露風險處理。",
    "C. 正確。水痘疫苗是活性減毒疫苗，懷孕期間不建議施打，通常應延至產後。",
    "D. 錯誤。破傷風類毒素或 Tdap 可在孕期依時程或傷口處置需要施打，並非孕期禁忌。"
  ],
  core: "孕期疫苗先分活性減毒與不活化/類毒素。水痘與 MMR 屬活性減毒，孕期避免；不活化流感與 Tdap 是常見建議疫苗。",
  key_point: "孕期禁用活性減毒疫苗如水痘；不活化流感、Tdap/破傷風與必要時狂犬病疫苗可接種。",
  flashcard_front: "孕期疫苗 / 活性減毒 / varicella",
  flashcard_back: "Varicella vaccine 是 live attenuated，孕期禁用；IIV influenza 與 Tdap 可於孕期施打。",
});

add(45, {
  stem: "Cotton swab test 用來評估用力時尿道角度是否過度改變。考題給的準則是靜止尿道角度大於 30 度或最大用力角度大於 30 度，因此是 or 關係。",
  options: [
    "A. 正確。只要 resting urethral angle > 30 degrees 或 maximal straining angle > 30 degrees，即符合題目採用的尿道過度移動準則。",
    "B. 錯誤。改成 and 會要求兩項都超過 30 度，條件比題目準則更嚴格。",
    "C. 錯誤。把最大用力角度門檻改成 45 度，與本題採用的 30 度界限不符。",
    "D. 錯誤。同時使用 and 與 45 度門檻，既改變邏輯也提高界限。"
  ],
  core: "尿道過度移動的 Q-tip test 題要看清楚角度門檻與 and/or。此題官方採 30 度，且為 or。",
  key_point: "Cotton swab test 診斷尿道過度移動採 resting angle >30 度或 maximal straining angle >30 度。",
  flashcard_front: "Cotton swab test / urethral hypermobility",
  flashcard_back: "本題準則：resting urethral angle >30 或 maximal straining angle >30；注意是 or，不是 and。",
});

add(46, {
  stem: "HPV 型別的錯誤敘述，是把 6、11 型歸為高危險型。HPV 6、11 是低危險型，典型造成尖圭濕疣；高危險型與子宮頸癌最相關的是 16、18，且 E6/E7 具有致癌作用。",
  options: [
    "A. 正確。Koilocytosis 是 HPV 感染的典型病理變化，可見核周空暈與核異型。",
    "B. 錯誤。第 6 與 11 型屬低危險型，常造成生殖器疣；高危險型主要是 16、18 等。",
    "C. 正確。HPV 16 是子宮頸癌與高階癌前病變最常見且最重要的型別之一。",
    "D. 正確。E6 會促進 p53 降解，E7 會抑制 Rb 路徑，兩者是高危險 HPV 致癌關鍵蛋白。"
  ],
  core: "HPV 型別要分低危險 6/11 與高危險 16/18。病理看到 koilocytosis，分子機轉看 E6-p53、E7-Rb。",
  key_point: "HPV 6/11 是低危險型；HPV 16/18 是高危險型，E6/E7 為致癌蛋白。",
  flashcard_front: "HPV 型別 / koilocytosis / E6 E7",
  flashcard_back: "6/11 低危險造成疣；16/18 高危險造成 CIN/cervical cancer。E6 抑制 p53，E7 抑制 Rb。",
});

add(47, {
  stem: "現代外陰癌處置不包括對所有病人常規做廣泛根除手術。治療趨勢是個別化與縮小不必要手術範圍，避免所有病人常規接受外陰根除加雙側腹股溝淋巴結廓清。",
  options: [
    "A. 包括。外陰癌治療需依腫瘤大小、位置、深度、淋巴結風險與病人狀況個別化。",
    "B. 包括。骨盆腔淋巴結清除不是所有病人常規需要；外陰癌主要淋巴引流先到腹股溝股部淋巴結。",
    "C. 包括。多顆腹股溝淋巴結陽性代表局部復發與死亡風險高，術後放射線可降低 groin recurrence。",
    "D. 不包括。把所有病人都做根除性外陰切除與雙側腹股溝淋巴結廓清是過度治療，會增加傷口、淋巴水腫與性功能併發症。"
  ],
  core: "外陰癌不是一律大範圍根除手術；處置強調個別化、適當淋巴結評估與術後放療選擇。看到 routine radical surgery for all 要排除。",
  key_point: "外陰癌處置強調個別化，不應對所有病人常規執行根除性外陰切除與雙側腹股溝淋巴結廓清。",
  flashcard_front: "外陰癌 / 個別化治療 / 淋巴結",
  flashcard_back: "Vulvar cancer 現代處置避免一律 radical vulvectomy + bilateral groin dissection；依風險個別化。",
});

add(48, {
  stem: "妊娠滋養細胞腫瘤中，對化療反應最差的是 PSTT。PSTT 來自中間型滋養細胞，hCG 常較低，對傳統化療敏感度低於絨毛癌與侵襲性葡萄胎，治療常以手術為主。",
  options: [
    "A. 錯誤。絨毛膜癌雖可高度惡性與轉移，但多數對化療相當敏感。",
    "B. 正確。Placental-site trophoblastic tumor 對化療反應較差，若局限於子宮常以子宮切除為主要治療。",
    "C. 錯誤。侵襲性 GTN 通常對 methotrexate、actinomycin D 或多藥化療有良好反應。",
    "D. 錯誤。轉移性 GTN 仍常以風險分層後化療為主，反應一般優於 PSTT。"
  ],
  core: "GTN 多數化療敏感，但 PSTT 是例外，因生物行為與中間型滋養細胞來源而較不敏感。考最差反應時選 PSTT。",
  key_point: "胎盤處滋養細胞腫瘤 PSTT 對化療反應較差，常以手術治療為主。",
  flashcard_front: "GTN / PSTT / 化療反應",
  flashcard_back: "多數 GTN chemo-sensitive；PSTT 對化療較差，局限病灶常以 hysterectomy 為主。",
});

add(49, {
  stem: "惡性卵巢生殖細胞腫瘤中，dysgerminoma 最可能雙側發生。它是此類腫瘤中雙側率最高者，常考比例約 10-15%。",
  options: [
    "A. 正確。無性胚胎瘤可雙側發生，比例高於多數其他惡性卵巢生殖細胞腫瘤。",
    "B. 錯誤。卵黃囊瘤通常單側，雖惡性度高且 AFP 升高，但不是雙側最常見者。",
    "C. 錯誤。多胚瘤罕見，不能作為雙側性最高的典型答案。",
    "D. 錯誤。混合性生殖細胞腫瘤可含多種成分，但雙側最具代表性的單一類型仍是 dysgerminoma。"
  ],
  core: "卵巢惡性生殖細胞腫瘤多為單側；例外要記 dysgerminoma 雙側率較高。這點會影響術中評估對側卵巢。",
  key_point: "Dysgerminoma 是惡性卵巢生殖細胞腫瘤中較常雙側發生的類型。",
  flashcard_front: "卵巢生殖細胞瘤 / dysgerminoma / 雙側",
  flashcard_back: "Malignant ovarian germ cell tumors 多單側；dysgerminoma 雙側率較高，約 10-15%。",
});

add(50, {
  stem: "多毛症治療的錯誤選項是 medroxyprogesterone acetate。治療常用抑制雄性素作用或降低雄性素來源的藥物，而 MPA 不是典型抗雄性素治療選項。",
  options: [
    "A. 錯誤。Medroxyprogesterone acetate 可用於異常子宮出血或避孕等情境，但不是多毛症的典型抗雄性素治療藥。",
    "B. 正確。Flutamide 是雄性素受體拮抗劑，可減少多毛症；臨床使用需注意肝毒性與避孕。",
    "C. 正確。Spironolactone 具抗雄性素作用，是多毛症常用藥物之一，需注意懷孕禁忌與高血鉀。",
    "D. 正確。Cyproterone acetate 有抗雄性素與黃體素作用，可用於高雄性素相關多毛症。"
  ],
  core: "多毛症藥物重點是抗雄性素：spironolactone、cyproterone、flutamide 等。使用抗雄性素時要避孕，避免男性胎兒女性化風險。",
  key_point: "多毛症藥物治療常用抗雄性素；medroxyprogesterone acetate 不是典型治療答案。",
  flashcard_front: "多毛症 / 抗雄性素治療",
  flashcard_back: "Hirsutism 常用 spironolactone、cyproterone acetate、flutamide；抗雄性素治療需避孕。",
});

add(51, {
  stem: "高泌乳激素血症與泌乳激素腺瘤的錯誤敘述，是說 dopamine agonist 無法縮小腫瘤。Bromocriptine 與 cabergoline 可抑制 prolactin 分泌並縮小 prolactinoma。",
  options: [
    "A. 正確。Bromocriptine 作用時間較短，常需每日服用，副作用可有噁心、姿態性低血壓。",
    "B. 正確。Cabergoline 半衰期較長，常每週 1-2 次給藥，耐受性與降 prolactin 效果常較佳。",
    "C. 錯誤。Dopamine agonist 不只降 prolactin，也常能明顯縮小泌乳激素腺瘤，是一線治療。",
    "D. 正確。若 prolactin 正常且腫瘤控制穩定達一定時間，可在醫師監測下考慮停藥追蹤。"
  ],
  core: "Prolactinoma 一線是 dopamine agonist，特別是 cabergoline。考點不是只改善荷爾蒙，而是也能縮小腫瘤。",
  key_point: "Bromocriptine 與 cabergoline 可有效降低 prolactin 並縮小 prolactinoma。",
  flashcard_front: "Prolactinoma / dopamine agonist",
  flashcard_back: "Cabergoline、bromocriptine 是 prolactinoma 一線治療，可降 prolactin 並縮小腫瘤。",
});

add(52, {
  stem: "肥胖、青春痘、月經稀發與不規則出血，最像多囊性卵巢症候群或慢性無排卵。評估需排除懷孕並檢查內分泌與卵巢形態；染色體檢查不是必要初步檢查。",
  options: [
    "A. 必要。E2、FSH、LH 可協助評估排卵異常、卵巢功能與 PCOS 相關內分泌型態。",
    "B. 必要。育齡女性停經或異常出血必須先排除懷孕，尿液懷孕試驗是基本檢查。",
    "C. 非必要。染色體檢查多用於原發性無月經、性發育異常或疑似 Turner/DSD；本例已有月經史與高雄性素線索，不是首要。",
    "D. 必要。婦產科超音波可評估多囊卵巢形態、子宮內膜厚度與其他卵巢或子宮病灶。"
  ],
  core: "次發性月經異常先排除懷孕，再依臨床看 PCOS、甲狀腺、泌乳激素與卵巢/子宮病灶。染色體檢查主要放在原發性無月經或性發育異常。",
  key_point: "疑似 PCOS 或慢性無排卵的初步評估不需常規染色體檢查。",
  flashcard_front: "PCOS / 月經稀發 / 非必要檢查",
  flashcard_back: "育齡女性異常出血先驗孕；PCOS 評估含荷爾蒙與超音波。染色體檢查偏原發性無月經或 DSD。",
});

add(53, {
  stem: "試管嬰兒的 controlled ovarian stimulation 目標是讓多顆濾泡同時成熟。平常 FSH 下降會讓非優勢濾泡閉鎖；外源性 FSH 維持高於閾值，讓多顆濾泡一起成長。",
  options: [
    "A. 錯誤。Estradiol 是濾泡分泌的結果與監測指標，不是刺激多顆濾泡成熟的主要外給荷爾蒙。",
    "B. 正確。額外給予 FSH 可持續支持多顆濾泡發育，使其避免閉鎖並達到取卵前成熟。",
    "C. 錯誤。LH 可參與卵泡膜細胞產生 androgen 作為 estrogen 原料，但 controlled stimulation 的主要驅動不是額外 LH。",
    "D. 錯誤。給 estradiol 負回饋延遲 LH surge 不是讓多顆濾泡成熟的主要策略；臨床會用 GnRH agonist/antagonist 控制 LH surge。"
  ],
  core: "超排卵的核心是 FSH threshold：外源性 FSH 讓多顆濾泡一起跨過發育門檻。GnRH 類藥物主要用來避免過早 LH surge。",
  key_point: "Controlled ovarian stimulation 主要靠外源性 FSH 支持多顆濾泡同步成熟。",
  flashcard_front: "IVF / controlled ovarian stimulation / FSH",
  flashcard_back: "外源性 FSH 維持濾泡發育訊號，讓多顆濾泡避免閉鎖並同步成熟；GnRH 類藥物控制 LH surge。",
});

add(54, {
  stem: "PGD/PGT 需配合 IVF，從胚胎取細胞做遺傳檢測後再選擇胚胎植入。檢測為 46,XX 可以代表正常女性胚胎，不能說最可能是母親細胞污染。",
  options: [
    "A. 正確。PGD/PGT 必須先取得體外受精胚胎，才能在植入前進行胚胎細胞檢測。",
    "B. 錯誤。46,XX 是正常女性核型，可能就是正常胚胎結果；母體細胞污染是技術上需避免的問題，不是最可能解釋。",
    "C. 正確。PGT-A 或相關檢測可協助排除染色體數目或結構異常胚胎，降低植入不良或流產風險。",
    "D. 正確。對習慣性流產且疑染色體因素者，植入前檢測可減少植入異常胚胎，進而降低流產機會。"
  ],
  core: "PGD/PGT 是 IVF 流程中的植入前檢測。46,XX 本身是正常女性胚胎核型，不可看到 XX 就直接判定母體污染。",
  key_point: "PGD/PGT 需配合 IVF；46,XX 可為正常女性胚胎，不應直接視為母體細胞污染。",
  flashcard_front: "PGD/PGT / IVF / 46,XX",
  flashcard_back: "PGD 是植入前胚胎檢測，可排除染色體異常；46,XX 是正常女性核型，不等於母體污染。",
});

add(55, {
  stem: "身材矮小、無第二性徵、蹼狀頸與先天性心臟病，最符合 Turner syndrome。典型為高性腺刺激素性性腺功能低下；若為鑲嵌型，仍可能有卵巢功能與自發月經。",
  options: [
    "A. 錯誤。Turner syndrome 卵巢衰竭使 estradiol 低，負回饋不足導致 FSH/LH 升高，不是三者皆低。",
    "B. 錯誤。只有檢出 Y 染色體物質時才因 gonadoblastoma 風險考慮性腺切除；典型 45,X 不需立即常規切除性腺。",
    "C. 錯誤。Turner 患者有女性內生殖道，通常有子宮；問題主要是 streak gonads 與雌激素不足。",
    "D. 正確。45,X/46,XX 等鑲嵌型可能保留部分卵巢功能，部分患者可有青春期發育、正常月經甚至自然懷孕。"
  ],
  core: "Turner syndrome 記短身材、蹼狀頸、左心系病變、卵巢衰竭。抽血是 FSH/LH 高、E2 低；有 Y 物質才特別考慮性腺切除。",
  key_point: "Turner syndrome 為高 FSH/LH、低雌激素；鑲嵌型可有部分卵巢功能與自發月經。",
  flashcard_front: "Turner syndrome / FSH LH / mosaicism",
  flashcard_back: "Turner：short stature、webbed neck、streak gonads，FSH/LH 高、E2 低；45,X/46,XX 可有月經。",
});

add(56, {
  stem: "OHSS 與卵巢對刺激反應過強、VEGF 造成血管通透性增加有關，hCG 會延長並加重風險。以 GnRH agonist trigger 搭配全胚胎冷凍，可降低當週期 OHSS。",
  options: [
    "A. 錯誤。增加 gonadotropin 劑量會讓濾泡數與 estradiol 更高，反而提高 OHSS 風險。",
    "B. 正確。在 GnRH antagonist 週期可用 GnRH agonist 觸發排卵，再採 freeze-all，避免 hCG 與早孕加重 OHSS。",
    "C. 錯誤。GnRH agonist 長療程不是降低 OHSS 的最佳答案，且較不利於使用 agonist trigger 預防 OHSS。",
    "D. 錯誤。黃體期補充 hCG 會刺激黃體分泌 VEGF，增加或延長 OHSS 風險。"
  ],
  core: "預防 OHSS 要降低 hCG 暴露、避免新鮮植入造成懷孕性 hCG 加重。高風險者常考 GnRH agonist trigger 加 freeze-all。",
  key_point: "預防 OHSS 可使用 GnRH agonist trigger 並冷凍全部胚胎，避免 hCG 與當週期懷孕加重病情。",
  flashcard_front: "OHSS 預防 / GnRH agonist trigger / freeze-all",
  flashcard_back: "高風險 OHSS：用 GnRH agonist trigger，搭配 freeze-all；增加 gonadotropin 或 luteal hCG 會增加風險。",
});

add(57, {
  stem: "初級卵母細胞從胎兒期停在第一次減數分裂前期，直到排卵前 LH surge 才完成 meiosis I，形成次級卵母細胞與第一極體。",
  options: [
    "A. 錯誤。青春期後每個週期會招募卵泡，但不是所有卵細胞在青春期一次完成第一次減數分裂。",
    "B. 正確。LH surge 使優勢濾泡中的初級卵母細胞完成 meiosis I，進入次級卵母細胞階段。",
    "C. 錯誤。精子進入卵子會促使次級卵母細胞完成第二次減數分裂，不是第一次。",
    "D. 錯誤。受精後完成的是 meiosis II 並排出第二極體；meiosis I 已在排卵前完成。"
  ],
  core: "卵母細胞時序：胎兒期停在 meiosis I prophase，LH surge 完成 meiosis I；排卵後停在 meiosis II metaphase，受精才完成 meiosis II。",
  key_point: "卵細胞在 LH surge 時完成第一次減數分裂；受精時完成第二次減數分裂。",
  flashcard_front: "卵母細胞減數分裂 / LH surge",
  flashcard_back: "Primary oocyte 停在 prophase I；LH surge 完成 meiosis I。Secondary oocyte 停在 metaphase II，受精後完成 meiosis II。",
});

add(58, {
  stem: "大腿外側感覺麻痛且神經在鼠蹊韌帶附近受壓，典型是股外側皮神經壓迫造成的感覺異常性股痛。此神經是純感覺神經，不會造成股四頭肌無力。",
  options: [
    "A. 錯誤。股神經受損會影響髖屈曲、膝伸直與大腿前側/小腿內側感覺，不是單純大腿外側麻痛。",
    "B. 正確。股外側皮神經穿過鼠蹊韌帶附近，易受肥胖、懷孕、皮帶或姿勢壓迫，造成大腿外側麻痛。",
    "C. 錯誤。閉孔神經支配大腿內收肌與大腿內側感覺，病灶不會以大腿外側麻痛為主。",
    "D. 錯誤。陰部神經負責會陰部感覺與括約肌功能，受壓會造成會陰痛或骨盆底症狀。"
  ],
  core: "Meralgia paresthetica 等於 lateral femoral cutaneous nerve 在 inguinal ligament 附近受壓。症狀是大腿前外側感覺異常，沒有肌力缺損。",
  key_point: "股外側皮神經在鼠蹊韌帶附近受壓會造成大腿外側麻痛，即感覺異常性股痛。",
  flashcard_front: "Meralgia paresthetica / LFCN",
  flashcard_back: "Lateral femoral cutaneous nerve 是純感覺神經，穿過 inguinal ligament 附近受壓造成大腿外側麻痛。",
});

add(60, {
  stem: "顱內動脈瘤破裂最典型造成蜘蛛網膜下腔出血。血液進入蜘蛛網膜下腔時，常表現為雷擊般頭痛與急性腦膜刺激症狀。",
  options: [
    "A. 錯誤。視丘出血較典型與長期高血壓造成深部穿通動脈破裂相關，不是動脈瘤最典型出血型態。",
    "B. 錯誤。皮層下或葉狀出血可見於類澱粉血管病變、血管畸形或高血壓等，並非動脈瘤破裂的代表答案。",
    "C. 正確。腦底動脈瘤破裂會使血液進入蜘蛛網膜下腔，是自發性 SAH 的重要原因。",
    "D. 錯誤。小腦出血常與高血壓或血管畸形相關；動脈瘤破裂優先想到 SAH。"
  ],
  core: "動脈瘤破裂的考試連結是 subarachnoid hemorrhage。深部腦實質出血則多連長期高血壓穿通動脈病變。",
  key_point: "顱內動脈瘤破裂最典型造成蜘蛛網膜下腔出血。",
  flashcard_front: "腦動脈瘤 / SAH",
  flashcard_back: "Ruptured intracranial aneurysm -> subarachnoid hemorrhage；視丘、小腦等深部出血常連到高血壓。",
});

add(62, {
  stem: "退化性膝關節炎爬山後急性疼痛、腫脹與積水，屬急性發炎發作。此時不宜強行把疼痛膝關節牽拉到正常角度，會加重疼痛與滑膜刺激。",
  options: [
    "A. 適宜。NSAID 可減少急性發炎與疼痛，但須評估腎功能、胃腸道與心血管風險。",
    "B. 適宜。TENS 可作為疼痛控制輔助，對急性膝痛可減少疼痛感受。",
    "C. 最不適宜。急性腫脹積水且屈曲到 100 度即劇痛時，立即強行牽拉到正常角度會惡化發炎與疼痛。",
    "D. 適宜。等長股四頭肌運動能維持肌力且關節活動幅度小，適合急性疼痛期避免廢用。"
  ],
  core: "急性關節發炎積水先止痛、減少刺激、維持安全肌力，不做強迫性牽拉。等長運動比大幅度關節活動更適合急性期。",
  key_point: "膝關節急性發炎積水時不宜強行牽拉關節，可用止痛、TENS 與等長運動。",
  flashcard_front: "膝 OA 急性發作 / 積水 / 復健禁忌",
  flashcard_back: "Acute effusion/pain：avoid forceful stretching；可 NSAID、TENS、isometric exercise。",
});

add(63, {
  stem: "肩部超音波很適合評估旋轉肌袖肌腱與滑液囊，但盂唇位在深層關節內且受骨性結構遮蔽，超音波不易完整檢測，因此較需 MRI 或 MR arthrography。",
  options: [
    "A. 錯誤。脊上肌肌腱位置表淺，是肩部超音波最常評估的旋轉肌袖結構之一。",
    "B. 錯誤。脊下肌肌腱也可由超音波動態評估，包含肌腱病變與撕裂。",
    "C. 錯誤。三角肌下滑液囊表淺，積液或滑囊炎常可用超音波看見。",
    "D. 正確。肩盂唇在關節深處，超音波受骨頭遮蔽，評估 labral tear 較依賴 MRI，特別是 MR arthrogram。"
  ],
  core: "肩部超音波強項是 rotator cuff 與 subdeltoid bursa；關節內盂唇病變是 MRI/MR arthrogram 的領域。",
  key_point: "肩關節盂唇位於深層關節內，超音波不易檢測，較需 MRI 或 MR arthrography。",
  flashcard_front: "肩部影像 / labrum / ultrasound limitation",
  flashcard_back: "US 可看 supraspinatus、infraspinatus、subdeltoid bursa；labrum 深且受骨遮蔽，靠 MRI/MRA。",
});

add(64, {
  stem: "非發炎性關節液的例外特徵，是白血球數高於 2000/mm3。非發炎性關節液通常黏稠度高、mucin clot 好、白血球少；超過 2000/mm3 已偏向發炎性關節液。",
  options: [
    "A. 錯誤。非發炎性關節液透明黏稠，透明質酸保存較好，因此 mucin clot test 通常佳。",
    "B. 錯誤。非發炎性關節液中多形核白血球比例低，通常小於 25%。",
    "C. 正確。白血球數高於 2000/mm3 不符合非發炎性關節液，較提示發炎性關節炎。",
    "D. 錯誤。非發炎性關節液黏稠度高；發炎時透明質酸被破壞，黏稠度下降。"
  ],
  core: "關節液分類先看 WBC 與黏稠度。非發炎性通常 WBC < 2000/mm3、PMN < 25%、黏稠度高、mucin clot 好。",
  key_point: "非發炎性關節液 WBC 應低於 2000/mm3；高於 2000/mm3 較支持發炎性。",
  flashcard_front: "關節液分析 / non-inflammatory",
  flashcard_back: "Non-inflammatory synovial fluid：WBC <2000/mm3、PMN <25%、viscosity high、mucin clot good。",
});

add(65, {
  stem: "骨折復健原則的錯誤點，是急性期對骨折處做局部熱療。骨折急性期局部發炎與腫脹明顯，熱療會增加血流與腫脹，通常先用冰敷與保護性活動。",
  options: [
    "A. 正確。未被固定的鄰近關節應儘早活動，避免僵硬、攣縮與肌力下降。",
    "B. 正確。老年人步態訓練常先用助行器增加支撐面與穩定性，再依能力進階。",
    "C. 錯誤。急性骨折處不宜局部熱療；熱會加重水腫與發炎，急性期較適合冰敷、抬高與保護。",
    "D. 正確。依骨折穩定度與醫囑逐步增加負重，可刺激骨痂形成與骨癒合，但不能過早過量。"
  ],
  core: "骨折復健抓兩件事：未固定關節早動，骨折處急性期避免熱療與過度牽拉。負重需漸進，配合固定穩定度。",
  key_point: "骨折急性期不宜局部熱療；未固定關節應早期活動，負重需依穩定度漸進。",
  flashcard_front: "骨折復健 / 急性期熱療",
  flashcard_back: "Acute fracture：avoid heat over fracture site；use protection/ice/elevation，unimmobilized joints move early，weight bearing gradual。",
});

add(66, {
  stem: "圖中的背架若為 Milwaukee brace，屬 CTLSO，能控制較高位胸椎側彎。頂點在 T6 的右凸胸椎側彎符合其適應症。",
  options: [
    "A. 錯誤。第七頸椎骨折需要頸椎固定或更高階頸胸固定，Milwaukee brace 不是處理急性頸椎骨折的典型答案。",
    "B. 正確。Milwaukee brace 適用於頂點在 T7 或以上的高位胸椎側彎，T6 頂點正符合。",
    "C. 錯誤。第十胸椎壓迫性骨折較常用 TLSO 或 Jewett brace 類型，不需要 Milwaukee 的頸環控制高胸段。",
    "D. 錯誤。第一腰椎骨折脫位通常是不穩定傷害，需手術評估或嚴格胸腰椎固定，不是側彎矯正背架適應症。"
  ],
  core: "Milwaukee brace 是 CTLSO，重點適合高胸椎側彎，特別是頂點 T7 以上。低胸腰椎側彎或壓迫骨折會用不同支架。",
  key_point: "Milwaukee brace 適用於頂點在 T7 以上的高位胸椎側彎，如 T6 頂點側彎。",
  flashcard_front: "Milwaukee brace / 高位胸椎側彎",
  flashcard_back: "Milwaukee brace = CTLSO，適合 scoliosis apex T7 or above；T10 compression fracture 多用 TLSO/Jewett。",
});

add(67, {
  stem: "肌力訓練的錯誤敘述，是把等張運動和等角速度運動畫上等號。等張是負荷相對固定、速度可變，等角速度是速度固定、阻力隨力矩改變。",
  options: [
    "A. 大致正確。阻力訓練可用高阻力誘發肌肉收縮，臨床可設計成等長、等張或等速；本選項描述偏向等長阻力訓練情境。",
    "B. 正確。等長阻力訓練時肌肉產生張力但關節角度不變，因此不產生可見關節動作。",
    "C. 錯誤。等張運動負重固定但速度會變；等角速度運動需特殊設備維持固定角速度，兩者不能畫上等號。",
    "D. 正確。高阻力訓練可使血壓與心臟負荷上升，心臟病患或老年人需謹慎評估與調整強度。"
  ],
  core: "肌力訓練名詞要分清：isometric 是長度不變，isotonic 是張力/負荷相對固定且有動作，isokinetic 是速度固定。等張不等於等速。",
  key_point: "等張運動與等角速度運動不同；等張負荷相對固定，等速需維持固定角速度。",
  flashcard_front: "肌力訓練 / isotonic / isokinetic",
  flashcard_back: "Isometric 無關節動作；isotonic 有動作且速度可變；isokinetic 用設備控制固定角速度。",
});

add(68, {
  stem: "Symmetric tonic neck reflex 是嬰兒原始反射之一，頭部位置會對上下肢張力造成相反影響。頭屈曲時上肢屈曲、下肢伸直；頭伸直時上肢伸直、下肢屈曲。",
  options: [
    "A. 錯誤。頭屈曲時上肢會屈曲沒錯，但下肢應伸直，不是同樣彎曲。",
    "B. 正確。這正是 STNR 頭部屈曲時的典型模式：上肢屈曲、下肢伸直。",
    "C. 錯誤。頭伸直時上肢會伸直，但下肢應屈曲，不是也伸直。",
    "D. 錯誤。頭伸直時上肢應伸直、下肢屈曲，本選項把上下肢反應寫反。"
  ],
  core: "STNR 可記成頭屈曲像跪爬準備：手彎、腳伸；頭伸直則手伸、腳彎。它和 ATNR 的單側姿勢不同。",
  key_point: "STNR：頭屈曲時上肢屈曲、下肢伸直；頭伸直時上肢伸直、下肢屈曲。",
  flashcard_front: "STNR / 頭屈曲與伸直反應",
  flashcard_back: "Symmetric tonic neck reflex：neck flexion -> arms flex, legs extend；neck extension -> arms extend, legs flex。",
});

add(69, {
  stem: "病人語言流暢、聽理解佳，但覆述、聽寫與朗讀困難，最符合傳導型失語症。典型病灶涉及弓狀束或顳頂葉連結，使理解與表達相對保留但重複能力明顯受損。",
  options: [
    "A. 錯誤。Wernicke aphasia 雖流暢，但聽理解明顯差，常說出語意空洞或錯亂語句，不符合本題理解佳。",
    "B. 正確。Conduction aphasia 的核心是 fluent speech、good comprehension、poor repetition，常有音韻性語誤。",
    "C. 錯誤。Transcortical mixed aphasia 會有非流暢、理解差但覆述相對保留，和本題覆述困難相反。",
    "D. 錯誤。Ataxic dysarthria 是構音協調問題，語言內容、理解與覆述語言迴路不是主要病灶。"
  ],
  core: "失語症分類先看流暢度、理解、覆述。理解好且流暢但覆述差，就是 conduction aphasia。",
  key_point: "傳導型失語症特徵為語言流暢與理解佳，但覆述能力明顯受損。",
  flashcard_front: "Conduction aphasia / repetition",
  flashcard_back: "Conduction aphasia：fluent、comprehension good、repetition poor，常和 arcuate fasciculus 病變相關。",
});

add(71, {
  stem: "評估吞嚥功能的黃金標準是錄影螢光吞嚥檢查。它可在透視下觀察口腔期、咽期與食道入口通過，並能偵測吸入與殘留。",
  options: [
    "A. 錯誤。Manometry 可量測壓力與括約肌功能，但不能完整呈現吞嚥時食團流動與吸入情形。",
    "B. 錯誤。超音波可輔助觀察舌骨或舌部動作，但不是吞嚥功能評估的黃金標準。",
    "C. 正確。Videofluorographic swallowing study，也常稱 VFSS 或 modified barium swallow，是吞嚥障礙評估的重要標準檢查。",
    "D. 錯誤。CT 可看結構性病灶，但無法動態評估吞嚥過程中的吸入、滯留與代償策略效果。"
  ],
  core: "吞嚥障礙評估要分動態功能與靜態影像。VFSS 能即時看含鋇食團通過與是否吸入，因此是常考黃金標準。",
  key_point: "錄影螢光吞嚥檢查 VFSS 是評估吞嚥功能與吸入風險的黃金標準之一。",
  flashcard_front: "吞嚥功能評估 / VFSS",
  flashcard_back: "VFSS/modified barium swallow 可動態看口咽吞嚥、殘留與 aspiration，是吞嚥評估黃金標準。",
});

add(72, {
  stem: "40 歲女性慢性單眼視力下降，增強脂肪抑制 T1 MRI 若見視神經鞘環狀或雙軌樣增強，最符合視神經鞘腦膜瘤。病灶通常包繞視神經，而非視神經本身梭狀膨大。",
  options: [
    "A. 錯誤。視神經膠質瘤較常見於兒童，影像多為視神經本身梭狀增粗，和中年女性、視神經鞘增強較不合。",
    "B. 正確。Optic nerve sheath meningioma 好發中年女性，MRI 可見 tram-track sign 或 doughnut sign，造成慢性漸進視力下降。",
    "C. 錯誤。視神經炎通常是急性或亞急性疼痛性視力下降，影像為視神經內增強，不是鞘膜包繞性腫瘤。",
    "D. 錯誤。眼窩假性腫瘤常見疼痛、眼外肌或淚腺等眼窩發炎腫脹，不是典型視神經鞘雙軌增強。"
  ],
  core: "視神經鞘腦膜瘤考中年女性、慢性視力下降、MRI tram-track/doughnut enhancement。視神經膠質瘤偏兒童，視神經炎偏急性疼痛。",
  key_point: "視神經鞘腦膜瘤在增強 MRI 可見視神經鞘包繞增強的 tram-track sign。",
  flashcard_front: "Optic nerve sheath meningioma / tram-track sign",
  flashcard_back: "ONSM：中年女性、慢性單眼視力下降、視神經鞘增強呈 tram-track；glioma 多兒童且視神經本身增粗。",
});

add(73, {
  stem: "動脈瘤性蜘蛛網膜下腔出血的錯誤敘述，是血管痙攣在前三天最嚴重。SAH 後血管痙攣與延遲性腦缺血通常在第 4-14 天發生，約第 7-10 天高峰。",
  options: [
    "A. 正確。出血在 basal cistern、sylvian fissure 或 interhemispheric fissure 的分布，可提供動脈瘤位置線索。",
    "B. 錯誤。Vasospasm 通常不是前三天最嚴重；臨床高風險期多在出血後第 4-14 天，約第 7-10 天高峰。",
    "C. 正確。CTA 對大於約 2 mm 的動脈瘤敏感度高，是急性 SAH 常用的非侵入性血管影像。",
    "D. 正確。SAH 的血液會阻礙蛛網膜顆粒吸收腦脊髓液，可造成交通性水腦。"
  ],
  core: "SAH 併發症時序很常考：再出血偏早，vasospasm/DCI 多在第 4-14 天，高峰約第 7-10 天。水腦可急性或延遲發生。",
  key_point: "SAH 後血管痙攣多在第 4-14 天，約第 7-10 天最嚴重，不是前三天。",
  flashcard_front: "SAH / vasospasm timing",
  flashcard_back: "Aneurysmal SAH vasospasm/DCI：days 4-14，peak around days 7-10；可造成 communicating hydrocephalus。",
});

add(74, {
  stem: "MRI 箭頭若顯示子宮底外緣凹陷並形成兩個子宮腔，最符合雙角子宮。雙角子宮是 Müllerian duct 融合不全，通常有單一子宮頸。",
  options: [
    "A. 正確。Bicornuate uterus 典型是子宮底外輪廓凹陷、兩個角分開，可在 MRI 上看到雙腔與外部 fundal cleft。",
    "B. 錯誤。雙子宮 didelphys 通常有兩個分離子宮體與兩個子宮頸，分離程度比雙角子宮更完全。",
    "C. 錯誤。子宮經血滯留會呈現子宮腔或陰道血液擴張訊號，重點是阻塞與血液滯留，不是雙角形態。",
    "D. 錯誤。單角子宮是一側 Müllerian duct 發育不全，子宮呈單側香蕉狀或單角外觀，不會形成對稱雙角。"
  ],
  core: "Müllerian anomaly 影像要看外部 fundal contour。雙角子宮有外部子宮底凹陷；中隔子宮外形較平，雙子宮分離更完全。",
  key_point: "雙角子宮 MRI 特徵為子宮底外緣明顯凹陷並形成兩個子宮腔。",
  flashcard_front: "雙角子宮 / MRI / Müllerian anomaly",
  flashcard_back: "Bicornuate uterus：融合不全，fundal cleft 明顯、雙子宮腔，多為單一 cervix；didelphys 分離更完全。",
});

add(76, {
  stem: "突發性耳聾的正確敘述，是多數屬特發性。突發性耳聾多定義為短時間內發生的感音神經性聽損，臨床多數找不到明確原因。",
  options: [
    "A. 錯誤。典型定義是 72 小時內發生，至少連續 3 個頻率下降 30 dB 以上，不是一個月內。",
    "B. 錯誤。突發性耳聾可見於各年齡，但發生率與年齡有關，並非完全無關。",
    "C. 正確。多數突發性感音神經性聽損找不到明確病因，歸為原發性或特發性。",
    "D. 錯誤。腮腺炎等病毒感染可造成感音神經性聽損，不能說已證實無關。"
  ],
  core: "突發性耳聾定義抓 72 小時、3 個連續頻率、30 dB。病因多數 idiopathic，但仍要評估病毒、血管、免疫與腫瘤等可能。",
  key_point: "突發性耳聾多為 72 小時內發生的感音神經性聽損，原因多數為 idiopathic。",
  flashcard_front: "突發性耳聾 / 定義 / idiopathic",
  flashcard_back: "Sudden SNHL：72 hours、3 contiguous frequencies、>=30 dB；多數 idiopathic，病毒如 mumps 仍可相關。",
});

add(77, {
  stem: "28 週孕婦高血壓疑子癲前症時，seizure 是子癇症而非單純子癲前症表現。高血壓、蛋白尿與寡尿可屬子癲前症或 severe features；一旦出現癲癇發作，診斷已是子癇症。",
  options: [
    "A. 錯誤。高血壓是子癲前症的核心診斷條件，通常為妊娠 20 週後新發高血壓。",
    "B. 錯誤。蛋白尿是傳統子癲前症重要表現之一；即使無蛋白尿，也可依器官受損診斷。",
    "C. 錯誤。寡尿代表腎臟灌流或腎功能受影響，可出現在較嚴重的子癲前症。",
    "D. 正確。癲癇發作代表從 pre-eclampsia 進展為 eclampsia，因此不是單純子癲前症的表現。"
  ],
  core: "子癲前症是 20 週後高血壓加蛋白尿或器官受損；若有不能用其他原因解釋的抽搐，就是子癇症。考題常用 seizure 區分兩者。",
  key_point: "子癲前症可有高血壓、蛋白尿與寡尿；出現癲癇發作則為子癇症。",
  flashcard_front: "子癲前症 vs 子癇症 / seizure",
  flashcard_back: "Preeclampsia：HTN + proteinuria/organ dysfunction after 20 weeks；seizure = eclampsia。",
});

add(79, {
  stem: "病人昏迷且過去已書面指定鄰居為醫療委任代理人時，代理決定權應回到病人事前授權。意定醫療委任代理人的指定是尊重病人自主意願，順位優先於未被指定的親屬。",
  options: [
    "A. 錯誤。兒子是親屬，但病人已在清楚時書面指定鄰居為醫療委任代理人，不能直接由兒子取代。",
    "B. 正確。若指定有效且鄰居為唯一受指定代理人，鄰居即依病人授權行使醫療代理決定。",
    "C. 錯誤。法律重點是病人已指定代理人；未被指定的兒子不會因此和鄰居自動成為共同代理。",
    "D. 錯誤。病人清楚時可指定符合資格的醫療委任代理人；不是因代理人是鄰居就不得代理。"
  ],
  core: "醫療決策代理要先尊重病人事前明示意願。有效書面指定的醫療委任代理人，優先於一般親屬順位或醫療團隊自行推定。",
  key_point: "有效書面指定的醫療委任代理人優先行使代理決定權，不能由未指定親屬任意取代。",
  flashcard_front: "醫療委任代理人 / 病人自主",
  flashcard_back: "病人清楚時書面指定代理人，該意定代理人優先；親屬不會自動共同或取代代理。",
});

add(80, {
  stem: "病人有妄想、監控與暴力風險，家屬安全受威脅，處置要兼顧病人治療、被害人保護與法律程序。直接把抗精神病藥交給家屬暗中下藥，違反知情同意與用藥安全，最不適當。",
  options: [
    "A. 最不適當。未經病人評估與同意就讓家屬暗中給藥，會造成劑量、副作用、責任與人權問題，也可能激化危險。",
    "B. 適當。若病人因精神病症狀有傷害自己或他人之虞，依法評估強制住院治療是可考慮的安全處置。",
    "C. 適當。家屬面臨暴力威脅時，需要社政、保護令、危機安置與精神醫療資源協助。",
    "D. 適當。當病人及家屬安全有立即風險，通知社工、保護網絡或警政單位有助於危機處理。"
  ],
  core: "精神科急性危機不能用暗中下藥處理。高暴力風險時，正確方向是正式評估、必要時強制住院，並啟動社政與警政安全網。",
  key_point: "具妄想與暴力風險的精神病人不可由家屬暗中給藥；應正式評估強制住院與通報安全資源。",
  flashcard_front: "精神病暴力風險 / 暗中給藥 / 強制住院",
  flashcard_back: "Covert medication 給家屬暗中下藥不適當；有傷人風險時要依法評估住院並連結社政警政。",
});

function loadSource() {
  return JSON.parse(fs.readFileSync(path.join(process.cwd(), SOURCE_FILE), "utf8"));
}

function buildUpdateForQuestion(question) {
  const item = updates[question.question_number];
  if (!item) {
    throw new Error(`Missing authored update for Q${question.question_number}`);
  }
  const flashcardSummary = item.flashcard_summary || summary(item.flashcard_front, item.flashcard_back);
  return {
    question_id: question.id,
    question_number: question.question_number,
    explanation: explanation(item.stem, item.options, item.core),
    key_point: item.key_point,
    flashcard_front: item.flashcard_front,
    flashcard_back: item.flashcard_back,
    flashcard_summary: flashcardSummary,
    review_status: "ai_generated",
    explanation_model: MODEL,
    explanation_generated_at: GENERATED_AT,
    manual_review_notes: item.manual_review_notes || [],
  };
}

function optionSection(text) {
  if (!text.includes("【選項詳解】")) return text;
  const after = text.split("【選項詳解】", 2)[1];
  return after.includes("【核心考點】") ? after.split("【核心考點】", 1)[0] : after;
}

function optionBlocks(text) {
  const section = optionSection(text);
  const pattern = /(?:^|\n)\s*-\s*([A-D])\.\s*/g;
  const matches = [...section.matchAll(pattern)];
  return matches.map((match, index) => {
    const start = match.index + match[0].length;
    const end = index + 1 < matches.length ? matches[index + 1].index : section.length;
    return { label: match[1], text: section.slice(start, end).trim() };
  });
}

function compact(text) {
  return String(text || "").replace(/\s+/g, "");
}

function repeatedOptionSegments(text) {
  const bySegment = new Map();
  for (const block of optionBlocks(text)) {
    for (const raw of block.text.split(/[。；;!?！？\n]+/)) {
      const segment = compact(raw);
      if (segment.length < 36) continue;
      if (!bySegment.has(segment)) bySegment.set(segment, new Set());
      bySegment.get(segment).add(block.label);
    }
  }
  return [...bySegment.entries()]
    .filter(([, labels]) => labels.size >= 3)
    .map(([segment, labels]) => ({ segment, labels: [...labels].sort() }));
}

function validatePayload(payload, source) {
  const errors = [];
  const sourceByNumber = new Map(source.questions.map((question) => [question.question_number, question]));

  if (payload.source_file !== SOURCE_FILE) errors.push(`${payload.range.start}-${payload.range.end}: source_file mismatch`);
  if (payload.dataset_id !== DATASET_ID) errors.push(`${payload.range.start}-${payload.range.end}: dataset_id mismatch`);
  if (!payload.range || typeof payload.range.start !== "number" || typeof payload.range.end !== "number") {
    errors.push(`${payload.source_file}: invalid range`);
  }
  if (!Array.isArray(payload.updates)) errors.push(`${payload.source_file}: updates must be array`);

  for (const update of payload.updates || []) {
    const qn = update.question_number;
    const sourceQuestion = sourceByNumber.get(qn);
    if (!sourceQuestion) errors.push(`Q${qn}: source question missing`);
    if (sourceQuestion && update.question_id !== sourceQuestion.id) errors.push(`Q${qn}: question_id mismatch`);
    if (qn < payload.range.start || qn > payload.range.end) errors.push(`Q${qn}: outside declared range`);
    for (const key of Object.keys(update)) {
      if (!ALLOWED_UPDATE_FIELDS.has(key)) errors.push(`Q${qn}: disallowed update field ${key}`);
    }
    for (const heading of REQUIRED_HEADINGS) {
      if (!String(update.explanation || "").includes(heading)) errors.push(`Q${qn}: missing heading ${heading}`);
    }
    const labels = new Set(optionBlocks(update.explanation).map((block) => block.label));
    for (const label of ["A", "B", "C", "D"]) {
      if (!labels.has(label)) errors.push(`Q${qn}: missing option ${label}`);
    }
    for (const phrase of BANNED_PHRASES) {
      if (String(update.explanation || "").includes(phrase)) errors.push(`Q${qn}: banned phrase ${phrase}`);
    }
    const repeated = repeatedOptionSegments(update.explanation);
    if (repeated.length) errors.push(`Q${qn}: repeated option segment ${repeated[0].labels.join(",")}`);
    if (compact(update.explanation).length < 260) errors.push(`Q${qn}: explanation too short`);
    if (!Array.isArray(update.manual_review_notes)) errors.push(`Q${qn}: manual_review_notes must be array`);
  }
  return errors;
}

function buildPayload(batch, source) {
  const questionsByNumber = new Map(source.questions.map((question) => [question.question_number, question]));
  return {
    source_file: SOURCE_FILE,
    dataset_id: DATASET_ID,
    range: batch.range,
    updates: batch.nums.map((questionNumber) => buildUpdateForQuestion(questionsByNumber.get(questionNumber))),
  };
}

function writeUpdates() {
  const source = loadSource();
  fs.mkdirSync(path.join(process.cwd(), UPDATE_DIR), { recursive: true });
  const authored = Object.keys(updates).map(Number).sort((a, b) => a - b);
  if (JSON.stringify(authored) !== JSON.stringify(TARGETS)) {
    throw new Error(`Authored target mismatch: ${authored.join(",")}`);
  }

  for (const batch of BATCHES) {
    const payload = buildPayload(batch, source);
    const errors = validatePayload(payload, source);
    if (errors.length) throw new Error(errors.join("\n"));
    fs.writeFileSync(path.join(process.cwd(), UPDATE_DIR, batch.file), `${JSON.stringify(payload, null, 2)}\n`, "utf8");
    console.log(`wrote ${batch.file}: ${payload.updates.length} updates`);
  }
}

function loadPayloads() {
  const source = loadSource();
  return BATCHES.map((batch) => {
    const fullPath = path.join(process.cwd(), UPDATE_DIR, batch.file);
    const payload = JSON.parse(fs.readFileSync(fullPath, "utf8"));
    const errors = validatePayload(payload, source);
    if (errors.length) throw new Error(errors.join("\n"));
    const actualNums = payload.updates.map((update) => update.question_number);
    if (JSON.stringify(actualNums) !== JSON.stringify(batch.nums)) {
      throw new Error(`${batch.file}: question list mismatch ${actualNums.join(",")}`);
    }
    return payload;
  });
}

function validateUpdates() {
  const payloads = loadPayloads();
  const total = payloads.reduce((sum, payload) => sum + payload.updates.length, 0);
  const reviewNotes = payloads.flatMap((payload) => payload.updates.filter((update) => update.manual_review_notes.length));
  console.log(`validated update files: ${payloads.length}`);
  console.log(`validated updates: ${total}`);
  console.log(`manual review notes: ${reviewNotes.map((update) => `Q${update.question_number}`).join(",") || "none"}`);
}

function mergeUpdates() {
  const source = loadSource();
  const payloads = loadPayloads();
  const sourceByNumber = new Map(source.questions.map((question) => [question.question_number, question]));
  const mergedNumbers = [];

  for (const payload of payloads) {
    for (const update of payload.updates) {
      const question = sourceByNumber.get(update.question_number);
      for (const field of ALLOWED_CHANGED_FIELDS) {
        if (Object.prototype.hasOwnProperty.call(update, field)) {
          question[field] = update[field];
        }
      }
      mergedNumbers.push(update.question_number);
    }
  }

  if (JSON.stringify(mergedNumbers.sort((a, b) => a - b)) !== JSON.stringify([...TARGETS].sort((a, b) => a - b))) {
    throw new Error(`Merged target mismatch: ${mergedNumbers.join(",")}`);
  }

  fs.writeFileSync(path.join(process.cwd(), SOURCE_FILE), `${JSON.stringify(source, null, 2)}\n`, "utf8");
  console.log(`merged updates into ${SOURCE_FILE}: ${mergedNumbers.length} questions`);
}

function deepEqual(a, b) {
  return JSON.stringify(a) === JSON.stringify(b);
}

function readHeadSource() {
  const stdout = cp.execFileSync("git", ["show", `HEAD:${SOURCE_FILE}`], {
    cwd: process.cwd(),
    encoding: "utf8",
    maxBuffer: 20 * 1024 * 1024,
  });
  return JSON.parse(stdout);
}

function checkSourceDiff() {
  const head = readHeadSource();
  const current = loadSource();
  const errors = [];
  if (head.questions.length !== current.questions.length) {
    errors.push(`question count changed: ${head.questions.length} -> ${current.questions.length}`);
  }
  if (head.id !== current.id || head.title !== current.title || head.year !== current.year || head.subject !== current.subject) {
    errors.push("top-level identity changed");
  }
  const targetSet = new Set(TARGETS);
  const byId = new Map(head.questions.map((question) => [question.id, question]));
  for (const question of current.questions) {
    const before = byId.get(question.id);
    if (!before) {
      errors.push(`new or changed id detected: ${question.id}`);
      continue;
    }
    const allKeys = new Set([...Object.keys(before), ...Object.keys(question)]);
    for (const key of allKeys) {
      if (ALLOWED_CHANGED_FIELDS.has(key)) continue;
      if (!deepEqual(before[key], question[key])) {
        errors.push(`Q${question.question_number}: immutable field changed: ${key}`);
      }
    }
    if (!targetSet.has(question.question_number)) {
      for (const key of ALLOWED_CHANGED_FIELDS) {
        if (!deepEqual(before[key], question[key])) {
          errors.push(`Q${question.question_number}: non-target explanation field changed: ${key}`);
        }
      }
    }
  }
  if (errors.length) throw new Error(errors.join("\n"));
  console.log("source diff check passed: only target explanation-related fields changed");
}

function reviewProse() {
  const source = loadSource();
  const targetSet = new Set(TARGETS);
  const issues = [];
  for (const question of source.questions) {
    if (!targetSet.has(question.question_number)) continue;
    const text = String(question.explanation || "");
    for (const phrase of BANNED_PHRASES) {
      if (text.includes(phrase)) issues.push(`Q${question.question_number}: banned phrase ${phrase}`);
    }
    const repeated = repeatedOptionSegments(text);
    if (repeated.length) issues.push(`Q${question.question_number}: repeated option segment`);
    const optionTexts = optionBlocks(text).map((block) => block.text);
    const starts = optionTexts.map((block) => block.slice(0, 16));
    const duplicateStarts = starts.filter((start, index) => starts.indexOf(start) !== index);
    if (duplicateStarts.length >= 2) {
      issues.push(`Q${question.question_number}: duplicate option opening`);
    }
    if ((text.match(/本題/g) || []).length > 4) {
      issues.push(`Q${question.question_number}: possible redundant 本題 wording`);
    }
  }
  if (issues.length) throw new Error(issues.join("\n"));
  console.log("prose review passed: no banned filler, repeated option segment, duplicate option opening, or redundant wording flags");
}

const mode = process.argv[2] || "--help";

if (mode === "--write-updates") {
  writeUpdates();
} else if (mode === "--validate-updates") {
  validateUpdates();
} else if (mode === "--merge") {
  mergeUpdates();
} else if (mode === "--check-source-diff") {
  checkSourceDiff();
} else if (mode === "--review-prose") {
  reviewProse();
} else {
  console.log("Usage: node scratch/rewrite_1082_medicine6.cjs --write-updates|--validate-updates|--merge|--check-source-diff|--review-prose");
}
