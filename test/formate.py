import json
import os

def convert_json_files(folder_path):
  for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
      with open(os.path.join(folder_path, file_name), "r") as f:
        data = json.load(f)

      with open(os.path.join(folder_path, "formatted_" + file_name), "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
  folder_path = r"C:\Users\ab9d\Downloads\sampleJson\test"
  convert_json_files(folder_path)
