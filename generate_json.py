import json
from datetime import datetime

updates = [
  {
    "question_id": "108-2_medicine-2_081",
    "question_number": 81,
    "explanation": "【題幹解析】\n本題詢問與 Li-Fraumeni 症候群（LFS）最相關的基因突變。LFS 是一種體染色體顯性遺傳癌症症候群，與抑癌基因 TP53 的生殖細胞突變直接相關。\n\n【選項詳解】\n- A. 錯誤，RB 基因突變主要與視網膜母細胞瘤（retinoblastoma）及骨肉瘤（osteosarcoma）相關。\n- B. 正確，TP53 是調控細胞週期的重要抑癌基因，其生殖細胞突變會導致 Li-Fraumeni 症候群，患者容易在年輕時罹患乳癌、肉瘤、腦瘤及白血病等多種癌症。\n- C. 錯誤，WT-1 基因突變與 Wilms tumor（威耳姆氏腫瘤，一種兒童腎臟惡性腫瘤）相關，常見於 WAGR 症候群或 Denys-Drash 症候群。\n- D. 錯誤，BRCA-1 及 BRCA-2 基因變異主要與遺傳性乳癌及卵巢癌相關，雖然也增加早發性癌症風險，但並非 Li-Fraumeni 症候群的致病基因。\n\n【核心考點】\nLi-Fraumeni 症候群由 TP53 抑癌基因突變引起，特徵為年輕患者發生多種原發性癌症（如肉瘤、乳癌、腦瘤及腎上腺皮質癌）。",
    "key_point": "Li-Fraumeni 症候群由 TP53 抑癌基因突變引起，特徵為年輕患者發生多種原發性癌症。",
    "flashcard_front": "Li-Fraumeni 症候群最常見的基因變異為何？",
    "flashcard_back": "TP53 基因的生殖細胞突變。",
    "flashcard_summary": "Li-Fraumeni syndrome 與 TP53",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-20T16:40:31+08:00",
    "manual_review_notes": []
  },
  {
    "question_id": "108-2_medicine-2_083",
    "question_number": 83,
    "explanation": "【題幹解析】\n本題測驗「依賴動脈導管（ductus-dependent）的先天性心臟病」。當左心或右心出口嚴重阻塞時，體循環或肺循環必須仰賴未閉合的動脈導管（PDA）來維持血液灌注。\n\n【選項詳解】\n- A. 錯誤，心室中隔缺損（VSD）會造成左向右分流，但不依賴動脈導管維持基本生命跡象。\n- B. 錯誤，成人型的主動脈縮窄主要依賴側枝循環（collateral circulation），雖然嬰兒型主動脈縮窄在動脈導管關閉前可能依賴其供應下半身血流，但相比主動脈閉鎖，主動脈閉鎖對 PDA 的依賴更為絕對與立即。\n- C. 錯誤，心房中隔缺損（ASD）通常早期無明顯症狀，且不需依賴開放的動脈導管來維持體循環或肺循環。\n- D. 正確，主動脈閉鎖屬於嚴重的左心阻塞型病變（如左心發育不全症候群），左心室無法將血液打入主動脈，體循環完全依賴右心室的血液經由動脈導管（PDA）進行右向左分流，若 PDA 關閉將導致心輸出量驟降而致死。\n\n【核心考點】\n主動脈閉鎖等嚴重的左心阻塞病變是依賴動脈導管的心臟病（ductus-dependent lesions），需持續給予前列腺素 E1（PGE1）以維持動脈導管開放。",
    "key_point": "主動脈閉鎖等嚴重左心阻塞病變屬於依賴動脈導管的心臟病，必須維持 PDA 開放以供應體循環血流。",
    "flashcard_front": "為何主動脈閉鎖的嬰兒必須維持動脈導管開放？",
    "flashcard_back": "因為左心室無法有效輸出血液，體循環必須仰賴右心室的血液經由動脈導管進行右向左分流來維持供血。",
    "flashcard_summary": "主動脈閉鎖與 PDA 依賴",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-20T16:40:31+08:00",
    "manual_review_notes": []
  },
  {
    "question_id": "108-2_medicine-2_084",
    "question_number": 84,
    "explanation": "【題幹解析】\n本題測驗何杰金氏淋巴瘤（Hodgkin lymphoma）的病理及臨床特徵。其最顯著的病理特點在於真正的腫瘤細胞（Reed-Sternberg cells）數量極少，背景充滿反應性的發炎細胞。\n\n【選項詳解】\n- A. 錯誤，何杰金氏淋巴瘤的治療效果通常極佳，整體存活率及治癒率皆顯著高於大多數的非何杰金氏淋巴瘤（non-Hodgkin lymphoma）。\n- B. 錯誤，何杰金氏淋巴瘤通常起源於單一或一組相鄰的淋巴結（如頸部、縱膈腔），並以連續性的方式向周圍淋巴結擴散，極少在早期就侵犯淋巴結以外的器官。\n- C. 正確，何杰金氏淋巴瘤的病理特徵是真正的腫瘤巨細胞（Reed-Sternberg cells 及其變異型）僅占總細胞群的 1-5%，其餘絕大多數為反應性發炎細胞，如淋巴球、嗜酸性白血球、組織球及漿細胞。\n- D. 錯誤，何杰金氏淋巴瘤的預後主要取決於臨床分期（stage），臨床分期對存活率及治療計畫的影響遠大於病理亞型。\n\n【核心考點】\n何杰金氏淋巴瘤以局部淋巴結起病，治癒率高，病理切片下典型的 Reed-Sternberg 腫瘤巨細胞僅占極少數（1-5%），多數為反應性發炎細胞。預後主要由臨床分期決定。",
    "key_point": "何杰金氏淋巴瘤真正的腫瘤巨細胞僅占 1-5%，其餘為反應性發炎細胞；臨床分期對預後影響大於病理亞型。",
    "flashcard_front": "何杰金氏淋巴瘤的腫瘤細胞在病灶中的比例特徵為何？",
    "flashcard_back": "真正的腫瘤巨細胞（如 Reed-Sternberg 細胞）僅占極小部分（1-5%），多數為反應性發炎細胞。",
    "flashcard_summary": "何杰金氏淋巴瘤的細胞組成",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-20T16:40:31+08:00",
    "manual_review_notes": []
  },
  {
    "question_id": "108-2_medicine-2_085",
    "question_number": 85,
    "explanation": "【題幹解析】\n本題詢問單株丙型球蛋白病變（monoclonal gammopathy）的特徵。此病變是因單一克隆的漿細胞（plasma cell）異常增生而產生大量單株免疫球蛋白（M protein）。\n\n【選項詳解】\n- A. 錯誤，急性發炎或感染反應通常會刺激多種 B 細胞及漿細胞，引起多株性（polyclonal）丙型球蛋白增生，而單株丙型球蛋白病變多見於腫瘤性疾病（如多發性骨髓瘤）或意義未明之單株斑球蛋白血症（MGUS）。\n- B. 正確，Bence-Jones 蛋白尿是指尿中出現游離的輕鏈（light chains），雖然常見於多發性骨髓瘤，但在部分單株丙型球蛋白病變（如只分泌完整免疫球蛋白而無過多輕鏈者）不一定會出現。\n- C. 正確，重鏈病（heavy chain disease）是單株丙型球蛋白病變的一種罕見亞型，其漿細胞僅分泌不完整的免疫球蛋白重鏈。\n- D. 正確，單株丙型球蛋白病變涵蓋多種疾病，如意義未明之單株斑球蛋白血症（MGUS）患者血液中雖有 M 蛋白，但無明顯的漿細胞瘤形成，也無多發性骨髓瘤的骨頭痛或腎病等臨床症狀。\n\n【核心考點】\n急性發炎會導致「多株性」免疫球蛋白上升；單株丙型球蛋白病變源於單一漿細胞克隆增生，涵蓋多發性骨髓瘤、MGUS 及重鏈病等，不一定皆伴隨 Bence-Jones 蛋白或惡性腫瘤。",
    "key_point": "單株丙型球蛋白病變源自單一漿細胞克隆，而急性發炎常導致多株性丙型球蛋白增生。",
    "flashcard_front": "急性發炎病人的免疫球蛋白增生通常是單株性還是多株性？",
    "flashcard_back": "多株性（polyclonal gammopathy）。單株增生多見於漿細胞腫瘤或 MGUS。",
    "flashcard_summary": "急性發炎與丙型球蛋白病變",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-20T16:40:31+08:00",
    "manual_review_notes": []
  },
  {
    "question_id": "108-2_medicine-2_086",
    "question_number": 86,
    "explanation": "【題幹解析】\n本題測驗機化性肺炎（organizing pneumonia，常被稱為隱源性機化性肺炎 COP 或 BOOP）的病理特徵。其核心病理表現為細支氣管與肺泡內出現機化組織。\n\n【選項詳解】\n- A. 正確敘述，機化性肺炎的典型病理特徵是在肺泡腔及細支氣管內，出現由纖維母細胞與結締組織構成的息肉狀機化組織栓（Masson bodies）。\n- B. 錯誤敘述，機化性肺炎的全名為「閉塞性細支氣管炎伴機化性肺炎（BOOP）」，其病變明確累及細支氣管（小支氣管）與肺泡，形成管腔內的結締組織栓塞。\n- C. 正確敘述，此病變的發炎和纖維化主要侷限於肺泡與細支氣管的「管腔內」，通常不會引起顯著的間質性纖維化（interstitial fibrosis）。\n- D. 正確敘述，蜂巢狀纖維化（honeycomb fibrosis）是末期不可逆的間質性肺病（如特發性肺纖維化 UIP）的特徵，機化性肺炎對類固醇治療反應良好，通常無蜂巢狀變化。\n\n【核心考點】\n機化性肺炎（COP/BOOP）的病理特徵為細支氣管與肺泡腔內出現 Masson bodies（纖維母細胞增生栓塞），病變涉及小支氣管，但不會造成嚴重的間質纖維化或蜂巢肺。",
    "key_point": "機化性肺炎（BOOP）病灶累及小支氣管及肺泡，特徵為管腔內的 Masson bodies，通常無嚴重間質性纖維化。",
    "flashcard_front": "機化性肺炎（organizing pneumonia）的典型病理特徵（Masson bodies）位於何處？",
    "flashcard_back": "位於肺泡腔及細支氣管（小支氣管）管腔內。",
    "flashcard_summary": "機化性肺炎的病理特徵",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-20T16:40:31+08:00",
    "manual_review_notes": []
  },
  {
    "question_id": "108-2_medicine-2_088",
    "question_number": 88,
    "explanation": "【題幹解析】\n本題測驗肺膨脹不全（atelectasis）的成因分類。肺膨脹不全是指部分或全部肺葉塌陷或失去含氣狀態，通常分為阻塞性（吸收性）、壓迫性及收縮性三大類。\n\n【選項詳解】\n- A. 常見，氣道阻塞（如異物、腫瘤或濃稠痰液阻塞）會使遠端肺泡氣體被吸收，導致阻塞性肺膨脹不全（resorption atelectasis）。\n- B. 常見，肋膜腔積水、氣胸或腹部腫瘤會由外向內壓迫肺臟實質，造成壓迫性肺膨脹不全（compression atelectasis）。\n- C. 常見，肺泡表面張力素（surfactant）不足（如新生兒呼吸窘迫症候群）會使肺泡表面張力過大，導致廣泛的微小肺泡塌陷（microatelectasis）。\n- D. 最少見，急性肺炎的主要病理變化是肺泡腔內充滿發炎細胞與滲出液，導致肺實質化（consolidation），而非肺泡塌陷萎縮，因此較少直接造成肺膨脹不全。\n\n【核心考點】\n肺膨脹不全常見於氣道阻塞、外部壓迫（積水/氣胸）、表面張力素不足或局部纖維化收縮；急性肺炎的特徵是肺泡充滿滲出液的「實質化」，而非「塌陷」。",
    "key_point": "急性肺炎主要造成肺泡實質化（consolidation），而非肺膨脹不全（塌陷）。",
    "flashcard_front": "急性肺炎為何較不會造成肺膨脹不全？",
    "flashcard_back": "因為急性肺炎主要是發炎滲出液充滿肺泡腔造成實質化，而非空氣被吸收或外部壓迫造成的塌陷。",
    "flashcard_summary": "急性肺炎與肺膨脹不全",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-20T16:40:31+08:00",
    "manual_review_notes": []
  },
  {
    "question_id": "108-2_medicine-2_090",
    "question_number": 90,
    "explanation": "【題幹解析】\n本題測驗肝細胞腺瘤（hepatocellular adenoma, HCA）的分類與各亞型的特徵。HCA 主要分為三種基因突變亞型：HNF1-alpha 失活型、β-catenin 活化型及發炎型。\n\n【選項詳解】\n- A. 正確敘述，肝細胞腺瘤（HCA）是肝細胞的良性腫瘤，通常與年輕女性長期使用口服避孕藥有關。\n- B. 正確敘述，HNF1-alpha 失活型腺瘤（inactivated HCA）與年輕人成年型糖尿病第三型（MODY-3）有密切關聯，此亞型惡性轉化風險極低，多見於女性。\n- C. 錯誤敘述，β-catenin 活化型腺瘤（activated HCA）在所有 HCA 亞型中具有「最高」的惡性化風險，極易轉變為肝細胞癌（HCC），常見於男性，通常建議手術切除。\n- D. 正確敘述，發炎型腺瘤（inflammatory HCA）常伴隨 IL-6 訊息傳遞路徑的基因突變，最常見的突變基因即為 gp130，患者常有 CRP 升高等發炎表現。\n\n【核心考點】\n肝細胞腺瘤（HCA）的三大亞型：β-catenin 活化型惡性轉化率最高；HNF1-alpha 失活型與口服避孕藥及 MODY-3 相關，惡性率極低；發炎型與 gp130 突變及 IL-6 路徑相關。",
    "key_point": "β-catenin 活化型肝細胞腺瘤在各亞型中具有最高的惡性轉化風險。",
    "flashcard_front": "肝細胞腺瘤（HCA）中，哪一個基因突變亞型的惡性化為肝細胞癌的風險最高？",
    "flashcard_back": "β-catenin 活化型（beta-catenin activated adenoma）。",
    "flashcard_summary": "β-catenin 活化型 HCA 的惡性風險",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-20T16:40:31+08:00",
    "manual_review_notes": []
  },
  {
    "question_id": "108-2_medicine-2_095",
    "question_number": 95,
    "explanation": "【題幹解析】\n本題測驗前列腺癌的常見基因與染色體變異。前列腺癌的發生常與特定基因融合及抑癌基因的缺失有關。\n\n【選項詳解】\n- A. 常見，約 40-50% 的前列腺癌具有 TMPRSS2（雄性素調控啟動子）與 ETS 家族轉錄因子（如 ERG 或 ETV1）的基因融合，這是前列腺癌最常見的早期基因變異。\n- B. 不常見（錯誤敘述），染色體 8q24 區域包含致癌基因 c-MYC，在前列腺癌中通常是發生基因「擴增（amplification）」，導致 c-MYC 過度表現以促進癌症進展，而非「缺失」。\n- C. 常見，PTEN 是重要的抑癌基因，其缺失（deletion）會導致 PI3K/AKT 訊息傳遞路徑過度活化，是晚期或侵襲性前列腺癌非常常見的基因變異。\n- D. 常見，TP53 是關鍵的抑癌基因，其缺失或突變常見於多種癌症，在前列腺癌的疾病進展及去勢抗性前列腺癌中也常觀察到 TP53 變異。\n\n【核心考點】\n前列腺癌常見的基因變化包括 TMPRSS2-ERG 基因融合、PTEN 缺失及 TP53 變異。染色體 8q24 含致癌基因 MYC，在攝護腺癌中會發生「擴增」而非缺失。",
    "key_point": "前列腺癌中，染色體 8q24 上的 MYC 基因常發生「擴增」而非缺失。",
    "flashcard_front": "前列腺癌中，染色體 8q24 區域通常會發生擴增還是缺失？為什麼？",
    "flashcard_back": "擴增（amplification）。因為該區域包含致癌基因 c-MYC，擴增會促進癌症發展。",
    "flashcard_summary": "前列腺癌的染色體 8q24 變異",
    "review_status": "ai_generated",
    "explanation_model": "codex-high-quality-rewrite",
    "explanation_generated_at": "2026-07-20T16:40:31+08:00",
    "manual_review_notes": []
  }
]

output_data = {
  "source_file": "public/data/exams/108-2/medicine-2.json",
  "dataset_id": "108-2_medicine-2",
  "range": { "start": 81, "end": 95 },
  "updates": updates
}

import os
os.makedirs('d:\\Antigravity\\med_exam_public\\scratch\\rewrite_updates\\108-2_medicine-2', exist_ok=True)
with open('d:\\Antigravity\\med_exam_public\\scratch\\rewrite_updates\\108-2_medicine-2\\q080-q095_selected.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("JSON file successfully written.")
