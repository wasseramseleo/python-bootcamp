# Lab 06: Numpy & Pandas Data Analysis

### Szenario

Die Datenmengen wachsen. Die IT-Abteilung hat Ihnen einen Extrakt von 100.000 Transaktionen bereitgestellt. Excel stürzt ab, und reine Python-Listen sind zu langsam und unübersichtlich. Sie nutzen nun Pandas, um den Datensatz zu laden, "High-Risk"-Transaktionen zu filtern und Währungsumrechnungen performant durchzuführen.

### Voraussetzungen

  * Installation von Pandas und Numpy:

    ```bash
    pip install pandas numpy
    ```

  * **Testdaten:** Stellen Sie sicher, dass die Testdaten `big_transactions.csv` im Ordner existieren.

-----

### Basis Aufgabe

Ziel ist der sichere Umgang mit DataFrames: Laden, Inspektion und Selektion.

**Anforderungen:**

1.  **Laden:** Importieren Sie `pandas` (üblicherweise als `pd`) und laden Sie die `big_transactions.csv` in einen DataFrame.
2.  **Inspektion:**
      * Geben Sie die ersten 5 Zeilen aus (`head`).
      * Geben Sie die Datentypen und Speicherverbrauch aus (`info`).
3.  **Selektion & Filterung:**
      * Erstellen Sie einen neuen DataFrame `usd_transactions`, der nur Transaktionen enthält, bei denen die `currency` gleich "USD" ist.
      * Erstellen Sie einen DataFrame `large_withdrawals`, der nur Abhebungen (`type` == 'withdrawal') über 2000.00 Einheiten enthält.
4.  **Reporting:**
      * Zählen Sie, wie viele `large_withdrawals` gefunden wurden.
      * Berechnen Sie die Summe aller Beträge in `large_withdrawals`.

-----

### Bonus Herausforderung

Ziel ist das Verständnis von **Vektorisierung**. Wir vergleichen die Performance einer klassischen Python-Schleife mit Pandas-Operationen.

**Anforderungen:**

1.  **Szenario:** Wir müssen alle Beträge in eine Basiswährung (EUR) umrechnen.
      * Kursannahme: USD -\> 0.9 EUR, GBP -\> 1.15 EUR, EUR -\> 1.0.
2.  **Der "Naive" Ansatz (Loop):**
      * Schreiben Sie eine Funktion, die über den DataFrame iteriert (z.B. mit `iterrows()`), jede Zeile prüft und den neuen Betrag berechnet. Hängen Sie das Ergebnis an eine Liste an.
      * Messen Sie die Zeit mit dem `time` Modul.
3.  **Der "Pandas" Ansatz (Vektorisierung):**
      * Nutzen Sie `numpy` (`np.select` oder `np.where`) oder Pandas Mapping, um eine neue Spalte `amount_eur` basierend auf der Spalte `currency` und `amount` zu berechnen – **ohne Schleife!**
      * Messen Sie auch hier die Zeit.
4.  **Vergleich:** Geben Sie den Performance-Faktor auf der Konsole aus (z.B. "Vektorisierung war 50x schneller").
