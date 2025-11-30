# Lösung Lab 05

### Lösungsansatz

  * **SQLAlchemy Core (Basis):** Wir nutzen `text()`, um SQL-Befehle sicher zu kapseln. Seit SQLAlchemy 2.0 ist das explizite `commit()` notwendig, was den Transaktions-Charakter von Bankgeschäften unterstreicht.
  * **ORM (Bonus):** Das Mapping von Klasse zu Tabelle reduziert Boilerplate-Code. `session.add_all` ist extrem performant für Massendaten (Batch Processing).

-----

### Code: Basis Aufgabe

```python
from sqlalchemy import create_engine, text

# 1. Engine Konfiguration
# echo=True gibt alle SQL Befehle in der Konsole aus (gut zum Debuggen)
engine = create_engine("sqlite:///bank.db", echo=True)

def manage_accounts_raw():
    # Context Manager schließt die Verbindung automatisch am Ende
    with engine.connect() as conn:
        
        # 2. Tabelle erstellen
        # IF NOT EXISTS verhindert Fehler beim mehrmaligen Ausführen
        create_sql = text("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                owner TEXT NOT NULL,
                balance FLOAT NOT NULL
            )
        """)
        conn.execute(create_sql)
        conn.commit() # Wichtig!
        
        # 3. Daten einfügen
        # Zuerst prüfen, ob leer (optional), dann einfügen
        insert_sql = text("INSERT INTO accounts (owner, balance) VALUES (:o, :b)")
        data = [
            {"o": "Alice Corp", "b": 50000.0},
            {"o": "Bob Consult", "b": 1250.50}
        ]
        
        conn.execute(insert_sql, data)
        conn.commit()
        
        # 4. Daten lesen
        select_sql = text("SELECT owner, balance FROM accounts")
        result = conn.execute(select_sql)
        
        print("\n--- Account Liste ---")
        for row in result:
            # Zugriff über Spaltennamen (row.owner) oder Index
            print(f"Kunde: {row.owner} | Saldo: {row.balance}")

if __name__ == "__main__":
    manage_accounts_raw()
```

-----

### Code: Bonus Herausforderung

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, select
from sqlalchemy.orm import declarative_base, sessionmaker

# Setup
engine = create_engine("sqlite:///bank.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

# 1. Model Definition
class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    currency = Column(String)
    purpose = Column(String)
    
    def __repr__(self):
        return f"<Tx(id={self.id}, amount={self.amount}, cur={self.currency})>"

# Tabellen in DB anlegen (passiert nur, wenn sie nicht existieren)
Base.metadata.create_all(engine)

def advanced_orm_operations():
    session = Session()
    
    # 2. Bulk Insert
    print("Generiere Testdaten...")
    new_transactions = []
    for i in range(1, 101): # 100 Transaktionen
        # Einfache Logik: Gerade ID = EUR, Ungerade = USD
        curr = "EUR" if i % 2 == 0 else "USD"
        tx = Transaction(
            amount=i * 10.0, 
            currency=curr, 
            purpose=f"Payment Ref {i}"
        )
        new_transactions.append(tx)
    
    session.add_all(new_transactions)
    session.commit()
    print("100 Transaktionen erfolgreich gespeichert.")
    
    # 3. Parameterized Query (Sicherer Zugriff)
    # Hier suchen wir sicher nach einer Währung
    target_currency = "USD"
    
    # Modern SQLAlchemy 2.0 Style select
    stmt = select(Transaction).where(Transaction.currency == target_currency)
    
    # Ausführen
    results = session.execute(stmt).scalars().all()
    
    print(f"\n--- Gefundene {target_currency} Transaktionen ---")
    print(f"Anzahl: {len(results)}")
    print(f"Erste 3 Treffer: {results[:3]}")
    
    session.close()

if __name__ == "__main__":
    advanced_orm_operations()
```
