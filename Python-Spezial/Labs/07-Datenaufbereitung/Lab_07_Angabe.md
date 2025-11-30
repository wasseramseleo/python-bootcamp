# Lab 07: Datenaufbereitung & Aggregation

### Szenario

Sie haben Transaktionsdaten, aber diese sind unvollständig und anonym. Zusätzlich haben Sie eine separate Liste mit Kunden-Stammdaten. Ihr Ziel: Daten bereinigen, beide Quellen verbinden und aggregierte Reports erstellen.

### Voraussetzungen

 * **Testdaten:** Stellen Sie sicher, dass die Testdaten `transactions_dirty.csv` und `customers.csv` im Ordner existieren.

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
