import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"

occ = pd.read_csv(DATA / "occupancy_snapshots.csv")
res = pd.read_csv(DATA / "residents.csv")
svc = pd.read_csv(DATA / "services.csv")
pay = pd.read_csv(DATA / "payments.csv")

print("SENIOR LIVING ANALYTICS KPIs")
print("=" * 50)

latest = occ["snapshot_date"].max()
latest_occ = occ[occ["snapshot_date"] == latest]

print(f"Latest occupancy snapshot: {latest}")
print(f"Overall occupancy: {latest_occ.occupied_units.sum()/latest_occ.total_units.sum()*100:.1f}%")
print(f"Occupied units: {latest_occ.occupied_units.sum():,}")
print(f"Available units: {latest_occ.available_units.sum():,}")

print("\nAverage resident age:", round(res.age.mean(), 1))

print("\nService cost by type:")
print(svc.groupby("service_type")["cost_inr"].sum().sort_values(ascending=False))

print("\nPayment summary:")
print(pay.groupby("payment_status")["amount_inr"].agg(["count","sum"]))

print("\nOccupancy by city/property:")
properties = pd.read_csv(DATA / "properties.csv")
summary = latest_occ.merge(properties[["property_id","property_name","city"]], on="property_id")
summary["occupancy_pct"] = summary.occupied_units / summary.total_units * 100
print(summary[["property_name","city","occupancy_pct"]].sort_values("occupancy_pct", ascending=False).to_string(index=False))
