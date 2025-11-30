# Lösung Lab 10

### Überblick

Hier finden Sie die Lösungen für die Aufgaben der Open Practice von Tag 1.

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
