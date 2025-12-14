# Lab 03: File Handling & Libraries

### Szenario

Das "PyBank" System wird integriert. Anstatt Testdaten im Code zu schreiben, erhalten Sie nun echte Exporte aus dem Altsystem (als CSV) und Logs von der neuen Mobile-App (als JSON). Ihre Aufgabe ist es, diese Dateien einzulesen, die Zeitstempel zu verstehen und Berichte zu speichern.

### Voraussetzungen

  * `transactions.csv` und `app_log.json` (Erstellen Sie diese Dateien lokal mit dem untenstehenden Inhalt).
  * Wissen über `open()`, `csv`, `json`, `datetime`.

-----

### Basis Aufgabe

Ziel ist das Lesen einer CSV-Datei, das Parsen von Datumsangaben und das Schreiben einer Zusammenfassung in eine Textdatei.

**Vorbereitung:**
Erstellen Sie eine Datei `transactions.csv` mit folgendem Inhalt:

```csv
date,type,amount,currency
2023-10-01T09:00:00,deposit,1000.00,EUR
2023-10-02T14:30:00,withdrawal,50.00,EUR
2023-10-05T10:15:00,payment,25.99,EUR
```

**Anforderungen:**

1.  **Einlesen:** Nutzen Sie das `csv` Modul (oder Standard File-IO mit Split), um die `transactions.csv` Zeile für Zeile zu lesen.
      * *Tipp:* Nutzen Sie den Context Manager `with open(...)`.
2.  **Datum Parsen:** Die Spalte `date` ist im ISO-Format. Nutzen Sie `datetime.fromisoformat()` (aus dem `datetime` Modul), um den String in ein echtes Datumsobjekt zu wandeln.
3.  **Logik:** Summieren Sie alle Beträge (behandeln Sie `withdrawal` und `payment` als negativ).
4.  **Schreiben:** Erstellen Sie eine neue Datei `daily_report.txt`.
      * Schreiben Sie das Datum der *ersten* Transaktion in der Datei.
      * Schreiben Sie den finalen Kontostand.

-----

### Bonus Herausforderung

Ziel ist das Verarbeiten komplexer, geschachtelter JSON-Daten und das Extrahieren von Informationen aus Freitext mittels Regular Expressions (`re`).

**Vorbereitung:**
Erstellen Sie eine Datei `app_log.json` mit folgendem Inhalt (beachten Sie die unstrukturierten "details"):

```json
{
  "batch_id": "BATCH-2023-X99",
  "transactions": [
    {
      "id": 1,
      "details": "Payment processed ref: TX-998877 sent to merchant."
    },
    {
      "id": 2,
      "details": "Refund initiated ref: TX-112233 for customer request."
    },
    {
      "id": 3,
      "details": "Internal transfer without ref ID."
    }
  ]
}
```

**Anforderungen:**

1.  **JSON Load:** Laden Sie die Datei mittels `json.load()`.
2.  **Regex Extraction:** Iterieren Sie durch die Transaktionen. Nutzen Sie das `re` Modul, um die Transaktions-Referenznummer aus dem Feld `details` zu extrahieren.
      * *Muster:* Das Muster beginnt immer mit "ref: " gefolgt von "TX-" und 6 Ziffern (z.B. `TX-998877`).
3.  **Fehlerbehandlung:** Wenn keine ID gefunden wird (siehe ID 3), soll "NO\_ID\_FOUND" ausgegeben werden.
4.  **Output:** Geben Sie für jeden Eintrag die interne `id` und die extrahierte `External Ref` auf der Konsole aus.
