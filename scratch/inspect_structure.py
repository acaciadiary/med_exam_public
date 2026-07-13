import json

with open("public/data/exams/110-2/medicine-2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Type of data:", type(data))
if isinstance(data, list):
    print("List length:", len(data))
    if len(data) > 0:
        print("First item keys:", data[0].keys())
elif isinstance(data, dict):
    print("Dict keys:", data.keys())
    if "questions" in data:
        print("Questions count:", len(data["questions"]))
        if len(data["questions"]) > 0:
            print("First question keys:", data["questions"][0].keys())
