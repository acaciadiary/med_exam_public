import json
from pathlib import Path


source = Path("public/data/exams/113-2/medicine-4.json")
data = json.loads(source.read_text(encoding="utf-8"))
q = data["questions"][75]
out = Path("scratch/rewrite_updates/113-2_medicine-4/repair_q076.json")

explanation = """【題幹解析】
本題來源欄位有明顯混題：question_text 前段是壞死性筋膜炎影像題，後段又混入第 77 題兒童維持輸液題幹；options 欄位則顯示 35、45、55、65，屬於第 77 題的數字選項。因本次工作嚴禁修改題目、選項與答案欄位，詳解只能依 question_text 中完整可見的壞死性筋膜炎 A-D 敘述來說明官方答案 B 的理由，同時標記人工複核。壞死性筋膜炎影像上常見深層筋膜增厚、筋膜平面積液與軟組織氣體；已壞死筋膜因缺乏血流，增強 CT/MRI 通常呈不顯影，而不是顯影後代表壞死。

【選項詳解】
- A. 35：若只看 options 欄位，35 是第 77 題輸液計算的數字，與第 76 題壞死性筋膜炎影像無法醫學對應。若依 question_text 內嵌的 A「沿著筋膜平面上有液體積存」判讀，筋膜平面積液是壞死性筋膜炎常見影像表現，因此不是錯誤敘述。
- B. 45：若只看 options 欄位，45 也是第 77 題的數字選項，與第 76 題影像題不相符。若依 question_text 內嵌的 B「如果筋膜可以被顯影劑顯現代表已經壞死」判讀，這句是錯的；壞死組織缺乏灌流，增強掃描多呈 non-enhancement，可顯影反而代表仍有血流或發炎反應，因此官方答案 B 可由內嵌選項支持。
- C. 55：若只看 options 欄位，55 是輸液題數字，不能用來判斷壞死性筋膜炎。若依 question_text 內嵌的 C「皮下或軟組織內有氣體積存」判讀，產氣菌或混合感染可造成皮下氣體，這是壞死性筋膜炎的重要影像警訊。
- D. 65：若只看 options 欄位，65 對應第 77 題輸液計算，與第 76 題不一致。若依 question_text 內嵌的 D「深層筋膜厚度增加」判讀，深層筋膜增厚是嚴重發炎、水腫與感染擴散的影像表現，屬壞死性筋膜炎可見特徵。

【核心考點】
壞死性筋膜炎的影像判讀重點是深層筋膜增厚、筋膜積液、軟組織氣體與壞死筋膜不顯影；但本題來源 options 與 question_text 不一致，正式教學或上線前應人工回查原始考卷，修正題目/選項資料後再完全定稿。"""

payload = {
    "source_file": "public/data/exams/113-2/medicine-4.json",
    "dataset_id": "113-2_medicine-4",
    "range": {"start": 76, "end": 76},
    "updates": [
        {
            "question_id": q["id"],
            "question_number": 76,
            "explanation": explanation,
            "key_point": "壞死性筋膜炎影像常見深層筋膜增厚、筋膜積液與軟組織氣體；壞死筋膜因缺乏血流在增強掃描上通常不顯影。本題來源題幹與選項混題，需人工回查。",
            "flashcard_front": "壞死性筋膜炎影像表現與增強掃描判讀？",
            "flashcard_back": "常見深層筋膜增厚、筋膜平面積液、軟組織氣體；已壞死筋膜缺乏血流，增強 CT/MRI 多呈不顯影。",
            "flashcard_summary": "壞死性筋膜炎影像 -> 筋膜增厚/積液/氣體；壞死筋膜 non-enhancing。本題來源欄位混題需人工回查。",
            "review_status": "ai_generated",
            "explanation_model": "codex-high-quality-rewrite",
            "explanation_generated_at": "2026-07-09T14:00:00+08:00",
            "manual_review_notes": [
                "來源資料欄位疑似混入第 77 題：question_text 內含壞死性筋膜炎題目與第 77 題題幹，options 欄位則為 35/45/55/65；本 repair 未修改題目、選項或答案，只在詳解中明確標示限制並依 question_text 內嵌 A-D 解析。"
            ],
        }
    ],
}

out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
