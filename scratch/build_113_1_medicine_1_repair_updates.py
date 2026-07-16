import json
from pathlib import Path

SOURCE_FILE = "public/data/exams/113-1/medicine-1.json"
DATASET_ID = "113-1_medicine-1"
OUT_DIR = Path("scratch/rewrite_updates/113-1_medicine-1")
STAMP = "2026-07-16T00:00:00+08:00"

QDATA = {
    6: {
        "analysis": "題目問鼓膜的一般體感覺支配，重點是排除第 VIII 對腦神經。鼓膜外側面主要由三叉神經 V3 的耳顳神經與迷走神經耳支支配，部分可由顏面神經支配；內側面由舌咽神經經鼓室叢支配。",
        "notes": {
            "A": "123 包含三叉神經與顏面神經，但錯把前庭耳蝸神經列入，且漏掉舌咽神經與迷走神經，因此不正確。",
            "B": "1234 雖包含舌咽神經，但仍錯列第 VIII 對前庭耳蝸神經，且漏掉迷走神經，因此不正確。",
            "C": "2345 包含顏面、舌咽與迷走神經，但仍錯列前庭耳蝸神經，且漏掉三叉神經 V3 的耳顳神經，因此不正確。",
            "D": "1245 排除了只負責聽覺與平衡的前庭耳蝸神經，保留三叉、顏面、舌咽與迷走神經，符合鼓膜體感覺支配。",
        },
        "core": "鼓膜體感覺支配為 CN V3、少部分 CN VII、CN IX 與 CN X；CN VIII 負責聽覺與平衡，不支配鼓膜體感覺。",
    },
    13: {
        "analysis": "翼點（pterion）骨質薄，深面有腦膜中動脈前支經過。側頭部撞擊後數小時出現硬腦膜外血腫，最典型就是腦膜中動脈破裂。",
        "notes": {
            "A": "硬腦膜靜脈竇受傷可造成靜脈性出血，但翼點撞擊後典型硬腦膜外血腫不是 dural sinus 破裂。",
            "B": "腦膜中動脈前支貼近翼點深面，骨折後易破裂，造成動脈性硬腦膜外血腫與 lucid interval，故正確。",
            "C": "前大腦動脈位於顱內蛛網膜下腔，破裂較會造成蛛網膜下腔或腦內相關出血，不是翼點 EDH 典型血管。",
            "D": "後大腦動脈供應枕葉與下顳葉等區域，位置與翼點外傷導致硬腦膜外血腫的典型機轉不符。",
        },
        "core": "翼點骨折最怕腦膜中動脈破裂，造成硬腦膜外血腫。",
    },
    18: {
        "analysis": "主胰管與膽總管通常在十二指腸壁內匯合成肝胰壺腹，經大十二指腸乳頭開口；大十二指腸乳頭位於十二指腸下降段。",
        "notes": {
            "A": "十二指腸上段接近幽門與球部，常與潰瘍相關，但不是膽總管與主胰管共同開口處。",
            "B": "十二指腸下降段內側壁有大十二指腸乳頭，膽總管與主胰管共同開口於此，故正確。",
            "C": "十二指腸水平段位於較遠端，與 SMA/SMV 前方通過等解剖關係較相關，沒有主要膽胰管開口。",
            "D": "十二指腸上升段接近十二指腸空腸曲與 Treitz ligament，不是肝胰壺腹開口處。",
        },
        "core": "膽總管與主胰管共同開口於十二指腸下降段的大十二指腸乳頭。",
    },
    19: {
        "analysis": "腹股溝管有兩個環口：深環是腹橫筋膜的開口，淺環是腹外斜肌腱膜的開口。深環位於腹壁下動脈外側，是間接腹股溝疝的入口。",
        "notes": {
            "A": "腹股溝深環是 transversalis fascia 向外形成的開口，精索或子宮圓韌帶由此進入腹股溝管，故正確。",
            "B": "腹內斜肌參與腹股溝管上壁與部分精索包被，但不形成深環。",
            "C": "腹外斜肌腱膜形成的是腹股溝淺環，不是深環。",
            "D": "腹橫肌腱膜可參與聯合腱與腹股溝管後壁補強，但不是深環所在層。",
        },
        "core": "腹股溝深環在腹橫筋膜；腹股溝淺環在腹外斜肌腱膜。",
    },
    20: {
        "analysis": "胰頭與十二指腸血供形成前腸與中腸的吻合。上胰十二指腸動脈來自胃十二指腸動脈，屬腹腔幹系統；下胰十二指腸動脈來自上腸繫膜動脈。",
        "notes": {
            "A": "前上胰十二指腸動脈來自胃十二指腸動脈，屬腹腔幹系統，不是 SMA 直接分支。",
            "B": "後上胰十二指腸動脈同樣來自胃十二指腸動脈，不是 SMA 分支。",
            "C": "左結腸動脈是下腸繫膜動脈分支，供應降結腸等後腸相關區域。",
            "D": "下胰十二指腸動脈由上腸繫膜動脈發出，並與上胰十二指腸動脈形成吻合，故正確。",
        },
        "core": "SMA 分支包含 inferior pancreaticoduodenal artery；superior pancreaticoduodenal arteries 來自 GDA。",
    },
}


def make_update(question, item):
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
    return {
        "question_id": question["id"],
        "question_number": question["question_number"],
        "explanation": explanation,
        "key_point": item["core"],
        "flashcard_front": question["question_text"].replace("\n", " ")[:80],
        "flashcard_back": item["core"],
        "flashcard_summary": item["core"],
        "review_status": "ai_generated",
        "explanation_model": "codex-high-quality-rewrite",
        "explanation_generated_at": STAMP,
        "manual_review_notes": [],
    }


def main():
    exam = json.loads(Path(SOURCE_FILE).read_text(encoding="utf-8"))
    questions = {q["question_number"]: q for q in exam["questions"]}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    updates = [make_update(questions[qnum], QDATA[qnum]) for qnum in [6, 13, 18, 19, 20]]
    payload = {
        "source_file": SOURCE_FILE,
        "dataset_id": DATASET_ID,
        "range": {"start": 6, "end": 20},
        "updates": updates,
    }
    out = OUT_DIR / "q006-q020-repair.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
