# LAB 07 DETAILS:

* **Lab Title/Topic:** Datenaufbereitung
* **Learning Objectives:**
    * Daten filtern, einfache Summen/Mittelwerte berechnen (Pivot) und Tabellen verbinden.
    * Advanced: + Komplexe apply-Funktionen schreiben, Multi-Indizes handhaben und Zeitreihen-Manipulation.
* **Context & Slide Summary:** 
    - Missing Values behandeln
    - GroupBy & Aggregationen
    - Merging & Concatenation
    - Advanced: Pivot table, Apply & Time Series

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

## `Lab_07_Angabe.md`

# Lab 07: Datenaufbereitung & Aggregation

### Szenario

Sie haben Transaktionsdaten, aber diese sind unvollständig (fehlende Werte) und anonym (nur Account-IDs). Zusätzlich haben Sie eine separate Liste mit Kunden-Stammdaten. Ihr Ziel: Daten bereinigen, beide Quellen verbinden und aggregierte Reports erstellen.

### Voraussetzungen

  * **Datengenerierung:** Führen Sie bitte dieses Skript aus, um `transactions_dirty.csv` und `customers.csv` zu erstellen.

<!-- end list -->

```python
import pandas as pd
import numpy as np

# 1. Stammdaten (Kunden)
customers = pd.DataFrame({
    'account_id': [101, 102, 103, 104, 105],
    'name': ['Alice Corp', 'Bob Ltd', 'Charlie Inc', 'Dave Co', 'Eve Ent'],
    'region': ['EU', 'US', 'EU', 'US', 'ASIA']
})
customers.to_csv('customers.csv', index=False)

# 2. Transaktionsdaten (mit Fehlern)
dates = pd.date_range(start='2024-01-01', periods=20, freq='D')
data = {
    'date': dates,
    'account_id': np.random.choice([101, 102, 103, 999], 20), # 999 existiert nicht in customers
    'amount': np.random.uniform(-500, 2000, 20),
    'type': np.random.choice(['deposit', 'withdrawal'], 20)
}
df = pd.DataFrame(data)

# Wir bauen "Schmutz" ein (Missing Values)
df.loc[0, 'amount'] = np.nan
df.loc[5, 'amount'] = np.nan
df.to_csv('transactions_dirty.csv', index=False)

print("Setup fertig: CSV-Dateien erstellt.")
```

-----

### Teil 1: Basis Aufgabe

Ziel ist das Bereinigen von `NaN` Werten und das Zusammenführen von Tabellen (SQL Join).

**Anforderungen:**

1.  **Load & Clean:**
      * Laden Sie `transactions_dirty.csv`.
      * Identifizieren Sie fehlende Werte (`df.isna().sum()`).
      * Ersetzen Sie fehlende Beträge in `amount` mit `0.0` (`fillna`).
2.  **Merge (Join):**
      * Laden Sie `customers.csv`.
      * Verbinden Sie die Transaktionen mit den Kunden basierend auf `account_id`.
      * Nutzen Sie einen **Left Join**, damit Transaktionen erhalten bleiben, auch wenn kein Kunde gefunden wird (z.B. ID 999).
3.  **Aggregation:**
      * Gruppieren Sie das Ergebnis nach `region`.
      * Berechnen Sie die Summe der `amount` Spalte pro Region.
      * Geben Sie das Ergebnis aus.

-----

### Teil 2: Bonus Herausforderung

Ziel ist die Arbeit mit Zeitreihen (Time Series) und Pivot-Tabellen.

**Anforderungen:**

1.  **Datetime Index:**
      * Stellen Sie sicher, dass die `date` Spalte ein echtes Datetime-Objekt ist (`pd.to_datetime`).
      * Setzen Sie das Datum als Index des DataFrames (`set_index`).
2.  **Resampling (Zeit-Aggregation):**
      * Nutzen Sie `.resample('W')` (Weekly), um die Summe der Transaktionen pro Woche zu berechnen.
3.  **Pivot Table:**
      * Erstellen Sie eine Pivot-Tabelle aus dem verbundenen DataFrame (aus Teil 1).
      * **Index:** `region`
      * **Columns:** `type`
      * **Values:** `amount`
      * **Aggfunc:** `mean` (Durchschnitt)
      * Ergebnis: Eine Übersicht, wie hoch die durchschnittliche Einzahlung/Abhebung pro Region ist.

-----

## `Lab_07_Lösung.md`

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
