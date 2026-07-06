import json
import os

todo_path = r"d:\Antigravity\med_exam_public\scratch\113-2_medicine-5\batch_02_todo.json"
done_path = r"d:\Antigravity\med_exam_public\scratch\113-2_medicine-5\batch_02_done.json"

explanations = {
    "113-2_medicine-5_011": {
        "explanation": """【題幹解析】
本題考查 L5 神經根的解剖與臨床定位。L5 神經根受損會導致其支配的肌群無力與皮節感覺異常，臨床上常以垂足與足背感覺減退來呈現。

【選項詳解】
- A. 錯誤。L5 神經根是沿著 L5 椎骨下方的椎間孔（L5-S1 椎間孔）出神經孔，而非 L4 椎莖下方或 L4-5 椎間孔。L4 神經根才是從 L4-5 椎間孔穿出。
- B. 錯誤。L5 的感覺皮節（dermatome）分布主要在小腿前外側、足背及大拇趾；而大腿後外側、小腿後側及外側足踝則主要由 S1 或 S2 神經根支配。
- C. 正確。脛前肌（tibialis anterior）主要由 L5 神經根（以及部分 L4）支配，負責足背屈（dorsiflexion）。當 L5 神經根受損時，脛前肌無力會導致患者無法主動背屈，臨床上呈現垂足（drop foot）表現。
- D. 錯誤。膝反射（patellar reflex / knee jerk）主要由 L4 神經根支配，L5 神經根病變通常不會影響膝反射。踝反射（ankle jerk）則由 S1 神經根支配。

【核心考點】
L5 神經根病變的典型表現為垂足（脛前肌無力）與足背感覺異常，其不影響膝反射（L4）與踝反射（S1）。""",
        "key_point": "L5受損致垂足，不影響膝踝反射",
        "flashcard_front": "L5 神經根受損時，患者最典型的運動功能障礙與感覺異常部位為何？",
        "flashcard_back": "運動功能障礙為垂足（drop foot，因脛前肌無力導致足背屈困難）；感覺異常主要分布在小腿前外側與足背。",
        "flashcard_summary": "L5 神經根支配脛前肌，受損時會導致垂足與足背感覺異常。"
    },
    "113-2_medicine-5_012": {
        "explanation": """【題幹解析】
本題評估輕中度創傷性腦損傷（GCS 13分）且少量實質內出血（額葉 10 c.c.）患者的急性期處置原則。此時患者狀況穩定且無腦壓嚴重增高或腦疝跡象，應優先採取保守治療而非侵入性手術。

【選項詳解】
- A. 正確。對於創傷性腦出血患者，在受傷後第一週內預防性投與抗癲癇藥物（如 Levetiracetam 或 Phenytoin）可以有效降低早期創傷後癲癇（early post-traumatic seizures）的發生率。
- B. 正確。將動脈血二氧化碳分壓（PaCO2）維持在正常偏低範圍（35~40 mmHg）是標準做法，可微幅收縮腦血管以降腦壓，同時避免因過度換氣（hyperventilation）導致 PaCO2 過低而引起嚴重的腦缺血。
- C. 錯誤。病患昏迷指數為 13 分，且額葉出血量僅 10 c.c.，並無大量血塊造成的質量效應（mass effect）或中線偏移。在此情況下，進行開顱手術（craniotomy）移除血塊是不適當的，應採取內科保守觀察。
- D. 正確。維持足夠的體循環血壓對於維持腦灌流壓（CPP）極為重要。臨床指引建議維持收縮壓在 100 mmHg 以上（50-69歲患者建議 >100 mmHg，其他年齡層甚至建議 >110 mmHg），以防止繼發性腦部缺血損傷。""",
        "key_point": "輕度腦出血免開顱，維持血壓與血氣",
        "flashcard_front": "頭部外傷 GCS 13分、額葉出血 10 c.c.，是否需要立即進行開顱手術？為什麼？",
        "flashcard_back": "不需要。因為患者意識尚清醒（GCS 13分）且出血量極小（10 c.c.，未達 30 c.c. 的手術指引標準），無明顯腦壓增高或腦疝風險，首選內科保守觀察。",
        "flashcard_summary": "輕微創傷性腦出血（<30 c.c.）無手術適應症，應以內科保守治療為主。"
    },
    "113-2_medicine-5_013": {
        "explanation": """【題幹解析】
本題考查單一顱縫早閉症中「舟形頭（scaphocephaly）」的病理生理特徵與臨床關聯。舟形頭大多屬於非綜合症性的孤立性病變，預後通常良好。

【選項詳解】
- A. 錯誤。舟形頭是由於「矢狀縫（sagittal suture）」過早融合所造成，導致頭骨橫向發育受限而代償性地向前後生長。冠狀縫（coronal suture）過早黏合則會導致短頭症（brachycephaly）。
- B. 錯誤。眼球突出通常見於侵犯雙側冠狀縫的綜合症型顱縫早閉（如 Crouzon 或 Apert 症候群），在單純矢狀縫黏合的舟形頭中非常罕見。
- C. 正確。舟形頭多為非綜合症性（non-syndromic）的單一顱縫黏合，通常不會合併中臉部發育不良，因此不常合併上頜骨發育不全（maxillary hypoplasia）。
- D. 錯誤。單一顱縫融合的患者，由於其他未融合的顱縫仍能代償性擴展，因此極少合併水腦症（hydrocephalus）或嚴重的顱內壓升高。""",
        "key_point": "舟形頭因矢狀縫早閉，多為孤立病變",
        "flashcard_front": "舟形頭（scaphocephaly）是由哪條顱縫過早融合引起？是否常合併其他系統性發育異常？",
        "flashcard_back": "由「矢狀縫」（sagittal suture）過早融合引起。它大多為非綜合症性的孤立病變，因此不常合併眼球突出、上頜骨發育不全或水腦症。",
        "flashcard_summary": "舟形頭起因於矢狀縫早閉，通常無其他中臉部或神經發育異常。"
    },
    "113-2_medicine-5_014": {
        "explanation": """【題幹解析】
本題考查手指伸肌腱不同部位斷裂所導致的典型臨床畸形。手指遠端指間關節（DIP）的伸指肌腱附著於末節指骨基部，此處斷裂會使 DIP 關節無法伸直。

【選項詳解】
- A. 正確。手指遠端伸指肌腱（附著於末節指骨基部）斷裂或撕裂，會導致遠端指間關節（DIP）失去伸直功能，使手指末端呈現被動彎曲的狀態，臨床上稱為槌狀指（mallet finger）。
- B. 錯誤。天鵝頸畸形（swan-neck deformity）的特徵是近端指間關節（PIP）過伸，同時遠端指間關節（DIP）屈曲。主要與側束移位或掌側板鬆弛有關，非遠端伸肌腱直接斷裂所致。
- C. 錯誤。鈕扣孔畸形（boutonnière deformity）是由於近端指間關節（PIP）處的伸肌腱中央束（central slip）斷裂，導致 PIP 屈曲、DIP 過伸。
- D. 錯誤。獵人指（gamekeeper's thumb）是指大拇指掌指關節（MCP）的尺側副韌帶（UCL）受損，與 DIP 伸肌腱無關。""",
        "key_point": "遠端伸肌腱斷裂導致槌狀指",
        "flashcard_front": "槌狀指（mallet finger）與鈕扣孔畸形（boutonnière deformity）在伸肌腱受損部位上有何不同？",
        "flashcard_back": "槌狀指是「遠端伸肌腱（DIP關節基部）」斷裂，導致 DIP 無法伸直；鈕扣孔畸形是「伸肌腱中央束（PIP關節處）」斷裂，導致 PIP 屈曲、DIP 過伸。",
        "flashcard_summary": "遠端伸肌腱斷裂引發槌狀指，中央束斷裂引發鈕扣孔畸形。"
    },
    "113-2_medicine-5_015": {
        "explanation": """【題幹解析】
本題考查整形外科中筋膜皮瓣（fasciocutaneous flap）的 Mathes-Nahai 解剖分類。該分類法根據血管供應的來源與走行路徑，將筋膜皮瓣分為 A、B、C 三類。

【選項詳解】
- A. 錯誤。第 A 類（Type A）皮瓣是由直接皮膚動脈（direct cutaneous artery）所支配，血管直接進入皮下，如腹股溝皮瓣（groin flap）或顳頂筋膜皮瓣（temporoparietal fascia flap）。
- B. 正確。第 B 類（Type B）皮瓣是由肌間隔穿支（septocutaneous perforator）所支配，血管走行於肌間隔中並發出分支供應皮膚。橈動脈前臂皮瓣（radial forearm flap）的血供即來自走在肌間隔中的橈動脈隔穿支，故屬於第 B 類。
- C. 錯誤。第 C 類（Type C）皮瓣是由肌皮穿支（musculocutaneous perforator）所支配，血管須穿過肌肉本體後才到達皮下，如大腿前外側皮瓣（ALT flap）常以肌皮穿支為主要血供。
- D. 錯誤。在 Mathes-Nahai 對於「筋膜皮瓣」的分類中，僅有 A、B、C 三類，並沒有第 D 類的劃分（第 D 類或 Type IV/V 僅存在於肌皮瓣 musculocutaneous flap 的分類中）。""",
        "key_point": "橈動脈前臂皮瓣屬B類肌間隔穿支",
        "flashcard_front": "在 Mathes-Nahai 筋膜皮瓣分類中，橈動脈前臂皮瓣（radial forearm flap）屬於哪一類？其血管解剖特徵為何？",
        "flashcard_back": "屬於第 B 類（Type B）。其解剖特徵是由肌間隔穿支（septocutaneous perforator，即源自橈動脈的隔穿支）來供應血流。",
        "flashcard_summary": "橈動脈前臂皮瓣為 Type B 筋膜皮瓣，由肌間隔穿支供血。"
    },
    "113-2_medicine-5_016": {
        "explanation": """【題幹解析】
本題考查頸部淋巴結分區（neck levels）的解剖學邊界。頭頸癌患者的淋巴結轉移位置是決定治療與手術範圍的關鍵。

【選項詳解】
- A. 正確。Level IA（頦下區，submental group）的解剖範圍是由雙側二腹肌前腹（anterior belly of the digastric muscle）、舌骨（hyoid bone）以及正中線（midline）所圍成的三角形區域。題幹中描述的腫塊位置完全符合此解剖邊界。
- B. 錯誤。Level IIA（頸深上組前部）位於舌骨上緣水平以上、胸鎖乳突肌後緣與副神經前方，不與二腹肌前腹或中線相鄰。
- C. 錯誤。Level IIB（頸深上組後部）位於副神經後上方，靠近顱底與胸鎖乳突肌深面。
- D. 錯誤。Level III（頸深中組）的解剖範圍為舌骨下緣至環狀軟骨下緣（cricoid cartilage）水平之間的頸內靜脈周圍淋巴結。""",
        "key_point": "Level IA位於二腹肌前腹與舌骨間",
        "flashcard_front": "頸部淋巴結 Level IA (頦下區) 與 Level IB (頜下區) 的解剖邊界分別為何？",
        "flashcard_back": "Level IA 邊界為雙側二腹肌前腹、舌骨與正中線；Level IB 邊界為二腹肌前腹、後腹與下頜骨下緣。",
        "flashcard_summary": "Level IA 位於二腹肌前腹與舌骨間的中線區，是頦下淋巴結所在地。"
    },
    "113-2_medicine-5_017": {
        "explanation": """【題幹解析】
本題考查 AJCC 第八版（8th edition）口腔癌（包含舌癌）的 TNM 分期診斷。相較於舊版，第八版在 T 分期引入了「侵犯深度（DOI）」作為升級指標，在 N 分期則強調了淋巴結的數量、側位與「囊外延伸（ENE）」狀態。

【選項詳解】
- T 分期判定：腫瘤最大徑為 3 cm（落於 2~4 cm 區間），但侵犯深度（DOI）高達 11 mm。根據 AJCC 第八版口腔癌指南，不論腫瘤大小，只要 DOI > 10 mm 即被判定為 T3。因此郭先生為 T3。
- N 分期判定：在同側頸部發現 3 顆轉移淋巴結（複數同側轉移，屬於多發性同側淋巴結），最大徑為 2 cm（均未超過 6 cm），且無囊外淋巴結延伸（extranodal extension, ENE-）。根據指引，同側多個淋巴結轉移、最大徑 ≤ 6 cm 且 ENE 陰性者，定義為 N2b。因此郭先生為 N2b。
- M 分期判定：無遠端器官轉移，判定為 M0。
- 綜合以上，郭先生的癌症分期為 T3N2bM0，故 D 選項為正確。而 A（N2a 為單顆同側 >3 cm 且 ≤6 cm，ENE-）、B 與 C（N2c 為雙側或對側淋巴結轉移）均為錯誤的分期。""",
        "key_point": "DOI>10mm為T3；同側多發為N2b",
        "flashcard_front": "在 AJCC 第八版中，口腔癌 T3 與 N2b 的分期定義分別為何？",
        "flashcard_back": "T3 定義為腫瘤最大徑 > 4 cm，或任何大小伴隨侵犯深度（DOI）> 10 mm；N2b 定義為同側多個轉移淋巴結且最大徑 ≤ 6 cm，同時無囊外延伸（ENE-）。",
        "flashcard_summary": "口腔癌 DOI > 10 mm 升為 T3；同側多顆 ≤ 6 cm 且 ENE- 歸為 N2b。"
    },
    "113-2_medicine-5_018": {
        "explanation": """【題幹解析】
本題考查壓瘡（褥瘡，pressure sore）的分級與重建手術選擇。當壓瘡病變深及骨頭，定義上屬於最嚴重的第四期，此時重建需提供具緩衝力且血循豐富的局部皮瓣來覆蓋外露的骨組織。

【選項詳解】
- A. 錯誤。Stage II 壓瘡僅涉及表皮或部分真皮缺損，臨床上表現為淺表潰瘍或水泡，不會深及骨頭，且通常不需要手術，更無法直接縫合深部壞死傷口。
- B. 錯誤。Stage III 壓瘡雖為全皮層缺損，但骨頭與肌肉尚未暴露。對於深及骨頭的傷口，由於骨頭缺乏血流，直接進行植皮（skin graft）無法存活，且植皮無法提供足夠的抗壓緩衝。
- C. 正確。Stage IV 壓瘡的定義為全皮層缺損且伴隨骨頭、肌腱或肌肉外露。題幹中「深及骨頭」符合 Stage IV。最好的重建方式是徹底清創後，使用具有良好血流與足夠厚度組織墊的局部皮瓣（如局部臀大肌皮瓣重建術，gluteus maximus flap）來覆蓋骨頭，以減少日後壓迫復發的機率。
- D. 錯誤。壓瘡的臨床分級系統中並不存在「Stage V」的分類。此外，壓瘡重建以局部皮瓣（local flap）為首選，不需要動用顯微吻合血管的自由皮瓣（free flap）重建。""",
        "key_point": "深及骨頭為Stage IV首選局部皮瓣",
        "flashcard_front": "深及骨頭的臀部壓瘡屬於第幾期？最佳的重建手術方式為何？",
        "flashcard_back": "屬於 Stage IV。最佳重建方式是「清創後以局部臀大肌皮瓣（或其他局部皮瓣）進行重建」，以提供血循良好且夠厚的軟組織墊覆蓋骨頭。植皮或直接縫合不適用。",
        "flashcard_summary": "深及骨頭屬 Stage IV 壓瘡，重建首選局部臀大肌皮瓣以提供緩衝。"
    },
    "113-2_medicine-5_019": {
        "explanation": """【題幹解析】
本題考查二尖瓣閉鎖不全（mitral regurgitation, MR）的病因、病理生理學、物理診斷（聽診）及影像學表現。掌握瓣膜性心臟病在收縮期與舒張期的心雜音差異是臨床評估的基礎。

【選項詳解】
- A. 正確。二尖瓣閉鎖不全（MR）的病因分為原發性與繼發性，常見病因包括黏液樣變性（myxomatous degeneration，與二尖瓣脫垂 MVP 密切相關）、風濕性心臟病（rheumatic heart disease）以及感染性心內膜炎（infective endocarditis）造成的瓣膜穿孔或腱索斷裂。
- B. 錯誤。二尖瓣閉鎖不全發生於心室收縮期，此時左心室的高壓使血液逆流入左心房，因此聽診的典型表現為全收縮期雜音（holosystolic 或 pan-systolic murmur），於心尖處最響亮且向左腋下傳導。而非全舒張期雜音（pan-diastolic murmur）。因此本選項敘述錯誤。
- C. 正確。在慢性二尖瓣閉鎖不全中，左心室與左心房會通過離心性肥大與擴張進行代償重塑，以維持足夠的每搏輸出量（stroke volume）並緩衝左心房壓力的上升，因此患者在早期至中期可能完全沒有自覺症狀。
- D. 正確。當二尖瓣閉鎖不全進入失代償期，逆流的血液會導致左心房顯著擴大，且壓力逆傳回肺循環，造成肺靜脈壓升高，胸部 X 光上可觀察到左心房擴大（雙重陰影、支氣管分叉角度變大）與肺淤血或肺水腫的變化。""",
        "key_point": "MR雜音為心尖全收縮期雜音",
        "flashcard_front": "二尖瓣閉鎖不全（MR）的典型心雜音為何？其特徵與傳導方向是什麼？",
        "flashcard_back": "典型心雜音為「全收縮期雜音」（holosystolic/pansystolic murmur）。其特徵是在「心尖處（apex）」最響亮，並且會向「左側腋下（left axilla）」傳導。",
        "flashcard_summary": "二尖瓣閉鎖不全的聽診特徵為向腋下傳導的心尖全收縮期雜音。"
    },
    "113-2_medicine-5_020": {
        "explanation": """【題幹解析】
本題考查冠狀動脈繞道手術（CABG）中雙側內乳動脈（Bilateral Internal Mammary Artery, BIMA）的使用適應症與禁忌症。剝離雙側內乳動脈會減少胸骨血供，增加深部胸骨感染（DSWI）與胸骨裂開的風險，因此需排除高危患者。

【選項詳解】
- A. 正確。此患者 60 歲相對年輕（能從 BIMA 獲得長期暢通的存活益處），且其慢性肺阻塞疾病（COPD）僅使用吸入型支氣管擴張劑（代表病情控制穩定，無長期全身性類固醇使用，咳嗽不嚴重），胸骨癒合不良的風險較低，是四個選項中最適合使用 BIMA 的患者。
- B. 不適合。該患者體重過重，身體質量指數（BMI）達 35，屬於重度肥胖。肥胖是術後胸骨裂開與深部胸骨切口感染（DSWI）的強烈獨立危險因子，通常應避免剝離雙側內乳動脈。
- C. 不適合。患者有末期腎病變（ESRD，傷口癒合極差，血管鈣化嚴重）；更重要的是，雙手收縮壓相差達 50 mmHg 提示存在嚴重的鎖骨下動脈狹窄（subclavian artery stenosis）。由於內乳動脈起源於鎖骨下動脈，狹窄側的內乳動脈血流量會嚴重不足，無法提供足夠的冠狀動脈灌流。
- D. 不適合。患者為 90 歲之超高齡（骨質疏鬆、胸骨強度低、預期壽命較短，難以凸顯 BIMA 的長期通暢優勢），且糖化血色素（HbA1c）為 8.0% 代表糖尿病控制不佳，此二者皆會極大化術後傷口不癒合與嚴重感染的機率。""",
        "key_point": "BIMA禁忌：肥胖、糖控差、雙手壓差大",
        "flashcard_front": "在冠狀動脈繞道手術（CABG）中，使用雙側內乳動脈（BIMA）的主要限制與禁忌症為何？",
        "flashcard_back": "主要限制是會減少胸骨血供，增加深部胸骨切口感染（DSWI）與裂開風險。禁忌症包括：重度肥胖（BMI>35）、糖尿病控制差（HbA1c>8%）、超高齡、末期腎病及鎖骨下動脈狹窄（雙手收縮壓相差大）。",
        "flashcard_summary": "BIMA 因減少胸骨血供，禁忌於重度肥胖、糖控差、末期腎病與鎖骨下動脈狹窄者。"
    }
}

with open(todo_path, "r", encoding="utf-8") as f:
    todo_data = json.load(f)

done_items = []
for q in todo_data["questions"]:
    qid = q["id"]
    ans = q["correct_answer"]
    
    if qid in explanations:
        exp_data = explanations[qid]
        item = {
            "question_id": qid,
            "correct_answer": ans,
            "explanation": exp_data["explanation"],
            "key_point": exp_data["key_point"],
            "flashcard_front": exp_data["flashcard_front"],
            "flashcard_back": exp_data["flashcard_back"],
            "flashcard_summary": exp_data["flashcard_summary"]
        }
        done_items.append(item)
    else:
        print(f"Warning: {qid} not found in explanations!")

done_data = {
    "year": todo_data["year"],
    "subject": todo_data["subject"],
    "batch_id": todo_data["batch_id"],
    "items": done_items
}

# Ensure directory exists
os.makedirs(os.path.dirname(done_path), exist_ok=True)

with open(done_path, "w", encoding="utf-8") as f:
    json.dump(done_data, f, ensure_ascii=False, indent=2)

print("Done! batch_02_done.json has been written successfully.")
