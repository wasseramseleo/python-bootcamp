# Lab 10: Open Practice (Tag 1)

### Szenario

Der erste Tag neigt sich dem Ende zu. Sie haben die Grundlagen, Module, File-I/O und einfache DB-Zugriffe gelernt. In dieser "Open Practice" Session können Sie wählen, welche Technologien Sie für die PyBank-Systemlandschaft vertiefen möchten.

**Freie Aufgabenwahl.**

### Voraussetzungen

Installieren Sie je nach gewählter Aufgabe die notwendigen Pakete:

```bash
pip install pandas openpyxl requests flask sqlalchemy
```

-----

### Option A: Functional Banking (Map, Filter & Lambda)

Im Banking müssen oft Listen transformiert werden, ohne den Originalzustand zu ändern (Immutability).

**Gegebene Daten:**

```python
transactions = [
    {"id": 1, "amount": 100.0, "currency": "EUR", "risk_score": 0.1},
    {"id": 2, "amount": 5000.0, "currency": "USD", "risk_score": 0.8}, # High Risk
    {"id": 3, "amount": 20.0, "currency": "EUR", "risk_score": 0.05},
    {"id": 4, "amount": 1000.0, "currency": "GBP", "risk_score": 0.6}, # High Risk
]
exchange_rates = {"EUR": 1.0, "USD": 0.9, "GBP": 1.15}
```

**Aufgabe:**

1.  **Filtern:** Extrahieren Sie alle Transaktionen mit einem `risk_score > 0.5`.
      * Lösen Sie dies einmal mit `filter()` und einer `lambda`-Funktion.
      * Lösen Sie dies einmal mit einer **List Comprehension**.
2.  **Mappen:** Erstellen Sie eine Liste, die nur die *Beträge in EUR* enthält.
      * Nutzen Sie `map()`, um die Währung umzurechnen.
      * Nutzen Sie alternativ eine List Comprehension.

-----

### Option B: Excel Reporting (Pandas & OpenPyXL)

Das Management verlangt Reports zwingend im `.xlsx` Format, nicht als CSV.

**Aufgabe:**

1.  Erstellen Sie mit Pandas einen DataFrame aus 10 fiktiven Transaktionen (Datum, Empfänger, Betrag).
2.  **Export:** Schreiben Sie diesen DataFrame in eine Datei `financial_report.xlsx`.
      * Die Datei soll **zwei** Arbeitsblätter (Sheets) enthalten:
          * `Sheet1`: Die Rohdaten.
          * `Sheet2`: Eine Zusammenfassung (Summe pro Empfänger).
3.  **Import:** Lesen Sie testweise nur das Blatt `Sheet2` wieder ein und geben Sie es auf der Konsole aus.

-----

### Option C: API Integration (Requests & JSON)

Die Bank muss die Bonität (Credit Score) von Kunden bei einer externen Agentur abfragen. Da wir keine echte API haben, simulieren wir diese.

**Schritt 1: Der Mock-Server (Setup)**
Starten Sie den Mock-Server mit der Datei `mock_server.py`.

**Schritt 2: Die Aufgabe (Client)**
Erstellen Sie ein Skript `api_client.py`:

1.  Importieren Sie `requests`.
2.  Fragen Sie die API für die Kunden `CUST-001`, `CUST-002` und `CUST-X` ab (`http://127.0.0.1:5000/credit-score/...`).
3.  Parsen Sie die JSON-Antwort.
4.  Geben Sie das Kreditlimit aus oder fangen Sie den Fehler ab, falls der Kunde nicht existiert (Status Code 404).

-----

### Option D: Advanced SQLAlchemy (Relationships)

Bisher haben wir nur einzelne Tabellen betrachtet. Nun modellieren wir eine **1-zu-n Beziehung** zwischen `Customer` und `Account`.

**Aufgabe:**

1.  Definieren Sie zwei Klassen (`Base`):
      * `Customer`: id (PK), name.
      * `Account`: id (PK), balance, customer\_id (ForeignKey auf customer.id).
2.  Nutzen Sie `relationship`, um die Verbindung im ORM sichtbar zu machen.
3.  **Insert:** Erstellen Sie einen Kunden "PyCorp" und fügen Sie ihm *direkt* zwei Konten hinzu (über die Relationship-Liste), bevor Sie `session.add(customer)` aufrufen.
4.  **Query:** Laden Sie den Kunden aus der DB und iterieren Sie über seine Konten (z.B. `print(my_customer.accounts)`).
