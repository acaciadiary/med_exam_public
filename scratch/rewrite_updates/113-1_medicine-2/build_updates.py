import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


SOURCE_FILE = "public/data/exams/113-1/medicine-2.json"
DATASET_ID = "113-1_medicine-2"
MODEL = "codex-high-quality-rewrite"


FACTS = {
    1: {
        "analysis": "牧場工人接觸動物或畜產品後，皮膚丘疹快速進展成無痛潰瘍與黑色壞死焦痂（necrotic eschar），並有水腫與淋巴結病變，是皮膚炭疽的典型線索。",
        "options": {
            "A": "枯草桿菌多為環境菌，偶見機會性感染，不會典型造成黑色焦痂與畜牧相關皮膚炭疽。",
            "B": "破傷風梭菌重點是破傷風毒素造成痙攣性麻痺，臨床不是壞死焦痂皮膚病灶。",
            "C": "肉毒桿菌造成肉毒毒素中毒，以顱神經症狀與下行性鬆弛性麻痺為主，不是本題皮膚潰瘍。",
            "D": "炭疽桿菌可形成孢子，常與動物皮毛或畜牧暴露有關；皮膚型炭疽會由丘疹、水疱進展成黑色壞死焦痂，符合題幹。",
        },
        "core": "牧場或動物製品暴露加上無痛黑色焦痂，要優先想到皮膚炭疽（Bacillus anthracis）。",
        "front": "牧場工人 + necrotic eschar",
        "back": "皮膚炭疽最典型病原是 Bacillus anthracis。",
    },
    2: {
        "analysis": "題目問傷寒沙門氏菌無症狀帶原最常藏在哪裡。Salmonella Typhi 可在膽囊長期存活，特別是膽結石或膽道生物膜環境，因此形成慢性帶原。",
        "options": {
            "A": "肝臟可在急性感染時受影響，但不是慢性無症狀帶原最典型的藏匿部位。",
            "B": "膽囊是 Typhoid Mary 這類慢性帶原者最典型的位置，細菌可在膽汁與膽結石表面生物膜中持續存在。",
            "C": "胰臟不是 Salmonella Typhi 慢性帶原的經典器官。",
            "D": "大腸可排出病菌造成傳播，但長期帶原的關鍵 reservoir 通常是膽囊而非大腸本身。",
        },
        "core": "傷寒帶原的高頻考點是 Salmonella Typhi 長期潛伏於膽囊，並經糞口途徑持續散播。",
        "front": "Typhoid Mary / Salmonella Typhi chronic carrier",
        "back": "最常藏匿於膽囊，尤其與膽結石、生物膜有關。",
    },
    3: {
        "analysis": "漢堡或生菜後出血性腹瀉，再併發溶血性尿毒症候群（HUS），典型指向產志賀毒素大腸桿菌，常見血清型為 O157:H7。",
        "options": {
            "A": "EIEC 以侵襲腸黏膜造成痢疾樣腹瀉為主，但不是 HUS 的典型病因。",
            "B": "EAEC 常造成持續性或旅行者腹瀉，與兒童慢性腹瀉較相關，不是出血性腸炎合併 HUS 的首選。",
            "C": "EPEC 常造成嬰幼兒水瀉，機轉是 attaching and effacing lesion，通常不產生志賀毒素造成 HUS。",
            "D": "STEC/EHEC 產生 Shiga toxin，會傷害腸道與腎臟內皮，引起出血性腹瀉與 HUS，正好串起本題的食物暴露、血便與腎臟併發症。",
        },
        "core": "生牛肉或生菜暴露後出血性腹瀉加 HUS，病原先想 STEC/EHEC。",
        "front": "出血性腹瀉 + HUS",
        "back": "Shiga toxin-producing E. coli（STEC/EHEC），典型 O157:H7。",
    },
    4: {
        "analysis": "β-內醯胺酶抑制劑本身抗菌力有限，主要價值是保護 β-內醯胺抗生素不被分解，與 penicillin 類合併時恢復或增強療效。",
        "options": {
            "A": "clavulanate、sulbactam、tazobactam 等本身通常沒有高度殺菌活性，不能單獨當主要抗生素。",
            "B": "它們不是以窄效型細胞壁抑制抗生素的角色使用，而是酵素抑制輔助藥。",
            "C": "與青黴素類或其他 β-內醯胺合併，可抑制細菌 β-內醯胺酶，保護主藥並產生協同效果。",
            "D": "MRSA 的關鍵是 PBP2a 改變，不是單純 β-內醯胺酶；β-內醯胺酶抑制劑不能解決典型 MRSA 抗藥性。",
        },
        "core": "β-內醯胺酶抑制劑的考點是「保護 β-內醯胺主藥」，不是自己強力殺菌，也不是治療 MRSA 的答案。",
        "front": "β-lactamase inhibitor 作用",
        "back": "與 β-lactam 合併，抑制 β-lactamase，保護主藥。",
    },
    5: {
        "analysis": "脂多醣體（LPS）是革蘭氏陰性菌外膜成分，毒性主要來自 lipid A，可活化先天免疫引發發炎反應、發燒與休克。",
        "options": {
            "A": "脂胞壁酸是革蘭氏陽性菌細胞壁成分，不是革蘭氏陰性菌特有結構。",
            "B": "LPS 又稱內毒素沒錯，但毒性主要來自 lipid A，不是核心多醣體。",
            "C": "LPS 可透過 TLR4 等路徑刺激巨噬細胞與發炎細胞激素，是最適當的敘述。",
            "D": "LPS 相對耐熱，煮沸不一定能有效去除其內毒素活性。",
        },
        "core": "LPS 屬革蘭氏陰性菌外膜內毒素，lipid A 是毒性核心，會強烈誘發發炎反應。",
        "front": "LPS / endotoxin",
        "back": "Gram-negative outer membrane；lipid A 造成毒性並誘發發炎。",
    },
    6: {
        "analysis": "題目考基本細菌構造。細菌沒有粒線體，革蘭氏陽性與陰性菌都有 peptidoglycan；部分細菌可有鞭毛以利運動。",
        "options": {
            "A": "壁膜間隙在革蘭氏陰性菌較明顯，不能說僅革蘭氏陽性菌具有。",
            "B": "peptidoglycan 是細菌細胞壁共同重要成分，革蘭氏陽性菌尤其厚，不是陰性菌才有。",
            "C": "細菌是原核生物，沒有粒線體；ATP 主要由細胞膜相關電子傳遞等機制產生。",
            "D": "部分細菌具有鞭毛，負責運動性，是正確的細菌構造描述。",
        },
        "core": "細菌為原核生物，沒有粒線體；peptidoglycan 非陰性菌專屬，鞭毛只存在於部分菌種。",
        "front": "細菌構造基本辨識",
        "back": "部分細菌有鞭毛；細菌沒有粒線體。",
    },
    7: {
        "analysis": "Haemophilus influenzae 需要 X factor（hemin）與 V factor（NAD）才能生長；巧克力瓊脂經加熱溶血，可釋放這些因子。",
        "options": {
            "A": "甘露醇鹽瓊脂主要用於篩選耐鹽的 Staphylococcus，特別是 S. aureus，不適合 H. influenzae。",
            "B": "巧克力瓊脂可提供 X 與 V factors，是培養 H. influenzae 的經典培養基。",
            "C": "MacConkey agar 用於革蘭氏陰性腸道菌分離與乳糖發酵判讀，不是嗜血桿菌的標準選擇。",
            "D": "一般血液培養基未充分釋放 V factor，H. influenzae 生長不如巧克力瓊脂理想。",
        },
        "core": "H. influenzae 需要 X 與 V factor，培養基選巧克力瓊脂。",
        "front": "Haemophilus influenzae 培養基",
        "back": "巧克力瓊脂，提供 hemin（X）與 NAD（V）。",
    },
    8: {
        "analysis": "Clostridium perfringens 依毒素分型。C 型產生 beta toxin，與壞疽性腸炎、腸壞死（pig-bel）關係最典型。",
        "options": {
            "A": "A 型最常見，常與氣壞疽和食物中毒相關，但不是壞疽性腸炎最典型分型。",
            "B": "B 型可造成動物腸毒血症，並非本題人類壞疽性腸炎高頻答案。",
            "C": "C 型的 beta toxin 可造成腸黏膜壞死，是 necrotizing enteritis 的典型分型。",
            "D": "D 型以 epsilon toxin 與動物疾病較相關，不是本題所問的壞疽性腸炎。",
        },
        "core": "產氣莢膜桿菌 C 型與 beta toxin、壞疽性腸炎最相關。",
        "front": "C. perfringens necrotizing enteritis",
        "back": "Type C，beta toxin。",
    },
    9: {
        "analysis": "題目問主要不是作用於細菌細胞壁的抗生素。linezolid 是 oxazolidinone，抑制 50S ribosome 起始複合體形成，屬蛋白質合成抑制劑。",
        "options": {
            "A": "isoniazid 抑制分枝桿菌 mycolic acid 合成，屬細胞壁相關作用。",
            "B": "ethambutol 抑制 arabinosyl transferase，影響分枝桿菌細胞壁 arabinogalactan。",
            "C": "linezolid 作用於 50S ribosomal subunit，抑制蛋白質合成，不是細胞壁作用藥。",
            "D": "vancomycin 結合 D-Ala-D-Ala，抑制 peptidoglycan 合成，明確作用於細胞壁。",
        },
        "core": "linezolid 是 50S 蛋白質合成抑制劑；INH、ethambutol、vancomycin 都與細胞壁合成相關。",
        "front": "非細胞壁作用抗生素",
        "back": "linezolid 抑制 50S ribosome，不是細胞壁合成。",
    },
    10: {
        "analysis": "本題是問 prion 敘述何者最不適當。prion 是錯誤摺疊蛋白造成傳染性海綿狀腦病變，對一般消毒與滅菌方式抗性高，但不代表只能在腦部測到。",
        "options": {
            "A": "prion 疾病主要病變在中樞神經，但異常 prion 可在淋巴網狀組織等部位出現；說只能在腦部測到過於絕對。",
            "B": "prion 對許多一般抗病毒化學與物理處理有抗性，這是經典特性。",
            "C": "腦內海綿狀變化是 prion disease 的代表性病理。",
            "D": "prion 不含核酸，主要以錯誤摺疊蛋白形式傳播感染性，敘述正確。",
        },
        "core": "prion 是具感染性的錯誤摺疊蛋白，可造成海綿狀腦病變，且對一般去活化方法抗性高；「只能在腦部測到」太絕對。",
        "front": "prion 最不適當敘述",
        "back": "不能說只能在腦部測到；本質是感染性錯誤摺疊蛋白。",
    },
    11: {
        "analysis": "Parvovirus B19 會感染紅血球前驅細胞，抑制紅血球生成；可造成第五病、再生不良危象與胎兒水腫。",
        "options": {
            "A": "parvovirus B19 是單股 DNA 病毒，不是雙股 DNA。",
            "B": "主要經呼吸道飛沫、血液或垂直傳播，不是典型糞口傳染。",
            "C": "病毒利用 P antigen 感染 erythroid precursor，造成細胞溶解與紅血球生成暫停，敘述正確。",
            "D": "兒童感染常為傳染性紅斑（fifth disease），嬰兒玫瑰疹主要是 HHV-6/7。",
        },
        "core": "Parvovirus B19 是單股 DNA 病毒，親紅血球前驅細胞，考點是 aplastic crisis 與 fifth disease。",
        "front": "Parvovirus B19 target cell",
        "back": "感染 erythroid precursor，抑制紅血球生成。",
    },
    12: {
        "analysis": "RT-QuIC 利用異常 PrPSc 作為 seed，誘導正常重組 PrP 轉成聚集纖絲，藉由即時螢光訊號偵測是否有 PrPSc。",
        "options": {
            "A": "正常 PrPC 不會自發成為檢測所依賴的病理性纖絲種子。",
            "B": "PrPSc 具有誘導錯誤摺疊與聚集成纖絲的 seeded conversion 特性，正是 RT-QuIC 的核心。",
            "C": "方向相反；PrPSc 會促使 PrPC 轉成異常構型，不是把 PrPSc 轉回 PrPC。",
            "D": "PrPSc 通常較抗蛋白酶分解、較穩定，不是因為半衰期較短而被偵測。",
        },
        "core": "RT-QuIC 考的是 PrPSc 的 seeded aggregation：異常 prion 可誘導正常 PrP 形成纖絲。",
        "front": "RT-QuIC 原理",
        "back": "利用 PrPSc seed 促進 PrP 聚集成 amyloid-like fibril。",
    },
    13: {
        "analysis": "大多數人類 DNA 病毒在細胞核複製；poxvirus 是重要例外，因具有完整複製與轉錄所需酵素，可在細胞質內複製。",
        "options": {
            "A": "poxvirus 在細胞質複製，是與多數 DNA 病毒最重要的差異。",
            "B": "線型雙股 DNA 不是 poxvirus 獨有，並非與多數 DNA 病毒最主要差異。",
            "C": "poxvirus 有自己的 DNA polymerase，但此特徵服務於細胞質複製；題目問主要差異時以細胞質複製最關鍵。",
            "D": "strand displacement 是某些病毒複製策略，不是 poxvirus 相對其他人類 DNA 病毒的典型主差異。",
        },
        "core": "poxvirus 是 DNA 病毒中少數在細胞質複製的高頻例外。",
        "front": "poxvirus 與其他 DNA virus 差異",
        "back": "poxvirus 在細胞質複製。",
    },
    14: {
        "analysis": "題目問抗病毒治療何者最不適當。indinavir 是 HIV protease inhibitor，不是 HSV 治療藥；HSV 常用 acyclovir、valacyclovir 等。",
        "options": {
            "A": "indinavir 用於 HIV 治療，機轉為抑制 HIV protease；拿來治療單純疱疹病毒感染不適當。",
            "B": "ribavirin 合併 interferon 曾是 C 型肝炎治療選項，雖現代已多由 DAA 取代，但作為考題敘述可接受。",
            "C": "狂犬病暴露後須做傷口處理並給予疫苗，未接種者也需狂犬病免疫球蛋白，敘述方向正確。",
            "D": "amantadine 可抑制 influenza A 的 M2 channel；臨床因抗藥性已少用，但藥理敘述正確。",
        },
        "core": "indinavir 是 HIV protease inhibitor；HSV 治療關鍵是 acyclovir 類核苷類似物。",
        "front": "indinavir 適應症",
        "back": "HIV protease inhibitor，不是 HSV 治療藥。",
    },
    15: {
        "analysis": "一歲托育中心幼兒出現水瀉、嘔吐、輕微發燒與脫水，是輪狀病毒腸胃炎的典型臨床情境。",
        "options": {
            "A": "輪狀病毒常造成嬰幼兒嚴重水瀉與嘔吐，托育環境易傳播，能解釋本題的年齡、群聚環境與脫水住院。",
            "B": "流感病毒主要造成呼吸道症狀、發燒與肌肉痠痛，非以水瀉脫水為主要表現。",
            "C": "B 型肝炎病毒主要造成肝炎與慢性感染，不是急性托育中心水瀉嘔吐的典型原因。",
            "D": "EB 病毒典型為傳染性單核球增多症等，不是嬰幼兒急性水瀉脫水首選。",
        },
        "core": "幼兒托育中心急性水瀉、嘔吐、脫水，先想 rotavirus。",
        "front": "嬰幼兒水瀉脫水",
        "back": "輪狀病毒（rotavirus）是典型原因。",
    },
    16: {
        "analysis": "Emergomyces 是溫度雙型性真菌，常經吸入感染，免疫低下尤其 HIV 患者可出現播散性疾病與皮膚病灶。",
        "options": {
            "A": "25°C 黴菌型、37°C 酵母型是溫度雙型性真菌的典型敘述。",
            "B": "吸入孢子後可播散，皮膚病灶常見，敘述正確。",
            "C": "Emergomyces 感染多見於免疫不全者，特別是 HIV/AIDS；說多數感染者健康不適當。",
            "D": "嚴重感染可使用 amphotericin B 後接 triazole 治療，敘述合理。",
        },
        "core": "Emergomyces 是機會性、溫度雙型性真菌，常見於免疫低下並可有皮膚病灶。",
        "front": "Emergomyces 高風險族群",
        "back": "多見於免疫不全者，不是多數健康人感染。",
    },
    17: {
        "analysis": "Echinocandin 抑制真菌 β-1,3-D-glucan cell wall synthesis，對 Candida 殺菌，對 Aspergillus 有活性；對 Cryptococcus、Mucorales 與 Fusarium 效果差。",
        "options": {
            "A": "毛黴菌對 echinocandin 效果差，治療常需 amphotericin B、手術與控制危險因子。",
            "B": "隱球菌細胞壁特性使 echinocandin 效果不佳，治療以 amphotericin B、flucytosine、fluconazole 等為主。",
            "C": "Fusarium 對 echinocandin 通常不理想，臨床多考慮 voriconazole 或 amphotericin B。",
            "D": "麴菌對 echinocandin 有治療活性，雖常非單一首選，但在選項中最符合。",
        },
        "core": "Echinocandin 對 Candida 與 Aspergillus 有用；對 Cryptococcus、Mucorales、Fusarium 較差。",
        "front": "Echinocandin 抗黴菌範圍",
        "back": "抑制 β-1,3-D-glucan；選項中 Aspergillus 最適合。",
    },
    18: {
        "analysis": "造血位置隨發育時期轉移：早期 yolk sac，胎兒期 fetal liver，出生前後骨髓成為主要造血處；fetal heart 不是典型造血器官。",
        "options": {
            "A": "yolk sac 是胚胎早期造血位置之一，不是最不可能。",
            "B": "fetal liver 是胎兒期重要造血器官。",
            "C": "fetal heart 不是造血作用的典型場所，因此最不可能。",
            "D": "bone marrow 是出生後主要造血處。",
        },
        "core": "造血發育順序可記 yolk sac -> fetal liver -> bone marrow；心臟不是造血器官。",
        "front": "胚胎與出生後造血位置",
        "back": "yolk sac、fetal liver、bone marrow；不是 fetal heart。",
    },
    19: {
        "analysis": "第一型干擾素（IFN-α/β）由病毒感染細胞誘發，建立抗病毒狀態並增加 MHC I 表現，但不是自己直接分解病毒。",
        "options": {
            "A": "病毒感染有核細胞可誘導 type I interferon，敘述正確。",
            "B": "type I interferon 是訊號分子，誘導宿主細胞抗病毒基因表現，不是直接把病毒分解。",
            "C": "它可誘導 RNase、PKR 等抗病毒路徑，破壞病毒 mRNA 或抑制蛋白轉譯。",
            "D": "增加 MHC I 表現可幫助 CD8 T 細胞辨識感染細胞，敘述正確。",
        },
        "core": "IFN-α/β 不是直接殺病毒，而是讓細胞進入抗病毒狀態並強化 MHC I 呈現。",
        "front": "type I interferon 作用",
        "back": "誘導抗病毒基因與 MHC I，不直接分解病毒。",
    },
    20: {
        "analysis": "clonal expansion 指成熟淋巴細胞遇到特異性抗原後在周邊淋巴組織大量增殖，不是在胸腺或骨髓發育階段發生。",
        "options": {
            "A": "TCR αβ 與 γδ 分別形成兩大類 T 細胞受體，敘述正確。",
            "B": "抗原受體與抗原間的非共價作用包括氫鍵、凡德瓦力等，敘述正確。",
            "C": "把 clonal expansion 說成胸腺或骨髓發育過程中的外來抗原刺激是錯的；它發生在成熟淋巴細胞遇抗原後。",
            "D": "MHC restriction 表示 TCR 辨識抗原胜肽時需搭配自身 MHC，敘述正確。",
        },
        "core": "clonal expansion 是成熟淋巴球在周邊遇到抗原後增殖，不是中樞淋巴器官發育過程。",
        "front": "clonal expansion 定義",
        "back": "成熟淋巴細胞遇特異性抗原後大量增殖。",
    },
    21: {
        "analysis": "B 細胞、樹突細胞與巨噬細胞都是 professional antigen-presenting cells，會表現 MHC II；活化後也可表現 B7 共刺激分子。",
        "options": {
            "A": "三者皆屬專業抗原呈獻細胞，能表現 MHC class II 與 B7，最適當。",
            "B": "有核細胞普遍表現 MHC I，不能說三者不表現 MHC I。",
            "C": "最能活化 naïve T cell 的通常是樹突細胞，不是 B 細胞。",
            "D": "樹突細胞具有未成熟巡邏到成熟遷移的典型過程，但 B 細胞與巨噬細胞不能一概套用同一句描述。",
        },
        "core": "專業 APC 包括 dendritic cell、macrophage、B cell；其中 dendritic cell 最擅長活化 naïve T cell。",
        "front": "professional APC",
        "back": "B cell、dendritic cell、macrophage 表現 MHC II 與共刺激分子。",
    },
    22: {
        "analysis": "B 細胞初次活化後最早分泌 IgM；IgG 可穿胎盤、IgE 活化肥大細胞、IgM 與 IgG 可活化補體。",
        "options": {
            "A": "可穿過胎盤的是 IgG，不是 IgA；IgA 主要見於黏膜分泌與母乳。",
            "B": "補體活化最典型是 IgM，其次 IgG；IgE 主要與過敏與寄生蟲反應相關。",
            "C": "IgM 是 naïve B 細胞活化後最早分泌的抗體，敘述正確。",
            "D": "活化 mast cells 主要是 IgE 經 FcεRI 結合後交聯，不是 IgG。",
        },
        "core": "抗體功能速記：IgM 最早且強補體；IgG 過胎盤；IgA 黏膜；IgE 肥大細胞與寄生蟲。",
        "front": "最早分泌抗體",
        "back": "B 細胞活化後最早分泌 IgM。",
    },
    23: {
        "analysis": "腸道上皮細胞可用 TLR、NOD1/2 偵測病原相關分子，也可透過 stress ligand 如 MIC-A/B 讓免疫細胞辨識異常細胞；PGE2 不是主要用來清除病原菌的辨識分子。",
        "options": {
            "A": "TLRs 可辨識微生物成分並啟動先天免疫，可能參與清除病原。",
            "B": "NOD1、NOD2 可感測細菌 peptidoglycan 片段，是腸道先天免疫重要分子。",
            "C": "PGE2 是發炎介質，主要調節血管、疼痛、發燒等反應，不是腸道上皮用來辨識並清除病原菌的典型分子。",
            "D": "MIC-A/B 是壓力誘導配體，可被 NKG2D 辨識，幫助免疫系統處理受感染或壓力細胞。",
        },
        "core": "腸道上皮清除病原重點是 PRR（TLR、NOD）與壓力配體；PGE2 是發炎調節介質。",
        "front": "腸道上皮抗病原分子",
        "back": "TLR、NOD1/2、MIC-A/B 可參與；PGE2 不是主要清除分子。",
    },
    24: {
        "analysis": "Wiskott-Aldrich syndrome 的缺陷基因是 WAS，影響 actin cytoskeleton；NF-κB 不是此病的標準配對。",
        "options": {
            "A": "X-linked SCID 常因 IL-2 receptor common gamma chain 缺陷，配對正確。",
            "B": "Wiskott-Aldrich syndrome 應配 WAS gene，不是 NF-κB，因此最不適當。",
            "C": "Bruton X-linked agammaglobulinemia 是 BTK 缺陷，配對正確。",
            "D": "DiGeorge syndrome 與 22q11.2 deletion、TBX1 相關，配對可接受。",
        },
        "core": "Wiskott-Aldrich = WAS gene；BTK = XLA；common gamma chain = X-linked SCID；TBX1 = DiGeorge。",
        "front": "Wiskott-Aldrich syndrome 基因",
        "back": "WAS gene，不是 NF-κB。",
    },
    25: {
        "analysis": "第一型過敏反應是 IgE 介導的立即型過敏，常見疾病包括過敏性鼻炎、結膜炎、氣喘與蕁麻疹。",
        "options": {
            "A": "麩質病主要與 T cell 免疫反應和 HLA-DQ2/DQ8 相關，不是 IgE 介導第一型過敏。",
            "B": "血清病是免疫複合體沉積造成的第三型過敏反應。",
            "C": "過敏性鼻結膜炎由 IgE 與 mast cell 介導，屬第一型過敏反應。",
            "D": "過敏性接觸性皮膚炎是 T cell 介導的第四型遲發型過敏反應。",
        },
        "core": "第一型過敏 = IgE + mast cell；過敏性鼻炎/結膜炎是典型例子。",
        "front": "IgE 介導第一型過敏",
        "back": "過敏性鼻結膜炎、過敏性氣喘、蕁麻疹等。",
    },
    26: {
        "analysis": "IL-10 是重要抗發炎 cytokine，能抑制 macrophage 與 Th1 發炎反應；缺乏 IL-10 容易造成腸道慢性發炎，模型上常見 colitis/IBD。",
        "options": {
            "A": "IL-10 knockout mice 典型會自發性腸炎，類似 inflammatory bowel disease，最符合。",
            "B": "lupus-like syndrome 與免疫複合體、自體抗體相關，但不是 IL-10 knockout 的典型首選。",
            "C": "淋巴增生性疾病常見於調控細胞死亡或免疫調節缺陷，不是本題 IL-10 缺失的經典表現。",
            "D": "類風濕性關節炎涉及多種 cytokine 與自體免疫機制，但 IL-10 knockout 最典型仍是腸炎。",
        },
        "core": "IL-10 是抗發炎煞車；缺乏時最典型造成腸道發炎/IBD 樣疾病。",
        "front": "IL-10 knockout mouse",
        "back": "容易發生 inflammatory bowel disease-like colitis。",
    },
    27: {
        "analysis": "題目問腫瘤抗原何者最不適當。TAA 可在正常組織低量表現、腫瘤高表現；TSA 多來自突變或病毒。鑑定 TAA 通常靠表現量與蛋白體/轉錄體比較，不能說單細胞轉錄體定序是目前最常用方法。",
        "options": {
            "A": "TAA 在正常與腫瘤都可能表現，但腫瘤量較高或位置不同，敘述正確。",
            "B": "TSA 可來自突變 neoantigen、病毒蛋白等，WES 常用於找突變來源的 neoantigen，敘述合理。",
            "C": "現行 CAR-T 多針對表面 TAA，例如 CD19、BCMA 等；少數 TSA 理論上也可成為目標，敘述可接受。",
            "D": "TAA 的鑑定不以單細胞轉錄體定序作為最常用標準方法；此說法過度絕對，最不適當。",
        },
        "core": "TAA 是腫瘤高表現的共享抗原；TSA 是突變/病毒等腫瘤特異抗原，TAA 不以單細胞轉錄體定序作為最常用鑑定法。",
        "front": "TAA vs TSA",
        "back": "TAA 正常也可能有；TSA 多來自突變或病毒。",
    },
    28: {
        "analysis": "題目問可用疫苗預防的腫瘤。HPV 疫苗可預防高風險 HPV 型別感染，進而降低 HPV-16 相關子宮頸癌風險。",
        "options": {
            "A": "non-Hodgkin lymphoma 沒有以常規疫苗直接預防的標準做法。",
            "B": "HER2 過度表現乳癌目前不是以常規預防疫苗避免發生的腫瘤。",
            "C": "轉移性黑色素瘤已有免疫治療概念，但不是可注射疫苗預防的典型腫瘤。",
            "D": "HPV 疫苗可預防 HPV-16/18 等感染，因此可預防相關子宮頸癌。",
        },
        "core": "能用疫苗預防的典型癌症：HPV 相關子宮頸癌、HBV 相關肝癌。",
        "front": "疫苗可預防癌症",
        "back": "HPV vaccine 預防 HPV-16 related cervical cancer。",
    },
    29: {
        "analysis": "題目考寄生蟲臨床表現組合。犬蛔蟲可造成眼部幼蟲移行，班氏絲蟲慢性感染可造成象皮病，蛔蟲可異位寄生；鞭蟲感染免疫低下並非必然死亡。",
        "options": {
            "A": "包含犬蛔蟲正確，但把鞭蟲必致死納入，所以不對。",
            "B": "班氏絲蟲與蛔蟲兩項正確，但漏掉犬蛔蟲眼部幼蟲移行症。",
            "C": "犬蛔蟲、班氏絲蟲、蛔蟲三項皆正確，且排除鞭蟲必致死的錯誤敘述。",
            "D": "四項全選會包含鞭蟲感染必造成死亡，過度絕對且錯誤。",
        },
        "core": "Toxocara 可 ocular larva migrans；Wuchereria 可 elephantiasis；Ascaris 可 ectopic parasitism；Trichuris 不等於免疫低下必死。",
        "front": "寄生蟲症狀配對",
        "back": "犬蛔蟲眼幼蟲移行、班氏絲蟲象皮病、蛔蟲異位寄生。",
    },
    30: {
        "analysis": "十二指腸鉤蟲幼蟲經皮膚進入後，會經血流到肺、穿入肺泡、上行至咽部被吞下，最後到小腸發育成成蟲。",
        "options": {
            "A": "犬蛔蟲在人類多為幼蟲移行症，人不是其正常成蟲宿主，不是到小腸發育成蟲的答案。",
            "B": "海獸胃線蟲由食入生魚感染，幼蟲侵入胃腸壁，不需心肺移行後到小腸成蟲。",
            "C": "十二指腸鉤蟲有典型皮膚侵入、心肺移行、吞入後小腸成蟲的生活史。",
            "D": "有棘頜口線蟲可造成移行性病灶，但在人類不是經心肺移行後到小腸成蟲的典型路徑。",
        },
        "core": "鉤蟲與蛔蟲常考肺部移行；本題選項中能到小腸發育成成蟲的是十二指腸鉤蟲。",
        "front": "心肺移行後小腸成蟲",
        "back": "Ancylostoma duodenale 鉤蟲。",
    },
    31: {
        "analysis": "血吸蟲成蟲寄生位置與產卵量是常考點。S. mansoni/japonicum 主要在腸繫膜靜脈系統，S. haematobium 在膀胱靜脈叢；S. japonicum 產卵量最高。",
        "options": {
            "A": "S. mansoni 主要在腸繫膜靜脈，膀胱靜脈叢是 S. haematobium 的重點。",
            "B": "S. haematobium 主要在膀胱靜脈叢，不是腸繫膜靜脈叢。",
            "C": "血吸蟲卵造成肉芽腫常在腸壁、肝臟或泌尿道等部位；題目說經血流異位陷入腎臟不是最適當概括。",
            "D": "S. japonicum 產卵量高，日產卵可非常多，是最適當敘述。",
        },
        "core": "S. haematobium 膀胱；S. mansoni/japonicum 腸繫膜；S. japonicum 產卵最多。",
        "front": "血吸蟲位置與產卵量",
        "back": "S. japonicum 產卵量最高；S. haematobium 在膀胱靜脈叢。",
    },
    32: {
        "analysis": "官方答案選水生植物相關的是 Fasciola hepatica 與 Fasciolopsis buski。兩者感染型囊蚴可附著在水生植物上，食入後感染；Clonorchis 以淡水魚為第二中間宿主，Dicrocoelium 與螞蟻相關。",
        "options": {
            "A": "牛羊肝吸蟲與薑片蟲都可由水生植物上的囊蚴感染，符合官方答案組合。",
            "B": "中華肝吸蟲主要與淡水魚有關，槍狀肝吸蟲則與螞蟻等陸生生活史相關，不是水生植物組合。",
            "C": "包含牛羊肝吸蟲正確，但中華肝吸蟲重點是淡水魚，不是水生植物。",
            "D": "包含薑片蟲正確，但槍狀肝吸蟲不是水生植物相關。",
        },
        "core": "水生植物感染線索：Fasciola hepatica、Fasciolopsis buski；Clonorchis 要想淡水魚，Dicrocoelium 要想螞蟻。",
        "front": "水生植物相關吸蟲",
        "back": "Fasciola hepatica 與 Fasciolopsis buski。",
        "notes": ["題幹稱水生植物為中間宿主較不精確；嚴格寄生蟲學上水生植物多是囊蚴附著的感染媒介，仍依官方答案解釋。"],
    },
    33: {
        "analysis": "發燒、腹脹、貧血、肝脾腫大，骨髓巨噬細胞內看到寄生蟲，是內臟利什曼病（kala-azar）的典型線索，病原為 Leishmania donovani。",
        "options": {
            "A": "Trypanosoma cruzi 造成 Chagas disease，常見心肌病或巨食道/巨結腸，不是巨噬細胞內 amastigote 的內臟利什曼病。",
            "B": "Leishmania tropica 主要造成皮膚利什曼病，不是肝脾腫大、骨髓巨噬細胞感染的典型答案。",
            "C": "T. brucei gambiense 造成非洲睡眠病，病媒為采采蠅，臨床不是本題骨髓巨噬細胞內寄生蟲。",
            "D": "Leishmania donovani 感染巨噬細胞，造成內臟利什曼病、發燒、貧血與肝脾腫大，最符合。",
        },
        "core": "骨髓巨噬細胞內寄生蟲加肝脾腫大，考 Leishmania donovani 的內臟利什曼病。",
        "front": "kala-azar 病原",
        "back": "Leishmania donovani，巨噬細胞內 amastigote。",
    },
    34: {
        "analysis": "Plasmodium knowlesi 是猴瘧，可感染人類，紅血球年齡選擇性較不嚴格，24 小時裂殖週期；形成 hypnozoite 是 P. vivax/ovale 的特色。",
        "options": {
            "A": "P. knowlesi 可感染人類與非人靈長類，宿主專一性不強，敘述正確。",
            "B": "它可侵犯不同年齡紅血球，不像 vivax 偏年輕、malariae 偏老紅血球，敘述正確。",
            "C": "P. knowlesi  erythrocytic schizogony 約 24 小時，可能每日發燒，敘述正確。",
            "D": "hypnozoites 是 P. vivax 與 P. ovale 的肝內休眠型，P. knowlesi 不形成，故此項錯誤。",
        },
        "core": "P. knowlesi：猴瘧、人畜共通、24 小時週期；沒有 hypnozoite。",
        "front": "Plasmodium knowlesi 錯誤敘述",
        "back": "不形成 hypnozoite；hypnozoite 屬 vivax/ovale。",
    },
    35: {
        "analysis": "病媒在傷口或皮膚產卵，幼蟲孵化後寄生組織，是蠅蛆症（myiasis）的典型表現；選項中以綠蠅最符合。",
        "options": {
            "A": "白蛉傳播 Leishmania，但不是最常在傷口產卵孵化成幼蟲寄生的病媒。",
            "B": "跳蚤可傳播鼠疫、斑疹傷寒等，某些可造成皮膚病灶，但不是本題蠅蛆症典型答案。",
            "C": "蝨可傳播流行性斑疹傷寒等，並非在傷口產卵造成組織蛆症的主角。",
            "D": "綠蠅等蠅類可在傷口產卵，幼蟲侵入或寄生組織造成 myiasis，最符合。",
        },
        "core": "傷口產卵、幼蟲寄生組織是蠅蛆症，病媒選蠅類。",
        "front": "傷口產卵幼蟲寄生",
        "back": "綠蠅造成 myiasis。",
    },
    36: {
        "analysis": "同一批病人服藥前後收縮壓比較是成對資料；單尾或雙尾會影響拒絕域與 p 值解讀，但不改變由資料算出的 test statistic。",
        "options": {
            "A": "200 筆看似兩組資料，其實來自 100 位病人前後測，前後值成對相關，不能視為互相獨立。",
            "B": "應用 paired t test 時自由度是配對差值數量減一，也就是 99，不是 198。",
            "C": "單尾或雙尾檢定改變臨界值與 p 值方向，但同一資料算出的 test statistic 不變，最恰當。",
            "D": "paired t test 主要假設配對差值近似常態，不必要求服藥前與服藥後原始血壓各自完全常態。",
        },
        "core": "前後測同一人是 paired data；paired t test 自由度 n-1，單/雙尾不改變 test statistic。",
        "front": "paired t test 前後測",
        "back": "同一人前後測為成對資料；df=n-1；test statistic 不因單/雙尾改變。",
    },
    37: {
        "analysis": "簡單線性迴歸以握力為依變項、年齡為自變項，模式為 y = intercept + slope × x；截距 26.8、斜率 -0.25。",
        "options": {
            "A": "截距不需除以樣本數 200；把 26.8/200 放進模式是錯誤理解。",
            "B": "題目指定握力是依變項，不能把年齡放成依變項。",
            "C": "握力 = 26.8 - 0.25 × 年齡，完全符合截距與斜率定義。",
            "D": "同樣把年齡錯放為依變項，且不符合題目指定模型。",
        },
        "core": "線性迴歸模式寫成 dependent variable = intercept + slope × independent variable。",
        "front": "簡單線性迴歸式",
        "back": "握力 = 26.8 - 0.25 × 年齡。",
    },
    38: {
        "analysis": "陰性預測值 80% 表示所有快篩陰性者中，真正沒有流感者佔 80%；因此陰性者中仍得到流感者為 1-80% = 20%。",
        "options": {
            "A": "40% 是把敏感度 60% 的漏診率誤當成陰性者中患病率，與題目給的 NPV 不同。",
            "B": "30% 是特異度 70% 的假陽性率概念，也不是陰性者中仍有病比例。",
            "C": "陰性預測值 80% 代表陰性者中 20% 實際仍有病，故此項正確。",
            "D": "題目已直接給陰性預測值，所以可以判斷陰性者中患病比例。",
        },
        "core": "NPV = 陰性者中真正無病比例；陰性者中仍有病 = 1 - NPV。",
        "front": "NPV 80%",
        "back": "陰性反應者中仍有病比例為 20%。",
    },
    39: {
        "analysis": "臨床試驗隨機分組的核心目的是讓已知與未知干擾因子在各組平均分布相近，降低 confounding。",
        "options": {
            "A": "測量誤差主要靠標準化量測、校正工具與盲法降低，不是隨機分組的主要目的。",
            "B": "隨機分組可使 confounders 在組間分布趨於平衡，是最重要目的。",
            "C": "測量準確度取決於量測工具與程序，隨機分組不直接提高準確度。",
            "D": "再現性與研究設計、樣本與方法透明度有關，非隨機分組的直接主要功能。",
        },
        "core": "Randomization 的考點是平衡干擾因子、降低 confounding。",
        "front": "臨床試驗隨機分組目的",
        "back": "讓干擾因子在兩組分布相似。",
    },
    40: {
        "analysis": "全球環境變遷可造成暖化、病媒分布改變、臭氧層破壞與海平面上升；畜牧業增加主要與甲烷、氧化亞氮等溫室氣體相關，不是二氧化硫濃度上升。",
        "options": {
            "A": "暖化可改變病媒蚊與動物宿主分布，增加傳染病風險，屬公共衛生衝擊。",
            "B": "臭氧層破壞使紫外線暴露增加，皮膚癌風險上升，屬公共衛生衝擊。",
            "C": "二氧化碳增加造成溫室效應與海平面上升，屬全球變遷重要影響。",
            "D": "牛隻畜養增加主要牽涉甲烷等溫室氣體，不是其排泄物造成二氧化硫濃度上升，因此不是恰當敘述。",
        },
        "core": "畜牧業與全球暖化常考甲烷，不是二氧化硫。",
        "front": "全球環境變遷錯誤敘述",
        "back": "畜牧業增加主要與甲烷相關，不是二氧化硫。",
    },
    41: {
        "analysis": "毒化物代謝常使物質更具極性，便於尿液或膽汁排泄；尿液排泄的代謝物多為較高極性，而非較低極性。",
        "options": {
            "A": "肝臟含豐富代謝酵素，是毒化物代謝最主要器官，敘述正確。",
            "B": "由尿液排泄的代謝物通常較水溶、較高極性；說較低極性最不恰當。",
            "C": "Phase II 主要是 conjugation，例如 glucuronidation、sulfation、acetylation 等，敘述正確。",
            "D": "代謝物可作為生物偵測與暴露評估指標，敘述正確。",
        },
        "core": "代謝通常增加極性與水溶性，利於尿液排泄；Phase II 是 conjugation。",
        "front": "毒化物代謝與尿液排泄",
        "back": "尿中代謝物多為較高極性，不是較低極性。",
    },
    42: {
        "analysis": "AQI 由各污染物副指標計算後，以最大值作為該測站 AQI，因為最大值代表當日健康風險最嚴重的污染物。",
        "options": {
            "A": "AQI 監測項目包括 O3、PM2.5、PM10、CO、SO2、NO2，敘述正確。",
            "B": "AQI 會將污染物濃度換算成健康影響相關的副指標值，敘述正確。",
            "C": "AQI 取各副指標最大值，不是最小值；此項最不恰當。",
            "D": "AQI 大於 100 表示對敏感族群或一般民眾健康不良風險增加，敘述正確。",
        },
        "core": "AQI 是各污染物副指標中的最大值，不是最小值。",
        "front": "AQI 計算",
        "back": "取各污染物副指標最大值作為 AQI。",
    },
    43: {
        "analysis": "作業環境測定標準用於評估與管理工作場所暴露，協助職業衛生控制；它不是職業病診斷標準本身。",
        "options": {
            "A": "8 小時日時量平均容許濃度是長期工作暴露可接受水準的概念，敘述大致正確。",
            "B": "短時間時量平均容許濃度通常指 15 分鐘內的平均暴露不得超過標準，敘述正確。",
            "C": "最高容許濃度是任何時間不得超過的上限，敘述正確。",
            "D": "作業環境測定標準是暴露評估與管理依據，不等於職業病診斷標準，因此最不恰當。",
        },
        "core": "容許濃度是職業暴露管理標準，不是直接的職業病診斷標準。",
        "front": "作業環境測定標準用途",
        "back": "用於暴露評估與管理，不是職業病診斷標準。",
    },
    44: {
        "analysis": "社會行銷 4P 為 product、price、place、promotion；politics 可屬政策或倡議環境，但不是基本 4P 之一。",
        "options": {
            "A": "promotion 是 4P 之一，指促銷或溝通推廣。",
            "B": "place 是 4P 之一，指通路或可近性。",
            "C": "politics 不是傳統社會行銷 4P 的核心項目，因此是答案。",
            "D": "price 是 4P 之一，指金錢與非金錢成本。",
        },
        "core": "社會行銷 4P：product、price、place、promotion。",
        "front": "社會行銷 4P",
        "back": "不包括 politics。",
    },
    45: {
        "analysis": "劉太太不想乳攝的主因是過去疼痛經驗造成她認為行動有障礙；健康信念模式中這屬於 perceived barriers，也可和 perceived benefits 一起權衡。",
        "options": {
            "A": "她距離近、有通知，但因疼痛經驗不願再做，最符合行動障礙與利益權衡。",
            "B": "易感受性是個人認為自己罹病風險高低；題幹沒有強調她覺得自己不會得乳癌。",
            "C": "衛生所通知是行動線索，但她已收到線索仍不去，真正阻力是疼痛障礙。",
            "D": "自我效能是相信自己能完成行動；題幹不是不會安排或無能力完成檢查。",
        },
        "core": "健康信念模式中，疼痛、費用、麻煩等阻礙屬 perceived barriers。",
        "front": "健康信念模式：疼痛不想篩檢",
        "back": "屬行動障礙與利益權衡。",
    },
    46: {
        "analysis": "渥太華憲章五大行動綱領包括制定健康公共政策、創造支持性環境、強化社區行動、發展個人技能、調整健康服務方向。",
        "options": {
            "A": "制定健康的公共政策是五大綱領之一。",
            "B": "強化社會行銷內涵不是渥太華憲章五大行動綱領之一。",
            "C": "發展個人技能是五大綱領之一。",
            "D": "創造支持性環境是五大綱領之一。",
        },
        "core": "Ottawa Charter 五大綱領不含社會行銷；要記健康政策、支持環境、社區行動、個人技能、健康服務再定位。",
        "front": "渥太華憲章五大行動綱領",
        "back": "不包括強化社會行銷內涵。",
    },
    47: {
        "analysis": "疾病管制署前身整併自防疫、檢疫、預防醫學研究與慢性病防治相關單位；選項中最符合的是防疫處、檢疫總所、預防醫學研究所、慢性病防治局。",
        "options": {
            "A": "疫情指揮中心不是當時合併改制的四個前身單位組合，故不適當。",
            "B": "熱帶醫學研究所不是此題標準組合中的單位。",
            "C": "防疫處、檢疫總所、預防醫學研究所、慢性病防治局符合疾病管制署改制前身的考點。",
            "D": "血清疫苗製造所不是此題所列標準合併組合。",
        },
        "core": "疾管署前身考點：防疫處、檢疫總所、預防醫學研究所、慢性病防治局。",
        "front": "疾病管制署前身",
        "back": "防疫處、檢疫總所、預防醫學研究所、慢性病防治局。",
    },
    48: {
        "analysis": "論量計酬依服務量付款，服務越多收入越高，容易誘發供給與醫療量增加，因此最不容易控制費用上漲。",
        "options": {
            "A": "總額預算設定整體支出上限，控制費用能力強。",
            "B": "論量計酬會鼓勵增加服務量，是控制費用最不利的支付制度。",
            "C": "論病例計酬以病例或診斷相關群組固定支付，較能限制單案費用。",
            "D": "論人計酬以人頭固定支付，醫療提供者有控制成本誘因。",
        },
        "core": "費用控制最差通常是 fee-for-service；總額、case payment、capitation 較有成本控制誘因。",
        "front": "最不易控制費用支付制度",
        "back": "論量計酬（fee for service）。",
    },
    49: {
        "analysis": "WHO 醫療照護體系績效三大目標常考健康、回應性與財務公平/風險保護；醫療提供者滿意度不是三大目標之一。",
        "options": {
            "A": "健康水準屬於醫療體系績效核心目標。",
            "B": "醫療提供者滿意度可作為管理指標，但不是 WHO 三大目標之一。",
            "C": "病人滿意、尊嚴與可近性可歸入 responsiveness，屬三大目標相關概念。",
            "D": "病人家庭財務負擔對應公平財務分擔/財務風險保護，是三大目標相關概念。",
        },
        "core": "WHO health system goals：health、responsiveness、fair financial contribution；不含 provider satisfaction。",
        "front": "WHO 醫療體系三大目標",
        "back": "不包括醫療提供者滿意度。",
    },
    50: {
        "analysis": "病人自主權利法允許依預立醫療決定處理特定臨床條件，如末期病人、不可逆昏迷、永久植物人、極重度失智等；不是所有程度失智症都適用。",
        "options": {
            "A": "癌症末期病人屬可適用預立醫療決定的條件之一。",
            "B": "不可逆轉昏迷屬可適用條件之一。",
            "C": "永久植物人狀態屬可適用條件之一。",
            "D": "法律並非涵蓋所有程度的失智症；通常限於極重度失智等特定情境，因此不得僅因任何程度失智就依預立決定撤除治療。",
        },
        "core": "預立醫療決定適用於法定特定臨床條件；失智症不是所有程度都適用。",
        "front": "病人自主權利法不適用條件",
        "back": "不是所有程度失智症都可依預立醫療決定撤除維生治療。",
    },
    51: {
        "analysis": "弱酸藥物用 Henderson-Hasselbalch：pH = pKa + log([A-]/[HA])。pH 4、pKa 6，log 比值 = -2，所以 [A-]:[HA] = 1:100。",
        "options": {
            "A": "1:10 代表 pH 比 pKa 低 1；本題 pH 比 pKa 低 2。",
            "B": "10:1 表示離子型較多，應發生在 pH 高於 pKa 的環境。",
            "C": "pH 比 pKa 低 2，弱酸多為非離子型，離子型與非離子型比例為 1:100。",
            "D": "100:1 是 pH 比 pKa 高 2 時的弱酸比例，方向相反。",
        },
        "core": "弱酸：pH-pKa = log(A-/HA)；pH 比 pKa 低 2 時 A-/HA = 1/100。",
        "front": "弱酸 pKa=6, pH=4",
        "back": "[A-]:[HA] = 1:100。",
    },
    52: {
        "analysis": "肺囊蟲肺炎（Pneumocystis jirovecii pneumonia, PCP）首選治療與預防藥物都是 trimethoprim-sulfamethoxazole。",
        "options": {
            "A": "TMP-SMX 是 PCP 首選治療組合，正確。",
            "B": "vancomycin-gentamicin 主要針對細菌感染組合，不是 PCP 首選。",
            "C": "penicillin V-streptomycin 不是肺囊蟲治療組合。",
            "D": "amoxicillin-clavulanate 用於部分細菌感染，不涵蓋 PCP 首選治療。",
        },
        "core": "PCP 的治療與預防首選均是 TMP-SMX。",
        "front": "肺囊蟲肺炎首選",
        "back": "trimethoprim-sulfamethoxazole。",
    },
    53: {
        "analysis": "vinca alkaloids 抑制微小管聚合。vincristine 的劑量限制毒性以周邊神經病變較典型；vinblastine 則骨髓抑制較明顯。",
        "options": {
            "A": "骨髓抑制較常是 vinblastine 明顯，非 vincristine 較突出副作用。",
            "B": "禿頭可見於多種化療，但不是 vincristine 相較 vinblastine 的主要差異。",
            "C": "心臟毒性不是 vinca alkaloids 的典型差異重點；anthracycline 才常考心毒性。",
            "D": "vincristine 較易造成周邊神經病變，是本題答案。",
        },
        "core": "vincristine = neurotoxicity；vinblastine = bone marrow suppression。",
        "front": "vincristine vs vinblastine",
        "back": "vincristine 較易周邊神經病變。",
    },
    54: {
        "analysis": "KRAS 突變的大腸直腸癌對抗 EGFR 單株抗體如 cetuximab 通常無效，因下游訊號已持續活化；因此與 FOLFOX 併用不會得到顯著療效。",
        "options": {
            "A": "KRAS 突變預測 cetuximab 效果差，此項說有顯著療效是錯誤。",
            "B": "sorafenib 曾是晚期或不可切除肝癌的代表性標靶藥物，考題脈絡下敘述可接受。",
            "C": "gemcitabine 可用於轉移性胰臟癌治療，敘述正確。",
            "D": "erlotinib、afatinib、osimertinib 都是 EGFR 突變 NSCLC 可用的 EGFR TKI，敘述正確。",
        },
        "core": "KRAS mutation 是 anti-EGFR therapy 在大腸直腸癌效果差的重要預測因子。",
        "front": "KRAS 突變與 cetuximab",
        "back": "KRAS 突變時 cetuximab 通常無效。",
    },
    55: {
        "analysis": "5-HT3 是 ligand-gated cation channel，與化學受器觸發區和嘔吐反射密切相關；5-HT2 是 Gq coupled，不是 chemoreceptor reflex 的主要受體。",
        "options": {
            "A": "5-HT1B/1D 為 Gi coupled，可降低 cAMP，敘述正確。",
            "B": "5-HT4 可促進腸道神經傳遞與蠕動，敘述正確。",
            "C": "chemoreceptor trigger zone 與嘔吐反射重點是 5-HT3；把它歸給 5-HT2 是錯誤。",
            "D": "5-HT3 是 ligand-gated Na+/K+ cation channel，敘述正確。",
        },
        "core": "嘔吐反射與 5-HT3 相關；5-HT2 是 Gq receptor。",
        "front": "serotonin receptor 錯誤敘述",
        "back": "chemoreceptor reflex 重點是 5-HT3，不是 5-HT2。",
    },
    56: {
        "analysis": "pertuzumab 是抗 HER2 單株抗體，阻斷 HER2 dimerization；不是抗 VEGFR。其他選項 PD-1/PD-L1/EGFR 對應正確。",
        "options": {
            "A": "avelumab 是 anti-PD-L1，可結合腫瘤細胞或免疫細胞上的 PD-L1，敘述正確。",
            "B": "nivolumab 是 anti-PD-1，主要作用於 T 細胞上的 PD-1，敘述正確。",
            "C": "panitumumab 是 anti-EGFR，可用於特定 RAS wild-type 大腸直腸癌，敘述正確。",
            "D": "pertuzumab 靶點是 HER2，不是 VEGFR，因此此項錯誤。",
        },
        "core": "pertuzumab/trastuzumab 都是 HER2 相關抗體；VEGF/VEGFR 另想 bevacizumab、ramucirumab 等。",
        "front": "pertuzumab 靶點",
        "back": "HER2，不是 VEGFR。",
    },
    57: {
        "analysis": "Erythropoietin 可治療 CKD 或化療相關貧血，但會增加血栓與高血壓風險；控制不良高血壓是重要禁忌或需避免情境。",
        "options": {
            "A": "貧血或缺氧會刺激腎臟增加 erythropoietin 合成，敘述正確。",
            "B": "可用於慢性腎病與部分化療引起貧血，敘述正確。",
            "C": "EPO 使紅血球生成增加，可能提高血栓事件風險，敘述正確。",
            "D": "高血壓控制不良者不宜使用或需先控制，說可使用是錯誤。",
        },
        "core": "EPO 可治 CKD/化療貧血，但副作用包括高血壓與血栓； uncontrolled hypertension 要避免。",
        "front": "EPO 禁忌/副作用",
        "back": "血栓與高血壓風險；高血壓控制不良不宜用。",
    },
    58: {
        "analysis": "直接凝血酶抑制劑中，dabigatran 是可口服的 DOAC，可降低非瓣膜性心房顫動的中風與全身性栓塞風險。",
        "options": {
            "A": "lepirudin 是注射用直接凝血酶抑制劑，非本題口服 AF 預防用藥。",
            "B": "bivalirudin 為注射用，常用於介入治療抗凝，不是口服 AF 用藥。",
            "C": "dabigatran 可口服，直接抑制 thrombin，是非瓣膜性 AF 抗凝選項。",
            "D": "argatroban 為注射用直接凝血酶抑制劑，常見於 HIT 情境，不是口服。",
        },
        "core": "可口服直接 thrombin inhibitor = dabigatran。",
        "front": "口服 direct thrombin inhibitor",
        "back": "dabigatran。",
    },
    59: {
        "analysis": "Repaglinide 是 meglitinide 類促胰島素分泌藥，作用短，主要控制餐後血糖；可用於腎功能不全或老年人時謹慎調整，不能說不宜用於所有這些患者。",
        "options": {
            "A": "repaglinide 服餐前使用、作用短，適合控制餐後血糖波動，敘述正確。",
            "B": "它不是 sulfonylurea，對磺脲類嚴重過敏者可作替代選項，敘述可接受。",
            "C": "可單用或與 metformin 等 biguanide 併用於第 2 型糖尿病，敘述正確。",
            "D": "repaglinide 多由肝臟代謝，腎功能不全或老年人可謹慎使用；說不宜用於腎功能不全和老年人過度絕對。",
        },
        "core": "repaglinide 短效、餐前、控餐後血糖；腎功能不全不是絕對不能用。",
        "front": "repaglinide 錯誤敘述",
        "back": "不應籠統說腎功能不全或老年人不宜使用。",
    },
    60: {
        "analysis": "Anastrozole 是 aromatase inhibitor，降低雌激素，長期使用可造成骨質流失與骨質疏鬆。",
        "options": {
            "A": "bazedoxifene 是 SERM，可用於骨質疏鬆相關治療，非典型造成骨鬆。",
            "B": "calcitonin 可抑制破骨細胞，用於骨質疏鬆或高血鈣治療。",
            "C": "strontium ranelate 曾用於骨質疏鬆治療，不是本題長期導致骨鬆答案。",
            "D": "anastrozole 抑制雌激素生成，長期會增加骨質疏鬆與骨折風險。",
        },
        "core": "aromatase inhibitor 會降低雌激素，副作用是骨質流失。",
        "front": "anastrozole 長期副作用",
        "back": "骨質疏鬆。",
    },
    61: {
        "analysis": "醫源性 Cushing syndrome 是 glucocorticoid 過多，常見月亮臉、軀幹肥胖、多毛、高血糖與肌肉無力；低血糖反而少見。",
        "options": {
            "A": "月亮臉是 Cushing syndrome 典型表現。",
            "B": "軀幹肥胖與脂肪重新分布是典型表現。",
            "C": "多毛或皮膚改變可見於 Cushing syndrome。",
            "D": "類固醇過多傾向造成高血糖與胰島素阻抗，不是低血糖，因此此項較少出現。",
        },
        "core": "Cushing syndrome 代謝表現是高血糖，不是低血糖。",
        "front": "Cushing syndrome 少見症狀",
        "back": "低血糖少見；常見高血糖、月亮臉、軀幹肥胖。",
    },
    62: {
        "analysis": "Furosemide 是 loop diuretic，作用在亨利氏環粗上升支，抑制 Na+/K+/2Cl- cotransporter。",
        "options": {
            "A": "亨利氏環上升支抑制 NKCC2 是 furosemide 的正確機轉。",
            "B": "Na+/Cl- cotransporter 是 thiazide 類在遠曲小管的主要靶點，不是 furosemide。",
            "C": "NKCC2 位置在亨利氏環粗上升支，不是近端腎小管。",
            "D": "近端腎小管 Na+/Cl- cotransporter 不是 furosemide 的主要作用點。",
        },
        "core": "Loop diuretic = thick ascending limb NKCC2 inhibitor。",
        "front": "furosemide 機轉",
        "back": "抑制亨利氏環粗上升支 Na+/K+/2Cl- cotransporter。",
    },
    63: {
        "analysis": "molsidomine、nitroprusside 釋放 NO 增加 cGMP；tadalafil 抑制 PDE5 也增加 cGMP。Bosentan 是 endothelin receptor antagonist，非透過增加 cGMP。",
        "options": {
            "A": "molsidomine 為 NO donor 類藥物，可經 cGMP 造成血管擴張。",
            "B": "bosentan 阻斷 endothelin receptor，減少內皮素造成的血管收縮，不是藉增加 cGMP。",
            "C": "sodium nitroprusside 釋放 NO，活化 guanylyl cyclase 增加 cGMP。",
            "D": "tadalafil 抑制 PDE5，減少 cGMP 分解而促進血管擴張。",
        },
        "core": "Bosentan 是 endothelin receptor antagonist；PDE5 inhibitor 與 NO donor 才走 cGMP。",
        "front": "非 cGMP 血管擴張藥",
        "back": "bosentan。",
    },
    64: {
        "analysis": "amiodarone、disopyramide、dofetilide 都有抑制 K+ channel、延長 repolarization 的作用；adenosine 主要作用於 A1 receptor，增加 K+ conductance 與抑制 Ca2+ influx，但不是 K+ channel blocker。",
        "options": {
            "A": "adenosine 不抑制 K+ channel；它透過腺苷受體減慢 AV node conduction，是本題答案。",
            "B": "amiodarone 屬 class III 為主，會抑制 K+ channel 延長動作電位。",
            "C": "disopyramide 屬 class IA，除 Na+ channel 外也延長 repolarization，具 K+ channel 抑制相關效果。",
            "D": "dofetilide 是選擇性 IKr K+ channel blocker。",
        },
        "core": "dofetilide/amiodarone 抑制 K；adenosine 是 AV node 抑制藥，不是 K blocker。",
        "front": "不抑制 K channel 抗心律不整藥",
        "back": "adenosine。",
    },
    65: {
        "analysis": "Scopolamine 是抗 muscarinic 藥，可用於暈車、散瞳與腸胃痙攣；但會造成尿滯留，因此排尿困難者不適用。",
        "options": {
            "A": "抗 muscarinic 藥可造成散瞳與睫狀肌麻痺，必要時可用於散瞳。",
            "B": "scopolamine 常用於暈動病預防，敘述正確。",
            "C": "抗膽鹼會抑制膀胱逼尿肌收縮、加重尿滯留，排尿困難最不適用。",
            "D": "抗 muscarinic 可減少腸蠕動與痙攣，腹痛腹瀉某些情境可用。",
        },
        "core": "抗 muscarinic 藥會加重尿滯留，BPH 或排尿困難要避免。",
        "front": "scopolamine 不適用",
        "back": "排尿困難或尿滯留。",
    },
    66: {
        "analysis": "doxazosin、clonidine、betaxolol 都可降血壓；midodrine 是 α1 agonist，造成血管收縮，用於姿勢性低血壓，會升血壓。",
        "options": {
            "A": "doxazosin 是 α1 blocker，可造成血管擴張、降低血壓。",
            "B": "clonidine 是中樞 α2 agonist，降低交感輸出而降血壓。",
            "C": "midodrine 是 α1 agonist，用來升高血壓治療姿勢性低血壓，因此不具降壓效果。",
            "D": "betaxolol 是 β1 blocker，可降低血壓與心率。",
        },
        "core": "midodrine 是升壓 α1 agonist；doxazosin、clonidine、β-blocker 才可降壓。",
        "front": "不降血壓藥物",
        "back": "midodrine 會升血壓。",
    },
    67: {
        "analysis": "Ciclesonide 是吸入後在肺部由 esterase 活化的 prodrug，口咽部活性較低，因此較少口腔念珠菌等局部副作用。",
        "options": {
            "A": "budesonide 是常用吸入類固醇，但不是以氣管 esterase 活化、降低口腔念珠菌風險的代表答案。",
            "B": "ciclesonide 為 prodrug，經肺部 esterase 轉成活性代謝物，局部口腔副作用較少。",
            "C": "flunisolide 不是本題所描述的 esterase 活化 prodrug 代表。",
            "D": "mometasone 為吸入/鼻用類固醇，但不是本題機轉代表。",
        },
        "core": "ciclesonide 是吸入性類固醇 prodrug，肺部活化，口腔念珠菌風險較低。",
        "front": "吸入後 esterase 活化 ICS",
        "back": "ciclesonide。",
    },
    68: {
        "analysis": "急性結腸假性阻塞（Ogilvie syndrome）可用 neostigmine 增加副交感活性，促進結腸蠕動解除擴張。",
        "options": {
            "A": "sucralfate 是胃黏膜保護劑，不會有效改善急性結腸假性阻塞。",
            "B": "bismuth 用於消化不良、腹瀉或幽門螺旋桿菌療法輔助，不是 Ogilvie syndrome 治療。",
            "C": "neostigmine 抑制 acetylcholinesterase，增加腸道蠕動，是急性結腸假性阻塞適合藥物。",
            "D": "metoclopramide 主要促進上消化道蠕動與止吐，對急性結腸假性阻塞不是最佳答案。",
        },
        "core": "Ogilvie syndrome 藥物治療首選常考 neostigmine。",
        "front": "acute colonic pseudo-obstruction",
        "back": "neostigmine。",
    },
    69: {
        "analysis": "腹瀉型腸躁症治療可用 5-HT3 antagonist 如 alosetron、抗痙攣藥等；linaclotide 促進腸液分泌，用於便秘型 IBS，會加重腹瀉。",
        "options": {
            "A": "alosetron 是 5-HT3 antagonist，可用於特定嚴重 IBS-D 患者。",
            "B": "scopolamine 抗膽鹼可減少腸痙攣，能緩解部分腹痛腹瀉症狀。",
            "C": "octreotide 可抑制腸道分泌與某些分泌性腹瀉，方向上可減少腹瀉。",
            "D": "linaclotide 是 guanylate cyclase-C agonist，增加腸液分泌與蠕動，主要治 IBS-C，最不適用 IBS-D。",
        },
        "core": "linaclotide 治便秘型 IBS，不適合腹瀉型 IBS。",
        "front": "IBS-D 最不適合藥物",
        "back": "linaclotide。",
    },
    70: {
        "analysis": "anakinra、canakinumab、rilonacept 都直接阻斷 IL-1 路徑；apremilast 是 PDE4 inhibitor，調節 cAMP 與發炎細胞激素，不是 IL-1 路徑抑制劑。",
        "options": {
            "A": "apremilast 抑制 PDE4，不能直接抑制 IL-1 訊息傳遞，因此符合題目。",
            "B": "anakinra 是 IL-1 receptor antagonist，可抑制 IL-1 訊息。",
            "C": "canakinumab 是 anti-IL-1β monoclonal antibody，可阻斷 IL-1β。",
            "D": "rilonacept 是 IL-1 trap，可結合 IL-1，抑制其路徑。",
        },
        "core": "IL-1 抑制藥：anakinra、canakinumab、rilonacept；apremilast 是 PDE4 inhibitor。",
        "front": "非 IL-1 pathway inhibitor",
        "back": "apremilast。",
    },
    71: {
        "analysis": "celecoxib、etodolac、meloxicam 都相對偏 COX-2；piroxicam 是傳統非選擇性 NSAID，對 COX-2 選擇性最低。",
        "options": {
            "A": "celecoxib 是選擇性 COX-2 inhibitor，選擇性高。",
            "B": "etodolac 相對偏 COX-2，選擇性高於傳統非選擇性 NSAID。",
            "C": "piroxicam 是非選擇性 NSAID，對 COX-2 選擇性最低。",
            "D": "meloxicam 有相對 COX-2 偏向性，選擇性高於 piroxicam。",
        },
        "core": "COX-2 選擇性：celecoxib 高；meloxicam/etodolac 偏 COX-2；piroxicam 低。",
        "front": "COX-2 選擇性最低",
        "back": "piroxicam。",
    },
    72: {
        "analysis": "躁症（mania）治療常用 lithium、valproate、carbamazepine 或抗精神病藥；fluoxetine 是 SSRI，可能誘發或惡化躁症，不適合單用治療 mania。",
        "options": {
            "A": "valproic acid 可用於急性躁症與雙相情感障礙維持治療。",
            "B": "lithium 是雙相情感障礙躁症的經典治療。",
            "C": "carbamazepine 可作為 mood stabilizer 治療躁症。",
            "D": "fluoxetine 為 SSRI 抗憂鬱藥，不是 mania 治療首選，且可能誘發躁轉。",
        },
        "core": "mania 治療用 mood stabilizer；SSRI 不適合治療急性 mania。",
        "front": "mania 最不適合藥物",
        "back": "fluoxetine。",
    },
    73: {
        "analysis": "tramadol 主要是弱 μ-opioid receptor agonist，並抑制 serotonin/norepinephrine reuptake；不是 κ receptor agonist。",
        "options": {
            "A": "μ opioid receptor 是 Gi/o coupled receptor，會抑制 adenylate cyclase，敘述正確。",
            "B": "opioid receptor 可位於突觸前抑制 neurotransmitter release，也可位於突觸後造成 hyperpolarization。",
            "C": "endorphins 與 dynorphins 都是內生性 opioid peptides，敘述正確。",
            "D": "tramadol 不是 κ agonist；其主要為弱 μ agonist 加上單胺再回收抑制，因此此項錯誤。",
        },
        "core": "tramadol = weak μ agonist + SNRI-like effect，不是 κ agonist。",
        "front": "tramadol 機轉",
        "back": "弱 μ agonist，並抑制 NE/5-HT 回收。",
    },
    74: {
        "analysis": "Paroxetine 是 SSRI，主要抑制 serotonin transporter（SERT），增加突觸間 serotonin。",
        "options": {
            "A": "抑制 serotonin 回收是 paroxetine 的主要作用機制。",
            "B": "抑制 norepinephrine 回收較屬 SNRI 或 TCA 相關機轉，不是 paroxetine 主要作用。",
            "C": "阻斷 D2 受體是抗精神病藥常見機轉，不是 SSRI。",
            "D": "阻斷 5-HT2 不是 paroxetine 的主要抗憂鬱機轉。",
        },
        "core": "paroxetine 是 SSRI，抑制 serotonin reuptake。",
        "front": "paroxetine 機轉",
        "back": "抑制 serotonin 回收。",
    },
    75: {
        "analysis": "β-blocker 過量造成心搏過緩與低血壓時，glucagon 可直接活化心肌 glucagon receptor，增加 cAMP，繞過 β receptor 改善心收縮與心率。",
        "options": {
            "A": "theophylline 可作為某些支氣管擴張或腺苷相關情境用藥，但不是 β-blocker 過量首選解毒。",
            "B": "caffeine 不是臨床處理 β-blocker 中毒的標準解毒藥。",
            "C": "metaproterenol 是 β agonist，但受體被阻斷時效果有限，不是最佳解毒選擇。",
            "D": "glucagon 不經 β receptor 而增加 cAMP，是 β-blocker 過量的經典解毒藥。",
        },
        "core": "β-blocker overdose 解毒先想 glucagon，因其可獨立增加心肌 cAMP。",
        "front": "β-blocker 過量解毒",
        "back": "glucagon。",
    },
    76: {
        "analysis": "心肌梗塞再灌流傷害的核心機轉之一是氧自由基大量生成，伴隨鈣離子失衡與發炎，反而加重細胞損傷。",
        "options": {
            "A": "中間絲減少不是再灌流傷害最典型的加重機轉。",
            "B": "血流恢復帶來氧氣，產生 reactive oxygen species/free radicals，是再灌流傷害關鍵。",
            "C": "粒線體腫脹可見於不可逆細胞傷害，但題目問再灌流後最可能加重的變化，最佳是自由基形成。",
            "D": "蛋白質合成減少可見於一般細胞傷害，但不是再灌流傷害核心機轉。",
        },
        "core": "Ischemia-reperfusion injury 重點：free radicals、calcium overload、inflammation。",
        "front": "再灌流傷害",
        "back": "自由基增加是重要機轉。",
    },
    77: {
        "analysis": "Apoptosis 典型為細胞縮小、染色質濃縮、DNA fragmentation 與 apoptotic bodies，通常不引起明顯發炎。",
        "options": {
            "A": "細胞腫脹較典型屬 necrosis，不是 apoptosis。",
            "B": "細胞內鈣離子明顯增加可見於細胞傷害與壞死相關機轉，但不是 apoptosis 最典型形態。",
            "C": "嗜中性球浸潤代表發炎反應，necrosis 較常見；apoptosis 通常不引起明顯發炎。",
            "D": "染色質濃縮是 apoptosis 最典型的形態學變化。",
        },
        "core": "Apoptosis = cell shrinkage、chromatin condensation、apoptotic bodies、少發炎。",
        "front": "apoptosis 典型現象",
        "back": "染色質濃縮。",
    },
    78: {
        "analysis": "Marfan syndrome 多由 FBN1 突變造成 fibrillin-1 異常，使 TGF-β 訊號過度活化；主要影響骨骼、眼睛與心血管系統。",
        "options": {
            "A": "Marfan 主要涉及心血管、骨骼與眼部，不是神經系統作為三大主要器官。",
            "B": "COL1A1/COL1A2 是第一型膠原相關，較與 osteogenesis imperfecta 等相關；Marfan 是 FBN1。",
            "C": "fibrillin 異常造成 TGF-β 過度活化，是 Marfan 致病機制之一，最適當。",
            "D": "診斷多依臨床、家族史與 FBN1 基因檢測；FISH 不是最適合的標準工具。",
        },
        "core": "Marfan = FBN1/fibrillin-1 defect + increased TGF-β signaling。",
        "front": "Marfan syndrome 機轉",
        "back": "FBN1 異常導致 TGF-β 過度活化。",
    },
    79: {
        "analysis": "Th2 反應與 IL-4、IL-5、IL-13、IgE、嗜酸性球、蠕蟲感染與外因性過敏相關；肉芽腫性發炎典型偏 Th1/macrophage。",
        "options": {
            "A": "把肉芽腫性發炎也納入 Th2 不適當，因其典型為 Th1 介導。",
            "B": "蠕蟲感染與外因性過敏性鼻炎都屬 Th2 相關反應，組合正確。",
            "C": "包含過敏性鼻炎正確，但肉芽腫性發炎不是 Th2 典型。",
            "D": "包含蠕蟲感染正確，但肉芽腫性發炎不是 Th2 典型。",
        },
        "core": "Th2 = helminth、IgE、eosinophil、allergy；Th1 = granuloma。",
        "front": "Th2 相關疾病",
        "back": "蠕蟲感染與外因性過敏性鼻炎。",
    },
    80: {
        "analysis": "腎移植超急性排斥由既存抗供者抗體造成，補體活化與內皮傷害導致血栓、嗜中性球浸潤與缺血性壞死。",
        "options": {
            "A": "微血管血小板與纖維素血栓、嗜中性球浸潤、缺血性傷害，最像超急性排斥。",
            "B": "淋巴細胞性間質血管炎較偏急性細胞性排斥的表現。",
            "C": "tubulitis 也是急性 T 細胞媒介排斥的重要表現，不是超急性。",
            "D": "腎絲球炎與腎小管周圍微血管炎可見於抗體媒介排斥，但題目問最類似超急性病變，血栓性缺血更典型。",
        },
        "core": "Hyperacute rejection = preformed antibody + complement + thrombosis + ischemic necrosis。",
        "front": "超急性排斥病理",
        "back": "微血管血栓與缺血性傷害。",
    },
    81: {
        "analysis": "紫外線最典型造成 DNA 相鄰嘧啶鹼基形成 pyrimidine dimer，特別是 thymine dimer；若修復失敗可導致皮膚癌。",
        "options": {
            "A": "形成嘧啶二聚體是 UV 致癌的核心 DNA 損傷。",
            "B": "雙股 DNA 斷裂較常與游離輻射等相關，不是 UV 主要考點。",
            "C": "染色體非平衡轉位不是 UV light 的主要直接 DNA 損傷。",
            "D": "基因擴增可見於癌症演化，但不是 UV 的主要初始 DNA 損傷。",
        },
        "core": "UV causes pyrimidine dimers；ionizing radiation causes double-strand breaks。",
        "front": "UV DNA damage",
        "back": "pyrimidine dimer。",
    },
    82: {
        "analysis": "生牛肉後 O157:H7 出血性腹瀉，接著少尿、血尿、急性腎衰竭，是 STEC-HUS；Shiga toxin 傷害內皮細胞，造成微血管病變性溶血與腎損傷。",
        "options": {
            "A": "ADAMTS13 下降是 TTP 的重要機轉，不是典型 STEC-HUS 主因。",
            "B": "Shiga toxin 對血管內皮尤其腎小球內皮造成傷害，是 HUS 致病主因。",
            "C": "HUS 屬血小板微血栓性病變，PT/PTT 通常不如 DIC 那樣延長；初期 PTT 延長不是常見核心。",
            "D": "產生 von Willebrand factor 抗體不是 STEC-HUS 的致病機制。",
        },
        "core": "STEC-HUS = endothelial injury by Shiga toxin，並非 ADAMTS13 缺乏的 TTP。",
        "front": "O157:H7 HUS 機轉",
        "back": "Shiga toxin 傷害血管內皮細胞。",
    },
    83: {
        "analysis": "白色梗塞常發生在緻密實質器官、終末動脈供血且缺乏雙重血流的器官，如心、脾、腎；腎臟梗塞屬典型白色梗塞。",
        "options": {
            "A": "睪丸扭轉因靜脈回流受阻，較易出現出血性/紅色梗塞。",
            "B": "肺有雙重血流且組織疏鬆，肺梗塞多為紅色梗塞。",
            "C": "小腸梗塞常因靜脈淤血與再灌流，偏紅色梗塞。",
            "D": "腎臟為緻密器官且終末動脈供血，典型為白色梗塞。",
        },
        "core": "白色梗塞：心、脾、腎；紅色梗塞：肺、腸、睪丸扭轉、靜脈阻塞或再灌流。",
        "front": "白色梗塞例子",
        "back": "腎臟梗塞。",
    },
    84: {
        "analysis": "前列腺素 E2 可維持動脈導管開放；抑制 PGE2 合成（如 indomethacin/ibuprofen）可促進開放性動脈導管關閉。",
        "options": {
            "A": "開放性動脈導管可用 NSAID 抑制 PGE2 促進關閉，最符合。",
            "B": "心房中膈缺損不是靠抑制 PGE2 治療。",
            "C": "心室中膈缺損也不是以 PGE2 抑制作為主要治療。",
            "D": "主動脈閉鎖等 ductal-dependent lesion 反而可能需要 PGE1 維持導管開放。",
        },
        "core": "PDA 關閉用 indomethacin/ibuprofen；ductal-dependent lesions 用 PGE1 維持開放。",
        "front": "PGE2 抑制治療",
        "back": "開放性動脈導管。",
    },
    85: {
        "analysis": "急性骨髓性白血病（AML）診斷通常以骨髓或周邊血 myeloblasts ≥20% 為門檻；25% 已符合 AML。",
        "options": {
            "A": "原發性骨髓纖維化重點是巨核細胞異常與骨髓纖維化，不以 myeloblast 25% 為診斷。",
            "B": "CML 可有慢性期、加速期、急變期；單看 myeloblast 25% 已偏向急性白血病/急變，不是一般 CML 診斷。",
            "C": "myeloblasts 25% 超過 AML 診斷門檻，最符合急性骨髓性白血病。",
            "D": "MDS 通常 blasts 未達 AML 門檻；達 20% 以上應診斷 AML。",
        },
        "core": "AML blast cutoff 常考 ≥20%。",
        "front": "myeloblast 25%",
        "back": "急性骨髓性白血病（AML）。",
    },
    86: {
        "analysis": "鬱血性脾腫大最常見原因是門脈高壓，而門脈高壓最常由肝硬化造成。",
        "options": {
            "A": "心臟衰竭可造成全身靜脈鬱血，但不是鬱血性脾腫大最常見原因。",
            "B": "門靜脈血栓可造成門脈壓升高與脾腫大，但流行上不如肝硬化常見。",
            "C": "脾靜脈血栓可造成局部脾鬱血，但不是最常見原因。",
            "D": "肝硬化導致門脈高壓，是鬱血性脾腫大最常見原因。",
        },
        "core": "鬱血性脾腫大最常因肝硬化造成門脈高壓。",
        "front": "鬱血性脾腫大最常見原因",
        "back": "肝硬化。",
    },
    87: {
        "analysis": "惡性間皮瘤與石棉暴露密切相關，最常發生於胸膜，可有 BAP1 等突變；其以局部侵犯為主，遠端轉移並非最典型常見表現。",
        "options": {
            "A": "石棉暴露是惡性間皮瘤最重要危險因子之一，敘述正確。",
            "B": "BAP1 突變可見於間皮瘤，敘述正確。",
            "C": "惡性間皮瘤最常見位置是胸膜，敘述正確。",
            "D": "間皮瘤常局部擴展包覆肺臟，遠端轉移不是最典型常見表現，因此此項錯誤。",
        },
        "core": "Mesothelioma：asbestos、pleura、BAP1；以局部侵犯為主。",
        "front": "惡性間皮瘤錯誤敘述",
        "back": "不以常造成遠端轉移為典型。",
    },
    88: {
        "analysis": "氣胸可造成縱膈偏移、肺塌陷後纖維化或感染相關併發症；肺癌不是氣胸的典型併發症，反而某些肺病或腫瘤可造成氣胸。",
        "options": {
            "A": "張力性氣胸可造成縱膈腔偏移，是重要併發症。",
            "B": "反覆或治療後可出現肺部瘢痕或沾黏，可能相關。",
            "C": "肺癌不是氣胸造成的併發症，因此最不可能。",
            "D": "感染或胸腔處置後可能有積膿等併發症，雖非最常見但比肺癌更合理。",
        },
        "core": "氣胸急性危險併發症是張力性氣胸與縱膈偏移；肺癌不是其併發症。",
        "front": "氣胸最不可能併發症",
        "back": "肺癌。",
    },
    89: {
        "analysis": "肺錯構瘤（hamartoma）是最常見良性肺腫瘤，常含軟骨、脂肪與結締組織等成熟組織。",
        "options": {
            "A": "hamartoma 是最常見良性肺腫瘤，為正確答案。",
            "B": "孤立性纖維瘤可發生於胸膜或肺相關部位，但不是最常見良性肺腫瘤。",
            "C": "血管瘤可為良性腫瘤，但在肺部不如 hamartoma 常見。",
            "D": "平滑肌瘤可發生但不是最常見肺良性腫瘤。",
        },
        "core": "最常見良性肺腫瘤是 hamartoma。",
        "front": "最常見良性肺腫瘤",
        "back": "錯構瘤（hamartoma）。",
    },
    90: {
        "analysis": "自體免疫性肝炎常有高 IgG/γ-globulin、漿細胞浸潤，對類固醇或免疫抑制劑反應佳；第二型較常見於兒童或年輕人，不是老年人。",
        "options": {
            "A": "IgG 或 γ-球蛋白增高是 AIH 常見實驗室表現。",
            "B": "第二型 AIH 通常較常見於兒童與年輕族群；說較常發生於老年人是錯誤。",
            "C": "病理可見界面性肝炎與漿細胞浸潤，未治療可進展肝硬化，敘述正確。",
            "D": "類固醇或免疫抑制治療通常可改善發炎，敘述正確。",
        },
        "core": "Type 2 autoimmune hepatitis 較常見於兒童/年輕人，不是老年人。",
        "front": "自體免疫性肝炎錯誤敘述",
        "back": "第二型不是較常發生於老年人。",
    },
    91: {
        "analysis": "慢性胰臟炎是反覆發炎造成的不可逆纖維化、腺泡萎縮與導管改變，常保留相對較多胰島；不是可逆變化。",
        "options": {
            "A": "嚴重急性胰臟炎可造成 shock、ARDS、DIC、AKI 等全身併發症，敘述正確。",
            "B": "PRSS1、SPINK1 等突變與遺傳性或反覆胰臟炎相關，敘述正確。",
            "C": "慢性胰臟炎組織學常見廣泛纖維化，導管與蘭氏小島相對殘留，敘述正確。",
            "D": "慢性胰臟炎造成永久結構破壞與纖維化，屬不可逆變化，因此此項錯誤。",
        },
        "core": "慢性胰臟炎 = 不可逆纖維化與外分泌破壞。",
        "front": "慢性胰臟炎錯誤敘述",
        "back": "不是可逆變化。",
    },
    92: {
        "analysis": "大量 NSAIDs 使用後上腹痛、噁心嘔吐與吐血，最可能是前列腺素下降造成胃黏膜保護減弱，引起急性糜爛性胃炎或潰瘍出血。",
        "options": {
            "A": "NSAIDs 抑制 COX、降低 PGE2，導致急性胃炎與出血，能直接解釋她大量止痛藥後的上腹痛與吐血。",
            "B": "胃腺癌通常不是幾天內因 NSAIDs 使用後急性吐血的最可能原因。",
            "C": "幽門螺旋桿菌可造成慢性胃炎與潰瘍，但題幹強調大量 NSAIDs 與急性症狀，較支持 NSAID 急性胃炎。",
            "D": "增生性息肉多為慢性病灶，非此急性上消化道出血最可能原因。",
        },
        "core": "NSAIDs 造成胃黏膜 PGE2 下降，導致急性胃炎/糜爛與出血。",
        "front": "NSAID + 吐血",
        "back": "急性胃炎或糜爛性胃炎最可能。",
    },
    93: {
        "analysis": "長期第二型糖尿病胰島常沉積 islet amyloid polypeptide（amylin）形成類澱粉沉積，並伴隨 β 細胞功能下降。",
        "options": {
            "A": "脂褐質是老化或耗損色素，不是第二型糖尿病胰島典型沉積物。",
            "B": "第二型糖尿病胰島常有 amylin 形成的類澱粉沉積，最符合。",
            "C": "鈣質沉積不是第二型糖尿病胰島最典型病理變化。",
            "D": "鋅與胰島素儲存有關，但不是長期第二型糖尿病胰島病理沉積答案。",
        },
        "core": "Type 2 DM 胰島病理：amylin amyloid deposition。",
        "front": "第二型糖尿病胰島沉積",
        "back": "類澱粉（amylin/IAPP）。",
    },
    94: {
        "analysis": "腎臟乳突狀癌常見 trisomy 7、trisomy 17 與男性 loss of Y；染色體 3p 缺失是透明細胞腎細胞癌的典型變化。",
        "options": {
            "A": "3p deletion 與 VHL/clear cell RCC 相關，最不可能是 papillary RCC 的典型異常。",
            "B": "trisomy 7 是 papillary RCC 常見異常。",
            "C": "trisomy 17 也是 papillary RCC 常見異常。",
            "D": "男性 loss of Y 可見於 papillary RCC，屬典型配對之一。",
        },
        "core": "Papillary RCC = trisomy 7/17、loss of Y；Clear cell RCC = 3p/VHL。",
        "front": "papillary RCC 非典型基因異常",
        "back": "3p deletion。",
    },
    95: {
        "analysis": "乳房放射狀疤痕是良性硬化性病灶，但影像與形態可呈星芒狀、不規則，容易與浸潤性乳癌混淆。",
        "options": {
            "A": "radial scar 與第一型糖尿病沒有典型關聯。",
            "B": "名稱有 scar，但不一定是外傷或手術後造成的疤痕。",
            "C": "血性乳頭分泌較常考乳管內乳突瘤等，不是 radial scar 最典型敘述。",
            "D": "radial scar 形狀不規則、影像可似癌，常需與乳癌鑑別，最適當。",
        },
        "core": "Radial scar 是良性但可模仿乳癌的不規則星芒狀病灶。",
        "front": "乳房 radial scar",
        "back": "形狀不規則，會與乳癌混淆。",
    },
    96: {
        "analysis": "原位乳癌代表癌細胞仍侷限於導管或小葉內，未突破基底膜；病理上保留完整肌上皮層是判斷未侵犯的重要特徵。",
        "options": {
            "A": "完整 myoepithelial layer 支持原位病灶，為最重要鑑別特徵。",
            "B": "纖維化與纖維母細胞增生可見於多種病灶，不是診斷原位乳癌的核心。",
            "C": "淋巴球漿細胞浸潤有無不是區分原位與侵犯的最重要標準。",
            "D": "ER 陽性可協助分類與治療，但不能作為原位乳癌診斷最重要特徵。",
        },
        "core": "原位癌的關鍵是未突破基底膜，乳房病理看肌上皮層仍完整。",
        "front": "原位乳癌最重要病理特徵",
        "back": "完整肌上皮層。",
    },
    97: {
        "analysis": "第一型子宮內膜癌通常較年輕、雌激素相關、endometrioid，前驅為子宮內膜增生；第二型較年長、較侵襲，serous carcinoma 可有 serous endometrial intraepithelial carcinoma 等前驅病灶，不能說罕見相關前驅病灶。",
        "options": {
            "A": "第一型通常發生年齡較早，與雌激素相關，敘述正確。",
            "B": "第一型多為 endometrioid adenocarcinoma，前驅為 endometrial hyperplasia，敘述正確。",
            "C": "serous carcinoma 屬第二型，且可有漿液性子宮內膜上皮內癌等前驅病灶；說罕見相關前驅病灶不適當。",
            "D": "第二型通常較高惡性度、臨床更 aggressive，敘述正確。",
        },
        "core": "Type I endometrial cancer = endometrioid/hyperplasia；Type II serous carcinoma 更 aggressive，且可有 serous intraepithelial precursor。",
        "front": "子宮內膜癌 Type I vs II",
        "back": "第二型 serous carcinoma 不是沒有重要前驅病灶。",
    },
    98: {
        "analysis": "血管炎造成周邊神經缺血，常呈不對稱、多灶性的單神經炎多發（mononeuritis multiplex）。",
        "options": {
            "A": "polyneuropathy 可見於糖尿病等瀰漫性病變，但不是血管炎最典型表現。",
            "B": "單一 mononeuropathy 太局限，血管炎常多灶分布。",
            "C": "polyradiculoneuropathy 較偏神經根與周邊神經廣泛發炎，非血管炎最常見型態。",
            "D": "mononeuritis multiplex 由多個神經血管供應區缺血造成，是血管炎最典型周邊神經病變。",
        },
        "core": "Vasculitic neuropathy 最典型是 mononeuritis multiplex。",
        "front": "血管炎周邊神經病變",
        "back": "mononeuritis multiplex。",
    },
    99: {
        "analysis": "題幹提示高度傳染性腦組織病變，搭配病理圖常指 prion disease 的海綿狀腦病變；臨床典型是快速進行性失智、肌陣攣與神經功能退化。",
        "options": {
            "A": "prion disease 不以惡性腦瘤為典型結局。",
            "B": "自發性蜘蛛膜下腔大出血多與腦動脈瘤破裂相關，不是海綿狀腦病變的典型表現。",
            "C": "Creutzfeldt-Jakob disease 等 prion disease 典型造成快速進行性失智，最符合。",
            "D": "腦膜炎以感染發炎與腦膜刺激症狀為主，不是高度傳染性海綿狀腦病變的典型臨床。",
        },
        "core": "prion disease/海綿狀腦病變的臨床關鍵是快速進行性失智。",
        "front": "高度傳染性腦組織病變",
        "back": "prion disease 常見快速進行性失智。",
    },
    100: {
        "analysis": "Willis 氏環若有囊狀動脈瘤，破裂最典型造成自發性蜘蛛膜下腔出血，常表現突發劇烈頭痛。",
        "options": {
            "A": "痴呆通常不是 Willis 氏環動脈瘤破裂的典型直接表現。",
            "B": "步態不穩與共濟失調較常定位小腦或後索/前庭系統，不是本題最可能結果。",
            "C": "舞蹈症常與基底核病變相關，不是 Willis 氏環動脈瘤典型表現。",
            "D": "Willis 氏環 berry aneurysm 破裂會導致自發性蜘蛛膜下腔出血，最符合。",
        },
        "core": "Circle of Willis berry aneurysm rupture = subarachnoid hemorrhage。",
        "front": "Willis 氏環動脈瘤",
        "back": "破裂造成自發性蜘蛛膜下腔出血。",
    },
}


def build_explanation(item):
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
    source_path = Path(SOURCE_FILE)
    exam = json.loads(source_path.read_text(encoding="utf-8-sig"))
    questions = exam["questions"]
    by_number = {q["question_number"]: q for q in questions}
    missing = sorted(set(range(1, 101)) - set(FACTS))
    if missing:
        raise SystemExit(f"missing facts for questions: {missing}")

    out_dir = Path("scratch/rewrite_updates/113-1_medicine-2")
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")

    for start in range(1, 101, 10):
        end = start + 9
        updates = []
        for qnum in range(start, end + 1):
            source_q = by_number[qnum]
            item = FACTS[qnum]
            updates.append(
                {
                    "question_id": source_q["id"],
                    "question_number": qnum,
                    "explanation": build_explanation(item),
                    "key_point": item["core"],
                    "flashcard_front": item["front"],
                    "flashcard_back": item["back"],
                    "flashcard_summary": f"{item['front']} -> {item['back']}",
                    "review_status": "ai_generated",
                    "explanation_model": MODEL,
                    "explanation_generated_at": timestamp,
                    "manual_review_notes": item.get("notes", []),
                }
            )

        update_file = out_dir / f"q{start:03d}-q{end:03d}.json"
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates,
        }
        update_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(update_file)


if __name__ == "__main__":
    main()
