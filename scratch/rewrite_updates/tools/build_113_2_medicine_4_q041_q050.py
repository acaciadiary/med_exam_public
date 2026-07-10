import json
from pathlib import Path


source = Path("public/data/exams/113-2/medicine-4.json")
data = json.loads(source.read_text(encoding="utf-8"))
out = Path("scratch/rewrite_updates/113-2_medicine-4/q041-q050.json")
out.parent.mkdir(parents=True, exist_ok=True)

manual = {
    43: [
        "本題選項 B 與 D 皆有疑義：SWS 癲癇比例高，且現代分子病因為 GNAQ 體細胞突變而非 EPHB4；來源答案欄仍維持 B。"
    ]
}

rewrites = {
    43: """【題幹解析】
Sturge-Weber syndrome 是臉部葡萄酒色斑、同側軟腦膜血管畸形與眼部青光眼構成的神經皮膚症候群。題目要找不正確敘述；B 說癲癇機率不高，與 SWS 常見嬰幼兒期癲癇的臨床事實相反，因此可作為答案。另需注意 D 的基因敘述在現代分子醫學也有問題，SWS 典型為 GNAQ 體細胞嵌合突變，不是 EPHB4。

【選項詳解】
- A. 血管病變常發生在單側臉部三叉神經第一分枝支配的皮膚區域：正確。SWS 的臉部葡萄酒色斑常位於三叉神經 V1 支配區，尤其眼周與額部病灶較提示合併顱內軟腦膜血管畸形風險。
- B. 病人伴有癲癇症的機率不高：錯誤。SWS 的顱內軟腦膜血管畸形會造成皮質缺血、鈣化與神經發育受損，癲癇相當常見，常在嬰幼兒期發作，且可能頑固難治。
- C. 單側眼周皮膚發生血管病變時，此眼後續發生青光眼的機率很高：正確。V1 及眼瞼周圍葡萄酒色斑與同側青光眼風險增加有關，需眼科追蹤眼壓與視神經狀態。
- D. 發生突變的基因是 EPHB4：此敘述也有疑義。Sturge-Weber syndrome 目前主要與 GNAQ 體細胞活化突變有關；EPHB4 較常連結於毛細血管畸形-動靜脈畸形症候群，並非 SWS 的典型致病基因。

【核心考點】
Sturge-Weber syndrome 的高產考點是 V1 區葡萄酒色斑、同側軟腦膜血管畸形、癲癇、青光眼與 GNAQ 體細胞突變；看到「癲癇機率不高」或「EPHB4 為致病基因」都要提高警覺。"""
}

updates = []
for q in data["questions"][40:50]:
    n = q["question_number"]
    expl = rewrites.get(n, q["explanation"])
    updates.append(
        {
            "question_id": q["id"],
            "question_number": n,
            "explanation": expl,
            "key_point": (
                "Sturge-Weber syndrome 常見 V1 區葡萄酒色斑、同側軟腦膜血管畸形、癲癇與青光眼；典型分子病因為 GNAQ 體細胞突變。"
                if n == 43
                else q.get("key_point", "")
            ),
            "flashcard_front": (
                "Sturge-Weber syndrome 的典型表現與基因？"
                if n == 43
                else q.get("flashcard_front", "")
            ),
            "flashcard_back": (
                "V1 區葡萄酒色斑、同側軟腦膜血管畸形、癲癇、青光眼；典型為 GNAQ 體細胞突變，非 EPHB4。"
                if n == 43
                else q.get("flashcard_back", "")
            ),
            "flashcard_summary": (
                "Sturge-Weber syndrome -> V1 葡萄酒色斑、癲癇、青光眼、GNAQ 體細胞突變。"
                if n == 43
                else q.get("flashcard_summary", "")
            ),
            "review_status": "ai_generated",
            "explanation_model": "codex-high-quality-rewrite",
            "explanation_generated_at": "2026-07-09T14:00:00+08:00",
            "manual_review_notes": manual.get(n, []),
        }
    )

payload = {
    "source_file": "public/data/exams/113-2/medicine-4.json",
    "dataset_id": "113-2_medicine-4",
    "range": {"start": 41, "end": 50},
    "updates": updates,
}

out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
