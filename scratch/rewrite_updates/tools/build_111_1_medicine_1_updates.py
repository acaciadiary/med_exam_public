import json
from pathlib import Path


SOURCE_FILE = "public/data/exams/111-1/medicine-1.json"
DATASET_ID = "111-1_medicine-1"
OUT_DIR = Path("scratch/rewrite_updates/111-1_medicine-1")
GENERATED_AT = "2026-07-19T00:00:00+08:00"


ENTRIES = {
    1: {
        "stem": "題目問哪一個腦神經核的軸突會先在腦幹內交叉到對側才離開。這是滑車神經的經典解剖特徵：CN IV 神經核位於中腦下丘水平，纖維在上髓帆交叉後由腦幹背側出腦。",
        "key": "滑車神經是唯一在腦幹內交叉、且由腦幹背側離開的腦神經。",
        "reasons": {
            "A": "動眼神經核的纖維主要從同側中腦腹側離開，並不先在腦幹內交叉，因此不符合題目所問的出腦路徑。",
            "B": "滑車神經核發出的纖維會在腦幹內交叉到對側，再從背側離開腦幹；這正是本題要考的唯一例外。",
            "C": "外旋神經核位於橋腦，纖維從橋延溝附近離開，沒有滑車神經那種先交叉再出腦的特徵。",
            "D": "舌下神經核位於延腦，纖維由橄欖與錐體之間出腦，路徑不會先在腦幹內交叉。",
        },
    },
    2: {
        "stem": "苔狀纖維進入小腦後，主要終止於顆粒層，與顆粒細胞形成突觸；顆粒細胞再經平行纖維影響蒲金氏細胞。",
        "key": "小腦 mossy fiber 主要和顆粒層的顆粒細胞突觸；climbing fiber 則直接強烈作用於蒲金氏細胞。",
        "reasons": {
            "A": "分子層含平行纖維與蒲金氏細胞樹突，是顆粒細胞輸出影響蒲金氏細胞的位置，不是苔狀纖維主要形成突觸的層次。",
            "B": "蒲金氏細胞層放置蒲金氏細胞胞體；苔狀纖維不以此層作為主要突觸目標，直接強烈接觸蒲金氏細胞的是 climbing fiber。",
            "C": "顆粒層含顆粒細胞與小腦小球，苔狀纖維主要在此與顆粒細胞樹突形成突觸，所以是正確答案。",
            "D": "把分子層與蒲金氏細胞層合併仍漏掉真正主要位置顆粒層，因此不符合 mossy fiber 的典型終止區。",
        },
    },
    3: {
        "stem": "兩眼共同向外側注視屬於隨意眼球運動控制，皮質主要由額葉眼動區啟動，再透過腦幹凝視中樞協調雙眼。",
        "key": "Frontal eye field 控制隨意性共軛凝視，病灶常使眼睛偏向病灶側、看向對側能力下降。",
        "reasons": {
            "A": "主要運動區控制對側身體骨骼肌的隨意動作，不是兩眼共軛凝視的專門皮質區。",
            "B": "主要視覺區負責接收與處理初級視覺訊息，並不主導眼球外側注視動作。",
            "C": "運動輔助區偏重動作計畫與雙側協調，並非控制 lateral gaze 的主要皮質定位。",
            "D": "額葉眼動區負責啟動隨意性共軛眼球運動，與外側注視最直接相關。",
        },
    },
    4: {
        "stem": "題目描述同側伸肌收縮、屈肌鬆弛，是維持姿勢與抗重力伸肌張力的前庭脊髓徑功能。",
        "key": "外側前庭脊髓徑促進同側軀幹與近端肢體伸肌，幫助姿勢與平衡。",
        "reasons": {
            "A": "外側前庭脊髓徑由外側前庭核下行，主要增強同側伸肌與抗重力肌張力，正符合題目描述。",
            "B": "網狀脊髓徑會調節姿勢與肌張力，但外側網狀脊髓徑不是題目所指典型促進同側伸肌的路徑。",
            "C": "紅核脊髓徑較偏向促進上肢屈肌活動，與伸肌收縮、屈肌鬆弛的描述相反。",
            "D": "外側皮質脊髓徑主要控制遠端肢體精細隨意動作，不是抗重力伸肌反射性促進的主要徑路。",
        },
    },
    5: {
        "stem": "本體感覺需要快速、精準傳遞肌梭與關節位置訊息，因此多由大直徑、有髓鞘纖維承擔，並經背根內側進入後索系統。",
        "key": "本體感覺與精細觸覺多走大直徑纖維，從背根內側進入脊髓；痛溫覺小纖維較偏外側。",
        "reasons": {
            "A": "大直徑纖維適合快速傳導本體感覺，且背根內側分支是這類纖維進入脊髓的典型位置。",
            "B": "雖然本體感覺纖維較粗，但背根外側較偏痛覺、溫覺等小纖維進入區，因此位置不對。",
            "C": "本體感覺不是以小直徑纖維為主；小纖維傳遞較慢，常見於痛溫覺或自主相關訊息。",
            "D": "小直徑加背根外側比較符合痛溫覺路徑，不符合 proprioception 的高速度傳導需求。",
        },
    },
    6: {
        "stem": "題目問哪一個不是間腦構造。間腦包含丘腦、下視丘、上丘腦與松果體等；豆狀核屬於大腦基底核。",
        "key": "間腦包括 thalamus、hypothalamus、epithalamus；lentiform nucleus 是 basal ganglia。",
        "reasons": {
            "A": "丘腦是間腦最大組成之一，負責多數感覺訊息中繼，因此不能選為例外。",
            "B": "松果體屬於上丘腦，也歸在間腦範圍內，因此不是本題要找的非間腦構造。",
            "C": "豆狀核由殼核與蒼白球組成，是基底核的一部分，不屬於間腦，所以是題目所問的例外。",
            "D": "下視丘位於間腦腹側，參與自主神經與內分泌調節，明確屬於間腦。",
        },
    },
    7: {
        "stem": "眼神經是三叉神經第一分支，功能以一般體感覺為主；題目問最不恰當，特殊感覺這個分類不適用。",
        "key": "Ophthalmic nerve 是 CN V1，屬一般體感覺，接收眼眶、角膜、前額與部分鼻部感覺。",
        "reasons": {
            "A": "眼神經不是視覺、嗅覺、味覺或聽平衡等特殊感覺神經；它是一般體感覺分支，所以此敘述最不恰當。",
            "B": "CN V1 傳遞一般體感覺，包括痛、溫、觸與角膜感覺，這是正確分類。",
            "C": "眼眶結構、角膜與眼周感覺可由眼神經分支傳入，因此這個描述合理。",
            "D": "前額、上眼瞼與鼻背等部分顏面感覺屬 CN V1 分布，並非錯誤敘述。",
        },
    },
    8: {
        "stem": "鼻淚管把淚液從淚囊導入鼻腔，開口在下鼻道；臨床上哭泣時流鼻水也來自這條通路。",
        "key": "Nasolacrimal duct/canal 連通到 inferior meatus。",
        "reasons": {
            "A": "最上鼻道位於上鼻甲上方，和鼻淚管開口無關。",
            "B": "上鼻道主要接收後篩竇開口，不是淚液進入鼻腔的位置。",
            "C": "中鼻道接收額竇、上頷竇與前中篩竇等開口，但不是鼻淚管終點。",
            "D": "鼻淚管通向下鼻道，位於下鼻甲下方，因此此選項正確。",
        },
    },
    9: {
        "stem": "鼓索神經從顏面神經分出，穿過中耳後經岩鼓裂進入顳下窩，之後加入舌神經。",
        "key": "Chorda tympani 經 petrotympanic fissure 離開中耳，攜帶前舌 2/3 味覺與副交感纖維。",
        "reasons": {
            "A": "岩鼓裂是鼓索神經離開中耳、進入顳下窩並加入舌神經的通道。",
            "B": "莖乳突孔是顏面神經主幹離開顱骨的位置，不是鼓索神經離開中耳進入顳下窩的裂隙。",
            "C": "乳突孔主要與導靜脈等構造相關，並非鼓索神經的典型路徑。",
            "D": "咽鼓室管連通中耳與鼻咽，用於壓力平衡，不是鼓索神經離開中耳的孔道。",
        },
    },
    10: {
        "stem": "頸動脈鞘內容物包含頸總動脈或內頸動脈、內頸靜脈與迷走神經；舌咽神經不在鞘內。",
        "key": "Carotid sheath 三大內容物是 common/internal carotid artery、internal jugular vein、vagus nerve。",
        "reasons": {
            "A": "頸總動脈位於頸動脈鞘內，向上分叉為內外頸動脈。",
            "B": "舌咽神經雖穿越頸部深處，但不是頸動脈鞘的標準內容物，因此是本題答案。",
            "C": "內頸動脈在頸動脈鞘內向上行進，是鞘內重要血管。",
            "D": "迷走神經位於頸動脈鞘內，通常在動脈與內頸靜脈之間偏後方。",
        },
    },
    11: {
        "stem": "題目問同時參與眼眶、鼻腔與口腔形成的骨。上頷骨構成眼眶底、鼻腔外側壁與硬顎前大部。",
        "key": "Maxilla 同時參與 orbit、nasal cavity、oral cavity 的骨性邊界。",
        "reasons": {
            "A": "篩骨參與鼻腔與眼眶內側壁，但不形成口腔硬顎的主要部分。",
            "B": "淚骨主要位於眼眶內側壁並與淚囊窩相關，沒有同時形成口腔。",
            "C": "顴骨參與眼眶外側壁與顴弓，但與鼻腔、口腔形成關係有限。",
            "D": "上頷骨形成眼眶底、鼻腔外側壁與硬顎，是三個空間共同相關的骨。",
        },
    },
    12: {
        "stem": "會厭附近黏膜屬於喉入口周邊區域，一般感覺由迷走神經的內喉神經負責。",
        "key": "Internal laryngeal nerve 供應會厭、喉入口以上喉黏膜的感覺。",
        "reasons": {
            "A": "舌神經負責前舌一般感覺與口底部分感覺，不是會厭附近黏膜的主要支配。",
            "B": "舌咽神經供應後舌 1/3、口咽與咽反射傳入，但會厭喉入口區更典型由內喉神經。",
            "C": "鼓索神經攜帶前舌 2/3 味覺與唾液腺副交感纖維，不支配會厭附近一般感覺。",
            "D": "內喉神經是上喉神經內支，負責會厭與聲門上喉黏膜感覺，因此正確。",
        },
    },
    13: {
        "stem": "蝶骨棘是蝶骨大翼後方的骨性突起，解剖定位上緊鄰棘孔，棘孔內有中腦膜動脈通過。",
        "key": "Spine of sphenoid 最靠近 foramen spinosum。",
        "reasons": {
            "A": "盲孔位於額骨與篩骨附近的前顱窩正中，和蝶骨棘距離較遠。",
            "B": "腭大孔位於硬顎後外側，屬口腔顎部區域，不是蝶骨棘旁孔洞。",
            "C": "棘孔就在蝶骨棘附近，是本題最直接的空間關係。",
            "D": "莖乳突孔位於顳骨，為顏面神經出顱處，與蝶骨棘不是最近關係。",
        },
    },
    14: {
        "stem": "三叉神經第三分支 V3 供應下頷區域的一般感覺，包括頰黏膜；硬顎與鼻腔多偏 V2，下眼瞼也屬 V2。",
        "key": "CN V3 負責 mandibular territory，包含下頷牙齦、下唇與口腔內頰黏膜部分感覺。",
        "reasons": {
            "A": "硬顎主要由上頷神經 V2 的腭神經分支供應，不是 V3 的典型區域。",
            "B": "鼻腔內感覺大多由 V1、V2 分支負責，與第三分支的下頷區域不同。",
            "C": "下眼瞼感覺主要屬 V2 的眶下神經分布，不屬於 V3。",
            "D": "口腔內頰黏膜可由 V3 的頰神經傳遞一般感覺，所以此選項正確。",
        },
    },
    15: {
        "stem": "心臟缺血痛屬內臟痛，主要隨交感神經傳入脊髓 T1-T5 節段，造成左胸、左上肢等牽涉痛。",
        "key": "Cardiac ischemic pain afferents travel with sympathetic fibers to upper thoracic spinal cord。",
        "reasons": {
            "A": "膈神經傳遞橫膈與心包部分體感覺，較常造成肩部牽涉痛，不是心肌缺血痛的主要路徑。",
            "B": "迷走神經雖參與心臟副交感與部分內臟傳入，但典型缺血痛主要沿交感傳入。",
            "C": "交感神經系統攜帶心肌缺血痛覺傳入至上胸髓節段，是本題正確答案。",
            "D": "左喉返神經支配喉部肌肉與感覺，與心肌缺血痛覺傳入無關。",
        },
    },
    16: {
        "stem": "胸交感幹的上胸節後纖維可直接形成心肺內臟神經到胸腔臟器；下胸節多送出節前纖維成內臟神經往腹部節前突觸。",
        "key": "上胸交感節可發出節後心肺內臟纖維；下胸內臟神經多為節前纖維往腹腔神經節。",
        "reasons": {
            "A": "胸交感節不只支配胸腹腔臟器，也經交通支影響體壁血管、汗腺與立毛肌。",
            "B": "胸脊神經與交感幹之間有白交通支與灰交通支，說僅有灰交通支不完整。",
            "C": "上五個胸交感節常發出節後交感纖維至心臟、肺等胸腔器官，描述最恰當。",
            "D": "下七個胸節往腹腔的內臟神經多為節前纖維，通常在腹腔神經節才突觸，不是節後纖維直接支配。",
        },
    },
    17: {
        "stem": "冠狀動脈優勢由後室間支 posterior interventricular artery 來源決定；來自左冠狀系統即左優勢。",
        "key": "Coronary dominance 看 PDA/後室間支來源；左優勢表示後室間支由左冠狀動脈系統供血。",
        "reasons": {
            "A": "前室間支通常來自左冠狀動脈的 LAD，這是一般解剖，不是判定左優勢的標準。",
            "B": "前室間支來自右冠狀動脈並非常態，也不是 dominance 的定義。",
            "C": "後室間支若由左冠狀動脈系統供血，即稱左側優勢冠狀動脈。",
            "D": "後室間支由右冠狀動脈供血是右優勢，不是左優勢。",
        },
    },
    18: {
        "stem": "咳血多來自高壓的支氣管循環，而不是低壓肺循環；支氣管動脈供應氣道與支氣管壁。",
        "key": "Hemoptysis 最常來自 bronchial arteries，因其屬體循環高壓血管。",
        "reasons": {
            "A": "肺動脈系統壓力較低，雖可在特定疾病出血，但不是咳血最常見來源。",
            "B": "肺靜脈主要回流氧合血，並非咳血最典型出血血管系統。",
            "C": "支氣管動脈屬體循環、高壓且供應氣道，咳血最常由此系統出血。",
            "D": "支氣管靜脈是回流通道，臨床咳血來源仍以支氣管動脈較典型。",
        },
    },
    19: {
        "stem": "主動脈裂口位於 T12，通過主動脈、胸管及奇靜脈系統；食道通過 T10 食道裂孔。",
        "key": "Aortic hiatus 通過 aorta、thoracic duct、azygos vein；esophageal hiatus 通過 esophagus 與迷走幹。",
        "reasons": {
            "A": "胸管會經橫膈主動脈裂口由腹腔進入胸腔，因此是正確答案。",
            "B": "食道通過食道裂孔，不是主動脈裂口。",
            "C": "內胸動脈位於胸前壁，分支往腹壁延續，並不經主動脈裂口穿越橫膈。",
            "D": "下膈靜脈在橫膈附近回流，並非主動脈裂口的標準通過內容。",
        },
    },
    20: {
        "stem": "性腺靜脈左右回流不對稱：右性腺靜脈入下腔靜脈，左性腺靜脈入左腎靜脈。",
        "key": "Left gonadal vein drains into left renal vein；right gonadal vein drains into IVC。",
        "reasons": {
            "A": "直接匯入下腔靜脈是右性腺靜脈的典型路徑，左側不是如此。",
            "B": "左性腺靜脈先匯入左腎靜脈，再回到下腔靜脈，因此此選項正確。",
            "C": "左總髂靜脈接收下肢與骨盆回流，不是左性腺靜脈的直接匯入點。",
            "D": "下腸繫膜靜脈屬門脈系統回流，與性腺靜脈直接回流無關。",
        },
    },
    21: {
        "stem": "精索內容包括輸精管、睪丸血管、蔓狀靜脈叢與生殖股神經生殖支；髂腹股溝神經通過腹股溝管但位在精索外。",
        "key": "Ilioinguinal nerve runs in inguinal canal but is not inside spermatic cord。",
        "reasons": {
            "A": "髂腹股溝神經可伴隨通過腹股溝管表層，但不被精索筋膜包在精索內，所以是本題答案。",
            "B": "生殖股神經的生殖支屬精索內容物，支配提睪肌等構造。",
            "C": "輸精管是精索核心內容物之一，從副睪往骨盆走行。",
            "D": "蔓狀靜脈叢包繞睪丸動脈並位於精索內，與睪丸溫度調節相關。",
        },
    },
    22: {
        "stem": "網膜孔前方是肝十二指腸韌帶內容物，後方是下腔靜脈；總膽管在孔的前方右側，不在後方。",
        "key": "Omental foramen：前方為 portal triad，後方為 IVC，上方肝臟，下方十二指腸第一部。",
        "reasons": {
            "A": "總膽管屬 portal triad，位在網膜孔前方右側；說在後方是錯誤關係，因此選 A。",
            "B": "肝門靜脈位於肝十二指腸韌帶內，屬網膜孔前方內容之一，此敘述正確。",
            "C": "網膜孔上方與肝臟尾狀葉附近相關，位置描述可接受。",
            "D": "十二指腸第一部構成網膜孔下界，故在其下方的說法正確。",
        },
    },
    23: {
        "stem": "直腸由骨盆底肌群支持，提肛肌與肛尾韌帶有助維持其位置與肛直腸角；題目問正確敘述。",
        "key": "Levator ani 尤其 puborectalis 維持 anorectal angle，直腸也有橫襞且部分受腹膜覆蓋。",
        "reasons": {
            "A": "直腸黏膜有橫襞，不是完全平滑無皺褶。",
            "B": "提肛肌與肛尾韌帶協助支持直腸與骨盆底關係，敘述正確。",
            "C": "腹膜會覆蓋直腸上段前面與側面、中段前面；不是只到乙狀結腸就停止。",
            "D": "肛直腸彎曲主要由恥骨直腸肌維持，不是 U 字型尾骨肌造成。",
        },
    },
    24: {
        "stem": "陰莖腳固定於坐骨恥骨支，表面由坐骨海綿體肌覆蓋；球海綿體肌則覆蓋陰莖球。",
        "key": "Ischiocavernosus covers crus of penis/clitoris；bulbospongiosus covers bulb。",
        "reasons": {
            "A": "坐骨海綿體肌覆蓋陰莖腳並協助維持勃起壓力，正是題目所問。",
            "B": "球海綿體肌主要覆蓋陰莖球與尿道海綿體近端，不是陰莖腳。",
            "C": "會陰淺橫肌穩定會陰體，並不覆蓋陰莖腳。",
            "D": "會陰深橫肌位於深會陰隙，功能與尿生殖膈支撐較相關，並非覆蓋陰莖腳的肌肉。",
        },
    },
    25: {
        "stem": "陰道上部與子宮頸的內臟痛覺常隨副交感路徑經骨盆內臟神經進入 S2-S4；陰道下部才偏陰部神經。",
        "key": "Cervix 與上陰道痛覺主要經 pelvic splanchnic nerves；下陰道體痛經 pudendal nerve。",
        "reasons": {
            "A": "陰部神經主要負責會陰與陰道下部體感覺，並非子宮頸與上陰道主要痛覺路徑。",
            "B": "下腹神經傳遞部分骨盆內臟交感與痛覺，但子宮頸、上陰道痛覺在本題以骨盆內臟神經為主。",
            "C": "骨盆內臟神經來自 S2-S4，傳遞子宮頸與陰道上部相關內臟痛覺，是正確答案。",
            "D": "腰內臟神經偏上腹與骨盆交感傳入，並非此區最典型痛覺傳導。",
        },
    },
    26: {
        "stem": "女性深會陰隙含外尿道括約肌、尿道與陰道的一部分；前庭球位於淺會陰隙。",
        "key": "Bulb of vestibule is in superficial perineal pouch, not deep perineal pouch。",
        "reasons": {
            "A": "前庭球屬女性淺會陰隙勃起組織，不在深會陰隙，因此是本題答案。",
            "B": "部分陰道穿過深會陰隙附近，可列為女性深會陰隙相關內容。",
            "C": "部分尿道位於深會陰隙並受外尿道括約肌環繞。",
            "D": "外尿道括約肌是深會陰隙的重要肌肉內容物。",
        },
    },
    27: {
        "stem": "棘上肌啟動肩外展前 15 度，之後三角肌成為主要外展肌；因此它是協助三角肌外展上臂的肌肉。",
        "key": "Supraspinatus initiates abduction and stabilizes humeral head。",
        "reasons": {
            "A": "棘上肌可啟動上臂外展並穩定肱骨頭，和三角肌共同完成肩外展。",
            "B": "棘下肌主要使肩關節外旋，不是外展的主要協助肌。",
            "C": "大圓肌負責內收、內旋與伸展肱骨，功能方向與外展不同。",
            "D": "小圓肌主要外旋肱骨，雖屬旋轉袖，卻不是協助三角肌外展的重點肌。",
        },
    },
    28: {
        "stem": "大腿闊筋膜附著於髂嵴、腹股溝韌帶、恥骨與坐骨等下肢近端骨性結構；薦棘韌帶屬骨盆後方韌帶，不是其附著點。",
        "key": "Fascia lata attaches to iliac crest、inguinal ligament、pubis、ischial tuberosity and sacrum/coccyx region, not sacrospinous ligament。",
        "reasons": {
            "A": "腹股溝韌帶與闊筋膜近端連續，是相關附著構造。",
            "B": "薦棘韌帶位於骨盆後外側，連接薦骨與坐骨棘，不是大腿闊筋膜典型附著點。",
            "C": "髂嵴是闊筋膜重要近端附著位置。",
            "D": "坐骨粗隆與近端大腿筋膜、後側肌群筋膜關係密切，屬相關附著區域。",
        },
    },
    29: {
        "stem": "題目原本依賴圖中黑色皮膚區域判斷。依官方答案，該區域對應尺神經皮枝分布，常見於小指與無名指尺側的手部感覺區。",
        "key": "尺神經供應小指、無名指尺側與手掌/手背尺側皮膚感覺；本題需參照原圖判讀。",
        "reasons": {
            "A": "官方答案為尺神經，通常代表黑色區域落在手部尺側、小指或無名指尺側感覺分布。",
            "B": "橈神經較典型支配手背橈側、第一背側指間隙與上肢後側皮膚，和官方標示區域不同。",
            "C": "正中神經主要供應橈側手掌與橈側三又二分之一指掌側感覺，不是官方圖示所對應的神經。",
            "D": "肌皮神經終末為外側前臂皮神經，供應前臂外側感覺，不是手部尺側皮膚區域。",
        },
    },
    30: {
        "stem": "乳房尤其外上象限淋巴主要先流向腋窩前群，也稱胸肌淋巴結，之後再到中央與尖群。",
        "key": "Pectoral/anterior axillary nodes receive most breast lymph, especially lateral breast。",
        "reasons": {
            "A": "中央淋巴結常接收前、後、外側群的二級回流，但不是乳房外上側最主要直接第一站。",
            "B": "前淋巴結又稱胸肌淋巴結，直接接收乳房多數淋巴，特別是外側與外上象限。",
            "C": "外側淋巴結主要接收上肢淋巴，並非乳房淋巴的主要直接收集站。",
            "D": "後淋巴結主要接收肩胛背側與胸背壁淋巴，不是乳房外上側的主要直接回流。",
        },
    },
    31: {
        "stem": "膕靜脈阻塞會影響匯入或流經膕靜脈的深靜脈與小隱靜脈；大隱靜脈在內踝前方上行並匯入股靜脈，不經膕窩匯入膕靜脈。",
        "key": "Great saphenous vein drains to femoral vein, while small saphenous drains to popliteal vein。",
        "reasons": {
            "A": "大隱靜脈屬表淺靜脈，直接匯入股靜脈，血流量最不會因膕靜脈血栓而下降。",
            "B": "小隱靜脈通常在膕窩匯入膕靜脈，因此膕靜脈血栓會影響其回流。",
            "C": "脛後靜脈屬小腿深靜脈，向上形成膕靜脈，膕靜脈阻塞會使其回流受阻。",
            "D": "股靜脈接收膕靜脈延續而來的深靜脈血流，上游阻塞可能減少其來自小腿的血流。",
        },
    },
    32: {
        "stem": "軸旁中胚層會分節形成體節；脊索來自軸中胚層，體腔與側板中胚層相關，原條是胚盤形成構造。",
        "key": "Paraxial mesoderm gives rise to somites, which form sclerotome、myotome、dermatome。",
        "reasons": {
            "A": "脊索屬中線軸性結構，來自脊索突與軸中胚層，不是軸旁中胚層的典型衍生物。",
            "B": "體節由軸旁中胚層分節形成，之後分化為椎骨、骨骼肌與真皮等組織。",
            "C": "體腔主要與側板中胚層分裂形成的腔隙相關，不是軸旁中胚層直接衍生。",
            "D": "原條是 gastrulation 時期的胚盤結構，用於細胞內移形成三胚層，不是軸旁中胚層產物。",
        },
    },
    33: {
        "stem": "呼吸道上皮與腺體皆源自前腸內胚層；軟骨、平滑肌與結締組織來自周圍臟層中胚層間葉。題目問錯誤敘述。",
        "key": "Tracheal epithelium and glands are endodermal; cartilage and smooth muscle are splanchnic mesenchyme。",
        "reasons": {
            "A": "氣管內襯上皮來自前腸內胚層，這是正確敘述。",
            "B": "氣管軟骨由周圍臟層間葉組織分化而來，屬正確胚層來源。",
            "C": "氣管腺體和內襯上皮同樣源自前腸內胚層，不是中胚層；因此此項錯誤。",
            "D": "氣管平滑肌源於臟層間葉組織，與軟骨、結締組織同源。",
        },
    },
    34: {
        "stem": "中腎管又稱 Wolffian duct，在男性形成副睪管、輸精管、精囊與射精管等導管系統。",
        "key": "Mesonephric duct derivatives include epididymis、ductus deferens、seminal vesicle、ejaculatory duct。",
        "reasons": {
            "A": "細精管來自性腺索，而非中腎管。",
            "B": "睪丸網與睪丸內導管系統來源不同，不是中腎管的典型衍生物。",
            "C": "射精管由中腎管相關的輸精管末端與精囊管形成，屬 Wolffian duct 衍生物。",
            "D": "睪丸附件常視為中腎旁管殘餘，不是中腎管典型男性導管產物。",
        },
    },
    35: {
        "stem": "動脈導管由左第六咽弓動脈遠端保留形成，出生後功能性關閉成動脈韌帶。",
        "key": "Ductus arteriosus derives from distal left sixth aortic arch。",
        "reasons": {
            "A": "左側第六動脈弓遠端形成動脈導管，是正確答案。",
            "B": "第五動脈弓通常退化或不發育，並非動脈導管來源。",
            "C": "右側第五動脈弓不是動脈導管來源，也通常不作為主要永久構造。",
            "D": "左側第四動脈弓形成主動脈弓的一部分，不形成動脈導管。",
        },
    },
    36: {
        "stem": "四肢發育時，上肢外側旋轉約 90 度，下肢則內側旋轉約 90 度；題目問錯誤敘述。",
        "key": "Upper limb rotates laterally; lower limb rotates medially during development。",
        "reasons": {
            "A": "肢芽約第四週末從腹外側體壁出現，屬正確發育時序。",
            "B": "頂外胚層嵴負責維持肢芽遠端生長與近遠端軸發育，敘述正確。",
            "C": "下肢芽比上肢芽稍晚出現，通常晚一到二天，敘述合理。",
            "D": "上肢與下肢旋轉方向不同；上肢外旋、下肢內旋，因此說兩者都朝外側旋轉是錯的。",
        },
    },
    37: {
        "stem": "纖毛的軸絲以微管構成，典型為 9+2 或 9+0 排列；微絨毛與靜纖毛主要以肌動蛋白為骨架。",
        "key": "Cilia are microtubule-based; microvilli and stereocilia are actin-based。",
        "reasons": {
            "A": "紋狀緣微絨毛的核心是 actin filament，不是 microtubule。",
            "B": "刷狀緣微絨毛同樣以肌動蛋白束支撐，和纖毛不同。",
            "C": "靜纖毛名稱雖有 cilia，但本質是長微絨毛，以 actin 為主。",
            "D": "纖毛內部軸絲由微管構成，因此是本題正確答案。",
        },
    },
    38: {
        "stem": "頂泌分泌時細胞頂端胞質與細胞膜一起脫落包覆分泌物，所以釋出後仍帶有細胞膜成分。",
        "key": "Apocrine secretion releases apical cytoplasm with membrane; merocrine exocytoses contents only。",
        "reasons": {
            "A": "全泌腺是整個細胞崩解成分泌物，並非分泌物外仍以細胞膜包覆的典型描述。",
            "B": "局泌腺以胞吐作用釋放分泌物，細胞膜不包著分泌物一起離開。",
            "C": "頂泌腺釋放細胞頂端部分，分泌物帶有細胞膜包覆，符合題目敘述。",
            "D": "內分泌腺將分泌物釋入血液或組織液，分類重點不是膜包覆的頂端斷裂。",
        },
    },
    39: {
        "stem": "骨細胞由骨母細胞埋入骨基質後形成，壽命可很長；蝕骨細胞是單核球巨噬細胞系統融合形成，壽命較短。",
        "key": "Osteocyte lives longest; osteoclast is multinucleated and relatively short-lived。",
        "reasons": {
            "A": "蝕骨細胞不是由骨生成細胞分化，而是由單核球/巨噬細胞系統融合而來。",
            "B": "骨細胞埋在骨陷窩中可長期維持骨基質；蝕骨細胞壽命較短，敘述正確。",
            "C": "骨母細胞、骨細胞、蝕骨細胞的數量比較不是此題標準判斷重點，且骨細胞通常數量很多。",
            "D": "蝕骨細胞為多核巨細胞，不是單核細胞。",
        },
    },
    40: {
        "stem": "中樞神經系統缺乏周邊神經那種 endoneurium 與 Schwann cell 基底層包覆；無髓鞘軸突也在神經膠細胞環境中走行。",
        "key": "CNS axons lack connective tissue sheaths and Schwann-cell basal lamina。",
        "reasons": {
            "A": "CNS 無髓鞘軸突可與神經膠細胞突起接觸，但不是被 Schwann 細胞式包埋作為本題最精準答案。",
            "B": "支持細胞包覆與基底層是 PNS 無髓鞘纖維較典型的說法，CNS 不用這樣描述。",
            "C": "基底層是 Schwann cell 周邊神經環境常見特徵，中樞無髓鞘軸突沒有此包覆。",
            "D": "中樞神經系統內沒有周邊神經的結締組織鞘，因此此敘述正確。",
        },
    },
    41: {
        "stem": "下腔靜脈屬大型靜脈，特徵是外膜很厚，含縱走平滑肌束；中膜相對薄。",
        "key": "Large veins have thick tunica adventitia with longitudinal smooth muscle bundles。",
        "reasons": {
            "A": "明顯內外彈性膜是動脈尤其 muscular artery 的特徵，不是下腔靜脈管壁重點。",
            "B": "大型靜脈的平滑肌不只在中膜，外膜也可有縱走平滑肌束。",
            "C": "下腔靜脈外膜比中膜厚，且有許多縱走平滑肌束，符合大型靜脈特徵。",
            "D": "中膜平滑肌多環形，外膜可縱走，排列方向不同，不應說相同。",
        },
    },
    42: {
        "stem": "膽汁由肝細胞分泌到膽小管，經赫林氏管連到小葉間膽管；其他選項多屬血液、淋巴或物質交換空間。",
        "key": "Canal of Hering is the transition ductule in bile flow from canaliculi to bile ducts。",
        "reasons": {
            "A": "赫林氏管是膽小管與小葉間膽管之間的膽汁運送管道，因此正確。",
            "B": "狄氏腔是肝竇內皮與肝細胞之間的交換空間，不是膽汁管道。",
            "C": "肝竇承載血液流動，方向與膽汁相反，並不運送膽汁。",
            "D": "乳糜管位於小腸絨毛內，負責脂質吸收後的淋巴運輸，不是肝內膽汁管。",
        },
    },
    43: {
        "stem": "肝細胞向膽小管分泌膽汁具外分泌功能，也向血液釋放白蛋白、凝血因子等，呈現類內分泌式分泌。",
        "key": "Hepatocytes have exocrine bile secretion and endocrine-like secretion into blood。",
        "reasons": {
            "A": "肝細胞同時把膽汁分泌到管腔系統，也把血漿蛋白等釋入血液，兼具外分泌與類內分泌功能。",
            "B": "胰島細胞主要是內分泌細胞，分泌胰島素、升糖素到血液，不具典型外分泌功能。",
            "C": "唾液腺腺泡細胞主要是外分泌，將唾液成分送入導管，不是兼具類內分泌的最佳答案。",
            "D": "庫弗氏細胞是肝內巨噬細胞，主要吞噬與免疫功能，不是腺性分泌細胞。",
        },
    },
    44: {
        "stem": "基底細胞與基底膜的附著靠半胞橋小體；胞橋小體則連接相鄰上皮細胞彼此。",
        "key": "Hemidesmosomes anchor basal epithelial cells to basement membrane via intermediate filaments。",
        "reasons": {
            "A": "胞橋小體連接細胞與細胞，常見於棘狀層，不是基底細胞連到基底膜的結構。",
            "B": "緊密接合主要封閉細胞間隙、維持屏障，不負責把基底細胞固定到基底膜。",
            "C": "間隙接合負責細胞間訊息與小分子通道，不是錨定結構。",
            "D": "半胞橋小體將基底細胞固定於基底膜，是表皮基底層的正確連接構造。",
        },
    },
    45: {
        "stem": "絨毛發育：初級是滋養層柱，次級加入胚外中胚層結締組織，三級再出現胎兒血管。",
        "key": "Tertiary chorionic villi are identified by fetal blood vessels in mesenchymal core。",
        "reasons": {
            "A": "初級絨毛主要由細胞滋養層被合體滋養層覆蓋，尚未有大量結締組織核心。",
            "B": "次級絨毛的定義是中胚層核心長入，不是只覆蓋部分絨毛膜囊；絨毛分布會隨發育形成絨毛膜板差異。",
            "C": "三級絨毛的結締組織核心內可見血管形成，這是區分三級絨毛的重點。",
            "D": "絨毛最外層是合體滋養層，不是細胞滋養層。",
        },
    },
    46: {
        "stem": "腎上腺絲球帶分泌礦物皮質素，尤其 aldosterone；糖皮質素主要由束狀帶分泌。題目問配對錯誤。",
        "key": "Zona glomerulosa secretes mineralocorticoids; zona fasciculata secretes glucocorticoids。",
        "reasons": {
            "A": "絲球帶不是糖皮質素主要分泌區，而是分泌 aldosterone 等礦物皮質素，所以配對錯誤。",
            "B": "腎上腺髓質含嗜鉻細胞，可分泌兒茶酚胺，配對正確。",
            "C": "腦上腺即松果體可見腦砂，配對正確。",
            "D": "腦下腺神經部可見赫氏小體，代表神經分泌物累積，配對正確。",
        },
    },
    47: {
        "stem": "膜允許水與 Na+ 通過，但 K+、Cl- 不通過。Na+ 會由右往左擴散，右側留下較多 Cl- 而帶負；左側因增加可滲透 Na+ 並受滲透效應影響，水量增加。",
        "key": "半透膜只讓 Na+ 與水通過時，Na+ 擴散會造成右側相對負電，水移向左側。",
        "reasons": {
            "A": "右側帶負電這半句合理，但左側水量不是減少，因此整體錯誤。",
            "B": "Na+ 從右側離開後右側相對留下 Cl-，不會帶正電；左側水量也不符。",
            "C": "Na+ 向左擴散使右側相對負電，且水往左側增加，符合平衡方向。",
            "D": "左側水量增加合理，但右側電性應偏負，不是正電。",
        },
    },
    48: {
        "stem": "排卵後黃體主要受 LH 支持分泌 progesterone；雌激素與黃體素可對下視丘腦下垂體產生負回饋，使 LH 分泌受抑制。",
        "key": "排卵後黃體期以 progesterone 為主，LH 支持黃體，estrogen/progesterone 對 LH/FSH 多為負回饋。",
        "reasons": {
            "A": "黃體主要受 LH 維持與刺激，不是 FSH 促進 progesterone 分泌。",
            "B": "排卵後雌激素合併黃體素可造成負回饋，抑制 LH 分泌，敘述正確。",
            "C": "子宮內膜增生主要由 estrogen 作用於子宮內膜，不是 FSH 直接刺激。",
            "D": "基礎體溫上升主要由 progesterone 的熱效應造成，不是 estrogen。",
        },
    },
    49: {
        "stem": "睪丸下降與 androgen 作用密切相關；精子生成能力也依賴睪固酮與正常陰囊溫度環境。",
        "key": "Androgen is important for inguinoscrotal phase of testicular descent and spermatogenesis。",
        "reasons": {
            "A": "激活素參與生殖軸與 FSH 調節，但不是睪丸下降到陰囊的主要因子。",
            "B": "雄性素促進睪丸下降，並與日後精子生成能力密切相關，是正確答案。",
            "C": "沃氏管退化因子這個概念不符合男性睪丸下降；Wolffian duct 在男性受雄性素維持。",
            "D": "血管內皮生長因子與血管生成有關，不是睪丸下降的主要考點。",
        },
    },
    50: {
        "stem": "視覺接受域在越往中樞通常越整合，視網膜節細胞接受域常呈同心圓拮抗；感光細胞本身接受域較小，節細胞通常整合多個感光細胞，直徑不會更小。",
        "key": "Ganglion cell receptive fields are center-surround and usually integrate input from multiple photoreceptors。",
        "reasons": {
            "A": "以移動光點觀察細胞放電變化來界定接受域，是合理的生理實驗描述。",
            "B": "相鄰神經元接受域較相似且重疊較高，符合視覺拓撲排列。",
            "C": "節細胞可呈同心圓拮抗接受域，但其接受域通常整合多個感光細胞，不會比單一感光細胞接受域更小；此項最不適當。",
            "D": "on-center/off-surround 與 off-center/on-surround 都有助邊界與位置解析，側抑制也可解釋 surround 效應。",
        },
    },
    51: {
        "stem": "上行網狀活化系統含橋腦膽鹼、藍斑去甲腎上腺素、縫線核血清素等；medial septal area 不是典型 dopaminergic arousal 核心。",
        "key": "ARAS 典型神經傳遞包括 ACh、NE、5-HT、histamine、orexin；dopamine 來源多不寫作 medial septal area。",
        "reasons": {
            "A": "橋腦網狀結構的膽鹼神經元是喚醒系統的重要組成。",
            "B": "藍斑核去甲腎上腺素神經元參與警醒與注意，屬 ARAS 典型部分。",
            "C": "內側中隔區不是主司意識喚起的典型 dopaminergic 核心，因此最不可能屬於題目系統。",
            "D": "背側縫線核血清素神經元與睡醒週期、喚醒調節相關，可列入上行調節系統。",
        },
    },
    52: {
        "stem": "Korsakoff syndrome 與硫胺素缺乏造成的記憶迴路病變有關，常牽涉 mammillary body、丘腦與前額/海馬旁網路；planum temporale 偏聽覺語言皮質。",
        "key": "Korsakoff 記憶缺損常與 mammillary bodies 和 limbic-diencephalic memory circuit 相關。",
        "reasons": {
            "A": "前額葉皮質和工作記憶、計畫與提取策略相關，可能與症狀有關。",
            "B": "海馬旁皮質參與情節記憶與臉孔/場景等記憶處理，和此個案記憶缺損相關。",
            "C": "乳頭體是 Korsakoff syndrome 的典型受損部位，與記憶障礙密切相關。",
            "D": "Planum temporale 主要與聽覺與語言處理相關；題幹還說長期聽覺記憶未明顯缺損，因此最不相關。",
        },
    },
    53: {
        "stem": "鈉鉀幫浦每消耗 1 ATP，將 3 Na+ 打出細胞、2 K+ 打入細胞。題目問錯誤敘述。",
        "key": "Na+/K+ ATPase pumps 3 Na+ out and 2 K+ in per ATP; inhibition can cause swelling and depolarization。",
        "reasons": {
            "A": "鈉鉀幫浦每循環需消耗一個 ATP，此敘述正確。",
            "B": "方向寫反了；正確是 3 個 Na+ 出細胞、2 個 K+ 入細胞，所以此項錯誤。",
            "C": "毛地黃抑制幫浦後細胞內 Na+ 增加，水分可能跟著進入，使細胞腫大。",
            "D": "幫浦被抑制會減少外向正電淨移動並改變離子梯度，細胞可趨向去極化。",
        },
    },
    54: {
        "stem": "肉毒桿菌毒素切割突觸前端 SNARE 蛋白，阻止乙醯膽鹼囊泡融合釋放，因此可降低肌肉收縮與痙攣。",
        "key": "Botulinum toxin cleaves SNARE proteins and blocks ACh release at neuromuscular junction。",
        "reasons": {
            "A": "直接阻斷鈣離子通道不是肉毒毒素的主要機轉；鈣離子進入仍需靠 SNARE 完成囊泡融合。",
            "B": "破壞 SNARE 蛋白會阻止乙醯膽鹼釋放，正是治療局部痙攣的藥理基礎。",
            "C": "抑制乙醯膽鹼受體是 postsynaptic 作用，較像神經肌肉阻斷劑，不是肉毒毒素。",
            "D": "抑制乙醯膽鹼酶會增加 ACh、加強膽鹼作用，與舒緩痙攣方向相反。",
        },
    },
    55: {
        "stem": "甘胺酸是脊髓與腦幹重要抑制性傳遞物質，受體為 Cl- 通道；strychnine 阻斷後會造成強直痙攣。",
        "key": "Glycine receptor is a chloride channel; strychnine antagonism causes disinhibition and spasms。",
        "reasons": {
            "A": "甘胺酸在脊髓與腦幹是主要抑制性神經傳遞物質，敘述正確。",
            "B": "甘胺酸受體開啟主要增加 Cl- 通透，不是讓 K+ 外流作為主要抑制機轉。",
            "C": "Strychnine 是甘胺酸受體拮抗劑，但過量會解除抑制導致肌肉痙攣，不是抑制肌肉收縮。",
            "D": "尼古丁型乙醯膽鹼受體沒有甘胺酸作為促進開啟的典型結合位；此描述混淆受體種類。",
        },
    },
    56: {
        "stem": "直線加速度與頭部相對重力的位置變化由耳石器偵測，也就是橢圓囊與球囊；半規管偵測角加速度。",
        "key": "Utricle and saccule detect linear acceleration; semicircular canals detect angular acceleration。",
        "reasons": {
            "A": "Ruffini corpuscle 是皮膚或關節伸展感受器，與前庭直線加速度偵測無關。",
            "B": "Corti 器是聽覺感受器，負責聲音轉導，不是平衡直線加速。",
            "C": "半規管偵測旋轉或角加速度，不是直線加速度的最主要構造。",
            "D": "橢圓囊與球囊含耳石膜，可偵測直線加速度與頭部傾斜，因此正確。",
        },
    },
    57: {
        "stem": "死亡後 ATP 不再供應，肌凝蛋白頭無法與肌動蛋白解離，造成肌肉僵硬，即屍僵。",
        "key": "ATP binding to myosin is required for detachment from actin; ATP depletion causes rigor mortis。",
        "reasons": {
            "A": "鈣離子結合 troponin 是啟動收縮所需，不是屍僵持續僵硬的主要原因。",
            "B": "Tropomyosin 持續覆蓋結合位會阻止收縮，和屍僵的固定橫橋不同。",
            "C": "缺乏 ATP 時 myosin cross-bridge 無法從 actin 脫離，正是屍僵主要機轉。",
            "D": "ATP 無法水解會影響能量循環，但屍僵關鍵是 ATP 缺乏使 myosin 無法解離。",
        },
    },
    58: {
        "stem": "IL-2 促進淋巴球增殖與 B 細胞分化反應；若 B 細胞無法形成漿細胞，最可能牽涉 T cell cytokine 支持不足。",
        "key": "IL-2 supports lymphocyte proliferation and can promote B-cell differentiation toward plasma cells。",
        "reasons": {
            "A": "Type I interferons 主要與抗病毒狀態相關，不是 B 細胞形成漿細胞的最典型缺乏因子。",
            "B": "Type II interferon 即 IFN-gamma 偏向巨噬細胞活化與 Th1 反應，不是本題核心。",
            "C": "IL-2 是促進淋巴球增殖與 B 細胞分化的重要 cytokine，最符合題目描述。",
            "D": "Colony-stimulating factors 主要促進骨髓造血細胞系分化，不是 B 細胞變漿細胞的主要訊號。",
        },
    },
    59: {
        "stem": "心臟交感作用主要是 norepinephrine 作用於 beta-1 受體加快心跳；副交感則釋放 ACh 作用於 muscarinic M2 受體減慢心跳。",
        "key": "Vagal ACh on M2 muscarinic receptors slows SA node firing and heart rate。",
        "reasons": {
            "A": "交感加快心跳主要靠 beta-1 受體，不是 alpha-1。",
            "B": "Alpha-2 不是心臟交感加快心跳的主要受體；交感活性通常增加心率。",
            "C": "副交感節後纖維作用於心臟 muscarinic 受體，不是 nicotinic 受體，且效果是減慢心跳。",
            "D": "副交感釋放 ACh 作用於 M2 muscarinic 受體，可降低竇房結放電頻率，敘述最合理。",
        },
    },
    60: {
        "stem": "等容收縮期開始時二尖瓣已關閉、主動脈瓣尚未打開；左室壓正在上升但仍低於主動脈壓，且高於左房壓。",
        "key": "Isovolumic contraction: aortic pressure > LV pressure > LA pressure before aortic valve opens。",
        "reasons": {
            "A": "主動脈瓣尚未開啟時，主動脈壓仍高於左室壓；左室壓已高於左房壓，排列正確。",
            "B": "左室壓在二尖瓣關閉後已高於左房壓，不會低於左心房。",
            "C": "若左室壓已高於主動脈壓，主動脈瓣會開啟進入射血期，不是等容收縮期。",
            "D": "等容收縮期主動脈壓不會低於左房壓，且左室壓尚未超過主動脈壓。",
        },
    },
    61: {
        "stem": "用 Fick principle：cardiac output = O2 consumption / (arterial O2 content - venous O2 content)。1.9 L/min 等於 1900 mL/min，動靜脈差為 54 mL/L。",
        "key": "CO = 1900 / (188-134) = 1900/54，約 35 L/min。",
        "reasons": {
            "A": "17.5 L/min 相當於把氧耗量或動靜脈差多除了一次，低估了計算值。",
            "B": "1900 mL/min 除以 54 mL/L 約為 35 L/min，符合 Fick principle。",
            "C": "70 L/min 約為正確值兩倍，常見於把動靜脈差誤算成 27 mL/L。",
            "D": "14 L/min 明顯低於公式計算結果，不符合題目給的耗氧量與含氧差。",
        },
    },
    62: {
        "stem": "失血造成 MAP 下降的直接原因是血容量下降、靜脈回流下降、舒張末期容積下降，進而心輸出量下降；副交感活性減少是代償反應，不是造成 MAP 下降的原因。",
        "key": "Hemorrhage lowers MAP by reducing blood volume, venous return, EDV, stroke volume, and cardiac output。",
        "reasons": {
            "A": "血液總體積下降是失血造成平均動脈壓下降的直接起點。",
            "B": "心臟副交感活性減少通常會使心跳變快，是壓力下降後的代償，不是最相關的致壓下降因素。",
            "C": "周邊靜脈壓和靜脈回流下降會降低前負荷，直接導致 MAP 下降。",
            "D": "心室舒張末期容積下降使搏出量下降，是失血性低血壓的重要機轉。",
        },
    },
    63: {
        "stem": "肺水腫增加擴散距離而降低氧氣擴散能力；運動時肺微血管招募與擴張，使有效交換面積增加，擴散能力上升。",
        "key": "Diffusing capacity decreases in pulmonary edema and increases during exercise。",
        "reasons": {
            "A": "肺水腫不會增加擴散能力；水腫使膜變厚，氧氣通過更困難。",
            "B": "運動時增加這半句正確，但肺水腫時方向錯誤。",
            "C": "肺水腫使擴散能力下降，運動使肺血管床招募而擴散能力上升，兩者皆正確。",
            "D": "肺水腫下降正確，但運動通常會增加而不是減少擴散能力。",
        },
    },
    64: {
        "stem": "過度換氣會排出更多 CO2，使肺泡 PCO2 與動脈 CO2 含量下降；依肺泡氣體方程式，肺泡 PO2 會上升。",
        "key": "Hyperventilation increases alveolar PO2, decreases alveolar PCO2, and lowers arterial total CO2 content。",
        "reasons": {
            "A": "1 與 2 都對，但漏掉體動脈血 CO2 總含量下降。",
            "B": "2 與 3 都對，但過度換氣也會使肺泡氧分壓上升。",
            "C": "1 與 3 都對，但也應包含肺泡 CO2 分壓下降。",
            "D": "三個敘述都符合過度換氣的氣體變化，因此正確。",
        },
    },
    65: {
        "stem": "D 細胞分泌 somatostatin，會抑制 G 細胞、ECL 細胞與壁細胞，促進胃酸效果最低；其他選項多促酸。",
        "key": "Somatostatin from D cells inhibits gastric acid secretion。",
        "reasons": {
            "A": "刺激 D 細胞會增加 somatostatin，抑制胃泌素、組織胺與壁細胞，所以促進胃酸效果最低。",
            "B": "ECL 細胞釋放 histamine，作用於 H2 受體促進壁細胞分泌胃酸。",
            "C": "G 細胞分泌 gastrin，可直接或經 ECL 細胞間接促進胃酸分泌。",
            "D": "迷走神經透過 ACh 與 GRP 等訊號促進胃酸分泌，效果不低。",
        },
    },
    66: {
        "stem": "分節運動是小腸局部來回收縮，重點在混合食糜與增加接觸吸收面，不是快速推進。",
        "key": "Segmentation primarily mixes intestinal contents; peristalsis propels。",
        "reasons": {
            "A": "分節運動反覆分割與混合腸腔內容物，是最適當的功能描述。",
            "B": "胃結腸反射是進食後促進結腸運動的反射，不是分節運動本身的主要功能。",
            "C": "快速推進食物是蠕動或 mass movement 的特性，不是 segmentation 的重點。",
            "D": "抑制胃排空與降低胃酸分泌和腸道分節運動的主要生理功能不符。",
        },
    },
    67: {
        "stem": "遠端腎小管鉀分泌受 aldosterone、管腔鈉量、流速與血鉀影響；aldosterone 降低會減少 ENaC 與 Na/K ATPase 活性，降低鉀分泌。",
        "key": "Aldosterone increases distal K+ secretion; low aldosterone decreases it。",
        "reasons": {
            "A": "血漿量減少通常啟動 RAAS，提高 aldosterone，反而促進遠端鉀分泌。",
            "B": "管腔鈉增加使鈉再吸收增加、管腔偏負，通常促進鉀分泌。",
            "C": "Aldosterone 降低會減少遠端鈉再吸收與鉀分泌，是最可能造成鉀分泌下降的原因。",
            "D": "飲食鉀增加會刺激 aldosterone 與遠端鉀分泌，方向相反。",
        },
    },
    68: {
        "stem": "菊糖清除率代表 GFR，公式為 C = UxV/P。題目給 U=35 mg/mL、V=0.6 mL/min、P=0.25 mg/mL。",
        "key": "Inulin clearance = 35 x 0.6 / 0.25 = 84 mL/min。",
        "reasons": {
            "A": "35 乘以 0.6 得 21，再除以 0.25 得 84 mL/min，計算正確。",
            "B": "106 mL/min 不是依 UxV/P 代入後的結果，可能來自分母誤用。",
            "C": "116 mL/min 接近一般男性 GFR，但本題要照給定數字計算。",
            "D": "126 mL/min 也是常見正常值範圍附近，但與本題清除率公式不符。",
        },
    },
    69: {
        "stem": "腦下垂體腫瘤切除會影響 ACTH、TSH、LH/FSH 等軸；aldosterone 主要由 RAAS 與血鉀調控，最不依賴腦下垂體。",
        "key": "Aldosterone secretion is mainly regulated by angiotensin II and plasma K+, not pituitary ACTH。",
        "reasons": {
            "A": "皮質醇受 ACTH 促進，腦下垂體手術後可能明顯受影響。",
            "B": "Aldosterone 主要受 RAAS 和血鉀控制，對腦下垂體依賴最小。",
            "C": "黃體素受 LH/FSH 所屬性腺軸影響，腦下垂體受損可能改變其分泌。",
            "D": "甲狀腺素受 TSH 調節，腦下垂體切除後可能下降。",
        },
    },
    70: {
        "stem": "Insulin、thyroid hormone、testosterone 多支持生長與蛋白合成；長期 cortisol 過多會分解蛋白、抑制骨與兒童生長。",
        "key": "Cortisol has catabolic and growth-inhibiting effects when excessive or chronic。",
        "reasons": {
            "A": "皮質醇具分解代謝作用，過多會抑制線性生長與蛋白合成，是本題答案。",
            "B": "胰島素促進葡萄糖攝取、脂肪與蛋白合成，整體偏促進生長。",
            "C": "甲狀腺荷爾蒙對兒童正常生長與神經發育必需，不是明顯抑制生長者。",
            "D": "睪固酮促進青春期生長、蛋白合成與第二性徵發育，屬生長促進方向。",
        },
    },
    71: {
        "stem": "發炎會啟動下視丘-腦下垂體-腎上腺軸，使腎上腺皮質分泌 cortisol，藉抗發炎與免疫調節限制過度反應。",
        "key": "Inflammation activates adrenal cortisol secretion, which suppresses inflammatory mediators。",
        "reasons": {
            "A": "Renin 主要調節血壓與體液容積，不是身體抗發炎的主要荷爾蒙反應。",
            "B": "皮膚與維生素 B 分泌的說法不符合生理；皮膚主要與維生素 D 合成相關。",
            "C": "胰臟 somatostatin 可抑制多種內分泌分泌，但不是對抗全身發炎的主要反應。",
            "D": "腎上腺分泌 cortisol 可抑制發炎介質與免疫反應，符合題目所問。",
        },
    },
    72: {
        "stem": "高張食鹽水會升高血漿滲透壓，刺激口渴與 ADH 分泌增加；題目問最不適當，因此 ADH 減少是錯誤處。",
        "key": "Hyperosmolality increases thirst and ADH secretion; volume depletion can stimulate thirst via angiotensin II。",
        "reasons": {
            "A": "口渴主要受滲透壓與細胞外液容積調控，此敘述正確。",
            "B": "高張食鹽水會使 ADH 增加而非減少，同時造成口渴，所以此項最不適當。",
            "C": "細胞外液下降可增加 renin 與 angiotensin II，刺激口渴中樞，敘述合理。",
            "D": "容積和滲透壓可分開變動，例如等張失血改變容積但滲透壓未必改變。",
        },
    },
    73: {
        "stem": "Insulin deficiency 使組織葡萄糖利用下降、脂解增加，肝臟把脂肪酸轉成酮體，造成 ketosis 或 ketoacidosis。",
        "key": "Insulin deficiency increases hepatic ketogenesis and decreases glycogen/lipid synthesis and muscle glucose uptake。",
        "reasons": {
            "A": "胰島素不足會降低肝醣合成，並促進肝醣分解與糖質新生，不會增加肝醣合成。",
            "B": "肌肉 GLUT4 依賴胰島素；胰島素不足時肌肉葡萄糖吸收下降。",
            "C": "胰島素不足促進脂解與肝臟酮體生成，是最典型代謝變化。",
            "D": "脂肪合成受胰島素促進，缺乏時會下降而不是增加。",
        },
    },
    74: {
        "stem": "Michaelis-Menten 反應在受質濃度遠大於 KM 時，酵素接近飽和，反應速率接近 Vmax，不再隨受質濃度明顯改變。",
        "key": "When [S] >> KM, enzyme reaction approximates zero-order kinetics。",
        "reasons": {
            "A": "酵素飽和時速率幾乎固定，與受質濃度無關，近似零級反應。",
            "B": "一級反應發生在低受質濃度、速率約與受質濃度成正比時，不是 [S] 遠大於 KM。",
            "C": "二級反應需速率與兩個反應物濃度相關，非典型酵素飽和狀態。",
            "D": "三元級反應不是 Michaelis-Menten 飽和時的常用近似。",
        },
    },
    75: {
        "stem": "酵素降低活化能但不改變反應平衡與自身總量；沒有酵素時反應仍可能慢速進行。題目問正確敘述。",
        "key": "Enzymes are catalysts: they are not consumed and do not change equilibrium.",
        "reasons": {
            "A": "酵素可催化放熱或吸熱反應，是否放熱由反應自由能決定，不由酵素決定。",
            "B": "酵素不改變平衡常數，催化反應仍可達到化學平衡。",
            "C": "酵素作為催化劑在反應前後總量不被消耗，敘述正確。",
            "D": "沒有酵素時反應通常仍可發生，只是速率可能極慢，不是完全不會發生。",
        },
    },
    76: {
        "stem": "雙硫鍵是兩個 cysteine 的硫醇氧化形成的共價鍵，對蛋白質三級或四級結構穩定很重要，可被強還原劑斷開。",
        "key": "Disulfide bonds are covalent cystine bonds and are broken by reducing agents。",
        "reasons": {
            "A": "雙硫鍵常顯著穩定蛋白質立體構形，特別是分泌蛋白與細胞外蛋白。",
            "B": "雙硫鍵由兩個 cysteine 形成 cystine，不是由 methionine 形成。",
            "C": "強還原劑可還原雙硫鍵為硫醇，破壞相關蛋白質結構，因此正確。",
            "D": "雙硫鍵是共價鍵，不屬於非共價交互作用。",
        },
    },
    77: {
        "stem": "真核細胞週期中，DNA 複製發生於 S phase，也就是 synthesis phase；G1 準備，G2 檢查，M 期分裂。",
        "key": "DNA replication occurs in S phase of the eukaryotic cell cycle。",
        "reasons": {
            "A": "G1 期主要進行生長與準備進入 DNA 合成，不是複製 DNA 的時期。",
            "B": "S 期是 DNA synthesis 的時期，染色體 DNA 在此完成複製。",
            "C": "G2 期在 DNA 複製後，主要進行修復檢查與有絲分裂準備。",
            "D": "M 期是染色體分離與細胞分裂，不是 DNA 複製期。",
        },
    },
    78: {
        "stem": "EGF receptor 是 receptor tyrosine kinase，ligand binding 後促使受體二聚化與自體磷酸化。",
        "key": "EGFR activation involves ligand-induced receptor dimerization and tyrosine autophosphorylation。",
        "reasons": {
            "A": "菸鹼型乙醯膽鹼受體本身是多次單元的 ligand-gated ion channel，不是由單體受配體後二聚化的典型 RTK。",
            "B": "EGF 與 EGFR 結合後促進受體由單體形成二聚體並啟動酪胺酸激酶活性。",
            "C": "Beta-adrenergic receptor 是 G protein-coupled receptor，活化重點不是受體二聚化。",
            "D": "Integrin 常作為細胞外基質受體並傳遞黏附訊號，不是典型 ligand-induced monomer-to-dimer receptor tyrosine kinase 題型。",
        },
    },
    79: {
        "stem": "類固醇源自膽固醇，脂溶性可穿透細胞膜，與細胞內受體結合後調控基因轉錄；題目問錯誤敘述。",
        "key": "Steroid hormones diffuse across membranes and bind intracellular receptors that regulate transcription。",
        "reasons": {
            "A": "腎上腺皮質類固醇以前驅物膽固醇合成，敘述正確。",
            "B": "類固醇可穿透細胞膜，主要作用於細胞質或細胞核內受體；說無法穿膜且必須作用膜受體是錯的。",
            "C": "類固醇與受體結合後會造成受體構形改變，使其能調控基因表現。",
            "D": "活化後的類固醇受體可作為轉錄調節因子，影響基因轉錄。",
        },
    },
    80: {
        "stem": "反義寡核酸可與 RNA 配對，影響 splicing、促進 RNase H 介導 mRNA 降解或阻礙轉譯；它不會把 RNA 序列直接突變成新序列。",
        "key": "Antisense oligonucleotides alter RNA processing, stability, or translation, not direct RNA sequence mutation。",
        "reasons": {
            "A": "反義寡核酸可遮蔽剪接位點或調整 exon inclusion，確實能影響 RNA splicing。",
            "B": "造成 RNA 序列突變不是反義寡核酸的典型作用；它是配對調控，不是改寫核苷酸序列。",
            "C": "某些 antisense oligonucleotides 可招募 RNase H，使目標 mRNA 降解。",
            "D": "與 mRNA 配對可阻礙 ribosome 或調整可用模板，影響蛋白質轉譯效率。",
        },
    },
    81: {
        "stem": "雙股 DNA 解旋時鹼基堆疊減少，260 nm 吸光度上升；利用低色度/增色效應可測定 melting temperature。",
        "key": "DNA melting is monitored by loss of hypochromicity and increased absorbance at 260 nm。",
        "reasons": {
            "A": "導電性不是測定 DNA Tm 的典型物理性質。",
            "B": "膠體泳動性可用於大小或構形分析，但不直接用來量測熱變性 Tm。",
            "C": "水溶性不是 DNA 雙股融解溫度的主要測量指標。",
            "D": "雙股 DNA 具低色度，受熱解旋後吸光增加，這個變化可用來測定 Tm。",
        },
    },
    82: {
        "stem": "糙皮病典型 3D 是 dermatitis、diarrhea、dementia，由 niacin 或 tryptophan 代謝不足導致 NAD/NADP 缺乏。",
        "key": "Niacin deficiency causes pellagra: dermatitis, diarrhea, dementia。",
        "reasons": {
            "A": "Thiamine 缺乏造成 beriberi 或 Wernicke-Korsakoff，不是 pellagra。",
            "B": "Niacin 缺乏造成糙皮病，典型有腹瀉、皮膚炎與癡呆。",
            "C": "Riboflavin 缺乏常見口角炎、舌炎、脂漏性皮膚炎，不是典型 3D 糙皮病。",
            "D": "Pantothenic acid 缺乏少見，與 CoA 合成相關，不是 pellagra 的主要原因。",
        },
    },
    83: {
        "stem": "CoA 由泛酸、ADP 衍生物與 beta-mercaptoethylamine 組成，反應硫原子來自巰基乙胺，不是 cysteine 本身；題目問錯誤。",
        "key": "CoA contains pantothenate, ADP, and beta-mercaptoethylamine; its thiol carries acyl groups。",
        "reasons": {
            "A": "CoA 結構不是直接由泛酸、ADP 衍生物與 cysteine 結合而成；反應性 thiol 在 beta-mercaptoethylamine 上，因此此項錯誤。",
            "B": "CoA 的硫原子能形成 thioester 與 acyl group 結合，這是 acyl-CoA 的核心化學。",
            "C": "Pyruvate dehydrogenase complex 會利用 CoA 形成 acetyl-CoA，敘述正確。",
            "D": "Alpha-ketoglutarate dehydrogenase complex 也需 CoA，產生 succinyl-CoA，敘述正確。",
        },
    },
    84: {
        "stem": "嘧啶可分解成可溶性產物；thymine 分解產生 beta-aminoisobutyric acid，而 cytosine/uracil 可產生 beta-alanine。",
        "key": "Thymine catabolism yields beta-aminoisobutyric acid。",
        "reasons": {
            "A": "Beta-aminoisobutyric acid 是 thymine 分解後可在尿中測得的代謝產物。",
            "B": "Beta-alanine 較對應 uracil 與 cytosine 分解，不是 thymine 的典型答案。",
            "C": "Uridine 是核苷，不是 thymine 分解的最終尿中代謝產物。",
            "D": "Cytidine 是胞嘧啶核苷，和 thymine 分解產物不相符。",
        },
    },
    85: {
        "stem": "DNA polymerase 的 proofreading 是在新生鏈方向反向移除錯誤核苷酸，靠 3' to 5' exonuclease activity。",
        "key": "DNA proofreading uses 3' to 5' exonuclease activity。",
        "reasons": {
            "A": "5'→3' polymerase 活性負責延長 DNA 鏈，不是校對切除錯誤鹼基。",
            "B": "DNA 聚合反應不是 3'→5' 方向進行；新鏈延長方向為 5'→3'。",
            "C": "5'→3' exonuclease 活性可移除前方引子或用於 nick translation，不是主要 proofreading。",
            "D": "3'→5' exonuclease 可從新生鏈 3' 端移除誤配核苷酸，是主要校對活性。",
        },
    },
    86: {
        "stem": "DNA 中出現 uracil 常來自 cytosine 去胺化或 dUTP 誤摻入，先由 uracil-DNA glycosylase 移除鹼基，再走 base excision repair。",
        "key": "Uracil in DNA is repaired mainly by base excision repair。",
        "reasons": {
            "A": "直接修復通常指不切除鹼基而直接還原損傷，例如光復活或 methylguanine 修復，不是移除 uracil 的主路徑。",
            "B": "重組修復用於雙股斷裂或複製叉相關問題，不是單一錯誤鹼基 uracil 的主要處理。",
            "C": "鹼基切除修復會先移除異常鹼基形成 AP site，再補回正確核苷酸，符合 uracil 修復。",
            "D": "Mismatch repair 主要修正複製後錯配，並非 DNA 上 uracil 鹼基本身的首要機制。",
        },
    },
    87: {
        "stem": "大腸桿菌 DNA polymerase III 是染色體複製的主要聚合酶，需要 primer 提供 3'-OH 來延長 DNA。",
        "key": "E. coli DNA polymerase III is the main replicative polymerase and requires a primer 3'-OH。",
        "reasons": {
            "A": "DNA polymerase 不能從無引子開始合成，需要既有 3'-OH。",
            "B": "DNA polymerase III 是大腸桿菌 DNA 複製時的主要聚合酶，負責快速延長新生鏈。",
            "C": "Nick translation 常用 DNA polymerase I，利用其 5'→3' exonuclease 與 polymerase 活性。",
            "D": "聚合酶需要的是 primer 的 3'-羥基，不是 5'-羥基；此選項把方向寫錯。",
        },
    },
    88: {
        "stem": "蛋白質接上 ubiquitin，尤其形成 polyubiquitin chain，會被 26S proteasome 辨識並分解。",
        "key": "Ubiquitination targets proteins for proteasomal degradation。",
        "reasons": {
            "A": "Methylation 常調控蛋白質或染色質功能，不是蛋白酶體辨識分解的直接標籤。",
            "B": "Acetylation 可影響蛋白活性、定位或染色質狀態，但不是典型 proteasome 降解訊號。",
            "C": "Ubiquitination 是蛋白酶體辨識蛋白並進行分解的直接標記。",
            "D": "Glycosylation 主要影響蛋白折疊、穩定性、分泌與細胞辨識，不是 proteasome 的直接降解標籤。",
        },
    },
    89: {
        "stem": "原核轉譯起始時，IF2-GTP 負責把帶 formyl-methionine 的 initiator tRNA 帶到核糖體 P site。",
        "key": "IF2 delivers fMet-tRNAi to the bacterial ribosome during initiation。",
        "reasons": {
            "A": "IF1 幫助阻止 tRNA 過早進入 A site，並促進起始複合體組裝，但不攜帶 fMet-tRNA。",
            "B": "IF2 是 GTP 結合起始因子，負責運送 fMet-tRNA 到核糖體，正確。",
            "C": "IF3 防止 30S 與 50S 過早結合並協助選擇起始位置，不是 tRNA 載體。",
            "D": "EF-Tu 在延長期攜帶 aminoacyl-tRNA 至 A site，不負責起始 fMet-tRNA。",
        },
    },
    90: {
        "stem": "轉譯釋放因子 RF1/RF2 具有 tRNA mimicry，能進入 A site 辨識 stop codon，立體上最像 tRNA。",
        "key": "Bacterial release factors structurally mimic tRNA to recognize stop codons in the A site。",
        "reasons": {
            "A": "IF2 參與起始並結合 GTP，但整體不是最典型的 tRNA mimic 答案。",
            "B": "EF-Tu 攜帶 aminoacyl-tRNA，本身與 tRNA 結合，但其立體結構不如釋放因子直接模擬 tRNA。",
            "C": "RF1 進入核糖體 A site 辨識終止密碼，具有類似 tRNA 的空間模擬特徵，因此最相似。",
            "D": "伴護蛋白協助蛋白折疊，與 tRNA 形狀模擬無關。",
        },
    },
    91: {
        "stem": "原核 DNA 結合調控蛋白常用 helix-turn-helix motif 插入 DNA major groove 辨識序列。",
        "key": "Helix-turn-helix is a common DNA-binding motif in prokaryotic transcription regulators。",
        "reasons": {
            "A": "Homeobox 是真核發育調控常見 DNA-binding domain，不是原核調控蛋白的典型答案。",
            "B": "Catalytic triad 是許多蛋白酶活性中心結構，和 DNA 結合調控無關。",
            "C": "EF hand 是鈣離子結合模體，不是原核 DNA 結合蛋白主要辨識結構。",
            "D": "Helix-turn-helix 是原核轉錄調控蛋白常見 DNA-binding motif，正確。",
        },
    },
    92: {
        "stem": "Cori cycle 中，肌肉無氧糖解產生 lactate，送到肝臟；肝臟經糖質新生把 lactate 轉回 glucose，再送回肌肉。",
        "key": "Cori cycle: muscle lactate to liver; liver gluconeogenesis produces glucose。",
        "reasons": {
            "A": "乳酸方向是由骨骼肌送到肝臟，不是由肝臟送到骨骼肌。",
            "B": "葡萄糖方向是由肝臟產生後送到骨骼肌，不是骨骼肌送到肝臟。",
            "C": "肝臟利用 lactate 進行糖質新生產生葡萄糖，是 Cori cycle 核心。",
            "D": "骨骼肌主要把 glucose 經糖解轉成 lactate；糖質新生主要在肝臟與腎臟，不是骨骼肌。",
        },
    },
    93: {
        "stem": "糖解作用不可逆三步為 hexokinase/glucokinase、PFK-1、pyruvate kinase；選項中只有 pyruvate kinase 屬不可逆步驟。",
        "key": "Pyruvate kinase catalyzes an irreversible glycolytic step: PEP to pyruvate。",
        "reasons": {
            "A": "Enolase 催化 2-phosphoglycerate 變 phosphoenolpyruvate，接近平衡，非主要不可逆步驟。",
            "B": "Phosphoglycerate kinase 催化產生 ATP 的可逆步驟，不是糖解三個不可逆控制點之一。",
            "C": "Pyruvate kinase 催化 PEP 轉成 pyruvate，為正常生理下不可逆反應。",
            "D": "Aldolase 催化 fructose-1,6-bisphosphate 裂解，反應可逆，不是本題答案。",
        },
    },
    94: {
        "stem": "麥芽糖由兩個葡萄糖以 alpha-1,4 糖苷鍵連接；蔗糖是 glucose-fructose，乳糖是 galactose-glucose。",
        "key": "Maltose = Glc alpha(1 to 4) Glc。",
        "reasons": {
            "A": "Glc alpha(1→2) Fru 是蔗糖，不是麥芽糖。",
            "B": "Gal beta(1→4) Glc 是乳糖，不是麥芽糖。",
            "C": "Glc alpha(1→4) Glc 是麥芽糖的結構，正確。",
            "D": "Glc alpha(1→1) Glc 不是麥芽糖典型鍵結；麥芽糖需 alpha-1,4。",
        },
    },
    95: {
        "stem": "葡萄糖進入細胞後被 hexokinase 或 glucokinase 磷酸化成 glucose-6-phosphate，帶電後不易穿膜離開，得以留在細胞內代謝。",
        "key": "Phosphorylation traps glucose inside cells as glucose-6-phosphate。",
        "reasons": {
            "A": "Glycosylation 是糖基接到蛋白或脂質上的修飾，不是葡萄糖被留在細胞內的主要方式。",
            "B": "Phosphorylation 使葡萄糖變成 glucose-6-phosphate，帶負電而被留在細胞內，正確。",
            "C": "Palmitoylation 是脂肪酸接到蛋白質上的修飾，與葡萄糖進入細胞後滯留無關。",
            "D": "Acetylation 常見於蛋白質或代謝中乙醯基轉移，不是葡萄糖初始代謝的 trapping 步驟。",
        },
    },
    96: {
        "stem": "Pyruvate oxidative decarboxylation、oxidative phosphorylation 與脂肪酸 beta-oxidation 主要在線粒體；pentose phosphate pathway 在細胞質。",
        "key": "Pentose phosphate pathway occurs in the cytosol, not mitochondria。",
        "reasons": {
            "A": "Pyruvate oxidative decarboxylation 由 mitochondrial pyruvate dehydrogenase complex 進行。",
            "B": "Pentose phosphate pathway 主要在細胞質產生 NADPH 與 ribose-5-phosphate，不在線粒體內進行。",
            "C": "Oxidative phosphorylation 發生在線粒體內膜電子傳遞鏈與 ATP synthase。",
            "D": "Fatty acid beta-oxidation 主要在線粒體基質進行；很長鏈脂肪酸另有過氧化體起始處理。",
        },
    },
    97: {
        "stem": "膽酸由肝細胞以膽固醇為前驅物合成，幫助脂質與脂溶性維生素吸收；題目問錯誤敘述，水溶性維生素不靠膽酸吸收。",
        "key": "Bile acids emulsify fats and aid absorption of fat-soluble vitamins A, D, E, K, not water-soluble vitamins。",
        "reasons": {
            "A": "脂肪消化吸收需要膽酸形成 micelle 協助，因此敘述正確。",
            "B": "膽酸可由肝細胞利用膽固醇合成，敘述正確。",
            "C": "膽酸促進的是脂溶性維生素吸收，不是水溶性維生素，所以此項錯誤。",
            "D": "膽固醇是膽酸合成前驅物，敘述正確。",
        },
    },
    98: {
        "stem": "支鏈胺基酸是 leucine、isoleucine、valine；lysine 不是 BCAA。題目問錯誤敘述。",
        "key": "BCAAs are leucine, isoleucine, and valine; MSUD is due to BCKD complex deficiency。",
        "reasons": {
            "A": "此選項把 lysine 放入 BCAA，卻漏掉 valine；因此是錯誤敘述。",
            "B": "BCAA 初始轉胺作用在肌肉較活躍，肌肉 BCAA aminotransferase 活性高於肝臟，敘述正確。",
            "C": "楓糖尿症源於 branched-chain alpha-keto acid dehydrogenase complex 缺陷，敘述正確。",
            "D": "BCAA 後續氧化代謝可產生 NADH 與 FADH2，敘述合理。",
        },
    },
    99: {
        "stem": "白胺酸是必需胺基酸，且為純生酮性胺基酸；lysine 也純生酮但不在選項中。",
        "key": "Leucine is both essential and exclusively ketogenic。",
        "reasons": {
            "A": "天門冬胺酸不是必需胺基酸，且主要為生糖性。",
            "B": "組胺酸是必需胺基酸，但主要屬生糖性，不是典型生酮性答案。",
            "C": "酪胺酸可生糖兼生酮，但不是必需胺基酸，因可由 phenylalanine 生成。",
            "D": "白胺酸是必需胺基酸，也是純生酮性胺基酸，因此符合兩個條件。",
        },
    },
    100: {
        "stem": "NADH 電子經 complex I、III、IV 傳到氧；I、III、IV 會把質子打到膜間腔，complex II 不打質子。Complex III 每對電子約移動 4 個 H+ 到膜間腔。",
        "key": "Electron transport from NADH pumps protons at complexes I, III, IV; complex III transfers 4 H+ to intermembrane space。",
        "reasons": {
            "A": "Complex I 把 H+ 送到粒線體膜間腔，不是細胞質；題目位置寫錯。",
            "B": "Complex II 接收 FADH2 電子但不幫浦質子，因此不會移轉 2 個 H+ 到膜間腔。",
            "C": "Complex III 經 Q cycle 每對電子可將 4 個 H+ 移到膜間腔，敘述正確。",
            "D": "Complex IV 將 H+ 往膜間腔泵送，且在基質側消耗 H+ 還原氧，不是移到基質。",
        },
    },
}


def make_explanation(entry):
    reasons = entry["reasons"]
    return (
        f"【題幹解析】{entry['stem']}\n\n"
        "【選項詳解】\n"
        f"- A. {reasons['A']}\n"
        f"- B. {reasons['B']}\n"
        f"- C. {reasons['C']}\n"
        f"- D. {reasons['D']}\n\n"
        f"【核心考點】{entry['key']}"
    )


def main():
    data = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8-sig"))
    questions = data["questions"]
    by_number = {q["question_number"]: q for q in questions}
    missing = sorted(set(range(1, 101)) - set(ENTRIES))
    if missing:
        raise SystemExit(f"missing entries: {missing}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for start in range(1, 101, 10):
        end = start + 9
        updates = []
        for number in range(start, end + 1):
            q = by_number[number]
            entry = ENTRIES[number]
            key = entry["key"]
            front = q.get("flashcard_front") or q["question_text"].strip()
            updates.append(
                {
                    "question_id": q["id"],
                    "question_number": number,
                    "explanation": make_explanation(entry),
                    "key_point": key,
                    "flashcard_front": front,
                    "flashcard_back": key,
                    "flashcard_summary": f"{front} -> {key}",
                    "review_status": "ai_generated",
                    "explanation_model": "codex-high-quality-rewrite",
                    "explanation_generated_at": GENERATED_AT,
                    "manual_review_notes": [],
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

    print(f"wrote {len(list(OUT_DIR.glob('q*.json')))} update files to {OUT_DIR}")


if __name__ == "__main__":
    main()
