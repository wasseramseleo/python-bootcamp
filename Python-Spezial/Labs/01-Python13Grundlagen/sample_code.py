"""--------------1-------------------"""
# Basic assignment (Dynamic Typing)
species_name = "Parus major"  # Kohlmeise
wing_length_mm = 74.5
is_migratory = False

# Type Hinting (Modern Standard)
ring_number: str = "AX-92831"
body_mass_g: float = 18.2

"""--------------2-------------------"""
# List: Mutable collection of daily captures
captured_birds = ["Blaumeise", "Kohlmeise", "Rotkehlchen"]
captured_birds.append("Amsel")  # List can grow

# Tuple: Immutable capture site coordinates (Lat, Lon)
site_coords = (48.2082, 16.3738)
site_coords[0] = 49.000  # TypeError

"""--------------3-------------------"""
# Dictionary representing a single bird's biometric record
bird_record = {
    "ring_id": "H77-201",
    "species": "Erithacus rubecula",  # Rotkehlchen
    "fat_score": 3,
    "wing_length": 72.0
}

# Accessing data efficiently
print(f"Fat Score: {bird_record['fat_score']}")

"""---------------4------------------"""
daily_weights = [18.5, 19.2, 17.8, 21.0]

for weight in daily_weights:
  if weight > 20.0:
    status = "High reserves"
  elif weight < 18.0:
    status = "Underweight"
  else:
    status = "Normal"

  # Logic to log status...

"""---------------5------------------"""
raw_data = [18.5, 19.2, 17.8, 21.0]

# List Comprehension: Convert all to integers (rounding down)
int_weights = [int(w) for w in raw_data]

# Generator Expression: Memory efficient for large datasets
# Calculates potential energy only when iterated over
energy_gen = (w * 0.5 for w in raw_data)

def process_bird(ring: str) -> bool:
    """Validates ring format."""
    return len(ring) == 6

