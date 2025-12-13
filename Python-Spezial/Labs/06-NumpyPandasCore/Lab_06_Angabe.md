# Lab 06: Numpy & Pandas Data Analysis

### Szenario
Die Datenmengen wachsen. Die IT-Abteilung hat Ihnen einen Extrakt von 100.000 Transaktionen bereitgestellt. Reine Python-Listen sind zu langsam. Sie nutzen nun Pandas, um den Datensatz zu laden, gezielt nach risikoreichen Transaktionen zu filtern und Berechnungen performant durchzuführen.

### Voraussetzungen
* `pandas` und `numpy` installiert (`pip install pandas numpy`).
* Datei `big_transactions.csv` (wird im Setup erstellt).

---

### Basis Aufgabe

Ziel ist der sichere Umgang mit DataFrames: Laden, Inspektion und Selektion mittels Boolean Indexing (wie im Theorie-Block "Filter rows" gezeigt).

**Anforderungen:**

1.  **Laden & Inspektion:**
    * Importieren Sie `pandas` (als `pd`).
    * Laden Sie die `big_transactions.csv`.
    * Nutzen Sie `.info()`, um Datentypen und Speicherverbrauch zu prüfen.
    * Nutzen Sie `.head()`, um die Struktur zu verstehen.

2.  **Selektion (Boolean Indexing):**
    * Erstellen Sie einen neuen DataFrame `high_value_tx`.
    * Filter-Kriterium: Betrag (`amount`) ist größer als 2000.00.
    * Erstellen Sie einen zweiten DataFrame `usd_deposits`.
    * Filter-Kriterium: Währung (`currency`) ist "USD" **UND** Typ (`type`) ist "deposit". (Nutzen Sie die `&` Syntax aus dem Sample Code).

3.  **Reporting:**
    * Geben Sie die Anzahl der Zeilen für beide gefilterten DataFrames aus.
    * Berechnen Sie den Durchschnitts-Betrag (`mean`) der `high_value_tx`.

---

### Bonus Herausforderung

Ziel ist das Verständnis von **Vektorisierung**. Wir vergleichen die Performance einer klassischen Python-Schleife mit Pandas-Spalten-Operationen, exakt wie im Theorie-Beispiel "BAD vs GOOD".

**Anforderungen:**

1.  **Szenario:**
    * Die Bank führt eine neue "Service Fee" von 2% auf alle Transaktionen ein.
    * Wir müssen eine neue Spalte `fee` berechnen (`amount * 0.02`).

2.  **Der "Naive" Ansatz (Loop):**
    * Importieren Sie `time`.
    * Iterieren Sie mit `iterrows()` über den DataFrame.
    * Berechnen Sie pro Zeile die Gebühr und schreiben Sie sie (z.B. in eine Liste oder Zelle).
    * Messen und drucken Sie die benötigte Zeit.

3.  **Der "Pandas" Ansatz (Vektorisierung):**
    * Berechnen Sie die Spalte `df['fee']` direkt durch Multiplikation der Spalte `df['amount']` mit `0.02`.
    * Dies entspricht dem Beispiel `wings_arr / 10.0` oder `df['weight'] / df['wing']` aus den Folien.
    * Messen und drucken Sie die Zeit.

4.  **Vergleich:**
    * Vergleichen Sie die Laufzeiten. (Die Vektorisierung sollte signifikant schneller sein).
```
