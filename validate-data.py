import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"

files = {
    "properties": "properties.csv",
    "residents": "residents.csv",
    "units": "units.csv",
    "occupancy": "occupancy_snapshots.csv",
    "services": "services.csv",
    "payments": "payments.csv",
}

print("DATA QUALITY CHECKS")
print("-" * 50)

for name, file in files.items():
    df = pd.read_csv(DATA / file)
    print(f"{name}: {len(df):,} rows | {df.isna().sum().sum()} null values")

residents = pd.read_csv(DATA / "residents.csv")
payments = pd.read_csv(DATA / "payments.csv")
services = pd.read_csv(DATA / "services.csv")

print("\nDuplicate resident IDs:", residents.resident_id.duplicated().sum())
print("Duplicate payment IDs:", payments.payment_id.duplicated().sum())
print("Duplicate service IDs:", services.service_id.duplicated().sum())

print("\nValidation complete.")
