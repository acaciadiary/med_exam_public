import json

def validate():
    file_path = "scratch/rewrite_updates/114-2_medicine-5/q001-q010.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert data["source_file"] == "public/data/exams/114-2/medicine-5.json", "source_file mismatch"
    assert data["dataset_id"] == "114-2_medicine-5", "dataset_id mismatch"
    assert data["range"] == {"start": 1, "end": 10}, "range mismatch"
    assert len(data["updates"]) == 10, "updates count mismatch"
    
    required_fields = {
        "question_id", "question_number", "explanation", "key_point",
        "flashcard_front", "flashcard_back", "flashcard_summary",
        "review_status", "explanation_model", "explanation_generated_at",
        "manual_review_notes"
    }
    
    banned_phrases = [
        "非本題答案", "不是本題標準答案", "回到題幹線索", "請用題幹線索連回",
        "不能最精準回答本題", "最符合題幹", "核心記憶點", "定義、機轉、典型表現或處置原則",
        "此選項不是最佳答案", "與正確答案的關鍵判斷點不一致", "原始解析重點指出",
        "題目中選項 A 所代表的鑑別或處置"
    ]
    
    for idx, item in enumerate(data["updates"]):
        fields = set(item.keys())
        extra = fields - required_fields
        missing = required_fields - fields
        if extra:
            print(f"Q{idx+1} extra fields: {extra}")
        if missing:
            print(f"Q{idx+1} missing fields: {missing}")
        assert fields == required_fields, f"Fields mismatch for Q{idx+1}"
        
        q_num = item["question_number"]
        assert q_num == idx + 1, f"Expected question_number {idx+1}, got {q_num}"
        expected_id = f"114-2_medicine-5_{q_num:03d}"
        assert item["question_id"] == expected_id, f"Expected ID {expected_id}, got {item['question_id']}"
        
        explanation = item["explanation"]
        
        # Check headings
        for heading in ["【題幹解析】", "【選項詳解】", "【核心考點】"]:
            assert heading in explanation, f"Heading {heading} missing in Q{q_num}"
        
        # Check options
        for opt in ["- A.", "- B.", "- C.", "- D."]:
            assert opt in explanation, f"Option marker {opt} missing in Q{q_num}"
            
        # Check for banned phrases
        for phrase in banned_phrases:
            if phrase in explanation:
                print(f"BANNED PHRASE \"{phrase}\" found in Q{q_num}!")
                raise ValueError(f"Banned phrase \"{phrase}\" found in Q{q_num}")
                
        print(f"Q{q_num} validation passed.")
        
    print("\n--- All validation checks passed successfully! ---")

if __name__ == "__main__":
    validate()
