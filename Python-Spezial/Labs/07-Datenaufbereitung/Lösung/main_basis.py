import pandas as pd


def clean_and_merge():
    # 1. Load Data
    tx_df = pd.read_csv('transactions_dirty.csv')
    cust_df = pd.read_csv('customers.csv')

    print("--- Missing Values vor Bereinigung ---")
    print(tx_df.isna().sum())

    # 2. Cleaning
    # Wir füllen NaNs im Betrag mit 0, um Berechnungen nicht zu verfälschen
    tx_df['amount'] = tx_df['amount'].fillna(0.0)

    # 3. Merge (Left Join)
    # Transaktionen sind die Basis (links), Kundendaten werden angereichert (rechts)
    merged_df = pd.merge(tx_df, cust_df, on='account_id', how='left')

    print("\n--- Merge Ergebnis (Auszug) ---")
    print(merged_df.head())

    # Check auf "Verwaiste" Transaktionen (wo Customer NaN ist)
    orphans = merged_df[merged_df['name'].isna()]
    if not orphans.empty:
        print(f"\nWarnung: {len(orphans)} Transaktionen ohne Kunden-Match gefunden!")

    # 4. Aggregation
    print("\n--- Summe pro Region ---")
    # groupby ignoriert automatisch NaNs in der Gruppierungs-Spalte (hier 'region')
    report = merged_df.groupby('region')['amount'].sum()
    print(report)

    return merged_df  # Rückgabe für Teil 2


if __name__ == "__main__":
    df_result = clean_and_merge()
