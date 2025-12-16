from sqlalchemy import create_engine, text

# 1. Engine Konfiguration
# echo=True gibt alle SQL Befehle in der Konsole aus (gut zum Debuggen)
engine = create_engine("sqlite:///bank.db", echo=True, isolation_level="AUTOCOMMIT")



def manage_accounts_raw():
    # Context Manager schließt die Verbindung automatisch am Ende
    create_sql = text(
        "CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY,owner TEXT NOT NULL, balance FLOAT NOT NULL) ")
    insert_sql = text("INSERT INTO accounts (owner, balance) VALUES (:o, :b)")
    select_sql = text("SELECT owner, balance FROM accounts")
    with engine.connect() as conn:
        # 2. Tabelle erstellen
        # IF NOT EXISTS verhindert Fehler beim mehrmaligen Ausführen
        conn.execute(create_sql)
        # 3. Daten einfügen
        data = [
            {"o": "Alice Corp", "b": 50000.0},
            {"o": "Bob Consult", "b": 1250.50}
        ]

        conn.execute(insert_sql, data)
        # 4. Daten lesen
        result = conn.execute(select_sql)

        print("\n--- Account Liste ---")
        for row in result:
            # Zugriff über Spaltennamen (row.owner) oder Index
            print(f"Kunde: {row.owner} | Saldo: {row.balance}")


if __name__ == "__main__":
    manage_accounts_raw()