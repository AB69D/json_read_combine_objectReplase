import json

with open(r"C:\Users\ab9d\Downloads\sampleJson\test\combined_json.json", "r") as f:
    data = json.load(f)

print(data)