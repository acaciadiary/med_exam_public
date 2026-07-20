import json
from pathlib import Path

def main():
    source_file = Path("public/data/exams/108-2/medicine-2.json")
    if not source_file.exists():
        print(f"Error: {source_file} not found.")
        return

    with open(source_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = data.get("questions", [])
    q_dict = {q["question_number"]: q for q in questions}

    # 指定題號
    target_numbers = [
        1, 2, 3, 4, 5, 6,
        8, 9, 10, 11, 12,
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
        26, 27, 28,
        30, 39, 47, 53,
        58, 59,
        61, 62,
        65, 66, 67,
        71, 72,
        74,
        78, 79, 80, 81,
        83, 84, 85, 86,
        88, 90, 95
    ]

    # 確認題數
    print(f"Total target numbers: {len(target_numbers)}")

    # 劃分批次
    batches = [
        # Batch 1: 1-10 內的指定題 (9 題)
        [1, 2, 3, 4, 5, 6, 8, 9, 10],
        # Batch 2: 11-20 內的指定題 (9 題)
        [11, 12, 14, 15, 16, 17, 18, 19, 20],
        # Batch 3: 21-30 內的指定題 (8 題)
        [21, 22, 23, 24, 26, 27, 28, 30],
        # Batch 4: 31-60 內的指定題 (5 題)
        [39, 47, 53, 58, 59],
        # Batch 5: 61-80 內的指定題 (11 題)
        [61, 62, 65, 66, 67, 71, 72, 74, 78, 79, 80],
        # Batch 6: 81 之後的指定題 (8 題)
        [81, 83, 84, 85, 86, 88, 90, 95]
    ]

    # 檢查是否有漏掉
    flattened_batches = [num for b in batches for num in b]
    # 去重
    unique_flattened = sorted(list(set(flattened_batches)))
    sorted_targets = sorted(target_numbers)
    if unique_flattened != sorted_targets:
        print("Warning: batch split mismatch!")
        print("Missing:", set(sorted_targets) - set(unique_flattened))
        print("Extra:", set(unique_flattened) - set(sorted_targets))

    output_dir = Path("scratch/tasks/108-2_medicine-2")
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, b_nums in enumerate(batches, 1):
        batch_questions = []
        for num in b_nums:
            if num in q_dict:
                q = q_dict[num]
                batch_questions.append({
                    "id": q["id"],
                    "question_number": q["question_number"],
                    "question_text": q["question_text"],
                    "options": q["options"],
                    "correct_answer": q["correct_answer"],
                    "category": q.get("category", ""),
                    "original_explanation": q.get("explanation", "")
                })
            else:
                print(f"Warning: question {num} not found in json.")

        batch_data = {
            "source_file": "public/data/exams/108-2/medicine-2.json",
            "dataset_id": "108-2_medicine-2",
            "batch_id": i,
            "questions": batch_questions
        }

        out_path = output_dir / f"batch_{i}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(batch_data, f, ensure_ascii=False, indent=2)
        print(f"Batch {i} written to {out_path} with {len(batch_questions)} questions.")

if __name__ == "__main__":
    main()
