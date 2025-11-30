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
        reader = csv.DictReader(csvfile)  # DictReader macht Zugriff per Spaltenname möglich

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