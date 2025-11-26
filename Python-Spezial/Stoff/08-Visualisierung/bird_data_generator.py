import pandas as pd
import numpy as np
import random
from datetime import date, timedelta

# --- Configuration ---
YEARS = [2024, 2025]
START_MONTH = 8
START_DAY = 1
END_MONTH = 10
END_DAY = 31

# Species DB for realistic filler data (reused from previous steps)
SPECIES_DB = {
  "Kohlmeise": {"w_mu": 75, "w_sigma": 2, "mass_mu": 18, "mass_sigma": 1.5},
  "Blaumeise": {"w_mu": 62, "w_sigma": 1.5, "mass_mu": 11, "mass_sigma": 1},
  "Amsel": {"w_mu": 128, "w_sigma": 4, "mass_mu": 95, "mass_sigma": 8},
}


def get_base_migration_potential(d: date) -> int:
  """Returns theoretical migration volume based on season."""
  if d.month == 8:
    return int(np.random.normal(10, 3))
  elif d.month == 9:
    return int(np.random.normal(25, 5)) if d.day <= 15 else int(np.random.normal(80, 15))
  elif d.month == 10:
    return int(np.random.normal(90, 20)) if d.day <= 15 else int(np.random.normal(30, 8))
  return 0


def generate_data():
  records = []

  for year in YEARS:
    current_date = date(year, START_MONTH, START_DAY)
    end_date = date(year, END_MONTH, END_DAY)
    accumulated_birds = 0

    while current_date <= end_date:
      base_potential = get_base_migration_potential(current_date)

      # Weather simulation (Rain stops migration -> Dam Effect)
      is_bad_weather = random.random() < 0.20

      if is_bad_weather:
        daily_count = 0
        accumulated_birds += base_potential
      else:
        daily_count = int((base_potential + accumulated_birds) * np.random.uniform(0.9, 1.1))
        accumulated_birds = 0

      daily_count = max(0, daily_count)

      for _ in range(daily_count):
        sp = random.choice(list(SPECIES_DB.keys()))
        conf = SPECIES_DB[sp]

        sex = random.choice(['M', 'F', 'U'])

        # --- SEXUAL DIMORPHISM LOGIC ---
        # Males generally have slightly longer wings (~1-2mm difference in passerines)
        w_mu_adjusted = conf["w_mu"]
        if sex == 'M':
          w_mu_adjusted += 1.5
        elif sex == 'F':
          w_mu_adjusted -= 1.5

        wing = np.random.normal(w_mu_adjusted, conf["w_sigma"])
        weight = np.random.normal(conf["mass_mu"], conf["mass_sigma"])

        records.append({
          "ring_id": f"AX-{random.randint(10000, 99999)}",
          "species": sp,
          "wing_length_mm": round(wing, 1),
          "weight_g": round(weight, 1),
          "fat_score": random.randint(0, 5),
          "date": current_date.strftime("%Y-%m-%d"),
          "sex": sex
        })

      current_date += timedelta(days=1)

  df = pd.DataFrame(records).sort_values("date")
  filename = "clean_ringing_data_phenology.csv"
  df.to_csv(filename, index=False)
  print(f"Generated {filename} with {len(df)} captures.")


if __name__ == "__main__":
  generate_data()