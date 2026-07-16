import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/113-1/medicine-4.json"
DATASET_ID = "113-1_medicine-4"
OUT_DIR = Path("scratch/rewrite_updates/113-1_medicine-4")
STAMP = "2026-07-16T00:00:00+08:00"


def make_explanation(analysis, options, core):
    lines = ["【題幹解析】", analysis.strip(), "", "【選項詳解】"]
    for letter in ("A", "B", "C", "D"):
        lines.append(f"- {letter}. {options[letter].strip()}")
    lines.extend(["", "【核心考點】", core.strip()])
    return "\n".join(lines)


ITEMS = {
    1: {
        "analysis": "題目問足月新生兒體重變化何者最可能異常。足月新生兒出生後可有生理性體重下降，通常不超過出生體重約 7-10%，並在 10-14 天內回到出生體重；之後約每日增加 20-30 g。",
        "options": {
            "A": "出生 3000 g 的嬰兒 3 天大降到 2600 g，下降約 13%，超過常見生理性下降範圍，需評估餵食不足、脫水或疾病，最可能異常。",
            "B": "5 天大 2800 g 約下降 6.7%，仍在生理性體重下降可接受範圍內，若活力與尿量正常可追蹤。",
            "C": "1 個月 4000 g 約增加 1000 g，符合嬰兒前幾個月快速增重的期待。",
            "D": "2 個月 4900 g 相較出生增加 1900 g，大致符合每月增加約 0.6-1 kg 的趨勢。",
        },
        "key_point": "足月新生兒生理性體重下降通常不超過出生體重約 7-10%，超過 10% 要評估餵食與脫水。",
        "front": "足月新生兒體重下降",
    },
    2: {
        "analysis": "題目描述全母乳新生兒 7 天大體重幾乎回到出生體重，總膽紅素 12 mg/dL、活力佳且大便顏色正常。這比較像生理性或母乳相關黃疸，沒有膽道阻塞或需立即照光的警訊。",
        "options": {
            "A": "腹部超音波主要用於懷疑膽道閉鎖、肝膽構造異常或持續直接膽紅素上升；本題大便顏色正常且總膽紅素不高，尚非優先。",
            "B": "是否照光需依出生時數、胎齡與危險因子判斷；7 天大 12 mg/dL 且臨床穩定，通常未達住院照光門檻。",
            "C": "持續母乳、評估餵食與尿便量、門診追蹤黃疸與體重，是最適當處置。",
            "D": "母乳哺餵相關黃疸通常不需停止母乳；停餵反而可能影響營養與親餵建立。",
        },
        "key_point": "全母乳新生兒若體重恢復、活力佳、糞便顏色正常且膽紅素未達治療門檻，多以持續哺餵與追蹤為主。",
        "front": "新生兒母乳黃疸",
    },
    3: {
        "analysis": "題目問早產兒呼吸暫停診斷何者最不適當。早產兒呼吸暫停通常定義為呼吸停止超過 20 秒，或較短暫但伴隨心搏過緩、發紺、氧飽和下降或張力改變。",
        "options": {
            "A": "單純無症狀呼吸中止大於 10 秒不足以作為典型診斷定義，因此是不適當敘述。",
            "B": "早產兒呼吸暫停常伴隨迷走神經反應與低氧，出現心搏過緩很典型。",
            "C": "若暫停造成低氧，可出現發紺或血氧下降，敘述正確。",
            "D": "早產兒多為中樞與阻塞成分混合的 mixed apnea，敘述正確。",
        },
        "key_point": "早產兒呼吸暫停重點是超過 20 秒，或較短但合併心搏過緩、發紺或低氧。",
        "front": "早產兒呼吸暫停定義",
    },
    4: {
        "analysis": "新生兒復甦流程中，初始步驟後若仍呼吸不良且心跳低於每分鐘 100 下，首要處置是有效正壓換氣；心跳每分鐘 50 下代表通氣更急迫。",
        "options": {
            "A": "胸外按壓通常在有效正壓換氣 30 秒後心跳仍低於每分鐘 60 下才開始，不是第一步。",
            "B": "Epinephrine 用於正壓換氣與胸外按壓後心跳仍低於每分鐘 60 下的情境，不能取代通氣。",
            "C": "單純氧氣面罩無法解決通氣不足；呼吸窘迫合併心搏過緩需正壓換氣。",
            "D": "給與正壓換氣是此時最重要且最適當的下一步。",
        },
        "key_point": "新生兒復甦先看呼吸與心跳；呼吸不良且 HR <100/min 時，立即給有效正壓換氣。",
        "front": "新生兒復甦 PPV",
    },
    5: {
        "analysis": "題目問壞死性腸炎何者最不適當。NEC 常見於早產兒，典型 X 光可見腸壁積氣，但發生時間多在開始餵食後、出生後數天至數週，不是通常都在出生後 1 週內。",
        "options": {
            "A": "NEC 是新生兒重要且可危及生命的腸胃道急症，敘述正確。",
            "B": "早產、腸道菌叢移生與配方奶餵食都是典型危險因子，母乳相對保護。",
            "C": "活力差、體溫不穩、腹脹、餵食不耐、血便到穿孔休克都符合 NEC 表現。",
            "D": "腸壁積氣是典型影像，但『通常在出生後 1 週內發生』過於絕對；早產兒常在較晚餵食後發生，因此為不適當敘述。",
        },
        "key_point": "NEC 以早產兒、餵食後腹脹血便與腸壁積氣為核心，發生時間常為出生後數天到數週。",
        "front": "壞死性腸炎 NEC",
    },
    6: {
        "analysis": "題目問先天性心臟病照護何者最不適當。感染預防、疫苗與脫水貧血照護都重要，但細菌性心內膜炎預防只限高風險心臟病與特定處置，不是所有先天性心臟病都需要。",
        "options": {
            "A": "多數常規疫苗與流感疫苗對先天性心臟病兒童是建議施打的，除非有個別禁忌。",
            "B": "有血行動力學顯著異常的嬰幼兒 RSV 感染風險高，單株抗體預防具重要性。",
            "C": "牙科處置前抗生素預防心內膜炎只適用於高風險族群，例如未修補發紺型、人工材料修補後早期或曾有心內膜炎者；『所有』兒童都需預防是錯的。",
            "D": "發紺性心臟病病童脫水會增加血栓風險，缺鐵會使缺氧耐受更差，需特別注意。",
        },
        "key_point": "心內膜炎預防不是所有先天性心臟病都做，而是限高風險病灶與高風險牙科處置。",
        "front": "先天性心臟病心內膜炎預防",
    },
    7: {
        "analysis": "PGE1 用於維持動脈導管開放，幫助導管依賴型的全身或肺循環。若問題是阻塞型全肺靜脈回流異常，關鍵是肺靜脈回流受阻，需緊急手術解除阻塞，PGE1 幫助有限。",
        "options": {
            "A": "嚴重主動脈弓窄縮屬導管依賴型全身循環，PGE1 可維持下半身灌流。",
            "B": "三尖瓣閉鎖常需靠開放性動脈導管增加肺血流，PGE1 有幫助。",
            "C": "危急型肺動脈瓣狹窄可能為導管依賴型肺循環，PGE1 可維持肺血流。",
            "D": "阻塞型 TAPVR 的主要問題不是動脈導管關閉，而是肺靜脈回流阻塞造成嚴重肺水腫與低氧，PGE1 最沒有幫助。",
        },
        "key_point": "PGE1 用於導管依賴型循環；阻塞型 TAPVR 需緊急解除肺靜脈阻塞。",
        "front": "PGE1 導管依賴型心臟病",
    },
    8: {
        "analysis": "新生兒脈搏血氧篩檢若下肢血氧比上肢低，提示右向左分流或導管依賴型左心阻塞病灶。輕中度肺動脈瓣狹窄通常不會造成這種嚴重發紺與上下肢差異。",
        "options": {
            "A": "左心室發育不全可造成導管依賴型全身循環與血氧異常，屬可能診斷。",
            "B": "大動脈轉位可在新生兒期造成發紺與脈搏血氧篩檢異常，屬可能診斷。",
            "C": "輕度或中度肺動脈瓣狹窄通常血流仍可通過肺動脈，不會是危急發紺型病灶，最不可能。",
            "D": "主動脈弓中斷屬導管依賴型全身循環病灶，可造成上下肢血氧差異與灌流問題。",
        },
        "key_point": "新生兒上下肢血氧差異要想到導管依賴型或重大發紺型心臟病；輕中度肺狹窄通常不會。",
        "front": "新生兒脈搏血氧篩檢",
    },
    9: {
        "analysis": "先天性巨大結腸症是遠端腸道神經節細胞缺如造成的功能性阻塞。題目問最適當敘述，重點在臨床可有腹脹、嘔吐、生長不良、便秘或腸炎相關腹瀉。",
        "options": {
            "A": "神經節細胞缺如位於狹窄的遠端腸段，不是在脹大的近端結腸，因此敘述錯誤。",
            "B": "胎便延遲可提示疾病，但早產兒胎便排出本來可較晚，不能只憑超過 48 小時診斷。",
            "C": "腹脹是常見表現，並可合併嘔吐、生長不良、便秘或 Hirschsprung-associated enterocolitis 造成腹瀉，最適當。",
            "D": "治療可依病況選擇一期 pull-through 或分期手術，不是唯一都必須先做造瘻。",
        },
        "key_point": "Hirschsprung disease 是遠端無神經節造成近端擴張；診斷靠直腸切片，治療不一定都分期造瘻。",
        "front": "先天性巨大結腸症",
    },
    10: {
        "analysis": "男童符合急性胰臟炎：典型腹背痛、lipase 超過正常上限 3 倍與影像胰臟腫大。治療以支持療法為主，包括疼痛控制、輸液與早期腸道營養；預防性抗生素不常規使用。",
        "options": {
            "A": "急性胰臟炎疼痛明顯，適當止痛是標準支持療法。",
            "B": "早期足量靜脈輸液可維持灌流並降低併發症風險，敘述適當。",
            "C": "嘔吐改善、疼痛可接受時可嘗試早期進食，兒童急性胰臟炎不需長期禁食。",
            "D": "無感染性壞死或其他感染證據時，不建議常規給預防性廣效抗生素，因此最不適當。",
        },
        "key_point": "兒童急性胰臟炎治療以止痛、輸液與早期進食為主；不要常規使用預防性抗生素。",
        "front": "兒童急性胰臟炎處置",
    },
    11: {
        "analysis": "題目比較肝炎病毒垂直感染。B 型肝炎在高病毒量或 HBeAg 陽性母親中垂直傳播風險最高，是新生兒免疫球蛋白與疫苗預防的重點。",
        "options": {
            "A": "A 型肝炎主要經糞口傳染，母嬰垂直感染並非常見路徑。",
            "B": "B 型肝炎可經產程血液體液暴露垂直感染，若未預防傳播率高，是最典型答案。",
            "C": "C 型肝炎可垂直感染，但整體風險通常低於未預防的 B 型肝炎。",
            "D": "E 型肝炎可使孕婦重症風險增加，但不是最容易垂直感染嬰兒的肝炎病毒。",
        },
        "key_point": "肝炎病毒垂直感染考題首選 B 型肝炎，預防靠新生兒 HBIG 加 HBV 疫苗。",
        "front": "肝炎垂直感染",
    },
    12: {
        "analysis": "題目問何者最不可能造成高血鉀。高血鉀常見於腎排鉀下降、細胞內鉀外移或藥物抑制排鉀；furosemide 是 loop diuretic，通常增加尿鉀流失，傾向造成低血鉀。",
        "options": {
            "A": "腎衰竭使鉀排泄下降，是高血鉀常見原因。",
            "B": "Furosemide 促進鈉鉀氯排出並增加遠端尿流，常造成低血鉀，最不可能造成高血鉀。",
            "C": "橫紋肌溶解會釋放細胞內鉀，可造成高血鉀。",
            "D": "Cyclosporine 可造成腎功能影響與遠端鉀排泄下降，可引起高血鉀。",
        },
        "key_point": "Loop diuretics 通常造成低血鉀；腎衰竭、組織崩解與 calcineurin inhibitor 可造成高血鉀。",
        "front": "高血鉀原因",
    },
    13: {
        "analysis": "CNDI 是腎臟對 ADH 反應不良造成多尿、高鈉與脫水風險。最常見為 X-linked AVPR2 突變；AQP2 突變較少見，多為 autosomal recessive 或 dominant。",
        "options": {
            "A": "最常見遺傳模式是 X-linked recessive，通常與 AVPR2 基因相關，敘述正確。",
            "B": "大多數 CNDI 是 AVPR2 而不是 AQP2 突變，因此是不適當敘述。",
            "C": "限制鈉攝取可降低滲透負荷與尿量，是治療原則之一。",
            "D": "Thiazide 可造成輕度體液收縮，增加近端水鈉再吸收，反而降低尿量，是常用治療。",
        },
        "key_point": "先天性腎源性尿崩症最常見 X-linked AVPR2 突變；治療包括低鈉飲食、thiazide、NSAID 等。",
        "front": "CNDI 遺傳與治療",
    },
    14: {
        "analysis": "AKI 處置重點是處理危及生命的電解質與體液問題。高血鉀要先穩定心肌再移鉀或排鉀；代謝性酸中毒可視情況補 bicarbonate，但不應積極把 HCO3 維持在正常上緣範圍。",
        "options": {
            "A": "高血鉀心電圖可見高尖 T 波、PR 延長、QRS 變寬，嚴重可致心律不整，敘述大致正確。",
            "B": "Calcium gluconate 主要穩定心肌膜，作用快但不降低血鉀，敘述正確。",
            "C": "若水分足夠仍對 furosemide 無反應，繼續利尿劑價值低，需限水並評估透析，敘述合理。",
            "D": "NaHCO3 應用於明顯酸中毒等情境，不是積極維持 HCO3 在 20-26 mEq/L；過度補充可造成鈉負荷與容量問題，最不適當。",
        },
        "key_point": "AKI 高血鉀先保心肌；bicarbonate 不是為了把 HCO3 常規維持在正常範圍。",
        "front": "兒童 AKI 高血鉀",
    },
    15: {
        "analysis": "ANA 是 SLE 很敏感但不夠特異的篩檢抗體。低力價 ANA 可見於健康人、感染或其他自體免疫疾病，所以不能說正常人不到 1% 陽性或特異度達 90%。",
        "options": {
            "A": "ANA titer 越高，自體免疫疾病可能性通常越高，但仍需搭配臨床判斷。",
            "B": "健康人可有一定比例 ANA 陽性，尤其低力價；ANA 特異度不高，因此此敘述最不適當。",
            "C": "SLE 患者 ANA 陽性率很高，常超過 95%，所以陰性 ANA 會讓 SLE 可能性下降。",
            "D": "ANA titer 不適合追蹤 SLE 活性；疾病活性常看 anti-dsDNA、補體與臨床器官表現。",
        },
        "key_point": "ANA 對 SLE 敏感但不特異，不能用 ANA titer 追蹤疾病活性。",
        "front": "ANA 解讀",
    },
    16: {
        "analysis": "SLE 是慢性自體免疫疾病，好發女性，可因免疫複合體沉積造成腎炎。血液系統常見白血球、淋巴球、血小板下降或溶血性貧血，不是上升。",
        "options": {
            "A": "狼瘡腎炎核心機轉是免疫複合體沉積與補體活化，敘述正確。",
            "B": "SLE 屬慢性反覆發炎性自體免疫疾病，敘述正確。",
            "C": "SLE 明顯好發於女性，尤其生育年齡女性，敘述正確。",
            "D": "SLE 的血液表現常是白血球低下、血小板低下與貧血；說白血球及血小板上升不適當。",
        },
        "key_point": "SLE 血液異常常是 cytopenia，不是白血球與血小板上升。",
        "front": "SLE 血液表現",
    },
    17: {
        "analysis": "嬰兒異位性皮膚炎通常在出生後數月逐漸出現，不是大多數出生即有。嬰兒期分布與過敏進程是常見考點。",
        "options": {
            "A": "多數患童不是一出生就有皮膚炎，常在 2-6 個月後出現，因此最不適當。",
            "B": "異位性皮膚炎與日後氣喘、過敏性鼻炎相關，屬 atopic march。",
            "C": "嬰兒期常見於臉頰、頭皮與四肢伸側；年長兒較常在屈側。",
            "D": "家族史、早發嚴重病灶與高 IgE 可提示較差預後或持續過敏傾向。",
        },
        "key_point": "嬰兒異位性皮膚炎多在出生後數月出現，嬰兒期好發臉頰、頭皮與伸側。",
        "front": "嬰兒異位性皮膚炎",
    },
    18: {
        "analysis": "兒童 ALL 預後染色體變化常考：ETV6-RUNX1 與 hyperdiploidy 通常預後較好；KMT2A rearrangement，尤其 t(4;11)，預後不佳。",
        "options": {
            "A": "ETV6-RUNX1 t(12;21) 是兒童 ALL 常見且預後較好的變化。",
            "B": "Hyperdiploidy 超過 50 條染色體通常屬預後較佳族群。",
            "C": "KMT2A(MLL)-AF4 t(4;11) 與嬰兒 ALL、較高風險及預後不佳相關，是正確答案。",
            "D": "TLX1/HOX11 t(10;14) 可見於 T-ALL，並非本題最典型的不良預後答案。",
        },
        "key_point": "兒童 ALL：ETV6-RUNX1、hyperdiploidy 較好；KMT2A rearrangement 較差。",
        "front": "ALL 預後基因",
    },
    19: {
        "analysis": "題目問癌症易感症候群配對何者最不適當。NF1 常見 optic pathway glioma 與 MPNST；NF2 典型是雙側 vestibular schwannoma、meningioma、ependymoma，不是 optic glioma。",
        "options": {
            "A": "NF1 可發生惡性周邊神經鞘腫瘤，配對正確。",
            "B": "視神經膠質瘤典型與 NF1 相關，不是 NF2 的代表腫瘤，因此最不適當。",
            "C": "家族性視網膜母細胞瘤 RB1 突變者日後骨肉瘤風險上升，配對正確。",
            "D": "Li-Fraumeni 與肉瘤、乳癌、腦瘤、腎上腺皮質癌等相關，配對正確。",
        },
        "key_point": "NF1 配 optic glioma 與 MPNST；NF2 配 vestibular schwannoma。",
        "front": "遺傳性癌症症候群",
    },
    20: {
        "analysis": "G6PD 缺乏在氧化壓力後會發生急性溶血，表現深色尿、黃疸與貧血。抹片可見 Heinz body 經脾臟咬除後形成 bite cell。",
        "options": {
            "A": "G6PD 缺乏為 X-linked recessive，不是體染色體隱性；雖是臺灣新生兒篩檢項目，但前半錯誤。",
            "B": "氧化性溶血可見 bite cell、blister cell 等紅血球形態，最適當。",
            "C": "G6PD 是非免疫性溶血，Coombs test 通常陰性，不是 Coombs positive hemolysis。",
            "D": "Aspirin 可能增加溶血風險，G6PD 缺乏者退燒止痛選藥需避免高風險氧化藥物，不能說較適合。",
        },
        "key_point": "G6PD 缺乏是 X-linked 氧化性溶血，抹片可見 bite cell，Coombs test 通常陰性。",
        "front": "G6PD 溶血",
    },
    21: {
        "analysis": "兒童異物吸入急救重點是避免盲目手指挖取，因為可能把異物推得更深。依年齡與意識狀態選擇咳嗽鼓勵、背拍胸壓或腹部壓迫。",
        "options": {
            "A": "上呼吸道阻塞可能出現喘鳴或吸氣性聲音，敘述正確。",
            "B": "未看到異物時不可盲目伸手挖取，可能讓阻塞惡化，因此最不適當。",
            "C": "清醒且能有效咳嗽時，鼓勵咳嗽是合理處置。",
            "D": "小於 1 歲使用背拍加胸壓，大於 1 歲可用腹部壓迫，敘述正確。",
        },
        "key_point": "異物吸入急救不可盲目 finger sweep；只有看得到且能安全取出時才取異物。",
        "front": "兒童異物吸入急救",
    },
    22: {
        "analysis": "2 歲安靜時若有明顯心搏過速，要警覺發燒、疼痛、脫水、休克或組織灌流不足。其他選項多為正常或灌流良好的表現。",
        "options": {
            "A": "2 歲安靜呼吸每分鐘 20-30 次大致可接受，單獨不提示灌流不足。",
            "B": "安靜心跳每分鐘 160 下偏高，可能是休克或代償性心搏過速，需注意組織灌流不足。",
            "C": "四肢溫暖且無大理石斑通常代表周邊灌流尚可。",
            "D": "微血管回填 1.5 秒屬正常範圍，不支持灌流不足。",
        },
        "key_point": "兒童休克早期常靠心搏過速代償；安靜時明顯 tachycardia 要警覺灌流不足。",
        "front": "兒童灌流不足",
    },
    23: {
        "analysis": "生長激素治療有多個適應症，包括 Turner、SHOX 缺陷、Prader-Willi 等；DiGeorge syndrome 並非典型 FDA 與健保給付適應症。",
        "options": {
            "A": "DiGeorge syndrome 主要是 22q11.2 deletion，典型問題為心臟、胸腺、低鈣與顏面異常，不是生長激素常規適應症。",
            "B": "Turner syndrome 是生長激素治療的經典適應症之一。",
            "C": "SHOX gene abnormality 可造成身材矮小，屬生長激素可考慮的適應症。",
            "D": "Prader-Willi syndrome 可使用生長激素改善身高、體組成與肌張力等，屬適應症之一。",
        },
        "key_point": "GH 治療常見適應症包括 GH deficiency、Turner、SHOX deficiency、Prader-Willi 等，不包括 DiGeorge 作為常規適應症。",
        "front": "生長激素適應症",
    },
    24: {
        "analysis": "失鹽型先天性腎上腺增生症最常見為 21-hydroxylase deficiency，造成 cortisol 與 aldosterone 不足，急性期出現低血鈉、高血鉀、代謝性酸中毒、低血糖與脫水休克。",
        "options": {
            "A": "Aldosterone 不足使氫離子排泄下降，可有代謝性酸血症，符合。",
            "B": "Aldosterone 不足造成腎臟鈉流失，低血鈉符合。",
            "C": "典型是高血鉀，不是低血鉀，因此最不符合。",
            "D": "Cortisol 不足可造成低血糖，尤其嬰幼兒急性發作時常見。",
        },
        "key_point": "失鹽型 CAH 急性危象：低鈉、高鉀、酸中毒、低血糖與脫水。",
        "front": "失鹽型 CAH",
    },
    25: {
        "analysis": "甲狀腺腫大合併 retroorbital tissue 淋巴球與漿細胞浸潤、家族自體免疫病史，指向 Graves disease；Graves 的眼病變與 TSH receptor 相關自體免疫反應有關。",
        "options": {
            "A": "Chronic lymphocytic thyroiditis 是 Hashimoto thyroiditis，雖有淋巴球浸潤與甲狀腺腫，但不典型造成後眼眶組織浸潤。",
            "B": "Graves disease 可有甲狀腺腫與 Graves ophthalmopathy，後眼眶組織浸潤支持此診斷。",
            "C": "Toxic multinodular goiter 多見於較年長者，與後眼眶免疫浸潤不符。",
            "D": "急性感染性甲狀腺炎通常疼痛、發燒並以感染發炎為主，不符合自體免疫眼病變。",
        },
        "key_point": "Graves disease 可造成甲狀腺功能亢進與眼眶病變；後眼眶淋巴球浸潤是重要線索。",
        "front": "Graves disease 眼病變",
    },
    26: {
        "analysis": "此嬰兒發燒超過 5 天、皮疹、四肢變化、結膜炎、草莓舌與頸部淋巴結，符合 Kawasaki disease。IVIG 後活性疫苗需延後，但題目把日本腦炎疫苗也列為需延後，較不適當。",
        "options": {
            "A": "Kawasaki disease 又稱 mucocutaneous lymph node syndrome，診斷最可能。",
            "B": "急性期 IVIG 後退燒可用低劑量 aspirin 作為抗血小板治療，敘述適當。",
            "C": "IVIG 會干擾麻疹、水痘等活性減毒疫苗抗體反應；日本腦炎疫苗在現行常規多為不活化疫苗，不能一概因 IVIG 延後，故最不適當。",
            "D": "Kawasaki 最重要併發症是冠狀動脈擴張或動脈瘤，需心臟超音波追蹤。",
        },
        "key_point": "Kawasaki disease 治療為 IVIG 加 aspirin，需追蹤冠狀動脈；IVIG 後主要延後活性疫苗。",
        "front": "Kawasaki disease 與 IVIG",
    },
    27: {
        "analysis": "10 個月大嬰兒可接種的疫苗要看年齡限制。流感不活化疫苗通常 6 個月以上即可接種；其他選項多不符合年齡。",
        "options": {
            "A": "4 價去活化流感疫苗可用於 6 個月以上嬰幼兒，10 個月大適合。",
            "B": "23 價肺炎鏈球菌多醣體疫苗通常用於 2 歲以上高風險族群，不適合一般 10 個月嬰兒。",
            "C": "日本腦炎疫苗常規接種年齡較晚，10 個月通常未到接種時程。",
            "D": "HPV 疫苗用於青少年或較年長兒童，10 個月嬰兒不適合。",
        },
        "key_point": "不活化流感疫苗 6 個月以上可接種；PPSV23、JE、HPV 各有較晚年齡限制。",
        "front": "嬰兒疫苗年齡",
    },
    28: {
        "analysis": "13 個月大發燒、咳嗽流鼻水、結膜炎後出疹，需鑑別麻疹、Kawasaki disease、病毒疹或細菌感染。IgE 是過敏評估，對這類感染與發炎診斷最沒有幫助。",
        "options": {
            "A": "IgE 主要評估過敏體質，無法有效區分麻疹、Kawasaki 或細菌感染，最沒有幫助。",
            "B": "疫苗史、接觸史與旅遊史對麻疹等傳染病診斷非常重要。",
            "C": "若考慮 Kawasaki disease，心臟超音波評估冠狀動脈有幫助。",
            "D": "持續發燒且 CRP 上升時，血液培養可協助排除細菌感染。",
        },
        "key_point": "發燒結膜炎與皮疹要查疫苗接觸旅遊史並鑑別麻疹與 Kawasaki；IgE 對急性診斷幫助低。",
        "front": "兒童發燒皮疹鑑別",
    },
    29: {
        "analysis": "嬰兒餵食困難、張力低、發展遲緩、眼神互動差，加上母系親屬有智能不足與早夭，提示粒線體疾病可有母系遺傳表現；Leigh syndrome 是嬰幼兒期神經退化與張力低下的重要診斷。",
        "options": {
            "A": "Prader-Willi 可有新生兒低張與餵食困難，但家族母系早夭與多系統神經退化線索較不典型。",
            "B": "Duchenne muscular dystrophy 常在較大幼兒出現近端肌無力與 Gowers sign，8 個月不會翻身合併母系多位智能不足早夭不典型。",
            "C": "Congenital myasthenic syndromes 主要為神經肌肉接合傳遞障礙，不解釋母系遺傳與明顯互動/智能線索。",
            "D": "Leigh syndrome 可有嬰幼兒期餵食困難、低張、發展遲緩與神經退化，且粒線體遺傳可呈母系家族史，最可能。",
        },
        "key_point": "嬰幼兒低張、餵食困難、發展遲緩合併母系家族史，要想到粒線體疾病如 Leigh syndrome。",
        "front": "Leigh syndrome",
    },
    30: {
        "analysis": "2 歲發展評估要分辨該年齡應會與較晚才出現的能力。揮手再見屬嬰幼兒早期社交溝通能力，2 歲仍不會是明顯警訊。",
        "options": {
            "A": "單腳站通常是較晚的粗動作里程碑，2 歲不會不一定異常。",
            "B": "騎三輪車常在約 3 歲左右出現，2 歲不會不算警訊。",
            "C": "畫圓多在約 3 歲左右成熟，2 歲不會不一定遲緩。",
            "D": "揮手再見應在 2 歲前已具備，若 2 歲仍不會，需警覺社交溝通或整體發展遲緩。",
        },
        "key_point": "2 歲不會揮手再見是發展警訊；單腳站、騎三輪車、畫圓屬較晚里程碑。",
        "front": "2 歲發展警訊",
    },
    31: {
        "analysis": "3 歲男童語言表達明顯落後、眼神迴避、重複玩小車與看旋轉物，符合自閉症類群障礙的社交溝通缺損與侷限重複行為。",
        "options": {
            "A": "Rett syndrome 多見於女童，典型有早期正常後退化、手部刻板動作與頭圍成長減慢，與題幹不符。",
            "B": "ADHD 以不專注、過動與衝動為主，不能解釋眼神迴避與重複侷限興趣。",
            "C": "學習障礙通常在學齡期學業技能困難時明顯，不以 3 歲社交溝通與重複行為為核心。",
            "D": "自閉症類群障礙最能解釋語言社交缺損、眼神迴避與侷限重複行為。",
        },
        "key_point": "ASD 核心為社交溝通缺損加侷限重複行為，幼兒常見語言遲緩與眼神互動差。",
        "front": "自閉症類群障礙",
    },
    32: {
        "analysis": "未具水痘免疫的醫療人員暴露後，若無禁忌，應在暴露後儘快接種水痘疫苗，通常 3-5 天內可降低感染或疾病嚴重度。",
        "options": {
            "A": "等到有症狀才治療會錯過暴露後預防與院內感染控制時機。",
            "B": "抗病毒藥可用於特定高風險暴露或發病後治療，但健康、無免疫力者首要是暴露後接種疫苗。",
            "C": "立即接種水痘疫苗是最適當的暴露後處置。",
            "D": "隔離觀察時間通常需依潛伏期與院內政策安排，不是只在家隔離一週即可；且仍應做暴露後預防。",
        },
        "key_point": "無免疫力者暴露水痘後，無禁忌時應儘快接種水痘疫苗作暴露後預防。",
        "front": "水痘暴露後預防",
    },
    33: {
        "analysis": "Trisomy 18 常見小頭、小下巴、拳頭緊握、重疊手指、搖椅腳與凸枕。扁平枕骨比較典型聯想到 Down syndrome。",
        "options": {
            "A": "小頭可見於 Edwards syndrome，屬常見表徵。",
            "B": "小下巴是 Edwards syndrome 常見顏面特徵。",
            "C": "Edwards syndrome 典型是 prominent occiput，而非 flat occiput；扁平枕骨較像 Down syndrome，因此不是常見表徵。",
            "D": "Rocker-bottom feet 是 Edwards syndrome 經典表徵之一。",
        },
        "key_point": "Trisomy 18 典型為 prominent occiput、小下巴、拳頭緊握與 rocker-bottom feet；flat occiput 偏 Down syndrome。",
        "front": "Trisomy 18 表徵",
    },
    34: {
        "analysis": "異位性皮膚炎與 Th2 發炎、皮膚屏障缺損及感染併發症有關。Filaggrin 突變是重要危險因子，但不是絕大多數患者都有。",
        "options": {
            "A": "Th2 免疫反應與 IL-4、IL-13 等路徑在異位性皮膚炎很重要，敘述正確。",
            "B": "病灶常有金黃色葡萄球菌移生，也可能發生 eczema herpeticum，敘述正確。",
            "C": "Filaggrin 突變增加風險且與較嚴重病程相關，但並非絕大多數患者都有，故錯誤。",
            "D": "濕疹樣病灶合併血小板低下與免疫缺陷要想到 Wiskott-Aldrich syndrome，敘述正確。",
        },
        "key_point": "Filaggrin 突變是異位性皮膚炎風險因子，但不是所有或絕大多數患者都有。",
        "front": "異位性皮膚炎 filaggrin",
    },
    35: {
        "analysis": "題目問藥物皮膚反應何者正確。Sorafenib 等 multikinase/signal transduction inhibitors 可造成 hand-foot skin reaction 與落髮，屬常考藥疹型態。",
        "options": {
            "A": "AGEP 常與抗生素相關且出現無菌小膿疱，但典型不是以關節炎為主要特徵，此敘述混入不典型內容。",
            "B": "Tetracycline 可造成光敏感反應，常影響 sun-exposed areas，不是只造成黏膜色素沉著。",
            "C": "藥物誘發 subacute cutaneous lupus erythematosus 通常可在用藥後數週到數月出現，不是平均一週內。",
            "D": "Sorafenib 可引起手足皮膚反應與落髮，敘述正確。",
        },
        "key_point": "Sorafenib 等標靶藥常考 hand-foot skin reaction；tetracycline 可光敏感。",
        "front": "藥物皮膚反應",
    },
    36: {
        "analysis": "乾癬性關節炎診斷線索包括乾癬皮疹、指甲病變、dactylitis、enthesitis 與 RF 陰性傾向。RF 陽性反而較支持類風濕關節炎，對乾癬性關節炎幫助較小。",
        "options": {
            "A": "香腸指是乾癬性關節炎重要臨床特徵，有診斷幫助。",
            "B": "頭皮乾癬是乾癬病灶常見位置，支持乾癬性關節炎背景。",
            "C": "類風濕因子陽性較支持 rheumatoid arthritis，乾癬性關節炎常為 seronegative，因此幫助較無。",
            "D": "指甲點狀凹陷、甲床分離或增厚常見於乾癬，對診斷有幫助。",
        },
        "key_point": "Psoriatic arthritis 常見 dactylitis、nail pitting、乾癬皮疹與 RF 陰性。",
        "front": "乾癬性關節炎診斷",
    },
    37: {
        "analysis": "甲癬可由 dermatophytes、yeasts 或 nondermatophyte molds 引起，常伴足癬。治療效果較佳的口服藥多為 terbinafine 或 itraconazole；griseofulvin 不是最佳選擇。",
        "options": {
            "A": "非皮癬菌黴菌也可造成甲癬，尤其在特定宿主或環境中，敘述正確。",
            "B": "足癬常與甲癬共存，腳部皮膚可作為感染來源，敘述正確。",
            "C": "Griseofulvin 治療甲癬療程長、效果較差，現今不是最佳口服選擇，因此錯誤。",
            "D": "糖尿病與免疫低下如 HIV 是甲癬危險因子，敘述正確。",
        },
        "key_point": "甲癬口服治療常用 terbinafine 或 itraconazole；griseofulvin 不是效果最佳選擇。",
        "front": "甲癬治療",
    },
    38: {
        "analysis": "疥瘡治療以 permethrin 5% 外用為常用第一線；crusted/Norwegian scabies 常需外用殺疥藥合併口服 ivermectin 並處理接觸者與環境。",
        "options": {
            "A": "Lindane 有神經毒性疑慮，老人與小孩不建議作第一線。",
            "B": "孕婦通常避免口服 ivermectin，較常選擇 permethrin 等安全性較佳外用藥。",
            "C": "Crotamiton 效果較不穩定，不是目前最有效外用藥。",
            "D": "挪威型疥瘡蟲量高，常需 permethrin 合併口服 ivermectin 治療，敘述正確。",
        },
        "key_point": "疥瘡第一線常用 permethrin；crusted scabies 可合併 oral ivermectin。",
        "front": "疥瘡治療",
    },
    39: {
        "analysis": "黑色素沿指甲延伸到近端或側方甲褶皮膚稱 Hutchinson sign，是 subungual/acral lentiginous melanoma 的重要警訊。",
        "options": {
            "A": "Darier sign 是摩擦肥大細胞病灶後出現風團紅斑，與甲周黑色素延伸無關。",
            "B": "Hutchinson sign 指甲色素延伸到甲周皮膚，支持甲下或肢端惡性黑色素瘤。",
            "C": "Auspitz sign 是刮除乾癬鱗屑後點狀出血，與本題不符。",
            "D": "Nikolsky sign 是摩擦皮膚造成表皮剝離，見於 pemphigus vulgaris 或 SJS/TEN 等。",
        },
        "key_point": "甲色素延伸到甲周皮膚是 Hutchinson sign，需警覺 melanoma。",
        "front": "Hutchinson sign",
    },
    40: {
        "analysis": "腎移植後免疫抑制病人出現紫色斑塊丘疹，切片有 spindle cells 與 slit-like vascular spaces，最符合 Kaposi sarcoma，與 HHV-8 及免疫抑制相關。",
        "options": {
            "A": "血管肉瘤雖為血管性惡性腫瘤，但臨床與移植後紫色多發病灶、HHV-8 典型線索較不合。",
            "B": "隆凸性皮膚纖維肉瘤常為緩慢生長的隆起斑塊或結節，病理不以裂隙狀血管腔為典型。",
            "C": "Kaposi sarcoma 典型為紫紅色斑塊/丘疹，病理有紡錘細胞與裂隙狀血管腔，最可能。",
            "D": "鬱血性皮膚炎多與靜脈功能不全相關，病理與題幹不符。",
        },
        "key_point": "免疫抑制病人紫色皮膚病灶加 spindle cells、slit-like vascular spaces 要想到 Kaposi sarcoma。",
        "front": "Kaposi sarcoma",
    },
    41: {
        "analysis": "四肢與手掌靶心樣紅疹、反覆發作，符合 erythema multiforme。最常見相關病原是 herpes simplex virus，尤其復發型。",
        "options": {
            "A": "Treponema pallidum 可造成二期梅毒皮疹含手掌足底，但不是典型靶心樣反覆 erythema multiforme 的主要病原。",
            "B": "HSV 是 erythema multiforme 最常見感染誘因，尤其反覆發作者，最相關。",
            "C": "Enterovirus 71 可造成手足口病與神經併發症，不是此靶心樣反覆病灶的主要關聯。",
            "D": "EBV 可造成多種皮疹或傳染性單核球增多症，但與 erythema multiforme 的典型高關聯不如 HSV。",
        },
        "key_point": "Erythema multiforme 的反覆靶心樣病灶最常與 HSV 相關。",
        "front": "多形性紅斑 HSV",
    },
    42: {
        "analysis": "停經荷爾蒙治療後臉部色素沉著，最像 melasma。治療重點是防曬、避免誘因與外用淡斑藥，例如 hydroquinone；雷射不是第一線最佳選擇。",
        "options": {
            "A": "Melasma 較常見於較深膚色族群與女性，不能說白人較易發生。",
            "B": "Melasma 與荷爾蒙、紫外線、膚色相關，通常不伴肝功能異常。",
            "C": "CO2 雷射不是 melasma 最佳處置，且可能造成發炎後色素沉著。",
            "D": "Hydroquinone 外用可抑制黑色素生成，是常用治療之一。",
        },
        "key_point": "Melasma 治療以防曬與外用 hydroquinone 等淡斑藥為主。",
        "front": "Melasma 治療",
    },
    43: {
        "analysis": "Epidermolysis bullosa 是遺傳性皮膚脆弱與水疱疾病，依皮膚裂解層次分類；不是自體免疫水疱病，因此治療不以免疫抑制為主。",
        "options": {
            "A": "由淺到深為 EB simplex、junctional EB、dystrophic EB，敘述正確。",
            "B": "Localized EB simplex 是常見 subtype，敘述正確。",
            "C": "嚴重 EB 可合併指甲、牙齒、眼睛、頭髮或黏膜等問題，敘述正確。",
            "D": "EB 屬遺傳性結構蛋白缺陷，不是自體免疫水疱病；治療以傷口照護、防感染與營養支持為主，故錯誤。",
        },
        "key_point": "EB 是遺傳性皮膚裂解疾病，不是免疫性水疱病。",
        "front": "Epidermolysis bullosa",
    },
    44: {
        "analysis": "大腦靜脈竇栓塞危險因子包括避孕藥、懷孕產褥、感染、惡性腫瘤與血栓形成體質。高同半胱胺酸血症會增加血栓風險，不是同半胱胺酸缺乏。",
        "options": {
            "A": "口服避孕藥會增加靜脈血栓風險，是 CVST 常見危險因子。",
            "B": "抗磷脂質症候群造成血栓傾向，可導致 CVST。",
            "C": "腦膜炎或頭頸部感染可造成局部靜脈竇血栓，屬可能原因。",
            "D": "血栓風險與高同半胱胺酸血症相關，不是同半胱胺酸缺乏，因此最不會是原因。",
        },
        "key_point": "CVST 危險因子含 OCP、APS、感染與高同半胱胺酸血症。",
        "front": "CVST 危險因子",
    },
    45: {
        "analysis": "Factor Xa inhibitor 相關腦出血需立即停藥、支持治療並考慮反轉抗凝。若特異性 andexanet alfa 不在選項中，常考答案為 PCC。",
        "options": {
            "A": "新鮮冷凍血漿對直接 factor Xa inhibitor 的反轉效果有限，且需大量輸注。",
            "B": "Idarucizumab 是 dabigatran 的反轉劑，不是 factor Xa inhibitor 的主要反轉劑。",
            "C": "Prothrombin complex concentrate 可作為 factor Xa inhibitor 出血時的反轉治療選項，最恰當。",
            "D": "血小板輸注用於血小板低下或抗血小板藥相關情境，不能反轉 factor Xa inhibitor。",
        },
        "key_point": "Factor Xa inhibitor 嚴重出血若無 andexanet alfa 選項，考 PCC；idarucizumab 用於 dabigatran。",
        "front": "Factor Xa inhibitor 反轉",
    },
    46: {
        "analysis": "缺血性腦中風時 ATP 下降導致離子幫浦失效、去極化、glutamate excitotoxicity、鈣離子內流、自由基與發炎反應；細胞內鈣不是降低而是上升。",
        "options": {
            "A": "缺氧缺糖使粒線體無法有效生成 ATP，是缺血傷害起點之一。",
            "B": "缺血造成細胞內鈣離子濃度上升，啟動酵素與細胞死亡路徑；說降低最不可能。",
            "C": "Glutamate excitotoxicity 與自由基生成是缺血傷害的重要機轉。",
            "D": "缺血後發炎與血腦屏障破壞會加重腦傷，敘述正確。",
        },
        "key_point": "腦缺血的 excitotoxicity 會造成細胞內 Ca2+ 上升、自由基與發炎反應。",
        "front": "缺血性腦傷機轉",
    },
    47: {
        "analysis": "早晨肌陣攣、睡眠不足誘發、全身強直陣攣發作、正常智力與 generalized spike/polyspike-wave，符合 juvenile myoclonic epilepsy。傳統最有效廣效抗癲癇藥為 valproate，但女性與肝病史需臨床謹慎。",
        "options": {
            "A": "Valproate 對 JME 的肌陣攣與全面性發作效果佳，是官方答案邏輯下最適合。",
            "B": "Levetiracetam 也可用於 JME，且在育齡女性常被考慮，但本題官方答案選 valproate。",
            "C": "Phenytoin 對全面性強直陣攣可有效，但可能惡化 myoclonic seizure，不是 JME 首選。",
            "D": "Carbamazepine 可能惡化肌陣攣與失神發作，不適合 JME。",
        },
        "key_point": "JME 典型為青少年早晨肌陣攣、睡眠不足誘發；valproate 傳統效果佳，但育齡女性與肝病需權衡。",
        "front": "Juvenile myoclonic epilepsy",
        "notes": ["官方答案為 valproate；因題幹為 13 歲女性且提到肝炎病史，實務上需評估肝功能與致畸風險，可人工複核是否符合現代用藥偏好。"],
    },
    48: {
        "analysis": "Delayed sleep phase syndrome 是生理時鐘延後，治療目標是把睡眠相位往前移。早晨強光與傍晚低劑量 melatonin 可提前相位；晚上照光會使相位更延後。",
        "options": {
            "A": "晚上照光會延後晝夜節律，會讓延遲型睡眠週期更惡化，最不合適。",
            "B": "傍晚或睡前前段低劑量 melatonin 可幫助相位提前，屬治療選項。",
            "C": "每天延後睡覺 2-3 小時的 chronotherapy 可繞行重置時鐘，是可用但需嚴格執行的方法。",
            "D": "晚間使用 melatonin agonist 可協助調整生理時鐘，屬合理治療。",
        },
        "key_point": "延遲型睡眠相位治療要相位提前；早晨光照、傍晚 melatonin，避免晚上強光。",
        "front": "Delayed sleep phase 治療",
    },
    49: {
        "analysis": "癲癇治療預後常考：多數病人可用抗癲癇藥達到控制或緩解，約 60-70%。其他選項對病因與外傷後癲癇比例描述過度誇大或錯置。",
        "options": {
            "A": "腦傷後並非 90% 都在一年內發生創傷後癲癇，此比例明顯過高。",
            "B": "癲癇病因隨年齡不同；頭部外傷不是所有年齡層最常見病因。",
            "C": "小於 15 歲癲癇常與遺傳、先天、感染或發展因素相關，腦血管病變不是最常見。",
            "D": "抗癲癇藥治療後約 6-7 成病人可達發作緩解，敘述正確。",
        },
        "key_point": "癲癇約 60-70% 可用藥達到發作控制；癲癇病因會隨年齡改變。",
        "front": "癲癇治療預後",
    },
    50: {
        "analysis": "快速進展失智、視幻覺、步態不穩、聲音誘發肌陣攣與 DWI 典型高訊號，最符合 Creutzfeldt-Jakob disease。",
        "options": {
            "A": "邊緣性腦炎可有記憶與精神症狀，但典型 MRI 位置與肌陣攣、快速進展失智組合不如 CJD。",
            "B": "CJD 典型為快速進展失智、肌陣攣、共濟失調與 DWI 皮質/基底核異常，最可能。",
            "C": "血管性失智常呈階梯式退化並有血管病灶，不符合快速進展與 startle myoclonus。",
            "D": "多發性硬化症多為年輕成人復發緩解的中樞脫髓鞘，與 66 歲快速進展失智不符。",
        },
        "key_point": "快速進展失智加肌陣攣與 DWI 典型異常，要想到 CJD。",
        "front": "Creutzfeldt-Jakob disease",
    },
    51: {
        "analysis": "Memantine 用於中重度 Alzheimer disease，主要是 NMDA glutamate receptor antagonist，可降低 glutamate excitotoxicity。",
        "options": {
            "A": "乙醯膽鹼酯酶抑制劑是 donepezil、rivastigmine、galantamine 等，不是 memantine。",
            "B": "Memantine 的主要機轉是阻斷 NMDA glutamate 受體，為正確答案。",
            "C": "抑制 gamma secretase 是針對 amyloid 生成的研究方向，不是 memantine 機轉。",
            "D": "抑制 beta secretase 也不是 memantine 的作用機轉。",
        },
        "key_point": "Memantine 是 NMDA receptor antagonist；donepezil 類才是 cholinesterase inhibitor。",
        "front": "Memantine 機轉",
    },
    52: {
        "analysis": "ALS 是上下運動神經元退化疾病，多數散發，少數家族性。SOD1 是早期重要發現基因，但目前歐洲最常見 familial ALS 原因通常是 C9orf72 repeat expansion，不是 SOD1。",
        "options": {
            "A": "ALS 會造成上下運動神經元漸進退化，散發與家族性臨床上可相似，敘述正確。",
            "B": "ALS 與 FTD 有基因與病理光譜重疊，臨床變異性高，敘述正確。",
            "C": "SOD1 是第一個被發現的重要 ALS 基因之一，但不是目前歐洲最常見 familial ALS 原因，因此錯誤。",
            "D": "無痛漸進肌無力萎縮、肌束跳動、缺乏感覺與眼外肌/膀胱症狀，符合 ALS 線索。",
        },
        "key_point": "Familial ALS 常見基因包括 C9orf72、SOD1 等；歐洲最常見多為 C9orf72，不是 SOD1。",
        "front": "ALS 基因",
    },
    53: {
        "analysis": "Lambert-Eaton myasthenic syndrome 是自體抗體攻擊 presynaptic P/Q-type voltage-gated calcium channel，造成 acetylcholine 釋放減少，不是鉀離子通道。",
        "options": {
            "A": "LEMS 抗體目標是突觸前電壓依賴性鈣離子通道，不是鉀離子通道，因此錯誤。",
            "B": "LEMS 多於成年人發病，常需尋找腫瘤，敘述正確。",
            "C": "約半數與惡性腫瘤相關，尤其 small cell lung cancer，敘述正確。",
            "D": "自律神經症狀如口乾、便秘、陽痿可見，敘述正確。",
        },
        "key_point": "LEMS 是 presynaptic P/Q-type calcium channel antibody，常合併 small cell lung cancer 與口乾。",
        "front": "Lambert-Eaton syndrome",
    },
    54: {
        "analysis": "三叉神經痛是三叉神經分布的短暫劇烈電擊樣疼痛，常由根入口區血管壓迫引起，最典型壓迫血管是 superior cerebellar artery，不是 inferior cerebellar artery。",
        "options": {
            "A": "疼痛局限於三叉神經一支或多支分布，符合三叉神經痛。",
            "B": "三叉神經痛較常見於中老年人，敘述正確。",
            "C": "血管壓迫機轉正確，但典型是 superior cerebellar artery；說尤其是 inferior cerebellar artery 錯誤。",
            "D": "Carbamazepine 是三叉神經痛第一線藥物之一，敘述正確。",
        },
        "key_point": "三叉神經痛常由 superior cerebellar artery 壓迫，治療常用 carbamazepine。",
        "front": "三叉神經痛",
    },
    55: {
        "analysis": "GBS 若合併呼吸肌無力屬嚴重病程，需加護監測呼吸並給免疫治療。有效治療為 IVIG 或 plasma exchange；選項中首選為血漿交換/分離術。",
        "options": {
            "A": "類固醇對 GBS 整體效果不佳，並非首選治療。",
            "B": "Cyclophosphamide 不是 GBS 急性期標準治療。",
            "C": "呼吸肌無力有生命危險，不能只做一般支持性治療。",
            "D": "Plasma exchange 可移除致病抗體，與 IVIG 同為有效治療；本題選項中最適當。",
        },
        "key_point": "GBS 嚴重或呼吸肌無力時用 IVIG 或 plasma exchange，類固醇不是首選。",
        "front": "GBS 治療",
    },
    56: {
        "analysis": "MS 與 NMOSD 都女性較多，但 NMOSD 的女性優勢更明顯；不能說 NMOSD 男比女多。其他選項是兩者鑑別重點。",
        "options": {
            "A": "MS 女多於男，NMOSD 也多見於女性，因此此比較錯誤。",
            "B": "NMOSD 發作常較嚴重，視神經炎與脊髓炎預後可比 MS 差，敘述正確。",
            "C": "MS 常見 CSF oligoclonal bands；NMOSD 與 aquaporin-4 antibody 相關，敘述正確。",
            "D": "MS 脊髓病灶通常短於 3 節，NMOSD 常為 longitudinally extensive transverse myelitis，敘述正確。",
        },
        "key_point": "NMOSD 不是男多於女；AQP4 antibody 與長節段脊髓炎是鑑別重點。",
        "front": "MS vs NMOSD",
    },
    57: {
        "analysis": "腦下垂體腫瘤可壓迫視交叉造成雙顳側偏盲、頭痛與視力問題。壓迫 pituitary stalk 會減少 dopamine 抑制而造成泌乳激素上升，不是低下。",
        "options": {
            "A": "腫瘤向上壓迫視交叉可造成雙顳側偏盲，敘述正確。",
            "B": "視交叉或視神經受壓可造成視力下降，敘述正確。",
            "C": "Pituitary tumor 常見 hyperprolactinemia，尤其 prolactinoma 或 stalk effect；說低泌乳激素最不恰當。",
            "D": "頭痛可因腫瘤體積效應或鞍區壓力而出現，敘述正確。",
        },
        "key_point": "Pituitary tumor 可造成雙顳側偏盲、頭痛與高泌乳激素。",
        "front": "腦下垂體腫瘤",
    },
    58: {
        "analysis": "Huntington disease 與多種 spinocerebellar ataxia 是 trinucleotide repeat expansion。Wilson disease 是 ATP7B 銅代謝基因突變，不是三核苷酸重複擴增。",
        "options": {
            "A": "Huntington disease 是 HTT 基因 CAG repeat expansion，屬三核苷酸重複擴增。",
            "B": "SCA type 2 是 ATXN2 CAG repeat expansion，屬此類疾病。",
            "C": "Wilson disease 是 ATP7B 突變造成銅代謝異常，不是 trinucleotide repeat expansion。",
            "D": "SCA type 3/Machado-Joseph disease 是 ATXN3 CAG repeat expansion。",
        },
        "key_point": "Wilson disease 是 ATP7B 銅代謝缺陷；Huntington 與多種 SCA 才是 CAG repeat expansion。",
        "front": "三核苷酸重複疾病",
    },
    59: {
        "analysis": "Catatonia 可見於 mood disorders、psychotic disorders、藥物或身體疾病。現代臨床中 mood disorders 是常見原因，不能說住院病人以 schizophrenia 最多且情感疾患次之。",
        "options": {
            "A": "Catatonia 可有 stupor、mutism，也可有 agitation，運動活動減少或增加可交替，敘述正確。",
            "B": "僵直狀態常見於情感疾患，尤其 mood disorders；說思覺失調症最多較不適當。",
            "C": "抗精神病藥可能造成或惡化 catatonia-like 狀態，也需鑑別 NMS，敘述正確。",
            "D": "Echolalia 與 echopraxia 是 catatonia 可見症狀，敘述正確。",
        },
        "key_point": "Catatonia 不只見於 schizophrenia，mood disorders 是重要且常見原因。",
        "front": "Catatonia",
    },
    60: {
        "analysis": "雙相情緒障礙具高度遺傳性，同卵雙胞胎一致率通常遠高於 25%。家族史、鬱期較常見與鋰鹽治療濃度都是常見考點。",
        "options": {
            "A": "雙相家族史也會增加憂鬱症與其他 mood disorder 風險，敘述合理。",
            "B": "同卵雙胞胎雙相障礙一致率通常約 40-70% 範圍，25%過低，因此最不適當。",
            "C": "雙相病程中鬱期常比躁期更頻繁；只有躁期而無鬱期者為少數，敘述正確。",
            "D": "鋰鹽急性期治療濃度常抓約 0.6-1.2 mEq/L，需依病況與副作用調整。",
        },
        "key_point": "雙相障礙遺傳性高，同卵雙胞胎一致率明顯高於 25%。",
        "front": "雙相障礙遺傳",
    },
    61: {
        "analysis": "鋰鹽治療指數狹窄，毒性監測不能只靠臨床觀察，必須搭配血中鋰濃度、腎功能、電解質與甲狀腺功能等追蹤。",
        "options": {
            "A": "鋰鹽可造成腸胃症狀、顫抖、視力模糊等副作用，敘述正確。",
            "B": "嚴重鋰中毒可有意識改變、痙攣、心律不整或昏迷，敘述正確。",
            "C": "嚴重中毒、腎功能不良或神經症狀明顯時可用血液透析，敘述正確。",
            "D": "最有效監測不是單靠臨床觀察，而是定期測血中鋰濃度與相關檢驗，因此最不適當。",
        },
        "key_point": "鋰鹽需用血中濃度與腎功能等監測；嚴重中毒可血液透析。",
        "front": "鋰鹽中毒監測",
    },
    62: {
        "analysis": "病人有被害/被偷妄想、Capgras delusion、關係妄想與攻擊行為。診斷 schizophrenia 前需排除物質、藥物或身體疾病造成的精神病症狀。",
        "options": {
            "A": "強制住院依精神衛生法與危險性評估進行，不是只需丈夫同意即可。",
            "B": "被偷妄想可見於失智、妄想症、憂鬱或其他精神病，不只出現於 schizophrenia。",
            "C": "診斷 schizophrenia 前需排除 amphetamine 等物質或其他身體/藥物因素，最適當。",
            "D": "主要治療精神病症狀通常是抗精神病藥；benzodiazepine 可短期鎮靜但非首選核心治療。",
        },
        "key_point": "診斷 schizophrenia 前要排除物質、藥物與身體疾病造成的精神病。",
        "front": "思覺失調症診斷排除",
    },
    63: {
        "analysis": "安樂死分類常考主動與被動。撤除或不啟動無效維生治療屬被動式；由醫師在病人要求下給予措施直接造成死亡則屬主動式，不是被動式。",
        "options": {
            "A": "撤除維生系統可被歸在被動式安樂死或停止無效治療的討論範圍，敘述可接受。",
            "B": "在病人要求下以措施協助其死亡，若是主動施予致死行為，屬主動式而非被動式，因此最不適當。",
            "C": "主動式安樂死牽涉醫師角色、同意能力與生命倫理，爭議仍多。",
            "D": "憂鬱症會影響自主決策與死亡意願評估，是重要評估項目。",
        },
        "key_point": "被動式偏向不啟動或撤除維生治療；主動式是直接施予導致死亡的措施。",
        "front": "安樂死分類",
    },
    64: {
        "analysis": "失眠症可為獨立疾病，也可與身體、精神或藥物因素共病；並非一定能找到單一潛在疾病。診斷需看頻率、持續時間與日間功能影響。",
        "options": {
            "A": "白天嗜睡要評估睡眠呼吸障礙、睡眠不足或其他睡眠疾患，敘述正確。",
            "B": "每週至少 3 次、持續至少 3 個月且造成困擾/功能影響，符合慢性失眠症標準。",
            "C": "失眠不一定都是其他疾病導致，也可能為原發或與多因素互相影響，因此最不適當。",
            "D": "鎮靜安眠藥一般建議短期使用，避免依賴、耐受與跌倒等風險，敘述合理。",
        },
        "key_point": "慢性失眠症可獨立診斷；不是所有失眠都能找出單一潛在疾病。",
        "front": "失眠症診斷",
    },
    65: {
        "analysis": "Binge eating disorder 與 bulimia nervosa 都有反覆暴食，但 bulimia 有反覆代償行為且自我評價過度受體重體型影響；嗜食症沒有固定代償行為。",
        "options": {
            "A": "Fluoxetine 等 SSRI 可用於 bulimia nervosa，能減少暴食與清除行為，敘述正確。",
            "B": "Binge eating disorder 沒有反覆催吐、瀉劑等代償性減重行為，敘述正確。",
            "C": "嗜食症不像 anorexia 或 bulimia 那樣以追求纖瘦和代償行為為核心，敘述大致正確。",
            "D": "Bulimia nervosa 的自我評價會不當受到身材或體重影響；說不受影響最不適當。",
        },
        "key_point": "Bulimia 有代償行為且自我評價受體重體型影響；binge eating disorder 無反覆代償行為。",
        "front": "嗜食症 vs 暴食症",
    },
    66: {
        "analysis": "Medical food 可作為特定營養療法的一部分，但不能把 omega-3 說成主要靠 serotonin reuptake inhibition；這是 SSRI 的機轉，不是 omega-3。",
        "options": {
            "A": "藥物上市通常需要嚴格臨床試驗與法規審查，與 medical food 的規範重點不同，敘述可接受。",
            "B": "憂鬱症病因多因子，單一藥物療法可能不足，需要心理、社會與生活型態等整合，敘述合理。",
            "C": "SAMe 參與甲基化反應，與 monoamine 合成代謝相關，可被討論於憂鬱症輔助治療。",
            "D": "Omega-3 主要與細胞膜、發炎調節與神經傳導調節相關，不是血清素回收抑制作用，因此最不適當。",
        },
        "key_point": "Omega-3 不是 SSRI；不要把營養補充品機轉混同為 serotonin reuptake inhibition。",
        "front": "Medical food 與憂鬱",
    },
    67: {
        "analysis": "老年精神醫學中，自殺、晚發焦慮與睡眠呼吸障礙都重要。慮病症/疾病焦慮症並非主要高峰在 60 歲以上，常在較早成人期即出現。",
        "options": {
            "A": "老年人自殺完成率高，孤單、疾病、喪偶與憂鬱都是重要危險因子，敘述可接受。",
            "B": "慮病症發生高峰不是主要在 60 歲以上，說老年人口為主要高峰最不適當。",
            "C": "焦慮症多始於早年或中年，但老年也可首次發病，需排除身體疾病與藥物。",
            "D": "睡眠呼吸障礙隨年齡與共病增加而較常見，老年人風險較高。",
        },
        "key_point": "老年人可有晚發焦慮與睡眠呼吸障礙，但疾病焦慮症不是以 60 歲以上為主要高峰。",
        "front": "老年精神疾病",
    },
    68: {
        "analysis": "譫妄治療以找原因、矯正誘因、環境定向與安全照護為主。約束需短期、最低限制且有明確必要；長時間約束會惡化譫妄與併發症。",
        "options": {
            "A": "嚴重激躁、危及安全時可短期使用抗精神病藥控制行為症狀，敘述可接受。",
            "B": "Benzodiazepine 一般可能惡化譫妄，但在酒精/鎮靜劑戒斷或特定失眠情境可謹慎短期使用；相較下長時間約束更明顯不適當。",
            "C": "家人照片、時鐘、日夜節律與熟悉環境可幫助定向感，是非藥物處置。",
            "D": "長時間約束會增加受傷、壓瘡、焦躁與譫妄惡化，不能作為常規治療，因此最不適當。",
        },
        "key_point": "譫妄優先處理原因與環境定向；約束只能短期最低限制，不能長時間常規使用。",
        "front": "譫妄治療",
        "notes": ["BZD 在一般譫妄常會惡化症狀，但題目官方答案為長時間約束；若作細部教學可補充 BZD 只限戒斷等特定情境。"],
    },
    69: {
        "analysis": "Methadone 是長效 opioid agonist，用於海洛因成癮替代療法，可減少非法使用與戒斷。其長半衰期使每日一次口服給藥通常可維持效果。",
        "options": {
            "A": "Methadone 可有嗜睡等副作用，但說長期使用多數導致憂鬱或嗜睡過度概括。",
            "B": "替代療法主要為口服給藥，不是靜脈注射。",
            "C": "Methadone 本身仍會造成生理依賴，需醫療監測與逐步調整。",
            "D": "Methadone 作用時間長，穩定後常每日一次治療即可，最適當。",
        },
        "key_point": "Methadone 替代療法為長效口服 opioid agonist，穩定後通常每日一次。",
        "front": "Methadone 替代療法",
    },
    70: {
        "analysis": "BZD 與酒精都作用於 GABA 系統，戒斷可有焦慮、失眠、自律神經亢進，嚴重可抽搐。戒斷時間與半衰期相關，短效藥較快出現且較容易造成強化使用。",
        "options": {
            "A": "BZD 戒斷與酒精戒斷相似，可有焦慮、不悅、失眠、震顫甚至抽搐，最適當。",
            "B": "抽搐時間取決於藥物半衰期，短效 BZD 可在停藥後較早出現，不是多半第 10 天。",
            "C": "通常短效、高效價、起效快的 BZD 濫用與依賴風險較高，不是半衰期長者較高。",
            "D": "濫用性別差異不能作為核心正確敘述，且不如戒斷症狀考點穩定。",
        },
        "key_point": "BZD 戒斷像酒精戒斷；短效高效價藥較易有依賴與較早戒斷。",
        "front": "BZD 戒斷",
    },
    71: {
        "analysis": "ASD 的認知輪廓常見非語文或視覺空間能力相對優於口語理解；社交互動與 theory of mind 常有缺損，但不是完全沒有依附行為。",
        "options": {
            "A": "ASD 兒童可有依附行為，只是社交互動品質與互惠性異常；說完全缺乏過度絕對。",
            "B": "ASD 面對陌生人的不安不一定比同齡兒更顯著，這不是核心診斷特徵。",
            "C": "許多 ASD 患者視覺空間或非語文能力相對強於口語理解，敘述最適當。",
            "D": "Theory of mind 缺損是 ASD 社交認知的重要特徵，不能說並無缺損。",
        },
        "key_point": "ASD 常見視覺空間能力相對較佳、口語與 theory of mind 較弱。",
        "front": "ASD 認知特徵",
    },
    72: {
        "analysis": "ADHD 常用中樞神經刺激劑如 methylphenidate，主要抑制 dopamine 與 norepinephrine transporter，提升突觸間 DA/NE，不是 serotonin reuptake inhibitor。",
        "options": {
            "A": "Methylphenidate 不是 SSRI，而是增加 dopamine/norepinephrine 傳遞，因此最不適當。",
            "B": "刺激劑改善核心症狀後，可提升社交互動與衝動控制，敘述合理。",
            "C": "對不專注、過動與衝動三大核心症狀多數有效，是 ADHD 第一線治療之一。",
            "D": "常見副作用包括食慾下降、失眠、心跳血壓上升等，敘述正確。",
        },
        "key_point": "Methylphenidate 主要增加 dopamine/norepinephrine，不是 serotonin reuptake inhibitor。",
        "front": "ADHD stimulant 機轉",
    },
    73: {
        "analysis": "詐病與佯病都可能有意製造或誇大症狀；最大差異是動機。詐病有明確外在誘因，佯病主要是扮演病人角色的內在心理需求。",
        "options": {
            "A": "佯病確實是有意製造或偽裝症狀，這不是與詐病的最大區別。",
            "B": "佯病不等於完全沒有身體或精神疾病；核心是症狀欺瞞與內在動機。",
            "C": "維持 sick role 是佯病的典型動機，不是詐病。",
            "D": "詐病有外在利益，例如逃避法律、兵役、獲得金錢或藥物，是最大區別。",
        },
        "key_point": "Malingering 是外在利益；factitious disorder 是內在 sick role 需求。",
        "front": "詐病 vs 佯病",
    },
    74: {
        "analysis": "廣泛蜘蛛網膜下腔出血常由顱內動脈瘤破裂造成；PCommA aneurysm 是常見位置。此題依官方影像與答案判讀為右側 ICA-PCommA 交界動脈瘤。",
        "options": {
            "A": "右側 ICA 與 PCommA 交界動脈瘤符合官方影像判讀，是造成 SAH 的最可能原因。",
            "B": "左側 ICA-PCommA 動脈瘤也是常見位置，但與本題官方影像側別不符。",
            "C": "右側前大腦動脈瘤可造成 SAH，但不是本題影像指示的病灶。",
            "D": "左側前大腦動脈瘤同樣非本題官方影像所示位置。",
        },
        "key_point": "SAH 常見原因是囊狀動脈瘤破裂；影像題需依血管攝影判讀側別與位置。",
        "front": "SAH 動脈瘤位置",
        "notes": ["本題需參照原始血管攝影圖，已依官方答案 A 撰寫；若圖片標示不清建議人工複核。"],
    },
    75: {
        "analysis": "腦梗塞早期 CT 可正常，MRI DWI 對急性缺血最敏感；出血性轉化通常 CT 很容易看見急性血，但題目官方答案認為『CT 比 MRI 更容易偵測』過度絕對或不精確。",
        "options": {
            "A": "急性腦梗塞 12 小時內非顯影 CT 可能看不到明顯變化，敘述正確。",
            "B": "約 1-2 週可因血腦屏障破壞出現 contrast enhancement，敘述正確。",
            "C": "MRI 對缺血與部分出血變化很敏感；說 CT 比 MRI 更容易偵測梗塞後出血性轉化是錯誤或過度簡化，因此為答案。",
            "D": "DWI 異常可在急性期出現並持續一段時間，約至 1-2 週仍可見，敘述可接受。",
        },
        "key_point": "急性腦梗塞 MRI DWI 最敏感；早期 CT 可正常，影像偵測不要把 CT 絕對說成優於 MRI。",
        "front": "腦梗塞影像",
    },
    76: {
        "analysis": "AHT 是兒童虐待造成的腦傷，常見於嬰幼兒，可有硬腦膜下出血、視網膜出血與骨折等。日常溫和搖晃或膝上晃動不等同造成典型嬰兒搖晃症候群的暴力加減速傷害。",
        "options": {
            "A": "AHT 過去常稱 shaken baby syndrome，屬兒童虐待，敘述正確。",
            "B": "Retinal hemorrhages 是 AHT 重要診斷線索之一，需眼科評估。",
            "C": "AHT 常見於未滿 3 歲，尤其嬰兒，敘述正確。",
            "D": "一般膝上晃動或拋起不應與造成 AHT 的暴力搖晃混為一談；此敘述過度誇大，故錯誤。",
        },
        "key_point": "AHT 代表暴力加減速或撞擊造成的虐待性腦傷，不是一般溫和玩耍動作。",
        "front": "Abusive head trauma",
    },
    77: {
        "analysis": "長期安非他命使用後停止可出現疲倦、全身無力、情緒低落、睡眠增加或食慾改變；生命徵象不一定有明顯自律神經亢進。",
        "options": {
            "A": "Amphetamine 戒斷常以憂鬱、疲倦、無力、嗜睡或睡眠障礙為主，與題幹的無力和情緒低落相符。",
            "B": "Heroin 戒斷常見流淚流鼻水、腹瀉、肌肉痛、瞳孔放大與自律神經症狀，不是本題型態。",
            "C": "Alcohol 戒斷常有顫抖、焦慮、心跳血壓上升、抽搐或譫妄，生命徵象通常較亢進。",
            "D": "BZD 戒斷可焦慮、失眠、顫抖、抽搐，與本題情緒低落無力為主不符。",
        },
        "key_point": "Stimulant 戒斷常是疲倦、憂鬱、嗜睡與無力；酒精/BZD 戒斷較怕抽搐與自律神經亢進。",
        "front": "安非他命戒斷",
    },
    78: {
        "analysis": "壞死性筋膜炎是外科急症，治療核心是早期廣泛清創、抗生素與支持療法。高壓氧可作輔助但不能說有極佳效果或取代手術。",
        "options": {
            "A": "丹毒多由 group A Streptococcus 引起，界線清楚、表淺，敘述正確。",
            "B": "健康成人局部蜂窩性組織炎且無菌血症或重症表現，可門診口服抗生素治療，敘述正確。",
            "C": "高壓氧對部分厭氧感染可能作輔助，但證據與可近性有限，不能視為極佳或主要治療，因此錯誤。",
            "D": "疼痛程度與皮膚表現不相稱是壞死性筋膜炎警訊，需高度懷疑。",
        },
        "key_point": "壞死性筋膜炎重點是 pain out of proportion 與立即外科清創；高壓氧只是可能輔助。",
        "front": "壞死性筋膜炎",
    },
    79: {
        "analysis": "產前遺傳檢測異常後，遺傳諮詢應提供確認檢查、疾病嚴重度、治療、預後與社會資源，尊重父母自主決策；不應單憑罹病就積極勸中止妊娠。",
        "options": {
            "A": "即使胎兒確定罹患遺傳疾病，也應進行非指令式諮詢與尊重決策，不能一律積極勸中止懷孕，因此最不適當。",
            "B": "產前篩檢或檢測結果需視方法確認，必要時以其他檢驗確認後再決策，敘述正確。",
            "C": "若疾病影響較輕或可治療，繼續懷孕是可被討論與尊重的選項。",
            "D": "重大遺傳疾病諮詢需包含治療、預後、照護與社會福利資源，敘述正確。",
        },
        "key_point": "遺傳諮詢應非指令式、重確認與自主決策，不應一律勸終止妊娠。",
        "front": "產前遺傳諮詢",
    },
    80: {
        "analysis": "HIV 病人不願告知懷孕性伴侶時，醫師需先鼓勵告知與輔導；若第三方有重大、可預防傷害風險，法律與公共衛生機制可允許或要求有限揭露，尤其保護伴侶與胎兒。",
        "options": {
            "A": "在特定且有限情況下，為避免重大傷害而揭露並不必然違反醫學倫理，敘述正確。",
            "B": "保密義務不是絕對；若只提醒患者而完全不能通知高風險第三方，忽略公共衛生與防止傷害原則，因此最不適當。",
            "C": "若保密會造成第三方嚴重傷害，醫師可依倫理與法律進行必要且最小揭露。",
            "D": "HIV 屬公共衛生通報與伴侶通知可介入的疾病，衛生主管機關可採直接或匿名通知方式。",
        },
        "key_point": "醫療保密有例外；HIV 伴侶通知可在防止第三方重大傷害與公共衛生框架下進行。",
        "front": "HIV 保密與伴侶通知",
    },
}


def main():
    source = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    questions = {q["question_number"]: q for q in source["questions"]}
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for start in range(1, 81, 10):
        end = start + 9
        updates = []
        for number in range(start, end + 1):
            item = ITEMS[number]
            q = questions[number]
            key_point = item["key_point"]
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": number,
                    "explanation": make_explanation(item["analysis"], item["options"], key_point),
                    "key_point": key_point,
                    "flashcard_front": item["front"],
                    "flashcard_back": key_point,
                    "flashcard_summary": f"{item['front']}：{key_point}",
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
        out_path = OUT_DIR / f"q{start:03d}-q{end:03d}.json"
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
