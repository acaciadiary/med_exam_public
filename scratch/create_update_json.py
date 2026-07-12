import json
import os

target_dir = 'd:/Antigravity/med_exam_public/scratch/rewrite_updates/109-1_medicine-1'
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, 'q041-q050.json')

update_data = {
  "source_file": "public/data/exams/109-1/medicine-1.json",
  "dataset_id": "109-1_medicine-1",
  "range": { "start": 41, "end": 50 },
  "updates": [
    {
      "question_id": "109-1_medicine-1_041",
      "question_number": 41,
      "explanation": "【題幹解析】\n本題詢問第一型肺泡細胞（type-I pneumocyte）的結構與生理功能特點。第一型肺泡細胞是高度扁平的單層扁平上皮細胞，主要功能為與微血管共同構成氣體交換的薄膜構造。\n\n【選項詳解】\n- A. 錯誤。膜狀的層狀體（lamellar body）是第二型肺泡細胞（type-II pneumocyte）的特徵性胞器，其內含有表面活性物質（surfactant），釋放後可降低肺泡表面張力，防止肺泡塌陷。\n- B. 錯誤。在肺泡中負責吞噬灰塵、碳粒、細菌或紅血球等異物的是肺泡巨噬細胞（alveolar macrophage，又稱塵細胞 dust cell），而非第一型肺泡細胞。\n- C. 正確。第一型肺泡細胞極為扁平細薄，它與微血管內皮細胞（endothelial cell）以及兩者之間融合的基底膜共同組成氣血屏障（air-blood barrier），為肺部進行氣體交換的主要通道。\n- D. 錯誤。第一型肺泡細胞的數量約占肺泡上皮細胞總數的40%（第二型占約60%），但因其扁平延展的構造，覆蓋了高達95%的肺泡表面積，選項中的細胞比例與覆蓋面積比例剛好顛倒。\n\n【核心考點】\n第一型肺泡細胞（扁平、覆蓋95%面積、構成氣血屏障）與第二型肺泡細胞（立方、分泌表面活性物質、含層狀體）的組織學與功能鑑別。",
      "key_point": "第一型肺泡細胞為扁平上皮，與微血管內皮細胞組成氣血屏障；第二型肺泡細胞具層狀體並分泌表面活性物質。",
      "flashcard_front": "第一型肺泡細胞（type-I pneumocyte）之結構與功能特點",
      "flashcard_back": "第一型肺泡細胞為單層扁平上皮，與內皮細胞共組氣血屏障以進行氣體交換；其數量占40%但覆蓋95%表面積。第二型肺泡細胞則具層狀體，分泌表面活性物質。",
      "flashcard_summary": "第一型肺泡細胞 -> 與內皮細胞及基底膜組成氣血屏障，負責氣體交換；數量占40%但覆蓋95%表面積（第二型具層狀體分泌表面活性物質）。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_042",
      "question_number": 42,
      "explanation": "【題幹解析】\n本題詢問膽囊（gallbladder）黏膜內襯上皮的組織學分類。膽囊的主要生理功能為儲存與濃縮膽汁，其黏膜層具有許多高皺襞，且細胞表面有微絨毛以利於重吸收水分。\n\n【選項詳解】\n- A. 錯誤。移形上皮（transitional epithelium）分布於泌尿道系統（如腎盞、腎盂、輸尿管及膀胱），能隨著尿液積聚與排空而改變上皮層數與細胞形狀，不分布於膽囊。\n- B. 正確。膽囊的內襯上皮為單層柱狀上皮（simple columnar epithelium），細胞表面有許多微絨毛以進行密集的水分與電解質重吸收，從而達到濃縮膽汁的效果。\n- C. 錯誤。複層柱狀上皮（stratified columnar epithelium）在人體內極為罕見，僅分布於部分大腺體的排泄管（如唾液腺大導管）、結膜基底或男性尿道的部分區段，不構成膽囊內襯。\n- D. 錯誤。角質化複層扁平上皮（keratinized stratified squamous epithelium）主要構成皮膚的表皮層（epidermis），具有極佳的耐磨損與防止體液流失屏障功能，不適合作為膽囊的重吸收內襯。\n\n【核心考點】\n膽囊黏膜層的上皮組織學分類為單層柱狀上皮，其微絨毛結構具備重吸收水分以濃縮膽汁之生理功能。",
      "key_point": "膽囊的內襯上皮為單層柱狀上皮，利於濃縮膽汁。",
      "flashcard_front": "膽囊（gallbladder）的內襯上皮分類與功能",
      "flashcard_back": "膽囊內襯上皮為單層柱狀上皮，細胞游離面有豐富微絨毛，負責吸收水分與電解質以濃縮膽汁。",
      "flashcard_summary": "膽囊內襯上皮 -> 單層柱狀上皮，具微絨毛以利吸收水分與濃縮膽汁。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_043",
      "question_number": 43,
      "explanation": "【題幹解析】\n本題詢問正常胃黏膜層（mucosa）中不包含哪種細胞。胃黏膜上皮屬於單層柱狀上皮，含有多種特化分泌細胞以應對強酸性的消化環境，而小腸特有的細胞在正常胃黏膜中是不存在的。\n\n【選項詳解】\n- A. 錯誤。表面黏液細胞（surface mucous cell）位於胃黏膜最表面，能分泌富含碳酸氫根離子（HCO3-）的鹼性黏液，在胃黏膜表面形成一道「黏液-碳酸氫鹽屏障」，以防止胃酸及胃蛋白酶的自身消化。\n- B. 正確。杯狀細胞（goblet cell）是小腸和大腸黏膜的特徵性分泌細胞，正常胃黏膜中並不存在杯狀細胞。若在胃黏膜切片中觀察到杯狀細胞，臨床上診斷為「腸上皮化生（intestinal metaplasia）」，這是一種癌前病變，常與幽門螺幹菌慢性感染引發的萎縮性胃炎相關。\n- C. 錯誤。壁細胞（parietal cell，又稱 oxyntic cell）主要分布於胃底腺的中段，負責分泌胃酸（HCl，提供胃蛋白酶所需的強酸環境）及內在因子（intrinsic factor，與維生素 B12 結合以利於迴腸重吸收）。\n- D. 錯誤。未分化的成體幹細胞（undifferentiated adult stem cell）位於胃小凹（gastric pit）與胃腺交界處的頸部（isthmus），具有強大的分裂分化能力，可向上遷移分化為表面黏液細胞，或向下遷移分化為壁細胞、主細胞等，用以維持胃黏膜的快速更新。\n\n【核心考點】\n胃黏膜上皮的細胞組成與腸道特有杯狀細胞的分布差異；胃部出現杯狀細胞為腸化生（metaplasia）的病理特徵。",
      "key_point": "正常胃黏膜無杯狀細胞，若出現杯狀細胞則屬於腸化生（癌前病變）。",
      "flashcard_front": "胃黏膜（mucosa）的細胞組成與異常判定",
      "flashcard_back": "胃黏膜含有表面黏液細胞、壁細胞、主細胞與頸部幹細胞。正常胃中沒有杯狀細胞（goblet cell）；杯狀細胞是小腸與大腸特有，若在胃中出現代表腸化生（intestinal metaplasia）。",
      "flashcard_summary": "胃黏膜細胞 -> 含表面黏液細胞（屏障）、壁細胞（胃酸及內在因子）、主細胞、幹細胞。正常無杯狀細胞（出現代表腸化生）。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_044",
      "question_number": 44,
      "explanation": "【題幹解析】\n本題詢問皮膚的游離神經末梢（free nerve ending）在表皮層（epidermis）內分布的最深（最外側）終止位置。表皮由內而外分為基底層、棘狀層、顆粒層、透明層及角質層，游離神經末梢會穿過基底膜並向上延伸。\n\n【選項詳解】\n- A. 錯誤。游離神經末梢是無髓鞘的感覺神經末梢，穿過真皮-表皮交界處的基底膜後，會首先進入最內層的基底層（stratum basale），但它們還會繼續向上穿行至更淺層，因此基底層並非最遠終點。\n- B. 錯誤。游離神經末梢在基底層分支後會繼續向上延伸入棘狀層（stratum spinosum），在細胞間隙中穿行，但此處依然不是其分布的極限高度。\n- C. 正確。游離神經末梢在表皮中縱向延伸的最遠終點可達到顆粒層（stratum granulosum）。在此處它們終止於顆粒層細胞之間，負責感應溫覺、痛覺以及粗觸覺。\n- D. 錯誤。角質層（stratum corneum）是表皮最外層，由多層已經完全死亡、無核且充滿角蛋白的角質細胞所組成，主要發揮物理屏障作用，沒有活細胞生存的環境，游離神經末梢不會穿入此死細胞層。\n\n【核心考點】\n皮膚游離神經末梢的解剖分布範圍（自基底膜向上穿行，最遠終止於顆粒層，不進入角質層）。",
      "key_point": "游離神經末梢最遠可穿入表皮的顆粒層，但不進入已死亡的角質層。",
      "flashcard_front": "皮膚游離神經末梢（free nerve ending）的分布界限",
      "flashcard_back": "游離神經末梢穿過基底膜進入表皮，在表皮內最遠可向上延伸至顆粒層（stratum granulosum），負責傳導痛覺、溫度覺與粗觸覺，但不穿入死細胞組成的角質層。",
      "flashcard_summary": "游離神經末梢 -> 負責痛、溫、粗觸覺，表皮內穿行最遠至顆粒層（不入角質層）。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_045",
      "question_number": 45,
      "explanation": "【題幹解析】\n本題考查精索（spermatic cord）各組成構造的組織學微細結構。精索是懸吊睪丸並自腹股溝管通往腹腔的條索狀構造，其內包含輸精管、睪丸動靜脈、神經及淋巴管。\n\n【選項詳解】\n- A. 正確。輸精管（ductus deferens）的管壁肌層非常發達，由內縱（inner longitudinal）、中環（middle circular）、外縱（outer longitudinal）三層平滑肌所構成。強大的肌層收縮能提供足夠的蠕動壓力，以在射精時迅速運送精子。\n- B. 錯誤。蔓狀叢（pampiniform plexus）是由多條特殊的小型及中型靜脈所組成的網狀結構，其管壁中膜富含極厚的縱行平滑肌，這與一般的典型中型靜脈結構不同。這種特殊結構有助於在睪丸動脈與靜脈之間進行熱逆流交換，以維持睪丸低於體溫的溫度。\n- C. 錯誤。輸精管的黏膜內襯屬於假複層柱狀上皮（pseudostratified columnar epithelium），且其表面具有特化的微絨毛（不動纖毛 stereocilia），並非單層柱狀上皮。\n- D. 錯誤。精索的包膜內部主要由疏鬆結締組織（loose connective tissue）填充，內含脂肪細胞、小血管、神經與淋巴管，而非主要由網狀纖維構成的網狀組織。\n\n【核心考點】\n輸精管的三層平滑肌（內縱、中環、外縱）管壁特徵；輸精管為假複層柱狀上皮；蔓狀叢的中膜具厚縱行平滑肌。",
      "key_point": "輸精管由假複層柱狀上皮內襯及三層發達的平滑肌管壁構成；蔓狀叢具有非典型的中膜縱行平滑肌。",
      "flashcard_front": "輸精管（ductus deferens）與蔓狀叢的組織特點",
      "flashcard_back": "輸精管上皮為假複層柱狀上皮（具不動纖毛），肌層由內縱、中環、外縱三層平滑肌構成。蔓狀叢非典型中型靜脈，其靜脈壁中膜含有極厚的縱行平滑肌，有利於逆流熱交換。",
      "flashcard_summary": "輸精管 -> 假複層柱狀上皮 + 內縱/中環/外縱三層平滑肌。蔓狀叢 -> 非典型靜脈，中膜含厚縱行平滑肌，負責睪丸降溫之熱逆流交換。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_046",
      "question_number": 46,
      "explanation": "【題幹解析】\n本題詢問何種內分泌腺（endocrine gland）的實質結構主要由濾泡（follicle）所構成。濾泡結構的特點是細胞包圍成一個中空的腔室，用以儲存分泌的激素前驅物。\n\n【選項詳解】\n- A. 錯誤。胰臟的內分泌部為胰島（islets of Langerhans），是由多個多角形細胞（如分泌升糖素的 alpha 細胞、分泌胰島素的 beta 細胞等）聚集而成的球狀實心團塊，細胞間穿插豐富的竇狀微血管，並不形成濾泡結構。\n- B. 錯誤。腎上腺皮質實質細胞排列呈顯著的板狀或索狀：球狀帶排列成球團狀，束狀帶排列成平行放射狀的細胞索，網狀帶細胞呈交錯的網狀，而髓質的嗜鉻細胞亦排列成索狀或小團塊，皆無濾泡結構。\n- C. 正確。甲狀腺（thyroid gland）是人體中唯一主要由濾泡（thyroid follicles）組成的內分泌腺。濾泡壁為單層立方上皮，濾泡腔內充滿了富含甲狀腺球蛋白（thyroglobulin）的膠質（colloid），作為甲狀腺素的儲存庫。\n- D. 錯誤。松果腺（pineal gland）的實質主要由松果體細胞（pinealocytes）及膠質細胞組成，細胞多呈不規則索狀、團塊狀排列，並無濾泡結構。\n\n【核心考點】\n甲狀腺以濾泡為基本結構與功能單位，其濾泡腔內充填膠質以儲存甲狀腺素前驅物的組織學獨特性。",
      "key_point": "甲狀腺是唯一的濾泡狀結構內分泌腺，濾泡腔內充填膠質用以儲存激素。",
      "flashcard_front": "濾泡（follicle）結構內分泌腺的判定",
      "flashcard_back": "甲狀腺是體內唯一以濾泡為基本結構單位的內分泌腺，腔內充滿含有甲狀腺球蛋白的膠質。而胰腺胰島、腎上腺及松果腺均呈索狀或團塊狀實心排列。",
      "flashcard_summary": "濾泡狀內分泌腺 -> 甲狀腺（濾泡上皮圍成腔室儲存膠質）。胰腺、腎上腺、松果腺為索狀/團塊狀排列。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_047",
      "question_number": 47,
      "explanation": "【題幹解析】\n本題詢問細胞凋亡（apoptosis）的典型特徵。細胞凋亡是基因控制的程序性細胞死亡，其在生化反應與形態特徵上與被動受損死亡的細胞壞死（necrosis）有著根本的不同。\n\n【選項詳解】\n- A. 錯誤。細胞凋亡需要啟動 caspase 家族的酵素級聯反應（caspase cascade）。在此過程中，無論是內源性或外源性死亡路徑，都會使啟動型（如 caspase-8, -9）和執行型（如 caspase-3, -6, -7）的 caspases 活性大幅被活化，而非被抑制。\n- B. 正確。在細胞凋亡的中晚期，活化的執行型 caspase 會進一步活化內切酶（如 CAD），該內切酶會在核小體連接區（linker region）切斷 DNA，使 DNA 斷裂（fragmentation）成約 180-200 bp 的整數倍片段。在凝膠電泳中會呈現特徵性的階梯狀條帶（DNA laddering）。\n- C. 錯誤。細胞凋亡的形態學特徵是細胞萎縮（shrinkage）、細胞質濃縮及核碎裂，隨後形成完整的凋亡小體（apoptotic bodies），最後被周圍細胞吞噬。細胞體積變大並因水分大量湧入而脹破（swelling and lysis）是細胞壞死（necrosis）的典型特徵。\n- D. 錯誤。細胞凋亡過程中，細胞膜始終保持完整，胞內溶酶體等內容物不會釋放到細胞外，因此通常不引起局部發炎反應。相反地，細胞壞死因細胞膜破裂、內容物外溢，會釋放大量促發炎介質，進而引起嚴重的發炎反應。\n\n【核心考點】\n細胞凋亡的關鍵生化變化（caspase 活化、DNA 階梯狀斷裂）與形態特徵（細胞萎縮、無發炎反應），並與細胞壞死（膨脹破裂、釋放內容物引發炎）進行鑑別。",
      "key_point": "細胞凋亡表現為細胞萎縮、不發炎、caspase 級聯活化與 DNA 階梯狀斷裂；而細胞壞死則為膨脹破裂並引發嚴重發炎。",
      "flashcard_front": "細胞凋亡（apoptosis）與細胞壞死（necrosis）的關鍵區別",
      "flashcard_back": "凋亡為程序性死亡：caspases 活性升高、DNA 斷裂（呈 DNA ladder）、細胞萎縮、細胞膜完整且不引起發炎。壞死為被動破壞：細胞膨脹破裂、釋放內容物引發嚴重的發炎反應。",
      "flashcard_summary": "凋亡與壞死 -> 凋亡：caspase 活化，DNA斷裂（180-200bp），細胞萎縮，不發炎。壞死：膨脹破裂，發炎。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_048",
      "question_number": 48,
      "explanation": "【題幹解析】\n本題詢問中腦邊緣多巴胺路徑（mesolimbic dopamine pathway）的主要生理功能。多巴胺在腦中主要有四大傳導路徑，其中中腦邊緣路徑與情感、動機及回饋機制的調控最為密切。\n\n【選項詳解】\n- A. 錯誤。恐懼感的感知（perception of fear）主要由邊緣系統中的杏仁核（amygdala）以及前額葉皮質（prefrontal cortex）進行調控與處理，並非由中腦邊緣多巴胺路徑所主導。\n- B. 錯誤。初級視覺感知（primary visual perception）是由視網膜接收光線後，經視神經傳至視丘的外側膝狀體（LGN），再投射至枕葉的初級視覺皮質（V1），此神經通路的傳導不涉及中腦多巴胺路徑。\n- C. 錯誤。身體平衡（body balance）的維持與調節主要依賴小腦（cerebellum）、內耳的前庭系統（vestibular system）以及脊髓傳遞的深部本體感覺，與多巴胺獎賞系統無關。\n- D. 正確。中腦邊緣多巴胺路徑（mesolimbic dopamine pathway）起自中腦的腹側被蓋區（ventral tegmental area, VTA），投射至伏隔核（nucleus accumbens）、杏仁核及海馬迴等邊緣系統結構。這條路徑是腦部「獎賞系統」的核心，主要調控動機（motivation）、愉悅感、成癮行為以及回饋增強行為。\n\n【核心考點】\n大腦四大多巴胺路徑中中腦邊緣路徑（VTA 投射至伏隔核等邊緣系統）控制動機與獎賞行為的生理角色。",
      "key_point": "中腦邊緣多巴胺路徑連接中腦 VTA 與邊緣系統（如伏隔核），為腦內獎賞系統的核心，調控動機與成癮行為。",
      "flashcard_front": "中腦邊緣多巴胺路徑（mesolimbic pathway）的生理功能",
      "flashcard_back": "中腦邊緣多巴胺路徑起自中腦腹側被蓋區（VTA），投射至伏隔核等邊緣系統，為獎賞系統的核心，主要調控動機與獎賞行為（motivation and reward behaviors）。",
      "flashcard_summary": "mesolimbic dopamine pathway -> 起自中腦 VTA，投射至伏隔核，調控動機、成癮與獎賞行為。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_049",
      "question_number": 49,
      "explanation": "【題幹解析】\n本題考查味覺訊息傳導的神經解剖路徑。舌與咽部不同部位的味覺感受器由不同的腦神經所支配，且味覺信號在傳遞至大腦皮質前，必須經過特定的腦幹與視丘核團進行中繼轉接。\n\n【選項詳解】\n- A. 錯誤。來自舌前三分之二的味覺訊息是由顏面神經（CN VII）的鼓索支（chorda tympani）負責收集並傳遞至延腦的孤獨核，而非經由舌咽神經。\n- B. 錯誤。來自舌後三分之一的味覺訊息是由舌咽神經（CN IX）傳導至延腦。舌下神經（CN XII）是單純的運動神經，負責支配舌肌以控制舌頭的運動，與味覺傳導完全無關。\n- C. 正確。來自咽部（pharynx）與會厭（epiglottis）周圍的味覺訊息是由迷走神經（CN X）傳遞至延腦的孤獨核（nucleus solitarius）。\n- D. 錯誤。所有味覺傳導神經（CN VII, IX, X）的一級纖維都會先終止於延腦的孤獨核；其二級神經元發出纖維後會經由同側的孤獨丘腦束（solitariothalamic tract）投射至視丘的腹後內側核（VPM nucleus of thalamus）進行換元，最後三級神經元才會投射至大腦皮質的初級味覺區（位於島葉及額葉蓋部），並非直接投射。\n\n【核心考點】\n味覺傳導支配腦神經的解剖分布（舌前2/3為CN VII、舌後1/3為CN IX、咽與會厭為CN X）以及經延腦孤獨核、視丘VPM核至大腦味覺皮質的三級神經傳導通路。",
      "key_point": "味覺由 CN VII（舌前2/3）、CN IX（舌後1/3）、CN X（咽與會厭）傳遞至延腦孤獨核，再經視丘 VPM 核投射至初級味覺皮質。",
      "flashcard_front": "味覺傳導支配的腦神經與中繼路徑",
      "flashcard_back": "味覺支配：舌前2/3由顏面神經（CN VII，鼓索支）、舌後1/3由舌咽神經（CN IX）、咽與會厭由迷走神經（CN X）傳導。傳導途徑為：外周感受器 -> 延腦孤獨核 -> 視丘腹後內側核（VPM） -> 大腦初級味覺皮質。",
      "flashcard_summary": "味覺傳導 -> 舌前2/3為CN VII，舌後1/3為CN IX，咽部為CN X。中繼點：延腦孤獨核 -> 視丘VPM核 -> 大腦皮質。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    },
    {
      "question_id": "109-1_medicine-1_050",
      "question_number": 50,
      "explanation": "【題幹解析】\n本題詢問何種視覺路徑損傷會導致兩眼的外側（顳側）視野缺損。解答此題需要理解光學成像在視網膜的投影關係（左右顳側視野投射於鼻側視網膜），以及鼻側視網膜發出之視神經纖維在中線交叉的解剖走向。\n\n【選項詳解】\n- A. 正確。兩眼外側（顳側）視野缺失稱為「雙顳側偏盲（bitemporal hemianopsia）」。外側視野的光線會投射到雙眼的鼻側視網膜（nasal retina）。鼻側視網膜發出的視神經纖維在向後傳導時，會在視神經交叉（optic chiasm）處跨越中線交叉至對側。因此，當視神經交叉處受損（如腦下垂體腫瘤壓迫）時，會專一性地壓迫這些交叉的鼻側視網膜纖維，導致雙眼外側視野喪失。\n- B. 錯誤。左側視神經（left optic nerve）受損會導致左側眼球傳導完全中斷，造成左眼全盲（ipsilateral blindness，左眼鼻側與顳側視野均喪失），而右眼視野則完全正常。\n- C. 錯誤。右側視神經（right optic nerve）受損會導致右側眼球傳導完全中斷，造成右眼全盲（右眼鼻側與顳側視野均喪失），而左眼視野則完全正常。\n- D. 錯誤。右側視神經束（right optic tract）包含了來自右眼顳側視網膜（負責左眼鼻側視野）和左眼鼻側視網膜（負責左眼顳側視野）的纖維。因此，右側視神經束受損會導致左側同向偏盲（contralateral homonymous hemianopsia），即雙眼的左側視野缺失。\n\n【核心考點】\n視覺傳導通路的解剖病變與視野缺損的對應關係：視神經交叉受損導致雙顳側偏盲，單側視神經受損導致同側全盲，單側視神經束受損導致對側同向偏盲。",
      "key_point": "視神經交叉處含有來自雙眼鼻側視網膜（負責雙眼外側顳側視野）的交叉纖維，受損時會導致雙顳側偏盲。",
      "flashcard_front": "視野缺損與視覺傳導通路受損位置的對應關係",
      "flashcard_back": "雙顳側偏盲（雙眼外側視野缺失）由視神經交叉（optic chiasm）受損引起。單側視神經受損導致同側單眼全盲。單側視神經束（optic tract）受損導致對側同向偏盲。",
      "flashcard_summary": "視野缺損對應 -> 視神經交叉受損 -> 雙顳側偏盲（雙眼外側缺失）；單側視神經受損 -> 同側單眼盲；單側視神經束受損 -> 对側同向偏盲。",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-12T21:20:00+08:00",
      "manual_review_notes": []
    }
  ]
}

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(update_data, f, ensure_ascii=False, indent=2)

print(f"Update JSON successfully generated at: {target_file}")
