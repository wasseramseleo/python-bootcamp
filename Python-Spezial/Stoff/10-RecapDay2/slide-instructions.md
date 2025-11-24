**Input Data:**
Create 1-2 Slides highlighting the key-takeaways from the topics of day 1.

* **Topic Title:** Recap Tag 1
* **Content Points:**
    - Python 13 Grundlagen
    - Modularisierung & Best Practices
    - File Handling & Wichtige Libraries
    - Unstrukturierte Daten (Docs)
    - Datenbankzugriff

-----

**Slide 1: Recap Tag 2 – Data Engineering & Analysis**

**Body Text (German):**

  * **Vectorization:** In `numpy` und `pandas` vermeiden wir Loops. Operationen auf ganzen Spalten (Arrays) sind durch C-Optimierung massiv schneller.
  * **Wrangling:** Daten sind selten perfekt.
      * **Cleaning:** `dropna()` oder `fillna()` strategisch einsetzen, um `NaN`-Werte zu behandeln.
      * **Transformation:** `groupby()` ist das mächtigste Werkzeug, um von Einzeltieren auf Populations-Statistiken zu schließen.
  * **Performance:** Nutzen Sie Vektorisierung statt `iterrows()`, besonders bei großen Migrations-Datensätzen.

**Code Snippet (Python):**

```python
import pandas as pd

# The "Day 2 Workflow": Load, Clean, Aggregate
df = pd.read_csv("raw_migration_data.csv")

# 1. Clean: Remove invalid weights
clean_df = df[df['weight_g'] > 0].copy()

# 2. Vectorized Calc: BMI (No loop!)
clean_df['bmi'] = clean_df['weight_g'] / clean_df['wing_len_mm']

# 3. Aggregate: Stats per Species
report = clean_df.groupby('species')['bmi'].mean()
```

**Speaker Notes (German):**
An Tag 2 haben wir gelernt, wie man Daten massiert. Das wichtigste Takeaway für Ihre Performance: Schreiben Sie keine `for`-Schleifen, um Spalten zu berechnen. Nutzen Sie die Power von Pandas (Vektorisierung), sonst wartet Ihr Skript bis zur nächsten Brutsaison. Denken Sie immer an den Dreischritt: Laden, Bereinigen (Null-Values behandeln), Aggregieren. Nur saubere Daten liefern valide Ergebnisse.

**Image Prompt:** A funnel diagram: "Raw Data" (messy blocks) enters at the top, passes through "Filters" (Pandas logic), and emerges as "Gold Bars" (Aggregated Insights) at the bottom.

-----

**Slide 2: Recap Tag 2 – Insights & Vorhersagen**

**Body Text (German):**

  * **Visualisierung:** `plotly.express` erzeugt interaktive Grafiken. HTML-Exports ermöglichen es, Ergebnisse ohne Python-Setup zu teilen ("Data Storytelling").
  * **Machine Learning:**
      * **Workflow:** Einheitliches Schema in `scikit-learn`: `Import` -\> `Instantiate` -\> `Fit` -\> `Predict`.
      * **Validierung:** Der `train_test_split` ist obligatorisch. Ein Modell, das nur auf bekannten Daten gut ist, ist wertlos (Overfitting).
  * **Interpretation:** Nutzen Sie Metriken wie RMSE oder R², um die Qualität Ihrer Vorhersagen kritisch zu hinterfragen.

**Code Snippet (Python):**

```python
from sklearn.linear_model import LinearRegression
import plotly.express as px

# 1. Model: Learn relationship (Wing -> Weight)
model = LinearRegression().fit(X_train, y_train)

# 2. Visualize: Compare Truth vs. Prediction
fig = px.scatter(
    x=y_test, 
    y=model.predict(X_test), 
    labels={'x': 'True Weight', 'y': 'Predicted Weight'},
    title="Model Accuracy: The closer to diagonal, the better"
)
fig.show()
```

**Speaker Notes (German):**
Zum Abschluss haben wir die Daten zum Sprechen gebracht. Mit Plotly erstellen wir Dashboards, die Entscheidungsträger verstehen. Mit Machine Learning schauen wir in die Zukunft. Aber Vorsicht: Ein Modell ist nur so gut wie seine Validierung. Vertrauen Sie keinem R²-Wert, der nicht auf einem separaten Test-Set berechnet wurde. Nutzen Sie Visualisierungen (wie Scatter Plots von "Wahrheit vs. Vorhersage"), um Fehler visuell zu erkennen.

**Image Prompt:** A split view: Left side is a robot (ML Model) examining a bird. Right side is a futuristic HUD (Plotly Chart) displaying the robot's analysis with interactive clickable elements.
