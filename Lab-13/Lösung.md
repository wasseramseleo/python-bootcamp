# Lab 13: Daten-Analyse mit Pandas - Lösung

## Erläuterung der Lösung

### Angabe

Die Lösung folgt einem Standard-Workflow der Datenanalyse: Laden, Inspizieren, Bereinigen, Filtern, Analysieren.

1.  **Laden & Inspizieren**: `pd.read_csv` liest die Datei in einen DataFrame. `info()` ist entscheidend, um zu sehen, ob Spalten die richtigen Datentypen haben (z.B. `amount` als `float64`) und ob Daten fehlen (non-null count). `describe()` gibt einen schnellen Überblick über die Verteilung der numerischen Daten.
2.  **Bereinigung**: `df[df['status'] == 'COMPLETED']` ist der Kern von Pandas: **Boolean Indexing** (oder "Masking").
      * `df['status'] == 'COMPLETED'` erstellt eine *Series* von True/False-Werten.
      * `df[...]` (wobei `...` die Series ist) behält nur die Zeilen, bei denen der Wert `True` war. Wir speichern dies in `df_completed`, da Analysen auf fehlgeschlagenen Transaktionen oft unerwünscht sind.
3.  **Filtern**: Wir wenden Boolean Indexing erneut an, diesmal mit zwei Bedingungen. Der `&` (logisch UND) Operator ist zwingend. (Klammern um die einzelnen Bedingungen sind aufgrund der Operator-Rangfolge in Python/Pandas erforderlich).
4.  **Groupby**: Dies ist die "Split-Apply-Combine"-Logik:
      * **Split**: `df_completed.groupby('account_id')` teilt den DataFrame in separate "Töpfe" für jedes einzigartige Konto (AT123, DE456, CH789).
      * **Apply**: `.sum()` wird auf die `['amount']`-Spalte *innerhalb* jedes "Topfes" angewendet.
      * **Combine**: Pandas fügt die Ergebnisse (die Summen) in einer neuen Series zusammen, indiziert nach den Gruppennamen (den `account_id`s).

### Bonus-Herausforderung

1.  **Multi-Level Grouping**: `groupby` kann eine Liste von Spalten annehmen (`['account_id', 'transaction_type']`). Pandas erstellt eine "MultiIndex"-Ausgabe, die alle Kombinationen (z.B. AT123-DEPOSIT, AT123-WITHDRAW) anzeigt.
2.  **`.agg()`**: Die `.agg()`-Methode ist extrem mächtig. Statt nur eine Aggregation (wie `.sum()`) anzuwenden, können wir eine Liste von Aggregationsfunktionen (als Strings: `'sum'`, `'mean'`, `'count'`) übergeben, um eine reichhaltige Zusammenfassungstabelle zu erhalten.
3.  **Fehleranalyse**:
      * Wir filtern zuerst den `df` nach fehlgeschlagenen Transaktionen (`df_failed`).
      * `df_failed['amount'].idxmax()` findet den *Index* (in diesem Fall `T1012`) des Maximalwerts in der `amount`-Spalte.
      * `df.loc[index_label]` wird verwendet, um die *gesamte Zeile* basierend auf ihrem Index-Label (das wir in Schritt 1 beim Laden nicht explizit gesetzt haben, also verwendet Pandas die `transaction_id` *nicht* als Index. `.idxmax()` gibt den Zeilen-Index zurück. *Korrektur:* `read_csv` verwendet einen 0-basierten Index. `idxmax()` gibt diesen 0-basierten Index zurück. `.loc` kann diesen Index verwenden).
      * *Präzisere Lösung:* Es ist sauberer, `transaction_id` als Index zu setzen, falls wir label-basiert arbeiten wollen. Aber für diese Lösung bleiben wir beim Standard-Index.

## Python-Code: Angabe

```python
import pandas as pd

print("--- Angabe Test ---")

# 1. Laden und Inspizieren
try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    print("Fehler: transactions.csv nicht gefunden.")
    exit()

print("--- 1. Inspektion (Head) ---")
print(df.head())

print("\n--- 1. Inspektion (Info) ---")
df.info()

print("\n--- 1. Inspektion (Describe) ---")
print(df.describe())


# 2. Datenbereinigung (Filtern)
# Erstelle eine Maske für 'COMPLETED' Status
mask_completed = (df['status'] == 'COMPLETED')
df_completed = df[mask_completed]

print(f"\n--- 2. Datenbereinigung ---")
print(f"Originale Einträge: {len(df)}, Bereinigte Einträge: {len(df_completed)}")


# 3. Selektion und Filterung (Masking)
print("\n--- 3. Filterung (DEPOSIT > 500) ---")
# Kombinierte Maske (anhand df_completed)
mask_deposits = (df_completed['transaction_type'] == 'DEPOSIT')
mask_high_value = (df_completed['amount'] > 500)

high_value_deposits = df_completed[mask_deposits & mask_high_value]
print(high_value_deposits)


# 4. Analyse (Groupby)
print("\n--- 4. Analyse (Summe pro Konto) ---")
# Split-Apply-Combine
account_totals = df_completed.groupby('account_id')['amount'].sum()
print(account_totals)
```

## Python-Code: Bonus-Herausforderung

```python
import pandas as pd

# Annahme: df und df_completed sind bereits aus der Angabe geladen
try:
    df = pd.read_csv("transactions.csv")
    df_completed = df[df['status'] == 'COMPLETED']
except FileNotFoundError:
    print("Fehler: transactions.csv nicht gefunden.")
    exit()

print("\n--- Bonus-Herausforderung ---")

# 1. Multi-Level Grouping
print("\n--- 1. Multi-Level Grouping (Konto & Typ) ---")
multi_level_summary = df_completed.groupby(['account_id', 'transaction_type'])['amount'].sum()
print(multi_level_summary)


# 2. Komplexe Aggregation (.agg())
print("\n--- 2. Aggregation (Details pro Typ) ---")
type_summary = df_completed.groupby('transaction_type')['amount'].agg(
    ['count', 'sum', 'mean', 'max']
)
print(type_summary)


# 3. Fehleranalyse (Höchste fehlgeschlagene Transaktion)
print("\n--- 3. Fehleranalyse (Höchste FAILED Tx) ---")

# Filtern nach FAILED
df_failed = df[df['status'] == 'FAILED']

if not df_failed.empty:
    # Finde den INDEX der Zeile mit dem max. Betrag
    idx_max_failed = df_failed['amount'].idxmax()
    
    # .loc verwenden, um die gesamte Zeile anhand ihres Index zu holen
    highest_failed_tx = df.loc[idx_max_failed]
    
    print("Transaktion mit höchstem FAILED-Betrag:")
    print(highest_failed_tx)
else:
    print("Keine FAILED-Transaktionen gefunden.")
```