# LAB 08 DETAILS:

* **Lab Title/Topic:** Datenvisualisierung
* **Learning Objectives:**
    * Standard-Diagramme (Bar, Line, Scatter) interaktiv erstellen.
    * Advanced: Dashboards layouts anpassen, Subplots erstellen und Custom-Styling anwenden.
* **Context & Slide Summary:** 
    - Plotly Express
    - Interaktive Charts
    - Advanced: Layouts & Export von Grafiken

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

## `Lab_08_Angabe.md`

# Lab 08: Datenvisualisierung mit Plotly

### Szenario

Das Management ist begeistert von Ihren Zahlen, findet reine Tabellen aber ermüdend. Sie sollen ein interaktives Dashboard erstellen, das es den Managern ermöglicht, Umsätze per Mouse-Hover zu inspizieren und in Zeiträume hinein zu zoomen.

### Voraussetzungen

  * Installation von Plotly:

    ```bash
    pip install plotly pandas
    ```

  * **Daten-Setup:** Da wir saubere Daten brauchen, nutzen Sie bitte dieses Skript, um den DataFrame für die Übung zu generieren:

    ```python
    import pandas as pd
    import numpy as np

    # Reproduzierbare Daten erzeugen
    np.random.seed(42)
    dates = pd.date_range(start="2024-01-01", periods=100)

    df = pd.DataFrame({
        "date": np.repeat(dates, 3), # 3 Transaktionen pro Tag
        "region": np.random.choice(["EU", "US", "ASIA"], 300),
        "type": np.random.choice(["deposit", "withdrawal", "payment"], 300),
        "amount": np.random.uniform(10, 500, 300)
    })

    # Withdrawal/Payment negativ machen
    df.loc[df["type"] != "deposit", "amount"] *= -1

    print("Daten geladen. Zeilen:", len(df))
    ```

-----

### Teil 1: Basis Aufgabe

Ziel ist das Erstellen der zwei wichtigsten Chart-Typen im Banking: Entwicklung über Zeit (Line) und Vergleich von Kategorien (Bar).

**Anforderungen:**

1.  **Import:** Importieren Sie `plotly.express` als `px`.
2.  **Balkendiagramm (Bar Chart):**
      * Aggregieren Sie die Daten: Berechnen Sie die Summe von `amount` pro `region`. (Tipp: `groupby`).
      * Erstellen Sie ein Balkendiagramm (`px.bar`), das die Regionen auf der X-Achse und die Summen auf der Y-Achse zeigt.
      * Setzen Sie den Titel auf "Gesamtvolumen pro Region".
      * Zeigen Sie den Plot mit `.show()` an.
3.  **Liniendiagramm (Line Chart):**
      * Erstellen Sie eine kumulative Summe der Beträge über die Zeit (machen Sie dazu eine Kopie des DataFrames, sortieren Sie nach Datum und nutzen Sie `.cumsum()`).
      * Erstellen Sie ein Liniendiagramm (`px.line`), das den Verlauf des Gesamtkontostands der Bank über die Zeit zeigt.

-----

### Teil 2: Bonus Herausforderung

Ziel ist die Erstellung eines komplexen "Multidimensionalen Plots" und das Exportieren als Report.

**Anforderungen:**

1.  **Scatter Plot mit Faceting:**
      * Wir wollen Zusammenhänge erkennen. Erstellen Sie einen Scatter Plot (`px.scatter`).
      * **X-Achse:** Datum
      * **Y-Achse:** Betrag (`amount`)
      * **Color:** Färben Sie die Punkte basierend auf dem `type` (Einzahlung/Abhebung).
      * **Facet Column:** Teilen Sie das Diagramm automatisch in drei Nebendiagramme (Subplots) auf, eines für jede `region` (`facet_col="region"`).
2.  **Layout Anpassung:**
      * Ändern Sie das Template auf `plotly_dark` für einen modernen Look.
      * Fügen Sie Range-Slider auf der X-Achse hinzu (`update_xaxes(rangeslider_visible=True)`).
3.  **Export:**
      * Speichern Sie die Grafik als `dashboard.html`. Öffnen Sie diese Datei in Ihrem Browser, um zu sehen, dass die Interaktivität erhalten bleibt.

-----

## `Lab_08_Lösung.md`

# Lösung Lab 08

### Lösungsansatz

  * **Plotly Express (`px`):** Wir nutzen die High-Level API. Sie erwartet "Tidy Data" (Long Format), was Pandas DataFrames meistens ohnehin sind.
  * **Interaktivität:** Beachten Sie, dass Sie im Lösungscode nichts extra programmieren müssen, um Zoom oder Tooltips zu erhalten – das ist "gratis" in Plotly enthalten.

-----

### Code: Basis Aufgabe

```python
import pandas as pd
import numpy as np
import plotly.express as px

# --- DATEN GENERIERUNG (wie in Angabe) ---
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=100)
df = pd.DataFrame({
    "date": np.repeat(dates, 3),
    "region": np.random.choice(["EU", "US", "ASIA"], 300),
    "type": np.random.choice(["deposit", "withdrawal", "payment"], 300),
    "amount": np.random.uniform(10, 500, 300)
})
df.loc[df["type"] != "deposit", "amount"] *= -1
# -----------------------------------------

# 1. Balkendiagramm (Aggregation nötig)
# Wir gruppieren, um eine Zeile pro Region zu haben
df_grouped = df.groupby("region", as_index=False)["amount"].sum()

fig_bar = px.bar(
    df_grouped, 
    x="region", 
    y="amount", 
    title="Gesamtvolumen pro Region",
    color="region" # Optional: Färbt die Balken unterschiedlich
)
fig_bar.show()

# 2. Liniendiagramm (Kumulativ)
# Wir sortieren erst sicherheitshalber nach Datum
df_sorted = df.sort_values("date")
# Wir berechnen den "Laufenden Kontostand"
df_sorted["running_balance"] = df_sorted["amount"].cumsum()

fig_line = px.line(
    df_sorted,
    x="date",
    y="running_balance",
    title="Entwicklung des Bank-Gesamtsaldos (YTD)",
    markers=True # Punkte auf der Linie anzeigen
)
fig_line.show()
```

-----

### Code: Bonus Herausforderung

```python
import plotly.io as pio

# 1. Advanced Scatter mit Faceting
# Facet Col erstellt automatisch Subplots für jede Region
fig_complex = px.scatter(
    df,
    x="date",
    y="amount",
    color="type",           # Unterschiedliche Farben für Transaktionstypen
    facet_col="region",     # Ein Diagramm pro Region (Nebeneinander)
    title="Transaktionsanalyse: Typenverteilung nach Region",
    template="plotly_dark", # Dark Mode
    hover_data=["amount"]   # Extra Info im Tooltip
)

# 2. Layout Anpassungen (Range Slider)
# update_xaxes wendet die Einstellung auf alle Subplots an
fig_complex.update_xaxes(rangeslider_visible=True)

# Überschrift zentrieren
fig_complex.update_layout(title_x=0.5)

fig_complex.show()

# 3. Export
# Dies erzeugt eine eigenständige HTML Datei (kann per E-Mail verschickt werden)
fig_complex.write_html("dashboard.html")
print("Dashboard erfolgreich als 'dashboard.html' gespeichert.")
```
