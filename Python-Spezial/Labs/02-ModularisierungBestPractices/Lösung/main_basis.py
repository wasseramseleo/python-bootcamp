import datetime


# 1. Funktion für Währung
def convert_currency(amount, currency, rate=0.90):
  """Konvertiert Fremdwährung in EUR."""
  if currency == "USD":
    return amount * rate
  # Annahme: Andere Währungen sind bereits EUR oder werden ignoriert
  return amount


# 2. Funktion für Verarbeitung
def process_ledger(transaction_list):
  """Iteriert über Transaktionen und berechnet den Endstand."""
  balance = 0.0

  for tx in transaction_list:
    # Extraktion
    amount = tx["amount"]
    curr = tx["currency"]
    t_type = tx["type"]

    # Nutzung der Helper-Funktion
    amount_in_eur = convert_currency(amount, curr)

    # Logik
    if t_type == "deposit":
      balance += amount_in_eur
    elif t_type in ["withdrawal", "payment"]:
      balance -= amount_in_eur

  return balance


# Ausführung
data = [
  {"type": "deposit", "amount": 100.00, "currency": "EUR"},
  {"type": "withdrawal", "amount": 50.00, "currency": "EUR"},
  {"type": "deposit", "amount": 200.00, "currency": "USD"},
]

final_balance = process_ledger(data)

# 3. Datetime Output
now = datetime.datetime.now()
print(f"Final Balance: {final_balance:.2f} EUR")
print(f"Report generated at: {now}")