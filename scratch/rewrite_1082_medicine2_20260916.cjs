const fs = require("fs");
const path = require("path");

const sourceFile = "public/data/exams/108-2/medicine-2.json";
const datasetId = "108-2_medicine-2";
const updateDir = "scratch/rewrite_updates/108-2_medicine-2";
const timestamp = "2026-09-16T00:00:00+08:00";
const model = "codex-high-quality-rewrite";

const allowedUpdateFields = new Set([
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

const bannedPhrases = [
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
];

const updates = {
  7: {
    explanation: `【題幹解析】
本題考分枝桿菌以培養生長速度分類。結核分枝桿菌培養通常需數週，屬慢速生長型；龜、偶發與膿瘍分枝桿菌則是典型快速生長型，標準答案為 B。

【選項詳解】
- A. 龜分枝桿菌 (M. chelonae) 錯在它屬快速生長型非結核分枝桿菌，常可在約 7 天內長出菌落，與慢速生長型相反。
- B. 結核分枝桿菌 (M. tuberculosis) 正確。它是典型慢速生長型分枝桿菌，臨床培養常需 2 到 8 週，這也是肺結核檢驗回報慢的原因之一。
- C. 偶發分枝桿菌 (M. fortuitum) 錯在它屬快速生長型，名稱也常和術後、外傷或導管相關感染一起考。
- D. 膿瘍分枝桿菌 (M. abscessus) 錯在它同樣屬快速生長型，常與皮膚軟組織、肺部或醫療處置相關感染有關。

【核心考點】
分枝桿菌考生長速度時，M. tuberculosis 是慢速生長型；M. fortuitum、M. chelonae、M. abscessus 是快速生長型。`,
    key_point: "M. tuberculosis 為慢速生長型分枝桿菌；M. chelonae、M. fortuitum、M. abscessus 屬快速生長型。",
    flashcard_front: "分枝桿菌中，哪一個是典型慢速生長型？哪些常考為快速生長型？",
    flashcard_back: "慢速生長型：M. tuberculosis。快速生長型：M. fortuitum、M. chelonae、M. abscessus。",
    flashcard_summary: "分枝桿菌生長速度分類：結核分枝桿菌慢，龜、偶發、膿瘍分枝桿菌快。",
  },
  13: {
    explanation: `【題幹解析】
本題比較幾種蟲媒病毒的主要天然宿主或維持宿主。基孔肯雅病毒在人際流行時以人類作為重要放大宿主，較符合題幹「人類是最明確天然宿主」的問法，標準答案為 D。

【選項詳解】
- A. 辛德畢斯病毒 (Sindbis virus) 主要在鳥類與蚊子之間維持傳播，人類多是偶然感染者，不是最明確的天然宿主。
- B. 塞姆利基森林病毒 (Semliki Forest virus) 原本與非洲森林生態圈、蚊媒及動物宿主較相關，人類不是此病毒最典型的維持宿主。
- C. 西尼羅腦炎病毒 (West Nile virus) 的主要自然循環是鳥類與蚊子；人類與馬多為終末宿主，病毒血症通常不足以有效回傳給蚊子。
- D. 基孔肯雅病毒 (Chikungunya virus) 正確。都市流行循環中，人類可產生足以感染蚊子的病毒血症，與埃及斑蚊或白線斑蚊形成「人-蚊-人」傳播。

【核心考點】
西尼羅病毒要記鳥類是主要放大宿主；基孔肯雅病毒在都市流行中以人類作為重要放大宿主，是本題選 D 的關鍵。`,
    key_point: "基孔肯雅病毒在都市流行循環中以人類作為重要放大宿主；西尼羅病毒主要宿主是鳥類。",
    flashcard_front: "West Nile virus 與 Chikungunya virus 的主要自然宿主或放大宿主如何區分？",
    flashcard_back: "West Nile virus：鳥類為主要放大宿主，人類多為終末宿主。Chikungunya virus：都市流行中人類可作為重要放大宿主，經斑蚊人際傳播。",
    flashcard_summary: "蟲媒病毒宿主：West Nile 偏鳥類循環；Chikungunya 都市流行可人-蚊-人傳播。",
  },
  25: {
    explanation: `【題幹解析】
肉芽腫是慢性發炎中巨噬細胞被持續刺激後形成的結構。圍繞中心壞死或難以清除病原的那層整齊單核細胞，是由活化巨噬細胞轉變而來的類上皮細胞，標準答案為 B。

【選項詳解】
- A. 上皮細胞 (epithelial cells) 是覆蓋體表或腔道的真正上皮，不是肉芽腫中由巨噬細胞活化形成的細胞。
- B. 類上皮細胞 (epithelioid cells) 正確。它們是活化巨噬細胞，胞質豐富、排列緊密，會圍繞肉芽腫中心，常見於結核、異物或某些黴菌感染。
- C. 漿細胞 (plasma cells) 是分泌抗體的 B 細胞分化產物，可出現在慢性發炎背景，但不是肉芽腫的典型環狀主體細胞。
- D. 壞死嗜中性白血球與微生物可構成化膿性壞死或中心壞死內容物，但題幹問的是外圍排列整齊的單核細胞層，不是中心碎屑。

【核心考點】
肉芽腫的代表細胞是類上皮細胞，也就是活化巨噬細胞；可伴隨 Langhans giant cells、淋巴球與中央乾酪性壞死。`,
    key_point: "肉芽腫中圍繞中心的主要細胞是由活化巨噬細胞形成的類上皮細胞。",
    flashcard_front: "肉芽腫中排列成層、圍繞中心壞死或病原的主要細胞是什麼？",
    flashcard_back: "類上皮細胞 (epithelioid cells)，本質是活化巨噬細胞。",
    flashcard_summary: "肉芽腫病理：類上皮細胞是活化巨噬細胞，圍繞中心壞死或難清除病原。",
  },
  29: {
    explanation: `【題幹解析】
本題是三段敘述組合題，需找出鉤蟲感染的錯誤敘述。十二指腸鉤蟲不只可經皮膚感染，鉤蟲重度感染會因慢性失血造成缺鐵性貧血，而感染後最早的臨床表現通常是幼蟲穿皮造成的局部皮膚炎，不是嗜伊紅性白血球增多本身；錯誤為 1、3，標準答案為 B。

【選項詳解】
- A. 僅 1、2 錯誤不對。第 2 點「重度感染加上鐵攝取不足會造成缺鐵性貧血」是鉤蟲吸血的典型後果，不能列為錯誤。
- B. 僅 1、3 錯誤正確。A. duodenale 可經皮膚，也可經口感染；早期可見穿皮處搔癢性皮膚炎，嗜伊紅性白血球增多是實驗室變化，不是最早症狀。
- C. 僅 2、3 錯誤不對，因為第 2 點是正確敘述；鉤蟲重度感染會導致慢性腸道失血與鐵缺乏。
- D. 1、2、3 全錯不對。第 2 點保留了鉤蟲感染最重要的臨床危害，也就是缺鐵性貧血。

【核心考點】
A. duodenale 可經皮膚或口腔感染；鉤蟲病的重點是穿皮早期皮膚症狀與腸道吸血造成缺鐵性貧血。`,
    key_point: "十二指腸鉤蟲可經皮膚或口腔感染；鉤蟲重度感染會造成慢性失血與缺鐵性貧血。",
    flashcard_front: "鉤蟲感染的感染途徑與主要臨床後果是什麼？",
    flashcard_back: "A. duodenale 可經皮膚或口腔感染；重度感染因腸道吸血造成慢性失血，導致缺鐵性貧血。早期臨床可有穿皮處皮膚炎。",
    flashcard_summary: "鉤蟲感染：十二指腸鉤蟲不只經皮膚；重度感染會缺鐵性貧血。",
  },
  31: {
    explanation: `【題幹解析】
本題問哪一種寄生蟲感染不會造成腦部病變。日本血吸蟲卵、豬肉絛蟲囊尾蚴與包蟲病都可能侵犯中樞神經；棘口吸蟲主要寄生腸道，不是造成腦病變的典型寄生蟲，標準答案為 D。

【選項詳解】
- A. 日本血吸蟲錯在可發生異位蟲卵沉積，累及腦部時可造成肉芽腫、癲癇或局灶神經症狀，因此不能選。
- B. 豬肉絛蟲錯在其囊尾蚴可造成神經囊蟲病 (neurocysticercosis)，是寄生蟲性腦病變的重要考點。
- C. 單胞絛蟲 (Echinococcus granulosus) 錯在包蟲囊腫雖以肝、肺常見，但也可能發生於腦部造成佔位病灶。
- D. 棘口吸蟲正確。Echinostoma spp. 是腸道吸蟲，感染主要造成腸胃道症狀，並非典型腦部病變寄生蟲。

【核心考點】
寄生蟲腦病變常考 Taenia solium 神經囊蟲病、Echinococcus 腦包蟲囊腫與 Schistosoma japonicum 異位蟲卵；Echinostoma 主要是腸道吸蟲。`,
    key_point: "Echinostoma spp. 主要造成腸道感染，不是典型腦部病變寄生蟲。",
    flashcard_front: "哪些寄生蟲常與腦部病變相關？Echinostoma 的主要感染部位是什麼？",
    flashcard_back: "Taenia solium 可造成神經囊蟲病；Echinococcus 可造成腦包蟲囊腫；Schistosoma japonicum 蟲卵可異位至腦部。Echinostoma 主要寄生腸道。",
    flashcard_summary: "寄生蟲腦病變：豬肉絛蟲、包蟲與日本血吸蟲可累及腦；棘口吸蟲偏腸道。",
  },
  32: {
    explanation: `【題幹解析】
本題考絛蟲蟲卵形態。廣節裂頭絛蟲的蟲卵具有卵蓋，是在絛蟲中很常被拿來與吸蟲卵混淆的特徵，標準答案為 C。

【選項詳解】
- A. 單胞絛蟲 (Echinococcus granulosus) 蟲卵外觀與 Taenia 類似，具有放射狀條紋胚膜，不是卵蓋卵。
- B. 牛肉絛蟲 (Taenia saginata) 蟲卵沒有卵蓋，常見特徵是厚殼與放射狀條紋，形態上難與豬肉絛蟲卵區分。
- C. 廣節裂頭絛蟲 (Diphyllobothrium latum) 正確。其蟲卵呈橢圓形、具卵蓋，另一端可有小突起，這點與多數絛蟲不同。
- D. 短小包膜絛蟲 (Hymenolepis nana) 蟲卵有極絲 (polar filaments) 等特徵，不是卵蓋卵。

【核心考點】
絛蟲卵中，Diphyllobothrium latum 具卵蓋；Taenia 與 Echinococcus 類蟲卵偏放射狀條紋，H. nana 要記極絲。`,
    key_point: "廣節裂頭絛蟲蟲卵具有卵蓋，是多數絛蟲卵中需特別記住的例外特徵。",
    flashcard_front: "哪一種絛蟲蟲卵具有卵蓋？Hymenolepis nana 蟲卵有什麼特徵？",
    flashcard_back: "Diphyllobothrium latum 蟲卵具有卵蓋；Hymenolepis nana 蟲卵常見極絲 (polar filaments)。",
    flashcard_summary: "絛蟲卵形態：廣節裂頭絛蟲有卵蓋；短小包膜絛蟲有極絲。",
  },
  33: {
    explanation: `【題幹解析】
本題問寄生蟲地理分布與臨床敘述何者錯誤。岡比亞錐蟲偏西非、中非，羅得西亞錐蟲偏東非、南部非洲；把兩者說成同時分布於蘇丹境內是本題不正確敘述，標準答案為 A。

【選項詳解】
- A. 錯誤。T. b. gambiense 與 T. b. rhodesiense 有不同地理分布與流行型態；前者偏西非、中非慢性病程，後者偏東非、南部非洲急性病程，不能簡化成蘇丹境內兩者同時分布。
- B. 正確。黑熱病治療後可能出現 post-kala-azar dermal leishmaniasis，病原仍與原先利什曼原蟲感染相關，可在皮膚產生病灶。
- C. 正確。枯西氏錐蟲 (T. cruzi) 雖以拉丁美洲查加斯病最典型，美國也曾報告本土感染病例，與錐蝽媒介及動物宿主有關。
- D. 正確。前往東非野生動物保護區旅遊者可因采采蠅叮咬感染 T. b. rhodesiense，病程常較急。

【核心考點】
非洲錐蟲要分清 gambiense 與 rhodesiense 的地理與病程；黑熱病治療後皮膚病灶則是 post-kala-azar dermal leishmaniasis。`,
    key_point: "T. b. gambiense 偏西非、中非慢性病程；T. b. rhodesiense 偏東非、南部非洲急性病程。",
    flashcard_front: "T. b. gambiense 與 T. b. rhodesiense 在地理分布與病程上如何區分？",
    flashcard_back: "T. b. gambiense：西非/中非，較慢性。T. b. rhodesiense：東非/南部非洲，較急性，常與野生動物保護區旅遊史相關。",
    flashcard_summary: "非洲錐蟲分布：gambiense 偏西/中非慢性；rhodesiense 偏東/南非急性。",
  },
  34: {
    explanation: `【題幹解析】
本題要找病症與病原蟲配對錯誤者。Megaesophagus 是查加斯病的慢性消化道表現，病原是枯西氏錐蟲，不是杜氏利什曼原蟲，標準答案為 C。

【選項詳解】
- A. Romaña's sign 與枯西氏錐蟲正確配對。這是查加斯病急性感染時眼周腫脹的經典表現，常與錐蝽糞便污染黏膜有關。
- B. Winterbottom's sign 與岡比亞錐蟲正確配對，指後頸部淋巴結腫大，常見於非洲睡眠病。
- C. Megaesophagus 配杜氏利什曼原蟲錯誤。巨食道來自 T. cruzi 破壞腸壁自主神經叢，是慢性查加斯病的消化道併發症。
- D. Espundia 與巴西利什曼原蟲正確配對，屬黏膜皮膚型利什曼病，可侵犯鼻咽口腔黏膜。

【核心考點】
Romaña sign 與 megaesophagus 都連到 T. cruzi；Winterbottom sign 連到非洲錐蟲；Espundia 連到 L. braziliensis。`,
    key_point: "Megaesophagus 是 T. cruzi 慢性查加斯病表現，不是 Leishmania donovani。",
    flashcard_front: "Romaña sign、Winterbottom sign、megaesophagus、Espundia 分別對應哪些寄生蟲？",
    flashcard_back: "Romaña sign：T. cruzi；Winterbottom sign：T. b. gambiense；megaesophagus：T. cruzi；Espundia：L. braziliensis。",
    flashcard_summary: "寄生蟲臨床配對：巨食道屬查加斯病 T. cruzi，Espundia 屬 L. braziliensis。",
  },
  35: {
    explanation: `【題幹解析】
巴貝氏原蟲感染紅血球，臨床從無症狀到類瘧疾發燒溶血皆可見。重症與高寄生蟲血症特別常見於脾臟切除、免疫低下或高齡患者；把「無症狀感染」說成常有高度寄生蟲血症並不合理，標準答案為 B。

【選項詳解】
- A. 正確。Babesia 主要寄生在紅血球內，血液抹片可見環狀體，偶可見 Maltese cross 形態。
- B. 錯誤。無症狀感染通常寄生蟲量低或臨床表現輕；高度寄生蟲血症多提示重症風險，尤其在無脾或免疫低下者。
- C. 正確。脾臟負責清除受感染紅血球，脾臟切除病人較容易出現嚴重溶血、高寄生蟲血症與死亡。
- D. 正確。診斷可用血液抹片觀察紅血球內蟲體，也可用血清免疫螢光抗體試驗或分子檢測輔助。

【核心考點】
Babesia 是蜱媒介、寄生紅血球的原蟲；無脾患者重症風險高，診斷重點是血液抹片與血清/分子檢測。`,
    key_point: "Babesia 寄生紅血球；高度寄生蟲血症與重症多見於無脾或免疫低下者，而非一般無症狀感染。",
    flashcard_front: "人類巴貝氏原蟲病的感染位置、重症危險因子與診斷方式是什麼？",
    flashcard_back: "感染紅血球；無脾、免疫低下與高齡者易重症；診斷可用血液抹片、IFA 或 PCR。",
    flashcard_summary: "Babesia：紅血球內原蟲，蜱媒介；無脾者易高寄生蟲血症與重症。",
  },
  36: {
    explanation: `【題幹解析】
型一錯誤是「虛無假說其實為真，卻被檢定錯誤拒絕」，也就是假陽性。若兩組實際無差異，分析結果卻推翻虛無假說，就是型一錯誤，標準答案為 A。

【選項詳解】
- A. 正確。兩組實際上無差異代表 H0 為真；檢定卻拒絕 H0，就是把不存在的差異判成有差異，屬 type I error。
- B. 兩組實際無差異且分析支持虛無假說，是正確不拒絕 H0，不是錯誤。
- C. 兩組實際有差異且分析推翻虛無假說，是正確拒絕 H0，屬檢定成功偵測到差異。
- D. 兩組實際有差異但分析支持虛無假說，是型二錯誤 (type II error)，也就是假陰性。

【核心考點】
Type I error = false positive = H0 真的卻拒絕 H0；Type II error = false negative = H0 假的卻未拒絕 H0。`,
    key_point: "型一錯誤是虛無假說為真時卻拒絕虛無假說，也就是假陽性。",
    flashcard_front: "Type I error 與 Type II error 分別代表什麼？",
    flashcard_back: "Type I error：H0 為真卻拒絕 H0，假陽性。Type II error：H0 為假卻未拒絕 H0，假陰性。",
    flashcard_summary: "假說檢定錯誤：Type I 是假陽性；Type II 是假陰性。",
  },
  37: {
    explanation: `【題幹解析】
單尾與雙尾檢定的差別在於替代假說方向與拒絕區分配，不是顯著水準本身必須不同。研究者可同樣設定 α = 0.05；單尾把拒絕區放在一側，雙尾則分到兩側，標準答案為 C。

【選項詳解】
- A. 錯誤。單尾與雙尾的 p 值計算不同；在對稱分布且同一方向效果時，雙尾 p 值常約為單尾的兩倍。
- B. 錯誤。在效果方向符合預先指定方向時，單尾檢定把 α 集中在一側，通常比雙尾更容易拒絕虛無假說。
- C. 正確。顯著水準 α 可設為相同總量，例如都用 0.05；差別是雙尾將 α 分配到兩端，單尾集中於一端。
- D. 錯誤。實務與考試中較常使用雙尾檢定，因為多數研究需偵測任一方向的差異，單尾檢定須事先有明確方向性理由。

【核心考點】
單尾檢定必須在分析前明確指定方向；與雙尾檢定可用相同總 α，但拒絕區配置與 p 值算法不同。`,
    key_point: "單尾與雙尾檢定可設定相同總 α；差別在拒絕區方向與 p 值計算。",
    flashcard_front: "單尾檢定與雙尾檢定在 α、拒絕區與 p 值上有何差異？",
    flashcard_back: "總 α 可相同；單尾拒絕區集中一側，雙尾分於兩側；同方向效果下雙尾 p 值通常大於單尾 p 值。",
    flashcard_summary: "單尾 vs 雙尾：總 α 可相同，但拒絕區與 p 值計算不同。",
  },
  38: {
    explanation: `【題幹解析】
簡單線性迴歸斜率 b 與 Pearson 相關係數 r 的符號相同，但代表意義不同。r 不受 X、Y 角色互換影響；斜率 b 會因誰當反應變項而改變，標準答案為 D。

【選項詳解】
- A. 正確。大的 |b| 或 |r| 只表示線性關聯強或斜率大，觀察性資料本身不能證明 X 對 Y 有因果效果。
- B. 正確。Pearson 相關係數 r 的範圍固定在 -1 到 1 之間。
- C. 正確。在以 Y 對 X 做簡單線性迴歸時，斜率 b = r × SD(Y)/SD(X)，因此 b 與 r 必定同正或同負。
- D. 錯誤。X 與 Y 角色互換時，r 仍相同，但迴歸斜率會變成 r × SD(X)/SD(Y)，通常不會與原本 b 相同。

【核心考點】
Pearson r 對 X、Y 互換對稱；線性迴歸斜率不對稱，會受反應變項與解釋變項的尺度影響。`,
    key_point: "Pearson r 在 X/Y 互換後不變，但迴歸斜率 b 會隨反應變項與解釋變項角色改變。",
    flashcard_front: "簡單線性迴歸斜率 b 與 Pearson r 的關係是什麼？X/Y 互換時何者會改變？",
    flashcard_back: "b = r × SD(Y)/SD(X)，所以 b 與 r 同號；X/Y 互換時 r 不變，但斜率通常改變。",
    flashcard_summary: "迴歸與相關：r 對稱且介於 -1 到 1；b 不對稱且受尺度影響。",
  },
  40: {
    explanation: `【題幹解析】
病例對照研究中吸菸與疾病通常整理成 2×2 類別資料。若列聯表樣本數小或有期望值偏小的格子，應用 Fisher's exact test 比一般卡方近似更合適，標準答案為 D。

【選項詳解】
- A. 獨立 t 檢定用於比較兩組連續變項平均值，例如血壓或膽固醇平均值，不適合檢定吸菸/不吸菸與有病/無病這種分類資料。
- B. 配對 t 檢定用於同一人前後測或配對連續資料，本題不是連續型配對差值。
- C. McNemar 卡方檢定用於配對的二元分類資料，例如同一受試者治療前後陽性/陰性變化；一般未配對病例對照 2×2 表不首選它。
- D. Fisher's exact test 正確。它直接計算小樣本 2×2 列聯表的精確機率，適合期望值過小時檢定兩類別變項是否相關。

【核心考點】
小樣本或期望值小於 5 的 2×2 類別資料優先想到 Fisher's exact test；t 檢定處理連續資料，McNemar 處理配對二元資料。`,
    key_point: "小樣本 2×2 分類資料或期望值偏小時，適合使用 Fisher's exact test。",
    flashcard_front: "病例對照研究的 2×2 列聯表若樣本數小，應使用哪一種檢定？",
    flashcard_back: "Fisher's exact test。它適合小樣本或期望值偏小的未配對二元分類資料。",
    flashcard_summary: "統計檢定選擇：小樣本 2×2 類別資料用 Fisher exact test。",
  },
  41: {
    explanation: `【題幹解析】
本題有官方更正，B 與 D 都列為給分答案。若兩地每一個年齡層的年齡別死亡率完全相同，套用同一組標準人口後，年齡標準化死亡率必定相同；兩地標準化率差異也會維持為 0，不受標準人口組成改變影響。

【選項詳解】
- A. 錯誤。粗死亡率會受人口年齡結構影響；即使每個年齡層死亡率相同，老年人口比例較高的地區粗死亡率仍可能較高。
- B. 正確且為官方給分答案。年齡標準化是把各年齡層死亡率套到同一標準人口，因此年齡別死亡率完全相同時，標準化死亡率必定相同。
- C. 錯誤。若甲地人口比乙地老化，在年齡別死亡率相同下，甲地粗死亡率通常會較高，不會「必小於」乙地。
- D. 正確且為官方給分答案。因兩地每一層年齡別死亡率都相同，不論採用哪一組標準人口，兩地標準化率的差異都會是 0。

【核心考點】
粗死亡率受年齡結構影響；年齡標準化死亡率用同一標準人口消除年齡結構差異。本題官方接受 B、D。`,
    key_point: "年齡別死亡率完全相同時，兩地年齡標準化死亡率相同；本題官方更正接受 B、D。",
    flashcard_front: "若兩地各年齡層年齡別死亡率完全相同，粗死亡率與年齡標準化死亡率如何判斷？",
    flashcard_back: "粗死亡率仍會受年齡結構影響；年齡標準化死亡率在同一標準人口下必相同。本題官方更正 B、D 皆給分。",
    flashcard_summary: "死亡率標準化：年齡別率相同則標準化率相同；粗死亡率仍受人口老化影響。",
  },
  42: {
    explanation: `【題幹解析】
粒狀污染物是懸浮在空氣中的固體或液滴，例如煙、霧、粉塵、油煙。揮發性有機物 (VOCs) 主要以氣態存在，屬氣態污染物，不是粒狀污染物，標準答案為 D。

【選項詳解】
- A. 黑煙 (soot) 是燃燒後產生的碳質細小顆粒，屬粒狀污染物。
- B. 酸霧 (acid mist) 是液滴氣膠，雖然成分為酸性液體，但在空氣污染分類上仍屬粒狀或氣膠污染物。
- C. 油煙 (oil smoke) 包含燃燒或烹調產生的細小液滴與顆粒，屬粒狀污染物。
- D. 揮發性有機物 (VOCs) 正確。VOCs 如苯、甲苯等主要是氣態化學污染物，不歸類為粒狀污染物。

【核心考點】
空污分類要分「顆粒/氣膠」與「氣體」：soot、mist、smoke 是粒狀；VOCs、SO2、NOx、CO 常歸為氣態污染物。`,
    key_point: "VOCs 屬氣態污染物；黑煙、酸霧、油煙屬粒狀或氣膠污染物。",
    flashcard_front: "黑煙、酸霧、油煙與 VOCs 中，何者不是粒狀污染物？",
    flashcard_back: "VOCs。黑煙、酸霧與油煙可視為粒狀/氣膠污染物；VOCs 主要是氣態污染物。",
    flashcard_summary: "空污分類：VOCs 是氣態污染物，不是粒狀污染物。",
  },
  43: {
    explanation: `【題幹解析】
危害商數 (hazard quotient, HQ) 是將估計暴露量與參考劑量或容許暴露值相除，用來描述非致癌健康風險是否可能超過可接受範圍。這是在整合危害、劑量反應與暴露資訊後的風險特徵描述，標準答案為 D。

【選項詳解】
- A. 危害辨識是在判斷某物質是否具有造成不良健康效應的能力，尚未計算 HQ。
- B. 劑量反應評估是在建立暴露劑量與健康效應間的關係，例如推估參考劑量；HQ 會使用這個結果，但不屬於此步驟本身。
- C. 暴露評估是在估計族群接觸污染物的濃度、頻率與劑量；它提供 HQ 的分子資料，但不是 HQ 的主要使用步驟。
- D. 風險特徵描述正確。HQ = 暴露量 / 參考劑量，常用來總結非致癌風險，HQ 大於 1 代表可能有健康疑慮。

【核心考點】
健康風險評估四步驟中，hazard quotient 用於風險特徵描述；它把暴露評估與劑量反應評估整合成可判讀的風險指標。`,
    key_point: "Hazard quotient 用於風險特徵描述，常以暴露量除以參考劑量判斷非致癌風險。",
    flashcard_front: "Hazard quotient (HQ) 在健康風險評估四步驟中屬於哪一步？公式概念是什麼？",
    flashcard_back: "屬於風險特徵描述。HQ = 暴露量 / 參考劑量；HQ > 1 表示可能有非致癌健康風險。",
    flashcard_summary: "風險評估：HQ 是風險特徵描述指標，整合暴露量與參考劑量。",
  },
  44: {
    explanation: `【題幹解析】
整體換氣系統主要用於一般空間空氣交換，例如稀釋污染物、控制溫度與濕度。工作環境氣壓的精密調整通常需要專門空調壓差設計，不是一般整體換氣最適合處理的目的，標準答案為 D。

【選項詳解】
- A. 保持濕度可透過整體空調與換氣系統協助控制，因此不是最不適合的項目。
- B. 稀釋污染物濃度是整體換氣的典型用途，尤其是低毒性、低濃度且污染源分散時。
- C. 降低工作環境溫度可藉通風或空調達成，也是整體換氣常見功能之一。
- D. 調整工作環境氣壓正確。壓差控制需要特定送排風平衡與空調設計，例如負壓隔離室或潔淨室，不宜只用一般整體換氣概念處理。

【核心考點】
整體換氣適合稀釋分散污染物與調節溫濕度；高毒性源頭控制用局部排氣，精密壓差控制則需專門 HVAC 設計。`,
    key_point: "整體換氣適合稀釋污染物與調節溫濕度；氣壓壓差控制需專門空調設計。",
    flashcard_front: "整體換氣系統適合處理哪些工作環境問題？哪一類需求較不適合？",
    flashcard_back: "適合稀釋污染物、控制溫度與濕度；較不適合精密調整工作環境氣壓或壓差。",
    flashcard_summary: "工業衛生換氣：整體換氣管稀釋與溫濕度，不是精密壓差控制。",
  },
  45: {
    explanation: `【題幹解析】
臺灣中部油症事件是食用米糠油受到多氯聯苯及相關污染物污染所造成的重大公害事件。題目選項中最直接對應的暴露物質是多氯聯苯，標準答案為 B。

【選項詳解】
- A. 靈丹 (lindane) 是有機氯殺蟲劑，可造成神經毒性等問題，但不是臺灣油症事件的代表污染物。
- B. 多氯聯苯 (PCB) 正確。油症事件與受污染米糠油中的 PCB/相關氯化污染物暴露有關，患者可出現氯痤瘡、色素沉著、眼分泌物增加等表現。
- C. 甲苯 (toluene) 是有機溶劑，常考職業暴露與中樞神經抑制，不是油症事件原因。
- D. 有機汞 (organic mercury) 典型連到水俁病等甲基汞污染造成的神經毒性，不是臺灣油症事件主因。

【核心考點】
臺灣油症事件要連到米糠油污染與 PCB；水俁病連到有機汞，兩者是公衛公害史常見對照。`,
    key_point: "臺灣油症事件主要與受污染米糠油中的 PCB 暴露有關。",
    flashcard_front: "臺灣油症事件與哪一類污染物暴露有關？它常與哪個公害事件作對照？",
    flashcard_back: "油症事件：PCB/相關氯化污染物污染米糠油。對照：水俁病與有機汞污染。",
    flashcard_summary: "公害事件：臺灣油症是 PCB 污染米糠油；水俁病是有機汞。",
  },
  46: {
    explanation: `【題幹解析】
職業性肺結核認定需要比較就職前健康狀態、工作暴露風險、感染時序與臨床證據。員工就職時胸部 X 光可作為後續判斷是否新發病變的重要基準，標準答案為 A。

【選項詳解】
- A. 正確。就職時胸部 X 光能提供基線資料，若日後出現肺結核，可協助判斷是否為在職期間新發感染或病灶惡化。
- B. 錯誤。法定傳染病身分不排除職業病認定；若符合工作相關暴露與認定條件，仍可能涉及職業病與相關給付。
- C. 錯誤。醫院內不同部門接觸開放性肺結核病人的機會不同，感染風險不會完全相同，例如胸腔、急診、負壓隔離或檢驗相關工作風險較高。
- D. 錯誤。醫護人員得到肺結核不必然都是職業病，仍需依暴露史、基線資料、群聚或分子流行病學等證據判斷工作相關性。

【核心考點】
職業性肺結核認定重點是基線健康資料、工作暴露機會與發病時序；不能因為是醫護人員或法定傳染病就自動肯定或否定。`,
    key_point: "職業性肺結核需依基線胸部 X 光、工作暴露與發病時序判斷。",
    flashcard_front: "醫護人員職業性肺結核認定時，就職時胸部 X 光有何用途？",
    flashcard_back: "作為基線比較資料，協助判斷後續肺結核是否為在職期間新發或與工作暴露相關。",
    flashcard_summary: "職業性肺結核：看基線胸片、暴露風險與時序，不是醫護確診就自動算職業病。",
  },
  48: {
    explanation: `【題幹解析】
題幹問的是衛生計畫執行過程中的參與率、資源運用與執行者投入，這些都是計畫是否照預定方式被執行的問題，屬過程評價，標準答案為 A。

【選項詳解】
- A. 過程評價正確。它檢查計畫執行品質、活動覆蓋率、參與率、人力與資源使用情形，回答「做得是否到位」。
- B. 結果評價重點是最終健康結果或目標是否達成，例如發生率、死亡率、血壓控制率改變，不是執行過程監測。
- C. 衝擊評價多看較短中期的行為、知識、態度或環境改變，例如戒菸意圖或運動習慣提升，與資源投入檢核不同。
- D. 形式評價常在計畫正式推行前用來了解需求、可行性或設計是否合適，不是評估執行中參與率與資源使用。

【核心考點】
計畫評價常分形式、過程、衝擊、結果：執行過程與資源使用屬過程評價；健康結局才是結果評價。`,
    key_point: "參與率、資源運用與執行者投入屬衛生計畫的過程評價。",
    flashcard_front: "衛生計畫評價中，檢查參與率、資源運用與執行者投入屬哪一類評價？",
    flashcard_back: "過程評價。它回答計畫是否依預定方式執行、資源與活動覆蓋是否到位。",
    flashcard_summary: "衛生計畫評價：執行品質與資源使用是過程評價。",
  },
  49: {
    explanation: `【題幹解析】
醫院整體策略可包含成長、穩定、緊縮與混合策略。垂直整合是向供應鏈上下游延伸服務或控制資源，通常屬成長策略，不是穩定策略，因此標準答案為 B。

【選項詳解】
- A. 正確。整體策略可依組織發展方向分為成長、穩定、緊縮與混合策略。
- B. 錯誤。垂直整合是擴張到上游或下游，例如醫院整合診所、長照、檢驗或供應鏈，屬成長策略的一種。
- C. 正確。作業流程再造與合理化可在不大幅擴張規模下提升效率與維持營運，較可歸入穩定或改善既有運作的策略方向。
- D. 正確。混合策略可讓不同部門採不同方向，例如某科擴張服務、另一科縮減或整併。

【核心考點】
垂直整合、水平整合與多角化多屬成長策略；穩定策略重點是維持既有服務並改善效率。`,
    key_point: "垂直整合屬成長策略，不是穩定策略。",
    flashcard_front: "醫院策略中，垂直整合通常歸於哪一類整體策略？",
    flashcard_back: "成長策略。垂直整合代表向上游或下游延伸與整合服務/資源。",
    flashcard_summary: "醫院策略：垂直整合是成長策略；流程合理化偏穩定與效率改善。",
  },
  50: {
    explanation: `【題幹解析】
新藥上市前的第三期臨床試驗通常納入約數百到數千名病人，重點是確認療效、常見副作用與與標準治療比較。題幹的 1000 到 3000 名受試者最符合第三期，標準答案為 B。

【選項詳解】
- A. 第四期是在藥物上市後進行的上市後監測，重點是長期安全性、罕見副作用與真實世界效果。
- B. 第三期正確。Phase III 是上市前大型病人試驗，常見規模為 1000 到 3000 人或更多，用來支持核准上市。
- C. 第二期通常人數較少，重點是初步療效、劑量範圍與短期安全性，多在數十到數百名病人。
- D. 第一期多在少數健康志願者或特定病人中評估安全性、耐受性與藥物動力學，規模最小。

【核心考點】
臨床試驗分期：Phase I 安全/藥動；Phase II 初步療效與劑量；Phase III 大型上市前確認；Phase IV 上市後監測。`,
    key_point: "1000-3000 名受試者的上市前大型臨床試驗屬第三期臨床試驗。",
    flashcard_front: "新藥臨床試驗 Phase I-IV 的重點如何快速區分？",
    flashcard_back: "Phase I：安全與藥動；Phase II：初步療效與劑量；Phase III：上市前大型確認試驗；Phase IV：上市後監測。",
    flashcard_summary: "臨床試驗分期：1000-3000 人上市前大型試驗是 Phase III。",
  },
  51: {
    explanation: `【題幹解析】
題幹描述旅行後腹瀉且懷疑革蘭氏陰性桿菌感染，傳統藥理考點會選對腸道革蘭氏陰性菌有效的 fluoroquinolone。Levofloxacin 是四個選項中最合理的治療選擇，標準答案為 A。

【選項詳解】
- A. Levofloxacin 正確。它是 fluoroquinolone，可抑制 DNA gyrase/topoisomerase，對多種腸道革蘭氏陰性桿菌有活性，傳統上可用於旅行者腹瀉。
- B. Sulfacetamide 主要作為局部眼科磺胺類用藥，不是旅行者腹瀉的首選全身性治療。
- C. Trimethoprim 單方抗菌範圍與臨床使用情境不如 fluoroquinolone 符合本題；常見組合是 TMP-SMX，但本題選項不是首選。
- D. Vancomycin 主要針對革蘭氏陽性菌，口服時用於困難梭菌腸炎，對一般革蘭氏陰性旅行者腹瀉不適合。

【核心考點】
傳統考題中旅行者腹瀉若指向革蘭氏陰性桿菌，fluoroquinolone 是常考答案；實務用藥仍需考慮地區抗藥性、發燒血便與病人風險。`,
    key_point: "旅行者腹瀉傳統藥理考點中，疑似革蘭氏陰性桿菌感染可選 fluoroquinolone，如 levofloxacin。",
    flashcard_front: "旅行者腹瀉若疑似革蘭氏陰性桿菌感染，傳統藥理考題常選哪類抗生素？",
    flashcard_back: "Fluoroquinolone，例如 levofloxacin；但臨床實務須依地區抗藥性與病情調整。",
    flashcard_summary: "旅行者腹瀉：傳統考點選 fluoroquinolone；vancomycin 偏革蘭陽性/困難梭菌。",
    manual_review_notes: ["旅行者腹瀉實務用藥會受地區抗藥性與侵襲性症狀影響；本題依 108 年藥理考點保留 fluoroquinolone。"],
  },
  52: {
    explanation: `【題幹解析】
藥物塗層冠狀動脈支架要抑制血管平滑肌細胞增生，避免再狹窄。Sirolimus 又稱 rapamycin，是 mTOR 抑制劑，能抑制細胞週期進展與增生，標準答案為 C。

【選項詳解】
- A. Cyclosporine 抑制 calcineurin，降低 T 細胞 IL-2 轉錄，主要用於移植與免疫疾病，不是典型冠狀動脈支架塗層抗增生藥。
- B. Tacrolimus (FK506) 也抑制 calcineurin，免疫抑制用途類似 cyclosporine，並非本題支架再狹窄常考藥物。
- C. Sirolimus (rapamycin) 正確。它抑制 mTOR，阻止 T 細胞與血管平滑肌細胞由 G1 進入 S 期，可降低支架內再狹窄。
- D. Azathioprine 是嘌呤合成抑制劑，抑制淋巴球增殖，但不是藥物塗層支架的代表藥物。

【核心考點】
Sirolimus/rapamycin 是 mTOR 抑制劑，可抑制細胞增生，因此可用於藥物塗層支架防止再狹窄。`,
    key_point: "Sirolimus 抑制 mTOR 與平滑肌細胞增生，可用於藥物塗層支架降低再狹窄。",
    flashcard_front: "哪一種免疫抑制劑可用於冠狀動脈藥物塗層支架以防止再狹窄？機轉是什麼？",
    flashcard_back: "Sirolimus (rapamycin)。它抑制 mTOR，阻止細胞週期進展與平滑肌細胞增生。",
    flashcard_summary: "支架再狹窄：sirolimus/rapamycin 抑制 mTOR 與細胞增生。",
  },
  54: {
    explanation: `【題幹解析】
遠端彎曲小管早段的 Na+/Cl- cotransporter 是 thiazide 類利尿劑的主要作用標的。題目問抑制 distal convoluted tubule Na+/Cl- transporter 的藥物，標準答案為 C。

【選項詳解】
- A. Acetazolamide 是碳酸酐酶抑制劑，主要作用在近端小管，增加 bicarbonate 排出，不是 DCT 的 Na+/Cl- cotransporter。
- B. Triamterene 是保鉀利尿劑，作用在集尿管上皮鈉通道 (ENaC)，不是遠端彎曲小管 Na+/Cl- cotransporter。
- C. Thiazide 正確。Thiazide 抑制遠端彎曲小管 Na+/Cl- cotransporter，也會增加鈣再吸收，常用於高血壓。
- D. Bumetanide 是 loop diuretic，抑制亨利氏環上升支粗段的 Na+/K+/2Cl- cotransporter。

【核心考點】
利尿劑定位：acetazolamide 近端小管，loop 利尿劑 TAL，thiazide DCT 的 NCC，triamterene/amiloride 集尿管 ENaC。`,
    key_point: "Thiazide 抑制遠端彎曲小管 Na+/Cl- cotransporter。",
    flashcard_front: "Thiazide、loop diuretic、acetazolamide、triamterene 分別作用於哪個腎小管部位或轉運體？",
    flashcard_back: "Acetazolamide：近端小管 carbonic anhydrase；loop：TAL NKCC2；thiazide：DCT NCC；triamterene：集尿管 ENaC。",
    flashcard_summary: "利尿劑作用部位：thiazide 抑制 DCT 的 Na+/Cl- cotransporter。",
  },
  55: {
    explanation: `【題幹解析】
氣喘急性發作需要能迅速支氣管擴張的藥物；nedocromil 是肥大細胞穩定劑，只能預防發炎介質釋放，不能解除已經發生的急性支氣管痙攣，標準答案為 D。

【選項詳解】
- A. Albuterol 是短效 beta-2 agonist，可快速放鬆支氣管平滑肌，是急性氣喘症狀緩解藥。
- B. Theophylline 是 methylxanthine，可支氣管擴張，但治療窗窄、使用較受限；仍不是「只適合預防、發作無效」的代表。
- C. Salmeterol 是長效 beta-2 agonist，主要作維持治療並需搭配吸入型類固醇，不適合單獨急救，但其機轉仍是支氣管擴張。
- D. Nedocromil 正確。它穩定肥大細胞、減少發炎介質釋放，適合預防誘發性氣喘，急性發作時給藥無法快速逆轉支氣管收縮。

【核心考點】
急性氣喘緩解靠短效 beta-2 agonist；cromolyn/nedocromil 屬預防性肥大細胞穩定劑，不能當急救藥。`,
    key_point: "Nedocromil 是肥大細胞穩定劑，適合預防氣喘，不適合急性發作救急。",
    flashcard_front: "哪類氣喘藥只適合預防、不能用於急性發作？急性發作首選哪類藥？",
    flashcard_back: "Nedocromil/cromolyn 等肥大細胞穩定劑只適合預防；急性發作首選短效 beta-2 agonist，如 albuterol。",
    flashcard_summary: "氣喘用藥：nedocromil 預防用；albuterol 急性緩解用。",
  },
  56: {
    explanation: `【題幹解析】
偏頭痛用藥要分急性止痛與預防。Sumatriptan 與 dihydroergotamine 可治療急性偏頭痛，propranolol 可作預防；buspirone 是 5-HT1A 部分促效的抗焦慮藥，不是偏頭痛治療或預防標準藥，標準答案為 A。

【選項詳解】
- A. Buspirone 正確。它用於廣泛性焦慮症，沒有作為急性偏頭痛止痛或常規預防藥的角色。
- B. Sumatriptan 是 5-HT1B/1D agonist，可造成顱內血管收縮並抑制三叉神經胜肽釋放，是急性偏頭痛常用藥。
- C. Propranolol 是 beta blocker，可降低偏頭痛發作頻率，屬預防用藥而非急性止痛。
- D. Dihydroergotamine 是 ergot 類藥物，可用於急性偏頭痛，尤其部分難治或持續發作情境。

【核心考點】
急性偏頭痛可用 triptan 或 ergot 類；預防可用 propranolol、topiramate 等。Buspirone 是抗焦慮藥，不屬偏頭痛標準用藥。`,
    key_point: "Buspirone 是抗焦慮藥，不能作為急性偏頭痛治療或常規預防藥。",
    flashcard_front: "Sumatriptan、dihydroergotamine、propranolol、buspirone 在偏頭痛治療中如何區分？",
    flashcard_back: "Sumatriptan 與 dihydroergotamine 可治療急性偏頭痛；propranolol 可預防；buspirone 不屬偏頭痛治療/預防標準藥。",
    flashcard_summary: "偏頭痛用藥：triptan/ergot 急性治療，propranolol 預防，buspirone 不用於偏頭痛。",
  },
  57: {
    explanation: `【題幹解析】
乙醇主要在肝臟代謝，經 alcohol dehydrogenase 與 aldehyde dehydrogenase 生成乙醛與乙酸。乙醇相關病變嚴重度與肝臟代謝負荷、脂肪變性、酒精性肝炎與肝硬化最密切，標準答案為 D。

【選項詳解】
- A. 胰臟可受酒精影響而發生急性或慢性胰臟炎，但不是決定乙醇病變程度最核心的代謝器官。
- B. 心臟可出現酒精性心肌病變或心律不整，但乙醇毒性與代謝負荷的主要器官仍是肝臟。
- C. 肺臟不是乙醇代謝與慢性酒精病變的主要標的器官。
- D. 肝臟正確。肝臟是乙醇代謝中心，乙醛、NADH 增加與氧化壓力會造成脂肪肝、酒精性肝炎、纖維化與肝硬化。

【核心考點】
乙醇代謝主要在肝臟；酒精性肝病的連續變化包括脂肪肝、酒精性肝炎、纖維化與肝硬化。`,
    key_point: "乙醇主要由肝臟代謝，肝臟是酒精相關病變程度最重要的器官。",
    flashcard_front: "乙醇主要在哪個器官代謝？酒精性肝病可有哪些連續變化？",
    flashcard_back: "主要在肝臟代謝。酒精性肝病可由脂肪肝進展為酒精性肝炎、纖維化與肝硬化。",
    flashcard_summary: "酒精病變：肝臟是主要代謝與受損器官。",
  },
  60: {
    explanation: `【題幹解析】
本題考孕婦或新生兒相關抗生素禁忌的副作用配對。Sulfonamides 在新生兒可增加溶血與膽紅素相關風險，尤其 G6PD 缺乏者較易溶血；也可因膽紅素置換增加核黃疸疑慮，標準答案為 C。

【選項詳解】
- A. Erythromycin estolate 的典型問題是孕婦膽汁鬱積性肝炎風險，不是胎兒第八對腦神經受損；第八腦神經毒性常連到 aminoglycosides。
- B. Streptomycin 屬 aminoglycoside，主要擔心胎兒耳毒性與第八對腦神經損傷，不是嬰兒軟骨受損；軟骨問題較常考 fluoroquinolones。
- C. Sulfonamides 正確。磺胺類可造成 G6PD 缺乏者溶血，且接近分娩或新生兒使用時有膽紅素置換與核黃疸風險。
- D. Tetracycline 會沉積在胎兒牙齒與骨骼，造成牙齒變色與骨生長影響；灰嬰症候群是 chloramphenicol 的典型毒性。

【核心考點】
孕期抗生素副作用配對：aminoglycoside 耳毒性，tetracycline 牙齒/骨骼，chloramphenicol 灰嬰症候群，sulfonamide 溶血與核黃疸風險。`,
    key_point: "Sulfonamides 可造成 G6PD 缺乏者溶血，近分娩或新生兒使用有核黃疸風險。",
    flashcard_front: "孕期或新生兒相關抗生素禁忌中，sulfonamide、tetracycline、chloramphenicol、aminoglycoside 各連到什麼毒性？",
    flashcard_back: "Sulfonamide：G6PD 溶血/核黃疸；tetracycline：牙齒變色與骨生長；chloramphenicol：灰嬰症候群；aminoglycoside：耳毒性/第八腦神經。",
    flashcard_summary: "孕期抗生素副作用：磺胺溶血核黃疸，四環牙骨，chloramphenicol 灰嬰，aminoglycoside 耳毒。",
  },
  63: {
    explanation: `【題幹解析】
停經婦女低骨密度要想到原發性停經後骨鬆，也要辨識藥物造成的繼發性骨鬆。慢性使用 glucocorticoid 會抑制成骨、增加骨吸收並降低鈣平衡，prednisone 最可能造成骨質疏鬆，標準答案為 D。

【選項詳解】
- A. Lovastatin 是 HMG-CoA reductase inhibitor，主要用於降 LDL，不是慢性用藥造成骨質疏鬆的典型藥物。
- B. Metformin 是第一線第二型糖尿病用藥，主要作用是降低肝臟糖質新生，並非骨質疏鬆常見原因。
- C. Propranolol 是非選擇性 beta blocker，常用於高血壓、心律不整、偏頭痛預防等，不是典型造成骨鬆的慢性藥物。
- D. Prednisone 正確。長期 glucocorticoid 會抑制 osteoblast、促進 osteoclast 活性、減少腸鈣吸收並增加腎鈣流失，造成骨質疏鬆與骨折風險。

【核心考點】
長期全身性類固醇是繼發性骨質疏鬆的高風險原因；用藥時需評估鈣、維生素 D、骨密度與抗骨鬆治療需求。`,
    key_point: "長期 prednisone 等 glucocorticoid 使用會造成繼發性骨質疏鬆。",
    flashcard_front: "哪類慢性用藥最典型會造成繼發性骨質疏鬆？主要機轉是什麼？",
    flashcard_back: "長期 glucocorticoid，如 prednisone。機轉包括抑制成骨、增加骨吸收、降低腸鈣吸收與增加腎鈣流失。",
    flashcard_summary: "藥物性骨鬆：長期 glucocorticoid 是高風險原因。",
  },
  64: {
    explanation: `【題幹解析】
題幹有攝護腺腫大、PSA 上升、淋巴結與骨轉移線索，治療方向指向抑制雄性素訊號。Flutamide 是 androgen receptor antagonist，可用於攝護腺癌荷爾蒙治療，標準答案為 D。

【選項詳解】
- A. Oxandrolone 是合成同化性雄性素，會提供 androgenic/anabolic 作用，不適合治療依賴雄性素訊號的攝護腺腫瘤。
- B. Desogestrel 是 progestin 類避孕藥成分，不是轉移性攝護腺癌的典型抗雄性素治療。
- C. Anastrozole 是 aromatase inhibitor，主要用於雌激素受體陽性乳癌，作用是降低雌激素生成，不是本題最佳藥物。
- D. Flutamide 正確。它阻斷 androgen receptor，降低 testosterone/DHT 對攝護腺癌細胞的刺激，屬抗雄性素治療選項。

【核心考點】
攝護腺癌藥理治療常考抑制雄性素軸：GnRH 類藥、CYP17 抑制、5α-reductase 抑制或 androgen receptor antagonists；flutamide 是抗雄性素。`,
    key_point: "Flutamide 是 androgen receptor antagonist，可用於攝護腺癌抗雄性素治療。",
    flashcard_front: "Flutamide 的藥理分類與攝護腺癌治療角色是什麼？",
    flashcard_back: "Flutamide 是 androgen receptor antagonist，阻斷雄性素對攝護腺癌細胞的刺激。",
    flashcard_summary: "攝護腺癌：flutamide 抗雄性素，阻斷 androgen receptor。",
  },
  68: {
    explanation: `【題幹解析】
甲醇本身毒性較低，危險在於被 alcohol dehydrogenase 代謝成 formaldehyde 與 formic acid，造成視神經毒性與代謝性酸中毒。乙醇可競爭 alcohol dehydrogenase，減少毒性代謝物生成，標準答案為 B。

【選項詳解】
- A. 加速甲醇從腎臟排除不是乙醇治療的主要機制；嚴重中毒時可用血液透析移除甲醇與 formate。
- B. 抑制甲醇毒性代謝物產生正確。乙醇與 alcohol dehydrogenase 親和力較高，可競爭性抑制甲醇代謝，降低 formic acid 生成。
- C. 加速甲醇從肝臟代謝錯誤。若加速甲醇代謝，反而會增加 formaldehyde/formic acid，毒性更嚴重。
- D. 加速從呼吸道排除不是主要治療原理；甲醇不是靠呼氣排除作為治療核心。

【核心考點】
甲醇中毒治療重點是阻斷 alcohol dehydrogenase 產生 formic acid；乙醇與 fomepizole 都是利用這個酵素競爭或抑制原理。`,
    key_point: "乙醇治療甲醇中毒的機制是競爭 alcohol dehydrogenase，減少 formic acid 等毒性代謝物生成。",
    flashcard_front: "乙醇或 fomepizole 為何可治療甲醇中毒？",
    flashcard_back: "它們抑制或競爭 alcohol dehydrogenase，減少甲醇被代謝成 formaldehyde/formic acid，降低視神經毒性與酸中毒。",
    flashcard_summary: "甲醇中毒：毒性來自 formic acid；乙醇競爭 ADH 阻斷毒性代謝。",
  },
  69: {
    explanation: `【題幹解析】
鴉片類藥物作用於 μ 等 opioid receptors，可止痛、鎮咳、造成便秘、呼吸抑制與瞳孔縮小。抗痙攣不是 opioid 的典型作用，部分 opioid 反而可能降低癲癇閾值，標準答案為 A。

【選項詳解】
- A. 抗痙攣正確為本題所問「不是」。Opioids 不是抗癲癇或抗痙攣藥，meperidine 等藥物代謝物還可能誘發癲癇。
- B. 抑制咳嗽是 opioid 作用之一，例如 codeine 或 dextromethorphan 類似中樞鎮咳機制常被考。
- C. 便秘是 opioid 常見副作用，來自腸道蠕動下降與括約肌張力增加。
- D. 瞳孔縮小是 opioid 中毒典型表現之一，與副交感 Edinger-Westphal nucleus 作用相關。

【核心考點】
Opioid 典型作用：止痛、鎮咳、呼吸抑制、便秘、噁心、鎮靜與針尖瞳孔；不是抗痙攣藥。`,
    key_point: "Opioids 可鎮咳、便秘與縮瞳，但不是抗痙攣藥。",
    flashcard_front: "Opioid 的典型藥理作用與副作用有哪些？哪個不是典型作用？",
    flashcard_back: "典型作用包括止痛、鎮咳、呼吸抑制、便秘、鎮靜與瞳孔縮小；抗痙攣不是 opioid 作用。",
    flashcard_summary: "Opioid 作用：鎮痛鎮咳便秘縮瞳；不具抗痙攣作用。",
  },
  70: {
    explanation: `【題幹解析】
急性無機汞鹽中毒可用含巰基的螯合劑結合重金屬，常考藥物包括 dimercaprol、succimer 與 DMPS/unithiol。D-dimethylcysteine 不是標準治療螯合劑，標準答案為 D。

【選項詳解】
- A. Unithiol 可接受。它又稱 DMPS，是含巰基螯合劑，可用於某些重金屬中毒治療。
- B. Dimercaprol 可接受。BAL 含有巰基，可螯合砷、汞等重金屬，是傳統重金屬中毒治療藥。
- C. Succimer 可接受。DMSA 是口服螯合劑，可用於鉛中毒，也可用於汞等重金屬暴露情境。
- D. D-dimethylcysteine 錯誤。它不是急性無機汞鹽中毒的標準螯合治療藥物，不能與 BAL、DMSA、DMPS 混為一談。

【核心考點】
汞等重金屬中毒常用含巰基螯合劑：dimercaprol、succimer、unithiol/DMPS；看到非典型藥名要能排除。`,
    key_point: "無機汞鹽中毒可用 dimercaprol、succimer、unithiol/DMPS；D-dimethylcysteine 不是標準螯合劑。",
    flashcard_front: "急性無機汞鹽中毒常考哪些螯合劑？",
    flashcard_back: "Dimercaprol (BAL)、succimer (DMSA)、unithiol (DMPS)；D-dimethylcysteine 不是標準答案。",
    flashcard_summary: "重金屬螯合：汞中毒可用 BAL、DMSA、DMPS。",
  },
  73: {
    explanation: `【題幹解析】
題幹描述抗 PD-L1 單株抗體，藉由阻斷腫瘤細胞 PD-L1 與 T 細胞 PD-1 的抑制訊號，使 T 細胞恢復攻擊癌細胞。Atezolizumab 是抗 PD-L1 抗體，標準答案為 A。

【選項詳解】
- A. Atezolizumab 正確。它抑制 PD-L1，阻斷免疫檢查點訊號，提升 T 細胞抗腫瘤反應。
- B. Panitumumab 是抗 EGFR 單株抗體，主要用於特定 RAS wild-type 大腸直腸癌等，不是 PD-L1 抑制劑。
- C. Ramucirumab 是抗 VEGFR-2 單株抗體，主要抑制血管新生訊號，不是免疫檢查點藥物。
- D. Rituximab 是抗 CD20 單株抗體，用於 B 細胞淋巴瘤或某些自體免疫疾病，不是 PD-L1 抗體。

【核心考點】
免疫檢查點藥物要分靶點：atezolizumab 抗 PD-L1；nivolumab/pembrolizumab 抗 PD-1；rituximab 抗 CD20。`,
    key_point: "Atezolizumab 是抗 PD-L1 單株抗體，可解除 PD-1/PD-L1 對 T 細胞的抑制訊號。",
    flashcard_front: "Atezolizumab、panitumumab、ramucirumab、rituximab 分別靶向什麼？",
    flashcard_back: "Atezolizumab：PD-L1；panitumumab：EGFR；ramucirumab：VEGFR-2；rituximab：CD20。",
    flashcard_summary: "單株抗體靶點：atezolizumab 抗 PD-L1，活化抗腫瘤 T 細胞反應。",
  },
  75: {
    explanation: `【題幹解析】
Ezetimibe 降 LDL 的關鍵是抑制小腸刷狀緣的 NPC1L1 cholesterol transporter，減少飲食與膽汁膽固醇吸收。題目問作用標的，標準答案為 C。

【選項詳解】
- A. HMG-CoA reductase 是 statin 類藥物的標的，例如 atorvastatin、lovastatin；它抑制肝臟膽固醇合成，不是 ezetimibe。
- B. ApoB-100 是 LDL、VLDL 等脂蛋白結構蛋白，與 LDL receptor 結合有關，但不是 ezetimibe 的作用標的。
- C. Transport protein NPC1L1 正確。Ezetimibe 抑制腸上皮 NPC1L1，降低膽固醇吸收，使肝臟增加 LDL receptor 表現、降低血中 LDL。
- D. Microsomal triglyceride transfer protein (MTP) 是 lomitapide 等藥物的標的，影響 VLDL/乳糜微粒組裝，不是 ezetimibe。

【核心考點】
Ezetimibe = NPC1L1 inhibitor；statins = HMG-CoA reductase inhibitors；MTP inhibitor 另記 lomitapide。`,
    key_point: "Ezetimibe 抑制小腸 NPC1L1 transporter，減少膽固醇吸收並降低 LDL。",
    flashcard_front: "Ezetimibe 的作用標的是什麼？它和 statin 的機轉差在哪？",
    flashcard_back: "Ezetimibe 抑制腸道 NPC1L1，減少膽固醇吸收；statin 抑制肝臟 HMG-CoA reductase，減少膽固醇合成。",
    flashcard_summary: "降血脂機轉：ezetimibe 抑制 NPC1L1；statin 抑制 HMG-CoA reductase。",
  },
  76: {
    explanation: `【題幹解析】
骨化性肌炎是在肌肉或軟組織內形成成熟骨組織，屬於一種成熟細胞型態被另一種成熟細胞型態取代的適應性變化。這是化生，不是異生或增生，標準答案為 D。

【選項詳解】
- A. 異生 (dysplasia) 指上皮細胞出現排列混亂、大小形狀異常與核異型性，屬癌前變化概念，不是軟組織變成骨。
- B. 增生 (hyperplasia) 是細胞數目增加，例如荷爾蒙刺激造成組織變大；它不代表細胞種類改變成骨組織。
- C. 萎縮 (atrophy) 是細胞大小或數量下降，組織變小，與骨化性肌炎的新骨形成相反。
- D. 化生 (metaplasia) 正確。骨化性肌炎的骨頭組織是軟組織內形成骨性組織，屬異位骨化/骨性化生。

【核心考點】
化生是成熟細胞型態轉換成另一種成熟細胞型態；骨化性肌炎代表軟組織內骨性化生。`,
    key_point: "骨化性肌炎中的骨形成屬化生，也就是成熟組織型態轉換。",
    flashcard_front: "骨化性肌炎中的骨組織形成屬於異生、增生、萎縮還是化生？",
    flashcard_back: "化生 (metaplasia)。軟組織內形成骨組織，是成熟細胞/組織型態轉換。",
    flashcard_summary: "細胞適應：骨化性肌炎是骨性化生，不是 dysplasia。",
  },
  77: {
    explanation: `【題幹解析】
漿細胞內若堆積大量免疫球蛋白，會形成嗜伊紅、圓形的胞質內包涵體，稱為 Russell body。題幹已點出 plasma cell 與 immunoglobulin，標準答案為 A。

【選項詳解】
- A. Russell body 正確。它是漿細胞粗糙內質網內免疫球蛋白堆積形成的胞質內嗜伊紅包涵體。
- B. Amyloid 是細胞外不溶性蛋白沉積，剛果紅染色可見蘋果綠雙折光，不是漿細胞內免疫球蛋白包涵體。
- C. Mallory-Denk body 是肝細胞內受損中間絲堆積，常見於酒精性肝炎等肝病，不在漿細胞內。
- D. Psammoma body 是同心圓層狀鈣化，常見於乳突狀甲狀腺癌、漿液性乳突狀腫瘤、腦膜瘤等，不是免疫球蛋白堆積。

【核心考點】
Russell body = plasma cell 內免疫球蛋白堆積；Mallory-Denk = 肝細胞中間絲；psammoma = 層狀鈣化；amyloid = 細胞外蛋白沉積。`,
    key_point: "Russell body 是漿細胞內免疫球蛋白堆積形成的嗜伊紅包涵體。",
    flashcard_front: "Russell body、Mallory-Denk body、psammoma body、amyloid 分別代表什麼？",
    flashcard_back: "Russell：漿細胞內免疫球蛋白；Mallory-Denk：肝細胞中間絲；psammoma：層狀鈣化；amyloid：細胞外蛋白沉積。",
    flashcard_summary: "病理包涵體：漿細胞內 Ig 堆積是 Russell body。",
  },
  82: {
    explanation: `【題幹解析】
血栓閉塞性血管炎又稱 Buerger disease，幾乎都與吸菸高度相關，年輕男性吸菸者常見，早期戒菸可減緩惡化與降低截肢風險，標準答案為 C。

【選項詳解】
- A. Churg-Strauss syndrome 現稱 eosinophilic granulomatosis with polyangiitis，與氣喘、嗜酸性球增多和小血管炎相關，不是吸菸關聯最強者。
- B. 結節性多動脈炎 (polyarteritis nodosa) 是中小動脈壞死性血管炎，可與 B 型肝炎相關，但不是典型吸菸導致。
- C. 血栓閉塞性血管炎正確。它與菸草暴露關係極密切，影響四肢中小血管，戒菸是最重要的治療與預後因素。
- D. Henoch-Schönlein purpura 現稱 IgA vasculitis，與 IgA 免疫複合物沉積、紫斑、腹痛、關節痛與腎炎相關，不是吸菸相關血管炎。

【核心考點】
Buerger disease = thromboangiitis obliterans = 強烈吸菸相關；治療核心是完全戒菸。`,
    key_point: "血栓閉塞性血管炎 (Buerger disease) 與吸菸最密切，早期戒菸可減緩惡化。",
    flashcard_front: "哪一種血管炎與吸菸最密切，且戒菸是最重要治療？",
    flashcard_back: "血栓閉塞性血管炎 (thromboangiitis obliterans, Buerger disease)。",
    flashcard_summary: "血管炎：Buerger disease 強烈吸菸相關，戒菸最重要。",
  },
  87: {
    explanation: `【題幹解析】
急性氣管炎合併肺部瀰漫性間質發炎，病理型態較像病毒性或非典型感染造成的間質性肺炎。四個選項中病毒最符合此種瀰漫性間質發炎，標準答案為 A。

【選項詳解】
- A. 病毒正確。病毒性呼吸道感染常造成氣管支氣管炎與間質性肺炎，病理上以單核細胞浸潤、肺泡隔增厚等間質發炎為主。
- B. 肺炎雙球菌典型造成大葉性肺炎或肺泡腔內中性球與滲出物，較不是「瀰漫性間質發炎」的代表。
- C. 葡萄球菌肺炎常與壞死性肺炎、膿瘍或流感後細菌性肺炎有關，病理偏化膿性破壞，不是本題描述的首選。
- D. 黴菌感染型態依病原與免疫狀態而異，可造成肉芽腫或血管侵犯，但急性氣管炎合併瀰漫性間質發炎最典型仍是病毒。

【核心考點】
病毒性肺炎常呈間質性發炎；典型細菌性肺炎較偏肺泡腔中性球滲出與實變。`,
    key_point: "病毒感染最常造成急性氣管炎合併瀰漫性間質性肺炎型態。",
    flashcard_front: "瀰漫性間質性肺炎較常聯想到病毒、典型細菌、葡萄球菌還是黴菌？",
    flashcard_back: "病毒。病毒性肺炎常見肺泡隔單核細胞浸潤與間質發炎；典型細菌較偏肺泡腔滲出。",
    flashcard_summary: "肺炎病理：病毒偏間質性發炎；典型細菌偏肺泡滲出實變。",
  },
  89: {
    explanation: `【題幹解析】
酒精性肝炎典型表現包括 AST 高於 ALT、脂肪變性、Mallory-Denk bodies 與嗜中性球浸潤。酒精性纖維化通常從中央靜脈周圍與竇周區開始，不是由 portal areas 開始，標準答案為 C。

【選項詳解】
- A. 正確。酒精性肝病常見 AST > ALT，比例常大於 2，與粒線體受損與 pyridoxal phosphate 缺乏有關。
- B. 正確。酒精性肝炎病理可見脂肪堆積、肝細胞 ballooning、Mallory-Denk bodies 與嗜中性球浸潤。
- C. 錯誤。酒精性肝纖維化典型從 central vein 周圍、perisinusoidal 或 pericellular fibrosis 開始，之後可進展為橋接纖維化與肝硬化。
- D. 正確。在相同飲酒量下，女性較容易發生酒精性肝損傷，與代謝、體脂與荷爾蒙等因素有關。

【核心考點】
酒精性肝炎病理記 AST/ALT > 2、Mallory-Denk bodies、嗜中性球與中央靜脈周圍/竇周纖維化。`,
    key_point: "酒精性肝纖維化通常從中央靜脈周圍與竇周區開始，不是 portal areas。",
    flashcard_front: "酒精性肝炎的典型病理與肝纖維化起始位置是什麼？",
    flashcard_back: "脂肪變性、Mallory-Denk bodies、嗜中性球浸潤，AST 通常高於 ALT；纖維化常從中央靜脈周圍/竇周區開始。",
    flashcard_summary: "酒精性肝炎：AST>ALT、Mallory-Denk、嗜中性球；纖維化由 central/perisinusoidal 開始。",
  },
  91: {
    explanation: `【題幹解析】
自身免疫性胃炎主要攻擊胃體與胃底的壁細胞，造成胃酸低下、內在因子缺乏與維生素 B12 缺乏。胃竇通常相對保留，低胃酸會刺激 G 細胞分泌 gastrin，並非胃竇內分泌細胞減少，標準答案為 D。

【選項詳解】
- A. 正確。可測得抗壁細胞抗體與抗內在因子抗體，後者與惡性貧血及 B12 吸收不良更直接相關。
- B. 正確。內在因子不足會使末端迴腸吸收維生素 B12 受阻，造成巨幼紅細胞性貧血與神經病變。
- C. 正確。壁細胞破壞造成胃酸分泌不足，負回饋下降後 gastrin 分泌上升，可導致 enterochromaffin-like cell 增生。
- D. 錯誤。自身免疫性胃炎主要累及胃體/胃底而相對保留胃竇；胃竇 G 細胞不會因本病典型地減少，反而會因低胃酸刺激 gastrin 上升。

【核心考點】
自身免疫性胃炎：胃體/胃底壁細胞破壞、低胃酸、高 gastrin、內在因子不足與 B12 缺乏；胃竇相對保留。`,
    key_point: "自身免疫性胃炎主要累及胃體/胃底壁細胞，胃竇相對保留且 gastrin 上升。",
    flashcard_front: "自身免疫性胃炎的受累部位、抗體、胃酸與 gastrin 變化為何？",
    flashcard_back: "主要累及胃體/胃底壁細胞；可有抗壁細胞與抗內在因子抗體；胃酸下降、gastrin 上升，導致 B12 缺乏。",
    flashcard_summary: "自身免疫性胃炎：壁細胞/內在因子抗體，胃酸低、gastrin 高，胃竇相對保留。",
  },
  92: {
    explanation: `【題幹解析】
膀胱泌尿上皮癌有兩條常考分子路徑：低惡性度乳突狀腫瘤常見 FGFR3 突變；高惡性度、原位癌與侵襲性腫瘤則常連到 TP53/RB 路徑。最常見 FGFR3 突變的是非侵襲性低惡性度乳突狀泌尿上皮癌，標準答案為 A。

【選項詳解】
- A. 正確。非侵襲性低惡性度乳突狀泌尿上皮癌常有 FGFR3 活化突變，臨床上較易復發但進展風險相對低。
- B. 非侵襲性高惡性度乳突狀泌尿上皮癌較常與 TP53、RB 等基因異常相關，不是 FGFR3 最典型類型。
- C. 原位癌 (carcinoma in situ) 是扁平高惡性度病灶，常屬 TP53 路徑，具有進展為侵襲癌風險。
- D. 侵襲性高惡性度泌尿上皮癌也較常連到 TP53/RB 路徑與染色體不穩定，不是 FGFR3 的代表病灶。

【核心考點】
膀胱低惡性度乳突狀腫瘤常見 FGFR3；高惡性度/CIS/侵襲性病灶常見 TP53、RB 異常。`,
    key_point: "FGFR3 突變最常見於非侵襲性低惡性度乳突狀泌尿上皮癌。",
    flashcard_front: "膀胱泌尿上皮癌中，FGFR3 與 TP53/RB 分別常見於哪類病灶？",
    flashcard_back: "FGFR3：非侵襲性低惡性度乳突狀泌尿上皮癌。TP53/RB：高惡性度、CIS 與侵襲性病灶。",
    flashcard_summary: "膀胱癌分子路徑：低度乳突狀常 FGFR3；高度/CIS/侵襲性常 TP53/RB。",
  },
  93: {
    explanation: `【題幹解析】
原發性膜性腎病變常與抗 PLA2R 抗體相關，免疫複合物沉積在腎小球基底膜上皮下。沉積的 IgG 亞型以 IgG4 最典型，標準答案為 D。

【選項詳解】
- A. IgG1 可出現在某些免疫複合物疾病，但不是原發性膜性腎病變最主要的沉積亞型。
- B. IgG2 不是原發性膜性腎病變典型主要沉積 IgG 亞型。
- C. IgG3 較能活化補體，常在其他免疫複合物腎炎中討論，不是本題膜性腎病變的代表。
- D. IgG4 正確。原發性膜性腎病變常見 IgG4 dominant 的上皮下免疫沉積，並可見 spike and dome 變化。

【核心考點】
原發性膜性腎病變：抗 PLA2R、上皮下沉積、spike and dome、IgG4 dominant。`,
    key_point: "原發性膜性腎病變的腎小球免疫沉積以 IgG4 最典型。",
    flashcard_front: "原發性膜性腎病變常見抗體、沉積位置與 IgG 亞型是什麼？",
    flashcard_back: "常與抗 PLA2R 抗體相關；沉積在上皮下；IgG4 dominant，光鏡/銀染可見 spike and dome。",
    flashcard_summary: "膜性腎病變：PLA2R、上皮下免疫沉積、IgG4、spike and dome。",
  },
  94: {
    explanation: `【題幹解析】
亞急性肉芽腫性甲狀腺炎又稱 de Quervain thyroiditis，常在上呼吸道病毒感染後發生，臨床可有疼痛性甲狀腺腫與暫時性甲狀腺毒症。最可能誘因為病毒感染，標準答案為 C。

【選項詳解】
- A. 細菌感染通常造成急性化膿性甲狀腺炎，會有明顯化膿與細菌感染表現，不是亞急性肉芽腫性甲狀腺炎的典型誘因。
- B. 黴菌感染多見於免疫低下者，甲狀腺黴菌感染罕見，不是本病常見病因。
- C. 病毒感染正確。de Quervain thyroiditis 被認為與病毒感染後免疫反應有關，病理可見肉芽腫與巨細胞反應。
- D. 結核菌感染可造成肉芽腫性病變，但不是亞急性肉芽腫性甲狀腺炎最常見或最典型的誘發原因。

【核心考點】
亞急性肉芽腫性甲狀腺炎是疼痛性、常病毒感染後發生的甲狀腺炎；Hashimoto 則是不痛、慢性自體免疫。`,
    key_point: "亞急性肉芽腫性甲狀腺炎最常與病毒感染後反應有關。",
    flashcard_front: "亞急性肉芽腫性甲狀腺炎的典型誘因與臨床特色是什麼？",
    flashcard_back: "常在病毒感染後發生，為疼痛性甲狀腺炎，可有暫時性甲狀腺毒症與肉芽腫/巨細胞反應。",
    flashcard_summary: "de Quervain thyroiditis：病毒感染後、疼痛性、肉芽腫性甲狀腺炎。",
  },
  96: {
    explanation: `【題幹解析】
本題是否定式，問成人睪丸生殖細胞腫瘤何者較不正確。成人卵黃囊腫瘤通常是混合型生殖細胞腫瘤的一部分，純卵黃囊腫瘤較典型見於兒童；因此 A 說「常常為單一組織型態」較不正確，標準答案為 A。

【選項詳解】
- A. 較不正確。成人卵黃囊腫瘤多以混合型成分出現，常可與胚胎癌等其他生殖細胞腫瘤混合；純型卵黃囊腫瘤較常見於幼兒。
- B. 正確。Seminoma 是成人睪丸生殖細胞腫瘤常見類型，病理上常見透明胞質、纖維分隔與淋巴球浸潤。
- C. 正確。Embryonal carcinoma 較 seminoma 更具侵襲性，常較早侵犯、出血壞死並與其他非精原細胞瘤成分混合。
- D. 正確。純 choriocarcinoma 睪丸腫瘤相當罕見，但若出現常惡性度高、血行轉移早且 hCG 顯著升高。

【核心考點】
成人睪丸生殖細胞腫瘤中，卵黃囊腫瘤多是混合成分；純型卵黃囊腫瘤是兒童較典型。否定式題目要把 A 當作例外。`,
    key_point: "成人卵黃囊腫瘤多為混合型成分；純型卵黃囊腫瘤較常見於兒童。",
    flashcard_front: "成人睪丸卵黃囊腫瘤與兒童卵黃囊腫瘤在組織型態上有何差異？",
    flashcard_back: "成人卵黃囊腫瘤多為混合型生殖細胞腫瘤的一部分；兒童較常見純型卵黃囊腫瘤。",
    flashcard_summary: "睪丸生殖細胞腫瘤：成人 yolk sac tumor 常為混合成分，純型偏兒童。",
  },
  97: {
    explanation: `【題幹解析】
子宮頸切片顯示異生細胞取代整層上皮，代表全層上皮內高度病變；又偵測到高危險型 HPV 16 DNA，最符合子宮頸上皮內贅生第三級，也就是 CIN III，標準答案為 C。

【選項詳解】
- A. 尖形濕疣多由低危險型 HPV 6、11 引起，病理常見 koilocytosis 與乳突狀疣狀病灶，不會以 HPV 16 與全層異生作為典型表現。
- B. 慢性子宮頸炎併鱗狀細胞化生是反應性或修復性變化，不應出現異生細胞取代整層上皮的 CIN III 圖像。
- C. 子宮頸上皮內贅生第三級正確。CIN III 指重度異生或原位癌範圍，異型細胞累及全層但尚未穿越基底膜。
- D. 子宮頸息肉是良性外生性病灶，常由發炎或局部增生造成，不會呈現 HPV 16 相關全層上皮異生。

【核心考點】
CIN III = 全層上皮高度異生但未侵襲，常與高危險 HPV 16/18 相關；尖形濕疣則連到低危險 HPV 6/11。`,
    key_point: "全層子宮頸上皮異生且 HPV 16 陽性最符合 CIN III。",
    flashcard_front: "CIN III 的病理定義與常見 HPV 型別是什麼？它和尖形濕疣如何區分？",
    flashcard_back: "CIN III：異生細胞累及全層上皮、未穿越基底膜，常與高危險 HPV 16/18 相關。尖形濕疣多為 HPV 6/11。",
    flashcard_summary: "子宮頸病變：HPV16 + 全層異生 = CIN III；HPV6/11 = condyloma。",
  },
  98: {
    explanation: `【題幹解析】
發育不良痣通常較一般痣大、形狀與色澤不規則，可出現在日曬或非日曬部位，病理多為交界痣或混合痣伴結構與細胞異型。它是黑色素瘤風險指標，但大多數病灶本身不會轉變成黑色素瘤，標準答案為 D。

【選項詳解】
- A. 錯誤。發育不良痣通常比一般痣大，常大於 5 mm，且可有邊界不規則與顏色不均。
- B. 錯誤。發育不良痣不只見於日曬部位，軀幹、臀部等非日曬區也可出現。
- C. 錯誤。其組織形態多為交界痣或混合痣，伴 lentiginous melanocytic hyperplasia 與異型性，不是典型皮內痣。
- D. 正確。發育不良痣會增加黑色素瘤風險，尤其多發或家族性者，但絕大多數單一病灶不會直接惡性化。

【核心考點】
發育不良痣是黑色素瘤風險標記：大於一般痣、可在非日曬區、常為交界/混合型且有異型，但多數病灶不會變癌。`,
    key_point: "發育不良痣多數不會轉變成黑色素瘤，但代表黑色素瘤風險增加。",
    flashcard_front: "發育不良痣的大小、分布、組織型態與黑色素瘤風險如何判斷？",
    flashcard_back: "通常較大且不規則，可見於非日曬區；多為交界痣或混合痣伴異型；多數病灶不直接惡性化，但是黑色素瘤風險指標。",
    flashcard_summary: "發育不良痣：較大、不限日曬區、多為交界/混合型；多數不變 melanoma。",
  },
  99: {
    explanation: `【題幹解析】
角化不全 (parakeratosis) 指角質層中的角質細胞分化不完全，到了角質層仍保留細胞核。牛皮癬因表皮更新速度加快，常見 parakeratosis，標準答案為 C。

【選項詳解】
- A. 增厚是 hyperkeratosis 或 acanthosis 等概念，並不等於角化不全；角化不全的核心是角質層保留細胞核。
- B. 形成玻璃質樣物質不是 parakeratosis 的定義，較像其他變性或沉積性描述。
- C. 角質並不成熟、仍有細胞核存在正確。這正是 parakeratosis，在牛皮癬等快速表皮增生疾病常見。
- D. 變薄是 atrophy 或角質層變薄的描述，與 parakeratosis 定義不符。

【核心考點】
Parakeratosis = stratum corneum retained nuclei；hyperkeratosis = 角質層增厚；acanthosis = 棘層增厚。`,
    key_point: "角化不全是角質層分化不成熟，角質細胞仍保留細胞核。",
    flashcard_front: "Parakeratosis、hyperkeratosis、acanthosis 分別代表什麼？",
    flashcard_back: "Parakeratosis：角質層保留細胞核；hyperkeratosis：角質層增厚；acanthosis：棘層增厚。",
    flashcard_summary: "牛皮癬病理：parakeratosis 是角質層仍有細胞核。",
  },
  100: {
    explanation: `【題幹解析】
惡性貧血會造成維生素 B12 缺乏，影響髓鞘維持，導致脊髓亞急性聯合變性。病變主要侵犯後索與側索，因此特殊神經病理學病變在脊髓，標準答案為 B。

【選項詳解】
- A. 大腦白質不是惡性貧血最具代表性的病變部位；B12 缺乏的經典考點是脊髓長徑路徑。
- B. 脊髓正確。B12 缺乏會造成 posterior columns 與 lateral corticospinal tracts 脫髓鞘，產生感覺共濟失調、振動/本體覺下降與上運動神經元徵象。
- C. 大腦皮質不是惡性貧血特異神經病理病變位置；雖可有認知或精神症狀，但病理定位考點仍是脊髓。
- D. 小腦病變會造成共濟失調，但惡性貧血的共濟失調主要來自後索本體覺受損，不是小腦本身。

【核心考點】
維生素 B12 缺乏造成脊髓亞急性聯合變性，侵犯後索與側索；常伴巨幼紅細胞性貧血與神經症狀。`,
    key_point: "惡性貧血的 B12 缺乏會造成脊髓後索與側索的亞急性聯合變性。",
    flashcard_front: "惡性貧血造成的特殊神經病理病變在哪裡？主要侵犯哪些脊髓路徑？",
    flashcard_back: "在脊髓，主要侵犯後索與側索，稱 subacute combined degeneration。",
    flashcard_summary: "惡性貧血/B12 缺乏：脊髓後索與側索亞急性聯合變性。",
  },
};

const batches = [
  { file: "q007-q036_selected_20260916.json", nums: [7, 13, 25, 29, 31, 32, 33, 34, 35, 36] },
  { file: "q037-q048_selected_20260916.json", nums: [37, 38, 40, 41, 42, 43, 44, 45, 46, 48] },
  { file: "q049-q063_selected_20260916.json", nums: [49, 50, 51, 52, 54, 55, 56, 57, 60, 63] },
  { file: "q064-q087_selected_20260916.json", nums: [64, 68, 69, 70, 73, 75, 76, 77, 82, 87] },
  { file: "q089-q100_selected_20260916.json", nums: [89, 91, 92, 93, 94, 96, 97, 98, 99, 100] },
];

const sourceText = fs.readFileSync(sourceFile, "utf8");
const data = JSON.parse(sourceText);

if (data.id !== datasetId) {
  throw new Error(`Unexpected dataset id: ${data.id}`);
}

const byNumber = new Map(data.questions.map((question) => [question.question_number, question]));
const targetNumbers = batches.flatMap((batch) => batch.nums);

for (const number of targetNumbers) {
  if (!byNumber.has(number)) throw new Error(`Missing source question ${number}`);
  if (!updates[number]) throw new Error(`Missing rewrite for question ${number}`);
}

for (const number of Object.keys(updates).map(Number)) {
  if (!targetNumbers.includes(number)) throw new Error(`Rewrite Q${number} is not assigned to any batch`);
}

function makeUpdate(number) {
  const question = byNumber.get(number);
  const rewrite = updates[number];
  return {
    question_id: question.id,
    question_number: number,
    explanation: rewrite.explanation,
    key_point: rewrite.key_point,
    flashcard_front: rewrite.flashcard_front,
    flashcard_back: rewrite.flashcard_back,
    flashcard_summary: rewrite.flashcard_summary,
    review_status: "ai_generated",
    explanation_model: model,
    explanation_generated_at: timestamp,
    manual_review_notes: rewrite.manual_review_notes || [],
  };
}

function validateUpdateObject(update, batch) {
  for (const key of Object.keys(update)) {
    if (!allowedUpdateFields.has(key)) {
      throw new Error(`Q${update.question_number} has forbidden update field ${key}`);
    }
  }
  const question = byNumber.get(update.question_number);
  if (!question) throw new Error(`Unknown question ${update.question_number}`);
  if (question.id !== update.question_id) throw new Error(`Q${update.question_number} id mismatch`);
  if (update.question_number < batch.range.start || update.question_number > batch.range.end) {
    throw new Error(`Q${update.question_number} outside batch range`);
  }
  for (const heading of ["【題幹解析】", "【選項詳解】", "【核心考點】"]) {
    if (!update.explanation.includes(heading)) {
      throw new Error(`Q${update.question_number} missing heading ${heading}`);
    }
  }
  for (const label of ["A", "B", "C", "D"]) {
    if (!update.explanation.includes(`- ${label}.`)) {
      throw new Error(`Q${update.question_number} missing option ${label}`);
    }
  }
  for (const phrase of bannedPhrases) {
    if (update.explanation.includes(phrase)) {
      throw new Error(`Q${update.question_number} contains banned phrase: ${phrase}`);
    }
  }
}

function writeJson(filePath, value) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

const updateFiles = [];
for (const batchDef of batches) {
  const batch = {
    source_file: sourceFile,
    dataset_id: datasetId,
    range: { start: Math.min(...batchDef.nums), end: Math.max(...batchDef.nums) },
    updates: batchDef.nums.map(makeUpdate),
  };
  for (const update of batch.updates) validateUpdateObject(update, batch);
  const filePath = path.join(updateDir, batchDef.file);
  writeJson(filePath, batch);
  updateFiles.push(filePath);
}

const backupFile = path.join(updateDir, "before_merge_medicine-2_20260916.json");
writeJson(backupFile, data);

for (const filePath of updateFiles) {
  const batch = JSON.parse(fs.readFileSync(filePath, "utf8"));
  for (const update of batch.updates) {
    const question = byNumber.get(update.question_number);
    for (const key of [
      "explanation",
      "key_point",
      "flashcard_front",
      "flashcard_back",
      "flashcard_summary",
      "review_status",
      "explanation_model",
      "explanation_generated_at",
      "manual_review_notes",
    ]) {
      question[key] = update[key];
    }
  }
}

writeJson(sourceFile, data);

console.log(JSON.stringify({
  sourceFile,
  datasetId,
  updatedQuestions: targetNumbers,
  updateFiles,
  backupFile,
}, null, 2));
