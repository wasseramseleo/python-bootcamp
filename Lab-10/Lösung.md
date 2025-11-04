# Lab 10: Type Annotations & typing - Lösung

## Erläuterung der Lösung

### Angabe

Die Lösung fügt der `BankAccount`-Klasse und der `find_account_by_number`-Funktion schrittweise Typ-Annotationen hinzu.

1.  **Klassen-Attribute:** Typen (`str`, `float`) werden direkt auf Klassenebene annotiert. Dies dient primär der Dokumentation und der Unterstützung durch IDEs/Type-Checkers.
2.  **`__init__` und Methoden:**
      * Argumente erhalten die Syntax `name: type` (z.B. `amount: float`).
      * Der Rückgabetyp wird mit `-> type` (z.B. `-> bool`) nach der Parameterliste festgelegt.
      * Für `__init__` wird kein Rückgabetyp annotiert, da er implizit `None` ist und der Konstruktor sich selbst (die Instanz) konfiguriert.
3.  **Container (`list[BankAccount]`):** In `find_account_by_number` verwenden wir die moderne Syntax `list[BankAccount]`, um anzugeben, dass `accounts` eine Liste ist, die *nur* `BankAccount`-Objekte enthält.
4.  **Optionale Typen (`BankAccount | None`):** Dies ist die (seit Python 3.10) bevorzugte Syntax statt `Optional[BankAccount]`. Sie zeigt klar an, dass die Funktion `find_account_by_number` *entweder* ein `BankAccount`-Objekt *oder* den Wert `None` zurückgeben kann. Statische Analyse-Tools (wie `mypy`) würden uns warnen, wenn wir versuchen würden, auf das Ergebnis zuzugreifen (z.B. `found_acc.get_owner_name()`), ohne vorher zu prüfen, ob `found_acc` nicht `None` ist.

### Bonus-Herausforderung

Die Bonus-Lösung zeigt zwei komplexere Anwendungsfälle für Annotationen:

1.  **Komplexe Dictionaries (`dict[str, str | float]`):**
      * `dict[KeyType, ValueType]` annotiert Dictionaries.
      * Da die Werte in unseren Transaktions-Dicts gemischt sind (z.B. `type: 'DEPOSIT'` (str) und `amount: 100.0` (float)), verwenden wir den Union-Typ `str | float` für den `ValueType`.
2.  **`Callable` (Callbacks):**
      * `Callable` wird verwendet, wenn eine Funktion als Argument an eine andere Funktion übergeben wird.
      * Die Syntax ist `Callable[[Arg1Type, Arg2Type], ReturnType]`.
      * In unserem Fall ist der Handler eine Funktion, die *ein* Argument entgegennimmt (das `dict`) und ein `bool` zurückgibt.
      * Die Annotation lautet daher: `Callable[[dict[str, str | float]], bool]`.

Dies ermöglicht es dem Type-Checker sicherzustellen, dass nur Funktionen als `handler` übergeben werden, die auch die erwartete "Signatur" (Argument-Typen und Rückgabe-Typ) aufweisen.

## Python-Code: Basis-Aufgabe

```python
class BankAccount:
    """
    Stellt ein Bankkonto dar. (Version für Type Hinting)
    """
    
    # 1. Klassen-Attribute annotiert
    owner: str
    account_number: str
    _balance: float

    def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0) -> None:
        # 2. __init__ Parameter annotiert (Return-Type ist None)
        self.owner = owner
        self.account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount: float) -> bool:
        # 3. 'amount' (float) und Return-Type (bool) annotiert
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        # 4. 'amount' (float) und Return-Type (bool) annotiert
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        # 5. Return-Type (float) annotiert
        return self._balance

    def get_owner_name(self) -> str:
        # 6. Return-Type (str) annotiert
        return self.owner

# --- Externe Funktion annotiert ---

def find_account_by_number(accounts: list[BankAccount], number: str) -> BankAccount | None:
    # 7. Vollständig annotiert (moderne Syntax list[T] und T | None)
    
    for acc in accounts:
        if acc.account_number == number:
            return acc
    return None

# --- Test-Code ---
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
```

## Python-Code: Bonus-Herausforderung

```python
from typing import Callable, Any

# Wir definieren einen "Type Alias" für unsere komplexe Transaktion
# Dies macht den Code viel lesbarer
TransactionData = dict[str, str | float | Any] 
# (Any hinzugefügt, falls dicts variieren, aber str | float ist präziser für die Angabe)
TransactionDataPrecise = dict[str, str | float]


# 1. Callback-Handler (jetzt auch annotiert)
def simple_deposit_handler(tx_data: TransactionDataPrecise) -> bool:
    """
    Ein Beispiel-Handler, der nur DEPOSIT-Transaktionen verarbeitet.
    """
    # Wir können 'type' sicher abrufen, aber mypy würde warnen,
    # wenn 'type' nicht im dict[str, str | float] enthalten wäre.
    if tx_data.get('type') == 'DEPOSIT' and isinstance(tx_data.get('amount'), float):
        print(f"Verarbeite Einzahlung: {tx_data['amount']}")
        return True
    return False

# 2. Die Hauptfunktion (vollständig annotiert)
def process_batch(
    transactions: list[TransactionDataPrecise],
    handler: Callable[[TransactionDataPrecise], bool]
) -> None:
    """
    Verarbeitet einen Stapel von Transaktionen mit einem 
    Callback-Handler.
    """
    print(f"\n--- Verarbeite Batch mit Handler: {handler.__name__} ---")
    processed_count = 0
    for tx in transactions:
        if handler(tx):
            processed_count += 1
    
    print(f"Verarbeitung abgeschlossen. {processed_count} Transaktionen verarbeitet.")


# --- Test-Code (Bonus) ---
print("--- Bonus-Herausforderung Test ---")

transactions_batch: list[TransactionDataPrecise] = [
    {'id': 'T1', 'type': 'DEPOSIT', 'amount': 100.0},
    {'id': 'T2', 'type': 'WITHDRAW', 'amount': 50.0}, # Wird ignoriert
    {'id': 'T3', 'type': 'DEPOSIT', 'amount': 300.0}
]

# Übergabe der Handler-Funktion an die process_batch-Funktion
process_batch(transactions_batch, simple_deposit_handler)

# --- Was würde mypy fangen? ---
# (Dieser Code wird nicht ausgeführt, dient nur der Demonstration)

def invalid_handler(tx: TransactionDataPrecise) -> str:
    # Falscher RÜCKGABEWERT (str statt bool)
    return "Processed"

def test_mypy():
    # mypy würde hier einen Fehler melden:
    # Argument 2 to "process_batch" has incompatible type
    # "Callable[[TransactionDataPrecise], str]";
    # expected "Callable[[TransactionDataPrecise], bool]"
    #
    # process_batch(transactions_batch, invalid_handler)
    pass
```
