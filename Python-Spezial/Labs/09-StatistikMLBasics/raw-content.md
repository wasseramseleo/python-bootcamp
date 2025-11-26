# LAB 09 DETAILS:

* **Lab Title/Topic:** Statistik & ML Basics
* **Learning Objectives:**
    * Ein einfaches Modell trainieren (z.B. Linear Regression) und eine Vorhersage treffen.
    * Advanced: Validierungsmetriken (R², MSE) interpretieren, Overfitting erkennen und Pipelines nutzen.
* **Context & Slide Summary:** 
    - Scikit-learn (Workflow)
    - Train/Test Split
    - Statsmodels (Regression)
    - Advanced: Pipelines & Overfitting

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

## `Lab_09_Angabe.md`

# Lab 09: Statistik & ML Basics

### Szenario

Die Risikoabteilung der "PyBank" möchte den Prozess der Kreditvergabe automatisieren. Bisher entscheiden Sachbearbeiter manuell über das Kreditlimit. Ihre Aufgabe ist es, ein Modell zu trainieren, das basierend auf dem Jahreseinkommen und dem aktuellen Kontostand das empfohlene **Kreditlimit** vorhersagt.

### Voraussetzungen

  * Installation von Scikit-Learn:

    ```bash
    pip install scikit-learn
    ```

  * **Daten-Setup:** Generieren Sie den Datensatz mit folgendem Code (wir simulieren hier einen linearen Zusammenhang mit etwas "Rauschen"):

    ```python
    import pandas as pd
    import numpy as np

    np.random.seed(42)
    n_samples = 200

    # Features: Jahreseinkommen (30k bis 120k) und Kontostand (0 bis 50k)
    income = np.random.uniform(30000, 120000, n_samples)
    balance = np.random.uniform(0, 50000, n_samples)

    # Target: Das Limit hängt von Einkommen und Balance ab + etwas Zufall (Noise)
    # Formel (unbekannt für das Modell): Limit = 10% vom Einkommen + 20% vom Balance
    credit_limit = (income * 0.10) + (balance * 0.20) + np.random.normal(0, 2000, n_samples)

    df_credit = pd.DataFrame({
        "income": income,
        "balance": balance,
        "credit_limit": credit_limit
    })

    print("Kredit-Daten generiert.")
    ```

-----

### Teil 1: Basis Aufgabe

Ziel ist das Training einer **Linearen Regression**.

**Anforderungen:**

1.  **Features & Target:**
      * Definieren Sie `X` (Die Eingabedaten: `income`, `balance`) und `y` (Das Ziel: `credit_limit`).
2.  **Split:**
      * Importieren Sie `train_test_split` aus `sklearn.model_selection`.
      * Teilen Sie die Daten in Trainings- (80%) und Testdaten (20%) auf. Setzen Sie `random_state=42` für Reproduzierbarkeit.
3.  **Training:**
      * Importieren Sie `LinearRegression` aus `sklearn.linear_model`.
      * Erstellen Sie das Modell und trainieren Sie es mit den **Trainingsdaten** (`fit`).
4.  **Vorhersage (Prediction):**
      * Ein neuer Kunde kommt zur Bank: Einkommen 85.000 EUR, Kontostand 12.000 EUR.
      * Nutzen Sie das trainierte Modell (`predict`), um das Kreditlimit für diesen Kunden zu schätzen. Geben Sie den Wert aus.

-----

### Teil 2: Bonus Herausforderung

Ziel ist die Validierung der Modellgüte und die Nutzung professioneller Pipelines.

**Anforderungen:**

1.  **Evaluation:**
      * Nutzen Sie das Modell, um Vorhersagen für das **Test-Set** (`X_test`) zu machen.
      * Importieren Sie `mean_squared_error` und `r2_score` aus `sklearn.metrics`.
      * Berechnen Sie den R²-Score (Bestimmtheitsmaß). Wie nah ist er an 1.0?
      * Interpretieren Sie das Ergebnis in einem Print-Statement.
2.  **Pipeline mit Skalierung:**
      * Algorithmen arbeiten oft besser, wenn alle Daten im gleichen Bereich liegen (Scaling).
      * Importieren Sie `StandardScaler` (`sklearn.preprocessing`) und `make_pipeline` (`sklearn.pipeline`).
      * Erstellen Sie eine Pipeline: Erst `StandardScaler`, dann `LinearRegression`.
      * Trainieren Sie die Pipeline erneut auf den Trainingsdaten und prüfen Sie, ob das Modell noch funktioniert (der R² sollte ähnlich bleiben, da einfache Regression robust ist, aber der Code ist nun "Production-Ready").
3.  **Koeffizienten-Analyse:**
      * Welchen Einfluss hat das Einkommen im Vergleich zum Kontostand?
      * Extrahieren Sie die `.coef_` (Steigungsparameter) aus dem Modell und geben Sie sie aus.

-----

## `Lab_09_Lösung.md`

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
