import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/112-2/medicine-2.json"
DATASET_ID = "112-2_medicine-2"
OUT_DIR = Path("scratch/rewrite_updates/112-2_medicine-2")
STAMP = "2026-07-15T00:00:00+08:00"


DATA = {
    1: {
        "topic": "痲瘋病：tuberculoid 與 lepromatous leprosy",
        "analysis": "題目問兩型痲瘋病比較中「最不適當」的敘述。Tuberculoid leprosy 以強細胞免疫、lepromin test 陽性和菌量少為特色；lepromatous leprosy 則細胞免疫差、菌量多、傳染力高，lepromin 反應通常弱或陰性，因此 A 是錯誤敘述。",
        "options": {
            "A": "錯。兩型並不都對 lepromin 有高度免疫反應；高度反應主要見於 tuberculoid leprosy，lepromatous leprosy 因細胞免疫低下常為陰性或弱反應。",
            "B": "對。Tuberculoid leprosy 以局部肉芽腫和細胞免疫為主，體液免疫球蛋白量通常不會像 lepromatous leprosy 那樣明顯上升。",
            "C": "對。Lepromatous leprosy 可發生 erythema nodosum leprosum，屬免疫複合體相關反應。",
            "D": "對。Lepromatous leprosy 菌量多、病灶廣泛，傳染力通常高於 tuberculoid leprosy。",
        },
        "core": "痲瘋病兩型的考點是細胞免疫強弱：tuberculoid 強、lepromin 陽性、菌少；lepromatous 弱、lepromin 弱或陰性、菌多且傳染力高。",
        "key": "Lepromatous leprosy 不是 lepromin 高反應，而是細胞免疫差、菌量多。",
    },
    2: {
        "topic": "Klebsiella pneumoniae 肝膿瘍與 hypermucoviscosity",
        "analysis": "題幹的關鍵是細菌性肝膿瘍、MacConkey agar 粉紅色菌落代表乳糖發酵，且菌落高度黏稠，最典型是高黏液型 Klebsiella pneumoniae。",
        "options": {
            "A": "大腸桿菌可乳糖發酵而呈粉紅色，但不以高度黏稠莢膜菌落和侵襲性肝膿瘍為典型線索。",
            "B": "創傷弧菌常與海水、海鮮、壞死性軟組織感染或敗血症相關，不是 MacConkey 高黏稠乳糖發酵菌落的典型答案。",
            "C": "霍亂弧菌以水樣腹瀉和 TCBS 培養基線索較典型，不是造成高黏稠肝膿瘍菌落的主角。",
            "D": "正確。Klebsiella pneumoniae 是乳糖發酵革蘭陰性桿菌，莢膜使菌落黏稠，亞洲常見侵襲性肝膿瘍表現。",
        },
        "core": "肝膿瘍加上 MacConkey 粉紅色、高黏稠菌落，要想到莢膜明顯的 Klebsiella pneumoniae。",
        "key": "高黏稠乳糖發酵菌落與肝膿瘍是 Klebsiella pneumoniae 的高產線索。",
    },
    3: {
        "topic": "Fluoroquinolone 抗藥性與 DNA gyrase",
        "analysis": "題目問 gyrase-A subunit 突變會影響哪類抗生素。Fluoroquinolones 作用於 DNA gyrase/topoisomerase，gyrA 突變會降低 ciprofloxacin 等藥物敏感性。",
        "options": {
            "A": "正確。Ciprofloxacin 屬 fluoroquinolone，主要抑制 DNA gyrase 與 topoisomerase IV；gyrA 突變是典型抗藥機轉。",
            "B": "Ampicillin 是 beta-lactam，作用在細胞壁轉胜肽酶，不是 DNA gyrase。",
            "C": "Cephalosporin 也是 beta-lactam，抗藥性多與 beta-lactamase、PBP 或通透性改變有關。",
            "D": "Clindamycin 作用在 50S ribosomal subunit，與 DNA gyrase 突變無直接關係。",
        },
        "core": "GyrA/topoisomerase 相關突變對應 fluoroquinolone 抗藥性；細胞壁與蛋白質合成抑制劑不是這個標的。",
        "key": "gyrase-A 突變最典型造成 ciprofloxacin 抗藥。",
    },
    4: {
        "topic": "革蘭陰性菌抗藥機轉",
        "analysis": "題目問革蘭陰性菌抗藥性通常無關的機制。水解酵素、標的突變與 efflux pump 都常見；形成內孢子是 Bacillus/Clostridium 等革蘭陽性桿菌特色，不是革蘭陰性菌常規抗藥機轉。",
        "options": {
            "A": "有關。Beta-lactamase 等酵素可水解抗生素，是革蘭陰性菌常見抗藥方式。",
            "B": "有關。藥物標的突變可使 quinolone、rifampin 等抗生素失效。",
            "C": "有關。Efflux pump 可降低菌體內藥物濃度，是多重抗藥的重要原因。",
            "D": "正確。形成內孢子不是革蘭陰性菌典型特徵，也不是其通常抗藥機制。",
        },
        "core": "革蘭陰性菌抗藥常考三件事：破壞藥物、改變標的、降低濃度；內孢子不是它們的典型答案。",
        "key": "革蘭陰性菌通常不靠形成內孢子產生抗藥性。",
    },
    5: {
        "topic": "Legionella 培養基",
        "analysis": "Legionella 需要 L-cysteine 和鐵等特殊營養，最適合的分離培養基是 buffered charcoal yeast extract agar。",
        "options": {
            "A": "正確。Buffered charcoal yeast extract agar 是分離 Legionella 的經典培養基。",
            "B": "Caffeic acid agar 常用於 Cryptococcus 等酚氧化酶相關鑑別，不是 Legionella 首選。",
            "C": "Regan-Lowe agar 用於 Bordetella pertussis 培養。",
            "D": "Cystine-tellurite agar 常用於 Corynebacterium diphtheriae。",
        },
        "core": "Legionella 難培養，記住 BCYE agar；Bordetella 對 Regan-Lowe，白喉桿菌對 tellurite。",
        "key": "Legionella 的分離培養基是 buffered charcoal yeast extract agar。",
    },
    6: {
        "topic": "Staphylococcus aureus 腸毒素食物中毒",
        "analysis": "金黃色葡萄球菌食物中毒是預先形成、耐熱 enterotoxin 引起，潛伏期短，常在數小時內噁心嘔吐，通常支持療法即可且病程短。",
        "options": {
            "A": "錯。Staphylococcal enterotoxin 具耐熱性，加熱後食物仍可能致病。",
            "B": "錯。疾病由毒素造成，通常以補液與支持療法為主，不需大量抗生素。",
            "C": "正確。潛伏期短，約 1-6 小時，平均約 4 小時符合預先形成毒素的特色。",
            "D": "錯。症狀多在 24-48 小時內改善，通常不會至少持續 4-5 天。",
        },
        "core": "短潛伏期嘔吐型食物中毒要想到預先形成毒素：S. aureus 耐熱腸毒素，治療重點是支持療法。",
        "key": "S. aureus 腸毒素食物中毒潛伏期短，約數小時發作。",
    },
    7: {
        "topic": "性傳染病病原",
        "analysis": "題目問最不可能經由性行為傳染的致病菌。淋病、梅毒、砂眼披衣菌都是典型性傳染病；Listeria monocytogenes 主要經污染食物感染。",
        "options": {
            "A": "Neisseria gonorrhoeae 是典型性傳染病病原，會造成尿道炎、子宮頸炎等。",
            "B": "Treponema pallidum 經性接觸傳播，是梅毒病原。",
            "C": "Chlamydia trachomatis 常造成性傳染之尿道炎、子宮頸炎和骨盆腔發炎。",
            "D": "正確。Listeria monocytogenes 多經受污染食物傳播，與孕婦、新生兒、免疫低下感染相關，不是典型性傳染病。",
        },
        "core": "性傳染病常見病原包括淋病雙球菌、梅毒螺旋體、砂眼披衣菌；Listeria 主要是食媒感染。",
        "key": "Listeria monocytogenes 最不可能是性行為傳染病原。",
    },
    8: {
        "topic": "細菌呼吸作用與 ATP 產量",
        "analysis": "題目問細菌呼吸作用最不適當的敘述。有氧呼吸以氧為終端電子接受者，能量產量通常高於無氧呼吸與發酵；無氧呼吸不會比有氧呼吸產生更多 ATP。",
        "options": {
            "A": "對。有氧呼吸利用電子傳遞鏈與氧化磷酸化，ATP 產量高於發酵。",
            "B": "對。細菌沒有粒線體，電子傳遞鏈位在細胞膜。",
            "C": "對。兼性厭氧菌可在無氧環境使用非氧電子接受者進行無氧呼吸，或改走發酵。",
            "D": "錯。有氧呼吸通常 ATP 產量最高，無氧呼吸因終端電子接受者能量較低，產量較少。",
        },
        "core": "能量產量大致為有氧呼吸最高，無氧呼吸次之，發酵較低；細菌電子傳遞鏈在細胞膜。",
        "key": "無氧呼吸不會比有氧呼吸產生更多 ATP。",
    },
    9: {
        "topic": "Clostridium septicum 特徵",
        "analysis": "題目問敗血梭狀芽胞桿菌不是何者。C. septicum 是厭氧、芽胞形成革蘭陽性桿菌，與 occult colon cancer、非外傷性肌壞死有關；「對氧氣有耐受性」不符合典型梭菌特色。",
        "options": {
            "A": "正確。Clostridium 屬多為厭氧菌，C. septicum 雖可存在環境中，但描述成對氧氣有耐受性並不恰當。",
            "B": "對。C. septicum bacteremia 或 myonecrosis 與潛藏性大腸癌有重要關聯。",
            "C": "對。梭菌在血液培養基可呈擴散或游走樣生長，並可有溶血表現。",
            "D": "對。C. septicum 可造成 spontaneous/nontraumatic gas gangrene 或 myonecrosis。",
        },
        "core": "C. septicum 的高產聯想是 occult colon cancer 與非外傷性肌壞死；梭菌整體仍以厭氧為核心。",
        "key": "C. septicum 與大腸癌、非外傷性肌壞死相關，不是耐氧菌。",
    },
    10: {
        "topic": "病毒複製與 RNA 病毒變異",
        "analysis": "題目問病毒敘述最適當者。RNA-dependent RNA polymerase 校對能力較差，RNA 病毒複製錯誤率通常高於 DNA 病毒。",
        "options": {
            "A": "正確。RNA 病毒聚合酶缺乏有效 proofreading，突變率通常高於 DNA 病毒。",
            "B": "不精確。病毒增殖是依感染週期產生大量子代，不能簡化成等比級數作為通則。",
            "C": "錯。無套膜的腸病毒通常比有套膜的流感病毒更能耐受環境。",
            "D": "錯。多數 RNA 病毒在細胞質複製，但 influenza virus 等會在細胞核進行重要複製步驟。",
        },
        "core": "RNA 病毒高突變率是核心；但不要忘記 influenza 是 RNA 病毒中會進入細胞核複製的例外。",
        "key": "RNA 病毒的複製錯誤率通常高於 DNA 病毒。",
    },
    11: {
        "topic": "病毒感染與干擾素造成類感冒症狀",
        "analysis": "病毒感染早期的全身性類感冒症狀常由先天免疫細胞分泌 type I interferons 與發炎介質造成，其中干擾素是最典型考點。",
        "options": {
            "A": "T 細胞參與適應性免疫與清除感染，但不是引發早期 flu-like systemic symptom 的最典型因子。",
            "B": "正確。Interferon 可誘導抗病毒狀態，也會造成發燒、倦怠、肌肉痠痛等類感冒症狀。",
            "C": "抗體負責中和病毒與後續保護，不是急性全身類感冒症狀的主要因子。",
            "D": "免疫複合物可造成第三型過敏或組織傷害，不是病毒感染早期類感冒症狀的典型答案。",
        },
        "core": "病毒感染早期的發燒、倦怠、肌痛常與 type I interferon 等先天免疫反應有關。",
        "key": "干擾素是病毒感染造成 flu-like symptoms 的代表性因子。",
    },
    12: {
        "topic": "Bunyaviridae 與 hantavirus",
        "analysis": "Bunyaviridae 多為分節、負股 RNA 病毒，許多由節肢動物傳播；hantavirus 的重要例外是主要以鼠類排泄物氣膠傳播。",
        "options": {
            "A": "錯。Bunyaviridae 不是正股 RNA，而多為負股或 ambisense 分節 RNA 病毒。",
            "B": "錯。Bunyavirus 多在細胞質複製；需要在細胞核中複製是 influenza 等少數 RNA 病毒特色。",
            "C": "正確。Hantavirus 主要以鼠類為自然宿主，經排泄物氣膠感染人類。",
            "D": "錯。大多數 hantavirus 並非以人傳人為主，雖少數新世界型別可例外。",
        },
        "core": "Bunyavirus 是分節負股 RNA；hantavirus 記鼠類傳播，不是典型人傳人。",
        "key": "漢他病毒主要以鼠類為媒介或宿主傳播。",
    },
    13: {
        "topic": "EBV 相關疾病",
        "analysis": "題目問與 EBV 較無關的疾病。EBV 與傳染性單核球增多症、鼻咽癌、免疫低下口腔毛狀白斑等相關；先天性聽力受損典型與 CMV 相關。",
        "options": {
            "A": "有關。AIDS 病人的 hairy oral leukoplakia 常與 EBV 感染上皮細胞有關。",
            "B": "正確。新生兒先天性聽力受損最典型是 congenital CMV，而不是 EBV。",
            "C": "有關。鼻咽癌與 EBV 有強關聯，尤其非角化型鼻咽癌。",
            "D": "有關。傳染性單核球增多症是 EBV 的經典臨床表現。",
        },
        "core": "EBV 要記 mononucleosis、nasopharyngeal carcinoma、Burkitt lymphoma、hairy leukoplakia；先天聽損想到 CMV。",
        "key": "先天性聽力受損較典型與 CMV 相關，不是 EBV。",
    },
    14: {
        "topic": "Retrovirus 與 provirus",
        "analysis": "題目問反轉錄病毒最不適當的敘述。Retrovirus 會整合成 provirus，但整合位置不是固定單一位置，而是可在宿主染色體不同位置發生。",
        "options": {
            "A": "錯。Provirus 會整合入宿主染色體，但整合位置不是固定的特定位點。",
            "B": "對。反轉錄時利用宿主 tRNA 作為 primer 是 retrovirus 的特徵之一。",
            "C": "對。病毒顆粒內通常有兩份相同的單股 RNA 基因體。",
            "D": "對。病毒顆粒攜帶 reverse transcriptase，才能在感染後進行反轉錄。",
        },
        "core": "Retrovirus 三件事：兩份 RNA、帶 reverse transcriptase、整合成 provirus；但整合位置不固定。",
        "key": "Provirus 整合入宿主基因體，但不是只在固定位置整合。",
    },
    15: {
        "topic": "SARS-CoV-2 初始鑑定",
        "analysis": "新病毒是否與蝙蝠冠狀病毒相近，最可靠的初始判定依據是病毒基因序列比對，而不是單靠形態、症狀或抗體交叉反應。",
        "options": {
            "A": "電子顯微鏡可看出冠狀病毒樣外觀，但無法精確證明與蝙蝠冠狀病毒序列相近。",
            "B": "正確。病人檢體病毒基因序列與蝙蝠冠狀病毒高度相似，是鑑定親緣關係的核心證據。",
            "C": "臨床症狀可提示呼吸道感染，但不能判定病毒演化來源或序列相似度。",
            "D": "抗體交叉反應可提供免疫相關資訊，但不是最初確認基因親緣關係的主要方法。",
        },
        "core": "新興病毒親緣關係的判定以核酸定序與序列比對最有力。",
        "key": "SARS-CoV-2 與蝙蝠冠狀病毒相近主要由病毒序列相似度判定。",
    },
    16: {
        "topic": "抗黴菌藥作用標的",
        "analysis": "題目問作用部位與其他不同者。Triazole、allylamine、polyene 都針對 ergosterol 合成或膜 sterol；echinocandin 則抑制 fungal cell wall 的 beta-glucan 合成。",
        "options": {
            "A": "Triazole 抑制 ergosterol 合成的 14-alpha-demethylase，屬細胞膜 sterol 路徑。",
            "B": "正確。Echinocandin 抑制 beta-1,3-glucan synthase，作用在黴菌細胞壁。",
            "C": "Allylamine 抑制 squalene epoxidase，影響 ergosterol 合成。",
            "D": "Polyene 如 amphotericin B 與 ergosterol 結合，破壞細胞膜。",
        },
        "core": "抗黴菌藥中，echinocandin 打細胞壁 beta-glucan；azole、allylamine、polyene 都圍繞 ergosterol。",
        "key": "Echinocandin 的標的是細胞壁 beta-glucan，不是 ergosterol。",
    },
    17: {
        "topic": "Rhodotorula 紅色酵母菌落",
        "analysis": "Rhodotorula 會產生類胡蘿蔔素色素，菌落常呈粉紅、珊瑚紅到紅色，是酵母鑑別的典型線索。",
        "options": {
            "A": "Trichosporon 可見節孢子等特色，但不是粉紅至紅色 carotenoid pigment 的典型答案。",
            "B": "正確。Rhodotorula spp. 會產生 carotenoid pigments，使菌落呈粉紅至紅色。",
            "C": "Cryptococcus 的重點是莢膜、urease 陽性與 India ink，不是紅色色素菌落。",
            "D": "Malassezia 與脂質依賴、皮屑芽孢菌相關，不以紅色類胡蘿蔔素菌落為主。",
        },
        "core": "粉紅到紅色酵母菌落要想到 Rhodotorula 的 carotenoid pigment。",
        "key": "Rhodotorula spp. 會合成 carotenoid pigments。",
    },
    18: {
        "topic": "中樞與周邊免疫器官",
        "analysis": "題目問周邊免疫組織/器官中的錯誤示範。Tonsil、lymph node、spleen 是周邊淋巴器官；thymus 是 T 細胞成熟的中樞淋巴器官。",
        "options": {
            "A": "Tonsil 是 mucosa-associated lymphoid tissue，屬周邊免疫組織。",
            "B": "Lymph node 是周邊淋巴器官，負責過濾淋巴液與啟動免疫反應。",
            "C": "Spleen 是周邊淋巴器官，主要過濾血液中的抗原。",
            "D": "正確。Thymus 是中樞淋巴器官，負責 T 細胞成熟與選汰，不是周邊免疫器官。",
        },
        "core": "中樞淋巴器官是骨髓與胸腺；周邊包含淋巴結、脾臟、扁桃腺與 MALT。",
        "key": "Thymus 是中樞免疫器官，不是周邊免疫器官。",
    },
    19: {
        "topic": "Defensin 殺菌機轉",
        "analysis": "題目問直接破壞病原菌細胞膜的先天免疫分子。Defensin 是陽離子抗菌胜肽，可插入並破壞微生物膜。",
        "options": {
            "A": "Cytokine 主要負責免疫細胞訊息傳遞與活化，不是直接打洞破膜的分子。",
            "B": "CRP 屬急性期蛋白，可結合病原並促進補體或調理作用，不是直接破膜。",
            "C": "TLR 是 pattern recognition receptor，負責辨識病原相關分子並啟動訊號。",
            "D": "正確。Defensin 是抗菌胜肽，可直接破壞病原菌細胞膜達到殺菌效果。",
        },
        "core": "Defensin 的考點是抗菌胜肽與膜破壞；TLR 負責辨識，CRP 負責急性期與調理。",
        "key": "Defensin 以直接破壞細菌細胞膜殺菌。",
    },
    20: {
        "topic": "TCR CDR3 最大變異度",
        "analysis": "TCR 的 CDR3 位於 V(D)J 接合處，受 junctional diversity 影響最大，因此是抗原結合區中變異度最高的部分。",
        "options": {
            "A": "CDR1 主要由 V gene 編碼，變異度低於接合處的 CDR3。",
            "B": "CDR2 也主要由 V gene 編碼，常與 MHC 接觸，變異度不是最大。",
            "C": "正確。CDR3 橫跨 V(D)J junction，是 TCR/BCR 變異度最高、直接影響抗原特異性的區域。",
            "D": "傳統 CDR 分區為 CDR1、CDR2、CDR3；CDR4 不是標準答案。",
        },
        "core": "最大變異度記 CDR3，因為它來自 V(D)J 接合與核苷酸增刪。",
        "key": "TCR 抗原結合區變異度最大的是 CDR3。",
    },
    21: {
        "topic": "TCR 與 BCR 功能差異",
        "analysis": "題目問 TCR/BCR 敘述何者錯誤。BCR 的膜型抗體可結合抗原，但 BCR 固定在 B 細胞膜上時主要負責抗原辨識與訊號；抗體 Fc 的補體、Fc receptor 等效應功能主要是分泌型抗體執行，不能說膜上 BCR 的功能和抗體完全一樣。",
        "options": {
            "A": "對。典型 TCR 由 alpha/beta 鏈構成，BCR 由兩重鏈兩輕鏈構成，兩者抗原結合位都在 variable region。",
            "B": "對。TCR 通常一個抗原結合位且只在細胞膜上；BCR/抗體有兩個 Fab，B 細胞活化後可分泌抗體。",
            "C": "錯。BCR 是膜型免疫球蛋白，Fab 可辨識抗原，但膜上 BCR 的 Fc 區不等同於分泌抗體在體液中執行 Fc 效應功能。",
            "D": "對。TCR 需要同時辨識 MHC 與 peptide，這是 T 細胞偵測感染細胞的核心。",
        },
        "core": "TCR 看 MHC-peptide；BCR 可直接認抗原。膜型 BCR 負責辨識與訊號，分泌型抗體才主要執行 Fc effector functions。",
        "key": "膜上 BCR 不等於分泌型抗體的完整 Fc 效應功能。",
    },
    22: {
        "topic": "Fingolimod 與 S1P receptor",
        "analysis": "Fingolimod/FTY720 是 S1P receptor modulator，會使淋巴球無法有效離開淋巴結，降低自體反應性淋巴球進入中樞神經造成多發性硬化症發炎。官方選項中 D 最接近此 S1PR1 路徑。",
        "options": {
            "A": "錯。Fingolimod 不是以阻斷自體抗體造成的 ADCC 為主要機轉。",
            "B": "錯。減少 IL-2、抑制 T 細胞增生較像 calcineurin inhibitor 的下游效果，不是 fingolimod 的核心。",
            "C": "錯。阻斷 IL-6 receptor/JAK-STAT 較接近 tocilizumab 或 JAK inhibitor 的概念。",
            "D": "正確但題目文字略簡化。Fingolimod 作用於 S1PR1，使淋巴球滯留於淋巴結、減少外周與中樞神經浸潤；不是主要靠誘發 T 細胞凋亡。",
        },
        "core": "Fingolimod 記 S1P receptor modulator：讓淋巴球出不了淋巴結，用於多發性硬化症。",
        "key": "Fingolimod 透過 S1PR1 調節造成淋巴球滯留。",
        "notes": ["官方答案 D 方向正確，但「進而凋亡」不是 fingolimod 的主要藥理重點。"],
    },
    23: {
        "topic": "抗體 Fc 與 Fab 功能",
        "analysis": "題目問不是 Fc 部分功能者。中和作用主要靠 Fab 抗原結合區阻斷毒素或病毒與受體結合；補體活化、調理與 mast cell degranulation 都與 Fc receptor 或 Fc 區相關。",
        "options": {
            "A": "是 Fc 功能。IgG/IgM 的 Fc 區可啟動 classical complement pathway。",
            "B": "正確。Neutralization 主要靠 Fab 區結合病毒、毒素或黏附分子，阻斷其作用。",
            "C": "是 Fc 功能。Opsonization 依靠 Fc 與吞噬細胞 Fc receptor 互動。",
            "D": "是 Fc 功能。IgE 的 Fc 區結合 mast cell/basophil 上 FcεRI，抗原交聯後促進 degranulation。",
        },
        "core": "Fab 負責 antigen binding 與 neutralization；Fc 負責補體、調理、ADCC、mast cell 活化等效應。",
        "key": "中和作用主要是 Fab，不是 Fc 功能。",
    },
    24: {
        "topic": "Oral tolerance",
        "analysis": "Oral tolerance 是腸道免疫對食物抗原或共生菌建立低反應性，常與 regulatory T cells、TGF-beta、IL-10 等免疫調節有關。",
        "options": {
            "A": "錯。食物抗原即使被消化，仍可有 peptide 被免疫系統辨識；oral tolerance 不是單純因小分子不刺激免疫。",
            "B": "錯。胸腺負選擇是中樞耐受，食物抗原的 oral tolerance 主要發生於周邊黏膜免疫環境。",
            "C": "錯。不是所有食物都必然引發 oral tolerance，且個體、劑量與黏膜環境會影響結果。",
            "D": "正確。分泌 TGF-beta 的調節型 T 細胞/輔助 T 細胞參與腸道周邊耐受。",
        },
        "core": "Oral tolerance 是周邊黏膜免疫耐受，重點是 Treg、TGF-beta、IL-10，而非胸腺刪除。",
        "key": "Oral tolerance 與分泌 TGF-beta 的調節性 T 細胞有關。",
    },
    25: {
        "topic": "衛生假說與第一型過敏",
        "analysis": "第一型過敏與 IgE、Th2 偏向和 mast cell 相關。衛生假說認為幼年過度乾淨、微生物暴露不足，可能使免疫調節不足並增加過敏風險。",
        "options": {
            "A": "正確。嬰幼兒時期過度乾淨、感染與微生物刺激少，符合 hygiene hypothesis 對過敏風險上升的解釋。",
            "B": "較不符合。早期某些微生物暴露反而可能促進免疫調節，不是第一型過敏最相關選項。",
            "C": "麻疹或 A 肝感染史不是第一型過敏發生最直接、最典型的危險因子。",
            "D": "第一型過敏核心是 allergen-specific IgE，不是高濃度 IgG2a。",
        },
        "core": "第一型過敏記 IgE、Th2、mast cell；衛生假說解釋幼年微生物暴露不足會增加過敏傾向。",
        "key": "過度乾淨的幼年環境與第一型過敏風險增加最相關。",
    },
    26: {
        "topic": "SLE anti-dsDNA 與 TLR9",
        "analysis": "TLR9 主要辨識 unmethylated CpG DNA。SLE 中核酸免疫複合物可刺激 endosomal TLR，anti-dsDNA 相關 DNA 訊號最符合 TLR9。",
        "options": {
            "A": "TLR1 常與 TLR2 形成異源二聚體辨識細菌脂蛋白，不是 dsDNA 主要受器。",
            "B": "TLR4 典型辨識 LPS，也可參與多種內源性訊號，但不是 anti-dsDNA 的核心答案。",
            "C": "TLR7 主要辨識單股 RNA，較常連到 RNA-containing immune complex。",
            "D": "正確。TLR9 位於 endosome，辨識 DNA/CpG，與 SLE anti-dsDNA 相關免疫活化相符。",
        },
        "core": "核酸 TLR 配對：TLR7 看 RNA，TLR9 看 DNA；SLE anti-dsDNA 對 TLR9。",
        "key": "Anti-dsDNA 免疫活化主要連到 TLR9。",
    },
    27: {
        "topic": "慢性移植排斥",
        "analysis": "慢性排斥的核心病理是血管內皮損傷、內膜增生、血管狹窄與纖維化，造成移植器官慢性缺血與功能下降。",
        "options": {
            "A": "NK cell 不是慢性排斥最典型主軸；移植排斥主要由 T 細胞與抗體等適應性免疫驅動。",
            "B": "正確。小血管內皮損傷、細胞浸潤、血管壁增厚硬化與蒼白缺血，是慢性排斥典型描述。",
            "C": "這比較像超急性排斥，預存抗體造成快速血管炎、血栓與植體壞死。",
            "D": "慢性排斥不是接受者突變出植體抗原，而是對 donor alloantigen 的長期免疫反應。",
        },
        "core": "移植排斥時間軸：超急性是預存抗體；急性是 T 細胞/抗體；慢性是血管狹窄、纖維化、缺血。",
        "key": "慢性排斥最典型是移植體血管硬化與慢性缺血。",
    },
    28: {
        "topic": "Anti-CTLA-4 腫瘤免疫療法",
        "analysis": "CTLA-4 是 T 細胞抑制性受器，會與抗原呈現細胞上的 CD80/CD86 競爭結合，降低共刺激。Anti-CTLA-4 阻斷此抑制訊號以增強抗腫瘤 T 細胞反應。",
        "options": {
            "A": "錯。CTLA-4 不結合 MHC；TCR 才辨識 MHC-peptide。",
            "B": "錯。PD-1 是另一個 T 細胞抑制受器，不是 CTLA-4 在樹突細胞上的配體。",
            "C": "正確。CTLA-4 結合 APC 上的 CD80/CD86，與 CD28 競爭共刺激配體。",
            "D": "錯。CD11b 是 integrin/髓系細胞標記，不是 CTLA-4 的主要配體。",
        },
        "core": "CTLA-4 對 CD80/CD86；PD-1 對 PD-L1/PD-L2。免疫檢查點治療就是解除 T 細胞煞車。",
        "key": "CTLA-4 結合樹突細胞上的 CD80/CD86。",
    },
    29: {
        "topic": "寄生蟲與眼部病變",
        "analysis": "Toxocara、Angiostrongylus、Loa loa 都可造成眼部或視神經相關病變；Anisakis 主要由生食海魚感染，引起胃腸道或過敏反應，眼病變最不典型。",
        "options": {
            "A": "Toxocara canis 可造成 ocular larva migrans，是兒童單眼視網膜病變的重要原因。",
            "B": "Angiostrongylus cantonensis 可造成嗜酸性腦膜炎，也可有眼內移行相關病變。",
            "C": "Loa loa 成蟲可在結膜下移行，眼蟲是經典線索。",
            "D": "正確。Anisakis 主要造成胃腸道 anisakiasis 或過敏反應，最不可能引起眼睛病變。",
        },
        "core": "眼部寄生蟲記 Toxocara 眼幼蟲移行、Loa loa 眼蟲；Anisakis 偏胃腸道與過敏。",
        "key": "Anisakis spp. 最不典型造成眼睛病變。",
    },
    30: {
        "topic": "鉤蟲爬行疹與土壤接觸",
        "analysis": "手腳接觸污泥後搔癢、延伸紅斑，最像皮膚幼蟲移行症/鉤蟲爬行疹。東方毛線蟲主要是腸道線蟲感染，通常不是造成皮膚延伸紅斑的原因。",
        "options": {
            "A": "可成立。寄生蟲幼蟲在皮膚移行可引發局部過敏與劇癢。",
            "B": "可成立。抓破皮後可能繼發細菌性感染，臨床上需要注意。",
            "C": "正確。Trichostrongylus orientalis 主要與腸道感染相關，不是皮膚爬行疹的典型病原。",
            "D": "可成立。鉤蟲幼蟲穿入皮膚後移行，可造成 creeping eruption。",
        },
        "core": "土壤接觸後線狀、蛇行、搔癢紅斑，要想到鉤蟲造成 cutaneous larva migrans。",
        "key": "爬行疹典型是動物鉤蟲幼蟲皮膚移行，不是東方毛線蟲。",
    },
    31: {
        "topic": "Schistosoma haematobium",
        "analysis": "埃及血吸蟲寄生於膀胱靜脈叢，蟲卵有 terminal spine，造成血尿、慢性膀胱炎，並與鱗狀細胞膀胱癌風險增加有關。",
        "options": {
            "A": "錯。S. haematobium 蟲卵是 terminal spine；lateral spine 是 S. mansoni。",
            "B": "錯。下腸繫膜靜脈叢較符合 S. mansoni；S. haematobium 主要在膀胱靜脈叢。",
            "C": "正確。慢性 S. haematobium 感染與埃及和非洲地區膀胱癌，尤其鱗狀細胞癌，有關。",
            "D": "錯。血吸蟲治療首選是 praziquantel，不是 metronidazole。",
        },
        "core": "S. haematobium：terminal spine、膀胱靜脈叢、血尿、膀胱鱗癌。",
        "key": "埃及血吸蟲與膀胱癌風險增加有關。",
    },
    32: {
        "topic": "Toxoplasmosis",
        "analysis": "題目問弓蟲症錯誤敘述。弓蟲可因食入含 bradyzoite 的組織囊體感染，免疫正常多無症狀或類感冒；急性感染大量腹水不是典型表現。",
        "options": {
            "A": "對。食入未熟肉類中含 bradyzoite 的 tissue cyst 是常見感染途徑之一。",
            "B": "對。免疫正常者多無症狀，或只有淋巴結腫大、類感冒症狀。",
            "C": "錯。急性 toxoplasmosis 不以大量腹水為典型表現。",
            "D": "對。慢性感染可在中樞形成組織囊體；免疫低下時再活化可造成腦炎，膠質結節可見於病理描述。",
        },
        "core": "Toxoplasma 記貓糞 oocyst、未熟肉 bradyzoite、免疫正常多輕微、免疫低下腦炎、孕婦先天感染。",
        "key": "弓蟲急性感染不典型表現為大量腹水。",
    },
    33: {
        "topic": "Free-living amebae 與 PAM",
        "analysis": "Naegleria fowleri 可造成原發性阿米巴腦膜腦炎，進展極快，常在症狀出現後數日死亡。其他自由生活阿米巴感染不一定都與游泳有關。",
        "options": {
            "A": "錯。Naegleria 常與溫淡水游泳有關，但 Acanthamoeba、Balamuthia 等感染不都以游泳為必要條件。",
            "B": "錯。Naegleria 在人體組織中主要見 trophozoite，通常不在組織切片中見 cyst。",
            "C": "正確。PAM 進展非常快速，若未及時治療，常在 3-6 天內死亡。",
            "D": "錯。Acanthamoeba keratitis 治療可包括抗阿米巴藥物與局部治療，並非所有患者都必須角膜移植。",
        },
        "core": "Naegleria fowleri 的 PAM 是急速致死腦膜腦炎；人體組織主要見 trophozoite，不是 cyst。",
        "key": "PAM 未治療常在症狀出現後數日內死亡。",
    },
    34: {
        "topic": "塵蟎與兒童過敏氣喘",
        "analysis": "兒童過敏與氣喘最重要、最常被確認的室內節肢動物致敏原是塵蟎，尤其其糞便與體蛋白。",
        "options": {
            "A": "疥蟎造成疥瘡，主要是皮膚寄生與搔癢，不是兒童氣喘主要室內 allergen。",
            "B": "正確。Dust mite 是兒童過敏性鼻炎與氣喘的重要致敏原。",
            "C": "毛囊蟎寄生毛囊，與酒糟等皮膚問題較相關，不是兒童氣喘主要致敏原。",
            "D": "恙蟎可傳播恙蟲病，並非氣喘主要 allergen。",
        },
        "core": "氣喘過敏常見室內 allergen：dust mite、蟑螂、黴菌、寵物皮屑；節肢動物中塵蟎最典型。",
        "key": "塵蟎是兒童過敏與氣喘的重要致敏原。",
    },
    35: {
        "topic": "Ehrlichiosis 與蜱媒感染",
        "analysis": "美國東部野外活動、蜱叮咬、發燒頭痛、白血球與血小板下降，且中性球內見菌體團塊，最符合人艾利希體症或相關 Anaplasma/Ehrlichia 感染。官方答案選 B。",
        "options": {
            "A": "Babesiosis 也可在美國東北部蜱媒傳播，但血液抹片重點是紅血球內寄生蟲與 Maltese cross，不是中性球內菌體。",
            "B": "正確。Ehrlichiosis/相關蜱媒立克次體樣感染可有發燒、白血球低下、血小板低下，白血球內 morulae 是線索。",
            "C": "Lyme disease 典型是 erythema migrans、關節炎、神經或心臟表現，不以中性球內菌體為主。",
            "D": "Bartonellosis 多與貓抓病、血管增生病變等相關，不符合此蜱媒與白血球內菌體線索。",
        },
        "core": "蜱媒發燒合併 leukopenia、thrombocytopenia、白血球內 morulae，要想到 Ehrlichia/Anaplasma 類感染。",
        "key": "白血球內菌體團塊加蜱叮咬最符合人艾利希體症。",
    },
    36: {
        "topic": "RCT 樣本數估計",
        "analysis": "雙樣本 t 檢定樣本數會隨變異增加而增加，隨效應值變大而減少；放寬 type I error 或降低 power 也會使樣本數需求下降。",
        "options": {
            "A": "Type I error 從 0.05 放寬到 0.1，臨界值較低，所需樣本數通常減少。",
            "B": "預期差異從 5 增至 10 mmHg，效應值變大，所需樣本數減少。",
            "C": "正確。標準差從 12 增至 16，資料變異變大，需更多樣本才能偵測同樣差異。",
            "D": "Power 從 0.9 降至 0.85，要求較低，所需樣本數減少。",
        },
        "core": "樣本數和變異、信心水準、power 同向；和效應值大小反向。",
        "key": "預期標準差增加會使 RCT 估計樣本數增加。",
    },
    37: {
        "topic": "粗發生率與年齡標準化",
        "analysis": "甲地粗發生率高但年齡標準化後低於乙地，表示甲地原本較高的粗率很可能被年齡結構拉高，尤其心血管疾病與高齡高度相關。",
        "options": {
            "A": "不能這樣推論。標準化後甲地反而較低，危險因子不一定比乙地多。",
            "B": "死亡分率不是由發生率標準化差異可直接判定的指標。",
            "C": "正確。甲地人口較老，會使心血管疾病粗發生率偏高；年齡標準化後才顯示真實比較較低。",
            "D": "盛行率與發生率不同，題幹資料不能推出甲地盛行率較高。",
        },
        "core": "粗率受人口結構影響；疾病與年齡強相關時，要看年齡標準化率才適合跨地比較。",
        "key": "粗率高但年齡標準化率低，常代表該地人口較老。",
    },
    38: {
        "topic": "相關係數解讀",
        "analysis": "相關係數 0.8 表示兩變項有強正向線性相關，但相關不代表因果；相關係數範圍是 -1 到 +1。",
        "options": {
            "A": "錯。0.8 是正相關，X 越大時 Y 傾向越大，不是越小。",
            "B": "錯。相關不能證明 X 導致 Y，仍可能有混雜或反向因果。",
            "C": "錯。相關係數最小為 -1，不是 0；0 代表無線性相關。",
            "D": "正確。Pearson correlation coefficient 衡量 X 與 Y 的線性相關方向與強度。",
        },
        "core": "Correlation 看線性關係，不等於 causation；範圍 -1 到 +1。",
        "key": "相關係數描述線性相關程度，不能推出因果。",
    },
    39: {
        "topic": "國家健康水平指標",
        "analysis": "嬰兒死亡率對醫療照護、營養、衛生環境與社經條件敏感，因此常作為評估國家健康水平的重要綜合指標。",
        "options": {
            "A": "流產率可反映部分生殖健康議題，但不是最常用的國家整體健康水平指標。",
            "B": "正確。嬰兒死亡率是公共衛生常用的國家健康與社會發展指標。",
            "C": "總生育率反映人口生育模式，不是健康水平最核心指標。",
            "D": "離婚率屬社會人口指標，不是健康水平常用主指標。",
        },
        "core": "評估國家健康水平常用 infant mortality rate，因其整合反映母嬰照護、環境與社經條件。",
        "key": "嬰兒死亡率是公共衛生常用健康水平指標。",
    },
    40: {
        "topic": "腎臟毒性與泌尿道暴露",
        "analysis": "題目問腎臟化學毒性最不恰當者。腎臟血流高、會濃縮毒物，易受重金屬與藥物傷害；毒物經尿液排出時也可能影響輸尿管、膀胱、尿道等泌尿道組織。",
        "options": {
            "A": "對。腎臟相對血流量高，暴露於血中毒物的機會大。",
            "B": "對。鎘與汞等重金屬可造成腎小管傷害，嚴重時可急性腎小管壞死。",
            "C": "對。腎臟濃縮尿液會提高某些外來毒物在腎小管或尿液中的濃度。",
            "D": "錯。化學物質或代謝物經尿液排出時，仍可能傷害膀胱等下泌尿道，例如尿路上皮暴露。",
        },
        "core": "腎臟易中毒因血流高、濃縮與主動運輸；排到尿中的毒物也可能傷害下泌尿道。",
        "key": "經尿液排出不代表不會影響輸尿管、膀胱或尿道。",
    },
    41: {
        "topic": "砷暴露指標與危害",
        "analysis": "題目問砷危害最不恰當者。長期砷暴露較適合用毛髮、指甲等累積性指標；血中砷較反映近期暴露，不是長期暴露最適宜指標。",
        "options": {
            "A": "對。半導體、晶圓、光電等產業可能涉及砷化物暴露，是職業衛生考點。",
            "B": "對。臺灣過去煉銅廠周遭曾有砷等環境污染暴露疑慮。",
            "C": "錯。血中砷較代表近期暴露；長期暴露常以毛髮或指甲砷作為較合適指標。",
            "D": "對。砷暴露會增加皮膚癌、肺癌、膀胱癌等風險。",
        },
        "core": "長期重金屬暴露常看能累積的組織指標；砷暴露與皮膚、肺、膀胱等癌症相關。",
        "key": "長期砷暴露較適合毛髮或指甲砷，不是血中砷。",
    },
    42: {
        "topic": "飲水加氯與消毒副產物",
        "analysis": "加氯便宜、有效且有餘氯保護，但氯會和水中有機物反應，產生 trihalomethanes 等鹵化有機消毒副產物，這是主要缺點。",
        "options": {
            "A": "不對。加氯通常成本相對低，是廣泛使用的原因之一。",
            "B": "不對。加氯操作相對方便，不是最主要缺點。",
            "C": "不對。餘氯反而可在配水系統中提供後續保護能力。",
            "D": "正確。氯與天然有機物反應可產生鹵化有機物等消毒副產物。",
        },
        "core": "飲水加氯優點是便宜有效且有 residual protection；缺點是消毒副產物如 THMs。",
        "key": "加氯消毒主要缺點是可能產生鹵化有機物。",
    },
    43: {
        "topic": "有機磷與膽鹼酯酶抑制",
        "analysis": "血中膽鹼酯酶活性下降是有機磷或 carbamate 暴露的重要生物指標；有機磷會抑制 acetylcholinesterase，造成膽鹼症狀。",
        "options": {
            "A": "四氯化碳主要造成肝毒性，與膽鹼酯酶抑制不是典型配對。",
            "B": "二甲基甲醯胺是溶劑暴露，可有肝毒性等問題，不是膽鹼酯酶下降典型原因。",
            "C": "鉻酸暴露與皮膚、呼吸道刺激和致癌性相關，不是膽鹼酯酶抑制主因。",
            "D": "正確。有機磷抑制 acetylcholinesterase，使血中膽鹼酯酶活性下降。",
        },
        "core": "有機磷中毒記 AChE inhibition、DUMBELS/SLUDGE，監測可看 cholinesterase activity。",
        "key": "血中膽鹼酯酶下降最典型是有機磷暴露。",
    },
    44: {
        "topic": "1848 Public Health Act",
        "analysis": "1848 年 Public Health Act 是英國公共衛生史的重要里程碑，與工業革命後都市衛生改革、Edwin Chadwick 等背景相關。",
        "options": {
            "A": "日本不是 1848 年訂定 Public Health Act 的國家。",
            "B": "美國有自己的公共衛生發展史，但本題 1848 Public Health Act 指英國。",
            "C": "正確。英國於 1848 年通過 Public Health Act，是近代公共衛生法制重要起點。",
            "D": "德國在社會醫學與保險制度史上重要，但不是此題所問的 1848 Public Health Act。",
        },
        "core": "公共衛生史考 1848 Public Health Act，答案是英國。",
        "key": "1848 年公共衛生法是英國的重要公共衛生里程碑。",
    },
    45: {
        "topic": "Rose prevention：群體取向與高風險取向",
        "analysis": "群體取向是讓整體族群的暴露分布往低風險移動；找出高血脂病人給治療屬於高風險個體取向，不是群體取向。",
        "options": {
            "A": "屬群體取向。降低整體鹽分攝取能讓全人口血壓與心血管風險下降。",
            "B": "正確。篩出高血脂個案並治療，是個體或高風險取向，不是群體取向。",
            "C": "屬群體取向。增加學童戶外活動是改變整體學童族群暴露。",
            "D": "屬群體取向。禁止菸品廣告是政策層級降低整體族群菸害暴露。",
        },
        "core": "群體取向改變整體暴露分布；個體取向找高風險者介入。",
        "key": "找出高血脂病人治療屬個體取向，不是群體取向。",
    },
    46: {
        "topic": "藥物成癮：耐受性",
        "analysis": "反覆使用後同一劑量效果變弱，需要增加劑量才達到原效果，這是 tolerance。它和停藥症狀的 withdrawal 不同。",
        "options": {
            "A": "重覆性不是描述劑量需增加的標準成癮藥理名詞。",
            "B": "正確。耐受性是反覆使用後效果下降，需更高劑量達到原效果。",
            "C": "戒斷現象是停藥或減量後出現不適症狀，不是題幹的劑量增加需求。",
            "D": "強化現象指藥物增加再次使用行為的獎賞效果，不是效果下降需加量。",
        },
        "core": "Tolerance 是同劑量效果變弱；withdrawal 是停藥不舒服；reinforcement 是促使再使用。",
        "key": "反覆使用後需增加劑量達原效果稱耐受性。",
    },
    47: {
        "topic": "醫藥分業與調劑權",
        "analysis": "題目問醫藥分業最不恰當者。醫藥分業原則上由醫師診斷開方、藥事人員調劑；醫師在急迫或特定偏鄉等例外可交付藥劑，但不能把醫師法交付藥劑等同藥事法調劑並作為一般調劑權來源。",
        "options": {
            "A": "對。醫療急迫或無藥事人員執業地區等情境可有例外。",
            "B": "對。醫藥分業核心是醫師負責診斷治療與處方，藥師負責調劑與藥事服務。",
            "C": "對。藥事人員調劑需符合優良調劑作業，以保障用藥安全。",
            "D": "錯。交付藥劑與藥事法調劑不能直接等同，也不是醫師一般調劑權的法源。",
        },
        "core": "醫藥分業重點是處方與調劑角色分工；例外交付藥劑不等於一般調劑權。",
        "key": "醫師法交付藥劑不可等同藥事法調劑。",
    },
    48: {
        "topic": "三段五級預防：第二段預防",
        "analysis": "第二段預防是早期發現、早期治療，常以篩檢為代表。無症狀者做胸部 X 光檢查屬篩檢概念。",
        "options": {
            "A": "均衡飲食與規律運動屬第一段預防的健康促進。",
            "B": "不吸菸或戒菸屬第一段預防，降低疾病發生。",
            "C": "正確。針對無症狀者進行胸部 X 光檢查屬篩檢，是第二段預防。",
            "D": "接種卡介苗是特殊保護，屬第一段預防。",
        },
        "core": "第一段預防防發生；第二段預防靠篩檢早發現；第三段預防減少失能與復健。",
        "key": "無症狀者篩檢是第二段預防。",
    },
    49: {
        "topic": "衛生計畫評估：可接受性",
        "analysis": "衛生服務的可近性、可用性，以及民眾對服務的認知與接受程度，最符合 acceptability 的概念。",
        "options": {
            "A": "合法性重點是計畫是否符合法令與政策授權，不是民眾可近性與認知。",
            "B": "正確。可接受性涵蓋服務是否可被民眾接近、使用、理解與接受。",
            "C": "重要性評估問題嚴重度或優先性，不是服務使用感受。",
            "D": "充分性較偏資源或服務量是否足以達成需求，不完全等同民眾認知與可近性。",
        },
        "core": "看到 accessibility、availability、民眾認知與接受度，優先想到 acceptability。",
        "key": "衛生資源可近性、可用性與民眾認知最符合可接受性。",
    },
    50: {
        "topic": "靜態人口統計指標",
        "analysis": "某一時間點觀察的人口特質屬靜態描述，如人口數量、分布、組成；人口推估是利用模型預測未來人口，並非同類型的時間點觀察指標。",
        "options": {
            "A": "人口分布可在某一時間點描述不同地區人口狀態，屬靜態描述。",
            "B": "正確。人口推估是依資料與假設推測未來人口，不是單一時間點直接觀察所得。",
            "C": "人口組成如年齡、性別結構，可在某一時間點觀察。",
            "D": "人口數量是最基本的時間點人口統計指標。",
        },
        "core": "靜態人口指標描述某時點的人口狀態；人口推估是預測，不是同類型觀察值。",
        "key": "人口推估不是某一時間點直接觀察所得的人口特質指標。",
    },
}


DATA.update({
    51: {
        "topic": "生體可用率與給藥途徑",
        "analysis": "Bioavailability 是到達全身循環的未改變藥物比例。靜脈注射直接進入血液，定義上生體可用率為 100%，高於口服、直腸或吸入等途徑。",
        "options": {
            "A": "口服會受吸收不完全與 first-pass metabolism 影響，bioavailability 通常低於 IV。",
            "B": "直腸給藥可部分避開首渡效應，但吸收變異大，不是最高。",
            "C": "吸入型藥物可有快速局部或全身作用，但全身生體可用率不一定最高。",
            "D": "正確。Intravenous injection 直接進入全身循環，bioavailability 為 100%。",
        },
        "core": "問最高 bioavailability，答案幾乎永遠先看 IV，因其沒有吸收與首渡代謝損失。",
        "key": "靜脈注射生體可用率最高，定義為 100%。",
    },
    52: {
        "topic": "Cephalosporin 世代與 Pseudomonas",
        "analysis": "題目問 cephalosporins 錯誤敘述。Ceftazidime 與 cefoperazone 是具有抗綠膿桿菌活性的 cephalosporins，因此說兩者都無法治療 Pseudomonas 是錯的。",
        "options": {
            "A": "對。Cephalexin 是第一代，對革蘭陽性菌較好，對 Pseudomonas 效果差。",
            "B": "對。Cefuroxime 第二代可涵蓋 H. influenzae 等呼吸道病原。",
            "C": "錯。Ceftazidime 與 cefoperazone 都具抗 P. aeruginosa 活性。",
            "D": "對。Enterobacter 可誘導 AmpC beta-lactamase，使用 ceftriaxone 容易出現抗藥性。",
        },
        "core": "抗綠膿 cephalosporin 要記 ceftazidime、cefepime、cefoperazone 等；Enterobacter 小心 AmpC。",
        "key": "Ceftazidime 與 cefoperazone 可用於 Pseudomonas 感染。",
    },
    53: {
        "topic": "Doxorubicin 機轉與毒性",
        "analysis": "Doxorubicin 是 anthracycline 類抗腫瘤抗生素，主要抑制 topoisomerase II、嵌入 DNA 並產生自由基；不是抑制 topoisomerase I。",
        "options": {
            "A": "對。Doxorubicin 屬 anthracycline，傳統分類為抗腫瘤抗生素。",
            "B": "錯。Doxorubicin 主要抑制 topoisomerase II；topoisomerase I 抑制劑是 irinotecan、topotecan 等。",
            "C": "對。心肌自由基傷害與累積劑量相關心臟毒性是高產考點。",
            "D": "對。Doxorubicin 屬 cell cycle-nonspecific agent。",
        },
        "core": "Doxorubicin：topoisomerase II、free radical、cardiotoxicity；topoisomerase I 是 irinotecan/topotecan。",
        "key": "Doxorubicin 不是 topoisomerase I 抑制劑，而是 topoisomerase II 相關。",
    },
    54: {
        "topic": "Bleomycin 抗癌抗生素",
        "analysis": "Bleomycin 是抗腫瘤抗生素，可造成 DNA strand breaks，臨床作為抗癌藥；其餘選項主要是抗菌藥或不同用途。",
        "options": {
            "A": "正確。Bleomycin 可抑制腫瘤細胞增殖，主要臨床用途是抗癌，毒性常考肺纖維化。",
            "B": "Gentamicin 是 aminoglycoside 抗生素，主要治療細菌感染，不是抗癌藥。",
            "C": "Telithromycin 是 ketolide/macrolide 類抗生素，用於呼吸道感染等，不是抗癌藥。",
            "D": "Daptomycin 是抗革蘭陽性菌藥物，作用於細胞膜，不作為抗癌藥。",
        },
        "core": "抗癌抗生素常見 doxorubicin、bleomycin、dactinomycin；bleomycin 要記 DNA breaks 與肺毒性。",
        "key": "Bleomycin 是臨床抗癌用的抗生素類藥物。",
    },
    55: {
        "topic": "抗癌藥物基礎機轉",
        "analysis": "Cyclophosphamide 是 alkylating agent prodrug，須經肝臟 cytochrome P450 活化後產生 DNA alkylating 作用。",
        "options": {
            "A": "錯。Azathioprine 是 6-mercaptopurine 的前驅物，兩者屬免疫抑制/抗代謝藥，不是免疫增強劑。",
            "B": "錯。CHOP 的 C 是 cyclophosphamide，不是 cisplatin；H 是 doxorubicin，O 是 vincristine，P 是 prednisone。",
            "C": "正確。Cyclophosphamide 經 CYP450 活化後形成具 alkylating 作用的代謝物。",
            "D": "錯。Methotrexate 抑制 dihydrofolate reductase，不是 topoisomerase II。",
        },
        "core": "Cyclophosphamide 是 CYP 活化的 alkylating prodrug；MTX 抑制 DHFR；CHOP 的 C 是 cyclophosphamide。",
        "key": "Cyclophosphamide 需經 CYP450 活化才具 DNA alkylating 作用。",
    },
    56: {
        "topic": "Cyclosporine 與 calcineurin",
        "analysis": "Cyclosporine 抑制 calcineurin，減少 NFAT 活化與 IL-2 transcription，抑制 T 細胞活化。它不是主要減少 IL-1 產生。",
        "options": {
            "A": "對。Cyclosporine-cyclophilin complex 抑制 calcineurin。",
            "B": "對。Calcineurin 被抑制後 NFAT 無法有效進入細胞核促進 IL-2 表現。",
            "C": "錯。Cyclosporine 的核心是減少 IL-2，而不是 IL-1。",
            "D": "對。腎毒性與高血壓是 cyclosporine 重要副作用。",
        },
        "core": "Calcineurin inhibitors：cyclosporine、tacrolimus；都降低 IL-2，毒性常考腎毒性、高血壓。",
        "key": "Cyclosporine 主要減少 IL-2，不是 IL-1。",
    },
    57: {
        "topic": "Abciximab 與 GPIIb/IIIa",
        "analysis": "Abciximab 是 monoclonal antibody fragment，抑制血小板 GPIIb/IIIa receptor，阻斷 fibrinogen 橋接造成的血小板凝集。題目選項 B 把 receptor 寫成 IIIb/IIa，順序與名稱錯誤。",
        "options": {
            "A": "對。Abciximab 是單株抗體片段類抗血小板藥。",
            "B": "錯。正確標的是 glycoprotein IIb/IIIa，不是 IIIb/IIa。",
            "C": "對。抑制 GPIIb/IIIa 會阻斷 fibrinogen 介導的血小板聚集。",
            "D": "對。Tirofiban 也是 GPIIb/IIIa inhibitor，機轉類似但不是抗體。",
        },
        "core": "GPIIb/IIIa inhibitors 阻斷 fibrinogen 連接血小板；abciximab 是抗體，tirofiban/eptifibatide 是非抗體類。",
        "key": "Abciximab 的標的是 GPIIb/IIIa，不是 GPIIIb/IIa。",
    },
    58: {
        "topic": "Oprelvekin 重組 IL-11",
        "analysis": "Oprelvekin 是 recombinant IL-11，可刺激 megakaryocyte 與血小板生成，用於化療後血小板低下；它不是用來減少周邊嗜中性球。",
        "options": {
            "A": "對。IL-11 可促進 megakaryocyte 發育並提高血小板數。",
            "B": "對。IL-11 對多種造血與免疫細胞可有刺激作用。",
            "C": "錯。Oprelvekin 目標是改善 thrombocytopenia，不是降低 neutrophil 數量。",
            "D": "對。常見副作用包括疲倦、頭痛、水腫與心律不整等。",
        },
        "core": "Oprelvekin = IL-11 = 提升血小板；G-CSF/GM-CSF 才是白血球生成相關高產藥。",
        "key": "Oprelvekin 用於化療後血小板低下，不會主要減少 neutrophil。",
    },
    59: {
        "topic": "Tamoxifen 與 estrogen receptor",
        "analysis": "Tamoxifen 是 selective estrogen receptor modulator，於乳房組織拮抗 estrogen receptor，常用於 ER 陽性乳癌輔助治療。",
        "options": {
            "A": "Progesterone 不是主要作為 ER 標的乳癌輔助治療的代表藥。",
            "B": "Ketoconazole 抑制真菌 ergosterol 與人體 steroid synthesis，非乳癌 ER 標的輔助治療代表。",
            "C": "正確。Tamoxifen 作用於 estrogen receptor，用於 ER-positive breast cancer。",
            "D": "Danazol 是弱 androgen 類藥物，常與子宮內膜異位症等用途相關，不是 ER 乳癌輔助治療代表。",
        },
        "core": "ER-positive breast cancer 的經典藥物：tamoxifen 是 SERM；aromatase inhibitors 降低 estrogen 生成。",
        "key": "Tamoxifen 以 estrogen receptor 為主要標的治療乳癌。",
    },
    60: {
        "topic": "注射型降血糖藥：GLP-1 agonist",
        "analysis": "Liraglutide 是 GLP-1 receptor agonist，為 peptide 類藥物，臨床需皮下注射；其餘選項為口服降血糖藥。",
        "options": {
            "A": "Acarbose 是 alpha-glucosidase inhibitor，口服使用。",
            "B": "Saxagliptin 是 DPP-4 inhibitor，口服使用。",
            "C": "正確。Liraglutide 是 GLP-1 receptor agonist，需注射給藥。",
            "D": "Rosiglitazone 是 thiazolidinedione/PPAR-gamma agonist，口服使用。",
        },
        "core": "GLP-1 receptor agonists 多為注射型 peptide；DPP-4 inhibitor、TZD、alpha-glucosidase inhibitor 多為口服。",
        "key": "Liraglutide 必須以注射方式給予。",
    },
    61: {
        "topic": "Ketoconazole 抑制 steroid synthesis",
        "analysis": "腎上腺腫瘤造成 Cushing syndrome 時，可用抑制 steroid synthesis 的藥物降低 cortisol。Ketoconazole 可抑制多個 CYP steroidogenic enzymes，減少皮質醇生成。",
        "options": {
            "A": "Triamcinolone 是糖皮質素，會加重類 Cushing 狀態，不是減輕症狀。",
            "B": "Betamethasone 也是強效糖皮質素，不適合用來降低 Cushing 症狀。",
            "C": "Fludrocortisone 主要具 mineralocorticoid 活性，不是抑制 cortisol 生成的藥物。",
            "D": "正確。Ketoconazole 可抑制腎上腺 steroid synthesis，減少 Cushing syndrome 的 cortisol 過多。",
        },
        "core": "Cushing 藥物治療可用 ketoconazole、metyrapone、mitotane 等降低 steroid synthesis。",
        "key": "Ketoconazole 可抑制類固醇生成以改善 Cushing syndrome。",
    },
    62: {
        "topic": "直接 renin inhibitor",
        "analysis": "Aliskiren 是直接 renin inhibitor，可降低 angiotensin I 生成，用於高血壓；其他選項分別作用在 ACE、aldosterone receptor、AT1 receptor。",
        "options": {
            "A": "正確。Aliskiren 直接抑制 renin。",
            "B": "Captopril 是 ACE inhibitor，抑制 angiotensin I 轉成 angiotensin II。",
            "C": "Eplerenone 是 aldosterone receptor antagonist。",
            "D": "Losartan 是 angiotensin II receptor blocker，阻斷 AT1 receptor。",
        },
        "core": "RAAS 藥物定位：aliskiren 抑 renin，ACEI 抑 ACE，ARB 阻 AT1，spironolactone/eplerenone 阻 aldosterone receptor。",
        "key": "Aliskiren 是直接 renin inhibitor。",
    },
    63: {
        "topic": "Amiodarone 與甲狀腺作用",
        "analysis": "Amiodarone 含碘且會影響甲狀腺功能，可抑制 T4 轉換成 T3，也可能造成 hypo- 或 hyperthyroidism。",
        "options": {
            "A": "Adenosine 作用於 AV node，短效治療 PSVT，不是 T4 轉 T3 的典型藥物。",
            "B": "正確。Amiodarone 可抑制 peripheral conversion of T4 to T3，且有多種甲狀腺毒性。",
            "C": "Lidocaine 是 class Ib 抗心律不整藥，不具此甲狀腺轉換抑制特色。",
            "D": "Dronedarone 結構類似但不含碘，甲狀腺影響較 amiodarone 少，較不符合題幹強調的 T4 轉 T3 抑制。",
        },
        "core": "Amiodarone 毒性記肺纖維化、甲狀腺異常、肝毒性、角膜沉積、皮膚變色。",
        "key": "Amiodarone 可抑制 T4 轉變為 T3。",
    },
    64: {
        "topic": "Vasopressin antagonist：vaptans",
        "analysis": "Tolvaptan 是口服 V2 receptor antagonist，可促進 free water excretion，用於低血鈉等情境；conivaptan 通常為靜脈使用。",
        "options": {
            "A": "Conivaptan 是 vasopressin receptor antagonist，但臨床多為 IV，不是口服型代表。",
            "B": "Metolazone 是 thiazide-like diuretic，不是 ADH antagonist。",
            "C": "Triamterene 是 ENaC blocker，屬保鉀利尿劑，不是 vaptan。",
            "D": "正確。Tolvaptan 是口服 V2 antagonist。",
        },
        "core": "Vasopressin antagonists 字尾常是 -vaptan；tolvaptan 口服，促進 aquaresis。",
        "key": "Tolvaptan 是口服 vasopressin/ADH receptor antagonist。",
    },
    65: {
        "topic": "Mirabegron 與過動膀胱",
        "analysis": "Mirabegron 是 beta-3 adrenergic receptor agonist，可放鬆逼尿肌，治療 overactive bladder。",
        "options": {
            "A": "Sibutramine 是減重相關藥物，非 beta-3 過動膀胱治療藥。",
            "B": "Lorcaserin 是 5-HT2C agonist 減重藥，不是膀胱 beta-3 藥物。",
            "C": "正確。Mirabegron 活化 beta-3 adrenoceptor，促進膀胱儲尿期逼尿肌放鬆。",
            "D": "Buspirone 是 5-HT1A partial agonist，主要用於焦慮，不治療 overactive bladder。",
        },
        "core": "過動膀胱藥物：抗 muscarinic 或 beta-3 agonist mirabegron。",
        "key": "Mirabegron 透過 beta-3 receptor 治療過動膀胱。",
    },
    66: {
        "topic": "Varenicline 戒菸藥理",
        "analysis": "Varenicline 是 alpha4beta2 nicotinic acetylcholine receptor partial agonist，用於戒菸；不是 muscarinic receptor antagonist。",
        "options": {
            "A": "錯。Varenicline 作用於 nicotinic receptor，非 muscarinic receptor antagonist。",
            "B": "對。主要臨床用途是 smoking cessation。",
            "C": "對。可能出現情緒、睡眠或神經精神相關副作用，需臨床注意。",
            "D": "對。戒菸效果通常優於 bupropion。",
        },
        "core": "Varenicline = alpha4beta2 nicotinic partial agonist；bupropion = NE/DA reuptake inhibition 與 nicotinic antagonism。",
        "key": "Varenicline 不是 muscarinic antagonist，而是 nicotinic partial agonist。",
    },
    67: {
        "topic": "Zafirlukast 氣喘機轉",
        "analysis": "Zafirlukast 是 leukotriene receptor antagonist，阻斷 cysteinyl leukotriene receptor，減少支氣管收縮與發炎。",
        "options": {
            "A": "Adenosine receptor antagonist 不是 zafirlukast 的機轉。",
            "B": "正確。Zafirlukast 拮抗 leukotriene receptor，用於氣喘控制。",
            "C": "減少 cAMP 降解是 phosphodiesterase inhibitor 如 theophylline 的機轉。",
            "D": "減少組織胺釋放較接近 mast cell stabilizer 或抗組織胺概念，不是 zafirlukast。",
        },
        "core": "Leukotriene modifiers：montelukast/zafirlukast 阻 receptor；zileuton 抑 5-lipoxygenase。",
        "key": "Zafirlukast 是 leukotriene receptor antagonist。",
    },
    68: {
        "topic": "Alvimopan",
        "analysis": "Alvimopan 是周邊 mu-opioid receptor antagonist，用於減少術後腸阻塞；中樞穿透少，但使用上有住院與療程限制，且曾有心血管安全疑慮。",
        "options": {
            "A": "正確。Alvimopan 屬周邊鴉片受體拮抗劑，臨床使用需注意心血管風險與限制。",
            "B": "錯。它較少進入中樞神經；限制使用不是因中樞作用強。",
            "C": "錯。因主要作用周邊，可與術後鴉片止痛併用以減少腸道副作用，不會明顯拮抗中樞止痛。",
            "D": "錯。Alvimopan 是口服藥，住院限制與安全管理相關，不是只能注射。",
        },
        "core": "Alvimopan 是周邊 mu antagonist：改善 opioid-related/postoperative ileus，少進 CNS，口服但有使用限制。",
        "key": "Alvimopan 是周邊鴉片受體拮抗劑並需注意心血管安全。",
    },
    69: {
        "topic": "5-HT4 agonist 與腸胃蠕動",
        "analysis": "官方答案為 tegaserod。Tegaserod 是 5-HT4 receptor agonist，可促進腸胃蠕動；cisapride 也有 5-HT4 agonist 性質但因心律風險限制，題目在選項中以 tegaserod 作為最適合答案。",
        "options": {
            "A": "正確。Tegaserod 是 5-HT4 agonist，促進 acetylcholine 釋放與腸胃蠕動。",
            "B": "Cisapride 也具 5-HT4 agonist/prokinetic 作用，但因 QT prolongation 與心律不整風險，臨床使用受限；本題官方取 tegaserod。",
            "C": "Fluoxetine 是 SSRI，主要用於憂鬱症等，不是 5-HT4 agonist。",
            "D": "Ritanserin 是 serotonin receptor antagonist 類，不是 5-HT4 agonist 促蠕動藥。",
        },
        "core": "5-HT4 agonist 可促進腸胃蠕動；考題若在 tegaserod 與其他藥間選，tegaserod 是典型答案。",
        "key": "Tegaserod 是 5-HT4 agonist。",
    },
    70: {
        "topic": "Dinoprostone 引產",
        "analysis": "Dinoprostone 是 prostaglandin E2，可促進子宮頸成熟與誘發子宮收縮，常用於引產。",
        "options": {
            "A": "正確。Dinoprostone/PGE2 可用於 cervical ripening 與 induction of labor。",
            "B": "Alprostadil 是 PGE1，常用於維持動脈導管開放或勃起功能相關用途，不是最適合引產答案。",
            "C": "Iloprost 是 prostacyclin analog，用於肺動脈高壓等，不作引產主藥。",
            "D": "Latanoprost 是 PGF2alpha analog，用於青光眼降低眼壓。",
        },
        "core": "引產與子宮頸成熟常用 PGE2 dinoprostone；維持 PDA 用 PGE1 alprostadil；青光眼用 latanoprost。",
        "key": "Dinoprostone 是適合用於懷孕婦女引產的 PGE2。",
    },
    71: {
        "topic": "Zileuton 與氣喘",
        "analysis": "Zileuton 抑制 5-lipoxygenase，減少 leukotriene 合成，可用於輕中度氣喘控制。其他選項不是氣喘控制藥，NSAIDs 還可能誘發氣喘惡化。",
        "options": {
            "A": "Misoprostol 是 PGE1 analog，用於胃潰瘍預防或婦產科用途，不治療氣喘。",
            "B": "Ibuprofen 是 NSAID，非氣喘治療藥，部分病人還會因 COX inhibition 誘發氣喘。",
            "C": "正確。Zileuton 抑制 5-lipoxygenase，降低 leukotriene，適用於氣喘控制。",
            "D": "Indomethacin 是 NSAID，不是氣喘治療藥，亦可能加重 aspirin-sensitive asthma。",
        },
        "core": "氣喘 leukotriene 路徑：zileuton 抑 5-LOX，montelukast/zafirlukast 阻 receptor。",
        "key": "Zileuton 可用於輕中度氣喘，因其抑制 leukotriene 合成。",
    },
    72: {
        "topic": "Fluoxetine 與 serotonin",
        "analysis": "Fluoxetine 是 selective serotonin reuptake inhibitor，抗憂鬱作用主要與增加 synaptic serotonin 有關。",
        "options": {
            "A": "Norepinephrine 與 SNRI、TCA 等有關，但 fluoxetine 最典型是 serotonin。",
            "B": "正確。Fluoxetine 抑制 serotonin reuptake，提高 5-HT 神經傳遞。",
            "C": "Glutamate 不是 fluoxetine 的主要抗憂鬱機轉。",
            "D": "Acetylcholine 與抗膽鹼副作用等較相關，不是 fluoxetine 的主要機轉。",
        },
        "core": "SSRI 名稱常 -oxetine、-traline、-pram；核心是增加 serotonin。",
        "key": "Fluoxetine 的抗憂鬱作用主要與 serotonin 有關。",
    },
    73: {
        "topic": "Phenytoin 藥理與酵素誘導",
        "analysis": "Phenytoin 延長 voltage-gated sodium channel inactive state，且是肝臟微粒體酵素誘導劑，會增加許多藥物代謝；說它抑制酵素、減少代謝是錯的。",
        "options": {
            "A": "對。Phenytoin 延長鈉離子通道不反應期，抑制高頻放電。",
            "B": "錯。Phenytoin 是 CYP enzyme inducer，通常增加其他藥物代謝。",
            "C": "對。Phenytoin 高度與 albumin 結合，低白蛋白時游離濃度會上升。",
            "D": "對。Fosphenytoin 是水溶性前驅藥，溶解度較 phenytoin 好。",
        },
        "core": "Phenytoin：Na channel、零級動力學、高蛋白結合、CYP inducer、牙齦增生與毛髮增多等副作用。",
        "key": "Phenytoin 是肝酵素誘導劑，不是抑制劑。",
    },
    74: {
        "topic": "鴉片類耐受性例外",
        "analysis": "長期使用鴉片類會對鎮痛、欣快、呼吸抑制等產生耐受，但 miosis 與 constipation 通常較不易產生耐受。",
        "options": {
            "A": "正確。瞳孔縮小對鴉片耐受性較不明顯，是長期使用仍可見的表現。",
            "B": "鎮痛效果會逐漸產生耐受，需要較高劑量。",
            "C": "咳嗽抑制也可產生一定耐受，不是最不容易的選項。",
            "D": "欣快感會產生耐受，與成癮用藥增加相關。",
        },
        "core": "Opioid tolerance 常見，但 miosis 和 constipation 相對不易產生耐受。",
        "key": "鴉片類作用中，miosis 最不容易產生耐受。",
    },
    75: {
        "topic": "鐵中毒解毒劑",
        "analysis": "Deferoxamine 是鐵螯合劑，適用於急性鐵中毒或鐵過量；會形成 ferrioxamine，可使尿液呈 vin rose 色。",
        "options": {
            "A": "Dimercaprol 用於砷、汞、鉛等重金屬中毒，不是鐵中毒首選。",
            "B": "Penicillamine 常用於銅中毒/Wilson disease，也可用於部分重金屬，不是鐵中毒主藥。",
            "C": "Melarsoprol 是非洲錐蟲病藥物，不治療鐵中毒。",
            "D": "正確。Deferoxamine 螯合鐵，是鐵中毒主要治療藥物。",
        },
        "core": "解毒劑配對：鐵 deferoxamine/deferasirox；銅 penicillamine；鉛 EDTA/dimercaprol/succimer。",
        "key": "鐵中毒使用 deferoxamine。",
    },
    76: {
        "topic": "腦梗塞與液化壞死",
        "analysis": "腦組織缺血梗塞後，因酵素分解與巨噬細胞清除，常形成液化壞死，數月後可留下囊性空洞。",
        "options": {
            "A": "正確。中樞神經系統梗塞典型是 liquefactive necrosis，晚期可形成 cystic cavity。",
            "B": "凝固性壞死較常見於心、腎、脾等實質器官缺血梗塞，不是腦梗塞典型。",
            "C": "乾酪性壞死常見於結核等肉芽腫感染。",
            "D": "凋亡是個別細胞程序性死亡，不會形成 4 公分囊性空洞的典型病理。",
        },
        "core": "缺血壞死例外：腦梗塞是液化壞死；多數其他實質器官是凝固性壞死。",
        "key": "大腦梗塞後囊性空洞代表液化壞死。",
    },
    77: {
        "topic": "TGF-beta 與纖維化",
        "analysis": "TGF-beta 是促進 fibroblast activation、collagen deposition 與組織纖維化的核心 cytokine/growth factor。",
        "options": {
            "A": "正確。TGF-beta 是纖維化與膠原沉積最重要的促進因子之一。",
            "B": "IL-1 促發炎與發燒等，雖可間接參與修復，但不是纖維化最核心答案。",
            "C": "Selectin 主要參與白血球滾動與黏附。",
            "D": "Histamine 造成血管擴張、通透性增加與過敏反應，不是纖維化主因。",
        },
        "core": "Fibrosis 高產因子就是 TGF-beta：刺激 fibroblast 與 collagen。",
        "key": "組織纖維化最相關的是 TGF-beta。",
    },
    78: {
        "topic": "感覺神經元潛伏感染：HSV/VZV",
        "analysis": "HSV 與 VZV 都屬 herpesvirus，可在感覺神經節建立 latent infection，日後再活化造成復發性疱疹或帶狀疱疹；poliovirus 不以感覺神經元潛伏感染為主要病理。",
        "options": {
            "A": "包含 poliovirus，因此錯。Poliovirus 主要侵犯運動神經元造成急性無力，不是感覺神經元潛伏。",
            "B": "包含 poliovirus 且缺少 VZV，因此錯。",
            "C": "包含 poliovirus 且缺少 HSV，因此錯。",
            "D": "正確。HSV 與 VZV 會潛伏於感覺神經節，造成復發性臨床表現。",
        },
        "core": "Herpesviruses 特色是 latent infection；HSV/VZV 潛伏在感覺神經節。",
        "key": "HSV 與 VZV 可在感覺神經元建立潛伏感染。",
    },
    79: {
        "topic": "象腿症與絲蟲病",
        "analysis": "象腿症是淋巴阻塞導致肢體或陰囊巨大腫脹，最典型病因是淋巴絲蟲感染，如 Wuchereria bancrofti。",
        "options": {
            "A": "猩紅熱由 A 群鏈球菌毒素造成皮疹與咽炎，不造成象腿症。",
            "B": "弓漿蟲病不以淋巴阻塞性象腿症為主要表現。",
            "C": "膿痂疹是皮膚細菌感染，不是象腿症典型病因。",
            "D": "正確。Filariasis 可造成慢性淋巴阻塞與 elephantiasis。",
        },
        "core": "Elephantiasis 幾乎直接聯想 lymphatic filariasis。",
        "key": "象腿症最典型出現於絲蟲病。",
    },
    80: {
        "topic": "惡性腫瘤細胞形態：不典型有絲分裂",
        "analysis": "高核質比、深染與多形性可在反應性或增生性良性細胞中某種程度出現；不典型有絲分裂最支持惡性，最不可能出現在良性細胞。",
        "options": {
            "A": "正確。Atypical mitoses 是惡性腫瘤重要形態特徵，良性細胞最不應出現。",
            "B": "高核質比可提示惡性，但某些未成熟或反應性細胞也可較高，不如 atypical mitoses 特異。",
            "C": "Hyperchromasia 可見於惡性，也可能在退化或反應性變化中出現。",
            "D": "Pleomorphism 支持惡性，但某些良性反應或內分泌組織也可有形態變異。",
        },
        "core": "惡性形態中最特異要看 atypical mitotic figures、侵犯與轉移；單一深染或多形性較不特異。",
        "key": "Atypical mitoses 最不可能出現在良性細胞。",
    },
    81: {
        "topic": "擴張型心肌病與收縮功能障礙",
        "analysis": "以 systolic dysfunction 為主的心肌病常見於 dilated cardiomyopathy，原因包括酒精、doxorubicin、病毒性心肌炎、TTN mutation 等；amyloidosis 通常造成 restrictive cardiomyopathy 與舒張功能障礙。",
        "options": {
            "A": "只包含酒精與 doxorubicin，漏掉 TTN mutation，因此不完整。",
            "B": "正確。酒精、doxorubicin、TTN 基因突變皆可造成以收縮功能障礙為主的心肌病。",
            "C": "漏掉酒精，且 doxorubicin 也是重要原因，因此不完整。",
            "D": "包含 amyloidosis；類澱粉沉積較典型是 restrictive cardiomyopathy，不是 systolic dysfunction 主機轉。",
        },
        "core": "Dilated cardiomyopathy 對 systolic dysfunction；restrictive cardiomyopathy 對 amyloidosis 與 diastolic dysfunction。",
        "key": "酒精、doxorubicin、TTN mutation 可造成收縮功能障礙心肌病。",
    },
    82: {
        "topic": "PTT 延長疾病",
        "analysis": "PTT 反映 intrinsic/common pathway。Hemophilia A 因 factor VIII 缺乏會延長 PTT；Von Willebrand disease 因 vWF 穩定 factor VIII，也可使 PTT 增加。TTP 與 Glanzmann 主要是血小板問題，PTT 通常不延長。",
        "options": {
            "A": "包含 Hemophilia A 正確，但 TTP 通常凝血時間正常，因此不對。",
            "B": "正確。Hemophilia A 與 VWD 都可造成 PTT 增加。",
            "C": "Glanzmann 是 GPIIb/IIIa 缺陷造成血小板聚集異常，PT/PTT 通常正常。",
            "D": "包含 Glanzmann，故不正確；TTP 與 VWD 的機轉也不同。",
        },
        "core": "PTT 延長：intrinsic pathway factor 缺乏或 inhibitor；VWD 可因 factor VIII 降低而延長 PTT。",
        "key": "Hemophilia A 與 Von Willebrand disease 可增加 PTT。",
    },
    83: {
        "topic": "胸腺濾泡增生與重症肌無力",
        "analysis": "Thymic follicular hyperplasia 最典型與 myasthenia gravis 相關，病理可見 germinal centers，反映自體免疫 B 細胞反應。",
        "options": {
            "A": "類風濕性關節炎可有淋巴濾泡樣變化，但不是胸腺濾泡增生最典型疾病。",
            "B": "正確。重症肌無力常合併 thymic follicular hyperplasia，也可合併 thymoma。",
            "C": "Graves disease 是自體免疫甲狀腺疾病，不是胸腺濾泡增生最常見配對。",
            "D": "硬皮症與纖維化、自體免疫相關，不是此胸腺病變典型答案。",
        },
        "core": "MG 與 thymus 關聯很強：可見 thymic hyperplasia 或 thymoma。",
        "key": "胸腺淋巴濾泡增生最常見於重症肌無力。",
    },
    84: {
        "topic": "Thymoma 與 pure red cell aplasia",
        "analysis": "Thymoma 可伴隨多種副腫瘤自體免疫表現，包含 myasthenia gravis、pure red cell aplasia 和 hypogammaglobulinemia。",
        "options": {
            "A": "畸胎瘤可含多胚層組織，但不是 pure red cell aplasia 最典型腫瘤。",
            "B": "正確。Thymoma 最常與 pure red cell aplasia 併發。",
            "C": "腦膜瘤不以純紅血球再生不良為典型副腫瘤表現。",
            "D": "生殖細胞瘤不是 PRCA 的經典配對。",
        },
        "core": "Thymoma 的伴隨疾病：myasthenia gravis、pure red cell aplasia、Good syndrome。",
        "key": "純紅血球再生不良最常併發胸腺瘤。",
    },
    85: {
        "topic": "藥物相關貧血類型",
        "analysis": "G6PD 溶血、大球性貧血與再生不良性貧血都可由藥物引發；小球性貧血最常與缺鐵、慢性病或血紅素合成異常相關，與藥物使用最不直接。",
        "options": {
            "A": "G6PD 缺乏者使用氧化性藥物可誘發溶血性貧血。",
            "B": "大球性貧血可由 methotrexate、trimethoprim、phenytoin 等影響葉酸代謝藥物造成。",
            "C": "再生不良性貧血可與 chloramphenicol、化療藥等藥物相關。",
            "D": "正確。小球性貧血多與缺鐵或 thalassemia 等相關，與藥物使用最不相關。",
        },
        "core": "藥物可造成溶血、巨球性或骨髓抑制；小球性貧血優先想缺鐵與血紅素病。",
        "key": "小球性貧血與藥物使用最不相關。",
    },
    86: {
        "topic": "肺腺癌流行病學",
        "analysis": "肺腺癌是最常見的原發性肺癌型態，特別常見於女性、年輕、非吸菸者與周邊肺部病灶。",
        "options": {
            "A": "鱗狀細胞癌與吸菸關聯強，常中央型，不是年輕不抽菸女性最常見。",
            "B": "正確。Adenocarcinoma 是年輕女性與非吸菸者最常見的原發性肺癌。",
            "C": "小細胞癌與吸菸高度相關，惡性度高，常中央型。",
            "D": "大細胞癌較少見，不是此族群最常見型態。",
        },
        "core": "非吸菸者、女性、周邊肺癌，優先想到 adenocarcinoma。",
        "key": "年輕不抽菸女性最常見原發性肺癌是腺癌。",
    },
    87: {
        "topic": "瀰漫性阻塞性肺疾病",
        "analysis": "COPD/阻塞性肺疾病包括肺氣腫、慢性支氣管炎、支氣管擴張與氣喘等；ARDS 是急性瀰漫性肺泡傷害造成的限制性/換氣障礙，不屬於瀰漫性阻塞性肺疾病。",
        "options": {
            "A": "肺氣腫是 COPD 代表之一，屬阻塞性肺疾病。",
            "B": "慢性支氣管炎是 COPD 代表之一。",
            "C": "支氣管擴張會造成阻塞性通氣障礙與慢性化膿性感染。",
            "D": "正確。ARDS 是急性肺泡上皮與微血管傷害，不屬於瀰漫性阻塞性肺疾病。",
        },
        "core": "阻塞性肺病看氣流呼出受限；ARDS 是 diffuse alveolar damage，不是 COPD 類。",
        "key": "ARDS 不屬於瀰漫性阻塞性肺疾病。",
    },
    88: {
        "topic": "氣喘病理與過敏型態",
        "analysis": "氣喘常與 Th2、IgE、eosinophil、Curschmann spirals、Charcot-Leyden crystals 相關，屬第一型過敏反應；說屬第二型過敏反應最不適當。",
        "options": {
            "A": "對。Th2 細胞分泌 IL-4、IL-5、IL-13，促進 IgE、嗜酸性球和黏液分泌。",
            "B": "錯。氣喘典型屬 type I hypersensitivity，不是 type II cytotoxic hypersensitivity。",
            "C": "對。嗜酸性白血球增加是過敏性氣喘常見特徵。",
            "D": "對。Curschmann spirals 是支氣管黏液栓旋渦狀結構，可見於氣喘。",
        },
        "core": "氣喘病理記 type I hypersensitivity、Th2、IgE、eosinophils、Curschmann spirals。",
        "key": "氣喘最不適當的敘述是屬於第二型過敏反應。",
    },
    89: {
        "topic": "急性胰臟炎原因",
        "analysis": "急性胰臟炎常見原因包括膽石、酒精、高三酸甘油脂、ERCP、藥物與高血鈣；低血鈣通常是胰臟炎結果或嚴重度指標，不是常見原因。",
        "options": {
            "A": "酗酒是急性胰臟炎最常見原因之一。",
            "B": "胰管阻塞，特別是膽石阻塞壺腹部，可引發急性胰臟炎。",
            "C": "高三酸甘油脂血症是急性胰臟炎重要原因。",
            "D": "正確。低血鈣不是常見原因；相反地，急性胰臟炎可因脂肪皂化造成低血鈣。",
        },
        "core": "急性胰臟炎原因記 gallstones、alcohol、hypertriglyceridemia、hypercalcemia；hypocalcemia 是結果。",
        "key": "低血鈣不是常見急性胰臟炎原因。",
    },
    90: {
        "topic": "唾液腺腫瘤",
        "analysis": "最常見唾液腺良性腫瘤是 pleomorphic adenoma；最常見惡性唾液腺腫瘤通常是 mucoepidermoid carcinoma，不是 squamous cell carcinoma。",
        "options": {
            "A": "對。Pleomorphic adenoma 是最常見唾液腺良性腫瘤。",
            "B": "錯。最常見唾液腺惡性腫瘤為 mucoepidermoid carcinoma，而不是 squamous cell carcinoma。",
            "C": "對。Mucoepidermoid carcinoma 常見 MAML2 translocation。",
            "D": "對。Adenoid cystic carcinoma 典型有 perineural invasion，疼痛與復發風險高。",
        },
        "core": "唾液腺：最常見良性 pleomorphic adenoma；最常見惡性 mucoepidermoid carcinoma；adenoid cystic carcinoma 愛侵犯神經。",
        "key": "最常見唾液腺惡性腫瘤不是鱗狀細胞癌，而是黏液表皮樣癌。",
    },
    91: {
        "topic": "Warthin tumor",
        "analysis": "老年男性、腮腺附近、雙層上皮、囊狀裂隙、豐富淋巴組織與 germinal center，典型是 Warthin tumor。出現軟骨樣間質是 pleomorphic adenoma 的特色，不是 Warthin tumor。",
        "options": {
            "A": "對。Warthin tumor 最常發生在腮腺。",
            "B": "對。Warthin tumor 可多發或雙側，約一部分病例為雙側。",
            "C": "錯。明顯上皮與間質分化、軟骨樣物質是 pleomorphic adenoma，不是 Warthin tumor。",
            "D": "對。Warthin tumor 與吸菸有強關聯。",
        },
        "core": "Warthin tumor：腮腺、吸菸、雙側、oncocytic epithelium 加 lymphoid stroma。",
        "key": "Warthin tumor 不以軟骨樣間質為特色；那是 pleomorphic adenoma。",
    },
    92: {
        "topic": "Brunn nests",
        "analysis": "Brunn nests 是膀胱尿路上皮向下陷入形成的小巢，最常位於 lamina propria。",
        "options": {
            "A": "正確。Brunn nests 位於膀胱固有層，是尿路上皮增生/內陷的常見良性變化。",
            "B": "內層肌肉不是 Brunn nests 最常位置。",
            "C": "外層肌肉更不是典型位置，若病變侵犯肌層需考慮惡性浸潤等問題。",
            "D": "外膜層不是 Brunn nests 的所在。",
        },
        "core": "Brunn nests 是 urothelium invagination into lamina propria。",
        "key": "Brunn nests 最常位於膀胱固有層。",
    },
    93: {
        "topic": "Renal angiomyolipoma",
        "analysis": "腎臟 angiomyolipoma 由血管、平滑肌與脂肪組成，與 tuberous sclerosis 有關；臨床重點是血管成分可導致自發性出血，尤其腫瘤較大時。",
        "options": {
            "A": "錯。Angiomyolipoma 是良性腫瘤，惡性轉變不是主要臨床意義。",
            "B": "正確。腎血管平滑肌脂肪瘤容易自發性出血，是重要臨床風險。",
            "C": "錯。早期腎衰竭不是其典型主要表現。",
            "D": "錯。散發性病例通常單側單發；雙側多發較常見於 tuberous sclerosis 相關病例。",
        },
        "core": "Angiomyolipoma 是良性但會出血；雙側多發要想到 tuberous sclerosis。",
        "key": "腎血管平滑肌脂肪瘤重要風險是自發性出血。",
    },
    94: {
        "topic": "Pituitary adenoma",
        "analysis": "Pituitary adenoma 大多為良性；良惡性不能靠一般形態可靠判斷，癌需有顱內外轉移。大型腺瘤可發生腫瘤內出血與壞死，造成 pituitary apoplexy。",
        "options": {
            "A": "錯。Pituitary carcinoma 的診斷需有轉移，單純局部侵犯腦組織不足以診斷為癌。",
            "B": "錯。腺瘤通常破壞正常 acinar architecture，reticulin network 減少而非明顯增加。",
            "C": "錯。垂體腺瘤良惡性不能單靠細胞形態可靠判定。",
            "D": "正確。Macroadenoma 可因供血不足出現出血、壞死與急性症狀。",
        },
        "core": "Pituitary carcinoma 靠轉移診斷；macroadenoma 可 apoplexy；reticulin pattern 有助區分腺瘤與正常垂體。",
        "key": "大型腦下垂體腺瘤常可出現腫瘤內出血與壞死。",
    },
    95: {
        "topic": "子宮內膜異位症與卵巢癌",
        "analysis": "Endometriosis 是子宮外出現 endometrial glands/stroma，最常在卵巢，可造成疼痛與不孕；相關卵巢癌主要是 endometrioid carcinoma 和 clear cell carcinoma，不是漿液性癌。",
        "options": {
            "A": "對。子宮內膜異位症指 ectopic endometrial tissue 位於子宮外。",
            "B": "對。最常見位置是卵巢，也可見於骨盆腹膜等。",
            "C": "對。可因發炎、沾黏與卵巢病灶增加不孕。",
            "D": "錯。與 endometriosis 相關的卵巢癌主要是 endometrioid 與 clear cell carcinoma。",
        },
        "core": "Endometriosis 關聯癌種：endometrioid carcinoma、clear cell carcinoma。",
        "key": "子宮內膜異位症相關卵巢癌不是主要漿液性癌。",
    },
    96: {
        "topic": "子宮平滑肌瘤基因",
        "analysis": "Leiomyoma 是最常見子宮肌層腫瘤，多數有 MED12 mutation，惡性轉化少見；但只有一部分有異常核型，不能說大部分都有異常且複雜的 karyotype。",
        "options": {
            "A": "對。子宮肌層最常見腫瘤是 leiomyoma。",
            "B": "錯。平滑肌瘤可有染色體異常，但大部分不是異常且複雜的 karyotype；此描述過度。",
            "C": "對。MED12 mutation 是多數 leiomyoma 的常見分子改變。",
            "D": "對。Leiomyosarcoma 多為 de novo，leiomyoma 惡性轉化少見。",
        },
        "core": "Leiomyoma：常見、良性、MED12 mutation、惡變少；leiomyosarcoma 通常 de novo。",
        "key": "多數平滑肌瘤有 MED12 突變，但不是大部分都有複雜異常核型。",
    },
    97: {
        "topic": "卵巢亮細胞癌",
        "analysis": "卵巢 clear cell carcinoma 是惡性上皮性腫瘤，常與 endometriosis 相關；良性或 borderline clear cell tumor 罕見，不比癌常見。",
        "options": {
            "A": "錯。良性或 borderline 卵巢亮細胞腫瘤少見，clear cell carcinoma 才是主要臨床實體。",
            "B": "對。治療原則多依卵巢上皮癌處理，包含手術分期與含鉑化療等。",
            "C": "對。常見基因改變如 ARID1A、PIK3CA 等，與 endometrioid carcinoma 有重疊。",
            "D": "對。晚期 clear cell carcinoma 預後較差，對化療反應也較不佳。",
        },
        "core": "Ovarian clear cell carcinoma 與 endometriosis、ARID1A/PIK3CA 相關；良性/交界性型態不常見。",
        "key": "良性或交界性卵巢亮細胞腫瘤不比亮細胞癌常見。",
    },
    98: {
        "topic": "感染與周邊神經病變",
        "analysis": "白喉毒素可造成神經病變，VZV 可造成神經痛，痲瘋病直接侵犯周邊神經；結核分枝桿菌較不典型直接造成周邊神經病變。",
        "options": {
            "A": "正確。Mycobacterium tuberculosis 主要造成肺部與全身性肉芽腫感染，較不會直接引起周邊神經病變。",
            "B": "白喉毒素可造成脫髓鞘性神經病變與顱神經/周邊神經症狀。",
            "C": "水痘帶狀疱疹病毒潛伏於感覺神經節，再活化可造成帶狀疱疹後神經痛。",
            "D": "痲瘋分枝桿菌特別侵犯 Schwann cells，周邊神經病變是核心表現。",
        },
        "core": "周邊神經感染高產：leprosy、diphtheria toxin、VZV；TB 不是典型答案。",
        "key": "結核分枝桿菌較不會引起周邊神經病變。",
    },
    99: {
        "topic": "高級別 astrocytoma 預後：IDH1",
        "analysis": "Diffuse astrocytoma/glioblastoma 中，IDH mutation 相較 IDH-wildtype 通常代表較好預後與較長存活，是 WHO 分類與預後的重要分子標記。",
        "options": {
            "A": "NF1 可見於部分 glioma 或症候群相關腫瘤，但不是本題高級別 astrocytoma 較佳存活率的代表突變。",
            "B": "TP53 常見於 astrocytoma 分子路徑，但單獨不是較佳預後最典型標記。",
            "C": "正確。IDH1 mutation 相較 wild-type 通常預後較好。",
            "D": "EGFR amplification/alteration 常與 glioblastoma IDH-wildtype 相關，並非較好預後標記。",
        },
        "core": "Adult diffuse glioma 分子預後：IDH-mutant 通常比 IDH-wildtype 好。",
        "key": "IDH1 突變相較 wild-type 具有較好存活率。",
    },
    100: {
        "topic": "TTF-1 免疫染色與肺腺癌轉移",
        "analysis": "TTF-1 是肺與甲狀腺來源上皮腫瘤常用免疫標記。多顆腦瘤疑似轉移時，做 TTF-1 可協助判斷是否為肺腺癌轉移。",
        "options": {
            "A": "TTF-1 不是用來直接判定良性或惡性的染色，良惡性需結合形態與臨床。",
            "B": "細胞分裂快慢通常看 mitotic count 或 Ki-67，不是 TTF-1。",
            "C": "正確。TTF-1 陽性支持肺腺癌或甲狀腺來源；在多發腦瘤情境常用來評估肺腺癌轉移。",
            "D": "TTF-1 是上皮來源特定器官標記，不是用來判定是否非上皮性腫瘤的主要染色。",
        },
        "core": "腦部轉移腫瘤做 TTF-1，是為了找肺腺癌/甲狀腺來源；肺腺癌腦轉移很常見。",
        "key": "TTF-1 染色可協助判斷是否肺腺癌轉移。",
    },
})


def make_explanation(item):
    return (
        f"【題幹解析】\n{item['analysis']}\n\n"
        "【選項詳解】\n"
        f"- A. {item['options']['A']}\n"
        f"- B. {item['options']['B']}\n"
        f"- C. {item['options']['C']}\n"
        f"- D. {item['options']['D']}\n\n"
        f"【核心考點】\n{item['core']}"
    )


def main():
    source = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    questions = {q["question_number"]: q for q in source["questions"]}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for start in range(1, 101, 10):
        end = start + 9
        updates = []
        for number in range(start, end + 1):
            q = questions[number]
            item = DATA[number]
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": number,
                    "explanation": make_explanation(item),
                    "key_point": item["key"],
                    "flashcard_front": item["topic"],
                    "flashcard_back": item["core"],
                    "flashcard_summary": f"{item['topic']}：{item['key']}",
                    "review_status": "ai_generated",
                    "explanation_model": "codex-high-quality-rewrite",
                    "explanation_generated_at": STAMP,
                    "manual_review_notes": item.get("notes", []),
                }
            )
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates,
        }
        (OUT_DIR / f"q{start:03d}-q{end:03d}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    missing = sorted(set(range(1, 101)) - set(DATA))
    if missing:
        raise SystemExit(f"missing DATA entries: {missing}")
    main()
