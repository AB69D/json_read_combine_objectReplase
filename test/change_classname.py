import json

def change_class_names(data):
  for object in data:
    if object["classTitle"] == "vehicle":
      object["classTitle"] = "car"
    if object["classTitle"] == "license plate":
      object["classTitle"] = "number"

if __name__ == "__main__":
  with open(r"C:\Users\ab9d\Downloads\sampleJson\test\combined_json.json", "r") as f:
    data = json.load(f)

  change_class_names(data)

  with open(r"C:\Users\ab9d\Downloads\sampleJson\test\combined_json.json", "w") as f:
    json.dump(data, f, indent=4)