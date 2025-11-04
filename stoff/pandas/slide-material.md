Hier sind die Inhalte für die Slides zum Thema "Data Analysis with Pandas".

-----

## Folie 1: Titel

**Titel:** 🐼 Datenanalyse mit Pandas
**Untertitel:** Die unverzichtbare Bibliothek für Data Science in Python

-----

## Folie 2: Das Problem: Python-Listen vs. "Daten"

**Titel:** Das Problem: Warum Python-Listen nicht ausreichen

Python ist flexibel, aber Standard-Listen oder Dictionaries sind für "tabellarische" Daten ungeeignet.

**Kritik (Evidence):**

  * **Keine Vektorisierung:** Eine Operation auf 1 Million Listenelemente erfordert eine langsame Python-`for`-Schleife.
  * **Keine Labels:** `data[0][4]` – Was bedeutet das? Spalten haben keine Namen.
  * **Mühsames Handling:** Operationen wie Gruppieren, Zusammenführen (Joins) oder der Umgang mit fehlenden Werten (`None`) müssen manuell implementiert werden.

**Pandas-Lösung:** Bietet Hochleistungs-Datenstrukturen (basierend auf NumPy), die speziell für tabellarische Datenanalyse optimiert sind.

-----

## Folie 3: Die Kern-Datenstrukturen (Series & DataFrame)

**Titel:** Die Kern-Datenstrukturen

Pandas hat zwei Hauptobjekte:

**1. `Series` (Die 1D-Struktur)**

  * Eine einzelne Spalte (ein 1D-Array).
  * Stellt man sich vor wie eine Spalte in Excel.
  * Hat einen **Index** (Labels für jede Zeile).

<!-- end list -->

```python
# s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
```

**2. `DataFrame` (Die 2D-Struktur)**

  * Die Haupt-Datenstruktur (eine Tabelle).
  * Stellt man sich vor wie ein Excel-Sheet oder eine SQL-Tabelle.
  * Ist im Grunde eine **Sammlung von `Series`-Objekten**, die sich einen Index teilen.

-----

## Folie 4: Daten einlesen (Der Startpunkt)

**Titel:** Daten einlesen (`pd.read_...`)

Pandas kann fast jedes gängige Datenformat direkt in einen DataFrame laden.

**Evidenz (Der häufigste Befehl):**

```python
import pandas as pd

# Liest eine CSV-Datei und leitet Spaltentypen/Header ab
df = pd.read_csv("sales_data.csv")

# Andere gängige Formate:
# df = pd.read_excel("report.xlsx")
# df = pd.read_json("api_response.json")
# df = pd.read_sql("SELECT * FROM users", db_connection)
```

Das Ergebnis `df` ist ein DataFrame-Objekt.

-----

## Folie 5: Erste Inspektion (Den Datensatz "verstehen")

**Titel:** Erste Inspektion (Die wichtigsten Befehle)

Nach dem Laden müssen Sie die Daten verstehen. Führen Sie **immer** diese Befehle aus:

  * `df.head()`
      * Zeigt die **ersten 5 Zeilen**. (Prüft, ob das Laden korrekt aussieht).
  * `df.info()`
      * **WICHTIG:** Zeigt Spaltennamen, die Anzahl der Nicht-Null-Werte und den Datentyp (`dtype`) jeder Spalte. (Zeigt fehlende Daten\!).
  * `df.describe()`
      * Generiert eine statistische Zusammenfassung (Mittelwert, Median, Min/Max, Quartile) für **numerische** Spalten.

<!-- end list -->

```python
# df.info() Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000 entries, 0 to 999
# Data columns (total 3 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   UserID     1000 non-null   int64
#  1   Product    950 non-null    object  <-- 50 fehlende Werte!
#  2   Price      1000 non-null   float64
```

-----

## Folie 6: Selektion 1: Spalten auswählen (`[]`)

**Titel:** Selektion: Spalten auswählen (Indexing)

Das Auswählen von Spalten (Projektion) ist intuitiv.

```python
# Syntax: df['Spaltenname']

# 1. Eine einzelne Spalte auswählen -> Ergibt eine Series
users = df['UserID']
# print(type(users)) # <class 'pandas.core.series.Series'>

# 2. Mehrere Spalten auswählen -> Ergibt einen DataFrame
# (Beachten Sie die doppelte Klammer: df[[list_of_names]])
user_data = df[['UserID', 'Product']]
# print(type(user_data)) # <class 'pandas.core.frame.DataFrame'>
```

-----

## Folie 7: Selektion 2: Zeilen auswählen (`.loc` & `.iloc`)

**Titel:** Selektion: Zeilen auswählen (`.loc` vs. `.iloc`)

**Kritik (Evidence):** Die `[]`-Syntax ist für Zeilen zweideutig. Verwenden Sie **immer** `.loc` oder `.iloc` für die Zeilenauswahl.

  * `.loc` (Label-basiert)

      * Wählt Zeilen basierend auf dem **Index-Label**.
      * `df.loc[5]` -\> Holt die Zeile mit dem Index-Label `5` (kann auch ein String sein, z.B. `'a'`).
      * `df.loc[5:10]` -\> Holt Zeilen `5` bis `10` (inklusive `10`\!).

  * `.iloc` (Integer-Position-basiert)

      * Wählt Zeilen basierend auf der **numerischen Position** (wie bei Python-Listen).
      * `df.iloc[5]` -\> Holt die 6. Zeile (0-basiert).
      * `df.iloc[5:10]` -\> Holt Position 5 bis 9 (exklusive `10`\!).

**Syntax (Bevorzugt): `df.loc[rows, columns]`**
`subset = df.loc[5:10, ['UserID', 'Price']]`

-----

## Folie 8: Filtern (Boolean Indexing / Masking)

**Titel:** Filtern (Boolean Indexing)

Dies ist der mächtigste Weg, um Daten basierend auf Bedingungen auszuwählen.

**Konzept (Die "Maske"):**

1.  Erstellen Sie eine `Series` von `True`/`False`-Werten (die "Maske").
2.  Übergeben Sie diese Maske an den DataFrame (`df[...]`).

<!-- end list -->

```python
df = pd.DataFrame({'age': [22, 45, 30], 'city': ['BER', 'NYC', 'BER']})

# 1. Die Bedingung (erzeugt eine Series [False, True, False])
mask = df['age'] > 40

# 2. Anwenden der Maske
# Pandas gibt nur die Zeilen zurück, bei denen die Maske True war.
old_users = df[mask]
# print(old_users) # Zeigt nur den 45-jährigen User

# --- Kombinierte Bedingungen ---
# & (und), | (oder). Klammern () sind zwingend!
mask_complex = (df['age'] > 25) & (df['city'] == 'BER')

users_berlin = df[mask_complex]
# print(users_berlin) # Zeigt nur den 30-jährigen User
```

-----

## Folie 9: 💡 Das Kernkonzept: `groupby` (Split-Apply-Combine)

**Titel:** Das Kernkonzept: `groupby` (Split-Apply-Combine)

`groupby` ist das wichtigste Werkzeug für fast jede Datenanalyse.

**Konzept (Evidenz):**

1.  **Split:** Teilt den DataFrame in Gruppen basierend auf einem Kriterium (z.B. "Stadt").
2.  **Apply:** Wendet eine Aggregations-Funktion auf jede Gruppe an (z.B. `sum()`, `mean()`, `count()`).
3.  **Combine:** Fügt die Ergebnisse zu einem neuen DataFrame zusammen.

<!-- end list -->

```python
# Frage: "Was ist der Durchschnittspreis pro Produktkategorie?"
# df hat Spalten: 'Category', 'Price'

# 1. Split (nach 'Category')
# 2. Apply (mean() auf 'Price')
# 3. Combine
avg_price_per_category = df.groupby('Category')['Price'].mean()

# Frage: "Wie viele Sales pro Stadt und Kategorie?"
sales_count = df.groupby(['City', 'Category'])['SalesID'].count()
```

-----

## Folie 10: Zusammenfassung

**Titel:** Key Takeaways

  * **DataFrame (2D):** Die primäre Datenstruktur. Eine Tabelle.
  * **Series (1D):** Eine einzelne Spalte.
  * **I/O:** `pd.read_csv()` (und andere) sind der Startpunkt.
  * **Inspektion:** `df.head()`, `df.info()`, `df.describe()` sind obligatorisch.
  * **Selektion:**
      * Spalten: `df[['Col_A', 'Col_B']]`
      * Zeilen: `.loc` (Label) oder `.iloc` (Position).
  * **Filtern (Evidenz):** Boolean Indexing (Masking) ist der Standard (`df[df['age'] > 30]`).
  * **Analyse (Kern):** `groupby()` (Split-Apply-Combine) ist das mächtigste Werkzeug zur Aggregation von Daten.