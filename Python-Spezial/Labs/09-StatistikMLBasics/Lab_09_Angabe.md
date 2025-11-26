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
