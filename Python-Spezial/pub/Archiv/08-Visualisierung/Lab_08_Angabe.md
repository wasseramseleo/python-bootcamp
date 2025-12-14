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

### Basis Aufgabe

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

### Bonus Herausforderung

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
