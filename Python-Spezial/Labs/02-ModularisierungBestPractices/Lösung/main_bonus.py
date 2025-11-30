import datetime


def convert_currency(amount, currency, rate=0.90):
  if currency == "USD":
    return amount * rate
  return amount


def process_ledger_safe(transaction_list):
  balance = 0.0

  for tx in transaction_list:
    # 3. Error Handling
    try:
      amount = tx["amount"]
      curr = tx.get("currency", "EUR")  # Default zu EUR wenn fehlt
      t_type = tx["type"]

      # Typ-Prüfung simulieren (würde sonst bei Mathe crashen)
      amount = float(amount)

      amount_in_eur = convert_currency(amount, curr)

      if t_type == "deposit":
        balance += amount_in_eur
      elif t_type == "withdrawal":
        balance -= amount_in_eur

    except KeyError as e:
      print(f"[WARN] Skipping transaction due to missing data: {e}")
    except ValueError as e:
      print(f"[WARN] Skipping transaction due to invalid number format: {e}")
    except Exception as e:
      # Catch-all für unerwartete Fehler (in Production mit Logging nutzen!)
      print(f"[ERROR] Unexpected error: {e}")

  return balance

# Ausführung
data = [
  {"type": "deposit", "amount": 100.00, "currency": "EUR"},
  {"type": "withdrawal", "amount": 50.00, "currency": "EUR"},
  {"type": "deposit", "amount": 200.00, "currency": "USD"},
]

final_balance = process_ledger_safe(data)

# 3. Datetime Output
now = datetime.datetime.now()
print(f"Final Balance: {final_balance:.2f} EUR")
print(f"Report generated at: {now}")