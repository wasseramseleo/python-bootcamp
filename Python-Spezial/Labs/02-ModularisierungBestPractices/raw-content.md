# LAB 02 DETAILS:

* **Lab Title/Topic:** Modularisierung & Best Practices
* **Learning Objectives:**
    * Code in Funktionen kapseln und externe Libraries importieren.
    * Advanced: Eigene Module erstellen, if __name__ == "__main__" verstehen, Exception Handling (try/except).
* **Context & Slide Summary:** 
    - Funktionen & Module
    - pip & Environments
    - Skript-Struktur (PEP 8)
    - Advanced: Eigenes Modul erstellen, Exception handling 

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

## `Lab_02_Angabe.md`

# Lab 02: Modularisierung & Best Practices

### Szenario

Das Skript aus Lab 01 funktioniert, ist aber schwer wiederverwendbar. Andere Abteilungen der PyBank möchten Ihre Umrechnungslogik nutzen. Wir müssen den Code ändern, Logik in Funktionen kapseln und Standard-Bibliotheken einbinden.

### Voraussetzungen

  * Lösung oder Code aus Lab 01
  * Verständnis von `def`, `return` und `import`

-----

### Teil 1: Basis Aufgabe

Ziel ist die Kapselung der Logik in wiederverwendbare Funktionen und die Nutzung der Python Standard Library.

**Anforderungen:**

1.  **Funktion `convert_currency`:**
      * Erstellen Sie eine Funktion, die `amount`, `currency` und optional `rate` (Standardwert 0.90) akzeptiert.
      * Die Funktion soll den Betrag in EUR zurückgeben. Wenn die Währung bereits "EUR" ist, wird der Betrag unverändert zurückgegeben.
2.  **Funktion `process_ledger`:**
      * Erstellen Sie eine Funktion, die eine Liste von Transaktionen akzeptiert.
      * Integrieren Sie die Logik aus Lab 01 (Loop, if/else für deposit/withdrawal) in diese Funktion.
      * **Wichtig:** Nutzen Sie innerhalb der Loop Ihre neue `convert_currency` Funktion.
      * Die Funktion soll den finalen `balance` zurückgeben (kein `print` innerhalb der Funktion!).
3.  **Standard Library:**
      * Importieren Sie das Modul `datetime`.
      * Geben Sie am Ende des Skripts den berechneten Kontostand aus, gefolgt von einem Zeitstempel: `Report generated at: YYYY-MM-DD HH:MM:SS`.

**Test-Daten:**

```python
transactions = [
    {"type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"type": "withdrawal", "amount": 50.00, "currency": "EUR"},
    {"type": "deposit", "amount": 200.00, "currency": "USD"}, # Sollte umgerechnet werden
]
```

-----

### Teil 2: Bonus Herausforderung

Ziel ist die Simulation einer echten Projektstruktur und Robustheit gegen Datenfehler (Resilience).

**Anforderungen:**

1.  **Module Split:** Lagern Sie die Funktionen (`convert_currency`, `process_ledger`) in eine neue Datei namens `banking_core.py` aus.
2.  **Import:** Erstellen Sie ein `main.py` Skript, das diese Funktionen importiert und ausführt.
3.  **Error Handling:** Modifizieren Sie die Schleife in `process_ledger`:
      * Fügen Sie einen `try-except` Block hinzu.
      * Fangen Sie Fehler ab, falls eine Transaktion unvollständig ist (z.B. fehlender Key "amount" oder "type").
      * Bei einem Fehler: Geben Sie eine Warnung auf der Konsole aus ("Skipping invalid transaction..."), aber lassen Sie das Programm **nicht abstürzen**.
4.  **Main Guard:** Schützen Sie den auszuführenden Code in `main.py` mit `if __name__ == "__main__":`.

**Korrupte Test-Daten für Bonus:**

```python
transactions = [
    {"type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"type": "payment"}, # FEHLER: Fehlender amount/currency
    {"type": "withdrawal", "amount": "fünfzig", "currency": "EUR"}, # FEHLER: String statt Float
]
```

-----

## `Lab_02_Lösung.md`

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
