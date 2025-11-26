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
