from account import BankAccount

print("--- Bonus: Ausgabe von help(BankAccount.withdraw) ---")
# help() liest den Docstring und formatiert ihn:
help(BankAccount.withdraw)
help(BankAccount.get_balance)

print("\n--- Bonus: Ausgabe von help(BankAccount) ---")
# help() auf der Klasse fasst ALLE Docstrings zusammen:
help(BankAccount)
