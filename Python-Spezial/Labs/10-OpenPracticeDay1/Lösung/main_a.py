transactions = [
    {"id": 1, "amount": 100.0, "currency": "EUR", "risk_score": 0.1},
    {"id": 2, "amount": 5000.0, "currency": "USD", "risk_score": 0.8},
    {"id": 3, "amount": 20.0, "currency": "EUR", "risk_score": 0.05},
    {"id": 4, "amount": 1000.0, "currency": "GBP", "risk_score": 0.6},
]
rates = {"EUR": 1.0, "USD": 0.9, "GBP": 1.15}

print("--- 1. Filtern (High Risk) ---")
# Ansatz: filter()
# Hinweis: filter gibt einen Iterator zurück, daher list()
high_risk_filter = list(filter(lambda tx: tx["risk_score"] > 0.5, transactions))
print(f"Filter/Lambda: {high_risk_filter}")

# Ansatz: List Comprehension (Pythonic Way)
high_risk_comp = [tx for tx in transactions if tx["risk_score"] > 0.5]
print(f"Comprehension: {high_risk_comp}")

print("\n--- 2. Mapping (Convert to EUR) ---")
# Helper Funktion für map
def convert(tx):
    return tx["amount"] * rates[tx["currency"]]

# Ansatz: map()
eur_values_map = list(map(convert, transactions))
print(f"Map: {eur_values_map}")

# Ansatz: List Comprehension
eur_values_comp = [tx["amount"] * rates[tx["currency"]] for tx in transactions]
print(f"Comprehension: {eur_values_comp}")
