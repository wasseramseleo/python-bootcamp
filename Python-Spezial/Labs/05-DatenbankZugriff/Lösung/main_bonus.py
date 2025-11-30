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
    for i in range(1, 101):  # 100 Transaktionen
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