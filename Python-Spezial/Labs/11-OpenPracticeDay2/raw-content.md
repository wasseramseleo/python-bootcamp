# LAB 11 DETAILS:

* **Lab Title/Topic:** Open Practice (Tag 2)
* **Learning Objectives:**
    * Teilnehmende haben die Möglichkeit, sich je nach persönlichen Interessen fortgeschrittene aufgaben zu den bisher behandelten themen durchzuführen.
* **Content:**
  * Create coding challenges for each of the following topics:
    * Pandas
    * Plotly
    * Scikit-learn

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, and two-file format) exept for the distinction of basis aufgabe and bonus herausforderung. Here only one type of task exists. 
Instead of haven one big task concerned with several topics, this open practice task is designed to offer several independent tasks for them to choose freely from. 
The tasks explore topics/functionalities not covered by the previous labs.

-----

## `Lab_11_Angabe.md`

# Lab 11: Open Practice (Tag 2)

### Szenario

Sie haben nun Zugriff auf das volle Arsenal der Python Data Science Tools. In dieser Session vertiefen wir spezifische Aspekte, die für Finanzanalysen kritisch sind: Zeitreihen-Glättung, hierarchische Visualisierung und binäre Klassifikation (Betrugserkennung).

**Wählen Sie mindestens eine der folgenden 3 Aufgaben.**

### Voraussetzungen

Da wir fortgeschrittene Daten benötigen, führen Sie bitte dieses Setup-Skript aus, um den gemeinsamen Datensatz `portfolio_data.csv` zu generieren:

```python
import pandas as pd
import numpy as np

# Setup
np.random.seed(99)
dates = pd.date_range(start="2023-01-01", periods=100, freq='D')
n = 1000

data = {
    "date": np.random.choice(dates, n),
    "customer_region": np.random.choice(["EU", "US", "ASIA"], n),
    "asset_class": np.random.choice(["Stocks", "Bonds", "Cash", "Crypto"], n, p=[0.4, 0.3, 0.2, 0.1]),
    "amount": np.random.exponential(1000, n).round(2), # Viele kleine, wenige große Beträge
    "is_fraud": np.random.choice([0, 1], n, p=[0.95, 0.05]) # 5% Betrugsrate
}

df = pd.DataFrame(data)
# Sortieren für Zeitreihen-Analysen wichtig
df = df.sort_values("date")
df.to_csv("portfolio_data.csv", index=False)
print("Setup fertig: 'portfolio_data.csv' erstellt.")
```

-----

### Option A: Pandas (Advanced Time Series)

Analysten schauen selten auf tagesaktuelle, volatile Zahlen. Sie wollen Trends sehen.

**Aufgabe:**

1.  Laden Sie die Daten und setzen Sie das Datum als Index.
2.  **Daily Aggregation:** Berechnen Sie das tägliche Gesamtvolumen (`sum` von `amount`).
3.  **Rolling Window:** Erstellen Sie eine neue Spalte `7d_moving_avg`.
      * Berechnen Sie den gleitenden Durchschnitt der letzten 7 Tage über das tägliche Volumen.
      * Nutzen Sie dazu `.rolling(window=7).mean()`.
4.  **Volatility:** Berechnen Sie die prozentuale Veränderung zum Vortag (`pct_change()`) für das tägliche Volumen.

-----

### Option B: Plotly (Hierarchische Charts)

Bankmanager wollen sehen, wie sich das Kapital verteilt ("Asset Allocation"), aufgebrochen nach Region und Anlageklasse. Balkendiagramme sind hierfür oft unübersichtlich.

**Aufgabe:**

1.  Laden Sie die Daten.
2.  **Sunburst Chart:** Nutzen Sie `px.sunburst`, um die Hierarchie darzustellen.
      * **Ebene 1 (Innen):** `customer_region`
      * **Ebene 2 (Außen):** `asset_class`
      * **Größe der Segmente:** `amount`
3.  **Interaktivität:** Fahren Sie mit der Maus über die Segmente, um zu prüfen, ob die Summen korrekt aggregiert werden.
4.  **Titel:** Setzen Sie einen passenden Titel, z.B. "Global Asset Allocation".

-----

### Option C: Scikit-learn (Fraud Detection / Classification)

In Lab 09 haben wir Werte vorhergesagt (Regression). Nun wollen wir Kategorien vorhersagen (Klassifikation): Ist eine Transaktion Betrug (1) oder nicht (0)?

**Aufgabe:**

1.  **Feature Prep:**
      * Nutzen Sie `amount` als Feature.
      * Erstellen Sie ein Dummy-Feature für `asset_class` (Text muss in Zahlen gewandelt werden). Nutzen Sie dazu `pd.get_dummies()`.
      * Target (`y`) ist die Spalte `is_fraud`.
2.  **Split:** Teilen Sie in Train/Test (70%/30%).
3.  **Model:** Importieren Sie `LogisticRegression` aus `sklearn.linear_model` (der Standard für binäre Klassifikation im Banking). Trainieren Sie das Modell.
4.  **Evaluation (Confusion Matrix):**
      * Ein R²-Score ergibt bei Klassifikation keinen Sinn. Wir brauchen eine "Confusion Matrix".
      * Importieren Sie `confusion_matrix` und `ConfusionMatrixDisplay` aus `sklearn.metrics`.
      * Vergleichen Sie die Vorhersagen (`y_pred`) mit den echten Werten (`y_test`) und zeigen Sie die Matrix an oder geben Sie sie als Text aus.
      * *Frage:* Wie viele Betrugsfälle (True Positives) wurden korrekt erkannt?

-----

## `Lab_11_Lösung.md`

# Lösung Lab 11

### Überblick

Die Lösungen nutzen fortgeschrittene Methoden der jeweiligen Libraries, die im täglichen Data-Science-Leben unverzichtbar sind.

-----

### Lösung A: Pandas (Rolling Windows)

```python
import pandas as pd
import matplotlib.pyplot as plt # Optional für schnelle visuelle Prüfung

# Daten laden
df = pd.read_csv("portfolio_data.csv", parse_dates=["date"])

# 1. Tägliche Aggregation
# Wir summieren alle Transaktionen pro Tag
daily_vol = df.groupby("date")["amount"].sum().to_frame(name="daily_amount")

# 2. Rolling Window (Gleitender Durchschnitt)
# min_periods=1 sorgt dafür, dass wir auch am Anfang (Tag 1-6) schon Werte haben
daily_vol["7d_moving_avg"] = daily_vol["daily_amount"].rolling(window=7, min_periods=1).mean()

# 3. Volatilität (Prozentuale Änderung)
daily_vol["daily_change_pct"] = daily_vol["daily_amount"].pct_change()

print(daily_vol.head(10))

# Optional: Kurzer Plot zur Kontrolle
# daily_vol[["daily_amount", "7d_moving_avg"]].plot(title="Daily Vol vs 7-Day Trend")
# plt.show()
```

-----

### Lösung B: Plotly (Sunburst)

```python
import plotly.express as px
import pandas as pd

df = pd.read_csv("portfolio_data.csv")

# Sunburst Charts benötigen keine explizite Vor-Aggregation (groupby), 
# Plotly macht das intern, wenn wir 'values' angeben.

fig = px.sunburst(
    df,
    path=['customer_region', 'asset_class'], # Die Hierarchie (Innen -> Außen)
    values='amount',                         # Was bestimmt die Größe?
    title='Global Asset Allocation (Region -> Class)',
    color='amount',                          # Optional: Färbung nach Volumen
    color_continuous_scale='RdBu'            # Farbskala
)

fig.show()
```

-----

### Lösung C: Scikit-learn (Classification)

[Image of confusion matrix explanation]

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("portfolio_data.csv")

# 1. Feature Engineering
# Wir wandeln Kategorien ("Stocks", "Bonds") in Spalten (asset_class_Stocks: 0/1)
df_features = pd.get_dummies(df, columns=["asset_class", "customer_region"], drop_first=True)

# Feature Matrix X und Target Vector y
X = df_features.drop(["date", "is_fraud"], axis=1) # Datum ignorieren wir hier
y = df_features["is_fraud"]

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Training (Logistische Regression für Ja/Nein Fragen)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 4. Evaluation
y_pred = model.predict(X_test)

print("--- Confusion Matrix ---")
# Struktur:
# [[True Negatives (Kein Betrug korrekt erkannt), False Positives (Falscher Alarm)],
#  [False Negatives (Betrug übersehen),           True Positives (Betrug erkannt)]]
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\n--- Detailed Report ---")
# Precision = Wie viele meiner "Betrug"-Rufe waren wahr?
# Recall = Wie viele der echten Betrugsfälle habe ich gefunden?
print(classification_report(y_test, y_pred))

# Hinweis: Da Betrug sehr selten ist (imbalanced data), wird ein einfaches Modell 
# oft einfach "Alles ist OK" vorhersagen und trotzdem 95% Accuracy haben. 
# Das sieht man im Recall für die Klasse '1'.
```
