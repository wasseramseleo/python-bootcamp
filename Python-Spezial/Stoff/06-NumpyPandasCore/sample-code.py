"""--------------1-------------------"""
import numpy as np

# List of wing lengths (mm)
wings_list = [74.5, 72.1, 78.0, 69.5]

# Convert to Numpy Array
wings_arr = np.array(wings_list)

# Vectorized operation: Convert all to cm instantly
# No loop needed!
wings_cm = wings_arr / 10.0

print(f"Mean Wing Length: {wings_arr.mean()} mm")

"""--------------2-------------------"""
import pandas as pd

# Data representing a single ringing session
data = {
    "ring_id": ["AX-01", "AX-02", "AX-03"],
    "species": ["Rotkehlchen", "Amsel", "Rotkehlchen"],
    "weight_g": [17.5, 98.2, 18.1]
}

# Create DataFrame
df = pd.read_csv("capture_data.csv") # Or from dict above
# df = pd.DataFrame(data)

print(df.info()) # Shows data types and missing values

"""--------------3-------------------"""
# Select single column (Returns a Series)
species_col = df['species']

# Boolean Indexing (Filter rows)
# Get all birds heavier than 20g
heavy_birds = df[df['weight_g'] > 20.0]

# Combine Logic
robins = df[(df['species'] == 'Rotkehlchen') & (df['weight_g'] > 18.0)]

"""--------------4-------------------"""
import time

# BAD: Looping (Slow)
start = time.time()
for index, row in df.iterrows():
    df.at[index, 'bmi'] = row['weight_g'] / row['wing_len']
print(f"Loop time: {time.time() - start}")

# GOOD: Vectorization (Fast)
start = time.time()
df['bmi'] = df['weight_g'] / df['wing_len']
print(f"Vector time: {time.time() - start}")

"""--------------5-------------------"""
# Lab Starter
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("materials/migration_data.csv")

# Hint for Task 3
# Ensure date column is actually datetime type first!
df['date'] = pd.to_datetime(df['date'])

