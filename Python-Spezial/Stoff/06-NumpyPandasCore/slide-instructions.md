**Input Data:**

* **Topic Title:** 6. Numpy & Pandas Core
* **Content Points:**
    - ndarray Basics
    - Pandas DataFrame & Series
    - Indexing & Slicing
* **Lab Objectives:**
    * Tabellarische Daten in Dataframes laden und bestimmte Spalten/Zeilen auswählen.
    * Advanced: Vektorisierung verstehen (Vermeidung von Loops), Performance-Unterschiede zu Listen kennen.

-----

Here are the slides for **Topic 6: Numpy & Pandas Core**, focusing on data manipulation within the Bird Ringing domain.

-----

**Slide 1: Numpy & ndarray Basics**

**Body Text (German):**

  * **ndarray (N-dimensional Array):** Der fundamentale Baustein für numerische Daten in Python. Im Gegensatz zu Listen müssen alle Elemente denselben Datentyp haben (z.B. nur `float64`).
  * **Performance:** Numpy-Arrays liegen kompakt im Speicher (C-Level) und sind bei Berechnungen 10x bis 100x schneller als Python-Listen.
  * **Vectorization:** Operationen werden auf das gesamte Array gleichzeitig angewendet, ohne explizite Loops zu schreiben.

**Code Snippet (Python):**

```python
import numpy as np

# List of wing lengths (mm)
wings_list = [74.5, 72.1, 78.0, 69.5]

# Convert to Numpy Array
wings_arr = np.array(wings_list)

# Vectorized operation: Convert all to cm instantly
# No loop needed!
wings_cm = wings_arr / 10.0 

print(f"Mean Wing Length: {wings_arr.mean()} mm")
```

**Speaker Notes (German):**
Bevor wir zu Tabellen kommen, brauchen wir das Fundament: Numpy. Stellen Sie sich vor, Sie haben 100.000 Messwerte. Eine Python-Liste ist langsam, weil sie für jedes Element Speichertypen prüfen muss. Ein `ndarray` ist ein kompakter Block im Speicher, wie in C. Das Wichtigste: Wir nutzen keine Loops für Mathe. Wir teilen das Array einfach durch 10, und Numpy erledigt das für alle Elemente gleichzeitig.

**Image Prompt:** A comparison graphic: Top shows a Python List as scattered pointers to objects in memory (messy). Bottom shows a Numpy Array as a tightly packed, contiguous block of data (clean, streamlined).

-----

**Slide 2: Pandas Series & DataFrame**

**Body Text (German):**

  * **Pandas:** Baut auf Numpy auf und bringt Struktur in die Daten (Tabellenkalkulation für Python).
  * **Series:** Eine einzelne Spalte mit Daten. Sie hat einen `Index` (Labels) und `Values`.
  * **DataFrame:** Eine Tabelle. Sie ist technisch gesehen eine Kollektion von Series, die denselben Index teilen.
  * **Analogie:** Denken Sie an Excel: Ein DataFrame ist das ganze Sheet, eine Series ist eine Spalte.

**Code Snippet (Python):**

```python
import pandas as pd

# Data representing a single ringing session
data = {
    "ring_id": ["AX-01", "AX-02", "AX-03"],
    "species": ["Rotkehlchen", "Amsel", "Rotkehlchen"],
    "weight_g": [17.5, 98.2, 18.1]
}

# Create DataFrame
df = pd.read_csv("capture_data.csv") # Or from dict above
# df = pd.DataFrame(data)

print(df.info()) # Shows data types and missing values
```

**Speaker Notes (German):**
Pandas ist Ihr Excel auf Steroiden. Wir haben zwei Hauptobjekte: `Series` (1D, eine Liste von Werten) und `DataFrame` (2D, Zeilen und Spalten). Das `df.info()` ist Ihr bester Freund – es zeigt sofort, welche Spalten existieren und ob Daten fehlen (Null Values), noch bevor Sie die Tabelle überhaupt ansehen.

**Image Prompt:** A visual assembly diagram: Multiple vertical strips labeled "Series" being clicked together to form a solid grid labeled "DataFrame".

-----

**Slide 3: Indexing & Slicing**

**Body Text (German):**

  * **Column Access:** Spalten werden wie Dictionary-Keys ausgewählt: `df['species']`.
  * **Row Access (`.iloc`):** Auswahl basierend auf der *Position* (Integer). `iloc[0]` ist die erste Zeile.
  * **Row Access (`.loc`):** Auswahl basierend auf dem *Label* oder einer Bedingung.
  * **Boolean Indexing:** Der mächtigste Filter. Wir übergeben eine Liste von Wahr/Falsch-Werten, um Zeilen zu filtern.

**Code Snippet (Python):**

```python
# Select single column (Returns a Series)
species_col = df['species']

# Boolean Indexing (Filter rows)
# Get all birds heavier than 20g
heavy_birds = df[df['weight_g'] > 20.0]

# Combine Logic
robins = df[(df['species'] == 'Rotkehlchen') & (df['weight_g'] > 18.0)]
```

**Speaker Notes (German):**
Daten laden ist einfach, Daten filtern ist die Kunst. Merken Sie sich: `[]` für Spalten. Für Zeilen nutzen wir meistens Boolean Indexing. Das Beispiel `df['weight_g'] > 20.0` erzeugt intern eine Liste von True/False. Pandas zeigt uns dann nur die Zeilen an, die "True" sind. Das ist viel lesbarer als komplexe SQL-Statements.

**Image Prompt:** A spreadsheet where rows unrelated to the query are faded out/blurred, while the selected rows (e.g., Heavy Birds) are highlighted and sharp.

-----

**Slide 4: Vectorization vs. Loops (Expert Track)**

**Body Text (German):**

  * **Anti-Pattern:** Iterieren Sie **niemals** mit einem `for`-Loop über einen DataFrame (`for index, row in df.iterrows()`), um Werte zu ändern. Das ist extrem langsam.
  * **Vectorization:** Nutzen Sie die eingebauten Pandas/Numpy-Funktionen. Diese laufen in kompiliertem C-Code ab (SIMD-Instruktionen).
  * **Apply:** Wenn keine Vektor-Operation möglich ist, nutzen Sie `.apply()`, aber sparsam.

**Code Snippet (Python):**

```python
import time

# BAD: Looping (Slow)
start = time.time()
for index, row in df.iterrows():
    df.at[index, 'bmi'] = row['weight_g'] / row['wing_len']
print(f"Loop time: {time.time() - start}")

# GOOD: Vectorization (Fast)
start = time.time()
df['bmi'] = df['weight_g'] / df['wing_len']
print(f"Vector time: {time.time() - start}")
```

**Speaker Notes (German):**
An die Experten: "The Loop is the enemy". In Python sind Loops langsam. Wenn Sie `iterrows` benutzen, wird jede Zeile einzeln in ein Python-Objekt umgewandelt. Bei 1 Million Zeilen warten Sie Minuten. Die vektorisierte Variante (unten) dauert Millisekunden. Pandas schiebt die Berechnung in den C-Layer. Schreiben Sie Pandas-Code so, als ob die ganze Spalte eine einzige Zahl wäre.

**Image Prompt:** A race track comparison: A person walking step-by-step (Loop) vs. a high-speed train moving everyone at once (Vectorization).

-----

**Slide 5: Lab Preparation**

**Body Text (German):**

  * **Szenario:** Analyse eines großen Datensatzes von Herbst-Migrationen.
  * **Aufgabe 1 (Basics):** Laden Sie die `migration_data.csv`. Geben Sie die ersten 5 Zeilen (`head`) und die Datentypen aus.
  * **Aufgabe 2 (Selection):** Erstellen Sie einen neuen DataFrame, der nur "Species" und "Weight" enthält.
  * **Aufgabe 3 (Filter):** Filtern Sie alle Datensätze der Spezies "Sylvia atricapilla" (Mönchsgrasmücke), die nach dem 01.10. gefangen wurden.
  * **Aufgabe 4 (Advanced - Performance):** Schreiben Sie eine Funktion, die den "Fat Score" normalisiert. Messen Sie die Zeitunterschiede zwischen einem `for`-Loop und der direkten Vektorisierung bei 100.000 Zeilen.

**Code Snippet (Python):**

```python
# Lab Starter
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("materials/migration_data.csv")

# Hint for Task 3
# Ensure date column is actually datetime type first!
df['date'] = pd.to_datetime(df['date'])
```

**Speaker Notes (German):**
Wir öffnen die Werkzeugkiste. Sie bekommen eine CSV-Datei mit Rohdaten. Versuchen Sie zuerst, ein Gefühl für die Daten zu bekommen (`head`, `info`). Die Anfänger üben das "Slicen" der Tabelle. Die Fortgeschrittenen unter Ihnen möchte ich schwitzen sehen: Beweisen Sie mir mit dem `time`-Modul, wie viel schneller Vektorisierung wirklich ist.

**Image Prompt:** A laptop screen showing a Jupyter Notebook interface with a DataFrame displayed, alongside a stopwatch measuring execution time.
