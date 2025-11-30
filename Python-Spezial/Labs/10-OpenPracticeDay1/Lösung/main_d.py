from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()
engine = create_engine("sqlite:///:memory:", echo=False)  # In-Memory DB


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
