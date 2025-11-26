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
