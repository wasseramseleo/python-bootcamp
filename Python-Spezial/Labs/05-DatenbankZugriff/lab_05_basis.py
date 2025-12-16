from sqlalchemy import create_engine, text

# 1. Engine Konfiguration
# echo=True gibt alle SQL Befehle in der Konsole aus (gut zum Debuggen)
engine = create_engine("sqlite:///bank.db", echo=True)


create_sql = text("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY,owner TEXT NOT NULL, balance FLOAT NOT NULL)")
insert_sql = "TODO"
select_sq = "TODO"

with engine.connect() as conn:
    # 2. Tabelle erstellen
    conn.execute(create_sql)
    conn.commit()
    # 3. Daten einfügen
    data = [
        {"o": "Alice Corp", "b": 50000.0},
        {"o": "Bob Consult", "b": 1250.50}
    ]

    # TODO: Implement
    # 4. Daten lesen
    # TODO: Implement

