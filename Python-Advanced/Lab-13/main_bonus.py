import pandas as pd

try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    print("Fehler: transactions.csv nicht gefunden.")
    exit()


mask_completed = (df['status'] == 'COMPLETED')
df_completed = df[mask_completed]

try:
  df = pd.read_csv("transactions.csv")
  df_completed = df[df['status'] == 'COMPLETED']
except FileNotFoundError:
  print("Fehler: transactions.csv nicht gefunden.")
  exit()

print("\n--- Bonus-Herausforderung ---")

# 1. Multi-Level Grouping
print("\n--- 1. Multi-Level Grouping (Konto & Typ) ---")
multi_level_summary = df_completed.groupby(['account_id', 'transaction_type'])['amount'].sum()
print(multi_level_summary)

# 2. Komplexe Aggregation (.agg())
print("\n--- 2. Aggregation (Details pro Typ) ---")
type_summary = df_completed.groupby('transaction_type')['amount'].agg(
  ['count', 'sum', 'mean', 'max']
)
print(type_summary)

# 3. Fehleranalyse (Höchste fehlgeschlagene Transaktion)
print("\n--- 3. Fehleranalyse (Höchste FAILED Tx) ---")

# Filtern nach FAILED
df_failed = df[df['status'] == 'FAILED']

if not df_failed.empty:
  # Finde den INDEX der Zeile mit dem max. Betrag
  idx_max_failed = df_failed['amount'].idxmax()

  # .loc verwenden, um die gesamte Zeile anhand ihres Index zu holen
  highest_failed_tx = df.loc[idx_max_failed]

  print("Transaktion mit höchstem FAILED-Betrag:")
  print(highest_failed_tx)
else:
  print("Keine FAILED-Transaktionen gefunden.")