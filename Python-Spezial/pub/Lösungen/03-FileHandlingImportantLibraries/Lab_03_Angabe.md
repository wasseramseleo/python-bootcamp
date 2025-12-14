# Lab 03: File Handling & Libraries

### Szenario
Das "PyBank" System wird integriert. Anstatt Testdaten im Code zu schreiben, erhalten Sie nun echte Exporte aus dem Altsystem (als CSV) und Logs von der neuen Mobile-App (als JSON). Ihre Aufgabe ist es, diese Dateien einzulesen, die Zeitstempel zu verstehen und Berichte zu speichern.

### Voraussetzungen
* `transactions.csv` und `app_log.json` (Erstellen Sie diese Dateien lokal mit dem untenstehenden Inhalt).
* Wissen über `open()`, `csv`, `json`, `datetime` und `re` (Regular Expressions).

---

### Basis Aufgabe

Ziel ist das Lesen einer CSV-Datei, das Parsen von benutzerdefinierten Datums-Strings (wie in den Folien gezeigt) und das Schreiben einer Zusammenfassung.

**Vorbereitung:**
Stellen Sie sicher, dass `transactions.csv` im Projektordner existiert.

```csv
date,type,amount,currency
2023-10-01 09:00:00,deposit,1000.00,EUR
2023-10-02 14:30:00,withdrawal,50.00,EUR
2023-10-05 10:15:00,payment,25.99,EUR
````

**Anforderungen:**
1.  **Einlesen:**
      * Nutzen Sie das `csv` Modul und `DictReader` (wie im Theorie-Code), um die `transactions.csv` zu lesen.
      * Verwenden Sie den `with open(...)` Context Manager.
2.  **Datum Parsen:**
      * Die Spalte `date` hat das Format `YYYY-MM-DD HH:MM:SS`.
      * Nutzen Sie `datetime.strptime()` (nicht `fromisoformat`), um den String in ein echtes Datumsobjekt zu wandeln.
      * Definieren Sie den korrekten Format-String (analog zum Theorie-Beispiel).
3.  **Logik:**
      * Iterieren Sie über die Zeilen.
      * Berechnen Sie die Summe aller Transaktionen (Withdrawal/Payment sind negativ).
4.  **Schreiben:**
      * Erstellen Sie eine neue Datei `daily_report.txt` im Schreib-Modus (`w`).
      * Schreiben Sie einen Satz hinein: "Final Balance calculated on [HEUTIGES DATUM]: [BETRAG] EUR".
      * Nutzen Sie `datetime.now()` für das heutige Datum.

-----

### Bonus Herausforderung (JSON & Regex)

Ziel ist das Verarbeiten geschachtelter JSON-Daten und das Extrahieren von IDs aus Fließtext mittels `re` (Regular Expressions).

**Vorbereitung:**
Stellen Sie sicher, dass `app_log.json` im Projektordner existiert.

**Anforderungen:**

1.  **JSON Load:**
      * Laden Sie die Datei mittels `json.load()` in ein Python Dictionary.
2.  **Regex Extraction:**
      * Iterieren Sie durch die Liste der Transaktionen.
      * Die "Reference ID" in `details` folgt immer dem Muster: Zwei Großbuchstaben, ein Bindestrich, sechs Ziffern (z.B. `TX-998877`).
      * Schreiben Sie ein Regex-Pattern (analog zum Vogelring-Beispiel `[A-Z]{2}-\d{4}`), passen Sie es aber auf 6 Ziffern an.
      * Nutzen Sie `re.findall()` oder `re.search()`, um die ID zu finden.
3.  **Output:**
      * Geben Sie für jeden Eintrag die interne `id` und die gefundene externe ID auf der Konsole aus.
      * Falls keine ID gefunden wurde, geben Sie "NO\_REF" aus.

<!-- end list -->
