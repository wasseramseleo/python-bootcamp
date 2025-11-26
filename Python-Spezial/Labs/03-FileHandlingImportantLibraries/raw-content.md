# LAB 03 DETAILS:

* **Lab Title/Topic:** File Handling & Wichtige Libraries
* **Learning Objectives:**
  * CSV/Excel/JSON Dateien öffnen, lesen und wieder schreiben. Timestamps im iso format mittels datetime modul parsen.
  * Advanced: Context Manager (with) beherrschen, Encoding-Fehler beheben, komplexe JSON-Strukturen parsen. Textmuster mit
    re filtern.
* **Context & Slide Summary:** 
  - open() für txt
  - json & csv Module
  - datetime
  - Advanced: Context manager, regular expression

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

## `Lab_03_Angabe.md`

# Lab 03: File Handling & Libraries

### Szenario

Das "PyBank" System wird integriert. Anstatt Testdaten im Code zu schreiben, erhalten Sie nun echte Exporte aus dem Altsystem (als CSV) und Logs von der neuen Mobile-App (als JSON). Ihre Aufgabe ist es, diese Dateien einzulesen, die Zeitstempel zu verstehen und Berichte zu speichern.

### Voraussetzungen

  * `transactions.csv` und `app_log.json` (Erstellen Sie diese Dateien lokal mit dem untenstehenden Inhalt).
  * Wissen über `open()`, `csv`, `json`, `datetime`.

-----

### Teil 1: Basis Aufgabe

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

### Teil 2: Bonus Herausforderung

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

-----

## `Lab_03_Lösung.md`

# Lösung Lab 03

### Lösungsansatz

  * **File I/O:** Wir nutzen konsequent den `with`-Block. Das garantiert, dass Datei-Handles auch bei Fehlern (Exceptions) korrekt geschlossen werden – essentiell in Server-Umgebungen, um "Too many open files"-Fehler zu vermeiden.
  * **Libraries:** Anstatt CSV oder JSON per Hand zu parsen (String manipulation), nutzen wir die robusten Standard-Libraries.
  * **Regex:** Erlaubt präzises Suchen in unstrukturierten Strings, was bei Verwendungszwecken in Überweisungen oft nötig ist.

-----

### Code: Basis Aufgabe

```python
import csv
from datetime import datetime

# Dateinamen definieren
INPUT_FILE = 'transactions.csv'
OUTPUT_FILE = 'daily_report.txt'

def process_csv_report():
    balance = 0.0
    first_date = None
    
    # 1. Einlesen mit Context Manager
    # newline='' ist best practice beim csv modul
    with open(INPUT_FILE, mode='r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile) # DictReader macht Zugriff per Spaltenname möglich
        
        for row in reader:
            # Daten extrahieren
            amount = float(row['amount'])
            tx_type = row['type']
            date_str = row['date']
            
            # 2. Datum Parsen
            current_date = datetime.fromisoformat(date_str)
            
            # Merke das Datum der allerersten Transaktion
            if first_date is None:
                first_date = current_date
            
            # 3. Logik
            if tx_type == 'deposit':
                balance += amount
            elif tx_type in ['withdrawal', 'payment']:
                balance -= amount

    # 4. Schreiben des Reports
    with open(OUTPUT_FILE, mode='w', encoding='utf-8') as f:
        f.write("--- PYBANK DAILY REPORT ---\n")
        # Formatierung des Datums in lesbares Format (Tag.Monat.Jahr)
        if first_date:
            f.write(f"First Transaction Date: {first_date.strftime('%d.%m.%Y')}\n")
        f.write(f"Final Balance: {balance:.2f} EUR\n")
        f.write("---------------------------\n")

    print(f"Report erfolgreich in {OUTPUT_FILE} geschrieben.")

# Ausführen
if __name__ == "__main__":
    # Hinweis: Stellen Sie sicher, dass transactions.csv existiert!
    try:
        process_csv_report()
    except FileNotFoundError:
        print("Fehler: Bitte erstellen Sie zuerst die 'transactions.csv'.")
```

-----

### Code: Bonus Herausforderung

```python
import json
import re

INPUT_JSON = 'app_log.json'

def extract_references():
    # 1. JSON Load
    try:
        with open(INPUT_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Datei {INPUT_JSON} nicht gefunden.")
        return

    print(f"Processing Batch: {data.get('batch_id')}")
    print("-" * 30)

    # Regex Muster kompilieren (effizienter bei vielen Durchläufen)
    # Erklärung: 
    # ref:\s+  -> Suche nach "ref:" gefolgt von Leerzeichen
    # (TX-\d+) -> Gruppe 1: "TX-" gefolgt von einer oder mehreren Ziffern
    pattern = re.compile(r"ref:\s+(TX-\d+)")

    transactions = data.get('transactions', [])

    for tx in transactions:
        internal_id = tx['id']
        details = tx['details']
        
        # 2. Regex Search
        match = pattern.search(details)
        
        if match:
            # group(1) greift auf den Teil in der Klammer (TX-...) zu
            external_ref = match.group(1)
        else:
            external_ref = "NO_ID_FOUND"
            
        # 4. Output
        print(f"Internal ID: {internal_id} | External Ref: {external_ref}")

if __name__ == "__main__":
    extract_references()
```
