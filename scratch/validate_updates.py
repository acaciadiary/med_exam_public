import json
import os

out_path = "d:\\Antigravity\\med_exam_public\\scratch\\rewrite_updates\\110-1_medicine-6\\q051-q060.json"

if not os.path.exists(out_path):
    print("Error: File does not exist")
    exit(1)

with open(out_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check basic structure
assert "source_file" in data, "source_file missing"
assert "dataset_id" in data, "dataset_id missing"
assert "range" in data, "range missing"
assert "updates" in data, "updates missing"

assert data["source_file"] == "public/data/exams/110-1/medicine-6.json"
assert data["dataset_id"] == "110-1_medicine-6"
assert data["range"] == {"start": 51, "end": 60}
assert len(data["updates"]) == 10, f"Expected 10 updates, got {len(data['updates'])}"

banned_phrases = [
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "題目中選項 A 所代表的鑑別或處置",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "此選項不是最佳答案",
    "與正確答案的關鍵判斷點不一致",
    "原始解析重點指出",
    "熟悉疾病機轉、臨床表現、診斷檢查與治療原則"
]

required_fields = {
    "question_id",
    "question_number",
    "explanation",
    "key_point",
    "flashcard_front",
    "flashcard_back",
    "flashcard_summary",
    "review_status",
    "explanation_model",
    "explanation_generated_at",
    "manual_review_notes"
}

for i, up in enumerate(data["updates"]):
    q_num = up["question_number"]
    assert 51 <= q_num <= 60, f"Question number {q_num} out of bounds"
    
    # Check fields
    actual_fields = set(up.keys())
    missing_fields = required_fields - actual_fields
    extra_fields = actual_fields - required_fields
    assert not missing_fields, f"Q{q_num} missing fields: {missing_fields}"
    assert not extra_fields, f"Q{q_num} has unexpected fields: {extra_fields}"
    
    # Check headings in explanation
    exp = up["explanation"]
    assert "【題幹解析】" in exp, f"Q{q_num} missing 【題幹解析】"
    assert "【選項詳解】" in exp, f"Q{q_num} missing 【選項詳解】"
    assert "【核心考點】" in exp, f"Q{q_num} missing 【核心考點】"
    
    # Check banned phrases
    for phrase in banned_phrases:
        assert phrase not in exp, f"Q{q_num} explanation contains banned phrase: '{phrase}'"
        
    # Check metadata fields
    assert up["review_status"] == "ai_generated"
    assert up["explanation_model"] == "antigravity-subagent"
    assert up["manual_review_notes"] == []

print("Validation PASSED! The updates JSON complies fully with the contract.")
