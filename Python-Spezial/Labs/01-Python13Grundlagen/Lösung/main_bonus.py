from typing import List, Dict, Any, Generator

# 1. Type Hinting Definitionen
# In Python 3.9+ kann man list[...] und dict[...] direkt nutzen,
# für Kompatibilität nutzen wir hier typing.
TransactionList = List[Dict[str, Any]]

transactions: TransactionList = [
    {"id": 101, "type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"id": 102, "type": "withdrawal", "amount": 50.00, "currency": "EUR"},
    {"id": 103, "type": "deposit", "amount": 200.00, "currency": "USD"},
    {"id": 104, "type": "payment", "amount": 25.50, "currency": "EUR"},
    {"id": 105, "type": "withdrawal", "amount": 1000.00, "currency": "USD"},
]

# 2. List Comprehension
# Logik: Nimm Betrag * 0.9 wenn USD, sonst Betrag.
eur_amounts: List[float] = [
    tx["amount"] * 0.90 if tx["currency"] == "USD" else tx["amount"]
    for tx in transactions
]

print(f"Alle Beträge in EUR (Comprehension): {eur_amounts}")

# 3. Generator
def transaction_id_generator(start_id: int, count: int) -> Generator[int, None, None]:
    """Generiert fortlaufende IDs lazy."""
    current = start_id
    for _ in range(count):
        yield current
        current += 1

# Generator Konsumieren
print("Generierte IDs:")
id_gen = transaction_id_generator(200, 5)
for new_id in id_gen:
    print(new_id)