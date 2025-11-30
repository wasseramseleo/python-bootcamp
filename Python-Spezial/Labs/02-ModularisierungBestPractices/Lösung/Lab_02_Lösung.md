# Lösung Lab 02

### Lösungsansatz

  * **Refactoring:** Wir trennen I/O (Input/Output) von der Logik. Funktionen berechnen Werte und geben sie zurück (`return`), anstatt direkt zu drucken. Das erhöht die Testbarkeit.
  * **Exceptions:** In Finanzsystemen ist "Fail Fast" oft gut, aber bei Batch-Verarbeitung (Tausende Transaktionen) ist "Skip and Report" oft besser, um den Gesamtprozess nicht zu gefährden. Wir fangen spezifische Fehler (`KeyError`, `TypeError`) ab, keine generischen `Exception`.

-----

### Code: Basis Aufgabe

```python
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
```

-----

### Code: Bonus Herausforderung

**Datei 1: `banking_core.py` (Das Modul)**

```python
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
            curr = tx.get("currency", "EUR") # Default zu EUR wenn fehlt
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
```

**Datei 2: `main.py` (Das Hauptskript)**

```python
import datetime
# 1. Import des eigenen Moduls
import banking_core 

# Korrupte Daten
transactions = [
    {"type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"type": "payment"}, # Löst KeyError aus
    {"type": "withdrawal", "amount": "InvalidNumber", "currency": "EUR"}, # Löst ValueError aus
    {"type": "deposit", "amount": 50.00, "currency": "USD"}, # Valid
]

# 4. Main Guard
if __name__ == "__main__":
    print("Starting Batch Processing...")
    
    # Aufruf der Funktion aus dem Modul
    final_balance = banking_core.process_ledger_safe(transactions)
    
    print("---")
    print(f"Final Valid Balance: {final_balance:.2f} EUR")
    print(f"Timestamp: {datetime.datetime.now()}")
```
