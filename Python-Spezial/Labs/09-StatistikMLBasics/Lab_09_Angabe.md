# Lab 09: Statistik & ML Basics

### Szenario
Die Risikoabteilung der "PyBank" möchte den Prozess der Kreditvergabe automatisieren. Ihre Aufgabe ist es, ein Modell zu trainieren, das basierend auf dem Jahreseinkommen und dem aktuellen Kontostand das empfohlene **Kreditlimit** vorhersagt.

### Voraussetzungen
* `scikit-learn`, `pandas`, `numpy` installiert.
* **Daten-Setup:** Generieren Sie den Datensatz mit folgendem Code:

```python
import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 200

# Features: Jahreseinkommen (30k bis 120k) und Kontostand (0 bis 50k)
income = np.random.uniform(30000, 120000, n_samples)
balance = np.random.uniform(0, 50000, n_samples)

# Target: Das Limit hängt von Einkommen und Balance ab + Noise
credit_limit = (income * 0.10) + (balance * 0.20) + np.random.normal(0, 2000, n_samples)

df_credit = pd.DataFrame({
    "income": income,
    "balance": balance,
    "credit_limit": credit_limit
})

print("Kredit-Daten generiert.")
````

-----

### Basis Aufgabe

Ziel ist das Training eines Regressionsmodells und die Vorhersage für einen Neukunden.

**Anforderungen:**

1.  **Features & Target:**

      * Definieren Sie `X` als DataFrame mit den Spalten `income` und `balance`.
      * Definieren Sie `y` als Series mit der Spalte `credit_limit`.

2.  **Split:**

      * Importieren Sie `train_test_split` (`sklearn.model_selection`).
      * Teilen Sie die Daten in Training (80%) und Test (20%). Nutzen Sie `random_state=42`.

3.  **Training:**

      * Importieren Sie `LinearRegression` (`sklearn.linear_model`).
      * Initialisieren Sie das Modell und trainieren Sie es mit den **Trainingsdaten** (`fit`).

4.  **Prediction:**

      * Ein neuer Kunde kommt zur Bank: Einkommen **85.000**, Kontostand **12.000**.
      * Nutzen Sie `model.predict(...)`, um das Limit zu schätzen.
      * *Wichtig:* Scikit-Learn erwartet 2D-Arrays für die Vorhersage (siehe Theorie-Code: `[[...]]`).
      * Geben Sie das geschätzte Limit aus.

-----

### Bonus Herausforderung

Ziel ist die Messung der Fehlerquote und der Aufbau einer professionellen Skalierungs-Pipeline wie in Sektion 5 des Theorie-Codes.

**Anforderungen:**

1.  **Evaluation (RMSE & R²):**

      * Nutzen Sie das trainierte Modell, um Vorhersagen für die **Testdaten** (`X_test`) zu machen.
      * Importieren Sie `mean_squared_error` und `r2_score` (`sklearn.metrics`).
      * Berechnen Sie den **RMSE** (Wurzel aus dem MSE), um den durchschnittlichen Fehler in EUR zu erhalten.
      * Berechnen Sie den **R²** Score.
      * Geben Sie beide Werte interpretiert aus.

2.  **Pipeline:**

      * Importieren Sie `Pipeline` (`sklearn.pipeline`) und `StandardScaler` (`sklearn.preprocessing`).
      * Erstellen Sie eine Pipeline-Liste mit zwei Schritten:
        1.  `'scaler'` -\> `StandardScaler()`
        2.  `'regressor'` -\> `LinearRegression()`
      * Trainieren Sie die Pipeline mit `fit` auf den Trainingsdaten.
      * Überprüfen Sie den Score der Pipeline auf den Testdaten (`pipe.score(...)`).

<!-- end list -->
