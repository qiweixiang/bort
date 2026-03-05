import json

with open(f"./mysession/user_oo1.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
