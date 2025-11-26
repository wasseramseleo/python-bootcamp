import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Settings
np.random.seed(42)
num_records = 200
species_db = {
  "Kohlmeise": {"w_mu": 75, "w_sigma": 2, "mass_mu": 18, "mass_sigma": 1.5},
  "Blaumeise": {"w_mu": 62, "w_sigma": 1.5, "mass_mu": 11, "mass_sigma": 1},
  "Rotkehlchen": {"w_mu": 71, "w_sigma": 2, "mass_mu": 19, "mass_sigma": 1.5},
  "Amsel": {"w_mu": 128, "w_sigma": 4, "mass_mu": 95, "mass_sigma": 8},
  "Buchfink": {"w_mu": 85, "w_sigma": 3, "mass_mu": 21, "mass_sigma": 2}
}

data = []
start_date = datetime(2023, 1, 1)

for _ in range(num_records):
  # Select random species
  sp = random.choice(list(species_db.keys()))
  conf = species_db[sp]

  # Generate biometrics (correlated)
  wing = np.random.normal(conf["w_mu"], conf["w_sigma"])
  z_score = (wing - conf["w_mu"]) / conf["w_sigma"]
  weight = np.random.normal(conf["mass_mu"] + (z_score * 0.5), conf["mass_sigma"])

  # Meta data
  date_str = (start_date + timedelta(days=random.randint(0, 700))).strftime("%Y-%m-%d")

  data.append({
    "ring_id": f"AX-{random.randint(1000, 9999)}",
    "species": sp,
    "wing_length_mm": round(wing, 1),
    "weight_g": round(weight, 1),
    "fat_score": random.choices(range(6), weights=[1, 2, 3, 2, 1, 1])[0],
    "date": date_str,
    "sex": random.choice(['M', 'F', 'U'])
  })

df = pd.DataFrame(data)
df.to_csv("clean_ringing_data.csv", index=False)
df.to_csv("final_lab_data.csv", index=False)  # For Lab Starter
print("Files generated.")