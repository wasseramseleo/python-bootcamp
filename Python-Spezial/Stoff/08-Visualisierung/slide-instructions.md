**Input Data:**

* **Topic Title:** 8. Datenvisualisierung
* **Content Points:**
    - Plotly Express
    - Interaktive Charts
    - Export von Grafiken
* **Lab Objectives:**
    * Standard-Diagramme (Bar, Line, Scatter) interaktiv erstellen.
    * Advanced: Dashboards layouts anpassen, Subplots erstellen und Custom-Styling anwenden.

-----

Here are the slides for the final topic: **8. Datenvisualisierung**, focusing on interactive plotting with Plotly Express within the Bird Ringing domain.

-----

**Slide 1: Einführung in Plotly Express**

**Body Text (German):**

  * **Warum Plotly?** Im Gegensatz zu statischen Bibliotheken (wie Matplotlib/Seaborn) erstellt Plotly interaktive Grafiken für den Browser (HTML/JS Basis).
  * **Interaktivität:** Funktionen wie Zoom, Pan, Mouseover-Tooltips und das Ausblenden von Legenden-Einträgen sind standardmäßig integriert.
  * **Plotly Express (`px`):** Die High-Level-API. Sie ermöglicht komplexe Charts mit minimalem Code ("Tidy Data" Format wird erwartet, d.h. ein DataFrame pro Chart).

**Code Snippet (Python):**

```python
import plotly.express as px
import pandas as pd

# Load prepared data
df = pd.read_csv("clean_ringing_data.csv")

# Basic workflow: One-liner command -> interactive figure
fig = px.scatter(df, x="wing_length_mm", y="weight_g")
fig.show() # Opens in browser/notebook
```

**Speaker Notes (German):**
Wir schließen den Kurs mit der Visualisierung. Wir nutzen Plotly Express. Der entscheidende Vorteil ist die Interaktivität: Sie erzeugen keine toten PNG-Bilder, sondern kleine Web-Applikationen. Ihre Kollegen können in die Daten hineinzoomen und Details per Mouseover sehen, ohne dass Sie dafür Code schreiben müssen. `px` ist der Standard-Import.

**Image Prompt:** A screenshot of a web browser displaying a Plotly chart, highlighting the interactive toolbar (zoom, pan buttons) in the top right corner and a tooltip pop-up displaying data values upon hovering mouse cursor.

-----

**Slide 2: Scatter Plots & Korrelationen**

**Body Text (German):**

  * **Anwendung:** Ideal zur Darstellung der Beziehung zwischen zwei numerischen Variablen (z.B. Flügel-Länge vs. Gewicht).
  * **Dimensionen:** Weitere Informationen können durch Farbe (`color`), Größe (`size`) oder Symbol (`symbol`) kodiert werden.
  * **Hover Data:** Definieren Sie, welche zusätzlichen Spalten im Tooltip angezeigt werden sollen, wenn die Maus über einem Punkt verweilt.

**Code Snippet (Python):**

```python
fig = px.scatter(
    df, 
    x="wing_length_mm", 
    y="weight_g",
    color="species",     # Different color per species
    size="fat_score",    # Larger points = more fat reserves
    hover_data=['ring_id', 'date'], # Extra info in tooltip
    title="Morphometric Analysis: Wing vs. Weight"
)
fig.show()
```

**Speaker Notes (German):**
Ein klassischer Scatter Plot für biometrische Daten. Sehen Sie, wie einfach wir Dimensionen hinzufügen: Wir färben nach Spezies ein und die Größe des Punktes zeigt den Fett-Score des Vogels. Das `hover_data` Argument ist extrem wichtig für die explorative Analyse: Fahren Sie über einen Ausreißer, und Sie sehen sofort die Ringnummer und das Datum.

**Image Prompt:** A scatter plot showing a positive correlation between wing length and weight. Points are differently colored based on bird species, and a tooltip shows details for a specific point "Ring: AX-99, Date: 2024-09-10".

-----

**Slide 3: Bar Charts & Vergleiche**

**Body Text (German):**

  * **Anwendung:** Vergleich von Kategorien (z.B. Anzahl der Fänge pro Spezies oder pro Standort).
  * **Datenbasis:** Plotly kann Rohdaten selbst aggregieren, aber es ist oft sauberer, einen vorbereiteten (gruppierten) DataFrame zu übergeben.
  * **Orientierung:** Horizontale Balken (`orientation='h'`) sind oft besser lesbar bei vielen oder langen Kategorienamen.

**Code Snippet (Python):**

```python
# Pre-aggregated data (e.g., from groupby)
top_species = df['species'].value_counts().nlargest(10).reset_index()
top_species.columns = ['species', 'count']

fig = px.bar(
    top_species,
    x="count",
    y="species",
    orientation='h', # Horizontal bars
    text="count",    # Display values on bars
    title="Top 10 Most Captured Species"
)
fig.update_traces(textposition='outside') # Style text labels
fig.show()
```

**Speaker Notes (German):**
Für kategoriale Vergleiche nutzen wir Balkendiagramme. Ein Tipp für die Praxis: Wenn Sie viele Spezies haben, nutzen Sie horizontale Balken, damit man die Namen lesen kann, ohne den Kopf zu verdrehen. Hier übergeben wir bereits aggregierte Daten (Top 10 Liste), was oft performanter ist und mehr Kontrolle bietet.

**Image Prompt:** A horizontal bar chart titled "Top 10 Species", showing species names on the y-axis and capture counts on the x-axis, with the count value numerically labeled at the end of each bar.

-----

**Slide 4: Line Charts & Zeitreihen**

**Body Text (German):**

  * **Anwendung:** Visualisierung von Trends über die Zeit (z.B. Migrationsverlauf über das Jahr).
  * **Voraussetzung:** Das Datumsfeld muss ein echtes `datetime` Format sein, damit Plotly die X-Achse korrekt skaliert.
  * **Gruppierung:** Mit `color` können mehrere Linien (z.B. pro Jahr oder pro Spezies) in einem Chart dargestellt werden.

**Code Snippet (Python):**

```python
# Assuming 'date' is datetime and counts are aggregated daily
fig = px.line(
    daily_counts_df, 
    x="date", 
    y="captures",
    color="year", # Compare different years
    markers=True, # Add markers to line points
    title="Migration Phenology (Daily Captures)"
)
# Customize x-axis ticks
fig.update_xaxes(dtick="M1", tickformat="%b") # Ticks every Month, format "Jan", "Feb"...
fig.show()
```

**Speaker Notes (German):**
Für die Phänologie (wann ziehen die Vögel?) sind Liniendiagramme essenziell. Stellen Sie sicher, dass Ihre Zeitspalte korrekt formatiert ist. Plotly ist schlau genug, eine Zeitachse zu erkennen und bietet automatisch passende Zoom-Stufen an. Wir nutzen hier Farbe, um verschiedene Jahre zu vergleichen, um zu sehen, ob der Zug dieses Jahr früher oder später begann.

**Image Prompt:** A multi-line chart showing daily bird captures over a year. Different colored lines represent different years (e.g., 2023 vs 2024), showing peaks in spring and autumn migration periods.

-----

**Slide 5: Advanced Layouts & Export (Expert Track)**

**Body Text (German):**

  * **Faceting (Subplots):** Aufteilen des Charts in mehrere kleine Charts basierend auf einer Kategorie (`facet_col`, `facet_row`).
  * **Styling:** Anpassung von Titeln, Achsenbeschriftungen, Templates (`plotly_dark`, `seaborn` etc.) über `update_layout()`.
  * **Export:** Speichern der interaktiven Grafik als eigenständige HTML-Datei zur Weitergabe an Kollegen oder Vorgesetzte (benötigt keinen Python-Server zum Ansehen).

**Code Snippet (Python):**

```python
fig = px.histogram(
    df, 
    x="wing_length_mm",
    color="sex",
    facet_col="species", # Creates separate plot for each species
    facet_col_wrap=3,    # Max 3 plots per row
    title="Wing Length Distribution per Species & Sex",
    template="plotly_white"
)

# Adjust layout labels globally
fig.update_layout(yaxis_title="Count", xaxis_title="Wing Length (mm)")

# Save as standalone HTML file
fig.write_html("ringing_analysis_report.html")
```

**Speaker Notes (German):**
Für die Experten: Faceting ("Small Multiples") ist eine extrem mächtige Technik. Statt alles in einen Chart zu quetschen, erstellen wir automatisch ein Gitter von Charts, z.B. ein Histogramm pro Spezies. Am Ende exportieren wir das Ganze mit `.write_html()`. Sie erhalten eine Datei, die Sie per E-Mail an Ihren Chef schicken können, und er kann sie interaktiv im Browser öffnen, ganz ohne Python-Installation.

**Image Prompt:** A screen showing a grid of small histograms (facets), each representing a different bird species, all within a single Plotly figure frame with a clean white background style.

-----

**Slide 6: Lab Preparation**

**Body Text (German):**

  * **Szenario:** Erstellung eines interaktiven Berichts für die Feldsaison.
  * **Daten:** Nutzen Sie den bereinigten Datensatz aus dem vorherigen Lab (mit Zeitreihen und Kategorien).
  * **Aufgabe 1 (Scatter):** Erstellen Sie einen Scatter Plot von Flügel-Länge vs. Gewicht. Färben Sie nach Spezies. Fügen Sie Ring-ID als Hover-Info hinzu.
  * **Aufgabe 2 (Bar):** Erstellen Sie ein horizontales Balkendiagramm der Top 10 gefangenen Spezies.
  * **Aufgabe 3 (Expert - Dashboard):**
      * Erstellen Sie ein Liniendiagramm der wöchentlichen Fänge.
      * Nutzen Sie `facet_col='location_id'`, um die Trends der verschiedenen Fangstandorte nebeneinander zu vergleichen.
      * Exportieren Sie das Ergebnis als HTML.

**Code Snippet (Python):**

```python
# Lab Starter Hint
import plotly.express as px
import pandas as pd

df = pd.read_csv("final_lab_data.csv")

# Task 1 Starter
# fig1 = px.scatter(df, x=..., y=..., color=..., hover_data=[...])
# fig1.show()
```

**Speaker Notes (German):**
Im finalen Lab visualisieren wir unsere harte Arbeit. Die Einsteiger erstellen die Standard-Plots für die Biometrie und die Artenliste. Die Fortgeschrittenen bauen ein Mini-Dashboard: Ich möchte sehen, wie sich die Fangzahlen an den verschiedenen Standorten über die Zeit entwickeln, nebeneinander dargestellt mittels Faceting. Viel Erfolg\!

**Image Prompt:** A split screen showing a Python script on the left and a web browser on the right displaying the generated, interactive Plotly charts organized as a simple dashboard report.

-----

**End of Course Material**

This concludes the 8-topic curriculum based on the provided instructions.