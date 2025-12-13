# Lab 01: Python Grundlagen & Datenstrukturen

### Szenario
Sie arbeiten im Backend-Team der "PyBank". Ihr System erhält einen rohen Feed von Transaktionen verschiedener Konten. Ihre Aufgabe ist es, diese Rohdaten zu normalisieren, Währungen umzurechnen und eine erste Bilanz zu ziehen.

### Voraussetzungen
* Python 3.10+
* Code Editor / Jupyter Notebook

---

### Basis Aufgabe

Ziel ist es, eine Liste von Transaktions-Dictionaries zu verarbeiten, Währungen zu konvertieren und den Kontostand zu berechnen. Dies entspricht der klassischen Logik (Loops, If-Else).

**Gegebene Daten:**
```python
transactions = [
    {"id": 101, "type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"id": 102, "type": "withdrawal", "amount": 50.00, "currency": "EUR"},
    {"id": 103, "type": "deposit", "amount": 200.00, "currency": "USD"},
    {"id": 104, "type": "payment", "amount": 25.50, "currency": "EUR"},
    {"id": 105, "type": "withdrawal", "amount": 1000.00, "currency": "USD"},
]
usd_to_eur_rate = 0.90
````

**Anforderungen:**

1.  **Initialisierung:** Erstellen Sie eine Variable `balance` (Startwert `0.0`) und eine leere Liste `processed_amounts`.
2.  **Verarbeitungsschleife:** Iterieren Sie über die `transactions` Liste.
3.  **Währungsumrechnung:**
      * Prüfen Sie, ob die Währung (`currency`) "USD" ist.
      * Falls ja: Rechnen Sie den Betrag in EUR um (`amount * usd_to_eur_rate`).
      * Falls nein: Nutzen Sie den Betrag unverändert.
4.  **Logik:**
      * Wenn `type` gleich "deposit" ist: Addieren Sie den (umgerechneten) Betrag zur `balance`.
      * Wenn `type` gleich "withdrawal" oder "payment" ist: Subtrahieren Sie den Betrag von der `balance`.
5.  **Speicherung:** Fügen Sie den finalen EUR-Betrag der Liste `processed_amounts` hinzu.
6.  **Output:** Geben Sie den finalen Kontostand (`balance`) auf der Konsole aus.

-----

### Bonus Herausforderung

Ziel ist die Anwendung kompakterer Syntax für Datenverarbeitung, wie in den Folien zu List Comprehensions und Generatoren gezeigt.

**Anforderungen:**

1.  **List Comprehension:**

      * Erstellen Sie eine neue Liste `eur_only_amounts` basierend auf der Liste `processed_amounts` aus Teil 1.
      * Diese neue Liste soll alle Beträge in `int` (Ganzzahlen) umwandeln (analog zum Abrunden der Vogelgewichte in den Folien).
      * Lösen Sie dies in einer einzigen Zeile.

2.  **Generator Expression:**

      * Simulieren Sie eine speichereffiziente Berechnung von Transaktionsgebühren.
      * Erstellen Sie einen Generator `fee_gen`.
      * Die Logik: Für jeden Betrag in `processed_amounts` soll 1% Gebühr (`amount * 0.01`) berechnet werden.
      * Iterieren Sie anschließend über `fee_gen` und geben Sie die Gebühren nacheinander aus.

3.  **Type Hinting:**

      * Schreiben Sie eine kleine Funktion `check_limit(amount: float) -> bool`.
      * Die Funktion soll `True` zurückgeben, wenn ein Betrag größer als 500.0 ist.
      * Verwenden Sie explizite Type Hints, wie im Theorie-Block ("Modern Standard") gezeigt.

<!-- end list -->
