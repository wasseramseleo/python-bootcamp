# Lab 13: Daten-Analyse mit Pandas

## Lernziele

In diesem Lab nutzen Sie die Pandas-Bibliothek, um Transaktionsdaten aus einer CSV-Datei zu laden, zu untersuchen, zu filtern und zu aggregieren.

  * Daten aus einer CSV-Datei in einen Pandas DataFrame laden (`pd.read_csv`).
  * Den DataFrame inspizieren (`.head()`, `.info()`, `.describe()`).
  * Daten selektieren (Spaltenauswahl).
  * Daten filtern (Boolean Indexing / Masking).
  * Datenanalyse mit `groupby` (Split-Apply-Combine) durchführen.

## Szenario

Die Finanzabteilung unserer Banking-App benötigt eine Auswertung der Transaktionen des letzten Tages. Die Rohdaten liegen als `transactions.csv` vor. Ihre Aufgabe ist es, mit Pandas schnelle Einblicke in diese Daten zu gewinnen: Welche Konten sind am aktivsten? Wie verteilen sich die Transaktionstypen?

**Hinweis:** Für dieses Lab müssen Sie die Bibliothek `pandas` installiert haben (`pip install pandas`).

### Angabe

**Ziel:** Laden Sie die Transaktionsdaten, bereinigen Sie sie und führen Sie eine erste Aggregations-Analyse durch.

1.  **Laden und Inspizieren:**

      * Importieren Sie `pandas` (typischerweise als `pd`).
      * Laden Sie die Datei `transactions.csv` in einen DataFrame namens `df`.
      * **Inspizieren:** Nutzen Sie `df.head()` (um die ersten Zeilen zu sehen), `df.info()` (um Datentypen und Null-Werte zu prüfen) und `df.describe()` (um eine statistische Zusammenfassung der numerischen Spalten zu erhalten).

2.  **Datenbereinigung (Filtern):**

      * Die Analyse soll nur *erfolgreiche* Transaktionen (`COMPLETED`) berücksichtigen.
      * Erstellen Sie einen neuen DataFrame `df_completed`, der nur die Zeilen aus `df` enthält, bei denen die `status`-Spalte den Wert `COMPLETED` hat.

3.  **Selektion und Filterung (Masking):**

      * (Arbeiten Sie ab jetzt nur noch mit `df_completed`.)
      * Erstellen Sie eine Maske (Filter), um alle `DEPOSIT`-Transaktionen (Einzahlungen) zu finden, deren `amount` (Betrag) größer als 500 ist.
      * Zeigen Sie nur diese gefilterten Zeilen an.

4.  **Analyse (Groupby):**

      * Wie hoch ist die Gesamtsumme (Summe der `amount`-Spalte), die pro `account_id` (Kontonummer) transferiert wurde?
      * Verwenden Sie `df_completed.groupby(...)`, um die Daten nach `account_id` zu gruppieren.
      * Selektieren Sie die `amount`-Spalte und berechnen Sie die `.sum()` für jede Gruppe.

-----

### Bonus-Herausforderung

**Ziel:** Führen Sie komplexere Filterungen und mehrstufige Aggregationen durch.

1.  **Multi-Level Grouping:**

      * Berechnen Sie die Gesamtsumme (Summe der `amount`-Spalte) für `df_completed`, aber diesmal gruppiert nach *zwei* Kriterien gleichzeitig: `account_id` und `transaction_type`.
      * (Tipp: `groupby` akzeptiert eine Liste von Spaltennamen).

2.  **Komplexe Aggregation (`.agg()`):**

      * Das Management möchte eine detaillierte Aufschlüsselung *pro Transaktionstyp* (für `df_completed`).
      * Gruppieren Sie nach `transaction_type`.
      * Verwenden Sie die `.agg()`-Methode auf der `amount`-Spalte, um *gleichzeitig* die Gesamt-Anzahl (`'count'`), die Summe (`'sum'`) und den Durchschnittsbetrag (`'mean'`) für jeden Typ zu berechnen.

3.  **Fehleranalyse (`.loc` und `.idxmax()`):**

      * (Verwenden Sie hier den ursprünglichen DataFrame `df`.)
      * Finden Sie die Transaktion mit dem höchsten Betrag unter allen `FAILED`-Transaktionen.
      * Filtern Sie `df` zuerst nach `status == 'FAILED'`.
      * Finden Sie den Index der Zeile mit dem maximalen `amount` (Tipp: `.idxmax()`).
      * Verwenden Sie `.loc[...]`, um die gesamte Zeile (alle Details) zu dieser fehlgeschlagenen Transaktion anzuzeigen.


`transactions.csv`
```csv
transaction_id,account_id,transaction_type,amount,currency,status
T1001,AT123,DEPOSIT,500.00,EUR,COMPLETED
T1002,DE456,DEPOSIT,1000.00,EUR,COMPLETED
T1003,AT123,WITHDRAW,150.00,EUR,COMPLETED
T1004,CH789,DEPOSIT,3000.00,CHF,COMPLETED
T1005,DE456,WITHDRAW,250.00,EUR,FAILED
T1006,AT123,PAYMENT,45.50,EUR,COMPLETED
T1007,DE456,WITHDRAW,50.00,EUR,COMPLETED
T1008,AT123,DEPOSIT,200.00,EUR,COMPLETED
T1009,CH789,WITHDRAW,1000.00,CHF,COMPLETED
T1010,DE456,PAYMENT,80.00,EUR,COMPLETED
T1011,AT123,DEPOSIT,50.00,USD,COMPLETED
T1012,DE456,DEPOSIT,2000.00,EUR,FAILED
T1013,CH789,PAYMENT,500.00,CHF,COMPLETED
T1014,AT123,WITHDRAW,100.00,USD,COMPLETED
```