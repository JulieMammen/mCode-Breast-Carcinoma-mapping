# scripts/mapping_api.py
import pandas as pd
import json
import os

print("✅ Starting mapping_api.py ...")

# Load CSV
csv_path = "mcode/encode.idc_DUMMY_DATA/IDC_dummy_data.csv"
if not os.path.exists(csv_path):
    print(f"❌ File not found: {csv_path}")
else:
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows from {csv_path}")
    print("\n--- First 5 Rows ---")
    print(df.head())
