import datetime
# 1. Import des eigenen Moduls
import banking_core

# Korrupte Daten
transactions = [
    {"type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"type": "payment"},  # Löst KeyError aus
    {"type": "withdrawal", "amount": "InvalidNumber", "currency": "EUR"},  # Löst ValueError aus
    {"type": "deposit", "amount": 50.00, "currency": "USD"},  # Valid
]

# 4. Main Guard
if __name__ == "__main__":
    print("Starting Batch Processing...")

    # Aufruf der Funktion aus dem Modul
    final_balance = banking_core.process_ledger_safe(transactions)

    print("---")
    print(f"Final Valid Balance: {final_balance:.2f} EUR")
    print(f"Timestamp: {datetime.datetime.now()}")