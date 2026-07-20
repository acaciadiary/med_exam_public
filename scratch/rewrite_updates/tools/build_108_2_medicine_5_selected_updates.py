import copy
import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/108-2/medicine-5.json"
DATASET_ID = "108-2_medicine-5"
OUT_DIR = Path("scratch/rewrite_updates/108-2_medicine-5_selected")
STAMP = "2026-07-20T18:20:00+08:00"

TARGET_BATCHES = [
    ("q007-q036_selected01.json", 7, 36, [7, 19, 23, 26, 29, 31, 32, 34, 35, 36]),
    ("q038-q045_selected02.json", 38, 45, [38, 39, 40, 41, 42, 43, 44, 45]),
    ("q051-q067_selected03.json", 51, 67, [51, 52, 58, 59, 60, 61, 62, 65, 66, 67]),
    ("q073-q080_selected04.json", 73, 80, [73, 75, 76, 80]),
]

MERGE_FIELDS = {
    "explanation",
    "key_point",
    "flashcard_front",
    "flashcard_back",
    "flashcard_summary",
    "review_status",
    "explanation_model",
    "explanation_generated_at",
}

IMMUTABLE_FIELDS = {
    "id",
    "question_number",
    "question_text",
    "options",
    "correct_answer",
    "correct_answers",
    "answer_status",
    "answer_source",
    "official_correction",
    "official_corrections",
    "answer_note",
}


def exp(stem, options, core):
    return f"【題幹解析】\n{stem}\n\n【選項詳解】\n{options}\n\n【核心考點】\n{core}"


def item(qnum, stem, options, core, key_point, front, back, summary):
    return {
        "question_id": f"{DATASET_ID}_{qnum:03d}",
        "question_number": qnum,
        "explanation": exp(stem, options, core),
        "key_point": key_point,
        "flashcard_front": front,
        "flashcard_back": back,
        "flashcard_summary": summary,
        "review_status": "ai_generated",
        "explanation_model": "codex-high-quality-rewrite",
        "explanation_generated_at": STAMP,
        "manual_review_notes": [],
    }


UPDATES = {
    7: item(
        7,
        "Dandy-Walker malformation 的病灶在後顱窩，典型包括小腦蚓部發育不全、後顱窩囊性擴大，以及第四腦室出口阻塞。腦脊髓液在第四腦室往蛛網膜下腔流出受阻，所以最早、最直接被撐大的腔室是第四腦室。",
        "- A. 第三腦室位在第四腦室上游；阻塞持續後可因水腦而擴大，但不是 Dandy-Walker 出口阻塞最早受影響的腦室。\n- B. 第四腦室正是 Dandy-Walker 畸形囊性擴張的核心位置，第四腦室出口閉鎖會使它最早變大，符合官方答案。\n- C. 大腦導水管連接第三、第四腦室；若導水管狹窄會造成第三與側腦室擴大，與 Dandy-Walker 的第四腦室出口問題不同。\n- D. 側腦室位於更上游，可能在後期水腦時擴大，但不是最先產生擴大現象的部位。",
        "Dandy-Walker 要抓「第四腦室出口阻塞加後顱窩囊性擴大」。出口卡在第四腦室之後，最早被壓力撐大的就是第四腦室，而不是第三腦室、導水管或側腦室。",
        "Dandy-Walker 畸形的第四腦室出口阻塞與最早擴大腦室",
        "Dandy-Walker / 第四腦室出口阻塞 / 最早擴大腦室",
        "Dandy-Walker malformation 最早擴大的是第四腦室，因為阻塞發生在第四腦室出口。",
        "Dandy-Walker -> 第四腦室出口阻塞 -> 第四腦室最早擴大",
    ),
    19: item(
        19,
        "急性左前胸痛不能只想心肌梗塞，也要把急性主動脈剝離放進鑑別。B 型主動脈剝離不波及升主動脈，若有併發症或適合介入治療，可考慮胸主動脈腔內修復術（TEVAR）。急性心肌梗塞的急性再灌流首選通常是 PCI；CABG 是特定冠狀動脈病灶或 PCI 不適合時才考慮，不是「立即必須」。因此 1、2、3 正確，4 錯。",
        "- A. 123 包含主動脈剝離鑑別、B 型剝離可考慮腔內支架、AMI 可考慮 PCI，三項都符合急診胸痛處置邏輯。\n- B. 134 把第 4 項納入，但 AMI 不是一診斷就必須立即 CABG；急性期常先評估 PCI 再灌流。\n- C. 僅24 少了主動脈剝離鑑別與 PCI，且包含錯誤的立即 CABG，組合不合理。\n- D. 僅4 只留下最不精確的處置敘述；CABG 不是急性心肌梗塞的一律第一線處置。",
        "急性胸痛先排除致命病因：AMI 與主動脈剝離都要想。B 型剝離可走 TEVAR 評估；AMI 急性再灌流重點是 PCI，不是反射性安排 CABG。",
        "急性胸痛中主動脈剝離與心肌梗塞的鑑別及初始介入原則",
        "急性胸痛 / B 型主動脈剝離 / AMI / PCI",
        "胸痛需同時鑑別主動脈剝離與 AMI；B 型剝離可評估 TEVAR，AMI 急性期常以 PCI 為主要再灌流方式。",
        "急性胸痛 -> 剝離和 AMI 都要鑑別；B 型剝離可 TEVAR；AMI 優先 PCI 而非一律 CABG",
    ),
    23: item(
        23,
        "題目問錯誤敘述。原發性縱膈腔生殖細胞瘤中，成熟畸胎瘤常見；seminoma 通常不會讓 AFP 升高，若 AFP 升高就要懷疑 nonseminomatous germ cell tumor 成分。nonseminomatous tumor 可見 beta-HCG 升高，而 seminoma 對放射治療相對敏感。",
        "- A. Teratoma 在縱膈腔生殖細胞瘤中常見，這是可接受的正確敘述，不是本題要選的錯誤項。\n- B. Seminoma 病人的 AFP 應維持正常；AFP 升高提示非精原細胞瘤成分，所以這句是錯誤敘述，符合官方答案。\n- C. Nonseminomatous tumor 可分泌 beta-HCG，也常伴 AFP 異常，這句並非錯誤。\n- D. Seminoma 通常比 nonseminomatous tumor 對放射治療更敏感，這是兩者治療反應的重要差異。",
        "生殖細胞瘤標記要記：AFP 升高不支持純 seminoma。看到 seminoma 加 AFP 上升，要改想 nonseminomatous 成分。",
        "縱膈腔生殖細胞瘤的 seminoma 與 nonseminomatous 腫瘤標記差異",
        "縱膈 germ cell tumor / seminoma / AFP / beta-HCG",
        "純 seminoma 不會升高 AFP；AFP 升高要懷疑 nonseminomatous germ cell tumor 成分。",
        "縱膈生殖細胞瘤 -> seminoma AFP 正常；AFP 高代表非精原細胞瘤成分",
    ),
    26: item(
        26,
        "題目問錯誤敘述。肝性腦病變來自肝臟解毒下降或門脈分流，使氨等神經毒性物質累積；表現可從睡眠、行為改變到撲翼樣震顫。胃腸道出血會增加腸道蛋白負荷與產氨，是典型誘因。急性期不應鼓勵大量高蛋白飲食，而是控制誘因並依狀況調整蛋白來源與量。",
        "- A. 行為改變與 flapping tremor 是肝性腦病變常考的神經精神表現，敘述正確。\n- B. 急性肝性腦病變時大量高蛋白會增加腸道產氨，可能惡化症狀；說「應多吃」是錯誤建議，符合官方答案。\n- C. 胃腸道出血後血液蛋白在腸道被分解，氨產生增加，確實可誘發肝性腦病變。\n- D. 氨濃度常升高，雖然臨床嚴重度不一定與數值完全平行，但方向上符合病理機轉。",
        "肝性腦病變考誘因時要想到感染、便秘、電解質異常與胃腸道出血。急性期處置是降低氨負荷與處理誘因，不是補大量高蛋白。",
        "肝性腦病變的誘因、血氨上升與蛋白飲食調整",
        "肝性腦病變 / 胃腸道出血 / 血氨 / 高蛋白",
        "肝性腦病變急性期不應大量高蛋白飲食；胃腸道出血會增加腸道產氨而誘發症狀。",
        "肝性腦病變 -> 血氨上升與 GI bleeding 誘發；急性期避免大量高蛋白",
    ),
    29: item(
        29,
        "題目問錯誤敘述。切口性疝氣是腹壁筋膜癒合失敗造成，張力過大、傷口感染、肥胖、營養不良等都會增加風險。症狀性或明顯缺損通常需手術修補；mesh 可降低復發，尤其適合較大缺損，但不是每個缺口在任何情境都一定要放人工網膜。",
        "- A. 過去手術傷口張力太大或癒合不良會使筋膜無法穩定癒合，是切口性疝氣的重要病因。\n- B. 術後傷口感染會破壞局部組織癒合強度，是形成切口性疝氣的常見危險因子。\n- C. 已形成的切口性疝氣若要根治，主要靠外科修補；束腹或觀察只能作為症狀控制或特定病人的暫時策略。\n- D. Mesh 很常用也能降低復發，但極小缺損或污染手術區可能選擇直接縫合或其他策略；「一定要」太絕對，因此錯誤。",
        "疝氣題看到「一定、全部、唯一」要小心。切口性疝氣根治靠手術，mesh 常是好選擇，但修補方式仍取決於缺損大小與污染風險。",
        "切口性疝氣成因與人工網膜修補的適用限制",
        "切口性疝氣 / 傷口感染 / mesh / 絕對化敘述",
        "切口性疝氣常因筋膜癒合不良形成，手術可根治；mesh 常用但不是所有缺口都一定要使用。",
        "切口性疝氣 -> 感染與張力是危險因子；mesh 常用但不等於一定使用",
    ),
    31: item(
        31,
        "本題依賴圖一 CT 與圖二標本，需保留官方答案解讀。題幹給的是肝門附近腫瘤造成膽道阻塞的判讀題；若腫瘤位在肝門膽管分叉處，會先影響左右肝管匯流，官方答案指向左肝管阻塞。它不是尾狀葉腫瘤，也不是典型完全實心肝腫塊或肝膿瘍。",
        "- A. Caudate lobe 是肝臟第一節，位置在肝門後方；題目重點是肝門膽管阻塞，不是單純尾狀葉腫瘤定位。\n- B. 左肝管阻塞可解釋肝門部腫瘤造成局部膽管擴張與手術標本所見，符合官方答案。\n- C. 肝門部膽管癌常沿膽管壁浸潤、造成膽道狹窄與阻塞，不一定呈現「全實心腫瘤」型態。\n- D. 肝膿瘍通常會有感染性囊腔、發燒或膿瘍影像脈絡；題幹手術標本與膽管阻塞更支持腫瘤性病灶。",
        "肝門部膽管癌（Klatskin tumor）考的是膽管分叉與左右肝管阻塞，不是把所有肝門病灶都當肝膿瘍或實心肝腫瘤。此題含附圖，最終仍以官方影像判讀為準。",
        "肝門部膽管腫瘤造成左肝管阻塞的影像與解剖判讀",
        "肝門部腫瘤 / Klatskin tumor / 左肝管阻塞 / 附圖判讀",
        "肝門部膽管腫瘤可阻塞左或右肝管；本題官方影像判讀為左肝管阻塞。",
        "肝門部膽管癌 -> 看左右肝管阻塞與膽道擴張；此題官方答案為左肝管阻塞",
    ),
    32: item(
        32,
        "題目問錯誤敘述。胰臟神經內分泌腫瘤中，功能性腫瘤以 insulinoma 常見；insulinoma 用 Whipple triad 抓低血糖、低血糖症狀、補葡萄糖後緩解。神經內分泌腫瘤典型為 hypervascular，contrast CT 常在動脈期顯影，不是大多 hypovascular 的完全低顯影腫塊。",
        "- A. 胰島素瘤是最常見的功能性胰臟神經內分泌腫瘤，會造成低血糖症狀，敘述正確。\n- B. Whipple triad 包含低血糖、低血糖時出現症狀、給葡萄糖後症狀緩解，是 insulinoma 的診斷線索。\n- C. Insulinoma 多為血管豐富，增強 CT 常可見明顯早期顯影；說大部分 hypovascular 且完全低顯影是錯誤敘述。\n- D. Insulinoma 的性別發生率差異不大，這不是本題的錯誤點。",
        "胰臟神經內分泌腫瘤和胰臟腺癌影像不同：NET 常 hypervascular。Insulinoma 再加 Whipple triad，是低血糖題的高頻組合。",
        "胰島素瘤的 Whipple triad 與 hypervascular 影像特徵",
        "Insulinoma / Whipple triad / hypervascular CT",
        "Insulinoma 常見 Whipple triad，影像多為 hypervascular，而非 hypovascular 低顯影腫塊。",
        "胰島素瘤 -> Whipple triad；胰臟 NET 多 hypervascular",
    ),
    34: item(
        34,
        "碘-131 治療需要腫瘤細胞保留攝碘能力，主要用在分化型甲狀腺癌，例如乳突癌與濾泡癌；Hürthle cell carcinoma 屬分化型範圍，攝碘能力較不穩定但仍可依風險評估。髓質癌來自濾泡旁 C 細胞，分泌 calcitonin，不靠碘代謝，因此不適合接受 I-131 治療。",
        "- A. 乳突癌是分化型甲狀腺癌，若有淋巴結轉移或中高風險特徵，甲狀腺全切後可考慮 I-131。\n- B. 濾泡癌同樣屬分化型甲狀腺癌，具攝碘特性，風險合適時可用放射性碘治療。\n- C. 髓質癌源自 C 細胞，不攝碘；I-131 對其治療效果不佳，是本題不適合者。\n- D. Hürthle cell carcinoma 雖攝碘率較傳統乳突癌、濾泡癌差，但仍歸在分化型癌風險評估脈絡，不是最典型禁忌答案。",
        "I-131 的核心是「分化型、會攝碘」。Medullary thyroid carcinoma 來自 C cell、看 calcitonin，不吃碘這套。",
        "碘-131 治療適用於分化型甲狀腺癌，不適用髓質癌",
        "I-131 / 分化型甲狀腺癌 / 髓質癌 / C cell",
        "乳突癌與濾泡癌可依風險考慮 I-131；髓質癌源自 C 細胞，不適合放射性碘治療。",
        "I-131 -> 分化型甲狀腺癌；medullary carcinoma 不攝碘",
    ),
    35: item(
        35,
        "題目問錯誤敘述。前哨淋巴結切片可在臨床腋下陰性的乳癌病人減少不必要腋下廓清，降低上肢淋巴水腫風險；全乳房切除時也常同時做 SLNB。臨床已摸到腋下淋巴結時，通常需進一步針吸或切片證實，不是典型直接做 SLNB 的族群。外科醫師有學習曲線，但不能因前百例出現偽陰性就絕對禁止再執行。",
        "- A. SLNB 若陰性可避免完整腋下淋巴廓清，因此能降低手臂淋巴水腫，是其主要優點。\n- B. SLNB 有學習曲線與可接受的偽陰性率監測；前百例若有偽陰性需檢討技術與品質，並非從此不應再做，故此句錯誤。\n- C. 乳房全切除者仍可做 SLNB，而且常建議在 mastectomy 同次完成，因日後較難再準確定位淋巴引流。\n- D. 若理學檢查已摸到可疑腋下淋巴結，代表臨床腋下陽性風險高，通常不屬標準 SLNB 適應症。",
        "SLNB 適合臨床腋下陰性病人，目的是減少 ALND 併發症。偽陰性率是品質監測與訓練問題，不是用一個絕對句把醫師資格永久否定。",
        "乳癌前哨淋巴結切片的適應症、優點與學習曲線",
        "乳癌 / SLNB / ALND / 偽陰性率",
        "SLNB 可降低 ALND 造成的淋巴水腫，適用於臨床腋下陰性病人；學習曲線需監測但非一有偽陰性即永久禁做。",
        "SLNB -> 減少 ALND；臨床腋下陰性較適合；偽陰性需品質監測",
    ),
    36: item(
        36,
        "題目問錯誤敘述。10 歲女童乳暈下單側、壓痛、約 2 公分硬塊，最常見是青春期前後乳芽發育或暫時性乳腺發育，可先觀察追蹤；另一側之後也可能出現。沒有快速變大、皮膚潰瘍、血性分泌物等警訊時，不應直接安排侵入性切片。",
        "- A. Prepubertal 或早期青春期乳腺發育可表現為乳暈下壓痛硬塊，是本題最可能的良性狀況。\n- B. 青春期乳芽可先單側出現，再變成雙側或較對稱，左側之後出現並不奇怪。\n- C. 典型乳芽發育以衛教與追蹤為主，觀察硬塊大小、疼痛與青春期進展即可。\n- D. 直接安排 biopsy 會增加疤痕與乳腺傷害風險；在典型良性乳芽發育下不是合適處置，因此為錯誤敘述。",
        "兒童乳暈下壓痛硬塊多先想生理性乳芽發育。除非有惡性或感染警訊，處置是追蹤，不是切片。",
        "女童乳暈下硬塊多為良性乳芽發育，典型情境先追蹤",
        "女童乳暈下硬塊 / prepubertal gynecomastia / follow-up",
        "兒童典型乳芽發育可單側且壓痛，通常觀察追蹤；沒有警訊不需立即切片。",
        "兒童乳暈下壓痛硬塊 -> 多為乳芽發育；先觀察，不直接 biopsy",
    ),
    38: item(
        38,
        "題目問錯誤敘述。乳房 Paget disease 是乳管內癌或侵襲性乳癌細胞沿乳管侵犯到乳頭表皮，表現為乳頭、乳暈濕疹樣或牛皮癬樣變化。原始病灶通常在乳管系統，不是說病灶一開始就在乳暈皮膚本身。",
        "- A. Paget disease 常與 ductal carcinoma in situ 或侵襲性乳管癌相關，屬乳癌表現的一種，敘述正確。\n- B. 原始病灶多來自乳管內癌細胞向乳頭表皮延伸，不是乳暈原發皮膚病灶；這句錯誤，符合官方答案。\n- C. 乳頭與乳暈可呈紅、癢、脫屑、滲液等濕疹樣變化，是 Paget disease 的典型臨床表現。\n- D. 因外觀可像濕疹或皮膚炎，需切片確認 Paget 細胞並排除單純皮膚病變。",
        "乳房 Paget disease 的陷阱是外觀看起來像皮膚病，但來源常是下方乳管內癌。慢性單側乳頭乳暈濕疹樣變化要切片。",
        "乳房 Paget disease 的乳管來源與乳頭乳暈濕疹樣表現",
        "Breast Paget disease / ductal carcinoma / nipple eczema",
        "Paget disease 常源自乳管內癌細胞侵犯乳頭表皮，表現像濕疹，需切片確認。",
        "乳房 Paget disease -> 乳管內癌來源；乳頭乳暈濕疹樣變化需切片",
    ),
    39: item(
        39,
        "肛門閉鎖可屬 VACTERL 相關異常的一部分，需注意其他先天畸形。新生兒出生後很快發紺、呼吸急促，且嘴角反覆有泡沫狀唾液，最典型是食道閉鎖合併或不合併氣管食道廔管，因唾液無法進入胃部而在口咽堆積，餵食時更容易嗆咳與發紺。",
        "- A. 十二指腸閉鎖常見膽汁性嘔吐與 double bubble，與口吐泡沫唾液、早期嗆咳發紺不如食道閉鎖吻合。\n- B. 肥厚性幽門狹窄多在出生後數週出現非膽汁性噴射狀嘔吐，出生 3 小時的發紺泡沫不是典型表現。\n- C. 食道閉鎖會使唾液無法順利進入胃部，造成口鼻泡沫、嗆咳、發紺；也可與肛門閉鎖合併，符合官方答案。\n- D. 橫膈膜疝氣會造成呼吸窘迫與胸腹部影像異常，但不會以大量泡沫狀唾液作為主要線索。",
        "新生兒「泡沫唾液、嗆咳、發紺」要想到 esophageal atresia/tracheoesophageal fistula。肛門閉鎖提醒可能有多系統先天異常合併。",
        "肛門閉鎖新生兒合併泡沫唾液與發紺時高度懷疑食道閉鎖",
        "Imperforate anus / frothy saliva / esophageal atresia",
        "食道閉鎖會造成新生兒口鼻泡沫、餵食嗆咳與發紺，且可與肛門閉鎖合併。",
        "新生兒泡沫唾液加發紺 -> 食道閉鎖；肛門閉鎖提示合併畸形",
    ),
    40: item(
        40,
        "先天性肌性斜頸多因胸鎖乳突肌纖維化或攣縮。患側胸鎖乳突肌變短時，頭會向患側側彎、臉轉向對側，因此「臉部向患側旋轉」會受限制；若長期未處理，可造成患側或相關臉部不對稱，但第 3 項寫成對側臉部發育不良不是典型考點。多數可先用伸展與復健，並非都要手術。",
        "- A. 24 把第 2 與第 4 項列為正確，但第 4 項「皆須手術」錯，不能選。\n- B. 134 同時包含第 3 與第 4 項；對側臉部發育不良與皆須手術都不符合典型先天性肌性斜頸。\n- C. 僅12 保留胸鎖乳突肌纖維化與患側旋轉受限，排除臉部發育敘述與一律手術，符合官方答案。\n- D. 123 把第 3 項納入，但臉部不對稱的方向與敘述不適合作為正確組合。",
        "肌性斜頸抓兩件事：胸鎖乳突肌纖維化、活動受限。治療以早期復健伸展為主，只有頑固或延遲個案才考慮手術。",
        "兒童先天性肌性斜頸的胸鎖乳突肌攣縮與治療原則",
        "Torticollis / sternocleidomastoid fibrosis / stretching",
        "先天性肌性斜頸由 SCM 纖維化造成，臉向患側旋轉受限；多數先復健，不是皆須手術。",
        "肌性斜頸 -> SCM 纖維化；早期伸展復健，不是一律手術",
    ),
    41: item(
        41,
        "Ladd procedure 是腸旋轉不良（intestinal malrotation）及其造成中腸扭轉風險的標準手術。手術重點包括鬆解 Ladd bands、擴大腸繫膜基底、處理扭轉並常合併闌尾切除，以降低日後診斷混淆。",
        "- A. 小腸閉鎖是腸道局部閉鎖或中斷，治療以切除閉鎖段與腸吻合為主，不是 Ladd procedure 的典型適應症。\n- B. 十二指腸閉鎖常做十二指腸十二指腸吻合或相關旁路手術，不是 Ladd procedure。\n- C. Hirschsprung disease 是遠端腸道神經節細胞缺如，治療是 pull-through 類手術，和 Ladd procedure 不同。\n- D. 腸旋轉異常會產生 Ladd bands 與中腸扭轉風險，正是 Ladd procedure 的適應症。",
        "Ladd procedure 看到就連到 intestinal malrotation。它不是處理閉鎖或巨大結腸症，而是處理旋轉不良造成的阻塞與扭轉風險。",
        "Ladd procedure 的適應症是腸旋轉不良",
        "Ladd procedure / intestinal malrotation / volvulus",
        "Ladd procedure 用於腸旋轉不良，處理 Ladd bands 與中腸扭轉風險。",
        "Ladd procedure -> intestinal malrotation",
    ),
    42: item(
        42,
        "兒童 rhabdomyosarcoma 是軟組織惡性腫瘤，可發生在沒有明顯骨骼肌的部位，但好發仍以頭頸部、泌尿生殖系統與四肢較常見。腸胃道不是典型高頻好發部位，因此在四個選項中較不好發。",
        "- A. 頭頸部是兒童 rhabdomyosarcoma 的常見部位，尤其眼眶、鼻咽與旁腦膜區域都常考。\n- B. 四肢也是 rhabdomyosarcoma 的重要發生部位，常與 alveolar subtype 相關。\n- C. 腸胃道不是兒童 rhabdomyosarcoma 的典型主要好發位置，和其他三項相比最不符合，為官方答案。\n- D. 泌尿生殖道，例如膀胱、前列腺、陰道等，是兒童 rhabdomyosarcoma 常見部位。",
        "兒童橫紋肌肉瘤好發頭頸、泌尿生殖與四肢。考題問較不好發時，腸胃道通常是可排除的選項。",
        "兒童橫紋肌肉瘤常見部位與較少見的腸胃道位置",
        "Rhabdomyosarcoma / head-neck / GU / extremities",
        "兒童 rhabdomyosarcoma 常見於頭頸部、泌尿生殖系統與四肢；腸胃道較少見。",
        "兒童 rhabdomyosarcoma -> 頭頸、GU、四肢常見；GI 較少見",
    ),
    43: item(
        43,
        "題目問錯誤敘述。隱睪症常合併 patent processus vaginalis 或腹股溝疝氣；治療以睪丸固定術為主，目的包括降低不孕、扭轉、創傷與日後腫瘤監測困難。手術時機應在嬰幼兒期完成，通常約 6 個月後至 1 歲多評估處理，不會等到學齡後。",
        "- A. 隱睪常與腹股溝疝氣或鞘狀突未閉相關，這是正確併發關係。\n- B. 睪丸固定術（orchidopexy）是主要治療，將睪丸固定於陰囊並處理合併疝氣囊。\n- C. 未治療隱睪因溫度與生殖細胞發育受影響，日後不孕風險上升，敘述正確。\n- D. 等到學齡後才手術太晚，會增加睪丸功能受損時間；這是本題錯誤敘述。",
        "隱睪症不要等上學。國考重點是早期 orchidopexy，兼顧生育功能、疝氣處理與腫瘤監測。",
        "隱睪症的腹股溝疝氣關聯、不孕風險與早期睪丸固定術",
        "Cryptorchidism / orchidopexy / timing",
        "隱睪症應在嬰幼兒期評估睪丸固定術，不應延到學齡後。",
        "隱睪症 -> 早期 orchidopexy；不等到學齡後",
    ),
    44: item(
        44,
        "老人家長期右上腹痛後突然腹脹、噁心嘔吐，X 光在右下腹看到 radiopaque mass，最符合膽石經膽囊腸道廔管掉入腸道後造成機械性阻塞，也就是 gallstone ileus。典型影像可有腸阻塞、膽道氣體與異位膽石。",
        "- A. Bezoar 也能造成腸阻塞，特別是胃手術後，但題幹有長期右上腹痛與 radiopaque 結石樣陰影，更指向膽石性腸梗阻。\n- B. Gallstone ileus 由膽石進入腸道並卡在遠端小腸造成阻塞，臨床與影像線索都吻合官方答案。\n- C. 尿道結石位置應沿泌尿道，通常造成泌尿症狀或腎絞痛，不會解釋腹脹嘔吐的腸阻塞表現。\n- D. 骨盆腔鈣化腫瘤不會典型造成急性小腸阻塞，也無法串連長期右上腹痛與異位結石。",
        "Gallstone ileus 的題幹常有高齡、膽囊病史、腸阻塞與異位鈣化結石。右下腹 radiopaque mass 在這裡不是尿路結石，而是掉進腸道的膽石。",
        "膽石性腸梗阻的病史、腸阻塞表現與異位膽石影像",
        "Gallstone ileus / pneumobilia / ectopic gallstone",
        "膽石經膽囊腸道廔管進入腸道，卡住後可造成 gallstone ileus，表現為腸阻塞與異位膽石。",
        "高齡加膽囊病史加腸阻塞加異位結石 -> gallstone ileus",
    ),
    45: item(
        45,
        "原發性副甲狀腺功能亢進造成 PTH 過高，典型是高血鈣與低磷，會導致骨質流失、腎結石，也可有情緒或認知症狀。Tetany 通常來自低血鈣使神經肌肉興奮性上升，與 PHPT 的高血鈣方向相反，因此無關。",
        "- A. Osteoporosis、osteopenia 來自 PTH 促進骨吸收，是 PHPT 常見併發症。\n- B. Tetany 是低血鈣常見表現；PHPT 造成高血鈣，所以這項最無關，符合官方答案。\n- C. Depression、anxiety 等神經精神症狀可見於高血鈣或 PHPT，不能排除。\n- D. Kidney stone 是 PHPT 的經典表現之一，來自高血鈣與高尿鈣。",
        "PHPT 記高血鈣：stones、bones、psychiatric symptoms。Tetany 反而是低血鈣方向，所以不是 PHPT 併發症。",
        "原發性副甲狀腺功能亢進造成高血鈣併發症，tetany 屬低血鈣表現",
        "Primary hyperparathyroidism / hypercalcemia / tetany",
        "PHPT 造成高血鈣、骨質流失與腎結石；tetany 通常是低血鈣表現。",
        "PHPT -> 高血鈣；骨鬆腎結石常見；tetany 是低血鈣",
    ),
    51: item(
        51,
        "肺動脈瓣閉鎖的新生兒若沒有足夠肺血流，會仰賴開放性動脈導管把主動脈血流導向肺動脈。前列腺素 E1 可維持或重新打開 ductus arteriosus，讓肺血流增加，因此發紺改善。",
        "- A. 前列腺素不會把閉鎖的肺動脈瓣打開；瓣膜本身仍然閉鎖，所以不是改善原因。\n- B. PGE1 使動脈導管維持開放或再開，提供到肺動脈的血流，正是 ductal-dependent pulmonary blood flow 的急救機轉。\n- C. 心房中隔缺損可幫助心房間混合，但不能直接增加肺動脈血流，無法解釋給 PGE1 後改善。\n- D. 體動脈到肺動脈側枝可能存在於部分先天心臟病，但 PGE1 的立即效果主要是作用在動脈導管。",
        "新生兒發紺性心臟病給 PGE1，要想到 ductal-dependent circulation。肺動脈瓣閉鎖靠動脈導管供應肺血流，打開導管就能改善缺氧。",
        "肺動脈瓣閉鎖的新生兒以 PGE1 重新開放動脈導管增加肺血流",
        "Pulmonary atresia / PGE1 / PDA / cyanosis",
        "PGE1 可開放動脈導管，使肺動脈瓣閉鎖的新生兒增加肺血流並改善發紺。",
        "肺動脈瓣閉鎖 -> ductal-dependent pulmonary flow；PGE1 開 PDA",
    ),
    52: item(
        52,
        "這題是肺動脈瓣閉鎖、完整心室中隔、右心室發育不良，且有右心室竇狀交通到冠狀動脈並合併左主冠狀動脈出口狹窄。這代表可能存在右心室依賴型冠狀動脈循環；若強行打開右心室出口或降低右心室壓力，可能造成冠狀動脈灌流惡化。最佳策略是先提供體肺分流，如 Blalock-Taussig shunt，而不是打開肺動脈瓣。",
        "- A. 肺動脈瓣切開會改變右心室壓力，對右心室依賴型冠狀循環可能危險，不是最佳選擇。\n- B. Blalock-Taussig 分流術可從體循環提供肺血流，避開直接減壓右心室的風險，符合官方答案。\n- C. Transannular patch 用於擴大右心室出口，但此病人右心室發育不良且冠狀循環風險高，不宜作為最佳處置。\n- D. 肺動脈瓣切開加分流仍包含右心室減壓風險，因此不如單純體肺分流安全。",
        "肺動脈瓣閉鎖合併完整心室中隔時，若看到 RV sinusoid 到冠狀動脈與冠狀狹窄，要小心 RVDCC。這種病人避免直接右心室減壓，先以體肺分流供肺血流。",
        "肺動脈瓣閉鎖合併右心室依賴型冠狀循環時避免右心室減壓",
        "PA-IVS / RVDCC / Blalock-Taussig shunt",
        "PA-IVS 合併 RVDCC 時，不宜直接肺動脈瓣切開；可用 Blalock-Taussig shunt 提供肺血流。",
        "PA-IVS 加 RVDCC -> 避免 RV decompression；選 BT shunt",
    ),
    58: item(
        58,
        "De Quervain 氏症是第一伸肌腱腔室狹窄性腱鞘炎，受累的是 abductor pollicis longus（APL）與 extensor pollicis brevis（EPB）。選項中只有拇指外展長肌腱屬於第一腔室。",
        "- A. Extensor carpi radialis brevis 位於第二伸肌腱腔室，不是 De Quervain 的第一腔室肌腱。\n- B. Extensor carpi radialis longus 也在第二腔室，主要負責手腕伸展與橈偏，解剖位置不在 APL/EPB 的狹窄腱鞘內。\n- C. Extensor pollicis longus 位於第三腔室，通過 Lister tubercle 尺側，不屬第一腔室。\n- D. Abductor pollicis longus 是第一伸肌腱腔室的肌腱之一，和 EPB 一起造成媽媽手，符合官方答案。",
        "媽媽手記第一腔室：APL 加 EPB。EPL 是第三腔室，ECRL/ECRB 是第二腔室。",
        "De Quervain 氏症侵犯第一伸肌腱腔室的 APL 與 EPB",
        "De Quervain / first extensor compartment / APL / EPB",
        "De Quervain 氏症是第一伸肌腱腔室病變，包含 APL 與 EPB。",
        "De Quervain -> 第一腔室 -> APL 和 EPB",
    ),
    59: item(
        59,
        "全髖人工關節置換的後方入路會從臀大肌分開後進入，通常需要處理短外旋肌群與後方關節囊；短外旋肌包括 piriformis、gemelli、obturator internus 等。選項中 superior gemellus 屬短外旋肌，會在後方入路中被切開或放鬆。",
        "- A. Gluteus medius 是外展肌，較常在側方或前外側入路被牽涉；後方入路通常會保留它。\n- B. Gluteus minimus 位於髖外展肌群深層，也不是後方入路必須切斷的主要肌肉。\n- C. Superior gemellus 是短外旋肌群之一，位於髖關節後方，後方入路常需切斷或放鬆，符合官方答案。\n- D. Vastus lateralis 在股骨外側，與標準後方髖關節入路的關節暴露不相符。",
        "THR 後方入路的關鍵是後方短外旋肌群，不是臀中肌。這也是後方入路術後脫位風險與後方軟組織修補常被一起考的原因。",
        "全髖關節置換後方入路需處理短外旋肌群",
        "Total hip replacement / posterior approach / short external rotators",
        "髖關節後方入路常切開短外旋肌群；superior gemellus 屬於此群。",
        "THR posterior approach -> short external rotators；superior gemellus",
    ),
    60: item(
        60,
        "遠端橈骨骨折合併遠端橈尺關節（DRUJ）脫位稱為 Galeazzi fracture-dislocation。此題的關鍵詞已直接給出「遠端橈骨骨折」與「遠端橈尺骨關節脫位」，因此選 Galeazzi。",
        "- A. Galeazzi 氏骨折就是橈骨遠端或中遠端骨折合併 DRUJ 脫位，與題幹完全相符。\n- B. Smith fracture 是遠端橈骨骨折合併掌側移位，沒有以 DRUJ 脫位作為定義。\n- C. Monteggia fracture 是尺骨近端骨折合併橈骨頭脫位，方向與本題相反。\n- D. Essex-Lopresti injury 是橈骨頭骨折、骨間膜破裂與 DRUJ 不穩定的組合，不是單純遠端橈骨骨折合併 DRUJ 脫位。",
        "前臂骨折命名最常考配對：Galeazzi 是 radius fracture 加 DRUJ dislocation；Monteggia 是 ulna fracture 加 radial head dislocation。",
        "Galeazzi 氏骨折為遠端橈骨骨折合併遠端橈尺關節脫位",
        "Galeazzi / distal radius fracture / DRUJ dislocation",
        "遠端橈骨骨折合併 DRUJ 脫位稱 Galeazzi fracture-dislocation。",
        "Galeazzi -> radius fracture + DRUJ dislocation",
    ),
    61: item(
        61,
        "題目問 terrible triad of the elbow 的除外。恐怖三合症是肘關節脫臼、橈骨頭骨折、尺骨冠狀突骨折三者並存，代表肘關節非常不穩定。肱骨髁上骨折是兒童常見肘部骨折，但不屬於 terrible triad 定義。",
        "- A. Coronoid fracture 是 terrible triad 的三個組成之一，不能選為除外。\n- B. Radial head fracture 也是 terrible triad 的必要組成之一。\n- C. Supracondylar fracture of humerus 不在 terrible triad 定義中，是本題除外答案。\n- D. Elbow dislocation 是 terrible triad 的核心傷害之一，常與橈骨頭與冠狀突骨折一起出現。",
        "Elbow terrible triad = elbow dislocation + radial head fracture + coronoid fracture。看到 supracondylar humerus fracture 要排除。",
        "肘關節恐怖三合症由脫臼、橈骨頭骨折與冠狀突骨折組成",
        "Terrible triad elbow / radial head / coronoid / dislocation",
        "肘關節 terrible triad 不包括肱骨髁上骨折。",
        "Elbow terrible triad -> dislocation + radial head fracture + coronoid fracture",
    ),
    62: item(
        62,
        "題目問哪個不是兒童足踝疾病名稱。Köhler disease 是足舟狀骨骨軟骨病變，Freiberg infarction 是蹠骨頭缺血壞死，Sever disease 是跟骨骨骺炎；三者都可歸在兒童或青少年足踝相關病變。Panner disease 是肱骨小頭骨軟骨病變，屬肘部，不是足踝。",
        "- A. Köhler disease 發生在足舟狀骨，是典型兒童足部骨軟骨病變。\n- B. Freiberg infarction 多影響第二蹠骨頭，也屬前足疾病。\n- C. Panner disease 發生在肘部肱骨小頭，不是足踝疾病，符合官方答案。\n- D. Sever disease 是跟骨骨骺炎，常見於兒童或青少年足跟痛。",
        "兒童足踝骨骺炎名稱要配部位：Köhler 足舟狀骨、Freiberg 蹠骨頭、Sever 跟骨。Panner 在肘部。",
        "兒童骨軟骨病變名稱與解剖部位鑑別",
        "Köhler / Freiberg / Sever / Panner",
        "Panner disease 是肱骨小頭病變，不是足踝疾病。",
        "足踝病名 -> Köhler 足舟狀骨、Freiberg 蹠骨頭、Sever 跟骨；Panner 是肘部",
    ),
    65: item(
        65,
        "題目問錯誤敘述。腎細胞癌常有副腫瘤症候群，可出現發燒、體重減輕、貧血、肝功能異常、ESR 升高、高血壓、高血鈣等。高血鈣是重要表現，但若說它是最常發生的臨床症狀，且其次是高血壓，過度簡化且不符合常見統計描述；ESR 升高反而常被列為最常見的全身性異常之一。",
        "- A. RCC 約有相當比例病人會出現 paraneoplastic syndrome，20% 是常見考試敘述，可接受。\n- B. ESR 升高常被列為 RCC 副腫瘤或全身性表現中很常見的異常，這句不是錯誤點。\n- C. 高血鈣雖重要，但不是最常見的 paraneoplastic 臨床表現；把它列為最常見且其次高血壓不精確，符合官方錯誤答案。\n- D. 高血鈣可由 PTHrP 等副腫瘤機轉或骨轉移溶骨造成，發生率可達題目所列範圍，敘述合理。",
        "RCC 是副腫瘤症候群大戶，但排序要小心。ESR 升高、貧血、發燒、肝功能異常等常見；高血鈣重要但不是最常見。",
        "腎細胞癌副腫瘤症候群常見表現與高血鈣排序陷阱",
        "RCC / paraneoplastic syndrome / ESR / hypercalcemia",
        "RCC 可有副腫瘤症候群；高血鈣重要但不應說成最常見表現。",
        "RCC paraneoplastic -> ESR 升高常見；高血鈣重要但非最常見",
    ),
    66: item(
        66,
        "題目問錯誤敘述。根除性膀胱切除術是重大骨盆手術，可用於肌肉侵犯性膀胱癌，以及部分 BCG 或膀胱內治療失敗的 high-grade Ta/T1 或 CIS。手術前需評估出血風險與抗血小板藥物，aspirin 通常不會說「不必停止」；是否停藥要依血栓風險與手術計畫決定。",
        "- A. High-grade 膀胱癌或 CIS 經膀胱內治療仍反覆復發，可能需早期根除性膀胱切除，敘述正確。\n- B. Radical cystectomy 出血風險高，aspirin 需術前評估並常需停用或調整；說完全不必停止是錯誤敘述。\n- C. 骨盆大手術後臥床與腫瘤本身會增加深層靜脈血栓風險，需預防與監測。\n- D. Radical cystectomy 有一定手術死亡率，約 1-3% 是常見考試範圍，敘述可接受。",
        "根除性膀胱切除是高風險大手術，術前抗血小板與抗凝藥一定要評估。不要把 aspirin 當成完全不用管的藥。",
        "根除性膀胱切除術的適應症、血栓風險與 aspirin 術前評估",
        "Radical cystectomy / aspirin / high-grade bladder cancer",
        "Radical cystectomy 前需評估 aspirin 等抗血小板藥物；不應說術前完全不必停止。",
        "Radical cystectomy -> 高風險手術；aspirin 需術前評估或調整",
    ),
    67: item(
        67,
        "題目問錯誤敘述。BPH 源自前列腺 transition zone，由上皮與基質增生組成；基質平滑肌受 alpha-1 交感神經影響，這也是 alpha-blocker 可改善症狀的理由。下泌尿道症狀嚴重度和前列腺大小不一定線性相關，因為症狀還受膀胱出口位置、平滑肌張力與膀胱功能影響。",
        "- A. BPH 主要發生在 transition zone，會壓迫尿道造成膀胱出口阻塞，敘述正確。\n- B. 顯微鏡下有 stromal 與 epithelial hyperplasia；stromal smooth muscle 受 alpha-1 adrenergic tone 影響，敘述正確。\n- C. BPH 與年齡、雄性素環境及雌雄素比例變化相關，題目列為正確敘述時可按官方邏輯保留。\n- D. 肛門指診估到的體積大小不必然與 LUTS 阻塞症狀成正相關；小腺體也可因位置造成明顯症狀，因此此句錯誤。",
        "BPH 的大小和症狀不是等號。考題常用 DRE 體積誤導；真正症狀取決於尿道壓迫位置、動態平滑肌張力與膀胱反應。",
        "BPH 的 transition zone 起源、alpha-1 支配與症狀不等於體積大小",
        "BPH / transition zone / alpha-1 / LUTS",
        "BPH 起源於 transition zone；LUTS 嚴重度不一定和 DRE 前列腺大小成正比。",
        "BPH -> TZ 起源；alpha-1 tone；LUTS 不必然和體積成正比",
    ),
    73: item(
        73,
        "本題需結合附圖 CT。題幹給左上腹痛、發燒、白血球增加，影像若顯示脾臟內低密度或囊性病灶，最符合脾臟膿瘍。重點是病灶位置在左上腹脾臟，而不是腰肌、結腸或胰臟周圍。",
        "- A. Spleen abscess 可表現為發燒、左上腹痛、白血球上升，CT 見脾臟內低密度膿瘍腔，符合官方答案。\n- B. Left psoas muscle abscess 病灶在後腹腔腰大肌，常有腰背痛、髖部活動痛或 psoas sign，位置和脾臟影像不同。\n- C. Colon diverticulitis 通常以左下腹痛、結腸壁增厚與周邊脂肪發炎為主，不是脾臟內病灶。\n- D. Peripancreatic abscess 多接在急性胰臟炎後，位置在胰臟周圍，題幹沒有胰臟炎病史與影像重點。",
        "影像診斷先定位。左上腹感染症狀加脾臟內低密度病灶，優先診斷 splenic abscess；不要被其他腹腔膿瘍名稱分散。",
        "脾臟膿瘍的左上腹感染症狀與 CT 定位",
        "Splenic abscess / LUQ pain / fever / CT",
        "左上腹痛、發燒、白血球升高加脾臟內低密度病灶，最符合脾臟膿瘍。",
        "LUQ pain + fever + splenic low-density lesion -> splenic abscess",
    ),
    75: item(
        75,
        "火燒車後眉毛鼻毛燒焦、臉頸部燒傷、聲音沙啞、呼吸快淺且氧飽和度 70%，高度懷疑吸入性燒傷與上呼吸道水腫。燒傷後水腫會進展，若等待檢查可能錯失插管時機；第一優先是先確保呼吸道。",
        "- A. ABG 可評估氧合、通氣與一氧化碳中毒，但不能取代立即建立呼吸道；在嚴重缺氧與聲音沙啞時不應先等抽血。\n- B. 胸部 X 光早期可能正常，也不能處理即將阻塞的上呼吸道。\n- C. 靜脈輸液是燒傷復甦的重要步驟，但本題已有呼吸道危象，依 ABC 原則 airway 優先。\n- D. Endotracheal intubation 可在水腫惡化前保護呼吸道並改善通氣，是第一優先處置。",
        "燒傷急救照 ABC：有吸入性傷害紅旗如臉頸燒傷、鼻毛燒焦、聲音沙啞、低氧，先插管保護 airway，再做檢查與輸液。",
        "吸入性燒傷有呼吸道水腫風險時須優先氣管插管",
        "Inhalation injury / hoarseness / airway / intubation",
        "吸入性燒傷伴聲音沙啞與低氧時，第一優先是氣管內插管保護呼吸道。",
        "燒傷 ABC -> hoarseness + facial burn + hypoxia -> early intubation",
    ),
    76: item(
        76,
        "尺骨近端骨折合併橈骨頭脫位就是 Monteggia fracture-dislocation。題幹明確給出 proximal ulna fracture 與 radial head dislocation，配對到 Monteggia。",
        "- A. Colles fracture 是遠端橈骨骨折向背側移位，常見於跌倒手撐地，並非尺骨近端骨折合併橈骨頭脫位。\n- B. Chauffeur's fracture 是橈骨莖突骨折，與前臂近端尺骨與橈骨頭關節不符。\n- C. Galeazzi fracture 是橈骨遠端或中遠端骨折合併 DRUJ 脫位，和 Monteggia 的骨頭與脫位位置相反。\n- D. Monteggia fracture 定義為尺骨近端骨折合併橈骨頭脫位，符合官方答案。",
        "Monteggia 與 Galeazzi 要成對記：Monteggia 是 proximal ulna 加 radial head；Galeazzi 是 radius 加 DRUJ。",
        "Monteggia 氏骨折為尺骨近端骨折合併橈骨頭脫位",
        "Monteggia / proximal ulna fracture / radial head dislocation",
        "尺骨近端骨折合併橈骨頭脫位稱 Monteggia fracture-dislocation。",
        "Monteggia -> proximal ulna fracture + radial head dislocation",
    ),
    80: item(
        80,
        "王醫師已掌握同儕為業績進行無適應症手術的事證，也已私下溝通但未改善。此時專業倫理重點是保護病人安全，並循正式、可追蹤且符合保密原則的內部管道處理，例如向主管、主任或倫理委員會通報。",
        "- A. 置之不理會讓病人持續暴露於不必要手術風險，違反醫療專業保護病人的義務。\n- B. 私下向媒體舉發可能破壞病人隱私與正當程序，通常不是第一線合適處置。\n- C. 攜帶具體資料向主管或倫理委員會檢舉，能兼顧病人安全、證據保存、程序正義與院內治理，最適當。\n- D. 已與陳醫師談過且未改善，再找其他同事談可能延誤正式處理，不能取代通報。",
        "醫療倫理題遇到同儕不當醫療且溝通無效，優先走正式內部通報與倫理程序；不要放任，也不要先訴諸媒體。",
        "同儕不當醫療行為應循正式內部倫理通報處理",
        "Medical ethics / unnecessary surgery / internal reporting",
        "同儕疑似無適應症手術且溝通無效時，應帶資料向主管或倫理委員會正式通報。",
        "同儕不當醫療 -> 溝通無效 -> 內部主管或倫理委員會通報",
    ),
}


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate_source(before, after, target_numbers):
    errors = []
    before_questions = before["questions"]
    after_questions = after["questions"]
    if len(before_questions) != len(after_questions):
        errors.append(f"question count changed: {len(before_questions)} -> {len(after_questions)}")
    for before_q, after_q in zip(before_questions, after_questions):
        qnum = after_q.get("question_number")
        for field in IMMUTABLE_FIELDS:
            if before_q.get(field) != after_q.get(field):
                errors.append(f"Q{qnum} immutable field changed: {field}")
        changed = {
            key
            for key in set(before_q) | set(after_q)
            if before_q.get(key) != after_q.get(key)
        }
        if qnum in target_numbers:
            unexpected = changed - MERGE_FIELDS
            if unexpected:
                errors.append(f"Q{qnum} unexpected changed fields: {sorted(unexpected)}")
        elif changed:
            errors.append(f"Q{qnum} changed but was not in selected target list: {sorted(changed)}")
    return errors


def main():
    source_path = Path(SOURCE_FILE)
    exam = load_json(source_path)
    before = copy.deepcopy(exam)
    questions = {q["question_number"]: q for q in exam["questions"]}
    target_numbers = set()
    written = []

    for filename, start, end, numbers in TARGET_BATCHES:
        target_numbers.update(numbers)
        updates = []
        for qnum in numbers:
            update = UPDATES[qnum]
            source_q = questions[qnum]
            if update["question_id"] != source_q["id"]:
                raise RuntimeError(f"Q{qnum} id mismatch")
            if not (start <= qnum <= end):
                raise RuntimeError(f"Q{qnum} outside batch range")
            updates.append(update)
        payload = {
            "source_file": SOURCE_FILE,
            "dataset_id": DATASET_ID,
            "range": {"start": start, "end": end},
            "updates": updates,
        }
        out_path = OUT_DIR / filename
        write_json(out_path, payload)
        written.append(str(out_path))

    for qnum, update in UPDATES.items():
        q = questions[qnum]
        for field in MERGE_FIELDS:
            q[field] = update[field]

    errors = validate_source(before, exam, target_numbers)
    if errors:
        raise RuntimeError("\n".join(errors))

    write_json(source_path, exam)
    report = {
        "source_file": SOURCE_FILE,
        "dataset_id": DATASET_ID,
        "update_files": written,
        "question_count": len(target_numbers),
        "question_numbers": sorted(target_numbers),
        "errors": [],
    }
    write_json(OUT_DIR / "merge_report.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
