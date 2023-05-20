import json
import os

def combine_json_files(folder_path):
  data = []
  for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
      with open(os.path.join(folder_path, file_name), "r") as f:
        data.append(json.load(f))

  with open("combined_json.json", "w") as f:
    json.dump(data, f, indent=4)

if __name__ == "__main__":
  folder_path = r"C:\Users\ab9d\Downloads\sampleJson\test\combine"
  combine_json_files(folder_path)