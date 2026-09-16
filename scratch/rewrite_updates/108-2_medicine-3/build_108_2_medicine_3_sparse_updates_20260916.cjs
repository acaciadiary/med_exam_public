const fs = require("fs");
const path = require("path");

const SOURCE_FILE = "public/data/exams/108-2/medicine-3.json";
const DATASET_ID = "108-2_medicine-3";
const OUTPUT_DIR = "scratch/rewrite_updates/108-2_medicine-3";
const GENERATED_AT = "2026-09-16T13:20:00+08:00";
const MODEL = "codex-high-quality-rewrite";

function explanation(stem, options, core) {
  return `【題幹解析】\n${stem}\n\n【選項詳解】\n${options}\n\n【核心考點】\n${core}`;
}

const UPDATES = {
  1: {
    explanation: explanation(
      `血清白蛋白 3.0 g/dL、腹水白蛋白 1.2 g/dL，SAAG 為 1.8 g/dL，代表腹水與門脈高壓相關。腹水總蛋白 2.8 g/dL 偏高，較支持心衰竭或肝靜脈/肝竇阻塞；肝硬化造成的門脈高壓腹水通常蛋白較低，因此本題問「最不可能」時選 C。`,
      `- A. early hepatic vein thrombosis 可造成肝後性或肝流出阻塞，SAAG 常偏高，早期腹水蛋白也可偏高，因此仍符合本題數據。\n- B. heart failure 造成肝鬱血與門脈壓升高，SAAG 會大於 1.1，且因肝竇通透與蛋白外漏，腹水總蛋白常大於 2.5 g/dL。\n- C. liver cirrhosis 是本題的例外。肝硬化雖會使 SAAG 升高，但腹水蛋白通常較低，常低於 2.5 g/dL，與本題 2.8 g/dL 不合。\n- D. hepatic sinusoidal obstruction syndrome 會阻礙肝竇或小肝靜脈流出，產生門脈高壓型且蛋白較高的腹水，所以不能優先排除。`,
      `腹水先用 SAAG 判斷是否為門脈高壓，再用腹水總蛋白分流病因：SAAG 高且蛋白高偏向心衰竭、Budd-Chiari 或肝竇阻塞；SAAG 高但蛋白低才典型支持肝硬化。`
    ),
    key_point: "SAAG > 1.1 且腹水總蛋白 > 2.5 g/dL 偏向心衰竭或肝靜脈/肝竇阻塞，較不支持典型肝硬化腹水。",
    flashcard_front: "腹水鑑別：SAAG 高且腹水蛋白高代表什麼？",
    flashcard_back: "SAAG > 1.1 表示門脈高壓；若腹水蛋白 > 2.5 g/dL，偏向心衰竭、Budd-Chiari 或肝竇阻塞，肝硬化典型蛋白較低。",
  },
  2: {
    explanation: explanation(
      `題目問最不可能造成呼吸性鹼中毒的藥物或狀況。呼吸性鹼中毒來自過度換氣使 PaCO2 下降；水楊酸、高山缺氧與懷孕都會刺激換氣，嗎啡則抑制呼吸中樞，較會造成 CO2 滯留與呼吸性酸中毒。`,
      `- A. 水楊酸鹽會直接刺激延腦呼吸中樞，早期中毒常先出現呼吸性鹼中毒，之後才可能合併代謝性酸中毒。\n- B. 高山環境的低氧會刺激周邊化學受器，使換氣增加，PaCO2 被吹低而形成呼吸性鹼中毒。\n- C. 懷孕時黃體素會提高呼吸中樞對 CO2 的敏感度，分鐘通氣量增加，常見輕度慢性呼吸性鹼中毒。\n- D. 嗎啡是本題例外。opioid 抑制呼吸中樞，會使肺泡通氣不足與 PaCO2 上升，方向是呼吸性酸中毒而非鹼中毒。`,
      `判斷酸鹼題先抓通氣方向：刺激換氣會造成低 PaCO2 與呼吸性鹼中毒；呼吸抑制藥物如 opioid 則造成高 PaCO2 與呼吸性酸中毒。`
    ),
    key_point: "呼吸性鹼中毒來自過度換氣；嗎啡抑制呼吸中樞，較會造成呼吸性酸中毒。",
    flashcard_front: "哪些情境造成呼吸性鹼中毒？嗎啡例外在哪？",
    flashcard_back: "水楊酸、高山低氧、懷孕會增加換氣造成呼吸性鹼中毒；嗎啡抑制呼吸，造成 CO2 滯留與呼吸性酸中毒。",
  },
  3: {
    explanation: explanation(
      `本題考心導管壓力數據的基本解讀。體循環血管阻力 SVR 的計算需要壓力差除以心輸出量，也就是平均主動脈壓、平均右心房壓與心輸出量，因此 D 正確。`,
      `- A. 正常平均肺動脈壓約 10-20 mmHg，通常不應是 30-40 mmHg；這個範圍已接近肺高壓表現。\n- B. constrictive pericarditis 的右、左心室舒張末壓常趨於相等，且會出現 dip-and-plateau；用「右心室舒張末壓小於右心室收縮壓 1/3」來區分並不正確。\n- C. 二尖瓣狹窄時，PCWP 反映的是左心房壓及二尖瓣近端壓力，因二尖瓣本身有狹窄壓力梯度，不能可靠代表左心室舒張末壓。\n- D. SVR = (平均動脈壓 - 平均右心房壓) / 心輸出量，再乘換算常數；所以需要心輸出量、平均主動脈壓與平均右心房壓。`,
      `血流動力學計算要分清楚壓力代表的位置：PCWP 通常近似左心房壓，但二尖瓣狹窄時不等於左心室舒張末壓；SVR 需要動脈壓、右心房壓與心輸出量。`
    ),
    key_point: "SVR 計算需平均主動脈壓、平均右心房壓與心輸出量；二尖瓣狹窄時 PCWP 不能代表 LVEDP。",
    flashcard_front: "心導管：SVR 需要哪些資料？PCWP 在二尖瓣狹窄有何限制？",
    flashcard_back: "SVR = (MAP - RAP) / CO；二尖瓣狹窄時 PCWP 反映左心房壓，不可直接當 LVEDP。",
  },
  4: {
    explanation: explanation(
      `PR interval 從 P 波開始到 QRS 開始，代表心房興奮傳到心室開始去極化前的時間。它包含心房去極化、AV node 延遲，以及被 QRS 遮住的心房再極化，但不包含心室去極化本身。`,
      `- A. 心房去極化形成 P 波，是 PR interval 的起始部分，因此屬於 PR 間距涵蓋的事件。\n- B. 心房再極化幅度小且常被 QRS 掩蓋，但時序上可落在 PR 到 QRS 附近，並非本題最不可能的部分。\n- C. 房室結傳導延遲是 PR interval 的核心，PR 延長常反映 AV nodal conduction delay 或房室傳導阻滯。\n- D. 心室去極化由 QRS complex 表示；PR interval 到 QRS 開始即結束，所以心室去極化不屬於 PR 間距。`,
      `PR interval 是「心房去極化開始到心室去極化開始前」的傳導時間；心室去極化看 QRS，不看 PR。`
    ),
    key_point: "PR interval 代表心房到房室結傳導至心室去極化開始前的時間；心室去極化由 QRS 表示。",
    flashcard_front: "ECG PR interval 包含哪些心跳週期？",
    flashcard_back: "包含 P 波與 AV nodal delay，到 QRS 開始前結束；心室去極化屬 QRS，不屬 PR interval。",
  },
  5: {
    explanation: explanation(
      `70 歲糖尿病女性急性胸痛、冒汗與噁心，題目附圖心電圖被官方判讀為左前降支供應區的急性心肌梗塞。LAD 阻塞典型影響前壁、前中隔與心尖，常對應 V1-V4 或前壁導程變化。`,
      `- A. 左主幹阻塞通常造成大範圍左心室缺血，常見廣泛 ST 變化並可能迅速休克；若題圖主要是前壁導程變化，較不優先選左主幹。\n- B. 左前降支供應前壁與前中隔，急性前壁心肌梗塞最典型要想到 LAD，這與官方答案相符。\n- C. 左迴旋支多供應側壁或後外側壁，心電圖常在 I、aVL、V5-V6 或後壁線索較突出，不是本題官方判讀的主血管。\n- D. 右冠狀動脈常造成下壁梗塞，對應 II、III、aVF 變化，也可能合併右心室梗塞；與前壁 LAD 型態不同。`,
      `心肌梗塞定位常用導程分布配冠狀動脈：前壁/前中隔導程想到 LAD，下壁想到 RCA，側壁想到 LCX 或 diagonal/obtuse marginal。`
    ),
    key_point: "急性前壁或前中隔心肌梗塞最常對應左前降支阻塞。",
    flashcard_front: "心肌梗塞導程定位：LAD 阻塞常見哪一區？",
    flashcard_back: "LAD 阻塞常造成前壁、前中隔或心尖梗塞，典型導程為 V1-V4 或前壁相關導程。",
  },
  6: {
    explanation: explanation(
      `cardiac tamponade 與 constrictive pericarditis 都可有頸靜脈壓上升與舒張受限，但吸氣時頸靜脈壓反而上升的 Kussmaul sign 較支持 constrictive pericarditis。心包膜填塞因右心充盈被液體壓迫，典型沒有 Kussmaul sign。`,
      `- A. pulsus paradoxus 常見於心包膜填塞，但嚴重 constrictive physiology 或其他胸腔疾病也可能出現，區分力不如 Kussmaul sign。\n- B. Kussmaul sign 在 constrictive pericarditis 較典型，因僵硬心包限制右心吸氣時擴張；tamponade 通常沒有此表現，是最佳區分點。\n- C. third heart sound 是心室快速充盈造成的聲音，可見於容量負荷或心衰竭，並非兩者最可靠的鑑別特徵。\n- D. prominent x descent 可見於 tamponade；constrictive pericarditis 也會有明顯頸靜脈波變化，單靠 x descent 不如 Kussmaul sign 清楚。`,
      `限制性心包膜炎常見 Kussmaul sign 與明顯 y descent；心包膜填塞重點是 pulsus paradoxus、x descent 保留且 y descent 受抑制。`
    ),
    key_point: "Kussmaul sign 較支持限制性心包膜炎，通常不見於典型心包膜填塞。",
    flashcard_front: "tamponade vs constrictive pericarditis：哪個徵象最能區分？",
    flashcard_back: "Kussmaul sign 支持 constrictive pericarditis；tamponade 常見 pulsus paradoxus、JVP 上升與 y descent 受抑制。",
  },
  7: {
    explanation: explanation(
      `題目問擴張性心肌症合併心衰竭的錯誤敘述。擴張性心肌症會有左心室擴大與收縮功能下降，但標準心衰竭藥物與合適病人的 CRT 都可能改善收縮功能、症狀與預後，所以 D 說藥物無法改善是錯的。`,
      `- A. 感染、酒精或化療毒性、內分泌/代謝異常、營養缺乏與家族遺傳都可造成擴張性心肌症，病因確實多樣。\n- B. 心臟超音波看到左心室擴張、射出分率下降與整體收縮不良，是擴張性心肌症的典型影像表現。\n- C. 合併 LBBB 且 QRS 延長、EF 降低並符合症狀條件者，CRT 可改善心室同步性，進而改善心功能與住院風險。\n- D. 這句是錯誤敘述。ACEi/ARB/ARNI、beta blocker、MRA、SGLT2 inhibitor 等心衰竭藥物可改善 remodeling、EF、症狀與存活。`,
      `擴張性心肌症治療不是只能支持療法；HFrEF 藥物與符合條件的 CRT 都可能逆轉 remodeling 並改善收縮功能。`
    ),
    key_point: "擴張性心肌症合併 HFrEF 可由標準心衰竭藥物與符合條件的 CRT 改善心功能與預後。",
    flashcard_front: "擴張性心肌症：藥物與 CRT 能否改善收縮功能？",
    flashcard_back: "可以。HFrEF guideline-directed therapy 與 LBBB/QRS 延長者的 CRT 可改善 remodeling、EF 與症狀。",
  },
  8: {
    explanation: explanation(
      `動脈壓波從中央傳到周邊時，因反射波與血管順應性下降，收縮壓會被放大，舒張壓則可略降或不如中央高，造成脈壓變大。題目問由近心端往周邊逐次測量，最佳選項是收縮壓上升、舒張壓降低。`,
      `- A. 正確。周邊動脈壓波常有 systolic pressure amplification，收縮壓上升且舒張壓下降，使脈壓加大。\n- B. 舒張壓通常不會隨周邊傳導一起明顯上升；若收縮與舒張都上升，無法反映典型周邊壓波放大。\n- C. 收縮壓不變忽略了周邊反射波造成的收縮壓放大，因此不符合生理。\n- D. 只寫舒張壓不變不夠準確；本題考典型由中央到周邊的壓波變化，舒張壓會較中央低。`,
      `中央到周邊的血壓變化重點是 pulse pressure amplification：周邊收縮壓較高、舒張壓較低或不增，平均壓差異較小。`
    ),
    key_point: "動脈壓波往周邊傳導時收縮壓上升、舒張壓下降，脈壓增大。",
    flashcard_front: "中央到周邊測血壓：收縮壓與舒張壓如何變？",
    flashcard_back: "周邊動脈收縮壓因波形反射而上升，舒張壓較低，脈壓變大。",
  },
  10: {
    explanation: explanation(
      `題目問肥厚型心肌病變心因性猝死的「非」主要預測因子。HCM 風險因子包含猝死家族史、極厚左心室壁、非持續性心室頻脈，以及運動時血壓異常不升或下降；年輕病人運動時血壓能正常上升，反而不是危險訊號。`,
      `- A. 猝死家族史代表可能有高風險基因與惡性心律不整傾向，是 HCM 猝死評估的重要項目。\n- B. 左心室壁厚超過 30 mm 屬 massive hypertrophy，與猝死風險上升相關。\n- C. 這是本題答案。運動到高強度時血壓上升是相對正常反應；HCM 要擔心的是運動時血壓反應不佳、無法上升或下降。\n- D. 24 小時心電圖出現 spontaneous nonsustained VT，表示有心室性心律不整傾向，是 HCM 猝死風險因子。`,
      `HCM 猝死風險要記「家族猝死、壁厚很厚、NSVT、暈厥、運動血壓異常、心尖瘤或廣泛纖維化」；正常運動血壓上升不算主要危險因子。`
    ),
    key_point: "HCM 猝死風險包含家族史、壁厚 >=30 mm、NSVT 與運動血壓反應異常；運動時血壓正常上升不是主要風險因子。",
    flashcard_front: "HCM 猝死風險：運動血壓正常上升算危險因子嗎？",
    flashcard_back: "不算。要擔心的是運動時血壓無法上升或下降；另有家族猝死、壁厚 >=30 mm、NSVT 等。",
  },
  11: {
    explanation: explanation(
      `本題問肺栓塞藥物治療的正確敘述。直接口服抗凝血劑如 rivaroxaban、apixaban、dabigatran 在合適病人治療靜脈血栓栓塞不劣於 warfarin，且整體出血風險較低，因此 D 正確。`,
      `- A. 肺栓塞可有胸痛、呼吸困難、心搏過速與 P2 增強；肺動脈壓升高時 P2 不是變小聲，因此這個敘述不正確。\n- B. 抗凝血療程取決於誘發因子、復發風險與出血風險，常見不是一律至少 3 年；許多初次且可逆誘因者約治療 3 個月。\n- C. massive PE 合併血流動力學不穩可考慮全身或導管導向溶栓，但導管局部治療常用較低劑量；說 tPA 建議與周邊給藥同樣 100 mg 不恰當。\n- D. 正確。多項研究支持 DOACs 治療 PE 的效果不劣於 warfarin，且可減少部分出血事件，已成為許多病人的常用選擇。`,
      `肺栓塞治療以抗凝血為核心；DOACs 對多數合適 VTE 病人可取代 warfarin。溶栓保留給 massive PE 或高危險情境，療程長短依誘因與復發風險調整。`
    ),
    key_point: "DOACs 治療肺栓塞不劣於 warfarin，且常有較低出血風險；抗凝療程不是一律 3 年。",
    flashcard_front: "肺栓塞治療：DOAC 與 warfarin、溶栓、療程怎麼判斷？",
    flashcard_back: "合適病人可用 DOACs，效果不劣於 warfarin 且出血較少；massive PE 才考慮溶栓，療程依誘因與復發風險決定。",
  },
  12: {
    explanation: explanation(
      `題目問 HDV 敘述何者錯誤。HDV 需要 HBV 提供 HBsAg 才能包裝與傳播，可與 HBV 同時急性感染，也可在慢性 HBV 帶原者發生 superinfection；干擾素可用但療效有限，D 把根治率寫成極高且不易復發是錯的。`,
      `- A. 正確。HDV 不能獨立完成感染週期，臨床可見 HBV/HDV coinfection，也可在 HBV 帶原者身上 superinfection。\n- B. 正確。HDV superinfection 常使原本慢性 B 肝快速惡化，可能造成嚴重肝炎、肝衰竭或加速肝硬化。\n- C. 正確。急性 HBV/HDV coinfection 後慢性化機率相對低；慢性化風險較高的是 HDV superinfection 於既有 HBV 帶原者。\n- D. 錯誤。pegylated interferon 是傳統可用治療之一，但持久病毒反應有限、復發不少，不能說根治率超過 80% 且不容易復發。`,
      `HDV 的高考點是依附 HBV、superinfection 較嚴重且較易慢性化；治療困難，干擾素效果有限，不能把它記成高根治率疾病。`
    ),
    key_point: "HDV 需 HBV 才能感染；superinfection 較嚴重且易慢性化，pegylated interferon 療效有限且可復發。",
    flashcard_front: "HDV：coinfection、superinfection 與治療陷阱？",
    flashcard_back: "HDV 依賴 HBV；coinfection 慢性化較低，superinfection 較嚴重且易慢性化；interferon 療效有限，不是高根治率。",
  },
  13: {
    explanation: explanation(
      `AIH 診斷評分會整合排除其他肝病、自體抗體、IgG、肝切片與治療反應等資訊。其遺傳背景常與 HLA-DR3、DR4 等相關，D 寫成 HLA-A2 與 DR6 是錯誤配對。`,
      `- A. 正確。AIH 是排除性與整合性診斷，需先排除病毒性肝炎、藥物性肝炎、酒精性肝病與其他常見原因。\n- B. 正確。對 corticosteroid 或免疫抑制治療反應良好，可支持 AIH 診斷，也被納入傳統評分思路。\n- C. 正確。ANA、SMA、anti-LKM1 等自體抗體是 AIH 重要免疫學線索，其中 ANA 是常見指標之一。\n- D. 錯誤。AIH 較典型 HLA 關聯是 DR3、DR4 等；HLA-A2 與 DR6 不是本題所問的標準關聯。`,
      `AIH 診斷不是單靠一個抗體，而是排除其他肝病後，結合自體抗體、IgG、切片與免疫抑制反應；HLA 典型記 DR3/DR4。`
    ),
    key_point: "AIH 評分重視排除其他肝病、自體抗體與治療反應；HLA 關聯以 DR3/DR4 較典型。",
    flashcard_front: "AIH 診斷評分與 HLA 關聯？",
    flashcard_back: "需排除病毒等常見肝病，結合 ANA/SMA、IgG、切片與免疫抑制反應；HLA 常記 DR3、DR4。",
  },
  14: {
    explanation: explanation(
      `E 型肝炎主要經糞口途徑傳播，潛伏期通常約 2-9 週，平均約 40 天左右。A 把潛伏期寫成約 24 週過長，因此是錯誤敘述。`,
      `- A. 錯誤。HEV 確實主要經糞口傳染，但潛伏期不是約 24 週；常見約數週，約 2-9 週較合理。\n- B. 正確。多數急性 HEV 會自行恢復，但少數可猛爆性肝衰竭，孕婦感染特別需要警覺嚴重病程。\n- C. 正確。急性 HEV 常以 IgM anti-HEV 作為血清診斷線索，也可依情境搭配 HEV RNA。\n- D. 正確。免疫功能正常者多完全痊癒；器官移植、血液腫瘤或免疫抑制病人則可能轉為慢性 HEV。`,
      `HEV 考點是糞口傳染、急性感染多自限、孕婦可嚴重、免疫低下可慢性化；潛伏期是數週而非半年。`
    ),
    key_point: "E 型肝炎經糞口傳播，潛伏期約 2-9 週；免疫低下者可慢性化，孕婦有猛爆性風險。",
    flashcard_front: "E 型肝炎：傳染途徑、潛伏期與慢性化？",
    flashcard_back: "糞口傳播，潛伏期約 2-9 週；多數急性自限，孕婦可能嚴重，免疫低下者可能慢性化。",
  },
  15: {
    explanation: explanation(
      `題目問肝臟疾病遺傳與基因檢測的錯誤敘述。Wilson disease 的致病基因是 ATP7B 沒錯，但 ATP7B 突變種類很多，不是只有一種突變會發生，因此 D 錯。`,
      `- A. 正確。酒精代謝先由 alcohol dehydrogenase 產生 acetaldehyde，再由 ALDH 轉成 acetate；ALDH2 變異會讓乙醛堆積，造成臉紅等反應。\n- B. 正確。自體免疫性肝炎與特定 HLA 背景有關，常見提到 HLA-B8、DR3、DR4 等遺傳易感性。\n- C. 正確。HFE 相關 hereditary hemochromatosis 常見 C282Y 與 H63D 變異，是經典基因檢測重點。\n- D. 錯誤。Wilson disease 與 ATP7B 有關，但 ATP7B 已知突變型態非常多，不能說只有一種突變會發生。`,
      `遺傳題要分清「基因名稱」與「突變多樣性」：Wilson disease 是 ATP7B，但突變種類繁多；hemochromatosis 常考 HFE C282Y/H63D。`
    ),
    key_point: "Wilson disease 的基因是 ATP7B，但突變種類很多，不是單一突變；HFE C282Y/H63D 是遺傳性血色沉著症重點。",
    flashcard_front: "肝臟遺傳病：Wilson 與 hemochromatosis 的基因？",
    flashcard_back: "Wilson disease 為 ATP7B 且突變多樣；遺傳性血色沉著症常見 HFE C282Y、H63D。",
  },
  17: {
    explanation: explanation(
      `題目問與門脈高壓相關性較低的情況。食道靜脈曲張、脾腫大與腹水都直接來自門脈壓升高；肝性腦病變雖可被門體分流促發，但主要和肝功能衰竭、氨與其他神經毒素清除下降有關，所以相關性較低。`,
      `- A. 肝性腦病變是本題答案。它常發生在肝硬化病人，但核心是肝臟解毒能力下降與門體分流使氨等物質進入體循環，不像靜脈曲張那樣是門脈壓的直接結構結果。\n- B. 食道靜脈曲張是門脈高壓最典型併發症之一，來自門體側枝循環擴張，與門脈壓高度相關。\n- C. 脾腫大與脾亢進可由門脈系統鬱血造成，導致血小板或白血球偏低，是門脈高壓常見表現。\n- D. 腹水形成與門脈高壓、內臟血管擴張、腎鈉水滯留與低白蛋白有關，其中門脈高壓是重要驅動因素。`,
      `肝硬化併發症中，靜脈曲張、脾腫大與腹水和門脈高壓最直接；肝性腦病變還需要肝解毒失衡與門體分流共同解釋。`
    ),
    key_point: "食道靜脈曲張、脾腫大與腹水直接由門脈高壓驅動；肝性腦病變較偏肝解毒失衡與門體分流。",
    flashcard_front: "肝硬化併發症：哪些最直接來自門脈高壓？",
    flashcard_back: "食道靜脈曲張、脾腫大/脾亢進與腹水最直接；肝性腦病變主要和氨等毒素清除下降及門體分流有關。",
  },
  18: {
    explanation: explanation(
      `本題問大腸直腸癌敘述何者正確。術後復發多集中在前幾年，特別是前 4-5 年，因此 5 年存活率常被用來評估治療結果與預後。其餘選項把分期或轉移器官寫錯。`,
      `- A. 正確。大腸直腸癌復發多發生在治療後前數年，故 5 年存活率具有重要臨床參考價值。\n- B. 錯誤。T3N0M0 沒有淋巴結或遠端轉移，屬於第二期，不是第三期。\n- C. 錯誤。T1N1M0 只要有區域淋巴結轉移 N1，就屬第三期，不是第二期。\n- D. 錯誤。大腸直腸癌最常見內臟轉移部位是肝臟，因腸道靜脈回流經門脈系統進入肝臟；肺也可轉移但不是最容易。`,
      `大腸直腸癌分期抓兩點：N 陽性就是第三期，M 陽性才是第四期；血行轉移最常先到肝臟。`
    ),
    key_point: "大腸直腸癌復發多在前 4-5 年；N 陽性為第三期，最常見內臟轉移是肝臟。",
    flashcard_front: "大腸直腸癌：復發時間、TNM 分期與常見轉移器官？",
    flashcard_back: "復發多在前幾年，5 年存活率有參考性；T3N0M0 為第二期，T1N1M0 為第三期，最常轉移肝臟。",
  },
  19: {
    explanation: explanation(
      `IBS 是腸腦互動障礙，和腸道敏感度、蠕動、腸道菌相與心理社會因素都有關。部分 IBS-D 病人可從非吸收性抗生素 rifaximin 獲益，因此 C 正確。`,
      `- A. 錯誤。嚴重 IBS 常與壓力、焦慮、憂鬱、疼痛放大等腸腦軸因素有關，不能說精神方面關聯較小。\n- B. 錯誤。IBS 整體盛行率常見女性高於男性，不是男性為女性 2-3 倍。\n- C. 正確。Rifaximin 可用於部分 IBS，尤其腹瀉型 IBS，可能和調整腸道菌相或小腸細菌過度生長有關。\n- D. 錯誤。低劑量三環抗憂鬱劑或 SSRI/SNRI 在特定 IBS 病人可改善腹痛、腸道敏感度與共病情緒症狀。`,
      `IBS 不是單純結構病灶，而是腸腦互動障礙；治療可包含飲食、腸道藥物、rifaximin、抗憂鬱藥與心理介入。`
    ),
    key_point: "IBS 女性較常見，腸腦軸與心理因素重要；rifaximin 與抗憂鬱藥可幫助特定病人。",
    flashcard_front: "IBS：性別、腸腦軸與 rifaximin/抗憂鬱藥角色？",
    flashcard_back: "女性較多，心理與腸腦軸因素重要；rifaximin 可用於部分 IBS-D，抗憂鬱藥可改善疼痛敏感與共病情緒。",
  },
  20: {
    explanation: explanation(
      `本題問消化道內視鏡處置何者正確。早期表淺消化道癌若侷限於黏膜或淺層、淋巴轉移風險低，越來越多可用內視鏡黏膜切除或黏膜下剝離等方式處理，因此 D 正確。`,
      `- A. 錯誤。大量鮮血便多來自下消化道，但也可能是快速大量上消化道出血造成，不能直接等同一定要緊急大腸鏡。\n- B. 錯誤。低劑量 aspirin 在許多低風險或必要情境可持續使用，不能一律要求內視鏡前停藥一週；需依出血風險與心血管風險決定。\n- C. 錯誤。ERCP 主要用於膽道阻塞、膽管結石、膽管炎或需治療性介入的情境；不是所有黃疸都適合 ERCP。\n- D. 正確。早期表淺癌若符合內視鏡切除條件，可用 EMR、ESD 或其他 endoluminal resection 方式達到根治或器官保留。`,
      `內視鏡處置要看適應症與風險分層：鮮血便不一定都是下消化道、aspirin 不一定停、ERCP 不是黃疸篩檢工具；早期表淺癌可考慮內視鏡切除。`
    ),
    key_point: "早期表淺消化道癌可考慮內視鏡切除；鮮血便、aspirin 停藥與 ERCP 適應症都不能一概而論。",
    flashcard_front: "消化道內視鏡：早期癌、鮮血便、aspirin、ERCP 的常見陷阱？",
    flashcard_back: "早期表淺癌可內視鏡切除；大量鮮血便也可能是上消化道出血，aspirin 不一定停，ERCP 需有膽道介入適應症。",
  },
  23: {
    explanation: explanation(
      `年輕女性急速腎功能惡化、C3 低 C4 正常、ANCA 陰性，切片為新月型腎炎且電顯有上皮下 electron-dense deposits，最典型是感染後腎絲球腎炎，尤其鏈球菌感染後的 subepithelial humps。`,
      `- A. membranous nephropathy 典型是腎病症候群與瀰漫性上皮下免疫沉積造成 spike and dome，補體型態與急速新月型表現不如 PSGN 符合。\n- B. MPGN type II 又稱 dense deposit disease，電顯重點是 GBM 內緻密沉積，常有持續低 C3；不是上皮下 hump。\n- C. lupus nephritis 常有 C3 與 C4 都下降，免疫螢光呈 full-house，臨床也常伴 SLE 線索；本題 C4 正常較不支持。\n- D. poststreptococcal GN 符合低 C3、C4 正常、感染後免疫複合物、上皮下 hump，嚴重時可呈 crescentic GN。`,
      `PSGN 的病理關鍵是 subepithelial humps，補體常見 C3 下降而 C4 相對正常；lupus nephritis 則常 C3/C4 都低且 full-house。`
    ),
    key_point: "PSGN 可見 C3 低、C4 正常與上皮下 hump 狀沉積；嚴重時可呈新月型腎炎。",
    flashcard_front: "低 C3、C4 正常、subepithelial hump 要想到？",
    flashcard_back: "鏈球菌感染後腎絲球腎炎；電顯上皮下 hump，補體替代路徑活化使 C3 降低。",
  },
  24: {
    explanation: explanation(
      `這位糖尿病患者 eGFR 約 59、有 1.5 g/day 蛋白尿且血壓仍高於糖尿病腎病變常用目標，最需要加上 ACE inhibitor 或 ARB 以降低腎絲球內壓與蛋白尿；選項中 ARB 最合適。`,
      `- A. HbA1c 6.8% 已接近控制目標，題目主要問題是蛋白尿與血壓，不是需要立刻加長效胰島素。\n- B. EPO 可治療符合條件的 CKD 貧血，但不會用來「減緩腎功能惡化」，且 Hb 10.7 g/dL 未必需要立即使用。\n- C. 正確。糖尿病腎病變合併明顯蛋白尿時，ACEi/ARB 可降蛋白尿並保護腎臟，也有助於血壓達標。\n- D. 低蛋白飲食可在 CKD 中個別考慮，但加胺基酸補充不是本題優先治療；不能取代 RAAS blockade 對蛋白尿的處理。`,
      `糖尿病腎病變看到蛋白尿與血壓未達標，優先想到 ACEi/ARB；EPO 治貧血不保腎，降糖已可接受時不必先加胰島素。`
    ),
    key_point: "糖尿病腎病變合併蛋白尿與高血壓時，ACEi 或 ARB 是降蛋白尿與腎保護的核心治療。",
    flashcard_front: "糖尿病腎病變有蛋白尿：下一步藥物？",
    flashcard_back: "加 ACEi 或 ARB 以降蛋白尿、降腎絲球內壓與保護腎臟；同時控制血壓。",
  },
  25: {
    explanation: explanation(
      `顯影劑腎病變與腎髓質缺氧、腎血管收縮、氧化壓力、腎小管細胞毒性及管腔阻塞等因素有關，因此 D 正確。有效預防以事前風險評估、減少顯影劑量與等張液體補充為主。`,
      `- A. 血清肌酸酐確實常在 24-48 小時後上升，但需要透析的比例通常很低，不應概括說高於 1%。\n- B. 生理食鹽水預防重點是顯影劑前就開始補水，並在檢查後持續；只在施打後才開始不是理想預防策略。\n- C. N-acetylcysteine 研究結果不一致，效果沒有穩定強到建議常規使用；水化仍是核心措施。\n- D. 正確。外髓質本來氧張力低，顯影劑可造成血管收縮、自由基傷害、腎小管毒性與暫時性阻塞，導致急性腎損傷。`,
      `顯影劑腎病變預防最重要是事前水化、降低顯影劑暴露與辨識高風險病人；NAC 不是可靠常規保護措施。`
    ),
    key_point: "顯影劑腎病變機轉包含外髓質缺氧、自由基/腎小管毒性與管腔阻塞；預防重點是事前等張液體補充。",
    flashcard_front: "顯影劑腎病變：機轉與預防重點？",
    flashcard_back: "機轉含外髓質缺氧、氧化壓力與腎小管毒性；預防以顯影前後等張水化與減少顯影劑量為主。",
  },
  26: {
    explanation: explanation(
      `慢性腎臟病腎性貧血的主因是腎臟 erythropoietin 製造不足，加上發炎、鐵利用不良與尿毒環境影響紅血球壽命。胃腸道出血可造成貧血，但不是腎性貧血最主要原因，所以 C 錯。`,
      `- A. 正確。腎性貧血典型為 normocytic、normochromic，因主要是 EPO 缺乏造成紅血球生成不足。\n- B. 正確。貧血會造成疲倦、運動耐受差、認知影響，並增加心臟負荷，嚴重時可惡化心衰竭。\n- C. 錯誤。CKD 病人雖可能有血小板功能異常與出血傾向，但腎性貧血的核心不是胃腸道出血，而是 EPO 缺乏。\n- D. 正確。ESA 治療不建議把 Hb 矯正到正常人標準或 >=13 g/dL，因心血管與血栓風險增加，且未證實改善心血管結果。`,
      `CKD 貧血是 EPO 不足造成的正球性正色素性貧血；ESA 目標是改善症狀與避免輸血，不是把 Hb 拉到正常高值。`
    ),
    key_point: "CKD 腎性貧血主因是 EPO 缺乏，ESA 不應把 Hb 矯正到 >=13 g/dL。",
    flashcard_front: "CKD 腎性貧血：主因與 ESA 目標？",
    flashcard_back: "主因是 EPO 製造不足，常為正球性正色素性；ESA 不建議把 Hb 矯正到正常人高值，避免心血管風險。",
  },
  27: {
    explanation: explanation(
      `題目問慢性腎臟病何者錯誤。CKD 病人的主要死亡原因通常是心血管疾病，而非敗血症；敗血症雖是重要併發與死亡原因，但不是最常見主因。`,
      `- A. 正確。糖尿病長期是台灣新進入透析病人最常見的原發病因之一。\n- B. 正確。CKD 合併糖尿病時需積極控制血壓；考試常用目標是 130/80 mmHg 以下，並重視蛋白尿。\n- C. 錯誤。CKD 病人最主要死亡原因是心血管疾病，包括冠心病、心衰竭與心律不整等，而不是敗血症。\n- D. 正確。適度低蛋白飲食可減少尿毒素產生並改善部分尿毒症狀，但需注意營養狀態與個別化。`,
      `CKD 考點常是糖尿病為透析主因、心血管疾病為死亡主因；血壓與蛋白尿控制是延緩惡化的核心。`
    ),
    key_point: "慢性腎臟病最常見死亡主因是心血管疾病，不是敗血症；糖尿病是透析重要原發病因。",
    flashcard_front: "CKD：台灣透析主因與死亡主因？",
    flashcard_back: "新發透析常見原發病因是糖尿病；CKD 死亡主因通常是心血管疾病。",
  },
  28: {
    explanation: explanation(
      `本題問痛風與急性痛風性關節炎何者錯誤。高尿酸血症是痛風重要病因與風險因子，但急性發作時血尿酸可能正常甚至下降，單次尿酸值不能可靠診斷急性痛風。`,
      `- A. 正確。急性痛風好發下肢，尤其第一蹠趾關節、足踝與膝關節，和溫度較低及結晶沉積有關。\n- B. 正確。痛風在男性較常見；停經前女性因雌激素促尿酸排泄而風險較低。\n- C. 錯誤。急性發作時血尿酸值不一定升高，診斷最可靠仍是關節液看到負雙折射針狀 monosodium urate crystal。\n- D. 正確。急性痛風關節液可呈發炎性，白血球從數千到數萬都可能出現，需和感染性關節炎鑑別。`,
      `痛風診斷不能只看血尿酸；急性期血尿酸可能正常，確診關鍵是關節液尿酸鈉結晶。`
    ),
    key_point: "急性痛風發作時血尿酸可正常；確診依關節液 monosodium urate 結晶。",
    flashcard_front: "急性痛風：血尿酸能否作為可靠診斷？",
    flashcard_back: "不能單靠。急性發作時血尿酸可能正常，應以關節液負雙折射針狀尿酸鈉結晶確診。",
  },
  29: {
    explanation: explanation(
      `非關節炎疾病也可有特定關節表現。Hypertrophic osteoarthropathy 典型和肺癌等胸腔內惡性腫瘤相關，會有杵狀指、骨膜新生與關節痛，因此 A 正確。`,
      `- A. 正確。肥大性骨關節病常和肺癌、慢性肺病或其他胸腔疾病相關，肺癌是經典考點。\n- B. 錯誤。PVNS 是滑膜增生性病變，和 hemosiderin 沉積相關，並非糖尿病典型關節病變。\n- C. 錯誤。Hemophilic arthropathy 來自反覆關節腔出血，典型關聯是血友病，不是慢性腎臟病。\n- D. 錯誤。Neuropathic joint disease 又稱 Charcot joint，和深部感覺喪失的神經病變有關，如糖尿病神經病變、脊髓癆或脊髓空洞；不是腕隧道症候群本身。`,
      `系統病與關節病變要配對：肺癌配 HOA，血友病配出血性關節病，感覺神經病變配 Charcot joint。`
    ),
    key_point: "Hypertrophic osteoarthropathy 與肺癌等胸腔疾病相關；Charcot joint 來自感覺神經病變。",
    flashcard_front: "非關節炎疾病與關節病變配對：HOA、PVNS、hemophilic、Charcot？",
    flashcard_back: "HOA 配肺癌；hemophilic arthropathy 配血友病反覆出血；Charcot joint 配感覺神經病變。",
  },
  30: {
    explanation: explanation(
      `侷限型系統性硬化症的皮膚硬化範圍較侷限，病程通常較慢，肺高壓較需留意；瀰漫型則常有較快速皮膚進展與較嚴重內臟纖維化。若侷限型合併間質性肺病，通常較瀰漫型進展慢，因此 B 正確。`,
      `- A. 錯誤。皮膚硬化進展較快是 diffuse systemic sclerosis 的特徵，不是 limited 型。\n- B. 正確。Limited 型的 ILD 風險與進展通常低於 diffuse 型；若有 ILD，進展常較慢。\n- C. 錯誤。關節痛可見於各型系統性硬化症，但不是 limited 型相較 diffuse 型的代表性區分特徵。\n- D. 錯誤。Anti-topoisomerase I 或 Scl-70 較典型與 diffuse 型和 ILD 風險相關；limited 型更常想到 anticentromere antibody。`,
      `系統性硬化症分型：limited 型進展慢、常見 ACA 與肺高壓；diffuse 型皮膚進展快、Scl-70 與 ILD 風險較高。`
    ),
    key_point: "Limited systemic sclerosis 的 ILD 通常較慢，常見 anticentromere；Scl-70 較支持 diffuse 型與 ILD 風險。",
    flashcard_front: "Limited vs diffuse systemic sclerosis 的差異？",
    flashcard_back: "Limited 皮膚進展較慢、ACA、肺高壓；diffuse 進展快、Scl-70、ILD 與內臟纖維化風險較高。",
  },
  32: {
    explanation: explanation(
      `這位 SLE 腎炎病人已穩定 5 年、蛋白尿少、腎功能正常，目前使用低劑量 prednisolone 與 hydroxychloroquine。準備懷孕時，HCQ 應繼續使用以降低復發風險，低劑量 prednisolone 也可接受，因此維持目前用藥最適當。`,
      `- A. 錯誤。Dexamethasone 較容易通過胎盤，除非有胎兒治療適應症，否則不會為了等效類固醇而把 prednisolone 換成 dexamethasone。\n- B. 正確。病情穩定、低劑量 prednisolone 加 HCQ 是孕前與孕期可接受組合，且不需無故改藥。\n- C. 錯誤。Hydroxychloroquine 在 SLE 懷孕通常建議繼續，可降低疾病 flare 與不良妊娠風險。\n- D. 錯誤。Azathioprine 可作為孕期相對安全免疫抑制劑，但本題病情穩定且沒有活動性腎炎，不需主動加藥。`,
      `SLE 懷孕最好在疾病穩定至少數月後進行；HCQ 通常續用，低劑量 prednisolone 可用，避免無必要換成會穿胎盤的 dexamethasone。`
    ),
    key_point: "SLE 穩定病人備孕時應續用 hydroxychloroquine；低劑量 prednisolone 可接受，不需無故加 azathioprine。",
    flashcard_front: "SLE 腎炎穩定備孕：HCQ 與 prednisolone 要停嗎？",
    flashcard_back: "通常不需停。HCQ 建議續用以降低 flare；低劑量 prednisolone 可接受，dexamethasone 會穿胎盤較不作常規替換。",
  },
  33: {
    explanation: explanation(
      `題目問 HCC 臨床評估與診治何者錯誤。HCC 診斷主要依動態影像的動脈期增強與門脈/延遲期 washout，常用超音波、三相 CT 或動態 MRI；FDG-PET 對分化較好的 HCC 敏感度有限，不是最敏感診斷工具。`,
      `- A. 正確。黃疸、腹水、蜘蛛痣與手掌紅斑提示慢性肝病或肝硬化，也會影響 HCC 分期與治療選擇。\n- B. 正確。AFP 是常用腫瘤標記，但敏感度與特異度都有限，部分 HCC AFP 不升高。\n- C. 正確。超音波可篩檢，triphasic CT 與 gadolinium-enhanced MRI 可用動態血流特徵協助診斷。\n- D. 錯誤。FDG-PET 對 HCC 尤其分化良好病灶敏感度不足，不能稱為診斷 HCC 最敏感影像。`,
      `HCC 影像診斷重點是動態增強：arterial hyperenhancement 加 washout；AFP 可輔助但不可靠，FDG-PET 不是首選診斷。`
    ),
    key_point: "HCC 診斷依動態 CT/MRI 血管特徵；FDG-PET 對 HCC 敏感度有限，不是最敏感工具。",
    flashcard_front: "HCC 診斷：AFP、CT/MRI、FDG-PET 的角色？",
    flashcard_back: "AFP 可輔助但不一定升高；三相 CT/MRI 看動脈期增強與 washout；FDG-PET 非最敏感診斷工具。",
  },
  34: {
    explanation: explanation(
      `黑色素瘤流行病學在東西方不同。西方常見表淺擴散型與 BRAF 突變；東方族群較常見 acral lentiginous melanoma，發生在手掌、腳底或甲下等非日曬部位，因此 B 正確。`,
      `- A. 錯誤。西方黑色素瘤常見 BRAF 突變，不是 NRAS 最多。\n- B. 正確。東方病患黑色素瘤常見肢端小痣型，和白人以表淺擴散型較常見不同。\n- C. 錯誤。教育、篩檢與早期偵測偏向次級預防；初級預防重點是減少紫外線暴露與避免曬傷。\n- D. 錯誤。轉移黑色素瘤除了 BRAF/MEK 等標靶治療，也可用免疫檢查點抑制劑，如 anti-PD-1 或 anti-CTLA-4。`,
      `黑色素瘤考點：東方人常見 acral lentiginous type；西方 BRAF 突變常見；轉移疾病治療包含標靶與免疫治療。`
    ),
    key_point: "東方人黑色素瘤較常見 acral lentiginous 型；轉移黑色素瘤可用免疫治療與標靶治療。",
    flashcard_front: "黑色素瘤：東方常見型態與轉移治療？",
    flashcard_back: "東方族群常見 acral lentiginous melanoma；轉移治療包含免疫檢查點抑制劑與 BRAF/MEK 標靶等。",
  },
  35: {
    explanation: explanation(
      `第四期肺癌需依組織型、驅動基因與免疫標記選擇全身治療。EGFR 或 ALK 變異可用相對應標靶藥，免疫檢查點抑制劑已能改善部分晚期非小細胞肺癌預後，所以 C 說毫無幫助是錯的。`,
      `- A. 正確。EGFR 突變陽性的晚期非小細胞肺癌可用 EGFR TKI；題目列 erlotinib、afatinib 符合當時常見選項。\n- B. 正確。ALK rearrangement 陽性的非小細胞肺癌可使用 ALK inhibitor，例如 crizotinib 或後續世代藥物。\n- C. 錯誤。PD-1/PD-L1 或 CTLA-4 相關免疫治療對部分第四期非小細胞肺癌有療效，不是毫無幫助。\n- D. 正確。廣泛期小細胞肺癌治療核心仍是全身性化學治療，近年也可合併免疫治療，但化療仍是基礎。`,
      `晚期肺癌治療先看小細胞或非小細胞，再看 EGFR、ALK 等驅動基因與 PD-L1/免疫治療適應症；免疫治療不是無效選項。`
    ),
    key_point: "第四期非小細胞肺癌可依 EGFR/ALK 使用標靶，也可在合適病人使用免疫檢查點抑制劑。",
    flashcard_front: "第四期肺癌：EGFR、ALK 與免疫治療角色？",
    flashcard_back: "EGFR/ALK 陽性用相應 TKI；部分非小細胞肺癌可用免疫檢查點抑制劑；小細胞肺癌以全身治療為主。",
  },
  36: {
    explanation: explanation(
      `題目問去勢抗性攝護腺癌的藥物治療不包括何者。CRPC 治療包括 androgen receptor signaling inhibitor、abiraterone、docetaxel 等；flutamide 是第一代抗雄性素，對 CRPC 不是標準有效治療，甚至常有 antiandrogen withdrawal 的概念。`,
      `- A. Flutamide 是本題答案。它屬第一代非類固醇抗雄性素，主要用於較早期 androgen blockade，不是 CRPC 的代表治療。\n- B. Enzalutamide 是 androgen receptor inhibitor，可用於 metastatic 或 nonmetastatic CRPC，屬重要治療。\n- C. Abiraterone acetate 抑制 CYP17，降低 androgen synthesis，常與 prednisone 合併使用，是 CRPC 標準藥物之一。\n- D. Docetaxel 化學治療可改善 metastatic CRPC 存活，是 CRPC 經典全身治療選項。`,
      `CRPC 治療要記 docetaxel、abiraterone、enzalutamide 等；第一代 flutamide 不是此階段的代表藥。`
    ),
    key_point: "CRPC 標準治療包含 enzalutamide、abiraterone 與 docetaxel；flutamide 不是代表性治療。",
    flashcard_front: "CRPC 藥物：哪個不是標準代表？",
    flashcard_back: "Flutamide 不是 CRPC 代表治療；enzalutamide、abiraterone、docetaxel 都是重要選項。",
  },
  37: {
    explanation: explanation(
      `染色體 t(2;8)(p12;q24) 牽涉 MYC 與 immunoglobulin light chain，是 Burkitt lymphoma/leukemia 的典型線索。此病生長極快且有腫瘤溶解風險，需要高強度治療與中樞神經預防；現代治療下長期存活率可遠高於 30%，所以 D 錯。`,
      `- A. 正確。Burkitt lymphoma 的核心機轉是 c-MYC deregulation，常見 t(8;14)，也可見 t(2;8) 或 t(8;22)。\n- B. 正確。Burkitt lymphoma 增殖非常快，LDH 與尿酸升高也提示腫瘤負荷與 tumor lysis risk，需儘快治療。\n- C. 正確。Burkitt lymphoma 有中樞神經侵犯風險，治療計畫通常需 CSF 評估與 intrathecal chemotherapy 預防或治療。\n- D. 錯誤。雖然病程兇猛，但對高強度化療相當敏感；在合適治療下長期存活率不應概括為小於三成。`,
      `Burkitt lymphoma 看到 MYC translocation、LDH/尿酸高與快速病程；治療積極且需 CNS prophylaxis，但並非現代治療下預後必然極差。`
    ),
    key_point: "Burkitt lymphoma 與 MYC deregulation 相關，進展快、需高強度化療與 CNS prophylaxis，但治療反應可佳。",
    flashcard_front: "t(2;8) + MYC：想到哪個淋巴瘤？治療重點？",
    flashcard_back: "Burkitt lymphoma/leukemia；進展快、腫瘤溶解風險高，需高強度化療與 CSF 評估、鞘內化療。",
  },
  38: {
    explanation: explanation(
      `維生素 B12 來自動物性食物，人體需求量少且肝臟儲存量大，所以完全無法吸收後也常需數年才耗盡。蔬果類不是 B12 的可靠來源，因此 D 錯。`,
      `- A. 正確。人體每日 B12 需求量約微克等級，遠低於許多水溶性維生素。\n- B. 正確。B12 肝臟儲存量可維持數年，所以吸收停止後常延遲 3-4 年才出現明顯缺乏。\n- C. 正確。哺乳婦女若 B12 缺乏，嬰兒可能因攝取不足而出現貧血、神經發育遲滯或生長問題。\n- D. 錯誤。蔬果不含足量可用 B12；素食者需靠強化食品或補充劑避免缺乏。`,
      `B12 的三個考點是動物性來源、肝臟儲存可撐數年、缺乏會造成巨球性貧血與神經症狀；蔬果不是可靠來源。`
    ),
    key_point: "維生素 B12 主要來自動物性食物，體內儲存可維持數年；蔬果不是可靠來源。",
    flashcard_front: "維生素 B12：來源、需求量與儲存時間？",
    flashcard_back: "需求量微克級，肝臟儲存可撐數年；來源以動物性食物或強化食品為主，蔬果不可靠。",
  },
  40: {
    explanation: explanation(
      `異體造血幹細胞移植能重建造血與免疫系統，也可為部分先天代謝疾病提供正常酵素來源；因此可用於嚴重再生不良性貧血、重度海洋性貧血與部分黏多醣症。肝細胞癌是實體肝臟腫瘤，不靠異體造血幹細胞移植達到長期緩解。`,
      `- A. 黏多醣症部分類型可透過造血幹細胞移植提供正常單核吞噬細胞來源與酵素，屬可考慮的適應症。\n- B. 嚴重再生不良性貧血是骨髓造血衰竭，年輕且有合適捐贈者時異體 HSCT 可達長期緩解或治癒。\n- C. 重度海洋性貧血可用異體 HSCT 取代缺陷造血系統，是少數可根治方式之一。\n- D. 肝細胞癌不是造血系統或可由造血細胞酵素補充改善的疾病，不能用異體 HSCT 作為長期緩解標準療法。`,
      `異體 HSCT 適合造血系統疾病、免疫缺陷或部分代謝疾病；一般實體癌如 HCC 不屬此類標準適應症。`
    ),
    key_point: "異體 HSCT 可治療造血衰竭、血紅素病與部分代謝病；肝細胞癌不靠 HSCT 達長期緩解。",
    flashcard_front: "異體造血幹細胞移植可用於哪些疾病？",
    flashcard_back: "可用於嚴重再生不良性貧血、重度海洋性貧血、部分黏多醣症；不適用於 HCC 這類實體肝癌。",
  },
  42: {
    explanation: explanation(
      `這位無抽菸女性有惡性胸水與兩側肺內轉移，屬晚期肺腺癌，PS 1 且器官功能可接受。最適當第一步是用腫瘤檢體做 EGFR mutation 與 ALK rearrangement 等驅動基因檢測，以決定全身性標靶或其他治療。`,
      `- A. 右下肺葉切除與縱膈淋巴廓清適合局部可切除疾病；本題已經有惡性胸水與雙肺轉移，不是手術根治情境。\n- B. Pleurodesis 可緩解反覆惡性胸水症狀，但不能處理全身性肺腺癌，也不是治療決策的最重要下一步。\n- C. 立體定位放射手術可用於小型局部病灶或寡轉移特定情境；本題是廣泛轉移，不應只照射原發腫瘤。\n- D. 正確。晚期非鱗狀非小細胞肺癌，尤其無抽菸女性，需檢測 EGFR、ALK 等驅動基因以選擇標靶治療。`,
      `晚期肺腺癌處置先做分子檢測再選全身治療；惡性胸水與雙肺轉移已非局部手術或單點放射治療問題。`
    ),
    key_point: "第四期肺腺癌應以腫瘤檢體進行 EGFR、ALK 等分子檢測，決定全身治療策略。",
    flashcard_front: "晚期肺腺癌、無抽菸女性：下一步最重要？",
    flashcard_back: "做 EGFR mutation、ALK rearrangement 等分子檢測，以決定標靶或全身治療；不是先手術切除。",
  },
  43: {
    explanation: explanation(
      `本題問氣胸何者正確。原發性自發性氣胸首次發作後復發率相當高，常用約三到五成描述，題目以約 50% 為正確選項；其他選項忽略了張力性氣胸臨床診斷、穿刺後氣胸成因與 COPD 次發性氣胸風險。`,
      `- A. 正確。Primary spontaneous pneumothorax 即使第一次改善後仍有高復發率，臨床需衛教戒菸與追蹤。\n- B. 錯誤。使用呼吸器者若突然低血壓、缺氧、氣道壓上升、單側呼吸音下降，張力性氣胸可由臨床立即診斷並先減壓。\n- C. 錯誤。胸腔穿刺後氣胸不一定是針刺破臟層胸膜，也可能與空氣進入系統、肺無法再擴張或 ex vacuo pneumothorax 有關。\n- D. 錯誤。COPD 病人是次發性氣胸，高風險且肺功能儲備差，常需要胸管或更積極處理，不能只用氧氣觀察一概處理。`,
      `氣胸處置要分 primary 與 secondary；COPD 氣胸風險高，張力性氣胸是臨床急症，不可等待影像才處理。`
    ),
    key_point: "原發性自發性氣胸復發率高；COPD 次發性氣胸與張力性氣胸需更積極處理。",
    flashcard_front: "氣胸：原發性復發率、張力性診斷、COPD 處置？",
    flashcard_back: "原發性自發性氣胸復發率高；張力性氣胸可臨床診斷並立即減壓；COPD 次發性氣胸常需胸管。",
  },
  46: {
    explanation: explanation(
      `非結核分枝桿菌可代表定殖、污染或真正疾病，尤其呼吸道檢體需結合症狀、影像與重複培養判斷。確認檢出 NTM 後不是一律立刻治療，所以 A 最不適當。`,
      `- A. 最不適當。NTM 肺部疾病治療時間長、副作用多，必須確認符合臨床、影像與微生物診斷標準，並評估病程與病人狀況。\n- B. 正確。NTM 肺部感染通常需多藥合併，以降低抗藥性與提高療效。\n- C. 正確。MAC 常用 macrolide 加 ethambutol，再加 rifampin 或 rifabutin，是典型組合。\n- D. 正確。M. kansasii 常對 rifampin 敏感，傳統治療包含 isoniazid、rifampin 與 ethambutol。`,
      `NTM 不是檢出就治療；先判斷是否為真正肺部疾病，再依菌種使用多藥療法。MAC 與 M. kansasii 的藥物組合要分清。`
    ),
    key_point: "NTM 檢出需先確認臨床疾病而非定殖；治療通常依菌種採多藥合併療法。",
    flashcard_front: "NTM 肺部感染：何時治療？MAC 與 M. kansasii 用藥？",
    flashcard_back: "不是檢出就治療，需符合臨床/影像/微生物標準；MAC 用 macrolide+ethambutol+rifamycin，M. kansasii 常用 INH+RIF+EMB。",
  },
  47: {
    explanation: explanation(
      `分化型甲狀腺癌經全甲狀腺切除與高劑量 I-131 後，正常甲狀腺組織應極少，血中 thyroglobulin 若上升就提示殘存或復發。T3、T4 與 TSH 主要用於甲狀腺功能與抑制治療監測，不是復發腫瘤標記。`,
      `- A. T4 反映甲狀腺素狀態與補充劑量，不能直接當作甲狀腺癌復發標記。\n- B. T3 也主要是功能性荷爾蒙指標，對追蹤分化型甲狀腺癌殘存或復發不如 thyroglobulin。\n- C. 正確。Thyroglobulin 由甲狀腺濾泡細胞產生，術後與放射碘後若仍可測得或逐漸上升，要懷疑殘餘或復發。\n- D. TSH 用於調整 levothyroxine 抑制治療與刺激 Tg 檢測，但 TSH 本身不是復發的腫瘤標記。`,
      `分化型甲狀腺癌追蹤記 thyroglobulin；medullary thyroid cancer 才想到 calcitonin/CEA。`
    ),
    key_point: "分化型甲狀腺癌全切除與 I-131 後，thyroglobulin 是追蹤復發的重要血液指標。",
    flashcard_front: "甲狀腺癌術後放射碘治療後追蹤復發看哪個指標？",
    flashcard_back: "分化型甲狀腺癌看 thyroglobulin；T3/T4 看功能，TSH 用於抑制治療調整。",
  },
  48: {
    explanation: explanation(
      `題目問低血糖何者最不適當。Insulinoma 會以 Whipple triad 表現，但它很罕見；臨床低血糖最常見原因多是糖尿病治療藥物，特別是胰島素或促胰島素分泌藥使用過量或進食不足。`,
      `- A. 最不適當。Whipple triad 可提示 insulinoma 或其他真性低血糖，但 insulinoma 不是低血糖最常見原因。\n- B. 正確。低血糖可造成癲癇、昏迷、心律不整甚至死亡，需要及時辨識與補糖。\n- C. 正確。交感神經症狀包含心悸、冒汗、焦慮、飢餓，神經缺糖可造成意識混亂、抽搐或昏迷。\n- D. 正確。胰島素、sulfonylureas 與 glinides 都可增加低血糖風險，尤其在腎功能差、進食少或劑量過高時。`,
      `低血糖臨床最常先想到藥物與進食/腎功能因素；insulinoma 雖是經典考題，但不是最常見病因。`
    ),
    key_point: "低血糖最常見原因是糖尿病藥物相關；insulinoma 有 Whipple triad 但罕見。",
    flashcard_front: "低血糖：最常見原因與 insulinoma 的考點？",
    flashcard_back: "最常見是胰島素、sulfonylurea、glinide 等藥物或進食不足；insulinoma 會有 Whipple triad 但罕見。",
  },
  49: {
    explanation: explanation(
      `非自主性體重流失常定義為 6-12 個月內體重下降超過 5% 或約 4.5 kg。甲狀腺功能亢進會增加基礎代謝，病人常食慾增加仍變瘦；說食慾減退是主因不正確。`,
      `- A. 正確。6-12 個月內減少約 4.5 kg 是常用警訊門檻之一，需評估惡性腫瘤、內分泌、慢性感染、心理與藥物原因。\n- B. 正確。體重下降大於原體重 5% 也是非自主性體重流失的重要定義。\n- C. 錯誤。甲亢造成體重下降主要因代謝率上升，典型反而會有食慾增加，不是食慾減退。\n- D. 正確。COPD 可因呼吸作功增加、慢性發炎與食慾下降造成 cachexia 或體重流失。`,
      `非自主體重減輕定義抓 5% 或 4.5 kg；甲亢是高代謝、常食慾增加但體重下降。`
    ),
    key_point: "非自主性體重流失常指 6-12 個月下降 >5% 或約 4.5 kg；甲亢常食慾增加但體重下降。",
    flashcard_front: "非自主性體重流失定義與甲亢體重下降機轉？",
    flashcard_back: "6-12 個月下降 >5% 或約 4.5 kg；甲亢因高代謝變瘦，常伴食慾增加而非減退。",
  },
  50: {
    explanation: explanation(
      `題目問脂質代謝何者錯誤。血液中乳糜微粒與 VLDL 內三酸甘油脂主要由 lipoprotein lipase 分解；hormone-sensitive lipase 位於脂肪細胞，負責動員儲存的三酸甘油脂，因此 B 錯。`,
      `- A. 正確。腸道吸收脂肪後在腸細胞組成 chylomicron，經乳糜管進入淋巴，再進入血液循環。\n- B. 錯誤。血中脂蛋白三酸甘油脂由 lipoprotein lipase 分解；hormone-sensitive lipase 分解脂肪細胞內儲存脂肪。\n- C. 正確。VLDL 釋放三酸甘油脂後形成 IDL，進一步轉為 LDL，負責運送膽固醇至周邊組織。\n- D. 正確。HDL 可透過 CETP 等機制和其他脂蛋白交換膽固醇酯與三酸甘油脂，參與反向膽固醇運輸。`,
      `LPL 在血管內皮處理血中 chylomicron/VLDL；HSL 在脂肪細胞內動員儲存脂肪。兩者名稱相近但位置與功能不同。`
    ),
    key_point: "血中三酸甘油脂由 LPL 分解；HSL 分解脂肪細胞內儲存的三酸甘油脂。",
    flashcard_front: "脂質代謝：LPL vs hormone-sensitive lipase？",
    flashcard_back: "LPL 分解血中 chylomicron/VLDL 的 TG；HSL 在脂肪細胞內動員儲存 TG。",
  },
  51: {
    explanation: explanation(
      `甲狀腺功能亢進合併心律不整時，應避免含大量碘且可能誘發或惡化甲狀腺功能異常的 amiodarone。控制心跳常優先使用 beta blocker，不能使用時可考慮非二氫吡啶類鈣離子阻斷劑。`,
      `- A. Digoxin 對甲亢造成的心房顫動可能較不靈敏、需要注意劑量，但它不是最典型會惡化甲亢的藥物。\n- B. 正確。Amiodarone 含碘量高且可造成甲狀腺毒症或甲狀腺低下，既有甲亢病人應盡量避免，除非特殊救命情境。\n- C. Propranolol 可降低交感症狀、控制心率，並部分抑制 T4 轉 T3，是甲亢心悸常用藥。\n- D. Diltiazem 可在 beta blocker 禁忌時用於心率控制，不會像 amiodarone 那樣因碘負荷惡化甲亢。`,
      `甲亢心律不整首選常是 beta blocker；amiodarone 因碘負荷與甲狀腺毒性，是考題最常要避免的藥。`
    ),
    key_point: "甲亢合併心律不整應避免 amiodarone；propranolol 常用於症狀與心率控制。",
    flashcard_front: "甲亢心律不整：哪個藥會惡化甲亢？",
    flashcard_back: "Amiodarone 含大量碘，可誘發或惡化甲狀腺毒症；propranolol 常用於控制甲亢症狀與心率。",
  },
  58: {
    explanation: explanation(
      `健康男性因牙結石接受牙科處置，沒有人工瓣膜、先前感染性心內膜炎、特定先天性心臟病或心臟移植瓣膜病等高風險條件，所以不需預防性抗生素。Penicillin 過敏只有在需要預防時才影響替代藥選擇。`,
      `- A. Clindamycin 不是本題答案，因為病人根本不符合心內膜炎預防性抗生素適應症；是否 penicillin 過敏不改變這點。\n- B. Vancomycin 不用於一般牙結石處置的健康者預防心內膜炎，過度使用反而增加副作用與抗藥性問題。\n- C. Tetracycline 也不是感染性心內膜炎牙科預防的標準選擇，且本題無預防需求。\n- D. 正確。一般健康人接受牙科清潔或牙結石處理，不需給預防性抗生素。`,
      `牙科處置預防感染性心內膜炎只給高風險心臟病人；沒有高風險條件時，不因牙科處置或 penicillin 過敏而給抗生素。`
    ),
    key_point: "感染性心內膜炎牙科預防只適用高風險心臟病人；健康者洗牙或牙結石處置不需抗生素。",
    flashcard_front: "牙科處置何時需預防感染性心內膜炎抗生素？",
    flashcard_back: "僅限高風險心臟病人如人工瓣膜、曾有 IE、特定先天心臟病等；一般健康者不需。",
  },
  63: {
    explanation: explanation(
      `承接第 62 題，病人排尿後仍有約 500 mL 餘尿，受壓時尿液緩慢溢出，屬溢流性尿失禁，常見機轉是前列腺肥大造成出口阻塞。能放鬆膀胱頸與前列腺平滑肌、降低尿道阻力的 alpha-blocker 最有幫助。`,
      `- A. 正確。Alpha-adrenergic antagonist 可放鬆前列腺與膀胱頸平滑肌，改善 BPH 造成的下泌尿道阻塞與尿滯留。\n- B. 骨盆底肌訓練主要用於應力性尿失禁，處理括約肌或骨盆底支持不足；對大量餘尿的溢流性尿失禁不是核心治療。\n- C. 抗膽鹼劑抑制逼尿肌收縮，適合部分急迫性尿失禁，但在尿滯留與大量餘尿時可能讓排尿更差。\n- D. Beta-3 agonist 可放鬆逼尿肌、改善膀胱過動症狀；對出口阻塞造成的溢流性尿失禁可能加重尿滯留風險。`,
      `溢流性尿失禁若來自 BPH/出口阻塞，治療要降低出口阻力；抗膽鹼或 beta-3 agonist 是過動膀胱藥物，不適合大量餘尿。`
    ),
    key_point: "BPH 造成尿滯留與溢流性尿失禁時，alpha-blocker 可降低出口阻力；抗膽鹼與 beta-3 agonist 可能加重滯留。",
    flashcard_front: "溢流性尿失禁合併 BPH：首選藥物方向？",
    flashcard_back: "使用 alpha-blocker 放鬆前列腺與膀胱頸；避免用抗膽鹼或 beta-3 agonist 加重尿滯留。",
  },
  66: {
    explanation: explanation(
      `周全性老年評估適合有多重問題、功能下降或反覆住院，且仍有介入後改善空間的老人。疾病末期或嚴重失智且預後不可逆者，評估能改變處置的機會有限，最不適合作為 CGA 對象。`,
      `- A. 最不適合。疾病末期或嚴重失智者照護重點常轉向舒適、預立醫療照護諮商與照顧者支持，完整 CGA 的效益較有限。\n- B. 多重疾病與多重用藥正是 CGA 常見適應症，可找出藥物交互作用、跌倒、營養與功能問題。\n- C. 日常生活功能不全且近期惡化，代表可能有可逆病因或照護需求改變，適合 CGA 統整評估。\n- D. 近期多次住院且原因不明時，CGA 可整合醫療、功能、認知、社會支持與居家安全，找出介入方向。`,
      `CGA 的價值在找出可治療、可介入的多面向問題；若已末期且介入不太可能改善功能，應改以安寧與照護目標為主。`
    ),
    key_point: "CGA 適合有多重問題且有改善潛力的老人；末期疾病或嚴重失智者較不適合完整 CGA。",
    flashcard_front: "周全性老年評估 CGA：誰最適合、誰較不適合？",
    flashcard_back: "適合多重疾病、多重用藥、功能退化或反覆住院且有改善空間者；末期或嚴重失智較不適合。",
  },
  67: {
    explanation: explanation(
      `17 歲女性半年瘦 10 公斤、口渴與多尿，最需要立即確認是否有高血糖，尤其要警覺第一型糖尿病與酮酸中毒風險。若只能安排一項檢查，指尖血糖最快速、最能直接支持診斷與下一步處置。`,
      `- A. 尿糖可提示高血糖，尿蛋白則非本題重點；尿檢不如血糖能即時量化高血糖程度。\n- B. 正確。指尖血糖可立即確認明顯高血糖，搭配典型症狀即可快速判斷糖尿病可能性並決定是否需急診評估 DKA。\n- C. 血清電解質對評估 DKA 嚴重度重要，但在只能做一項診斷檢查時，不如先確認血糖。\n- D. CBC 可評估感染或貧血，但不能診斷糖尿病，也無法解釋多尿、口渴與體重下降的核心問題。`,
      `年輕人多尿、口渴、消瘦要先量血糖；一旦高血糖明顯，再評估酮酸中毒、電解質與治療。`
    ),
    key_point: "年輕病人出現多尿、口渴與體重下降時，最直接診斷檢查是立即測血糖。",
    flashcard_front: "疑似第一型糖尿病：只能做一項檢查先做什麼？",
    flashcard_back: "先做指尖血糖測定，快速確認高血糖；之後再評估酮酸中毒與電解質。",
  },
  68: {
    explanation: explanation(
      `題目描述搜尋 Cochrane Library、MEDLINE，取得多個類似研究並合併分析，且報告 pooled OR 與信賴區間，這是綜合分析，也就是 meta-analysis。`,
      `- A. 錯誤。預後研究通常追蹤某族群看疾病結局與預後因子；本題是在合併多個 aspirin 隨機試驗結果。\n- B. 錯誤。治療效果問題通常以隨機對照試驗證據層級較高；case-control 不是此類療效分析優於 cohort 的設計。\n- C. 正確。把多個研究的資料用統計方法合併，並得到整體 OR 與 95% CI，就是 meta-analysis。\n- D. 錯誤。題幹只給平均追蹤 1.3 年與統計結果，沒有提供失訪比例，不能判斷追蹤完成率是否足夠。`,
      `EBM 設計辨識：合併多篇研究的統計結果是 meta-analysis；治療療效問題以 RCT 與其系統性回顧/綜合分析證據最強。`
    ),
    key_point: "檢索多個研究並合併統計結果、呈現 pooled effect size，屬於 meta-analysis。",
    flashcard_front: "EBM：多個 RCT 合併分析並報告 pooled OR 是什麼研究？",
    flashcard_back: "綜合分析 meta-analysis，通常建立在系統性回顧與統計合併之上。",
  },
  71: {
    explanation: explanation(
      `78 歲老人近期尿失禁、倦怠、失眠加重，自行增加安眠藥又自行購買降壓藥，呈現多重用藥、可能藥物副作用與功能問題。生命徵象穩定且無局部神經缺損時，最適合先做周全性老年評估，統整醫療、藥物、功能、認知與社會支持。`,
      `- A. 直接入住護理之家過早，題幹未顯示立即失去居家照護能力；應先評估可逆問題與照護需求。\n- B. 精神神經科可在需要時介入，但只調安眠藥會漏掉多重用藥、血壓藥自行使用、尿失禁與整體功能評估。\n- C. 正確。CGA 可系統性評估老人多重問題，找出藥物不良反應、跌倒風險、認知情緒、生活功能與照護資源。\n- D. 生命徵象穩定、意識清楚、無局部神經異常，沒有立即住院適應症；先門診整合評估較合適。`,
      `老人新出現症狀且伴多重用藥時，不要只看單一症狀；CGA 能找出可逆病因與照護計畫。`
    ),
    key_point: "老年人合併多重用藥、功能或尿失禁問題時，周全性老年評估可整合可逆病因與照護需求。",
    flashcard_front: "老年人多重用藥加新功能問題：下一步？",
    flashcard_back: "做周全性老年評估，統整藥物、功能、認知、情緒、營養、社會支持與照護計畫。",
  },
  73: {
    explanation: explanation(
      `癌症末期慢性疼痛治療強調規律給藥、足量止痛、優先口服、按階梯與個別化調整。若等到疼痛時才給藥，容易造成血中濃度起伏與突破痛，因此 B 是錯誤原則。`,
      `- A. 正確。能口服時優先口服，因為方便、非侵入且較易長期調整；吞嚥或吸收有問題時才考慮其他途徑。\n- B. 錯誤。慢性癌痛應按時給藥，並另外準備突破痛劑量；單純 PRN 會讓疼痛反覆失控。\n- C. 正確。神經病變痛、骨痛或發炎相關疼痛可合併輔助藥物，如抗癲癇藥、抗憂鬱藥、類固醇或 bisphosphonate 等。\n- D. 正確。多數癌痛若用正確藥物、劑量與時間間隔，並持續評估副作用，可得到明顯緩解。`,
      `癌痛控制記「by mouth、by the clock、by the ladder、for the individual」；慢性疼痛不是只在痛時才吃藥。`
    ),
    key_point: "慢性癌症疼痛應按時給藥並處理突破痛，不應以疼痛時才給藥為原則。",
    flashcard_front: "癌症末期疼痛治療：按時還是痛時才給？",
    flashcard_back: "慢性癌痛應 scheduled dosing，另給 breakthrough pain rescue dose；口服優先並可用輔助藥。",
  },
  74: {
    explanation: explanation(
      `急性口語不清與吞嚥困難提示腦幹相關神經功能障礙。非對比 CT 若在腦幹位置呈高密度病灶，代表急性出血；合併酗酒與熬夜後突然發作，最可能為腦幹出血，常見位置包含橋腦。`,
      `- A. 小腦梗塞可有眩暈、共濟失調、噁心嘔吐，CT 急性期通常不是腦幹高密度出血影像。\n- B. 小腦出血會在小腦半球或蚓部看到高密度出血，症狀可有頭痛、嘔吐與步態不穩，但題圖官方定位在腦幹。\n- C. 腦幹梗塞可造成口齒不清與吞嚥困難，但非對比 CT 急性梗塞多為低密度或早期不明顯，不是高密度出血樣病灶。\n- D. 正確。腦幹出血在非對比 CT 為腦幹高密度影，臨床可快速出現構音、吞嚥與意識或肢體神經症狀。`,
      `非對比 CT 判讀急性中風先分密度：高密度是出血，低密度或早期陰性偏梗塞；症狀定位再分小腦或腦幹。`
    ),
    key_point: "非對比 CT 腦幹高密度合併急性構音與吞嚥障礙，最支持腦幹出血。",
    flashcard_front: "急性腦幹症狀 + non-contrast CT 高密度：診斷？",
    flashcard_back: "腦幹出血；高密度代表急性出血，腦幹症狀包含構音、吞嚥、眼球運動、意識或肢體徵象。",
  },
  75: {
    explanation: explanation(
      `題目問肝臟超音波箭頭病灶最不可能是什麼。單純性肝囊腫典型為邊界清楚、完全無回音的黑色液體病灶，並有後方回音增強；若影像呈實體或混合回音病灶，就最不支持單純性囊腫。`,
      `- A. 肝膿瘍可呈複雜囊實性或混合回音病灶，邊界與內部回音可能不均，因此仍可能在影像鑑別中。\n- B. 原發性肝細胞癌常為實體肝臟腫瘤，超音波可呈低回音、高回音或混合回音，依大小與壞死而異。\n- C. 單純性囊腫是本題例外。它應該是無內部回音的液體病灶；若箭頭處不是典型無回音囊性外觀，就最不可能。\n- D. 轉移癌可在肝臟形成多樣實體性或 target-like 病灶，超音波表現變化大，也可列入鑑別。`,
      `超音波看到肝臟病灶，要先分液體囊性或實體性；單純囊腫應為 anechoic 加後方增強，實體回音病灶就不典型。`
    ),
    key_point: "單純性肝囊腫在超音波應為無回音液體病灶並有後方增強；實體或混合回音病灶不支持單純囊腫。",
    flashcard_front: "肝臟超音波：單純性囊腫的典型特徵？",
    flashcard_back: "邊界清楚、內部無回音、後方回音增強；若為實體或混合回音病灶，較不像單純囊腫。",
  },
  76: {
    explanation: explanation(
      `題目問中毒或藥物過量中，最不可能造成心搏過緩合併低血壓者。有機磷與 carbamate 會造成膽鹼性毒性，clonidine 會造成中樞交感抑制，三者都可有 bradycardia/hypotension；抗組織胺過量典型是抗膽鹼症候群，較常心跳過速。`,
      `- A. Organophosphates 抑制 acetylcholinesterase，造成 muscarinic 症狀如流涎、支氣管分泌增加、腹瀉、縮瞳，也可心搏過緩與低血壓。\n- B. Carbamates 同樣抑制 cholinesterase，臨床膽鹼性表現和有機磷相似，因此可造成心搏過緩與低血壓。\n- C. Clonidine 是 alpha-2 agonist，中毒會降低交感輸出，典型表現可有嗜睡、低血壓、心搏過緩與縮瞳。\n- D. Antihistamines 是本題例外。第一代抗組織胺過量常呈抗膽鹼毒性，包含心跳過速、瞳孔放大、皮膚乾熱、譫妄與癲癇風險。`,
      `中毒題用自律神經方向判斷：膽鹼性或 alpha-2 中樞抑制可慢脈低壓；抗膽鹼毒性多是快脈、乾、熱、譫妄。`
    ),
    key_point: "有機磷、carbamate 與 clonidine 可造成心搏過緩低血壓；抗組織胺過量多呈抗膽鹼性心跳過速。",
    flashcard_front: "中毒造成 bradycardia + hypotension：哪些藥常見？哪個例外？",
    flashcard_back: "有機磷、carbamate、clonidine 可慢脈低壓；抗組織胺過量多抗膽鹼，較常心跳過速。",
  },
  77: {
    explanation: explanation(
      `本題有官方更正，接受 C、D 為可給分答案。Lake Louise 急性高山病評估傳統症狀包含頭痛、腸胃症狀如噁心嘔吐、疲倦/虛弱、頭暈，以及早期版本曾包含睡眠障礙；後續版本移除睡眠項目，因此官方接受「腹瀉」與「失眠」兩個答案。`,
      `- A. 頭痛是急性高山病評估的核心症狀，沒有頭痛時通常不符合典型 AMS 判定，所以不屬於排除項。\n- B. 噁心、嘔吐屬 Lake Louise 評估中的腸胃症狀，屬於常見 AMS 表現。\n- C. 腹瀉是官方接受答案之一。AMS 的腸胃項目重點是食慾差、噁心或嘔吐，腹瀉不是典型評分項目。\n- D. 失眠也是官方接受答案之一。舊版 Lake Louise 曾包含睡眠障礙，但新版評估移除此項，造成考題答案更正為多重給分。`,
      `Lake Louise AMS 評估要看版本：頭痛與噁心嘔吐是典型項目；腹瀉不是典型項目，睡眠障礙在新版已移除。本題依官方更正接受 C、D。`
    ),
    key_point: "Lake Louise AMS 官方更正接受 C、D；腹瀉不是典型評分項，睡眠障礙在新版已移除。",
    flashcard_front: "Lake Louise AMS：本題官方更正接受哪些答案？",
    flashcard_back: "接受 C 腹瀉與 D 失眠；頭痛、噁心嘔吐屬典型 AMS 症狀，睡眠障礙因版本差異已由新版移除。",
    manual_review_notes: ["本題為官方更正多重答案，correct_answers 已接受 C、D；解釋需保留版本差異。"],
  },
  79: {
    explanation: explanation(
      `醫師不得在未親自診察病人的情況下，由護理人員直接蓋章讓病人拿藥。即使是慢性病續方，也需要符合親自診療、病歷與處方責任等法律與專業要求；方便病人不能取代醫師責任。`,
      `- A. 正確。王醫師未親自診療卻授權護士代蓋章開藥，違反親自診療與處方責任。\n- B. 錯誤。行政方便不能免除醫師法定義務；未評估病情變化與用藥安全會增加風險。\n- C. 錯誤。釋出處方箋仍須由醫師依診療結果開立，不能用形式上的處方替代實際診察。\n- D. 錯誤。電話問診是否可行需受法規與醫療情境限制；本題描述的是護士直接蓋章拿藥，並非合規遠距醫療流程。`,
      `處方代表醫師對診療判斷與用藥安全負責；未親自診療或未合規完成遠距診療時，不能讓他人代蓋章發藥。`
    ),
    key_point: "醫師開立處方須基於親自診療或合規診療流程，不能授權護士代蓋章讓病人直接拿藥。",
    flashcard_front: "醫師可否讓護士代蓋章續開處方？",
    flashcard_back: "不可以。處方須基於醫師親自診療或合規流程，醫師不能把診療與處方責任交由護士代蓋章。",
  },
};

const BATCHES = [
  { file: "q001-q011_sparse_20260916.json", nums: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11] },
  { file: "q012-q024_sparse_20260916.json", nums: [12, 13, 14, 15, 17, 18, 19, 20, 23, 24] },
  { file: "q025-q035_sparse_20260916.json", nums: [25, 26, 27, 28, 29, 30, 32, 33, 34, 35] },
  { file: "q036-q049_sparse_20260916.json", nums: [36, 37, 38, 40, 42, 43, 46, 47, 48, 49] },
  { file: "q050-q074_sparse_20260916.json", nums: [50, 51, 58, 63, 66, 67, 68, 71, 73, 74] },
  { file: "q075-q079_sparse_20260916.json", nums: [75, 76, 77, 79] },
];

function buildQuestionUpdate(question, update) {
  const flashcardSummary = update.flashcard_summary ?? `${update.flashcard_front} -> ${update.flashcard_back}`;
  return {
    question_id: question.id,
    question_number: question.question_number,
    explanation: update.explanation,
    key_point: update.key_point,
    flashcard_front: update.flashcard_front,
    flashcard_back: update.flashcard_back,
    flashcard_summary: flashcardSummary,
    review_status: "ai_generated",
    explanation_model: MODEL,
    explanation_generated_at: GENERATED_AT,
    manual_review_notes: update.manual_review_notes ?? [],
  };
}

function main() {
  const source = JSON.parse(fs.readFileSync(SOURCE_FILE, "utf8"));
  const questions = source.questions;
  const byNumber = new Map(questions.map((question) => [question.question_number, question]));
  const allBatchNumbers = BATCHES.flatMap((batch) => batch.nums);
  const updateNumbers = Object.keys(UPDATES).map(Number).sort((a, b) => a - b);

  if (allBatchNumbers.length !== updateNumbers.length) {
    throw new Error(`Batch count ${allBatchNumbers.length} does not match update count ${updateNumbers.length}`);
  }
  for (const number of updateNumbers) {
    if (!allBatchNumbers.includes(number)) {
      throw new Error(`Question ${number} exists in UPDATES but not in BATCHES`);
    }
    if (!byNumber.has(number)) {
      throw new Error(`Question ${number} not found in source`);
    }
  }

  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  for (const batch of BATCHES) {
    const updates = batch.nums.map((number) => buildQuestionUpdate(byNumber.get(number), UPDATES[number]));
    const updateFile = {
      source_file: SOURCE_FILE,
      dataset_id: DATASET_ID,
      range: { start: Math.min(...batch.nums), end: Math.max(...batch.nums) },
      updates,
    };
    fs.writeFileSync(path.join(OUTPUT_DIR, batch.file), `${JSON.stringify(updateFile, null, 2)}\n`, "utf8");
  }

  for (const number of updateNumbers) {
    const question = byNumber.get(number);
    const update = buildQuestionUpdate(question, UPDATES[number]);
    question.explanation = update.explanation;
    question.key_point = update.key_point;
    question.flashcard_front = update.flashcard_front;
    question.flashcard_back = update.flashcard_back;
    question.flashcard_summary = update.flashcard_summary;
    question.review_status = update.review_status;
    question.explanation_model = update.explanation_model;
    question.explanation_generated_at = update.explanation_generated_at;
    question.manual_review_notes = update.manual_review_notes;
  }

  fs.writeFileSync(SOURCE_FILE, `${JSON.stringify(source, null, 2)}\n`, "utf8");
  console.log(`Wrote ${BATCHES.length} update files and merged ${updateNumbers.length} questions into ${SOURCE_FILE}`);
}

main();
