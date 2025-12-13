# Lab 02: Modularisierung & Best Practices

### Szenario
Das Skript aus Lab 01 funktioniert, ist aber "Spaghetti-Code". Andere Abteilungen der PyBank möchten Ihre Umrechnungslogik nutzen. Wir müssen den Code aufräumen, Logik in Funktionen kapseln und robuster machen.

### Voraussetzungen
* Lösung aus Lab 01
* Verständnis von `def`, `return` und `import`

---

### Basis Aufgabe

Ziel ist die Kapselung der Logik in wiederverwendbare Funktionen mit klaren Schnittstellen (Type Hints), wie im Theorie-Beispiel `calculate_condition_index`.

**Anforderungen:**

1.  **Funktion `convert_currency`:**
    * Erstellen Sie eine Funktion, die `amount`, `currency` und optional `rate` (Standardwert 0.90) akzeptiert.
    * **Type Hints:** Nutzen Sie Type Hints für Parameter und Rückgabewert (z.B. `amount: float` -> `float`).
    * Die Funktion soll den Betrag in EUR zurückgeben. (Ist die Währung "EUR", wird der Betrag unverändert retourniert).

2.  **Funktion `process_ledger`:**
    * Erstellen Sie eine Funktion, die eine Liste von Transaktionen verarbeitet.
    * Integrieren Sie die Logik aus Lab 01 (Loop, if/else für deposit/withdrawal).
    * Nutzen Sie innerhalb der Loop Ihre neue `convert_currency` Funktion.
    * Die Funktion soll den finalen `balance` zurückgeben.

3.  **Zeitstempel:**
    * Importieren Sie `datetime` (wie im Theorie-Block gezeigt).
    * Erstellen Sie eine kleine Hilfsfunktion `get_timestamp()`, die den aktuellen Zeitpunkt als String (ISO Format) zurückgibt.

**Test-Daten:**
```python
transactions = [
    {"type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"type": "withdrawal", "amount": 50.00, "currency": "EUR"},
    {"type": "deposit", "amount": 200.00, "currency": "USD"},
]
````

-----

### Bonus Herausforderung

Ziel ist die Absicherung gegen Abstürze bei fehlerhaften Daten und die Definition eines klaren Einstiegspunkts (`Main Guard`).

**Anforderungen:**

1.  **Main Guard:**

      * Verpacken Sie Ihren Ausführungscode (Aufruf der Funktionen, `print` des Ergebnisses) in eine `main()` Funktion.
      * Nutzen Sie das `if __name__ == "__main__":` Konstrukt am Ende der Datei, um `main()` aufzurufen.

2.  **Error Handling:**

      * Die echte Welt liefert oft "schmutzige" Daten (z.B. Beträge als String mit Tippfehlern).
      * Erweitern Sie `process_ledger` um einen `try-except` Block innerhalb der Schleife (analog zum `weight`-Beispiel in den Folien).
      * Versuchen Sie, den `amount` explizit in einen `float` umzuwandeln.
      * Fangen Sie einen **`ValueError`** ab, falls dies fehlschlägt.
      * Geben Sie im Fehlerfall eine Meldung aus (`"Error processing transaction..."`) und überspringen Sie diesen Eintrag (addieren Sie nichts zur Balance), aber **lassen Sie das Programm nicht abstürzen**.

**Korrupte Test-Daten für die Bonus Herausforderung:**

```python
transactions = [
    {"type": "deposit", "amount": 100.00, "currency": "EUR"},
    {"type": "withdrawal", "amount": "fünfzig", "currency": "EUR"}, # FEHLER: String statt Zahl
    {"type": "deposit", "amount": "200.00", "currency": "USD"},    # OK: String, aber konvertierbar
]
```
