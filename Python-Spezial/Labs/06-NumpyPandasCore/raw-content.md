# LAB 06 DETAILS:

* **Lab Title/Topic:** Numpy & Pandas
* **Learning Objectives:**
    * Tabellarische Daten in Dataframes laden und bestimmte Spalten/Zeilen auswählen.
    * Advanced: Vektorisierung verstehen (Vermeidung von Loops), Performance-Unterschiede zu Listen kennen.
* **Context & Slide Summary:** 
    - ndarray Basics
    - Pandas DataFrame & Series
    - Indexing & Slicing
    - Advanced: Vectorization vs. Loops

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

## `Lab_06_Angabe.md`

# Lab 06: Numpy & Pandas Data Analysis

### Szenario

Die Datenmengen wachsen. Die IT-Abteilung hat Ihnen einen Extrakt von 100.000 Transaktionen bereitgestellt. Excel stürzt ab, und reine Python-Listen sind zu langsam und unübersichtlich. Sie nutzen nun Pandas, um den Datensatz zu laden, "High-Risk"-Transaktionen zu filtern und Währungsumrechnungen performant durchzuführen.

### Voraussetzungen

  * Installation von Pandas und Numpy:

    ```bash
    pip install pandas numpy
    ```

  * **Datengenerierung:** Führen Sie bitte *vor* dem Lab dieses Skript aus, um eine realistische CSV-Datei (`big_transactions.csv`) zu erzeugen:

    ```python
    import pandas as pd
    import numpy as np

    # Wir simulieren 100.000 Datensätze
    count = 100_000
    print(f"Generiere {count} Transaktionen...")

    data = {
        'transaction_id': np.arange(count),
        'amount': np.random.uniform(1.0, 5000.0, count).round(2),
        'currency': np.random.choice(['EUR', 'USD', 'GBP'], count),
        'type': np.random.choice(['deposit', 'withdrawal', 'payment'], count)
    }

    df = pd.DataFrame(data)
    df.to_csv('big_transactions.csv', index=False)
    print("Fertig: 'big_transactions.csv' erstellt.")
    ```

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

-----

## `Lab_06_Lösung.md`

# Lösung Lab 06

### Lösungsansatz

  * **Pandas (Basis):** DataFrames ermöglichen SQL-ähnliche Abfragen direkt in Python. `df[Bedingung]` ist der Standard-Weg zum Filtern (Boolean Indexing).
  * **Vektorisierung (Bonus):** Pandas und Numpy führen Operationen auf C-Ebene aus. Wenn wir `df['a'] * df['b']` schreiben, wird der Loop in kompiliertem C-Code ausgeführt. Nutzen wir `for row in df:`, zwingen wir Python, für jede Zeile Objekte zu erzeugen und Typen zu prüfen. Der Unterschied liegt oft im Faktor 100x bis 1000x.

-----

### Code: Basis Aufgabe

```python
import pandas as pd

def analyze_transactions():
    # 1. Laden
    print("Lade Daten...")
    df = pd.read_csv('big_transactions.csv')
    
    # 2. Inspektion
    print("\n--- Info ---")
    print(df.info())
    print("\n--- Head ---")
    print(df.head())
    
    # 3. Filterung
    # Filter: Nur USD
    usd_mask = df['currency'] == 'USD'
    usd_transactions = df[usd_mask]
    
    # Filter: Große Abhebungen (> 2000 UND type == withdrawal)
    # Beachten Sie die Klammern () bei mehreren Bedingungen & operator
    risk_mask = (df['amount'] > 2000.00) & (df['type'] == 'withdrawal')
    large_withdrawals = df[risk_mask]
    
    # 4. Reporting
    count = len(large_withdrawals)
    total_amount = large_withdrawals['amount'].sum()
    
    print("\n--- Report ---")
    print(f"Anzahl USD Transaktionen: {len(usd_transactions)}")
    print(f"Anzahl Risiko-Abhebungen: {count}")
    print(f"Summe Risiko-Beträge: {total_amount:,.2f}")

if __name__ == "__main__":
    analyze_transactions()
```

-----

### Code: Bonus Herausforderung

```python
import pandas as pd
import numpy as np
import time

def performance_benchmark():
    df = pd.read_csv('big_transactions.csv')
    print(f"\nStarte Benchmark mit {len(df)} Zeilen...")

    # --- METHODE 1: Iterrows (Der "langsame" Weg) ---
    start_time = time.time()
    
    converted_amounts = []
    # iterrows ist bekanntermaßen langsam, da es Series-Objekte pro Zeile erstellt
    for index, row in df.iterrows():
        if row['currency'] == 'USD':
            converted_amounts.append(row['amount'] * 0.90)
        elif row['currency'] == 'GBP':
            converted_amounts.append(row['amount'] * 1.15)
        else:
            converted_amounts.append(row['amount'])
    
    df['amount_eur_loop'] = converted_amounts
    
    duration_loop = time.time() - start_time
    print(f"Dauer Loop: {duration_loop:.4f} Sekunden")

    # --- METHODE 2: Vektorisierung (Der "Pandas" Weg) ---
    start_time = time.time()
    
    # Bedingungen definieren
    conditions = [
        (df['currency'] == 'USD'),
        (df['currency'] == 'GBP')
    ]
    
    # Werte definieren, die bei True gewählt werden
    choices = [
        df['amount'] * 0.90,
        df['amount'] * 1.15
    ]
    
    # np.select(Bedingungen, Auswahl, Default)
    df['amount_eur_vec'] = np.select(conditions, choices, default=df['amount'])
    
    duration_vec = time.time() - start_time
    print(f"Dauer Vektor: {duration_vec:.4f} Sekunden")

    # --- FAZIT ---
    if duration_vec > 0:
        factor = duration_loop / duration_vec
        print(f"\n>>> Vektorisierung war {factor:.1f}x schneller! <<<")

if __name__ == "__main__":
    performance_benchmark()
```
