import pandas as pd
from datetime import datetime
import os

# === CONFIG ===
input_file = "Sample_Data.csv" # <------ INPUT FILE!!
timestamp_col = "timestamp"
deployment_col = "deployment_id"

# === LOAD DATA ===
df = pd.read_csv(input_file)

# Convert timestamp column to datetime
df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')

# === FUNCTION TO PARSE DATE FROM deployment_id ===
def extract_date_from_deployment(deployment_string):
    try:
        date_str = deployment_string[:10]
        return datetime.strptime(date_str, "%m-%d-%Y").date()
    except:
        return None

# === FIX TIMESTAMPS (ONLY IF YEARS MISMATCH) ===
corrected_timestamps = []

for index, row in df.iterrows():
    original_ts = row[timestamp_col]
    deployment_date = extract_date_from_deployment(row[deployment_col])

    if pd.notnull(original_ts) and deployment_date is not None:
        if original_ts.year != deployment_date.year:
            # Only change date if year differs
            new_ts = datetime.combine(deployment_date, original_ts.time())
            corrected_timestamps.append(new_ts)
        else:
            corrected_timestamps.append(original_ts)
    else:
        corrected_timestamps.append(original_ts)

# Apply changes
df[timestamp_col] = corrected_timestamps

# === SAVE TO CLEANED FILE ===
file_root, file_ext = os.path.splitext(input_file)
output_file = f"{file_root}_CLEANED{file_ext}"
df.to_csv(output_file, index=False)

print(f"✅ Cleaned file saved as: {output_file}")
