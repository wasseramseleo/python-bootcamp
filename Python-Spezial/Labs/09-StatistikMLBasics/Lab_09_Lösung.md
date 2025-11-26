# Lösung Lab 09

### Lösungsansatz

  * **Split:** Wir trainieren nie auf allen Daten. Sonst wissen wir nicht, ob das Modell nur auswendig lernt (Overfitting). Der Test-Datensatz simuliert die "Realität".
  * **Linear Regression:** Das Modell versucht, eine Ebene durch den 3D-Raum (Einkommen, Balance, Limit) zu legen, die den Abstand zu allen Punkten minimiert.
  * **Pipeline:** In Skikit-Learn verhindern Pipelines "Data Leakage" (Informationen aus dem Test-Set fließen versehentlich ins Training ein), da der Scaler nur auf den Trainingsdaten "lernt" (fit) und auf Testdaten nur angewendet (transform) wird.

-----

### Code: Basis Aufgabe

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# --- Setup Daten (wie in Angabe) ---
np.random.seed(42)
n_samples = 200
income = np.random.uniform(30000, 120000, n_samples)
balance = np.random.uniform(0, 50000, n_samples)
credit_limit = (income * 0.10) + (balance * 0.20) + np.random.normal(0, 2000, n_samples)

df_credit = pd.DataFrame({
    "income": income,
    "balance": balance,
    "credit_limit": credit_limit
})
# -----------------------------------

# 1. Features & Target
X = df_credit[["income", "balance"]] # Wichtig: Doppelte Klammern für DataFrame (2D)
y = df_credit["credit_limit"]        # Series (1D)

# 2. Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training Samples: {len(X_train)}")
print(f"Test Samples: {len(X_test)}")

# 3. Training
model = LinearRegression()
model.fit(X_train, y_train) # Hier lernt das Modell

# 4. Vorhersage für neuen Kunden
new_customer = pd.DataFrame({
    "income": [85000],
    "balance": [12000]
})

prediction = model.predict(new_customer)
print(f"\nEmpfohlenes Kreditlimit: {prediction[0]:.2f} EUR")
```

-----

### Code: Bonus Herausforderung

```python
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

print("\n--- Model Evaluation ---")

# 1. Evaluation auf Testdaten
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"R² Score: {r2:.4f} (1.0 ist perfekt)")
print(f"Mean Squared Error: {mse:.2f}")

if r2 > 0.8:
    print(">> Das Modell ist sehr zuverlässig.")
else:
    print(">> Das Modell benötigt mehr Daten oder Features.")

print("\n--- Production Pipeline ---")

# 2. Pipeline erstellen (Scaling -> Model)
pipeline = make_pipeline(
    StandardScaler(),
    LinearRegression()
)

# Pipeline trainieren
pipeline.fit(X_train, y_train)
pipe_score = pipeline.score(X_test, y_test) # shortcut für predict + r2
print(f"Pipeline R² Score: {pipe_score:.4f}")

# 3. Koeffizienten Analyse
# Zugriff auf den Regression-Schritt in der Pipeline (der zweite Schritt, Index 1)
reg_step = pipeline.named_steps['linearregression']

# Hinweis: Da wir Standard Scaler genutzt haben, sind die Koeffizienten nun 
# normalisiert und zeigen die "Stärke" des Einflusses unabhängig von der Einheit (EUR vs Cent)
coeffs = reg_step.coef_
features = ["Income", "Balance"]

print("\nEinflussfaktoren (skaliert):")
for feat, coef in zip(features, coeffs):
    print(f"- {feat}: {coef:.4f}")
```
