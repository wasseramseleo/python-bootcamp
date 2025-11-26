**Input Data:**

* **Topic Title:** 7. Datenaufbereitung (Wrangling)
* **Content Points:**
    - Missing Values behandeln
    - GroupBy & Aggregationen
    - Merging & Concatenation
* **Lab Objectives:**
    * Daten filtern, einfache Summen/Mittelwerte berechnen (Pivot) und Tabellen verbinden.
    * Advanced: + Komplexe apply-Funktionen schreiben, Multi-Indizes handhaben und Zeitreihen-Manipulation.

-----

Here are the slides for **Topic 7: Datenaufbereitung (Wrangling)**, focusing on cleaning and restructuring datasets within the Bird Ringing domain.

-----

**Slide 1: Umgang mit Fehlenden Daten (Missing Values)**

**Body Text (German):**

  * **NaN (Not a Number):** Pandas markiert fehlende Werte als `NaN`. Diese entstehen oft durch Eingabefehler oder defekte Messinstrumente (z.B. Waage ausgefallen).
  * **Strategien:**
      * **Drop:** Löschen der gesamten Zeile (`dropna()`). Radikal, aber sicherste Methode für statistische Signifikanz, wenn der Datensatz groß genug ist.
      * **Imputation:** Auffüllen (`fillna()`) mit Mittelwert (`mean`) oder letztem bekannten Wert (`ffill`). **Kritisch:** Dies verfälscht die Varianz der Daten und darf wissenschaftlich nur begründet erfolgen.
  * **Analyse:** Prüfen Sie immer zuerst mit `df.isna().sum()`, wie viele Daten fehlen.

**Code Snippet (Python):**

```python
# Check for missing values
missing_count = df.isna().sum()

# Strategy 1: Remove birds with unknown sex
clean_df = df.dropna(subset=['sex'])

# Strategy 2: Impute missing weight with species average (Risky!)
# Only use if you understand the bias introduced
mean_weight = df['weight_g'].mean()
df['weight_g'] = df['weight_g'].fillna(mean_weight)
```

**Speaker Notes (German):**
Echte Daten sind schmutzig. Vielleicht wurde das Geschlecht nicht bestimmt oder die Waage war leer. Pandas nutzt `NaN` als Platzhalter. Sie haben zwei Optionen: Löschen oder Raten (Imputation). Seien Sie als Wissenschaftler vorsichtig mit `.fillna(mean)`: Wenn Sie fehlende Gewichte einfach mit dem Durchschnitt auffüllen, reduzieren Sie künstlich die natürliche Streuung (Standardabweichung) Ihrer Population. Das kann Ihre Studienergebnisse invalidieren.

**Image Prompt:** A visualization of a data table with holes (missing puzzle pieces). One path shows the row being discarded, the other shows a piece being fabricated to fit the hole.

-----

**Slide 2: GroupBy & Aggregationen**

**Body Text (German):**

  * **Split-Apply-Combine:** Das Kernkonzept der Datenanalyse.
      * **Split:** Daten in Gruppen teilen (z.B. nach "Spezies").
      * **Apply:** Eine Funktion auf jede Gruppe anwenden (z.B. "Mittelwert berechnen").
      * **Combine:** Ergebnisse wieder zusammenfügen.
  * **Aggregation:** Reduktion von vielen Datenpunkten auf eine Kennzahl (Mean, Sum, Count, Min, Max).

**Code Snippet (Python):**

```python
# Calculate statistics per species
species_stats = df.groupby('species')['weight_g'].agg(['mean', 'count', 'std'])

print(species_stats)
# Output example:
#               mean  count   std
# Parus major   18.2    150   1.1
# Cyanistes...  11.5    120   0.9
```

**Speaker Notes (German):**
Wir wollen selten den *einzelnen* Vogel betrachten, sondern die Population. `groupby` ist der Schlüssel. Wir gruppieren alle Kohlmeisen in einen Eimer und alle Blaumeisen in einen anderen. Dann wenden wir Aggregationen an: "Wie schwer ist die durchschnittliche Meise?". Mit `.agg()` können wir mehrere Metriken gleichzeitig berechnen (Mittelwert, Anzahl, Standardabweichung), um sofort Ausreißer in Gruppen zu erkennen.

**Image Prompt:** A diagram showing the "Split-Apply-Combine" process: A mixed pile of colored balls is separated into buckets by color (Split), weighed (Apply), and the results listed on a board (Combine).

-----

**Slide 3: Merging & Concatenation**

**Body Text (German):**

  * **Concatenation (`pd.concat`):** Stapeln von Daten.
      * *Anwendung:* Sie haben `daten_montag.csv` und `daten_dienstag.csv` und wollen eine lange Liste. (Vertikales Zusammenfügen).
  * **Merging (`pd.merge`):** Verknüpfen über Schlüssel (ähnlich SQL `JOIN`).
      * *Anwendung:* Sie haben eine Tabelle "Fänge" (mit Ringnummer) und eine Tabelle "Wiederfunde" (mit Ringnummer). Sie verknüpfen beide, um die Historie eines Vogels zu sehen. (Horizontales Zusammenfügen).
  * **Join-Typen:** `inner` (nur Treffer), `left` (alle von links, Treffer von rechts), `outer` (alles).

**Code Snippet (Python):**

```python
# Concatenation (Stacking days)
all_captures = pd.concat([monday_df, tuesday_df])

# Merging (Enriching data)
# capt_df has 'site_id', sites_df has 'site_id' + 'coordinates'
enriched_df = pd.merge(
    capt_df, 
    sites_df, 
    on='site_id', 
    how='left' # Keep all captures, add coords where known
)
```

**Speaker Notes (German):**
Anfänger verwechseln oft `concat` und `merge`. `Concat` macht die Tabelle länger (mehr Zeilen) – wie das Zusammenheften von Tagesberichten. `Merge` macht die Tabelle breiter (mehr Spalten) – wir reichern Daten an. Wenn Sie Capture-Daten haben, aber die GPS-Koordinaten in einer anderen Excel-Liste stehen, nutzen Sie `pd.merge` mit der Standort-ID als Schlüssel, genau wie ein VLOOKUP in Excel oder JOIN in SQL.

**Image Prompt:** Venn diagrams illustrating SQL Join types (Inner, Left, Right, Outer) applied to two data rectangles labeled "Captures" and "Site Info".

-----

**Slide 4: Pivot Tables (Advanced Summary)**

**Body Text (German):**

  * **Pivotierung:** Transformiert "lange" Listen in "breite" Übersichten (Matrix).
  * **Dimensionen:** Ermöglicht die Analyse von Daten über zwei Achsen (z.B. Spezies vs. Monat).
  * **Margins:** Fügt automatisch Zeilen- und Spaltensummen ("All") hinzu.
  * **Heatmaps:** Pivot-Tabellen sind die perfekte Vorstufe für Heatmap-Visualisierungen.

**Code Snippet (Python):**

```python
# Create a summary matrix
# Rows: Species, Columns: Sex, Values: Average Wing Length
summary = df.pivot_table(
    values='wing_len', 
    index='species', 
    columns='sex', 
    aggfunc='mean',
    margins=True # Adds 'All' row/col
)
```

**Speaker Notes (German):**
Die `pivot_table` ist das mächtigste Reporting-Tool in Pandas. Statt abstrakter Listen erhalten wir eine Matrix. Sehen Sie sich den Code an: Wir wollen die Flügel-Länge aufgeschlüsselt nach Spezies (Zeilen) und Geschlecht (Spalten). Das Ergebnis ist sofort lesbar und report-fertig. Nutzen Sie `margins=True`, um Gesamtsummen zu erhalten.

**Image Prompt:** An animation showing a long, scrolling list of data folding itself up into a compact, grid-like matrix structure.

-----

**Slide 5: Advanced: Apply & Time Series (Expert Track)**

**Body Text (German):**

  * **Custom Functions (`apply`):** Wenn Vektorisierung nicht möglich ist (komplexe If-Else-Logik pro Zeile), nutzen Sie `apply()`. *Hinweis: Langsamer als native Pandas-Funktionen.*
  * **Time Series Resampling:** Aggregation von Zeitreihen auf neue Intervalle (z.B. von "pro Sekunde" auf "pro Tag").
  * **Rolling Windows:** Berechnet gleitende Durchschnitte, um Trends in verrauschten Daten zu erkennen.

**Code Snippet (Python):**

```python
# Complex logic requiring row-by-row inspection
def classify_age(row):
    if row['plumage_code'] == 'J' and row['month'] < 6:
        return 'Juvenile'
    return 'Adult'

df['age_class'] = df.apply(classify_age, axis=1)

# Time Series: Resample daily captures to weekly sums
weekly_counts = df.set_index('date').resample('W').size()
```

**Speaker Notes (German):**
Für die Experten: Manchmal reicht Standard-Logik nicht. Wenn Sie das Alter eines Vogels basierend auf Mauser-Code *und* Monat bestimmen müssen, schreiben Sie eine Python-Funktion und wenden sie mit `apply` an. Vorsicht bei der Performance! Im unteren Teil sehen Sie `resample`. Damit können Sie hochfrequente Daten (z.B. jede Beringung) auf Wochen-Summen herunterbrechen – essenziell für Migrations-Trends.

**Image Prompt:** A calendar focusing on days, then zooming out to group them into weeks, visualizing the aggregation of time-series data.

-----

**Slide 6: Lab Preparation**

**Body Text (German):**

  * **Szenario:** Datenbereinigung nach einer chaotischen Feldsaison.
  * **Aufgabe 1 (Cleaning):** Laden Sie den Datensatz `dirty_data.csv`. Identifizieren Sie Spalten mit `NaN` Werten und entscheiden Sie: Drop oder Fill?
  * **Aufgabe 2 (Group):** Berechnen Sie das Durchschnittsgewicht pro Spezies.
  * **Aufgabe 3 (Merge):** Laden Sie `geo_locations.csv` und fügen Sie die Koordinaten an Ihren Hauptdatensatz an (`left join`).
  * **Aufgabe 4 (Expert - Time Series):**
      * Konvertieren Sie das Datum.
      * Nutzen Sie `resample`, um zu zählen, wie viele Vögel *pro Woche* gefangen wurden.
      * Erstellen Sie eine Pivot-Table: Zeilen=Woche, Spalten=Spezies.

**Code Snippet (Python):**

```python
# Lab Starter Hint
import pandas as pd

df = pd.read_csv("dirty_data.csv")
geo = pd.read_csv("geo_locations.csv")

# Merge hint
# merged = pd.merge(df, geo, on='...
```

**Speaker Notes (German):**
Das Lab simuliert den "Day After". Die Daten sind da, aber sie sind lückenhaft. Ihre Aufgabe: Machen Sie die Daten sauber. Verknüpfen Sie Standort-Daten. Die Experten erstellen am Ende eine Zeitreihe: Ich will sehen, in welcher Kalenderwoche der Zuzug der Rotkehlchen seinen Peak hatte. Dazu müssen Sie Resampling und Pivot kombinieren.

**Image Prompt:** A workspace showing "Dirty Data" entering a filter funnel and emerging as clean, structured charts and tables on a monitor.
