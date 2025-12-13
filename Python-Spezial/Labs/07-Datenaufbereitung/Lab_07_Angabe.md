# Lab 07: Datenaufbereitung & Aggregation

### Szenario
Sie haben Transaktionsdaten, aber diese sind unvollständig ("dirty data"). Zusätzlich liegt eine separate Liste mit Kunden-Stammdaten vor. Ihr Ziel: Daten bereinigen (Missing Values behandeln), beide Quellen verbinden und aggregierte Reports erstellen.

### Voraussetzungen
* `pandas` installiert.
* **Testdaten:** `transactions_dirty.csv` und `customers.csv` (werden im Setup erstellt).

---

### Basis Aufgabe

Ziel ist das Bereinigen von `NaN` Werten mittels der zwei in der Theorie gezeigten Strategien und das Zusammenführen von Tabellen.

**Anforderungen:**

1.  **Load & Clean (Missing Values):**
    * Laden Sie `transactions_dirty.csv`.
    * **Strategie 1 (Drop):** Transaktionen ohne `account_id` sind wertlos. Entfernen Sie Zeilen, in denen `account_id` fehlt (`dropna`).
    * **Strategie 2 (Impute):** Manche `amount` Werte sind leer (`NaN`). Füllen Sie diese mit `0.0` auf (`fillna`).

2.  **Merge (Left Join):**
    * Laden Sie `customers.csv`.
    * Verbinden Sie die bereinigten Transaktionen mit den Kunden basierend auf `account_id`.
    * Nutzen Sie einen **Left Join** (wie im Theorie-Code `how='left'`), damit Transaktionen erhalten bleiben, auch wenn dem Konto kein Kunde zugeordnet werden kann.

3.  **Aggregation (Group By):**
    * Gruppieren Sie das Ergebnis nach `region`.
    * Nutzen Sie `.agg()`, um gleichzeitig zwei Metriken für die Spalte `amount` zu berechnen:
        * `sum` (Gesamtvolumen)
        * `count` (Anzahl der Transaktionen)
    * *Hinweis:* Dies entspricht dem `species_stats` Beispiel aus den Folien.

---

### Bonus Herausforderung

Ziel ist die Anwendung komplexer Zeilen-Logik, Zeitreihen-Analyse und Pivot-Tabellen.

**Anforderungen:**

1.  **Custom Logic (Apply):**
    * Schreiben Sie eine Funktion `classify_risk(row)`, die eine Zeile entgegennimmt.
    * Logik: Wenn `amount` > 2000 ist, geben Sie "High Risk" zurück, sonst "Standard".
    * Wenden Sie diese Funktion mit `df.apply(..., axis=1)` auf den DataFrame an und erstellen Sie eine neue Spalte `risk_class`.

2.  **Time Series (Resampling):**
    * Stellen Sie sicher, dass die `date` Spalte ein echtes Datetime-Objekt ist.
    * Setzen Sie das Datum als Index (`set_index`).
    * Aggregieren Sie die Daten auf **Wochen-Basis** (`resample('W')`) und berechnen Sie die Anzahl (`size()` oder `count()`) der Transaktionen pro Woche.

3.  **Pivot Table:**
    * Erstellen Sie eine Zusammenfassungs-Matrix (`pivot_table`) aus dem Haupt-DataFrame.
    * **Zeilen:** `region`
    * **Spalten:** `risk_class` (aus Schritt 1)
    * **Werte:** `amount`
    * **Aggregat:** `mean` (Durchschnittshöhe der Transaktion)
    * Aktivieren Sie `margins=True` für Gesamtsummen.
```
