import pandas as pd

print("--- Angabe Test ---")

# 1. Laden und Inspizieren
try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    print("Fehler: transactions.csv nicht gefunden.")
    exit()

print("--- 1. Inspektion (Head) ---")
print(df.head())

print("\n--- 1. Inspektion (Info) ---")
df.info()

print("\n--- 1. Inspektion (Describe) ---")
print(df.describe())


# 2. Datenbereinigung (Filtern)
# Erstelle eine Maske für 'COMPLETED' Status
mask_completed = (df['status'] == 'COMPLETED')
df_completed = df[mask_completed]

print(f"\n--- 2. Datenbereinigung ---")
print(f"Originale Einträge: {len(df)}, Bereinigte Einträge: {len(df_completed)}")


# 3. Selektion und Filterung (Masking)
print("\n--- 3. Filterung (DEPOSIT > 500) ---")
# Kombinierte Maske (anhand df_completed)
mask_deposits = (df_completed['transaction_type'] == 'DEPOSIT')
mask_high_value = (df_completed['amount'] > 500)

high_value_deposits = df_completed[mask_deposits & mask_high_value]
print(high_value_deposits)


# 4. Analyse (Groupby)
print("\n--- 4. Analyse (Summe pro Konto) ---")
# Split-Apply-Combine
account_totals = df_completed.groupby('account_id')['amount'].sum()
print(account_totals)