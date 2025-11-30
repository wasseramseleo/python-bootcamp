# Lösung Lab 11

### Überblick

Die Lösungen nutzen fortgeschrittene Methoden der am Tag 2 behandelten Data-Science Libraries.

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
