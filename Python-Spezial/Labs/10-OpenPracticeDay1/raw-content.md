# LAB 10 DETAILS:

* **Lab Title/Topic:** Open Practice (Tag 1)
* **Learning Objectives:**
    * Teilnehmende haben die Möglichkeit, sich je nach persönlichen Interessen fortgeschrittene aufgaben zu den bisher behandelten themen durchzuführen.
* **Content:**
  * Create coding challenges for each of the following topics:
    * Mapping & Filtering with List Comprehension and map() & filter()
    * File-I/O with excel
    * http requests with json data using the requests library (supply a minimal flask backend serving static json data)
    * Advanced SqlAlchemy

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, and two-file format) exept for the distinction of basis aufgabe and bonus herausforderung. Here only one type of task exists. 
Instead of haven one big task concerned with several topics, this open practice task is designed to offer several independent tasks for them to choose freely from.
The tasks explore topics/functionalities not covered by the previous labs.

-----

## `Lab_10_Angabe.md`

# Lab 10: Open Practice (Tag 1)

### Szenario

Der erste Tag neigt sich dem Ende zu. Sie haben die Grundlagen, Module, File-I/O und einfache DB-Zugriffe gelernt. In dieser "Open Practice" Session können Sie wählen, welche Technologien Sie für die PyBank-Systemlandschaft vertiefen möchten.

**Wählen Sie mindestens eine der folgenden 4 Aufgaben.**

### Voraussetzungen

Installieren Sie je nach gewählter Aufgabe die notwendigen Pakete:

```bash
pip install pandas openpyxl requests flask sqlalchemy
```

-----

### Option A: Functional Banking (Map, Filter & Lambda)

Im Banking müssen oft Listen transformiert werden, ohne den Originalzustand zu ändern (Immutability).

**Gegebene Daten:**

```python
transactions = [
    {"id": 1, "amount": 100.0, "currency": "EUR", "risk_score": 0.1},
    {"id": 2, "amount": 5000.0, "currency": "USD", "risk_score": 0.8}, # High Risk
    {"id": 3, "amount": 20.0, "currency": "EUR", "risk_score": 0.05},
    {"id": 4, "amount": 1000.0, "currency": "GBP", "risk_score": 0.6}, # High Risk
]
exchange_rates = {"EUR": 1.0, "USD": 0.9, "GBP": 1.15}
```

**Aufgabe:**

1.  **Filtern:** Extrahieren Sie alle Transaktionen mit einem `risk_score > 0.5`.
      * Lösen Sie dies einmal mit `filter()` und einer `lambda`-Funktion.
      * Lösen Sie dies einmal mit einer **List Comprehension**.
2.  **Mappen:** Erstellen Sie eine Liste, die nur die *Beträge in EUR* enthält.
      * Nutzen Sie `map()`, um die Währung umzurechnen.
      * Nutzen Sie alternativ eine List Comprehension.

-----

### Option B: Excel Reporting (Pandas & OpenPyXL)

Das Management verlangt Reports zwingend im `.xlsx` Format, nicht als CSV.

**Aufgabe:**

1.  Erstellen Sie mit Pandas einen DataFrame aus 10 fiktiven Transaktionen (Datum, Empfänger, Betrag).
2.  **Export:** Schreiben Sie diesen DataFrame in eine Datei `financial_report.xlsx`.
      * Die Datei soll **zwei** Arbeitsblätter (Sheets) enthalten:
          * `Sheet1`: Die Rohdaten.
          * `Sheet2`: Eine Zusammenfassung (Summe pro Empfänger).
3.  **Import:** Lesen Sie testweise nur das Blatt `Sheet2` wieder ein und geben Sie es auf der Konsole aus.

-----

### Option C: API Integration (Requests & JSON)

Die Bank muss die Bonität (Credit Score) von Kunden bei einer externen Agentur abfragen. Da wir keine echte API haben, simulieren wir diese.

**Schritt 1: Der Mock-Server (Setup)**
Erstellen Sie eine Datei `mock_server.py` und starten Sie diese in einem *separaten* Terminal. Lassen Sie es laufen.

```python
# mock_server.py
from flask import Flask, jsonify

app = Flask(__name__)

# Statische "Datenbank"
SCORES = {
    "CUST-001": {"score": 750, "rating": "A", "limit": 50000},
    "CUST-002": {"score": 620, "rating": "B", "limit": 10000},
    "CUST-999": {"score": 300, "rating": "D", "limit": 0}
}

@app.route('/credit-score/<customer_id>', methods=['GET'])
def get_score(customer_id):
    data = SCORES.get(customer_id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    print("Starte Credit-Score API auf Port 5000...")
    app.run(port=5000)
```

**Schritt 2: Die Aufgabe (Client)**
Erstellen Sie ein Skript `api_client.py`:

1.  Importieren Sie `requests`.
2.  Fragen Sie die API für die Kunden `CUST-001`, `CUST-002` und `CUST-X` ab (`http://127.0.0.1:5000/credit-score/...`).
3.  Parsen Sie die JSON-Antwort.
4.  Geben Sie das Kreditlimit aus oder fangen Sie den Fehler ab, falls der Kunde nicht existiert (Status Code 404).

-----

### Option D: Advanced SQLAlchemy (Relationships)

Bisher haben wir nur einzelne Tabellen betrachtet. Nun modellieren wir eine **1-zu-n Beziehung** zwischen `Customer` und `Account`.

**Aufgabe:**

1.  Definieren Sie zwei Klassen (`Base`):
      * `Customer`: id (PK), name.
      * `Account`: id (PK), balance, customer\_id (ForeignKey auf customer.id).
2.  Nutzen Sie `relationship`, um die Verbindung im ORM sichtbar zu machen.
3.  **Insert:** Erstellen Sie einen Kunden "PyCorp" und fügen Sie ihm *direkt* zwei Konten hinzu (über die Relationship-Liste), bevor Sie `session.add(customer)` aufrufen.
4.  **Query:** Laden Sie den Kunden aus der DB und iterieren Sie über seine Konten (z.B. `print(my_customer.accounts)`).

-----

## `Lab_10_Lösung.md`

# Lösung Lab 10

### Überblick

Hier finden Sie die Lösungen für die gewählten Wahlaufgaben.

-----

### Lösung A: Functional Banking

```python
transactions = [
    {"id": 1, "amount": 100.0, "currency": "EUR", "risk_score": 0.1},
    {"id": 2, "amount": 5000.0, "currency": "USD", "risk_score": 0.8},
    {"id": 3, "amount": 20.0, "currency": "EUR", "risk_score": 0.05},
    {"id": 4, "amount": 1000.0, "currency": "GBP", "risk_score": 0.6},
]
rates = {"EUR": 1.0, "USD": 0.9, "GBP": 1.15}

print("--- 1. Filtern (High Risk) ---")
# Ansatz: filter()
# Hinweis: filter gibt einen Iterator zurück, daher list()
high_risk_filter = list(filter(lambda tx: tx["risk_score"] > 0.5, transactions))
print(f"Filter/Lambda: {high_risk_filter}")

# Ansatz: List Comprehension (Pythonic Way)
high_risk_comp = [tx for tx in transactions if tx["risk_score"] > 0.5]
print(f"Comprehension: {high_risk_comp}")

print("\n--- 2. Mapping (Convert to EUR) ---")
# Helper Funktion für map
def convert(tx):
    return tx["amount"] * rates[tx["currency"]]

# Ansatz: map()
eur_values_map = list(map(convert, transactions))
print(f"Map: {eur_values_map}")

# Ansatz: List Comprehension
eur_values_comp = [tx["amount"] * rates[tx["currency"]] for tx in transactions]
print(f"Comprehension: {eur_values_comp}")
```

-----

### Lösung B: Excel Reporting

```python
import pandas as pd

# 1. Daten erstellen
data = {
    'Datum': ['2024-01-01', '2024-01-02', '2024-01-02'],
    'Empfänger': ['Alpha GmbH', 'Beta AG', 'Alpha GmbH'],
    'Betrag': [1000, 250, 500]
}
df = pd.DataFrame(data)

# Aggregation für Sheet 2
df_summary = df.groupby('Empfänger')['Betrag'].sum().reset_index()

# 2. Export in mehrere Sheets
# Dazu brauchen wir den ExcelWriter Context Manager
output_file = 'financial_report.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Rohdaten', index=False)
    df_summary.to_excel(writer, sheet_name='Zusammenfassung', index=False)

print(f"Datei '{output_file}' erfolgreich erstellt.")

# 3. Import spezifischer Sheets
print("\n--- Check: Lese Zusammenfassung ---")
df_check = pd.read_excel(output_file, sheet_name='Zusammenfassung')
print(df_check)
```

-----

### Lösung C: API Client

*Hinweis: Stellen Sie sicher, dass `mock_server.py` läuft.*

```python
import requests

BASE_URL = "http://127.0.0.1:5000/credit-score"
customer_ids = ["CUST-001", "CUST-002", "CUST-X"]

print(f"Frage API ab: {BASE_URL}")

for cid in customer_ids:
    url = f"{BASE_URL}/{cid}"
    
    try:
        response = requests.get(url)
        
        # Check auf HTTP Status 200 (OK)
        if response.status_code == 200:
            data = response.json() # JSON dekodieren
            print(f"Kunde {cid}: Rating {data['rating']}, Limit {data['limit']} EUR")
        elif response.status_code == 404:
            print(f"Kunde {cid}: Nicht gefunden (404)")
        else:
            print(f"Kunde {cid}: Unerwarteter Fehler {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("FEHLER: Konnte Server nicht erreichen. Läuft 'mock_server.py'?")
        break
```

-----

### Lösung D: Advanced SQLAlchemy

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()
engine = create_engine("sqlite:///:memory:", echo=False) # In-Memory DB

# 1. Model Definitionen
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Relationship: Ein Customer hat viele Accounts
    # back_populates verlinkt zur Account-Klasse
    accounts = relationship("Account", back_populates="owner")

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    balance = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    # Gegenstück der Relationship
    owner = relationship("Customer", back_populates="accounts")

    def __repr__(self):
        return f"<Acc(id={self.id}, bal={self.balance})>"

# Tabellen erstellen
Base.metadata.create_all(engine)

# 2. Daten einfügen via Relationship
session = Session(engine)

# Wir erstellen einen Kunden und hängen Accounts direkt an die Liste
new_cust = Customer(name="PyCorp International")
new_cust.accounts = [
    Account(balance=100000),
    Account(balance=5000)
]

session.add(new_cust)
session.commit()

# 3. Abfrage
print(f"Kunde '{new_cust.name}' gespeichert mit ID {new_cust.id}.")

# Daten neu laden (oder neuen Session Scope nutzen) um zu beweisen, dass es in DB ist
saved_cust = session.query(Customer).filter_by(name="PyCorp International").first()

print("\n--- Konten Übersicht ---")
for acc in saved_cust.accounts:
    print(f"Konto-ID: {acc.id} | Saldo: {acc.balance} EUR")
```
