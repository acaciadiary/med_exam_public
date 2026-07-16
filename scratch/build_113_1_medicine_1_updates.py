import json
from pathlib import Path

SOURCE_FILE = "public/data/exams/113-1/medicine-1.json"
DATASET_ID = "113-1_medicine-1"
OUT_DIR = Path("scratch/rewrite_updates/113-1_medicine-1")
STAMP = "2026-07-16T00:00:00+08:00"


QDATA = {
    31: {
        "analysis": "題目考踝關節的骨性構成。真正的踝關節是脛骨遠端與腓骨外踝形成踝穴，和距骨滑車相接；跟骨主要參與距下關節，不是踝關節本體。",
        "notes": {
            "A": "股骨屬大腿骨，參與髖關節與膝關節，不參與踝關節，因此錯誤。",
            "B": "脛骨與腓骨正確，但跟骨是足跟骨，主要與距骨形成距下關節，不能取代距骨。",
            "C": "脛骨、腓骨與距骨共同形成踝穴與距骨滑車的關節面，是踝關節的正確組合。",
            "D": "脛骨與距骨正確，但漏掉腓骨外踝，且把跟骨列入踝關節本體，因此錯誤。",
        },
        "core": "踝關節由脛骨、腓骨與距骨形成；跟骨屬距下關節的關鍵骨，不是踝關節三骨之一。",
    },
    32: {
        "analysis": "胚內體腔來自外側中胚層內部裂隙的形成。外側中胚層分成體壁層與臟壁層，兩層之間的空間即為胚內體腔。",
        "notes": {
            "A": "軸旁中胚層主要形成體節，進一步衍生脊椎、骨骼肌與真皮，不是胚內體腔最早出現處。",
            "B": "中間中胚層主要衍生泌尿生殖系統，並非體腔裂隙形成的主要來源。",
            "C": "外側中胚層會裂開形成胚內體腔，並分成體壁與臟壁中胚層，故為正確答案。",
            "D": "內胚層主要形成消化道與呼吸道上皮，不形成胚內體腔。",
        },
        "core": "胚內體腔最早出現在外側中胚層，並把外側中胚層分成體壁層與臟壁層。",
    },
    33: {
        "analysis": "咽弓題要把弓序、衍生肌肉與腦神經配對。第二咽弓又稱 hyoid arch，其肌肉衍生物由第七對顏面神經支配。",
        "notes": {
            "A": "三叉神經主要對應第一咽弓，支配咀嚼肌、下頷舌骨肌、二腹肌前腹等，不是第二咽弓。",
            "B": "顏面神經支配第二咽弓衍生肌肉，例如表情肌、鐙骨肌、莖突舌骨肌與二腹肌後腹，故正確。",
            "C": "舌咽神經對應第三咽弓，典型支配 stylopharyngeus，不是第二咽弓。",
            "D": "副神經主要支配胸鎖乳突肌與斜方肌，不是咽弓衍生肌的標準配對。",
        },
        "core": "第二咽弓的支配神經是顏面神經；第一咽弓是三叉神經，第三咽弓是舌咽神經。",
    },
    34: {
        "analysis": "十二指腸由前腸末端與中腸前段共同形成，隨胃旋轉移向右側，且大部分成為次發性後腹膜構造。",
        "notes": {
            "A": "十二指腸不是由前腸與後腸共同形成；其遠端部分來自中腸，後腸不參與。",
            "B": "十二指腸血供反映前腸與中腸來源，來自腹腔動脈幹與上腸繫膜動脈，不是下腸繫膜動脈。",
            "C": "胃旋轉使十二指腸轉向右側並貼近後腹壁，形成大部分次發性後腹膜化，敘述最適當。",
            "D": "十二指腸發育時腔道會暫時被上皮增生填塞，之後再通，因此不是全程維持中空管狀。",
        },
        "core": "十二指腸源自前腸末端與中腸前段，因胃旋轉而右移並多數次發性後腹膜化。",
    },
    35: {
        "analysis": "出生後第一次呼吸讓肺泡擴張、肺氧分壓上升，肺血管阻力快速下降，肺血流量增加，左心房回流與壓力上升，促進胎兒循環轉換。",
        "notes": {
            "A": "出生後肺血管阻力是顯著下降，不是增加，因肺泡擴張與氧氣上升使肺血管舒張。",
            "B": "肺血管阻力下降後，右心輸出更多流入肺循環，因此肺部血流量上升，敘述正確。",
            "C": "肺動脈管壁不會在剛出生呼吸時立刻顯著變厚；急性變化主要是血管阻力與血流改變。",
            "D": "肺靜脈回流增加使左心房壓力高於右心房，促成卵圓孔功能性關閉，故此選項方向相反。",
        },
        "core": "出生後肺泡擴張使肺血管阻力下降、肺血流量上升，左房壓開始高於右房壓。",
    },
    36: {
        "analysis": "腦室系統的胚胎來源要和腦泡對應。中腦腔室在發育後變窄，形成連接第三與第四腦室的大腦導水管。",
        "notes": {
            "A": "菱腦主要形成第四腦室相關腔室，不是大腦導水管。",
            "B": "中腦（mesencephalon）的腔室保留為大腦導水管，連接第三與第四腦室，故正確。",
            "C": "間腦主要形成第三腦室，不是大腦導水管。",
            "D": "端腦形成大腦半球與側腦室，不形成大腦導水管。",
        },
        "core": "大腦導水管是中腦腔室變窄後的衍生物。",
    },
    37: {
        "analysis": "福馬林固定主要靠甲醛與蛋白質形成交聯，能抑制自溶、殺死微生物並讓組織變硬；對脂質與細胞膜保存並非強項。",
        "notes": {
            "A": "福馬林不以完整保存脂質或細胞膜為主要作用，脂質在常規處理中容易被溶出，因此這是錯誤敘述。",
            "B": "甲醛可與蛋白質形成交聯，使組織固定、變硬，是福馬林的典型作用。",
            "C": "固定可抑制細胞自溶與腐敗，因此可防止 autolysis。",
            "D": "福馬林具有殺菌與滅活微生物作用，可保存檢體並降低感染風險。",
        },
        "core": "福馬林主要固定蛋白質，不是脂質固定劑；因此對細胞膜脂質保存有限。",
    },
    38: {
        "analysis": "氣管內襯是典型呼吸上皮，為具纖毛的偽複層柱狀上皮，並有杯狀細胞協助黏液纖毛清除。",
        "notes": {
            "A": "單層柱狀上皮可見於腸胃道等處，但氣管典型不是單層柱狀。",
            "B": "複層扁平上皮適合抵抗摩擦，常見於口腔、食道與陰道，不是正常氣管上皮。",
            "C": "複層柱狀上皮較少見，可見於部分大導管，不是氣管的代表上皮。",
            "D": "具纖毛偽複層柱狀上皮就是氣管與大氣道的典型呼吸上皮，故正確。",
        },
        "core": "氣管內襯是具纖毛偽複層柱狀上皮，屬典型呼吸上皮。",
    },
    39: {
        "analysis": "軟骨缺乏血管、淋巴與神經，營養依靠軟骨膜或滑液擴散，所以修復能力有限。透明軟骨基質主要是第二型膠原蛋白。",
        "notes": {
            "A": "附加生長主要由軟骨膜內層的 chondrogenic cells 分化為 chondroblasts，不是成熟 chondrocytes 直接主導。",
            "B": "透明軟骨主要含第二型膠原蛋白；第一型膠原蛋白較典型見於纖維軟骨與骨等組織。",
            "C": "軟骨是無血管組織，營養靠擴散供應，敘述正確。",
            "D": "軟骨因缺血管而再生能力差，受傷後通常不易完整癒合。",
        },
        "core": "軟骨是 avascular structure，透明軟骨以 type II collagen 為主且修復能力差。",
    },
    40: {
        "analysis": "衛星細胞位於周邊神經系統神經節，包繞神經元胞體並提供支持；形成周邊髓鞘的是 Schwann cell，不是 satellite cell。",
        "notes": {
            "A": "衛星細胞包繞的是周邊神經節的神經元胞體；中樞神經系統由星狀膠細胞、少突膠細胞等支持。",
            "B": "衛星細胞不是大型柱狀細胞，而是小型扁平或立方樣支持細胞。",
            "C": "H&E 下衛星細胞不是多核細胞；它們環繞神經元胞體形成一圈支持細胞。",
            "D": "衛星細胞不形成 myelin；PNS 髓鞘由 Schwann cell 形成，故此選項正確。",
        },
        "core": "衛星細胞包繞 PNS 神經節胞體，不負責形成髓鞘；PNS 髓鞘由 Schwann cell 形成。",
    },
    41: {
        "analysis": "第二型肺泡細胞是立方形分泌細胞，負責製造 surfactant，降低肺泡表面張力並協助肺泡穩定。",
        "notes": {
            "A": "覆蓋大部分肺泡表面的是第一型肺泡細胞；第二型細胞數量可不少，但覆蓋表面積較小。",
            "B": "氣血屏障由第一型肺泡細胞、融合基底膜與微血管內皮等組成，肺泡巨噬細胞不是屏障成分。",
            "C": "第二型肺泡細胞分泌 surfactant，是最典型功能，故正確。",
            "D": "薄而扁平的是第一型肺泡細胞；第二型肺泡細胞較偏立方形。",
        },
        "core": "Type II pneumocyte 分泌 surfactant；type I pneumocyte 才是薄而覆蓋面積大的氣體交換細胞。",
    },
    42: {
        "analysis": "黏原顆粒代表黏液分泌細胞的特徵。胃賁門腺以分泌黏液為主，因此可見 mucinogen granules。",
        "notes": {
            "A": "胃賁門腺細胞屬黏液分泌細胞，含 mucinogen granules，故正確。",
            "B": "胰腺泡細胞主要分泌消化酵素，富含 zymogen granules，不是黏原顆粒。",
            "C": "耳下腺腺泡細胞是漿液性分泌細胞，主要有酶原顆粒，不是黏液顆粒。",
            "D": "潘氏細胞含抗菌顆粒，例如 lysozyme、defensins，不是典型 mucinogen granules。",
        },
        "core": "胃賁門腺是黏液腺，含黏原顆粒；胰腺泡與耳下腺偏漿液性，潘氏細胞偏抗菌顆粒。",
    },
    43: {
        "analysis": "題目問膽囊固有層最不可能出現何者，但官方已一律給分。讀書時仍要掌握膽囊黏膜的基本構造：固有層可見結締組織、小血管與淋巴管，黏液腺較常在頸部區域，且膽囊沒有典型黏膜肌層與黏膜下層。",
        "notes": {
            "A": "穿孔型微血管是否可作為最不可能選項有教材差異，是本題爭議來源之一，官方接受給分。",
            "B": "小靜脈可存在於固有層結締組織中，因此若單選為最不可能並不穩定，官方給分合理。",
            "C": "淋巴管可存在於固有層，並非明確排除構造，故本題不宜硬改答案。",
            "D": "膽囊黏液腺可見於頸部附近，若題目未限定區域容易產生爭議，因此官方一律給分。",
        },
        "core": "膽囊固有層可有小血管、淋巴與結締組織；本題因構造描述與區域差異，官方一律給分。",
        "manual_review_notes": ["第43題官方一律給分，保留全給分狀態。"],
    },
    44: {
        "analysis": "毛囊的養分與氧氣主要來自毛球底部的真皮乳頭。真皮乳頭含豐富微血管，並提供訊號支持毛髮生長。",
        "notes": {
            "A": "真皮乳頭位於毛球基部，血管豐富，是供應毛囊養分與氧氣的主要構造，故正確。",
            "B": "玻璃膜是毛囊外側的基底膜樣結構，主要提供界面支持，不是血管供應來源。",
            "C": "內根鞘包覆毛幹並協助成形，但不富含血管。",
            "D": "外根鞘是上皮性包覆構造，不是提供毛囊血供的主要部位。",
        },
        "core": "毛囊血供與營養重點在毛球底部的 dermal papilla。",
    },
    45: {
        "analysis": "腎上腺皮質束狀帶細胞含大量脂肪小滴，外觀泡沫狀，主要分泌 cortisol 等 glucocorticoids。",
        "notes": {
            "A": "球小帶主要分泌 aldosterone 等 mineralocorticoids，不是糖皮質素主力來源。",
            "B": "束狀帶含大量脂質前驅物並分泌 glucocorticoids，是本題正確答案。",
            "C": "網狀帶主要分泌 adrenal androgens，雖屬皮質但不是糖皮質素主要區帶。",
            "D": "腎上腺髓質分泌 catecholamines，不分泌 glucocorticoids。",
        },
        "core": "腎上腺皮質：球小帶 aldosterone、束狀帶 cortisol、網狀帶 androgen。",
    },
    46: {
        "analysis": "附圖題原重點指向具纖毛細胞與分泌細胞、黏膜皺褶明顯的單層柱狀上皮，最符合輸卵管。",
        "notes": {
            "A": "輸卵管黏膜有纖毛細胞與分泌細胞，形成皺褶並幫助卵子與受精卵移動，最符合題意。",
            "B": "陰道為非角化複層扁平上皮，不是纖毛單層柱狀上皮。",
            "C": "輸出小管可有高低不齊、鋸齒狀或波浪狀管腔邊界，與輸卵管典型皺褶不同。",
            "D": "尿道上皮依部位可變化，並非此題附圖所指的典型輸卵管上皮。",
        },
        "core": "輸卵管上皮由纖毛細胞與分泌細胞構成，常見黏膜皺褶。",
    },
    47: {
        "analysis": "細胞膜的基本架構是磷脂雙層加上膜蛋白。膽固醇可調節流動性，但不是題目問的主要化學骨架。",
        "notes": {
            "A": "甘油是脂質骨架的一部分，但不是細胞膜與蛋白質並列的主要化學組成答案。",
            "B": "三酸甘油酯是儲存脂質，不是細胞膜雙層的主要結構脂質。",
            "C": "磷脂質形成 phospholipid bilayer，是細胞膜最主要的脂質骨架，故正確。",
            "D": "膽固醇可調節膜流動性與穩定性，但不是本題所問的主要組成類別。",
        },
        "core": "細胞膜主要由磷脂雙層與蛋白質構成，膽固醇負責調節膜性質。",
    },
    48: {
        "analysis": "視網膜多數神經元以 graded potential 傳遞訊號；真正具有閾值並產生動作電位、將訊號送出眼球的是節細胞。",
        "notes": {
            "A": "雙極細胞主要以漸進電位傳遞，不是主要產生動作電位的輸出細胞。",
            "B": "水平細胞負責側向調節，主要使用漸進電位。",
            "C": "無軸突細胞多作局部調節，部分可有特殊放電特性，但不是視網膜主要外傳動作電位細胞。",
            "D": "節細胞達閾值後可產生 action potentials，其軸突組成視神經，故正確。",
        },
        "core": "視網膜節細胞是產生動作電位並形成視神經的主要輸出細胞。",
    },
    49: {
        "analysis": "自主神經節前神經元除腦幹副交感核外，也位於脊髓特定區域。交感節前神經元位於 T1-L2 的 intermediolateral column。",
        "notes": {
            "A": "dorsal root ganglion 內是感覺神經元胞體，不是自主神經節前神經元。",
            "B": "substantia gelatinosa 位於背角，主要和痛溫覺調節相關。",
            "C": "Rexed lamina IX 含軀體運動神經元，支配骨骼肌，不是自主節前神經元主要位置。",
            "D": "intermediolateral column 是胸腰髓交感節前神經元胞體所在，故正確。",
        },
        "core": "交感節前神經元胞體位於 T1-L2 intermediolateral column。",
    },
    50: {
        "analysis": "多數器官中交感與副交感作用相反，但唾液腺是例外：兩者都可促進分泌，只是分泌物性質不同。",
        "notes": {
            "A": "副交感促進大量水樣唾液，交感也促進較黏稠、蛋白較多的唾液，因此方向較一致。",
            "B": "心跳速率通常由交感增加、副交感降低，方向相反。",
            "C": "胃腸蠕動通常由副交感增加、交感降低，方向相反。",
            "D": "膀胱括約肌與排尿反射中交感、副交感多呈相反調控，不是同向例外。",
        },
        "core": "唾液分泌是交感與副交感都可增加的少數同向例外；心跳、腸蠕動與排尿多相反。",
    },
    51: {
        "analysis": "大腦皮質大型錐體神經元負責皮質輸出，其中 Betz cells 最典型位於第 V 層，向腦幹與脊髓投射。",
        "notes": {
            "A": "第 I 層主要為分子層，細胞稀少，不是大型錐體神經元密集層。",
            "B": "第 Ib 層不是六層新皮質中大型輸出錐體細胞的典型高密度位置。",
            "C": "第 II 層以小型顆粒細胞與局部皮質連結較典型，不是 Betz cell 主力層。",
            "D": "第 V 層是大型錐體細胞與皮質下輸出神經元密集處，故正確。",
        },
        "core": "新皮質第 V 層含大型錐體神經元，負責重要皮質下輸出。",
    },
    52: {
        "analysis": "黑暗促進 melatonin 的路徑為視網膜到視交叉上核，再經交感路徑影響松果體。geniculate ganglion 屬顏面神經感覺節，不在此路徑上。",
        "notes": {
            "A": "retinohypothalamic tract 把光暗訊號送到視交叉上核，受損會影響 melatonin 節律。",
            "B": "geniculate ganglion 是顏面神經感覺節，與松果體褪黑激素節律路徑無直接關係，最不可能影響。",
            "C": "松果體分泌細胞受損會直接影響 melatonin 生成。",
            "D": "N-acetyltransferase 是 melatonin 合成的重要酵素，受抑制會影響夜間濃度變化。",
        },
        "core": "Melatonin 節律需要視網膜、SCN、交感路徑與松果體；geniculate ganglion 不屬此路徑。",
    },
    53: {
        "analysis": "漸進電位可隨刺激強度改變，有時間與空間加成，可去極化或過極化；但它會隨距離衰減，不像動作電位能不衰減傳導。",
        "notes": {
            "A": "漸進電位可以進行時間加成與空間加成，敘述正確。",
            "B": "漸進電位幅度與刺激大小相關，刺激越強可產生越大電位變化。",
            "C": "漸進電位可能是 EPSP 型去極化，也可能是 IPSP 型過極化。",
            "D": "漸進電位屬被動電流傳播，會隨距離衰減；不衰減是動作電位特性，故 D 錯。",
        },
        "core": "Graded potential 可加成、幅度可變、可正可負，但會隨距離衰減。",
    },
    54: {
        "analysis": "Benzodiazepines 結合 GABA_A receptor 上的 BZD site，增強 GABA 造成的氯離子通道開啟頻率，產生鎮靜與助眠效果。",
        "notes": {
            "A": "多巴胺受體不是 BZD 的助眠作用標的。",
            "B": "麩胺酸是主要興奮性傳遞物質，BZD 不作用於 glutamate receptor 的 BZD site。",
            "C": "GABA_A receptor 具有 benzodiazepine binding site，BZD 增強 GABA 抑制作用，故正確。",
            "D": "甘胺酸也是抑制性傳遞物質，但不是 BZD 的典型受體標的。",
        },
        "core": "BZD 作用於 GABA_A receptor 的 benzodiazepine site，增強 GABAergic inhibition。",
    },
    55: {
        "analysis": "平滑肌收縮的鈣訊號不是透過 troponin，而是 Ca2+ 結合 calmodulin，活化 MLCK，使 myosin light chain 磷酸化後促進收縮。",
        "notes": {
            "A": "Troponin 是骨骼肌與心肌鈣調控的重要蛋白，平滑肌缺乏典型 troponin 調控。",
            "B": "Tropomyosin 參與肌絲調控，但不是平滑肌 Ca2+ 的主要結合蛋白。",
            "C": "Ca2+ 在平滑肌主要先結合 calmodulin，再啟動 MLCK，故正確。",
            "D": "Myosin light chain 是 MLCK 的磷酸化目標，不是 Ca2+ 直接結合的主要感受蛋白。",
        },
        "core": "平滑肌：Ca2+ 結合 calmodulin，活化 MLCK，磷酸化 myosin light chain。",
    },
    56: {
        "analysis": "Dynamic gamma motor neuron 支配肌梭內梭肌，特別提高肌梭對快速伸長與長度變化的敏感度，使牽張反射更靈敏。",
        "notes": {
            "A": "興奮 dynamic gamma neuron 不會使肌張力反射性降低；它會提高肌梭敏感度。",
            "B": "dynamic gamma 活化會增加肌梭對骨骼肌長度變化，尤其快速伸長的敏感度，故正確。",
            "C": "牽張反射不會消失，反而因肌梭傳入較敏感而較容易被調節。",
            "D": "dynamic gamma neuron 直接調整肌梭敏感性，不會完全無影響。",
        },
        "core": "Dynamic gamma motor neuron 增加肌梭對肌肉長度變化的敏感度。",
    },
    57: {
        "analysis": "惡性貧血多因內在因子缺乏造成 vitamin B12 吸收不良，引起巨球性貧血與可能神經症狀，治療重點是補充 B12。",
        "notes": {
            "A": "維生素 A 與視覺、上皮分化相關，不是惡性貧血的主要缺乏營養素。",
            "B": "惡性貧血是 vitamin B12 吸收障礙造成，補充 B12 最能改善症狀，故正確。",
            "C": "維生素 D 主要調節鈣磷與骨代謝，不治療惡性貧血主因。",
            "D": "維生素 K 參與凝血因子活化，與惡性貧血的巨球性貧血機轉不同。",
        },
        "core": "Pernicious anemia 來自 intrinsic factor 缺乏導致 B12 吸收不良，治療補充 vitamin B12。",
    },
    58: {
        "analysis": "第一心音 S1 到第二心音 S2 之間是心室收縮期，包含等容收縮與射血期；射血期心室容積快速下降。",
        "notes": {
            "A": "心房去極化對應 P wave，發生在心室收縮前，不是在 S1 到 S2 的主要事件。",
            "B": "S1 到 S2 之間有心室射血，心室容積快速下降，故正確。",
            "C": "心房壓力會有波動，但不是此期間最具代表性的主要生理變化。",
            "D": "心室壓力在等容收縮上升、射血期變化，並非維持不變。",
        },
        "core": "S1 到 S2 是心室收縮與射血期，心室容積下降。",
    },
    59: {
        "analysis": "慢性中度貧血降低血液攜氧量，身體常以增加心輸出量代償，以維持組織氧輸送。",
        "notes": {
            "A": "慢性貧血可造成高輸出狀態，心跳與心輸出量代償上升，故最可能增加 cardiac output。",
            "B": "心肌梗塞損害收縮功能，通常降低而非增加心輸出量。",
            "C": "心肌炎造成心肌發炎與收縮功能下降，不利於心輸出量增加。",
            "D": "靜脈順應性增加會讓血液滯留於靜脈，降低回心血量與前負荷，通常不增加心輸出量。",
        },
        "core": "慢性貧血可因氧輸送不足而代償性增加心輸出量。",
    },
    60: {
        "analysis": "大失血造成血壓下降時，壓力感受器反射會增加交感、降低副交感，以提升心跳、收縮力、靜脈回流與周邊阻力。",
        "notes": {
            "A": "副交感活性增加會降低竇房結心跳速率，不會使心跳變快；此敘述方向相反，最不可能發生。",
            "B": "交感刺激心室可增加收縮力，有助維持 stroke volume 與血壓。",
            "C": "交感刺激靜脈收縮可增加靜脈回流與舒張末期容積，是典型代償。",
            "D": "交感刺激微動脈收縮可增加總周邊阻力，有助拉回血壓。",
        },
        "core": "失血低血壓反射：交感上升、副交感下降，心跳收縮力與周邊阻力增加。",
    },
    61: {
        "analysis": "冠狀動脈受局部代謝調控很強。Adenosine、NO 與心肌代謝率上升都促進舒張；心跳變慢使耗氧下降，代謝性舒張訊號減少，較可能相對收縮。",
        "notes": {
            "A": "adenosine 是冠脈強力局部舒張因子，濃度增加會擴張而非收縮。",
            "B": "心跳速率減慢使心肌耗氧與代謝產物下降，冠脈局部舒張驅動降低，最可能造成相對收縮。",
            "C": "nitric oxide 會活化 cGMP 路徑造成血管平滑肌舒張，不會引起收縮。",
            "D": "心臟代謝率增加會產生更多代謝性舒張因子，使冠狀動脈擴張以增加供血。",
        },
        "core": "冠脈血流主要隨心肌代謝需求調整；代謝需求下降時冠脈較可能收縮。",
    },
    62: {
        "analysis": "吸入空氣的氧分壓最高；肺泡氣因持續與血液交換並含二氧化碳，氧分壓較低；呼出氣混合了解剖死腔空氣與肺泡氣，因此介於兩者之間。",
        "notes": {
            "A": "呼出氣不是最低，因為它混合了未參與氣體交換的死腔空氣，氧分壓高於純肺泡氣。",
            "B": "inspired air > expired air > alveolar air 符合死腔混合與肺泡氣交換後氧分壓較低的邏輯，故正確。",
            "C": "吸入氣與肺泡氣不相等；肺泡氣氧分壓因交換與 CO2 存在而較低。",
            "D": "呼出氣與肺泡氣不相等，呼出氣混有死腔空氣，所以氧分壓較高。",
        },
        "core": "氧分壓排序：吸入氣 > 呼出氣 > 肺泡氣。",
    },
    63: {
        "analysis": "CO2 可穿過血腦障壁刺激中樞化學感受器；題目給的碳酸酐酶抑制劑無法穿過血腦障壁，因此兩組中樞化學感受器所受直接影響相同。",
        "notes": {
            "A": "周邊碳酸酐酶被抑制會影響 CO2/H+ 轉換與周邊化學感受器反應，兩組肺泡通氣量不一定相同。",
            "B": "實驗組周邊化學感受器未必更強；碳酸酐酶受抑制通常會減慢局部 H+ 生成，不能穩定判為更強。",
            "C": "舌咽神經主要傳遞頸動脈體訊號，題幹選項談控制組較低並不符合周邊藥物效應的穩定判斷。",
            "D": "藥物不進入中樞，CO2 仍可進入腦脊髓液，因此兩組 central chemoreceptor 活性相同是最穩定答案。",
        },
        "core": "不能穿過血腦障壁的碳酸酐酶抑制劑不直接改變中樞化學感受器反應。",
    },
    64: {
        "analysis": "Secretin 由十二指腸 S cells 受酸刺激分泌，作用於胰臟管細胞與膽道上皮，促進 bicarbonate-rich fluid 分泌以中和胃酸。",
        "notes": {
            "A": "secretin 刺激 pancreatic duct cells 分泌 HCO3-，協助十二指腸酸鹼中和，敘述正確。",
            "B": "secretin 不是胰臟製造，也不是促進胃酸分泌；它通常抑制胃酸並促進中和。",
            "C": "secretin 主要經 Gs/cAMP 促進 bicarbonate 分泌，不是抑制 Gq 以促進胃酸。",
            "D": "氯離子通道可參與分泌液電解質運作，但此選項未指出 secretin 的主要標的與 bicarbonate 分泌，不如 A 完整。",
        },
        "core": "Secretin 由十二指腸 S cells 分泌，刺激胰管 HCO3- 分泌來中和胃酸。",
    },
    65: {
        "analysis": "小腸吸收單醣：glucose 與 galactose 由頂端膜 SGLT1 伴隨 Na+ 吸收；fructose 由 GLUT5；lactose 必須先被 lactase 分解。",
        "notes": {
            "A": "小腸 glucose 主要走 SGLT1；SGLT2 主要在腎近曲小管負責葡萄糖再吸收。",
            "B": "fructose 主要由 GLUT5 吸收；GLUT4 是胰島素敏感的肌肉與脂肪細胞轉運蛋白。",
            "C": "galactose 與 glucose 一樣主要經 SGLT1 與 Na+ 共同運輸進入腸細胞，故正確。",
            "D": "lactose 是雙醣，需先分解為 glucose 與 galactose；GLUT5 吸收的是 fructose。",
        },
        "core": "小腸：glucose/galactose 用 SGLT1，fructose 用 GLUT5，lactose 先消化再吸收。",
    },
    66: {
        "analysis": "Henle loop 上行粗支的頂端膜主要使用 Na+-K+-2Cl- cotransporter 進行鈉再吸收，這也是 loop diuretics 的抑制標的。",
        "notes": {
            "A": "Na+-K+-2Cl- cotransporter（NKCC2）位於上行粗支頂端膜，是本題正確答案。",
            "B": "Na+-glucose cotransporter 主要在近曲小管回收葡萄糖，不是上行粗支主力。",
            "C": "Na+-phosphate cotransporter 主要在近曲小管參與磷酸鹽再吸收。",
            "D": "Na+-Cl- cotransporter 是遠曲小管代表轉運子，為 thiazide 類利尿劑標的。",
        },
        "core": "上行粗支 apical Na+ 再吸收主力是 NKCC2；遠曲小管是 NCC。",
    },
    67: {
        "analysis": "限水會提高血漿滲透壓，刺激 ADH 分泌；ADH 增加集合管水通透性，使水回收增加、尿液濃縮，尿滲透壓上升。",
        "notes": {
            "A": "限水後 ADH 上升且尿液被濃縮，尿滲透壓與血漿 ADH 都增加，故正確。",
            "B": "ADH 增加會讓尿液濃縮，不會使尿滲透壓下降。",
            "C": "尿滲透壓雖會增加，但 ADH 不會減少；限水會刺激 ADH 分泌。",
            "D": "限水不是水負荷狀態，不會讓尿滲透壓與 ADH 同時下降。",
        },
        "core": "限水使 ADH 上升，集合管回收水增加，尿液滲透壓上升。",
    },
    68: {
        "analysis": "腎上腺網狀帶分泌 DHEA、DHEAS 等 androgen，主要受 ACTH 影響；gonadotropins 主要調控性腺，不是腎上腺雄性素主調控。",
        "notes": {
            "A": "腎上腺雄性素主要受 ACTH 調控，而非 LH/FSH 等 gonadotropins，因此此敘述最不適當。",
            "B": "DHEAS 常在年輕成人約 20 歲左右達高峰，之後隨年齡下降，敘述可接受。",
            "C": "青春期前男孩若腎上腺 androgen 過多，可造成假性性早熟或男性化表現。",
            "D": "成年女性 androgen 過多可造成多毛、痤瘡、月經異常等腎上腺性徵異常表現。",
        },
        "core": "腎上腺 androgen 主要受 ACTH 調控；gonadotropins 主要調控性腺。",
    },
    69: {
        "analysis": "急性壓力同時啟動 HPA axis 與交感-腎上腺髓質系統，使 ACTH、glucocorticoid 與 catecholamines 相關反應上升。",
        "notes": {
            "A": "壓力刺激會增加 CRH/ACTH，並同步活化交感神經，是最完整正確的敘述。",
            "B": "對兒茶酚胺心血管作用具有 permissive action 的主要是 glucocorticoids，不是 ACTH 本身。",
            "C": "脂肪分解在急性壓力中主要受 catecholamines 等快速訊號驅動；glucocorticoid 不是唯一或主要即刻原因。",
            "D": "交感神經是急性壓力反應核心，切除後不可能保有完整壓力反應。",
        },
        "core": "急性壓力會同時啟動 HPA axis 與交感神經；glucocorticoids 對 catecholamines 有 permissive effect。",
    },
    70: {
        "analysis": "甲狀腺素促進心臟對兒茶酚胺反應、促進腦發育並增加脂肪分解；過量時在肌肉常造成蛋白分解與肌肉消耗。",
        "notes": {
            "A": "甲狀腺素會增加 beta-adrenergic responsiveness，使心臟對兒茶酚胺反應上升，正確。",
            "B": "甲狀腺素過多時常增加肌肉蛋白分解，造成肌無力與消耗；概括為增加蛋白質合成最不恰當。",
            "C": "甲狀腺素對胎兒與嬰幼兒中樞神經發育很重要，敘述正確。",
            "D": "甲狀腺素可促進脂肪分解與基礎代謝，敘述正確。",
        },
        "core": "甲狀腺素促進代謝與兒茶酚胺反應；過量時肌肉偏分解而非單純合成。",
    },
    71: {
        "analysis": "低血鈣會刺激 PTH 分泌，促進腎臟保鈣並增加腎臟 1-alpha hydroxylase 活性，使 1,25-(OH)2D3 增加，進而增加腸鈣吸收。",
        "notes": {
            "A": "低血鈣會刺激副甲狀腺素分泌增加，是正確代償。",
            "B": "1,25-(OH)2D3 主要由腎臟活化生成；肝臟主要做 25-hydroxylation，因此說肝臟分泌增加最不恰當。",
            "C": "PTH 會增加腎小管鈣再吸收，使尿鈣排泄減少，屬低血鈣代償。",
            "D": "活性維生素 D 增加會促進小腸鈣吸收，屬低血鈣後續代償。",
        },
        "core": "低血鈣刺激 PTH；活性維生素 D 的 1-alpha hydroxylation 主要在腎臟，不是肝臟。",
    },
    72: {
        "analysis": "胰島素分泌主要受血糖調控，也受 incretin、迷走神經與部分胰島激素影響。副交感神經通常促進進食期胰島素分泌，不是抑制。",
        "notes": {
            "A": "副交感迷走神經活化會促進胰島素分泌；說會抑制是錯誤敘述。",
            "B": "血糖濃度是 beta cell 胰島素分泌最主要調控因子，正確。",
            "C": "GLP-1 在高血糖時增強 glucose-dependent insulin secretion，正確。",
            "D": "glucagon 可透過胰島內 paracrine 或血糖相關機制促進胰島素分泌，敘述可接受。",
        },
        "core": "胰島素分泌主軸是血糖；副交感與 GLP-1 通常促進胰島素分泌。",
    },
    73: {
        "analysis": "透明帶包覆 secondary oocyte、zygote 與 morula，可避免過早著床；囊胚著床前會 hatch，脫離透明帶。",
        "notes": {
            "A": "secondary oocyte 仍有 zona pellucida 包覆，並參與精卵辨識與防止多精入卵。",
            "B": "zygote 仍在透明帶內進行早期卵裂。",
            "C": "morula 仍被 zona pellucida 包覆，以避免輸卵管異位著床。",
            "D": "囊胚著床前已脫離透明帶；implanted blastocyst 不再有 zona pellucida，故正確。",
        },
        "core": "透明帶存在於卵母細胞到 morula；囊胚著床前會 hatch 而消失。",
    },
    74: {
        "analysis": "競爭性抑制劑與受質競爭活性位，增加達到半最大速率所需受質濃度，所以表觀 KM 上升；高受質濃度可克服抑制，Vmax 不變。",
        "notes": {
            "A": "競爭性抑制不降低 Vmax，也不降低 KM，此組合錯誤。",
            "B": "Vmax 不變正確，但 KM 應上升而非下降。",
            "C": "KM 上升正確，但 Vmax 不會下降；Vmax 下降較像非競爭性抑制。",
            "D": "competitive inhibition 的典型變化是 Vmax 不變、KM 上升，故正確。",
        },
        "core": "Competitive inhibitor：Vmax 不變，apparent KM 上升。",
    },
    75: {
        "analysis": "Alpha helix 主要由多肽主鏈內的氫鍵穩定，通常是第 i 個殘基 C=O 與第 i+4 個殘基 N-H 之間形成氫鍵。",
        "notes": {
            "A": "α 碳之間的疏水作用不是 α 螺旋主要穩定來源。",
            "B": "α 螺旋由胜肽主幹 C=O 與 N-H 之間規則氫鍵穩定，故正確。",
            "C": "側鏈靜電作用可影響螺旋傾向，但不是主要普遍穩定因素。",
            "D": "側鏈氫鍵可能局部影響結構，但 α 螺旋的核心穩定來自主幹氫鍵。",
        },
        "core": "α-helix 的主要穩定力是 peptide backbone 內部氫鍵。",
    },
    76: {
        "analysis": "EC 傳統六大酵素類別是 oxidoreductases、transferases、hydrolases、lyases、isomerases、ligases；dehydrogenase 是氧化還原酶中的一類酵素名稱，不是大類。",
        "notes": {
            "A": "lyases 是 EC 六大類之一，屬於裂解或加成反應相關酵素。",
            "B": "dehydrogenases 是具體酵素族群，歸在 oxidoreductases 之下，不是 EC 六大類名稱，故正確。",
            "C": "hydrolases 是 EC 六大類之一，催化水解反應。",
            "D": "isomerases 是 EC 六大類之一，催化異構化反應。",
        },
        "core": "EC 六大類沒有 dehydrogenases；它屬 oxidoreductases 的具體酵素族。",
    },
    77: {
        "analysis": "Lipoate 在 pyruvate dehydrogenase complex 中以 lipoamide 連到 E2 lysine，接受 hydroxyethyl 與乙醯基，再把 acetyl group 轉給 CoA；還原型 lipoamide 由 E3/FAD/NAD+ 再氧化。",
        "notes": {
            "A": "lipoate 的再氧化使用 FAD 與 NAD+，不是 NADP；且流程描述把氧化來源寫錯，因此為錯誤敘述。",
            "B": "lipoate 以 amide linkage 接在 dihydrolipoyl transacetylase（E2）的 lysine 上，敘述正確。",
            "C": "lipoamide 作為 acyl group carrier，將 acetyl group 轉移給 CoA 形成 acetyl-CoA，正確。",
            "D": "氧化型 lipoamide 可接受 hydroxyethyl-TPP 來的乙醯基與電子，敘述符合 PDH 流程。",
        },
        "core": "PDH lipoamide 連在 E2 lysine；還原型 lipoamide 由 FAD/NAD+ 再氧化，不是 NADP。",
    },
    78: {
        "analysis": "Transaminases 需要 pyridoxal phosphate（PLP）作為輔酶，PLP 來自維生素 B6，可穩定胺基轉移反應中間產物。",
        "notes": {
            "A": "methylcobalamin 是維生素 B12 形式，主要參與甲基轉移，不是轉胺酶典型輔酶。",
            "B": "pyridoxal phosphate 是 transaminase 的核心輔酶，故正確。",
            "C": "folic acid 參與一碳單位代謝，不是轉胺酶活性中心輔酶。",
            "D": "thiamine pyrophosphate 常參與脫羧反應，例如 PDH，不是轉胺反應主輔酶。",
        },
        "core": "轉胺酶的輔酶是 PLP，來源為 vitamin B6。",
    },
    79: {
        "analysis": "ATP、GTP 等 nucleoside triphosphates 的能量主要儲存在相鄰磷酸基之間的磷酸酐鍵，水解可釋放自由能。",
        "notes": {
            "A": "phosphoanhydride bonds 是核苷三磷酸攜帶與傳遞能量的關鍵鍵結，故正確。",
            "B": "phosphodiester bonds 是核酸糖磷酸骨架的連結，不是 ATP 高能磷酸鍵。",
            "C": "glycosidic bond 連接糖與鹼基，不是主要能量傳遞鍵。",
            "D": "氫鍵參與鹼基配對等非共價作用，不是 NTP 儲能的主要形式。",
        },
        "core": "NTP 的高能鍵是磷酸基之間的 phosphoanhydride bonds。",
    },
    80: {
        "analysis": "Topoisomerase 透過暫時切開與重新連接 DNA，改變 DNA supercoiling，解除複製與轉錄時的扭轉張力。",
        "notes": {
            "A": "改變 DNA supercoil 是 topoisomerase 的主要功能，故正確。",
            "B": "鹼基配對專一性由 A-T、G-C 配對與聚合酶選擇性決定，不是拓樸異構酶功能。",
            "C": "topoisomerase 不負責增加或減少 DNA 核苷酸數目。",
            "D": "DNA 與 RNA 置換不是 topoisomerase 的功能；這涉及轉錄或核酸雜合處理。",
        },
        "core": "Topoisomerase 改變 DNA 超螺旋，解除複製與轉錄造成的扭轉壓力。",
    },
    81: {
        "analysis": "Base excision repair 的第一步是 DNA glycosylase 辨識異常或受損鹼基並切斷 N-glycosidic bond，形成 AP site。",
        "notes": {
            "A": "DNA glycosylase 是 BER 的第一個關鍵酵素，先移除受損鹼基，故正確。",
            "B": "AP endonuclease 在 AP site 形成後才切開 DNA 骨架，不是第一步。",
            "C": "DNA ligase 在修補末端負責封合缺口，屬後期步驟。",
            "D": "Dam methylase 與細菌錯配修復中新舊股辨識相關，不是 BER 第一酵素。",
        },
        "core": "BER 第一酵素是 DNA glycosylase，先移除受損鹼基形成 AP site。",
    },
    82: {
        "analysis": "Klenow fragment 是 E. coli DNA polymerase I 去掉 N 端 5'→3' exonuclease 小片段後留下的大型 C 端片段，保留 polymerase 與 3'→5' proofreading 活性。",
        "notes": {
            "A": "Klenow fragment 保有 DNA polymerase 活性，敘述正確。",
            "B": "5'→3' exonuclease 活性位於被移除的 N 端片段，因此 Klenow fragment 不具有此活性，這是錯誤敘述。",
            "C": "Klenow fragment 是 polymerase C-terminal 的大片段，敘述正確。",
            "D": "Klenow fragment 保留 3'→5' exonuclease proofreading 活性，敘述正確。",
        },
        "core": "Klenow fragment 保留 polymerase 與 3'→5' exonuclease，缺少 5'→3' exonuclease。",
    },
    83: {
        "analysis": "Ras 需要脂質修飾才能穩定附著於細胞膜。其 C 端 CAAX motif 常經 prenylation（如 farnesylation）增加疏水性並定位到膜上。",
        "notes": {
            "A": "ubiquitination 多與蛋白降解或訊號調控相關，不是 Ras 典型膜定位修飾。",
            "B": "acetylation 常影響染色質或蛋白功能調控，不是 Ras 結合膜的主要機制。",
            "C": "adenylation 不是 Ras 膜定位的標準修飾。",
            "D": "prenylation 讓 Ras 取得疏水性脂質尾端以附著細胞膜，故正確。",
        },
        "core": "Ras 經 prenylation 取得膜定位能力。",
    },
    84: {
        "analysis": "原核 RNA polymerase holoenzyme 的 sigma subunit 主要負責 initiation 時辨識 promoter；進入 elongation 後，核心酶 alpha、beta、beta prime 才是主要執行者。",
        "notes": {
            "A": "alpha subunit 屬核心酶成分，在轉錄延伸中仍屬酶複合體的一部分。",
            "B": "beta subunit 參與 RNA 合成催化，是延伸期核心成分。",
            "C": "beta prime subunit 參與 DNA template 結合，是核心酶重要成分。",
            "D": "sigma subunit 主要在起始辨識 promoter，延伸期多脫離或參與最少，故正確。",
        },
        "core": "細菌 sigma factor 主責 promoter recognition/initiation，elongation 時參與最少。",
    },
    85: {
        "analysis": "Wobble 題要注意 anticodon 與 codon 方向相反。tRNAArg anticodon 5'-ICG 可和 arginine codon 5'-CGA 配對，且 inosine 在 wobble 位置可增加辨識彈性。",
        "notes": {
            "A": "5'-CGA 是 arginine codon，能與 5'-ICG anticodon 依方向性與 wobble 規則配對，故正確。",
            "B": "5'-AGC 不是此 tRNAArg 對應的 CGN 類 arginine codon，且配對方向不符。",
            "C": "5'-UGC 是 cysteine codon，不是 arginine codon。",
            "D": "5'-GGC 是 glycine codon，不是 arginine codon。",
        },
        "core": "Anticodon 要反向讀取配對；5'-ICG 可辨識 arginine codon 5'-CGA。",
    },
    86: {
        "analysis": "真核細胞 RNA polymerase 分工：Pol I 轉錄 45S pre-rRNA，產生 18S、5.8S、28S rRNA；Pol III 負責 5S rRNA 與 tRNA。",
        "notes": {
            "A": "RNA polymerase I 負責 18S 與 28S rRNA 的前驅轉錄，故正確。",
            "B": "RNA polymerase II 主要轉錄 mRNA 與部分 snRNA，不是 18S/28S rRNA 主力。",
            "C": "RNA polymerase III 轉錄 tRNA 與 5S rRNA，不轉錄 18S 與 28S。",
            "D": "ribosomal RNase 不是合成 rRNA 的聚合酶。",
        },
        "core": "Pol I 產生 18S、5.8S、28S rRNA；Pol III 產生 5S rRNA 與 tRNA。",
    },
    87: {
        "analysis": "無氧糖解中，每 1 mole glucose 淨產生 2 ATP；產生的 NADH 會在 lactate dehydrogenase 反應中把 pyruvate 還原為 lactate，同時再生 NAD+，所以不淨保留 NADH。",
        "notes": {
            "A": "糖解每葡萄糖淨 ATP 是 2，不是 1。",
            "B": "無氧轉成 2 mole lactate 後，淨能量為 2 mole ATP，故正確。",
            "C": "NADH 在 lactate dehydrogenase 反應中被消耗再生 NAD+，不淨保留 2 mole NADH。",
            "D": "ATP 兩莫耳正確，但 NADH 不會淨產生兩莫耳，因此此選項錯誤。",
        },
        "core": "無氧糖解：1 glucose 到 2 lactate，淨產生 2 ATP，NADH 被用來再生 NAD+。",
    },
    88: {
        "analysis": "飲食澱粉 amylose 與 amylopectin 先被 amylase 分解成 maltose、maltotriose 與 limit dextrins，刷狀緣再分解成 glucose；選項中最符合消化產物的是 glucose 與 maltose。",
        "notes": {
            "A": "glucose 與 maltose 是澱粉腸道消化過程中合理產物，故正確。",
            "B": "glucose-1-phosphate 是細胞內代謝中間物，不是腸道澱粉水解主要產物。",
            "C": "maltose 可出現，但 glucose-1-phosphate 不屬腸腔消化產物。",
            "D": "glucose-6-phosphate 是細胞內磷酸化葡萄糖，不是消化道水解產物。",
        },
        "core": "澱粉消化產物以 maltose、maltotriose、limit dextrins 到 glucose 為主，不產生 phosphorylated glucose。",
    },
    89: {
        "analysis": "醣蛋白鍵結常考 N-linked 與 O-linked。N-linked glycosylation 接在 asparagine；O-linked 常接在 serine 或 threonine。",
        "notes": {
            "A": "asparagine、serine、threonine 分別涵蓋 N-linked 與 O-linked 常見醣基連接位點，故正確。",
            "B": "cysteine、aspartate、glutamate 不是典型醣蛋白醣鏈連接組合。",
            "C": "serine 可參與 O-linked，但 glutamine 與 arginine 不是典型主要連接位點。",
            "D": "threonine 可參與 O-linked，但 aspartate 與 arginine 不是常見主要醣基接點。",
        },
        "core": "Glycoprotein 常見連接殘基：N-linked 到 Asn，O-linked 到 Ser/Thr。",
    },
    90: {
        "analysis": "膽鹽由膽固醇衍生，速率決定步驟由 cholesterol 7-alpha hydroxylase 催化，且具兩親性，可乳化脂質促進吸收；說它是非極性分子是錯的。",
        "notes": {
            "A": "cholesterol 7-alpha hydroxylase 是膽酸合成速率決定步驟，敘述正確。",
            "B": "膽鹽是兩親性分子，不是單純非極性；此敘述把分子特性說錯，故為答案。",
            "C": "膽酸合成涉及 cytochrome P450 酵素系統，敘述正確。",
            "D": "膽鹽由膽固醇衍生，合成與膽固醇供應及調控有關，敘述可接受。",
        },
        "core": "膽鹽是 cholesterol 衍生的兩親性分子，可乳化脂質；不是非極性分子。",
    },
    91: {
        "analysis": "Gaucher disease 是 lysosomal storage disorder，因 glucocerebrosidase 缺乏造成 glucocerebroside 累積；glucocerebroside 屬 sphingolipid。",
        "notes": {
            "A": "glycogen 代謝異常對應 glycogen storage diseases，不是 Gaucher disease。",
            "B": "choline 不是 Gaucher disease 累積物或主要代謝類別。",
            "C": "Gaucher disease 是 sphingolipid 代謝異常，故正確。",
            "D": "N-acetylglutamate 與尿素循環調控相關，不是 Gaucher disease 的核心物質。",
        },
        "core": "Gaucher disease 是 glucocerebrosidase 缺乏造成的 sphingolipid storage disease。",
    },
    92: {
        "analysis": "脂肪酸 omega-oxidation 主要在內質網，尤其肝臟 microsomal system；它氧化脂肪酸 omega 端，和粒線體 beta-oxidation 不同。",
        "notes": {
            "A": "細胞核負責 DNA/RNA 相關功能，不是脂肪酸 omega-oxidation 主要位置。",
            "B": "粒線體是 beta-oxidation 主場所，不是 omega-oxidation 主要位置。",
            "C": "高基氏體負責蛋白與脂質加工運輸，不是 omega-oxidation 主場所。",
            "D": "omega-oxidation 主要在內質網進行，故正確。",
        },
        "core": "脂肪酸 beta-oxidation 在粒線體；omega-oxidation 主要在內質網。",
    },
    93: {
        "analysis": "Glutamate 可轉為 glutamate semialdehyde，進一步和 proline、ornithine、arginine 代謝互通，因此是 proline 與 arginine 的重要來源。",
        "notes": {
            "A": "glutamate 可經共同中間產物連到 proline 與 arginine 生成路徑，故正確。",
            "B": "tryptophan 主要與 serotonin、niacin 等代謝相關，不是 proline/arginine 主來源。",
            "C": "valine 是支鏈胺基酸，不是 proline 或 arginine 的主要前驅物。",
            "D": "methionine 主要與 methyl group、SAM 與 sulfur amino acid 代謝相關，不是本題主來源。",
        },
        "core": "Proline 與 arginine 可由 glutamate 路徑衍生。",
    },
    94: {
        "analysis": "Leucine 與 lysine 是純生酮胺基酸，代謝產物偏向 acetyl-CoA 或 acetoacetate；飢餓時過度代謝最容易增加酮體生成。",
        "notes": {
            "A": "leucine 是純 ketogenic amino acid，過度代謝容易促進 ketosis，故正確。",
            "B": "methionine 是 glucogenic amino acid，不是最典型導致酮症的胺基酸。",
            "C": "arginine 屬 glucogenic，不是純生酮胺基酸。",
            "D": "glutamate 可進入 TCA cycle 成為 alpha-ketoglutarate，偏 glucogenic，不是本題答案。",
        },
        "core": "純生酮胺基酸是 leucine 與 lysine；本題選 leucine。",
    },
    95: {
        "analysis": "電子傳遞鏈 complex IV 是 cytochrome c oxidase，負責把電子從 cytochrome c 傳給氧，形成水。",
        "notes": {
            "A": "NADH dehydrogenase 是 complex I，不是 complex IV。",
            "B": "cytochrome oxidase 即 complex IV，負責氧作為最終電子接受者的步驟，故正確。",
            "C": "succinate dehydrogenase 是 complex II，也屬 TCA cycle 酵素。",
            "D": "ubiquinone:cytochrome c oxidoreductase 是 complex III，不是 complex IV。",
        },
        "core": "ETC：I NADH dehydrogenase、II succinate dehydrogenase、III cytochrome bc1、IV cytochrome c oxidase。",
    },
    96: {
        "analysis": "Calmodulin 是典型 Ca2+-binding protein，主要藉 EF-hand motif/domain 結合鈣離子，之後調節下游酵素與訊號傳遞。",
        "notes": {
            "A": "EF hand domain 是 calmodulin 結合 Ca2+ 的典型結構，故正確。",
            "B": "SH2 domain 主要辨識 phosphotyrosine，不是 Ca2+ 結合結構。",
            "C": "PTB domain 與特定 phosphotyrosine 或蛋白序列辨識相關，不是 calmodulin 鈣結合位點。",
            "D": "PH domain 多與 phosphoinositides 膜定位相關，不是 Ca2+ 結合主結構。",
        },
        "core": "Calmodulin 以 EF-hand motif 結合 Ca2+。",
    },
    97: {
        "analysis": "ANF/ANP 作用於具有 guanylyl cyclase 活性的受體，使 cGMP 增加；相較之下 glucagon 常走 Gs-cAMP，dopamine 與 serotonin 也有可影響 cAMP 的受體亞型。",
        "notes": {
            "A": "ANF 的主要 second messenger 是 cGMP，不是 cAMP，故是本題答案。",
            "B": "glucagon 典型透過 Gs 活化 adenylyl cyclase，使 cAMP 上升。",
            "C": "dopamine 受體中 D1-like 可增加 cAMP，D2-like 可降低 cAMP，因此與 cAMP 訊號有關。",
            "D": "serotonin 有多種受體亞型，其中部分經 G protein 影響 cAMP，不如 ANF 明確排除 cAMP。",
        },
        "core": "ANF/ANP 主要透過 guanylyl cyclase receptor 產生 cGMP。",
    },
    98: {
        "analysis": "Catecholamines 的生合成從 tyrosine 開始，依序形成 DOPA、dopamine、norepinephrine，最後可形成 epinephrine。",
        "notes": {
            "A": "asparagine 不是 catecholamine 合成路徑的前驅物。",
            "B": "glutamate 是興奮性神經傳遞物與多種胺基酸代謝中間，但不是兒茶酚胺前驅物。",
            "C": "arginine 與 NO、尿素循環等相關，不是 catecholamine 主要前驅物。",
            "D": "tyrosine 是 catecholamine hormones 的經典前驅物，故正確。",
        },
        "core": "Catecholamine 合成路徑：tyrosine -> DOPA -> dopamine -> norepinephrine -> epinephrine。",
    },
    99: {
        "analysis": "限制酶常辨識 DNA palindrome，也就是雙股 DNA 以相反方向讀取時呈現互補對稱。GCTAGC 的 reverse complement 仍為 GCTAGC。",
        "notes": {
            "A": "CCCCCC 的互補股為 GGGGGG，反向互補不等於原序列，不是典型限制酶 palindrome。",
            "B": "AGCAGC 的 reverse complement 為 GCTGCT，與原序列不同。",
            "C": "TAGGAT 的 reverse complement 為 ATCCTA，與原序列不同。",
            "D": "GCTAGC 的 reverse complement 仍為 GCTAGC，符合迴文序列，故正確。",
        },
        "core": "DNA palindrome 要看 reverse complement 是否與原序列相同；GCTAGC 符合。",
    },
    100: {
        "analysis": "一般 PCR 是以 DNA 模板擴增 DNA，必備核心包含 template DNA、primers、耐熱 DNA polymerase 與 dNTPs；reverse transcriptase 是 RNA 反轉錄成 cDNA 的 RT-PCR 才需要。",
        "notes": {
            "A": "DNA template 是一般 PCR 擴增的模板，屬必要成分。",
            "B": "primer 提供 DNA polymerase 延伸起點，屬 PCR 必要成分。",
            "C": "DNA polymerase 負責延伸新股 DNA，屬 PCR 必要成分。",
            "D": "reverse transcriptase 用於 RNA 先轉成 cDNA 的 RT-PCR，不是一般 PCR 必需物質，故正確。",
        },
        "core": "一般 PCR 需要 DNA template、primers、DNA polymerase 與 dNTPs；reverse transcriptase 是 RT-PCR 才需要。",
    },
}


def make_update(question, item):
    qnum = question["question_number"]
    notes = item["notes"]
    explanation = (
        "【題幹解析】\n"
        f"{item['analysis']}\n\n"
        "【選項詳解】\n"
        f"- A. {notes['A']}\n"
        f"- B. {notes['B']}\n"
        f"- C. {notes['C']}\n"
        f"- D. {notes['D']}\n\n"
        "【核心考點】\n"
        f"{item['core']}"
    )
    key_point = item.get("key_point", item["core"])
    return {
        "question_id": question["id"],
        "question_number": qnum,
        "explanation": explanation,
        "key_point": key_point,
        "flashcard_front": question["question_text"].replace("\n", " ")[:80],
        "flashcard_back": key_point,
        "flashcard_summary": key_point,
        "review_status": "ai_generated",
        "explanation_model": "codex-high-quality-rewrite",
        "explanation_generated_at": STAMP,
        "manual_review_notes": item.get("manual_review_notes", []),
    }


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    exam = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8"))
    questions = {q["question_number"]: q for q in exam["questions"]}
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for start in range(31, 101, 10):
        end = min(start + 9, 100)
        updates = [make_update(questions[qnum], QDATA[qnum]) for qnum in range(start, end + 1)]
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates,
        }
        write_json(OUT_DIR / f"q{start:03d}-q{end:03d}.json", payload)


if __name__ == "__main__":
    main()
