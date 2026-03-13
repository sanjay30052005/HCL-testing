
import json

try:
    with open("data.json") as f:
        data = json.load(f)
        print(data)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON format")
