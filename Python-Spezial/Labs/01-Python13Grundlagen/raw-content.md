# LAB 01 DETAILS:

* **Lab Title/Topic:** Python 13 Grundlagen
* **Learning Objectives:**
    * Syntax verstehen und einfache Datenspeicherungen in Listen/Dicts durchführen.
    * Advanced: List Comprehensions nutzen, Generatoren verstehen und Type Hinting anwenden.
* **Context & Slide Summary:** 
    - Syntax & Variablen
    - Listen, Dictionaries, Tuples
    - Kontrollstrukturen (Loops, If)
    -: List Comprehensions, Generators, Type Hinting


# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

Hier sind die Unterlagen für Lab 01.

### Design-Entscheidung

Dieses Lab etabliert die Datenstrukturen, die wir in den nächsten 2 Tagen nutzen werden. Die Trennung zwischen der Basis-Aufgabe (imperative Loops) und der Bonus-Aufgabe (funktionale Ansätze wie Comprehensions) ist hier entscheidend, um die Spanne zwischen Anfängern und Fortgeschrittenen abzudecken.

-----

## `Lab_01_Angabe.md`

# Lab 01: Python Grundlagen & Datenstrukturen

### Szenario

Sie arbeiten im Backend-Team der "PyBank". Ihr System erhält einen rohen Feed von Transaktionen verschiedener Konten (Checking, Savings). Ihre Aufgabe ist es, diese Rohdaten zu normalisieren, Währungen umzurechnen und eine erste Bilanz zu ziehen.

### Voraussetzungen

  * Python 3.10+ installiert
  * IDE oder Editor bereit

-----

### Teil 1: Basis Aufgabe

Ziel ist es, eine Liste von Transaktions-Dictionaries zu verarbeiten, Währungen zu konvertieren und den Kontostand zu berechnen.

**Gegebene Daten:**
Verwenden Sie diese Liste als Ausgangspunkt:

```python
transactions = [
    {"id": 101, "type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"id": 102, "type": "withdrawal", "amount": 50.00, "currency": "EUR"},
    {"id": 103, "type": "deposit", "amount": 200.00, "currency": "USD"},
    {"id": 104, "type": "payment", "amount": 25.50, "currency": "EUR"},
    {"id": 105, "type": "withdrawal", "amount": 1000.00, "currency": "USD"},
]
usd_to_eur_rate = 0.90
```

**Anforderungen:**

1.  **Initialisierung:** Erstellen Sie eine Variable `balance` mit Startwert `0.0` und zwei leere Listen: `processed_transactions` und `high_value_transactions`.
2.  **Verarbeitungsschleife:** Iterieren Sie über die `transactions` Liste.
3.  **Währungsumrechnung:** Falls die Währung "USD" ist, rechnen Sie den Betrag in EUR um (`amount * usd_to_eur_rate`).
4.  **Logik:**
      * Wenn `type` gleich "deposit" ist: Addieren Sie den Betrag zur `balance`.
      * Wenn `type` gleich "withdrawal" oder "payment" ist: Subtrahieren Sie den Betrag von der `balance`.
5.  **Speicherung:** Fügen Sie die *umgerechnete* Betragshöhe (als float) der Liste `processed_transactions` hinzu.
6.  **Output:** Geben Sie am Ende den finalen Kontostand (`balance`) und die Anzahl der verarbeiteten Transaktionen auf der Konsole aus.

-----

### Teil 2: Bonus Herausforderung

Ziel ist die Anwendung von modernem, "pythonischem" Code für effizientere Datenverarbeitung.

**Anforderungen:**

1.  **Type Hinting:** Kopieren Sie Ihren Code und fügen Sie explizite Type Hints hinzu (z.B. `List[Dict]`, `float`, etc.). Importieren Sie `List`, `Dict`, `Any` aus `typing` (oder nutzen Sie built-in types ab Python 3.9+).
2.  **List Comprehension:** Erstellen Sie eine neue Liste `eur_amounts`, die *nur* die Beträge aller Transaktionen enthält, bereits in EUR umgerechnet. Lösen Sie dies in einer **einzigen Zeile** mittels List Comprehension.
3.  **Generator:** Schreiben Sie eine Generator-Funktion `transaction_id_generator(start_id, count)`, die fortlaufende Transaktions-IDs erzeugt (`yield`). Nutzen Sie diesen Generator, um 5 neue IDs zu simulieren und auf der Konsole auszugeben.

-----

## `Lab_01_Lösung.md`

# Lösung Lab 01

### Lösungsansatz

  * **Basis:** Klassischer imperativer Ansatz. Wir nutzen `if/elif` für die Geschäftslogik und akkumulieren den Status in einer Variable. Dies ist leicht lesbar, aber verbos.
  * **Bonus:** Hier wird die Kompaktheit von Python demonstriert. Type Hints dokumentieren den Code (Best Practice im Enterprise-Umfeld). List Comprehensions reduzieren den Loop auf den reinen Datentransformations-Ausdruck.

-----

### Code: Basis Aufgabe

```python
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
```

-----

### Code: Bonus Herausforderung

```python
from typing import List, Dict, Any, Generator

# 1. Type Hinting Definitionen
# In Python 3.9+ kann man list[...] und dict[...] direkt nutzen, 
# für Kompatibilität nutzen wir hier typing.
TransactionList = List[Dict[str, Any]]

transactions: TransactionList = [
    {"id": 101, "type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"id": 102, "type": "withdrawal", "amount": 50.00, "currency": "EUR"},
    {"id": 103, "type": "deposit", "amount": 200.00, "currency": "USD"},
    {"id": 104, "type": "payment", "amount": 25.50, "currency": "EUR"},
    {"id": 105, "type": "withdrawal", "amount": 1000.00, "currency": "USD"},
]

# 2. List Comprehension
# Logik: Nimm Betrag * 0.9 wenn USD, sonst Betrag.
eur_amounts: List[float] = [
    tx["amount"] * 0.90 if tx["currency"] == "USD" else tx["amount"]
    for tx in transactions
]

print(f"Alle Beträge in EUR (Comprehension): {eur_amounts}")

# 3. Generator
def transaction_id_generator(start_id: int, count: int) -> Generator[int, None, None]:
    """Generiert fortlaufende IDs lazy."""
    current = start_id
    for _ in range(count):
        yield current
        current += 1

# Generator Konsumieren
print("Generierte IDs:")
id_gen = transaction_id_generator(200, 5)
for new_id in id_gen:
    print(new_id)
```

Would you like me to proceed with Lab 02? If so, please verify if the focus should be on **Functions & Modules** or **Error Handling**, as these are logical next steps.