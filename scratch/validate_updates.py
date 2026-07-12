import json
import os

update_file = r"scratch/rewrite_updates/109-1_medicine-4/q051-q060.json"
source_file = r"public/data/exams/109-1/medicine-4.json"

try:
    with open(update_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("Success: JSON is valid.")
    
    # Check fields
    assert data.get("source_file") == "public/data/exams/109-1/medicine-4.json", "source_file mismatch"
    assert data.get("dataset_id") == "109-1_medicine-4", "dataset_id mismatch"
    assert data.get("range") == {"start": 51, "end": 60}, "range mismatch"
    assert isinstance(data.get("updates"), list), "updates is not a list"
    assert len(data["updates"]) == 10, f"Expected 10 updates, got {len(data['updates'])}"
    
    allowed_keys = {
        "question_id", "question_number", "explanation", "key_point",
        "flashcard_front", "flashcard_back", "flashcard_summary",
        "review_status", "explanation_model", "explanation_generated_at",
        "manual_review_notes"
    }
    
    # Load source to compare
    with open(source_file, "r", encoding="utf-8") as sf:
        source_data = json.load(sf)
    source_q_map = {q["id"]: q for q in source_data.get("questions", [])}
    
    for i, u in enumerate(data["updates"]):
        # Key validation
        keys = set(u.keys())
        extra_keys = keys - allowed_keys
        missing_keys = allowed_keys - keys
        assert not extra_keys, f"Extra keys in update {i}: {extra_keys}"
        assert not missing_keys, f"Missing keys in update {i}: {missing_keys}"
        
        # ID and number matching
        q_id = u["question_id"]
        q_num = u["question_number"]
        assert q_id in source_q_map, f"Question ID {q_id} not found in source"
        assert source_q_map[q_id]["question_number"] == q_num, f"Question number mismatch for {q_id}"
        
        # Format checks
        assert "【題幹解析】" in u["explanation"], f"Missing 【題幹解析】 in {q_id}"
        assert "【選項詳解】" in u["explanation"], f"Missing 【選項詳解】 in {q_id}"
        assert "【核心考點】" in u["explanation"], f"Missing 【核心考點】 in {q_id}"
        
        # Check flashcard_front for slash
        assert "/" not in u["flashcard_front"], f"Slash '/' found in flashcard_front of {q_id}"
        
        # Banned phrases check
        banned_phrases = [
            "非本題答案", "不是本題標準答案", "回到題幹線索", "請用題幹線索連回",
            "題目中選項 A 所代表的鑑別或處置", "不能最精準回答本題", "最符合題幹",
            "核心記憶點", "定義、機轉、典型表現或處置原則"
        ]
        for phrase in banned_phrases:
            assert phrase not in u["explanation"], f"Banned phrase '{phrase}' found in explanation of {q_id}"
            
        print(f"Q{q_num} ({q_id}): OK")
    print("All checks passed successfully!")
    
except Exception as e:
    print("Error:", e)
