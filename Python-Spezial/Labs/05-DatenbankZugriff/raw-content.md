# LAB 05 DETAILS:

* **Lab Title/Topic:** Datenbankzugriff
* **Learning Objectives:**
    * Verbindung zu einer DB herstellen und ein einfaches SELECT Statement ausführen. (Sqlite)
    * Advanced: ORM-Konzepte verstehen, sichere parametrisierte Queries schreiben und Bulk-Inserts durchführen.
* **Context & Slide Summary:** 
    - SQLAlchemy Basics
    - Connection Strings
    - SQL-Queries ausführen
    - Advanced: ORM Basics (model, session)

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

## `Lab_05_Angabe.md`

# Lab 05: Datenbankzugriff mit SQLAlchemy

### Szenario

CSV-Dateien sind für dauerhafte Bankdaten ungeeignet. Wir migrieren nun auf eine relationale Datenbank (SQLite für diesen Workshop). Sie sollen eine Tabelle für Konten (`accounts`) anlegen und Transaktionen sicher speichern.

### Voraussetzungen

  * Installation von SQLAlchemy:
    ```bash
    pip install sqlalchemy
    ```
  * *(Optional)* Ein SQLite Viewer Tool, um die Datei `bank.db` später zu inspizieren.

-----

### Teil 1: Basis Aufgabe

Ziel ist das Herstellen einer Verbindung und das Ausführen von "Raw SQL" über Python.

**Anforderungen:**

1.  **Engine erstellen:**
      * Importieren Sie `create_engine` und `text` aus `sqlalchemy`.
      * Erstellen Sie eine Engine für eine lokale Datei: `sqlite:///bank.db`.
2.  **Verbindung & Setup:**
      * Öffnen Sie eine Verbindung (`engine.connect()`).
      * Führen Sie ein SQL-Statement aus, um eine Tabelle `accounts` zu erstellen (Spalten: `id` (INTEGER PK), `owner` (TEXT), `balance` (FLOAT)).
      * *Hinweis:* Vergessen Sie bei Datenänderungen (CREATE, INSERT) nicht, `connection.commit()` aufzurufen.
3.  **Daten einfügen:**
      * Fügen Sie 2-3 Beispiel-Konten per SQL `INSERT` ein.
4.  **Daten lesen:**
      * Führen Sie ein `SELECT * FROM accounts` aus.
      * Iterieren Sie über das Ergebnis und geben Sie den Besitzer und Kontostand aus.

-----

### Teil 2: Bonus Herausforderung

Ziel ist die Nutzung des ORM (Object Relational Mapper) für objektorientierten Datenbankzugriff und Sicherheits-Best-Practices.

**Anforderungen:**

1.  **ORM Setup:**
      * Nutzen Sie `declarative_base` (oder `DeclarativeBase` ab v2.0), um eine Basisklasse zu erstellen.
      * Definieren Sie eine Python-Klasse `Transaction`, die auf eine Tabelle `transactions` mappt.
      * Spalten: `id` (PK), `amount` (Float), `currency` (String), `purpose` (String).
2.  **Bulk Insert:**
      * Erstellen Sie eine Liste von 100 `Transaction`-Objekten (nutzen Sie eine Schleife und Zufallswerte oder Dummy-Daten).
      * Speichern Sie alle Objekte auf einmal in die Datenbank (`session.add_all(...)` und `commit`).
3.  **Sicherheit (Parameterized Query):**
      * Schreiben Sie eine Abfrage, die Transaktionen filtert, wo die Währung "USD" ist.
      * **Wichtig:** Nutzen Sie keine String-Concatenation (`"WHERE currency = '" + var + "'"`), sondern die sicheren Filter-Methoden des ORM oder Parameter-Binding, um SQL Injection zu verhindern.

-----

## `Lab_05_Lösung.md`

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
