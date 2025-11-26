"""--------------1-------------------"""
# Reading raw field notes
log_file = "field_notes_2024.txt"

# The 'with' statement ensures the file closes safely
with open(log_file, mode='r', encoding='utf-8') as f:
    content = f.read()
    # File is open here

# File is automatically closed here
print(f"Read {len(content)} characters.")

"""--------------2-------------------"""
import csv

# Reading ringing data
with open('capture_data.csv', mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Access by column name, not index
        print(f"Bird ID: {row['Ring_ID']} - Weight: {row['Weight']}")

"""--------------3-------------------"""
import json

bird_data = {
    "species": "Ciconia ciconia", # Weißstorch
    "rings": ["H8812", "GPS-Tracker-09"],
    "measurements": {"bill": 180, "wing": 590}
}

# Serialization (Writing to disk)
with open('stork_data.json', 'w') as f:
    json.dump(bird_data, f, indent=4)

"""--------------4-------------------"""
from datetime import datetime, timedelta

raw_date = "2024-05-12 14:30:00"
# Parse string to object
capture_time = datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")

# Calculate release time (20 mins later)
release_time = capture_time + timedelta(minutes=20)

print(f"Release ISO: {release_time.isoformat()}")

"""--------------5-------------------"""
import re

notes = "Bird spotted with ring AX-9921 near the lake, maybe AX-9922 too."

# Pattern: 2 Letters, hyphen, 4 Digits
pattern = r"[A-Z]{2}-\d{4}"

found_rings = re.findall(pattern, notes)
# Result: ['AX-9921', 'AX-9922']

"""--------------6-------------------"""
# Lab Hint: Structure
data_list = []
with open('input.csv', 'r') as f_in:
    # Read data...
    # Transform data...
    pass

with open('output.json', 'w') as f_out:
    # Dump data...
    pass
