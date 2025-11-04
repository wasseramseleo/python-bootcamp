from account import BankAccount, find_account_by_number

print("--- Angabe Test ---")
acc1 = BankAccount("Max Mustermann", "AT123", 100.0)
acc1.deposit(50.5)
print(f"Saldo: {acc1.get_balance()}")

accounts_list: list[BankAccount] = [acc1] # Variable auch annotiert
found_acc = find_account_by_number(accounts_list, "AT123")

if found_acc:
    print(f"Gefunden: {found_acc.get_owner_name()}")

not_found_acc = find_account_by_number(accounts_list, "XYZ")
print(f"Nicht gefunden: {not_found_acc}")