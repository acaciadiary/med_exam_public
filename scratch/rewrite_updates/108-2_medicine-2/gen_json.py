import json
from datetime import datetime

updates = [
    {
      "question_id": "108-2_medicine-2_021",
      "question_number": 21,
      "explanation": "【題幹解析】\n本題測驗T細胞在胸腺發育過程中的pre-T cell receptor (pre-TCR)結構特徵。pre-TCR是由已經重組成功的TCR β鏈與一條不變的替代α鏈 (pre-Tα, pTα) 所組成。\n\n【選項詳解】\n- A. pre-TCR階段尚未進行TCR α鏈的基因重組，而是由替代性的pre-Tα鏈來穩定TCR β鏈。\n- B. 正確敘述。T細胞發育時先進行β鏈基因重組，重組成功的β鏈會與pre-Tα結合形成pre-TCR，此結構會傳遞訊號促進細胞增殖並進入下一發育階段。\n- C. pre-TCR的主要功能是傳遞存活與增殖訊號（β-selection），尚未具備成熟TCR α/β二聚體，因此無法辨識外來抗原。\n- D. 辨識自體MHC的能力是在產生完整TCR α/β後，於正向選擇 (positive selection) 階段才進行測試，pre-T細胞尚無此能力。\n\n【核心考點】\npre-TCR由重組成功的TCR β鏈和替代性的pre-Tα鏈組成，負責傳遞存活與增殖訊號（β-selection），此時尚未能辨識抗原或MHC。",
      "key_point": "pre-TCR由TCR β鏈與替代性pre-Tα鏈組成，只負責傳遞存活增殖訊號，不能辨識外來抗原或MHC。",
      "flashcard_front": "pre-TCR (pre-T cell receptor) 的結構為何？具備什麼功能？",
      "flashcard_back": "結構：已重組成功的 TCR β 鏈 + 替代性 pre-Tα 鏈。\n功能：傳遞存活與增殖訊號（β-selection），尚無法辨識抗原或自體MHC。",
      "flashcard_summary": "pre-TCR 結構與功能",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": datetime.now().isoformat(),
      "manual_review_notes": []
    },
    {
      "question_id": "108-2_medicine-2_022",
      "question_number": 22,
      "explanation": "【題幹解析】\n本題測驗調節型T細胞 (Treg) 的生成、表面標記與免疫調控功能。Treg 負責抑制免疫反應、維持自體耐受性，而在腫瘤微環境中常被腫瘤利用以逃避免疫監測。\n\n【選項詳解】\n- A. 正確敘述。腫瘤細胞會分泌如TGF-β等細胞激素，誘導腫瘤微環境中的T細胞分化為誘導型Treg (iTreg)，進而抑制抗腫瘤免疫反應。\n- B. 自體免疫疾病的發生通常是因為Treg細胞功能「低下」或數量不足，導致無法有效抑制對抗自體抗原的免疫反應。\n- C. Treg分為在胸腺發育成熟的自然型Treg (nTreg) 以及在周邊淋巴組織受抗原與細胞激素刺激分化而成的誘導型Treg (iTreg)，並非全在周邊分化。\n- D. 典型的Treg細胞表面標記為CD4+、CD25+及轉錄因子Foxp3+，而負責清除胞內病原感染的主要是CD8+ 毒殺型T細胞 (CTL)。\n\n【核心考點】\nTreg表現CD4、CD25與Foxp3，功能為抑制免疫反應；腫瘤常分泌TGF-β誘導Treg生成以達成免疫逃避，而Treg功能不足則會導致自體免疫疾病。",
      "key_point": "Treg功能為抑制免疫反應；腫瘤會誘導微環境中的T細胞分化為Treg以逃避免疫系統。",
      "flashcard_front": "腫瘤如何利用調節型T細胞 (Treg) 逃避免疫監測？",
      "flashcard_back": "腫瘤微環境會分泌 TGF-β 等細胞激素，誘導周邊 T 細胞分化為 Treg，進而抑制抗腫瘤的免疫反應。",
      "flashcard_summary": "腫瘤與Treg的關係",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": datetime.now().isoformat(),
      "manual_review_notes": []
    },
    {
      "question_id": "108-2_medicine-2_023",
      "question_number": 23,
      "explanation": "【題幹解析】\n本題測驗濾泡輔助型T細胞 (TFH) 在B細胞活化及抗體類別轉換中的角色與作用機轉。TFH是幫助B細胞進行親和力成熟與抗體類別轉換的關鍵CD4+ T細胞。\n\n【選項詳解】\n- A. B細胞在生發中心 (germinal center) 增殖後會進入淺色區 (light zone)，在此與TFH細胞及濾泡樹突細胞 (FDC) 互動，進行親和力篩選。\n- B. Bcl-6是TFH細胞分化的關鍵轉錄因子，會抑制其他T helper細胞路徑並促進TFH相關基因表現。\n- C. TFH細胞會分泌IL-21，此細胞激素能強力促進B細胞增殖、分化為漿細胞，並協助抗體親和力成熟。\n- D. 錯誤敘述。TFH細胞要刺激B細胞進行抗體類別轉換（如產生IgG1），除了分泌IL-21外，還必須提供「接觸性」共刺激訊號（如CD40L與B細胞上的CD40結合）。單靠LPS、IL-2與IL-21等可溶性因子不足以完全替代TFH細胞提供的接觸依賴性幫助。\n\n【核心考點】\nTFH細胞在生發中心淺色區透過CD40L-CD40接觸性訊號及分泌IL-21，協助B細胞進行親和力成熟及抗體類別轉換，轉錄因子為Bcl-6。",
      "key_point": "TFH促進B細胞產生特定抗體必須同時提供IL-21與CD40L-CD40的細胞接觸訊號，單靠細胞激素無法取代。",
      "flashcard_front": "濾泡輔助型T細胞 (TFH) 幫助B細胞活化的兩個關鍵機制為何？",
      "flashcard_back": "1. 接觸性訊號：透過細胞表面的 CD40L 與 B 細胞的 CD40 結合。\n2. 可溶性訊號：分泌細胞激素 IL-21。\n兩者缺一不可。",
      "flashcard_summary": "TFH活化B細胞的機制",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": datetime.now().isoformat(),
      "manual_review_notes": []
    },
    {
      "question_id": "108-2_medicine-2_024",
      "question_number": 24,
      "explanation": "【題幹解析】\n本題測驗腸道共生菌群的生理意義及其與抗生素或免疫狀態的互動。正常共生菌對維持腸道恆定與免疫屏障至關重要。\n\n【選項詳解】\n- A. 錯誤敘述。長期使用廣效型抗生素會破壞腸道正常共生菌相（dysbiosis），導致致病菌（如困難梭狀桿菌 C. difficile）伺機增殖，引起偽膜性腸炎等嚴重疾病，無法保持腸道健康。\n- B. 腸道共生菌能協助消化代謝、合成維生素、與宿主免疫系統交互作用並透過空間與營養競爭抑制致病菌生長。\n- C. 腸道菌相的組成改變（dysbiosis）已被證實與多種代謝疾病（如肥胖、第二型糖尿病）及發炎性腸道疾病密切相關。\n- D. 免疫抑制劑會削弱宿主黏膜免疫與全身性免疫功能，使得原本不致病的共生菌或外來病原體容易在腸道引發嚴重伺機性感染。\n\n【核心考點】\n腸道共生菌有助於宿主代謝與抵抗致病菌；濫用廣效型抗生素會破壞正常菌相，引發伺機性感染（如C. difficile感染）。",
      "key_point": "廣效型抗生素會殺死正常腸道共生菌，導致菌相失衡與伺機性感染（如偽膜性腸炎）。",
      "flashcard_front": "長期使用廣效型抗生素對腸道有何負面影響？",
      "flashcard_back": "會破壞正常的腸道共生菌相 (dysbiosis)，降低空間與營養競爭，容易導致致病菌（如困難梭狀桿菌 Clostridium difficile）伺機增殖，引起偽膜性腸炎。",
      "flashcard_summary": "廣效抗生素破壞腸道菌相",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": datetime.now().isoformat(),
      "manual_review_notes": []
    },
    {
      "question_id": "108-2_medicine-2_026",
      "question_number": 26,
      "explanation": "【題幹解析】\n本題測驗免疫系統維持自體耐受性（防止對自身抗原產生免疫反應）的機制。自體耐受性包含中樞與周邊機制，主要依賴消滅或抑制具有自體反應性的淋巴球。\n\n【選項詳解】\n- A. 周邊不反應 (anergy) 是指周邊組織中的T或B細胞在辨識自體抗原時，若缺乏適當的共刺激訊號（如CD28-B7結合），細胞會進入長期功能性失活狀態。\n- B. 株落刪除 (clonal deletion) 是指透過細胞凋亡機制，清除具有強烈自體反應性的淋巴球，是中樞耐受性（負向選擇）的主要機制。\n- C. 錯誤敘述。株落增殖 (clonal proliferation) 是淋巴球辨識到外來抗原並被活化後進行的大量增生反應，目的是產生對抗病原的效應細胞，與「建立耐受性」的抑制機制相反。\n- D. 中樞耐受性發生在初級淋巴器官（骨髓、胸腺），透過負向選擇將辨識自體抗原的未成熟淋巴球刪除。\n\n【核心考點】\n自體耐受性透過中樞的株落刪除（負向選擇）與周邊的無能/不反應 (anergy)、調節型T細胞抑制來達成；株落增殖則是免疫活化的表現。",
      "key_point": "自體耐受性機制包括株落刪除、周邊不反應(anergy)與Treg抑制，而株落增殖(proliferation)是免疫活化反應。",
      "flashcard_front": "達成免疫系統自體耐受性 (self-tolerance) 的機轉有哪些？",
      "flashcard_back": "1. 中樞耐受性：株落刪除 (clonal deletion)。\n2. 周邊耐受性：周邊不反應/無能 (anergy)、株落刪除、調節型 T 細胞 (Treg) 抑制。",
      "flashcard_summary": "自體耐受性機轉",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": datetime.now().isoformat(),
      "manual_review_notes": []
    },
    {
      "question_id": "108-2_medicine-2_027",
      "question_number": 27,
      "explanation": "【題幹解析】\n本題測驗糖皮質類固醇 (corticosteroid) 的抗發炎與免疫抑制機轉。類固醇主要透過抑制多種發炎介質、細胞激素及黏著分子的基因表現來達到抗發炎效果。\n\n【選項詳解】\n- A. 類固醇會進入細胞內與受體結合，抑制NF-κB等轉錄因子，進而減少多種促發炎與免疫調節細胞激素（如IL-1、TNF-α、IL-4、IL-5）的轉錄與生成。\n- B. 類固醇可誘導 lipocortin-1 (annexin A1) 生成，抑制 phospholipase A2 活性，從源頭阻斷花生四烯酸 (arachidonic acid) 釋放，進而減少前列腺素 (prostaglandins) 與白血球三烯素 (leukotrienes) 合成。\n- C. 類固醇會抑制發炎處血管內皮細胞表現黏著分子（如ELAM-1、ICAM-1），減少白血球穿出血管進入發炎組織。\n- D. 錯誤敘述。類固醇在免疫抑制過程中，為了促進某些發炎細胞（如淋巴球、嗜酸性球）的細胞凋亡 (apoptosis)，反而會「增加」或活化內切核酸酶 (endonucleases) 的活性，造成DNA片段化，而非降低。\n\n【核心考點】\n糖皮質類固醇藉由抑制NF-κB與磷脂酶A2減少細胞激素及發炎介質，並會「活化」核酸內切酶來誘導淋巴球凋亡。",
      "key_point": "類固醇能降低細胞激素、前列腺素與黏著分子的生成，但會活化內切核酸酶 (endonucleases) 以促進淋巴球凋亡。",
      "flashcard_front": "糖皮質類固醇 (corticosteroid) 導致淋巴球凋亡的機轉為何？",
      "flashcard_back": "類固醇會增加／活化內切核酸酶 (endonucleases) 的活性，造成 DNA 片段化，進而誘導淋巴球與嗜酸性球發生細胞凋亡 (apoptosis)。",
      "flashcard_summary": "類固醇誘導淋巴球凋亡",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": datetime.now().isoformat(),
      "manual_review_notes": []
    },
    {
      "question_id": "108-2_medicine-2_028",
      "question_number": 28,
      "explanation": "【題幹解析】\n本題測驗單株抗體藥物 Natalizumab 的藥理機轉與臨床適應症。該藥物阻斷白血球表面的 α4 integrin，阻止其穿透血腦屏障進入中樞神經系統。\n\n【選項詳解】\n- A. 正確敘述。Natalizumab 是一種對抗 α4 integrin (VLA-4) 的單株抗體。VLA-4 可與血管內皮上的 VCAM-1 結合，阻斷此路徑可防止自體反應性T細胞穿過血腦屏障進入大腦，因此被核准用於治療多發性硬化症 (multiple sclerosis) 及克隆氏症。\n- B. 轉移性黑色素瘤 (metastatic melanoma) 的免疫治療多使用免疫檢查點抑制劑（如 anti-PD-1 的 Pembrolizumab 或 anti-CTLA-4 的 Ipilimumab），而非阻斷 integrin。\n- C. 慢性骨髓性白血病 (chronic myeloid leukemia) 的主要標靶治療是針對 BCR-ABL 融合蛋白的酪胺酸激酶抑制劑 (如 Imatinib)。\n- D. 慢性氣喘 (chronic asthma) 的生物製劑治療多針對 IgE (Omalizumab) 或 IL-5 (Mepolizumab) 等路徑，而非 Natalizumab。\n\n【核心考點】\nNatalizumab 藉由阻斷 α4 integrin (VLA-4) 減少白血球浸潤至中樞神經系統，主要用於治療多發性硬化症 (MS)及克隆氏症。",
      "key_point": "Natalizumab 藉由阻斷 α4 integrin (VLA-4) 減少白血球進入中樞神經，用於治療多發性硬化症 (MS)。",
      "flashcard_front": "Natalizumab 的藥理機轉與主要適應症為何？",
      "flashcard_back": "機轉：對抗 α4 integrin (VLA-4) 的單株抗體，阻斷其與內皮細胞 VCAM-1 的結合，阻止淋巴球穿過血腦屏障或腸道黏膜。\n適應症：多發性硬化症 (multiple sclerosis) 及克隆氏症。",
      "flashcard_summary": "Natalizumab 機轉與適應症",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": datetime.now().isoformat(),
      "manual_review_notes": []
    },
    {
      "question_id": "108-2_medicine-2_030",
      "question_number": 30,
      "explanation": "【題幹解析】\n本題測驗可引起人類「皮膚幼蟲移行症」(cutaneous larva migrans, CLM) 的特定寄生蟲感染。CLM主要由無法在人體發育成熟的動物鉤蟲幼蟲鑽入人體皮膚所致。\n\n【選項詳解】\n- A. 犬心絲蟲主要透過蚊子叮咬傳播，在人體多形成肺部結節（pulmonary dirofilariasis），極少引起皮膚幼蟲移行症。\n- B. 正確敘述。犬鉤蟲或巴西鉤蟲的第三期絲狀幼蟲接觸人體後會鑽入皮膚，但因人類非其自然宿主，幼蟲無法進入血液循環完成生活史，而滯留於皮下組織移行，引發線狀紅疹與劇癢，即為皮膚幼蟲移行症。\n- C. 犬蛔蟲或貓蛔蟲的蟲卵被人類誤食後，幼蟲會在人體內臟器官（如肝、肺、眼）移行，引起「內臟幼蟲移行症」(visceral larva migrans) 或「眼幼蟲移行症」，而非皮膚移行。\n- D. 肝毛細線蟲主要感染鼠類等囓齒動物的肝臟，人類若食入含胚胎的蟲卵，幼蟲主要在肝臟發育並產卵，引起肝炎或肝腫大，不導致皮膚幼蟲移行症。\n\n【核心考點】\n動物（貓犬）鉤蟲幼蟲鑽入人體皮膚會引發皮膚幼蟲移行症 (CLM)；動物蛔蟲卵被誤食則引發內臟幼蟲移行症 (VLM)。",
      "key_point": "動物鉤蟲（如犬鉤蟲、巴西鉤蟲）幼蟲鑽入人體皮膚會導致皮膚幼蟲移行症 (CLM)。",
      "flashcard_front": "皮膚幼蟲移行症 (cutaneous larva migrans, CLM) 與內臟幼蟲移行症 (VLM) 的常見致病原分別為何？",
      "flashcard_back": "皮膚幼蟲移行症 (CLM)：動物鉤蟲（如犬鉤蟲、巴西鉤蟲）幼蟲經皮膚鑽入。\n內臟幼蟲移行症 (VLM)：動物蛔蟲（如犬蛔蟲）蟲卵經口食入。",
      "flashcard_summary": "皮膚與內臟幼蟲移行症病原比較",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": datetime.now().isoformat(),
      "manual_review_notes": []
    }
]

output = {
  "source_file": "public/data/exams/108-2/medicine-2.json",
  "dataset_id": "108-2_medicine-2",
  "range": { "start": 21, "end": 30 },
  "updates": updates
}

with open("scratch/rewrite_updates/108-2_medicine-2/q021-q030_selected.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
