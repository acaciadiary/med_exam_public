import json
from pathlib import Path


base = Path("scratch/rewrite_updates/113-2_medicine-4")
notes = {
    "q011-q020.json": {
        11: [
            "官方更正為 B、C、D 均給分；膽囊積水最典型關聯仍為 Kawasaki disease，題目問法與選項造成爭議。"
        ],
        17: [
            "官方更正為 C、D 均給分；D 的少關節炎型定義同時錯在前 6 週與小於等於 5 個關節。"
        ],
        18: [
            "官方更正為 C、D 均給分；Ewing sarcoma 好發骨幹或骨幹骺交界，長骨幹骺端較支持 osteosarcoma。"
        ],
    },
    "q021-q030.json": {
        27: [
            "官方更正為 B、D 均給分；若氣管擴張劑指 nebulized epinephrine 可用於哮吼急性緩解，若指一般 beta-2 agonist 則不適用。"
        ]
    },
    "q031-q040.json": {
        32: [
            "官方更正為 A、C 均給分；兒科多數情境心搏過速是代償性休克早期表現，低血壓多代表代償失敗，但選項 A 仍被官方接受。"
        ]
    },
}

for filename, by_question in notes.items():
    path = base / filename
    payload = json.loads(path.read_text(encoding="utf-8"))
    for update in payload["updates"]:
        qn = update["question_number"]
        if qn in by_question:
            update["manual_review_notes"] = by_question[qn]
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
