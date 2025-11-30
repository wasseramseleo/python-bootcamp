# Lab 02: Modularisierung & Best Practices

### Szenario

Das Skript aus Lab 01 funktioniert, ist aber nicht wiederverwendbar. Andere Abteilungen der PyBank möchten Ihre Umrechnungslogik nutzen. Wir müssen den Code ändern, Logik in Funktionen kapseln und Standard-Bibliotheken einbinden.

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
