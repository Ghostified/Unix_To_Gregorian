import json
from datetime import datetime
import re

# Input/output file names
input_file = "tickets_29.json"
output_file = "converted_29.json"

# Step 1: Load JSON
try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"✅ Loaded JSON file with {len(data)} entries.")
except Exception as e:
    print("❌ Failed to read JSON:", e)
    exit()

# Step 2: Function to clean and convert UNIX timestamps
def convert_unix(value):
    try:
        match = re.search(r"\d{10,13}", str(value))
        if not match:
            return value  # If no timestamp found, keep original
        ts = int(match.group())
        if ts > 1e12:
            ts = ts // 1000
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return value

# Step 3: Apply conversion to each entry in JSON
for item in data:
    if "Created_date" in item:
        item["Created_date"] = convert_unix(item["Created_date"])

# Step 4: Save converted data
try:
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ Converted JSON written to: {output_file}")
except Exception as e:
    print("❌ Failed to write output file:", e)
