# Lösung Lab 07

### Lösungsansatz

  * **Merge:** Ein `how='left'` Merge ist im Banking Standard, um Datenintegrität zu prüfen. Wenn nach dem Merge in den Kunden-Spalten `NaN` steht (bei ID 999), wissen wir, dass hier Transaktionen für unbekannte Konten vorliegen (Datenfehler oder Betrug).
  * **Resample:** Pandas ist extrem stark bei Zeitreihen (aus dem Finanzsektor entstanden). `resample` ist wie ein `groupby` für Zeitintervalle und spart komplexe Datums-Rechnereien.

-----

### Code: Basis Aufgabe

```python
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
    
    return merged_df # Rückgabe für Teil 2

if __name__ == "__main__":
    df_result = clean_and_merge()
```

-----

### Code: Bonus Herausforderung

```python
import pandas as pd
# Wir importieren die Funktion aus Teil 1 oder nutzen den Code erneut
# Hier simulieren wir, dass df_result bereitsteht:
# df_result = clean_and_merge() 

def advanced_analysis(df):
    print("\n--- BONUS: Time Series & Pivot ---")
    
    # 1. Setup Datetime Index
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    
    # 2. Resampling (Wochen-Aggregation)
    # 'W' = Weekly frequency. Wir summieren die Beträge pro Woche.
    weekly_stats = df['amount'].resample('W').sum()
    
    print("Wöchentliches Volumen:")
    print(weekly_stats)
    
    # 3. Pivot Table
    # Zeigt multidimensionale Zusammenhänge
    pivot = pd.pivot_table(
        df, 
        values='amount', 
        index='region', 
        columns='type', 
        aggfunc='mean'
    )
    
    print("\nDurchschnittlicher Betrag (Pivot nach Region & Typ):")
    print(pivot)

if __name__ == "__main__":
    # Um dieses Skript standalone lauffähig zu machen, müssen wir Teil 1 kurz wiederholen
    # oder die Daten neu laden. Der Einfachheit halber:
    try:
        tx = pd.read_csv('transactions_dirty.csv').fillna(0)
        cu = pd.read_csv('customers.csv')
        full_df = pd.merge(tx, cu, on='account_id', how='left')
        advanced_analysis(full_df)
    except FileNotFoundError:
        print("Bitte zuerst das Setup-Skript aus der Angabe ausführen!")
```