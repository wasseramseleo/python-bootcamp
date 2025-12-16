# Lab 08: Datenvisualisierung mit Plotly

### Szenario
Das Management ist begeistert von Ihren Zahlen, findet reine Tabellen aber ermüdend. Sie sollen ein interaktives Dashboard erstellen. Der Fokus liegt auf der Visualisierung von Zusammenhängen (Scatter), Vergleichen (Bar) und Verteilungen (Histogram/Facet).

### Voraussetzungen
* `plotly` und `pandas` installiert.
* **Daten-Setup:** Da wir saubere Daten brauchen, nutzen Sie bitte dieses Skript, um den DataFrame für die Übung zu generieren:


-----

### Basis Aufgabe

Ziel ist die Darstellung von Zusammenhängen und Kategorien, unter Nutzung von Farben und Größen-Dimensionen (wie im Theory-Code Section 2 & 3).

**Anforderungen:**

1.  **Scatter Plot (Transaktions-Analyse):**

      * Erstellen Sie einen Scatter Plot (`px.scatter`).
      * **X-Achse:** `date`, **Y-Achse:** `amount`.
      * **Farbe (`color`):** Unterscheiden Sie die Punkte nach `type`.
      * **Größe (`size`):** Nutzen Sie die Spalte `abs_amount`, damit größere Transaktionen dickere Punkte erzeugen.
      * **Hover Data:** Fügen Sie die `region` zum Tooltip hinzu.
      * Setzen Sie den Titel auf "Transactions Overview".

2.  **Bar Chart (Regionale Verteilung):**

      * Aggregieren Sie die Daten zuerst: Berechnen Sie die **Anzahl** (`count`) der Transaktionen pro `region` (nutzen Sie `value_counts()` oder `groupby`).
      * Erstellen Sie ein Balkendiagramm (`px.bar`).
      * **Text-Label:** Lassen Sie den Wert direkt auf/über den Balken anzeigen (Argument `text` oder `text_auto`), wie im "Top Species" Beispiel der Folien.
      * Stylen Sie die Beschriftung ggf. mit `update_traces`.

-----

### Bonus Herausforderung

Ziel ist die Darstellung von Zeitverläufen mit Achsen-Formatierung und komplexen Subplots (Faceting) für den Export.

**Anforderungen:**

1.  **Line Chart (Zeitverlauf):**

      * Erstellen Sie einen neuen DataFrame, der die täglichen Transaktionen zählt (`groupby("date")`).
      * Erstellen Sie ein Liniendiagramm (`px.line`), das die Anzahl der Transaktionen über die Zeit zeigt.
      * Aktivieren Sie Marker auf der Linie (`markers=True`).
      * **Formatierung:** Ändern Sie die X-Achse so (`update_xaxes`), dass die Ticks monatlich erscheinen und das Format "Jan", "Feb" etc. haben (siehe Theory Code Section 4).

2.  **Histogramm mit Faceting:**

      * Wir wollen die Verteilung der Beträge (`amount`) sehen.
      * Erstellen Sie ein Histogramm (`px.histogram`).
      * Teilen Sie das Bild in separate Grafiken pro Region auf (`facet_col="region"`).
      * Nutzen Sie das Template `plotly_white`.
      * Passen Sie die Achsen-Titel global an (`update_layout`).

3.  **Export:**

      * Speichern Sie das Histogramm als `banking_report.html`.

<!-- end list -->

````
