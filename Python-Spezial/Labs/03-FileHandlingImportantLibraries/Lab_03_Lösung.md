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
