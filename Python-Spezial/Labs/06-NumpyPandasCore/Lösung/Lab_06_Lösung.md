# Lösung Lab 06

### Lösungsansatz

  * **Pandas (Basis):** DataFrames ermöglichen SQL-ähnliche Abfragen direkt in Python. `df[Bedingung]` ist der Standard-Weg zum Filtern (Boolean Indexing).
  * **Vektorisierung (Bonus):** Pandas und Numpy führen Operationen auf C-Ebene aus. Wenn wir `df['a'] * df['b']` schreiben, wird der Loop in kompiliertem C-Code ausgeführt. Nutzen wir `for row in df:`, zwingen wir Python, für jede Zeile Objekte zu erzeugen und Typen zu prüfen. Der Unterschied liegt oft im Faktor 100x bis 1000x.

-----

### Code: Basis Aufgabe

```python
import pandas as pd

def analyze_transactions():
    # 1. Laden
    print("Lade Daten...")
    df = pd.read_csv('big_transactions.csv')
    
    # 2. Inspektion
    print("\n--- Info ---")
    print(df.info())
    print("\n--- Head ---")
    print(df.head())
    
    # 3. Filterung
    # Filter: Nur USD
    usd_mask = df['currency'] == 'USD'
    usd_transactions = df[usd_mask]
    
    # Filter: Große Abhebungen (> 2000 UND type == withdrawal)
    # Beachten Sie die Klammern () bei mehreren Bedingungen & operator
    risk_mask = (df['amount'] > 2000.00) & (df['type'] == 'withdrawal')
    large_withdrawals = df[risk_mask]
    
    # 4. Reporting
    count = len(large_withdrawals)
    total_amount = large_withdrawals['amount'].sum()
    
    print("\n--- Report ---")
    print(f"Anzahl USD Transaktionen: {len(usd_transactions)}")
    print(f"Anzahl Risiko-Abhebungen: {count}")
    print(f"Summe Risiko-Beträge: {total_amount:,.2f}")

if __name__ == "__main__":
    analyze_transactions()
```

-----

### Code: Bonus Herausforderung

```python
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
```