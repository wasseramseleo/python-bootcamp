import pandas as pd
import numpy as np
import time


def performance_benchmark():
    df = pd.read_csv('big_transactions.csv')
    print(f"\nStarte Benchmark mit {len(df)} Zeilen...")

    # --- METHODE 1: Iterrows (Der "langsame" Weg) ---
    start_time = time.time()

    converted_amounts = []
    # iterrows ist bekanntermaßen langsam, da es Series-Objekte pro Zeile erstellt
    for index, row in df.iterrows():
        if row['currency'] == 'USD':
            converted_amounts.append(row['amount'] * 0.90)
        elif row['currency'] == 'GBP':
            converted_amounts.append(row['amount'] * 1.15)
        else:
            converted_amounts.append(row['amount'])

    df['amount_eur_loop'] = converted_amounts

    duration_loop = time.time() - start_time
    print(f"Dauer Loop: {duration_loop:.4f} Sekunden")

    # --- METHODE 2: Vektorisierung (Der "Pandas" Weg) ---
    start_time = time.time()

    # Bedingungen definieren
    conditions = [
        (df['currency'] == 'USD'),
        (df['currency'] == 'GBP')
    ]

    # Werte definieren, die bei True gewählt werden
    choices = [
        df['amount'] * 0.90,
        df['amount'] * 1.15
    ]

    # np.select(Bedingungen, Auswahl, Default)
    df['amount_eur_vec'] = np.select(conditions, choices, default=df['amount'])

    duration_vec = time.time() - start_time
    print(f"Dauer Vektor: {duration_vec:.4f} Sekunden")

    # --- FAZIT ---
    if duration_vec > 0:
        factor = duration_loop / duration_vec
        print(f"\n>>> Vektorisierung war {factor:.1f}x schneller! <<<")


if __name__ == "__main__":
    performance_benchmark()
