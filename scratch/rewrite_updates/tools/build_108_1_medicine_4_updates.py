import json
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


SOURCE_FILE = "public/data/exams/108-1/medicine-4.json"
DATASET_ID = "108-1_medicine-4"
OUT_DIR = Path("scratch/rewrite_updates/108-1_medicine-4")
STAMP = "2026-07-16T00:00:00+08:00"


def make_explanation(analysis, options, core):
    lines = ["【題幹解析】", analysis.strip(), "", "【選項詳解】"]
    for letter in ("A", "B", "C", "D"):
        lines.append(f"- {letter}. {options[letter].strip()}")
    lines.extend(["", "【核心考點】", core.strip()])
    return "\n".join(lines)


REWRITES = {
    17: {
        "analysis": "題目把粗動作、精細動作與語言社交里程碑放在一起考。單腳站立約10秒、能照樣畫圓圈、會使用「你的」「我的」等代名詞，整體最接近3歲到未滿4歲的發展範圍。",
        "options": {
            "A": "錯誤。2歲到未滿3歲可有跑、踢球、疊積木與短句，但單腳站10秒與照樣畫圓通常還偏成熟。",
            "B": "正確。3歲到未滿4歲可見較穩定的平衡能力、畫圓與較成熟的代名詞使用，與題目三條線索一致。",
            "C": "錯誤。4歲到未滿5歲通常可發展到單腳跳、畫十字或更複雜圖形，能力層級比題幹更進一步。",
            "D": "錯誤。5歲到未滿6歲會有更成熟的平衡、精細動作與人形或幾何圖形描畫，明顯晚於題目描述。",
        },
        "key_point": "單腳站約10秒、照樣畫圓、使用你我代名詞，整體指向3歲到未滿4歲。",
        "front": "兒童發展 / 單腳站10秒 / 畫圓 / 你我代名詞",
        "back": "發展里程碑題要合併粗動作、精細動作與語言社交判斷；畫圓與你我代名詞常指向3歲左右。",
        "summary": "發展里程碑 -> 單腳站10秒、畫圓、你我代名詞約3-4歲",
    },
    31: {
        "analysis": "題目問臺灣現行新生兒代謝異常篩檢何者錯誤。採血通常需等出生滿48小時或餵奶滿24小時後，讓代謝物有足夠累積；若出生一天內就採檢，可能提高偽陰性風險。",
        "options": {
            "A": "錯誤，為本題答案。新生兒篩檢不是剛出生一天內就採腳跟血；太早採血時胺基酸、有機酸或脂肪酸代謝異常可能尚未表現出來。",
            "B": "正確。串聯質譜儀（tandem mass spectrometry, MS/MS）可一次篩檢多種代謝物，是目前新生兒代謝異常篩檢的重要工具。",
            "C": "正確。常見篩檢疾病包含胺基酸、有機酸與脂肪酸氧化代謝異常，這些正是MS/MS可偵測的核心類別。",
            "D": "正確。低體重、早產、產程或新生兒狀況不穩都可能影響代謝物與採血品質，因此較容易出現偽陽性或需複檢。",
        },
        "key_point": "新生兒代謝異常篩檢通常等出生滿48小時或餵奶滿24小時後採血，不是在出生一天內立即採檢。",
        "front": "新生兒代謝篩檢 / 採血時間 / 出生滿48小時 / MS/MS",
        "back": "新生兒代謝篩檢需等餵食與代謝物累積後採腳跟血；太早採檢可能造成偽陰性。MS/MS常用於胺基酸、有機酸、脂肪酸代謝異常篩檢。",
        "summary": "新生兒篩檢 -> 出生滿48小時或餵奶滿24小時後採血",
    },
    32: {
        "analysis": "題目要由家族圖判斷遺傳型態。男女都可罹病、可見同胞發病而父母多為未發病帶因者時，最典型是體染色體隱性遺傳；選項中Cooley anemia符合這個模式。",
        "options": {
            "A": "錯誤。軟骨發育不全多為體染色體顯性，常見FGFR3突變，與題幹暗示的隱性遺傳不合。",
            "B": "正確。庫利氏貧血即重型乙型海洋性貧血，典型為體染色體隱性遺傳，父母常為帶因者。",
            "C": "錯誤。Duchenne muscular dystrophy是X染色體聯鎖隱性遺傳，主要影響男孩，不符合男女皆可同等受影響的AR圖譜。",
            "D": "錯誤。結節性硬化症多為體染色體顯性，也常有新生突變，不是本題最可能的隱性遺傳答案。",
        },
        "key_point": "Cooley anemia屬體染色體隱性遺傳；DMD是X連鎖隱性，軟骨發育不全與結節性硬化症多為體染色體顯性。",
        "front": "家族譜 / AR遺傳 / Cooley anemia",
        "back": "男女皆可罹病、父母未病但子代發病，常指向體染色體隱性遺傳；庫利氏貧血是典型例子。",
        "summary": "遺傳模式 -> Cooley anemia為體染色體隱性",
    },
    33: {
        "analysis": "15歲男生半夜突發單側睪丸劇痛、冒冷汗，急診首先要想到睪丸扭轉。睪丸扭轉是搶時間的缺血急症，若無法立刻以超音波確認，不應因等待檢查而延誤手術探查。",
        "options": {
            "A": "錯誤。抗生素適用於附睪睪丸炎等感染，但題幹急性劇痛與自主神經症狀更像扭轉，單給抗生素會延誤救睪。",
            "B": "錯誤。睪丸切片不是急性陰囊疼痛的標準處置，且會延誤復位與固定。",
            "C": "正確。高度懷疑睪丸扭轉且缺乏即時影像時，應緊急睪丸探查、復位並固定，以降低壞死風險。",
            "D": "錯誤。睪丸切除只在探查發現睪丸已壞死不可挽回時才考慮，初始處置不是直接切除。",
        },
        "key_point": "青少年突發單側睪丸劇痛要先排除睪丸扭轉；影像不可得時應緊急手術探查。",
        "front": "15歲 / 半夜睪丸劇痛 / 睪丸扭轉 / 急診處置",
        "back": "睪丸扭轉的救援時間很短；高度懷疑時不能等檢查，應緊急手術探查、復位與固定。",
        "summary": "急性睪丸扭轉 -> 不能延誤，優先手術探查",
    },
    34: {
        "analysis": "題目問脂漏性皮膚炎何者錯誤。脂漏性皮膚炎好發於皮脂腺豐富處，與Malassezia和發炎反應相關，因此外用抗黴菌藥物常有效，說不能有效治療是錯的。",
        "options": {
            "A": "正確。頭皮、眉毛、鼻翼兩側與耳後都是皮脂腺豐富區，符合脂漏性皮膚炎典型分布。",
            "B": "正確。脂漏性皮膚炎可見於嬰兒乳痂，也可見於成人慢性反覆發作。",
            "C": "錯誤，為本題答案。Ketoconazole等外用抗黴菌藥物可降低Malassezia相關發炎，常用且有效。",
            "D": "正確。病程頑固、範圍廣或表現不尋常時，要想到免疫低下，包含HIV感染。",
        },
        "key_point": "脂漏性皮膚炎與Malassezia相關，外用抗黴菌藥物可有效治療；頑固不尋常時留意HIV。",
        "front": "脂漏性皮膚炎 / Malassezia / ketoconazole / HIV",
        "back": "脂漏性皮膚炎好發皮脂腺豐富部位，嬰兒與成人都可發生；外用抗黴菌藥物常有效。",
        "summary": "脂漏性皮膚炎 -> 抗黴菌有效，頑固需想HIV",
    },
    35: {
        "analysis": "類天疱瘡是老年人常見的自體免疫表皮下水疱病。題目問錯誤敘述，『常發生於年輕人』與典型流行病學相反。",
        "options": {
            "A": "錯誤，為本題答案。Bullous pemphigoid典型好發於老年人，年輕族群相對少見。",
            "B": "正確。早期可先出現搔癢、蕁麻疹樣紅斑，之後形成張力性水疱。",
            "C": "正確。病理常見表皮下水疱，伴嗜伊紅球浸潤；免疫螢光可見基底膜帶沉積。",
            "D": "正確。治療常以局部或全身性皮質類固醇為主，嚴重或頑固者可搭配免疫抑制治療。",
        },
        "key_point": "Bullous pemphigoid好發老年人，為表皮下張力性水疱，常有嗜伊紅球浸潤。",
        "front": "Bullous pemphigoid / 老年人 / 張力性水疱 / eosinophil",
        "back": "類天疱瘡好發老年人，早期可癢與蕁麻疹樣，病理表皮下水疱伴嗜伊紅球，Nikolsky sign多陰性。",
        "summary": "類天疱瘡 -> 老年人、表皮下水疱、嗜伊紅球",
    },
    36: {
        "analysis": "慢性搔癢丘疹加上Congo red染色陽性、偏光下蘋果綠雙折射，代表類澱粉蛋白沉積。皮膚局部慢性苔癬樣病灶最符合類澱粉性苔癬。",
        "options": {
            "A": "錯誤。點滴狀乾癬常為小滴狀鱗屑性紅斑，常與鏈球菌感染後相關，不會以Congo red類澱粉沉積作為診斷重點。",
            "B": "錯誤。結節性癢疹可有劇癢結節，但病理核心是反覆搔抓造成的結節性變化，不是Congo red陽性類澱粉沉積。",
            "C": "錯誤。扁平苔癬常見紫紅色扁平丘疹與Wickham striae，病理是介面皮膚炎，不是偏光雙折射的類澱粉。",
            "D": "正確。類澱粉性苔癬可在真皮乳頭層有類澱粉沉積，Congo red染色與偏光雙折射支持診斷。",
        },
        "key_point": "Congo red陽性且偏光下蘋果綠雙折射代表類澱粉沉積；慢性癢疹樣皮膚病灶可指向lichen amyloidosis。",
        "front": "Congo red / apple-green birefringence / lichen amyloidosis",
        "back": "皮膚慢性搔癢丘疹若切片顯示類澱粉沉積，診斷想到類澱粉性苔癬。",
        "summary": "Congo red + 偏光雙折射 -> 類澱粉性苔癬",
    },
    37: {
        "analysis": "Patch testing主要用來找出造成過敏性接觸性皮膚炎的特定接觸性過敏原，屬於第IV型延遲性超敏反應的臨床測試。",
        "options": {
            "A": "錯誤。貼膚試驗不能確診所有接觸性皮膚炎；刺激性接觸性皮膚炎主要靠病史與暴露判斷。",
            "B": "正確。貼膚試驗的目的就是辨認特定接觸性過敏原，協助病人日後避免接觸。",
            "C": "錯誤。嚴重度需依病灶範圍、發炎程度與功能影響評估，patch testing不是嚴重度量表。",
            "D": "錯誤。雖然貼膚試驗通常需在貼後48小時左右判讀，但它不是用來確認發病是否超過48小時。",
        },
        "key_point": "Patch testing的主要目的，是找出過敏性接觸性皮膚炎的接觸性過敏原。",
        "front": "Patch testing / allergic contact dermatitis / allergen",
        "back": "貼膚試驗檢測第IV型延遲性過敏，臨床目的在找出接觸性過敏原，不是判斷嚴重度或所有接觸性皮膚炎。",
        "summary": "貼膚試驗 -> 找接觸性過敏原",
    },
    38: {
        "analysis": "6歲兒童自2歲起反覆劇癢皮膚病變，加上父母有過敏性鼻炎症狀，提示異位性體質。兒童慢性反覆濕疹與劇癢最符合異位性皮膚炎。",
        "options": {
            "A": "錯誤。脂漏性皮膚炎偏頭皮、眉間、鼻翼等皮脂腺部位，嬰兒乳痂常見，但不以強烈異位性家族史與反覆劇癢為核心。",
            "B": "錯誤。接觸性皮膚炎通常與特定外界接觸區域相關，病灶分布與暴露史比家族過敏史更重要。",
            "C": "正確。異位性皮膚炎常自幼兒期開始，反覆劇癢濕疹，並常合併或家族有過敏性鼻炎、氣喘等異位性疾病。",
            "D": "錯誤。鬱血性皮膚炎多見於成人慢性靜脈功能不全的下肢病灶，不符合6歲男孩。",
        },
        "key_point": "兒童慢性反覆劇癢濕疹加異位性家族史，最符合異位性皮膚炎。",
        "front": "兒童 / 劇癢濕疹 / 過敏家族史 / atopic dermatitis",
        "back": "異位性皮膚炎常從幼兒期開始，反覆劇癢，常有過敏性鼻炎或氣喘個人或家族史。",
        "summary": "劇癢反覆濕疹 + 異位性家族史 -> 異位性皮膚炎",
    },
    39: {
        "analysis": "Nikolsky sign陽性代表表皮容易被推開，常見於表皮內鬆解或嚴重表皮壞死。Bullous pemphigoid是表皮下水疱，水疱壁較厚且緊繃，因此Nikolsky sign多為陰性。",
        "options": {
            "A": "錯誤。SSSS由金黃色葡萄球菌剝脫毒素造成表皮淺層剝離，可出現Nikolsky sign陽性。",
            "B": "錯誤。Pemphigus vulgaris是表皮內棘層鬆解，Nikolsky sign典型陽性。",
            "C": "錯誤。Stevens-Johnson syndrome有表皮壞死與剝離，也可出現Nikolsky sign陽性。",
            "D": "正確。Bullous pemphigoid為表皮下張力性水疱，表皮不易被輕推剝離，Nikolsky sign通常陰性。",
        },
        "key_point": "Bullous pemphigoid是表皮下水疱，Nikolsky sign通常陰性；pemphigus vulgaris、SSSS、SJS可陽性。",
        "front": "Nikolsky sign / bullous pemphigoid / pemphigus vulgaris",
        "back": "Nikolsky sign陽性多見表皮內鬆解或壞死；類天疱瘡為表皮下水疱，所以多為陰性。",
        "summary": "Nikolsky陰性 -> bullous pemphigoid",
    },
    40: {
        "analysis": "題目問Toxic shock syndrome何者錯誤。TSS重點是金黃色葡萄球菌TSST-1或A群鏈球菌外毒素造成超抗原反應與休克，不是Pseudomonas剝脫毒素。",
        "options": {
            "A": "正確。TSS可有瀰漫性紅疹、皮膚疼痛與後續脫屑，也可能伴局部感染病灶。",
            "B": "正確。TSS可由術後傷口、軟組織或其他深部感染引起，早期皮膚疼痛可很明顯。",
            "C": "正確。發燒、肌痛、喉嚨痛、嘔吐腹瀉、低血壓與多器官衰竭都是TSS的重要全身表現。",
            "D": "錯誤，為本題答案。TSS不是由Pseudomonas exfoliative toxin造成；葡萄球菌剝脫毒素較與SSSS相關，TSS則是超抗原毒素。",
        },
        "key_point": "TSS由葡萄球菌TSST-1或鏈球菌外毒素等超抗原引起，不是Pseudomonas exfoliative toxin。",
        "front": "Toxic shock syndrome / TSST-1 / superantigen / Pseudomonas錯",
        "back": "TSS有發燒、低血壓、皮疹脫屑與多器官侵犯；致病重點是葡萄球菌或鏈球菌超抗原毒素。",
        "summary": "TSS -> Staph/Strep superantigen，不是Pseudomonas剝脫毒素",
    },
    41: {
        "analysis": "題目問青年型皮肌炎何者錯誤。成人皮肌炎較需警覺惡性腫瘤，但juvenile dermatomyositis較典型的是皮膚血管病變、肌炎與鈣化症，鼻咽癌關聯不是其常見特色。",
        "options": {
            "A": "正確。Juvenile dermatomyositis可有皮膚表現明顯而肌肉症狀較少的amyopathic或hypomyopathic表現。",
            "B": "正確。皮膚鈣化症是兒童皮肌炎常考併發症，尤其病程慢性或控制不佳時更常見。",
            "C": "正確。血管病變是JDM的重要病理機轉，可造成皮膚潰瘍、甲摺微血管變化與系統性表現。",
            "D": "錯誤，為本題答案。鼻咽癌等惡性腫瘤關聯主要是成人皮肌炎考點，青年型皮肌炎並不常見。",
        },
        "key_point": "Juvenile dermatomyositis常見鈣化症與血管病變；惡性腫瘤關聯遠低於成人型。",
        "front": "JDM / calcinosis cutis / vasculopathy / malignancy少",
        "back": "青年型皮肌炎與成人不同，重點是皮膚肌肉發炎、血管病變與鈣化症，不是鼻咽癌。",
        "summary": "JDM -> calcinosis與vasculopathy常見，癌症關聯少",
    },
    42: {
        "analysis": "題目問皮膚黑色素過度沉著何者錯誤。汗斑可造成低色素或高色素斑，不是只會變深；Malassezia相關代謝物可影響黑色素生成。",
        "options": {
            "A": "正確。黑色素細胞數量增加或黑色素生成、轉運增加，都可能造成皮膚顏色變深。",
            "B": "錯誤，為本題答案。汗斑可呈現低色素、紅褐色或高色素斑，並非只造成膚色變深。",
            "C": "正確。轉移性黑色素瘤可釋放或造成廣泛色素變化，少數情況可見universal melanosis。",
            "D": "正確。基因、荷爾蒙與紫外線都可影響黑色素細胞活性或黑色素合成。",
        },
        "key_point": "汗斑可造成低色素或高色素斑；說只會造成膚色變深是錯誤的。",
        "front": "Pityriasis versicolor / hypopigmentation / hypermelanosis",
        "back": "汗斑由Malassezia造成，臨床可變深也可變淺，因此不是單純黑色素過度沉著疾病。",
        "summary": "汗斑 -> 可低色素也可高色素",
    },
    43: {
        "analysis": "題目問黑色素沉著治療何者錯誤。表皮黑色素較能用外用淡斑藥處理；真皮深層色素需要能穿透較深且選擇性破壞色素的雷射，Nd:YAG通常比IPL更適合。",
        "options": {
            "A": "正確。表皮層黑色素增加時，hydroquinone可抑制黑色素生成，常用於表皮型色素沉著。",
            "B": "錯誤，為本題答案。真皮層色素較深，IPL穿透與選擇性較有限，Q-switched Nd:YAG等雷射通常更合適。",
            "C": "正確。雷射能量過高或治療太密集會破壞黑色素細胞，可能造成醫源性色素脫失。",
            "D": "正確。外用A酸可促進角質代謝並輔助淡化雀斑或表皮型色素問題，但常需合併防曬。",
        },
        "key_point": "真皮色素沉著通常較適合Nd:YAG等可達深層的雷射，IPL不是較佳選擇。",
        "front": "真皮黑色素 / IPL / Nd:YAG / hydroquinone",
        "back": "表皮黑色素可用hydroquinone等外用藥；真皮深層色素需較深穿透雷射，過度治療會色素脫失。",
        "summary": "色素治療 -> 表皮外用藥，真皮偏Nd:YAG",
    },
    44: {
        "analysis": "高齡男性足部紫色斑塊，加上病理篩板狀或裂隙狀血管增生，最典型是Kaposi sarcoma。此病常與HHV-8相關，可見於老年、免疫低下或HIV感染者。",
        "options": {
            "A": "錯誤。血管肉瘤多為侵襲性惡性血管腫瘤，常見頭頸部或放射後皮膚，不以足部慢性紫斑與HHV-8脈絡為典型。",
            "B": "正確。Kaposi sarcoma典型表現為紫紅色斑塊、結節，病理有裂隙狀血管增生與梭形細胞。",
            "C": "錯誤。血管角化瘤是表淺血管擴張合併角化，通常為小丘疹，不符合本題病理描述。",
            "D": "錯誤。竇狀血管瘤是良性血管病變，與高齡足部紫色斑塊及Kaposi典型病理不合。",
        },
        "key_point": "足部紫色斑塊加裂隙狀/篩板狀血管增生，最符合Kaposi sarcoma。",
        "front": "紫色斑塊 / slit-like vascular spaces / Kaposi sarcoma",
        "back": "Kaposi sarcoma可見紫紅色皮膚斑塊或結節，病理有裂隙狀血管與梭形細胞，與HHV-8相關。",
        "summary": "紫色斑塊 + 裂隙狀血管 -> Kaposi sarcoma",
    },
    45: {
        "analysis": "承上題為Kaposi sarcoma。Kaposi sarcoma最重要的病毒關聯是human herpesvirus 8，也稱Kaposi sarcoma-associated herpesvirus。",
        "options": {
            "A": "正確。HHV-8與Kaposi sarcoma有強關聯，是本題承上題最直接的病毒答案。",
            "B": "錯誤。HSV-2主要造成生殖器疱疹，與Kaposi sarcoma不是典型關聯。",
            "C": "錯誤。HPV與子宮頸癌、肛門癌、疣等相關，不是Kaposi sarcoma的致病病毒。",
            "D": "錯誤。EBV與鼻咽癌、Burkitt lymphoma、部分Hodgkin lymphoma等相關，不是Kaposi sarcoma的典型病毒。",
        },
        "key_point": "Kaposi sarcoma與HHV-8感染相關。",
        "front": "Kaposi sarcoma / HHV-8",
        "back": "看到Kaposi sarcoma就連到HHV-8；它也稱Kaposi sarcoma-associated herpesvirus。",
        "summary": "Kaposi sarcoma -> HHV-8",
    },
    46: {
        "analysis": "病人晚間10點正常、早上8點醒來即有中風症狀，屬wake-up stroke；到院時已無法確定在傳統IV tPA時間窗內。題幹未提供可做再灌流治療的特殊影像條件，因此最適合急性處置是抗血小板治療。",
        "options": {
            "A": "錯誤。IV tPA需符合時間窗與影像條件；醒後中風若無進階影像篩選，不可直接視為可溶栓。",
            "B": "錯誤。頸動脈支架不是左側放射冠小梗塞的急性標準處置，需有相對應大血管狹窄適應症。",
            "C": "正確。無法使用溶栓或取栓時，缺血性中風急性期常以抗血小板藥物作為基本治療。",
            "D": "錯誤。抗凝血主要用於心房顫動等心因性栓塞特定情境，急性小梗塞不能常規立即抗凝。",
        },
        "key_point": "Wake-up stroke若無法證明在再灌流治療適應症內，急性處置以抗血小板等標準治療為主。",
        "front": "Wake-up stroke / IV tPA時間窗 / antiplatelet",
        "back": "醒後中風發作時間不明；若未符合溶栓或取栓條件，急性缺血性中風以抗血小板治療為主。",
        "summary": "醒後中風 -> 未符溶栓條件時抗血小板",
    },
    47: {
        "analysis": "此題有官方更正為A與C皆可給分。一般臨床上蜘蛛膜下腔出血最常見原因可包含外傷；若限定自發性SAH，最典型原因是囊狀動脈瘤破裂。題解應保留官方多重答案。",
        "options": {
            "A": "正確。外傷是整體SAH常見原因，官方更正接受此選項。",
            "B": "錯誤。動靜脈畸形可造成顱內出血或SAH，但不是最常見答案。",
            "C": "正確。自發性SAH最典型、最常考原因是顱內囊狀動脈瘤破裂，官方也接受此選項。",
            "D": "錯誤。梭狀動脈瘤不是SAH最常見原因，考試上不如囊狀動脈瘤典型。",
        },
        "key_point": "本題官方更正A、C皆給分；整體SAH可見外傷，自發性SAH最典型是囊狀動脈瘤破裂。",
        "front": "SAH / trauma / saccular aneurysm / 官方更正",
        "back": "蜘蛛膜下腔出血若問整體原因可考外傷；若問自發性SAH，最典型是berry/saccular aneurysm破裂。本題A、C皆接受。",
        "summary": "SAH原因 -> 官方更正A與C皆可",
        "notes": ["官方更正多重答案：A與C皆接受，已保留原始答案欄位不改動。"],
    },
    48: {
        "analysis": "Cerebral venous sinus thrombosis最常見表現是頭痛，可能因靜脈壓上升與顱內壓升高造成。其他局灶神經症狀、癲癇或意識障礙可出現，但不是最常見。",
        "options": {
            "A": "錯誤。複視可因顱內壓升高造成第六腦神經麻痺而出現，但不是最常見主訴。",
            "B": "正確。頭痛是CVST最常見臨床表現，可為亞急性、漸進或類似偏頭痛樣。",
            "C": "錯誤。單側肢體無力可因靜脈性梗塞或出血出現，但頻率低於頭痛。",
            "D": "錯誤。意識障礙代表較嚴重或廣泛病變，並非最常見初始表現。",
        },
        "key_point": "腦靜脈竇栓塞最常見臨床表現是頭痛。",
        "front": "CVST / 最常見症狀 / headache",
        "back": "CVST可有頭痛、癲癇、局灶神經缺損與顱內壓升高；最常見仍是頭痛。",
        "summary": "CVST -> 頭痛最常見",
    },
    49: {
        "analysis": "REM sleep behavior disorder是REM睡眠肌肉失張力消失，病人會把夢境動作演出來。REM睡眠較集中在後半夜，因此RBD通常在後半夜出現，且常與未來突觸核蛋白病變相關。",
        "options": {
            "A": "正確。REM期在睡眠後半夜較多，所以RBD事件常在後半夜發生。",
            "B": "錯誤。RBD動作通常隨夢境內容變化，不像某些癲癇或刻板行為有高度固定模式。",
            "C": "錯誤。RBD較預示Parkinson disease、Lewy body dementia或multiple system atrophy等synucleinopathy，不是最典型變成阿茲海默症。",
            "D": "錯誤。RBD夢境常是被追趕、攻擊或防衛等不愉快內容，病人可能揮拳踢腿而受傷。",
        },
        "key_point": "RBD常在後半夜發生，且是Parkinson disease與Lewy body dementia等synucleinopathy的重要前驅線索。",
        "front": "REM sleep behavior disorder / 後半夜 / synucleinopathy",
        "back": "RBD是REM期肌肉失張力消失，病人演出夢境；常在後半夜發生，未來要警覺巴金森相關神經退化。",
        "summary": "RBD -> 後半夜、夢境演出、synucleinopathy",
    },
    50: {
        "analysis": "14歲、晨起肌陣攣、跌倒、智力正常與家族史，典型是青少年肌陣攣性癲癇（JME）。題目問錯誤，診斷成兒童失神性癲癇不恰當。",
        "options": {
            "A": "正確。JME腦波可見廣泛性多棘慢波，常在4-6 Hz附近描述。",
            "B": "正確。JME常有遺傳傾向，家族癲癇基因資訊可作為診斷輔助，但仍需臨床與EEG判斷。",
            "C": "正確。Valproate對JME效果佳，常被視為首選之一；女性用藥需另外評估致畸與生殖風險。",
            "D": "錯誤，為本題答案。兒童失神性癲癇典型是短暫發呆與3-Hz spike-wave，不是晨起肌陣攣跌倒。",
        },
        "key_point": "青少年晨起肌陣攣加廣泛性多棘慢波，最符合JME；不是兒童失神性癲癇。",
        "front": "14歲 / morning myoclonus / JME / valproate",
        "back": "JME常在青春期出現晨起肌陣攣，可伴全身強直陣攣；EEG為廣泛性多棘慢波，治療常用valproate等。",
        "summary": "晨起肌陣攣 -> Juvenile myoclonic epilepsy",
    },
    51: {
        "analysis": "題目問何者不是ICHD-3偏頭痛診斷標準。偏頭痛典型包含4-72小時、噁心嘔吐、畏光怕吵、活動加劇；流淚與結膜充血屬三叉自主神經頭痛如叢集性頭痛特色。",
        "options": {
            "A": "正確。偏頭痛未治療或治療無效時常持續4-72小時，是診斷標準之一。",
            "B": "正確。噁心及/或嘔吐，或畏光怕吵，是偏頭痛常見伴隨症狀。",
            "C": "正確。日常活動加重頭痛是偏頭痛特徵之一，因此患者常想休息避免活動。",
            "D": "錯誤，為本題答案。流淚與眼結膜充血較像叢集性頭痛等三叉自主神經頭痛，不是偏頭痛診斷標準。",
        },
        "key_point": "偏頭痛診斷包含4-72小時、活動加重與噁心嘔吐/畏光怕吵；流淚結膜充血偏向叢集性頭痛。",
        "front": "Migraine / ICHD-3 / cluster headache autonomic signs",
        "back": "偏頭痛可有噁心嘔吐、畏光怕吵與活動加劇；同側流淚、結膜充血是叢集性頭痛線索。",
        "summary": "偏頭痛標準 -> 不含流淚結膜充血",
    },
    52: {
        "analysis": "譫妄與失智都可有認知障礙，但譫妄最核心是急性、波動性的注意力不集中與意識清晰度改變。這是與慢性失智最大的鑑別點。",
        "options": {
            "A": "錯誤。幻覺可見於譫妄，也可見於部分失智或精神病，不能作為最大區別。",
            "B": "正確。注意力不集中是譫妄診斷核心，病人常無法維持或轉移注意力。",
            "C": "錯誤。攻擊行為可由譫妄、失智或其他精神疾患造成，不具特異性。",
            "D": "錯誤。癲癇發作可能造成意識改變或譫妄樣狀態，但不是譫妄與失智的最大鑑別症狀。",
        },
        "key_point": "譫妄的核心是急性波動性意識與注意力障礙；失智多為慢性進行性認知退化。",
        "front": "Delirium vs dementia / attention",
        "back": "看到急性、波動、注意力不集中，要先想到譫妄；失智通常是慢性記憶與認知退化。",
        "summary": "譫妄鑑別 -> 注意力不集中",
    },
    53: {
        "analysis": "紅核附近出血後數月出現軟腭肌陣攣，提示Guillain-Mollaret triangle受損後的下橄欖核假性肥大。中腦紅核病灶會影響同側中央被蓋束，導致同側下橄欖核肥大。",
        "options": {
            "A": "錯誤。齒狀核是此迴路的一端，但本題病灶在左側紅核附近，後續影像重點不是左側齒狀核肥大。",
            "B": "錯誤。右側齒狀核也不是軟腭肌陣攣後典型假性肥大的部位。",
            "C": "正確。左側紅核/中央被蓋束受損後，可造成左側下橄欖核去神經化後假性肥大。",
            "D": "錯誤。若病灶位置在左側紅核附近，典型對應為同側下橄欖核，不是右側。",
        },
        "key_point": "軟腭肌陣攣與Guillain-Mollaret triangle病灶相關；紅核/中央被蓋束病灶可造成同側下橄欖核肥大。",
        "front": "Palatal myoclonus / red nucleus / inferior olive hypertrophy",
        "back": "紅核、齒狀核、下橄欖核構成Guillain-Mollaret triangle；路徑受損後可見下橄欖核假性肥大與軟腭肌陣攣。",
        "summary": "紅核病灶後軟腭肌陣攣 -> 同側下橄欖核肥大",
    },
    54: {
        "analysis": "原發性巴金森氏病可伴隨非動作症狀，如嗅覺減退、REM睡眠行為異常與不寧腿。皮質性感覺喪失屬皮質功能缺損，較支持非典型巴金森症候群或其他皮質病變。",
        "options": {
            "A": "錯誤。嗅覺減退是Parkinson disease常見前驅或非動作症狀。",
            "B": "錯誤。不寧腿症候群可與巴金森病共病或相關，不是最強烈排除原發性PD的線索。",
            "C": "正確。皮質性感覺喪失代表皮質整合功能受損，較不符合單純原發性PD，需想到非典型或皮質基底核症候群。",
            "D": "錯誤。REM睡眠行為異常是synucleinopathy常見前驅症狀，與PD關聯很強。",
        },
        "key_point": "皮質性感覺喪失不是原發性巴金森氏病典型表現，應警覺非典型巴金森症候群。",
        "front": "Idiopathic Parkinson disease / cortical sensory loss / atypical parkinsonism",
        "back": "PD常見嗅覺減退與RBD；若出現皮質性感覺喪失、失用等皮質徵象，較不支持原發性PD。",
        "summary": "非典型PD警訊 -> cortical sensory loss",
    },
    55: {
        "analysis": "題目問哪個神經疾病最不侵犯感覺系統。運動神經元病變主要影響上、下運動神經元，感覺通常保留；其他選項本質上都可造成感覺症狀。",
        "options": {
            "A": "錯誤。糖尿病多發性神經病變常先影響遠端感覺神經，出現麻、痛或感覺喪失。",
            "B": "錯誤。腕隧道症候群壓迫正中神經，常有拇、食、中指麻木刺痛等感覺症狀。",
            "C": "正確。運動神經元疾病以肌無力、萎縮、束顫與錐體束徵象為主，感覺系統相對保留。",
            "D": "錯誤。腰神經根病變常沿皮節分布造成疼痛、麻木或感覺異常。",
        },
        "key_point": "運動神經元病變主要侵犯運動系統，感覺通常保留。",
        "front": "Motor neuron disease / sensory sparing",
        "back": "ALS/MND的考點是上下運動神經元徵象並存，感覺、眼動與括約肌多相對保留。",
        "summary": "感覺最少受侵犯 -> motor neuron disease",
    },
    56: {
        "analysis": "背重物跑步後急性腰痛，合併沿右下肢後側到腳底的放射麻痛，符合腰椎椎間盤突出壓迫神經根造成的坐骨神經痛表現。",
        "options": {
            "A": "錯誤。帶狀皰疹神經炎通常有皮節分布疼痛與水疱皮疹，不會由負重跑步立即誘發典型坐骨神經痛。",
            "B": "錯誤。Guillain-Barre症候群是急性免疫性多發神經根神經病變，常對稱上升性無力，不是單側放射痛。",
            "C": "錯誤。多發性肌炎造成近端肌無力與肌酵素上升，不以腰痛合併皮節放射麻痛為主。",
            "D": "正確。椎間盤突出常因負重或彎腰誘發，壓迫腰薦神經根造成腰痛與下肢放射痛。",
        },
        "key_point": "負重後急性腰痛加後腿至足底放射麻痛，最符合腰椎椎間盤突出壓迫神經根。",
        "front": "負重 / 腰痛 / 坐骨神經痛 / 椎間盤突出",
        "back": "椎間盤突出可造成神經根壓迫，表現為腰痛與沿皮節或坐骨神經分布的下肢放射痛。",
        "summary": "急性腰痛 + 下肢放射痛 -> herniated disc",
    },
    57: {
        "analysis": "右下肢無力合併肚臍以下左側痛溫覺喪失，像Brown-Sequard樣脊髓半側病灶。急性脊髓炎MRI通常病灶T2高訊號、可腫脹或增強；T1高訊號且T2不變不典型。",
        "options": {
            "A": "錯誤，為本題答案。急性脊髓炎較典型是T2 hyperintense病灶，T1高訊號而T2等訊號不符合常見影像表現。",
            "B": "正確。視神經檢查與視神經炎證據可幫助評估NMOSD或其他中樞脫髓鞘疾病。",
            "C": "正確。部分發炎性或免疫性神經病變評估可能見蛋白升高與細胞數不相稱，雖需依臨床鑑別解讀。",
            "D": "正確。Anti-SSA可見於自體免疫疾病相關脊髓炎或NMOSD重疊情境，血液自體抗體檢查有助鑑別。",
        },
        "key_point": "急性脊髓炎MRI典型為T2高訊號；T1高訊號且T2等訊號不是典型描述。",
        "front": "急性脊髓炎 / MRI / T2 hyperintense / Brown-Sequard",
        "back": "脊髓炎常有T2高訊號與脊髓腫脹或增強；同側運動/本體覺、對側痛溫覺異常可呈半切症候群。",
        "summary": "急性脊髓炎MRI -> T2高訊號",
    },
    58: {
        "analysis": "NF1典型包含cafe-au-lait spots、Lisch nodules、皮膚神經纖維瘤等。雙側聽神經瘤是NF2的經典表現，因此不是NF1典型症狀。",
        "options": {
            "A": "錯誤。Lisch nodule是NF1典型眼部表現，為虹膜錯構瘤。",
            "B": "錯誤。咖啡牛奶斑是NF1最常見、最早出現的皮膚線索之一。",
            "C": "正確。雙側聽神經瘤更典型屬NF2，與NF1區分很重要。",
            "D": "錯誤。多發性皮膚神經纖維瘤是NF1典型表現。",
        },
        "key_point": "NF1典型為cafe-au-lait spots、Lisch nodules、神經纖維瘤；雙側聽神經瘤屬NF2。",
        "front": "NF1 vs NF2 / Lisch nodule / bilateral acoustic neuroma",
        "back": "NF1看咖啡牛奶斑、腋下雀斑、Lisch nodules與神經纖維瘤；NF2看雙側前庭神經鞘瘤。",
        "summary": "NF1不是雙側聽神經瘤；那是NF2",
    },
    59: {
        "analysis": "NMOSD常造成縱向延伸性脊髓炎，MRI病灶跨越三個或以上脊髓節段。相較MS，NMOSD視神經炎與脊髓炎常更嚴重，預後未必較好。",
        "options": {
            "A": "正確。脊髓病灶常超過三節，是NMOSD與MS鑑別的重要線索。",
            "B": "錯誤。典型核心症候群是視神經炎、急性脊髓炎、area postrema syndrome等，中樞病灶為主，不以周邊神經病變為典型三聯。",
            "C": "錯誤。NMOSD發作可造成嚴重視力與脊髓功能殘障，預後常比MS差，不能說多可恢復80%以上。",
            "D": "錯誤。NMOSD腦脊髓液可有蛋白或細胞變化，oligoclonal band較MS少見但不能用『不會出現』絕對化。",
        },
        "key_point": "NMOSD脊髓炎常為longitudinally extensive transverse myelitis，病灶跨三節以上。",
        "front": "NMOSD / LETM / 三節以上",
        "back": "NMOSD常有AQP4-IgG相關，視神經炎與縱向廣泛性脊髓炎常嚴重；脊髓病灶跨三節以上是高產考點。",
        "summary": "NMOSD -> 脊髓病灶常超過三節",
    },
    60: {
        "analysis": "神經性梅毒晚期可造成脊髓癆，侵犯後索與後根，表現為閃電樣疼痛、感覺性共濟失調與本體感覺缺失。檢驗上血清VDRL不能單獨確診神經梅毒。",
        "options": {
            "A": "錯誤。血清VDRL陽性只能支持梅毒感染，神經梅毒需合併臨床與腦脊髓液檢查判讀。",
            "B": "錯誤。CSF FTA-ABS敏感度高但治療後可持續陽性，不適合用來監測療效；追蹤常看症狀與CSF細胞數、蛋白、VDRL等。",
            "C": "錯誤。Argyll-Robertson瞳孔是光反射消失但近反射保留，不是近看收縮反射消失。",
            "D": "正確。Tabes dorsalis可造成刀割樣神經痛、感覺性共濟失調與本體感覺缺失。",
        },
        "key_point": "神經性梅毒晚期tabes dorsalis侵犯後索/後根，造成閃電痛、共濟失調與本體感覺缺失。",
        "front": "Neurosyphilis / tabes dorsalis / Argyll Robertson pupil",
        "back": "Tabes dorsalis有閃電痛、感覺性共濟失調與本體覺缺失；Argyll Robertson pupil是accommodation preserved, light reflex absent。",
        "summary": "神經性梅毒 -> tabes dorsalis與後索症狀",
    },
    61: {
        "analysis": "題目問妄想症何者錯誤。妄想症發病年齡範圍廣，平均約中年，個案常缺乏病識感而少主動求醫；性別上不以男性明顯較常見為典型。",
        "options": {
            "A": "正確。妄想症可在成年各年齡發作，平均發病約40歲左右。",
            "B": "正確。因妄想內容常被病人視為真實，缺乏病識感，常由家屬、司法或其他系統帶來就醫。",
            "C": "正確。社交孤立、移民、聽力缺損或壓力等都可能增加妄想形成風險。",
            "D": "錯誤，為本題答案。妄想症沒有典型男性明顯較多的流行病學特徵，部分資料反而女性略多或相近。",
        },
        "key_point": "妄想症平均發病約中年，病識感差且少主動就醫；不以男性較常見為典型。",
        "front": "Delusional disorder / 流行病學 / 病識感差",
        "back": "妄想症可在成人各年齡發作，常因病識感不足而不主動就醫；社交孤立是危險因子。",
        "summary": "妄想症 -> 不典型男性較多",
    },
    62: {
        "analysis": "題目問哪個不是FDA核准治療雙極性疾患急性躁期。Lithium、valproate、carbamazepine可用於躁期；lamotrigine主要用於維持治療與預防憂鬱復發，不適合急性躁期。",
        "options": {
            "A": "錯誤。鋰鹽是急性躁期與維持治療的經典藥物。",
            "B": "錯誤。Carbamazepine可用於急性躁期治療，是情緒穩定劑選項之一。",
            "C": "錯誤。Valproic acid常用於急性躁期，尤其混合特徵或快速循環情境。",
            "D": "正確。Lamotrigine需慢慢滴定以避免嚴重皮疹，主要用於維持期與雙極憂鬱預防，不是急性躁期核准治療重點。",
        },
        "key_point": "Lamotrigine主要用於雙極性疾患維持期，不是急性躁期治療藥物。",
        "front": "Bipolar mania / lithium / valproate / lamotrigine",
        "back": "急性躁期可用lithium、valproate、carbamazepine或抗精神病藥；lamotrigine偏維持與憂鬱期預防。",
        "summary": "急性躁期 -> lamotrigine不是主要核准藥",
    },
    63: {
        "analysis": "題目比較雙極性疾患與重度憂鬱症。雙極性疾患遺傳關聯通常較強；MDD終生盛行率較高且女性較多。雙極性疾患不一定每位都經歷重鬱期，且憂鬱期治療不能單純以抗憂鬱劑為首選。",
        "options": {
            "A": "錯誤。重度憂鬱症終生盛行率通常高於雙極性疾患，不是較低。",
            "B": "錯誤。Bipolar I需有躁期即可診斷，重鬱期常見但不是定義上必須經歷。",
            "C": "正確。重度憂鬱症的家族遺傳關聯性一般低於雙極性疾患，且女性患者較多。",
            "D": "錯誤。雙極性憂鬱治療需避免單用抗憂鬱劑誘發躁期，常以情緒穩定劑或特定抗精神病藥為基礎。",
        },
        "key_point": "MDD較常見且女性較多；雙極性疾患遺傳性較強，治療不能把抗憂鬱劑一律當首選。",
        "front": "Bipolar disorder vs MDD / prevalence / heredity / antidepressant",
        "back": "Bipolar I診斷需要躁期，不一定要有重鬱期；雙極性憂鬱不可隨意單用抗憂鬱劑。",
        "summary": "MDD vs bipolar -> MDD女性多、遺傳性較低",
    },
    64: {
        "analysis": "老年自殺常與憂鬱症、身體疾病、失落與社會孤立相關；自殺死亡男性多於女性，且老年人常使用較致命、激烈的方法，因此說較少採用激烈手段是錯誤的。",
        "options": {
            "A": "正確。憂鬱症是老年自殺最重要且常見的共病精神疾患。",
            "B": "錯誤，為本題答案。老年自殺常計畫性較高、使用較致命方式，死亡率高，不是較少激烈。",
            "C": "正確。自殺死亡率通常男性高於女性，老年男性尤其是高風險族群。",
            "D": "正確。配偶喪失、慢性疼痛、重大身體疾病與功能退化都可誘發自殺危機。",
        },
        "key_point": "老年自殺常與憂鬱、身體疾病與失落相關，且常使用較致命手段；男性死亡多於女性。",
        "front": "老年自殺 / 憂鬱症 / 致命手段 / 男性",
        "back": "老年自殺要特別留意憂鬱症、重大身體病痛、失落與社會孤立；老年男性風險高。",
        "summary": "老年自殺 -> 不少用致命手段",
    },
    65: {
        "analysis": "社交焦慮症核心是害怕被他人負面評價，因而逃避社交或表現場合。通常起病於兒童或青少年期，不是成人早期才初次發生最典型。",
        "options": {
            "A": "正確。害怕被批評、出糗或被負面評價，是社交焦慮症核心認知。",
            "B": "正確。病人常逃避上台、與陌生人互動、聚會或被注視的場合。",
            "C": "正確。許多個案知道害怕過度或不合理，但仍難以控制焦慮與逃避。",
            "D": "錯誤，為本題答案。社交焦慮症通常較早，常在兒童或青少年期開始，不是典型成人早期才初發。",
        },
        "key_point": "社交焦慮症多起於兒童或青少年期，核心是害怕他人負面評價並逃避社交場合。",
        "front": "Social anxiety disorder / onset / negative evaluation",
        "back": "社交焦慮症怕被評價與出糗，常逃避社交；起病多在兒童或青少年期。",
        "summary": "社交焦慮症 -> 不是通常成人早期初發",
    },
    66: {
        "analysis": "認知學說認為情緒反應主要受個體對事件的解讀與想法影響，不是事件本身直接決定情緒。這是CBT的基本前提。",
        "options": {
            "A": "正確。想法、信念與自動化思考是認知學說解釋情緒障礙的核心。",
            "B": "錯誤。同一事件可因不同解讀產生不同情緒，因此事件本身不是最主要因素。",
            "C": "錯誤。結果可能影響情緒，但認知模式強調結果被個體如何理解與評價。",
            "D": "錯誤。潛意識較偏心理動力學觀點，不是認知學說的主要答案。",
        },
        "key_point": "認知學說強調想法與信念影響情緒，治療上會修正自動化思考與認知扭曲。",
        "front": "Cognitive theory / mood disorder / thoughts",
        "back": "不是事件本身，而是人對事件的解讀與想法造成情緒反應；這是認知治療的核心。",
        "summary": "認知學說 -> 情緒受想法影響",
    },
    67: {
        "analysis": "尼古丁戒癮最有效通常是多模式介入：藥物治療搭配行為治療或團體治療，比單靠意志力、簡短建議或單一尼古丁替代療法更好。",
        "options": {
            "A": "錯誤。單靠意志力戒菸成功率低，復發率高。",
            "B": "錯誤。醫師簡短建議有幫助，但效果有限，通常需更完整支持。",
            "C": "錯誤。尼古丁貼片或口香糖有效，但單一替代療法通常不如藥物加心理社會介入。",
            "D": "正確。戒菸藥物合併團體或行為治療，可同時處理生理依賴與行為觸發，成效最好。",
        },
        "key_point": "尼古丁戒癮以藥物治療結合行為/團體治療效果最佳。",
        "front": "Nicotine dependence / cessation / medication + group therapy",
        "back": "戒菸成功率最高的方向是藥物加心理社會支持；單靠意志力或簡短建議效果較差。",
        "summary": "戒菸 -> 藥物合併團體治療最佳",
    },
    68: {
        "analysis": "精神科照會評估拒絕手術病人時，重點是決策能力、理解利弊、拒絕原因與照顧支持。告知手術必要性與成功率屬外科主治醫師的醫療說明責任，不是精神科會談重點。",
        "options": {
            "A": "正確。術後照顧能力會影響病人是否能理解與執行治療計畫，可作為決策能力與支持系統評估的一部分。",
            "B": "正確。精神科需評估病人是否能理解手術利弊、後遺症、替代方案並作出一致決定。",
            "C": "錯誤，為本題答案。手術必要性與成功率的告知主要由外科團隊負責；精神科不應取代原團隊做手術同意說明。",
            "D": "正確。了解拒絕原因可區分價值選擇、資訊不足、憂鬱、妄想、認知障礙或其他影響決策能力的因素。",
        },
        "key_point": "照會精神醫學評估拒絕手術，重點是決策能力與拒絕原因，不是替外科告知手術成功率。",
        "front": "Consultation psychiatry / refusal of surgery / capacity",
        "back": "精神科評估病人是否理解、欣賞、推理並表達穩定選擇；手術必要性與成功率仍由外科說明。",
        "summary": "拒絕手術照會 -> 評估決策能力，不是代替外科告知",
    },
    69: {
        "analysis": "長期高劑量diazepam突然停用會造成benzodiazepine withdrawal。嚴重戒斷可有焦慮、顫抖、失眠、自律神經亢進、譫妄與癲癇發作；diazepam半衰期長，症狀可延後出現。",
        "options": {
            "A": "錯誤。戒斷通常是交感活性上升，較可能心跳變快而不是變慢。",
            "B": "錯誤。Diazepam是長效型benzodiazepine，戒斷症狀可在停藥數天後才明顯出現。",
            "C": "正確。抽搐發作是benzodiazepine戒斷的重要嚴重併發症，長期高劑量者風險更高。",
            "D": "錯誤。嚴重benzodiazepine戒斷可產生譫妄、幻覺甚至癲癇，不能說不致於譫妄。",
        },
        "key_point": "長期高劑量benzodiazepine突然停用可造成嚴重戒斷，包含譫妄與癲癇發作；長效藥可延後出現。",
        "front": "Diazepam withdrawal / seizure / delirium / long-acting",
        "back": "BZD需逐漸減量；突然停用可出現焦慮、顫抖、失眠、自律神經亢進、譫妄與癲癇。",
        "summary": "BZD戒斷 -> 癲癇是嚴重症狀",
    },
    70: {
        "analysis": "8歲兒童搬家換學校後害怕與父母分離、擔心父母不來接、抗拒上學且做分離惡夢，最符合分離焦慮症。若需要藥物治療，可選SSRI等具血清素回收抑制效果的抗憂鬱劑。",
        "options": {
            "A": "錯誤。廣泛性焦慮症是多面向過度擔憂；本題焦慮集中在與父母分離與上學分離情境。",
            "B": "錯誤。第一線心理治療通常是認知行為治療、暴露與親職介入，不是精神分析性心理治療。",
            "C": "正確。症狀嚴重或心理治療不足時，可使用SSRI作為藥物治療選擇。",
            "D": "錯誤。家長衛教與家庭介入應早期同步進行，不需等症狀明顯改善後才做。",
        },
        "key_point": "兒童分離焦慮症以害怕與依附對象分離為核心；治療以CBT與家庭介入為主，必要時可用SSRI。",
        "front": "Separation anxiety disorder / school refusal / SSRI",
        "back": "分離焦慮常見上學前哭鬧、擔心父母出事、分離惡夢與身體不適；治療可用CBT、家長介入與SSRI。",
        "summary": "分離焦慮症 -> 必要時SSRI",
    },
    71: {
        "analysis": "題目問妥瑞氏症何者錯誤。Tourette disorder需有多個動作tic與至少一個聲音tic，病程超過一年，且起病在18歲以前；不是12歲以前。",
        "options": {
            "A": "正確。診斷需多個動作抽搐與至少一個聲音抽搐，但兩者不一定同時出現。",
            "B": "錯誤，為本題答案。診斷標準是18歲以前發病，選項說12歲前過於嚴格。",
            "C": "正確。症狀造成明顯困擾時，可用低劑量抗精神病藥物如aripiprazole、risperidone或haloperidol。",
            "D": "正確。妥瑞氏症男性多於女性，是常見流行病學特徵。",
        },
        "key_point": "Tourette disorder需動作與聲音tic、病程超過一年，且18歲以前發病。",
        "front": "Tourette disorder / motor tic / vocal tic / onset before 18",
        "back": "妥瑞氏症不是12歲前，而是18歲前發病；可用行為治療與低劑量抗精神病藥物。",
        "summary": "妥瑞氏症 -> 18歲以前發病",
    },
    72: {
        "analysis": "ADHD過動衝動症狀常隨年齡較早改善，但注意力問題可能延續到成人，且物質使用共病風險較高。治療統合分析並不支持非藥物治療遠優於藥物治療。",
        "options": {
            "A": "正確。過動與衝動常比注意力缺陷更容易隨年齡下降。",
            "B": "正確。部分ADHD患者到成人仍有注意力、執行功能與組織能力困難。",
            "C": "錯誤，為本題答案。藥物治療，尤其刺激劑，對核心症狀效果明確；非藥物治療不是遠優於藥物。",
            "D": "正確。ADHD與物質使用疾患、行為問題、焦慮或情緒疾患等共病風險增加。",
        },
        "key_point": "ADHD藥物治療對核心症狀效果明確；非藥物治療並非遠優於藥物治療。",
        "front": "ADHD / treatment / stimulant / adult attention symptoms",
        "back": "ADHD過動可改善較早，注意力問題可持續；治療上藥物對核心症狀效果強，常搭配行為介入。",
        "summary": "ADHD治療 -> 藥物療效不弱於非藥物",
    },
    73: {
        "analysis": "Narcolepsy的白天嗜睡可用促醒藥物治療。選項中modafinil是被FDA認可用於治療嗜睡症白天過度嗜睡的藥物。",
        "options": {
            "A": "錯誤。Clozapine是抗精神病藥，與嗜睡症治療無關且可能造成嗜睡。",
            "B": "錯誤。Lorazepam是benzodiazepine，具鎮靜效果，不是治療narcolepsy的促醒藥。",
            "C": "錯誤。Lithium用於雙極性疾患等情境，不是narcolepsy標準治療。",
            "D": "正確。Modafinil可促進清醒，是narcolepsy日間嗜睡常用且核准的治療藥物。",
        },
        "key_point": "Modafinil可用於narcolepsy的日間過度嗜睡治療。",
        "front": "Narcolepsy / modafinil",
        "back": "嗜睡症白天過度嗜睡可用modafinil等促醒藥物；猝倒另依情況治療。",
        "summary": "Narcolepsy -> modafinil",
    },
    74: {
        "analysis": "題目問酒精相關障礙何者錯誤。酒精可幫助入睡但會破壞睡眠結構，增加夜間醒來，減少REM與深睡期品質，因此說減少睡眠中斷、增加REM與stage 4 sleep是錯的。",
        "options": {
            "A": "正確。酒精使用疾患常共病其他物質使用、反社會人格、情感性疾患與焦慮疾患。",
            "B": "正確。酒精戒斷可有手抖、焦慮、噁心、幻覺、癲癇，嚴重可譫妄震顫。",
            "C": "正確。Benzodiazepines是酒精戒斷治療首選，可降低癲癇與譫妄風險。",
            "D": "錯誤，為本題答案。酒精雖可縮短入睡時間，但會造成睡眠片段化，抑制REM並降低深睡品質。",
        },
        "key_point": "酒精會破壞睡眠結構並使睡眠片段化；戒斷治療首選benzodiazepines。",
        "front": "Alcohol / withdrawal / benzodiazepines / sleep architecture",
        "back": "酒精戒斷可手抖、焦慮、幻覺、癲癇；治療首選BZD。酒精不會改善睡眠品質，反而使睡眠中斷。",
        "summary": "酒精 -> 入睡快但睡眠品質差",
    },
    75: {
        "analysis": "睡眠驚恐與夢遊屬NREM parasomnia，常發生於前半夜的深睡期；夢魘則多發生於REM睡眠，常在後半夜。",
        "options": {
            "A": "錯誤。睡眠驚恐多在前半夜深層NREM睡眠，不是後半夜。",
            "B": "錯誤。夢遊主要發生於NREM深睡期，不是REM期。",
            "C": "錯誤。夢魘主要發生於REM睡眠，醒後常記得夢境內容。",
            "D": "正確。睡眠驚恐常發生於非快速動眼期的深睡期，病人可尖叫、驚恐且醒後記憶少。",
        },
        "key_point": "睡眠驚恐與夢遊發生於深層NREM，夢魘發生於REM。",
        "front": "Sleep terror / NREM deep sleep / nightmare REM",
        "back": "NREM parasomnia包含睡眠驚恐與夢遊，常在前半夜；REM夢魘多在後半夜且醒後記得。",
        "summary": "睡眠驚恐 -> deep NREM",
    },
    76: {
        "analysis": "腹部鈍傷後懷疑肝臟血管傷害或出血，穩定病人首選影像通常是對比增強電腦斷層，可快速評估肝臟裂傷、血腫、活動性出血與其他腹內傷害。",
        "options": {
            "A": "錯誤。血管攝影可用於診斷兼栓塞治療，但通常不是初步最優先的整體腹部評估工具。",
            "B": "正確。電腦斷層掃描是鈍傷性腹部臟器與血管傷害評估的優先影像。",
            "C": "錯誤。MRI耗時且急診可近性較差，不適合作為急性腹部創傷首選。",
            "D": "錯誤。同位素肝臟掃描不適合急性創傷出血評估。",
        },
        "key_point": "穩定腹部鈍傷懷疑肝臟血管傷害，優先做對比增強CT。",
        "front": "腹部鈍傷 / 肝臟出血 / CT",
        "back": "急性腹部創傷要快速評估實質器官與活動性出血，對比CT最實用；血管攝影偏治療性栓塞。",
        "summary": "肝臟創傷血管傷害 -> CT優先",
    },
    77: {
        "analysis": "發燒合併macules、papules、vesicles不同階段皮疹，是水痘典型表現。水痘在出疹前1-2天就有傳染力，因此說疹子出現後才開始傳染最不恰當。",
        "options": {
            "A": "正確。水痘由varicella-zoster virus引起，屬Herpesviridae。",
            "B": "錯誤，為本題答案。水痘在出疹前即具傳染性，並持續到所有病灶結痂。",
            "C": "正確。水痘可併發腦炎、肺炎、細菌性皮膚感染等，成人或免疫低下更需警覺。",
            "D": "正確。兒童病毒感染尤其水痘或流感應避免aspirin，以免增加Reye syndrome風險。",
        },
        "key_point": "水痘出疹前1-2天已具傳染性，直到所有病灶結痂；避免使用aspirin。",
        "front": "Varicella / macule papule vesicle / contagious before rash / aspirin",
        "back": "水痘皮疹可同時有不同階段病灶；傳染期從出疹前開始到結痂，避免aspirin以防Reye syndrome。",
        "summary": "水痘 -> 出疹前已具傳染性",
    },
    78: {
        "analysis": "急性缺血性中風多數血壓會因疼痛、焦慮、顱壓等因素上升，通常不急著降壓；若未接受rt-PA，降壓門檻比200/100更高。rt-PA符合條件可改善預後，最大劑量90 mg。",
        "options": {
            "A": "正確。許多中風病人的血壓在疼痛、躁動、顱壓與壓力改善後會下降，過早降太低可能影響腦灌流。",
            "B": "錯誤，為本題答案。缺血性中風若不溶栓，通常需更高血壓才急降；200/100以上就緊急降壓過度籠統且門檻不對。",
            "C": "正確。發病3小時內且符合適應症的缺血性中風，rt-PA可改善神經學預後。",
            "D": "正確。Alteplase劑量常為0.9 mg/kg，最大劑量90 mg。",
        },
        "key_point": "急性缺血性中風未溶栓時避免過度降壓；rt-PA劑量0.9 mg/kg、最大90 mg。",
        "front": "Acute ischemic stroke / BP control / rt-PA 90 mg",
        "back": "缺血性中風血壓控制要保留腦灌流；溶栓者需降到較低門檻，未溶栓者通常門檻更高。",
        "summary": "缺血性中風血壓 -> 不可200/100就一律急降",
    },
    79: {
        "analysis": "本題考病人自主與拒絕輸血。成年且有行為能力者，若有明確文書證據表達拒絕輸血，即使情況危及生命，醫師原則上應尊重其自主決定；兒童與未成年人則需以最佳利益保護為核心。",
        "options": {
            "A": "正確。具行為能力成年病人有清楚拒絕輸血意願時，醫師應尊重其自主，即使緊急且不輸血可能死亡。",
            "B": "錯誤。懷孕36週涉及母體自主與胎兒利益的複雜衝突，不能作為本題最明確應尊重拒絕輸血的單純情境。",
            "C": "錯誤。15歲未成年人拒絕救命輸血時，醫師需評估法律、父母代理與未成年人最佳利益，不能單純等同成年自主。",
            "D": "錯誤。父母不能以宗教理由替8歲病童拒絕必要救命治療；兒童最佳利益可優先於父母決定。",
        },
        "key_point": "具行為能力成年病人若有明確拒絕輸血意願，應尊重其自主；未成年病童以最佳利益為核心。",
        "front": "Jehovah's Witness / refusal of blood / adult capacity / child best interest",
        "back": "成年有能力且有清楚文書拒絕輸血時，醫師原則上尊重；未成年人或兒童不可任意拒絕救命治療。",
        "summary": "拒絕輸血 -> 成年有能力且明確意願才最能尊重",
    },
    80: {
        "analysis": "早產兒長期呼吸器依賴、慢性腎衰竭、腹膜透析與黴菌性腹膜炎，整體預後極差且治療負擔高。若經充分溝通、取得父母同意並符合法規與倫理程序，可轉向緩和醫療，由醫療團隊撤除維生治療以減輕痛苦。",
        "options": {
            "A": "錯誤。父母是代理決策者，但撤除呼吸器應由醫療團隊依程序執行，不是要求父母親自移除。",
            "B": "正確。在病童最佳利益、充分告知與同意下，施予緩和醫療並由醫護人員撤除呼吸器是較合適作法。",
            "C": "錯誤。若治療已高度無效且只增加痛苦，倫理上不必無限度使用所有醫療手段搶救到最後。",
            "D": "錯誤。只停止手術但保留長期維生治療，可能延長痛苦且未完整回應家庭與病童最佳利益；需整體緩和照護計畫。",
        },
        "key_point": "重症新生兒若預後極差且治療負擔高，經父母同意與醫療團隊程序，可轉向緩和醫療並撤除維生治療。",
        "front": "重症新生兒 / 緩和醫療 / withdrawal of ventilator / 父母同意",
        "back": "撤除維生治療不是放棄照護，而是轉向緩和醫療；需以病童最佳利益、充分溝通與程序正義為核心。",
        "summary": "重症新生兒末期照護 -> 父母同意後醫療團隊施行緩和撤除",
    },
}


def load_source():
    return json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))["questions"]


def update_from_question(q):
    qnum = q["question_number"]
    rewrite = REWRITES.get(qnum)
    if rewrite:
        explanation = make_explanation(rewrite["analysis"], rewrite["options"], rewrite["core"] if "core" in rewrite else rewrite["key_point"])
        return {
            "question_id": q["id"],
            "question_number": qnum,
            "explanation": explanation,
            "key_point": rewrite["key_point"],
            "flashcard_front": rewrite["front"],
            "flashcard_back": rewrite["back"],
            "flashcard_summary": rewrite["summary"],
            "review_status": "ai_generated",
            "explanation_model": "codex-high-quality-rewrite",
            "explanation_generated_at": STAMP,
            "manual_review_notes": rewrite.get("notes", []),
        }
    return {
        "question_id": q["id"],
        "question_number": qnum,
        "explanation": q["explanation"],
        "key_point": q.get("key_point", ""),
        "flashcard_front": q.get("flashcard_front", ""),
        "flashcard_back": q.get("flashcard_back", ""),
        "flashcard_summary": q.get("flashcard_summary", ""),
        "review_status": "ai_generated",
        "explanation_model": "codex-high-quality-rewrite",
        "explanation_generated_at": STAMP,
        "manual_review_notes": [],
    }


def main():
    questions = load_source()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for start in range(1, 81, 10):
        end = start + 9
        block = [update_from_question(q) for q in questions if start <= q["question_number"] <= end]
        data = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": block,
        }
        out = OUT_DIR / f"q{start:03d}-q{end:03d}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{out}: {len(block)} updates")


if __name__ == "__main__":
    main()
