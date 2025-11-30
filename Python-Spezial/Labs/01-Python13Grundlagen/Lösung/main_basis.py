# Rohdaten
transactions = [
  {"id": 101, "type": "deposit", "amount": 100.00, "currency": "EUR"},
  {"id": 102, "type": "withdrawal", "amount": 50.00, "currency": "EUR"},
  {"id": 103, "type": "deposit", "amount": 200.00, "currency": "USD"},
  {"id": 104, "type": "payment", "amount": 25.50, "currency": "EUR"},
  {"id": 105, "type": "withdrawal", "amount": 1000.00, "currency": "USD"},
]

usd_to_eur_rate = 0.90

# 1. Initialisierung
balance = 0.0
processed_transactions = []

# 2. Verarbeitungsschleife
for tx in transactions:
  amount = tx["amount"]
  currency = tx["currency"]
  tx_type = tx["type"]

  # 3. Währungsumrechnung
  if currency == "USD":
    amount = amount * usd_to_eur_rate

  # 4. Logik für Balance
  if tx_type == "deposit":
    balance += amount
  elif tx_type in ["withdrawal", "payment"]:
    balance -= amount

  # 5. Speicherung
  processed_transactions.append(amount)

# 6. Output
print(f"Final Balance: {balance:.2f} EUR")
print(f"Processed Count: {len(processed_transactions)}")