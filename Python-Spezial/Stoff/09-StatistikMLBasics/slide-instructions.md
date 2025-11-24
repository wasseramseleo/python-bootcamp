**Input Data:**

* **Topic Title:** 9. Statistik & ML Basics
* **Content Points:**
    - Scikit-learn (Workflow)
    - Train/Test Split
    - Statsmodels (Regression)
* **Lab Objectives:**
    * Ein einfaches Modell trainieren (z.B. Linear Regression) und eine Vorhersage treffen.
    * Advanced: Validierungsmetriken (R², MSE) interpretieren, Overfitting erkennen und Pipelines nutzen.

-----

Here are the slides for **Topic 9: Statistik & ML Basics**, focusing on predictive modeling within the Bird Ringing domain.

-----

**Slide 1: Machine Learning Workflow (Scikit-learn)**

**Body Text (German):**

  * **Das Konzept:** Machine Learning in `scikit-learn` folgt immer demselben strikten Schema, egal ob Regression oder Klassifikation.
  * **Der 4-Schritte-Workflow:**
    1.  **Import:** Wahl der Modell-Klasse (z.B. `LinearRegression`).
    2.  **Instantiate:** Erstellen des Modell-Objekts (Hyperparameter setzen).
    3.  **Fit:** Training des Modells mit Daten (`model.fit(X, y)`).
    4.  **Predict:** Vorhersage auf neuen Daten (`model.predict(X_new)`).
  * **Daten-Struktur:** `X` (Features) muss zwingend 2D sein (Matrix), `y` (Target) ist meist 1D (Vektor).

**Code Snippet (Python):**

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Features (Wing Length in mm) - Must be 2D array!
X = np.array([[74.5], [72.1], [78.0], [69.5]])
# Target (Weight in g)
y = np.array([18.5, 17.2, 19.8, 16.5])

# Workflow
model = LinearRegression()
model.fit(X, y)

# Predict weight for a bird with 75mm wing
prediction = model.predict([[75.0]])
print(f"Predicted Weight: {prediction[0]:.2f}g")
```

**Speaker Notes (German):**
Wir betreten das Feld der Vorhersagen. Scikit-learn ist der Goldstandard in Python. Merken Sie sich das Mantra: Import, Instantiate, Fit, Predict. Im Code sehen wir ein einfaches Szenario: Können wir das Gewicht eines Vogels vorhersagen, wenn wir nur seine Flügel-Länge kennen? Achten Sie auf die Dimensionen: `X` muss immer eine Matrix sein, auch wenn es nur eine Spalte hat.

**Image Prompt:** A flowchart visualizing the four steps: Robot arm picking a tool (Import/Instantiate), Robot reading a book (Fit/Training), and Robot painting a picture based on the book (Predict).

-----

**Slide 2: Train / Test Split**

**Body Text (German):**

  * **Kritische Validierung:** Ein Modell darf niemals mit denselben Daten getestet werden, mit denen es trainiert wurde. Das wäre wie das Auswendiglernen der Lösungen vor einer Klausur.
  * **Split:** Wir teilen den Datensatz (meist 80/20 oder 70/30).
      * **Train Set:** Zum Lernen der Muster.
      * **Test Set:** Zum Überprüfen der Generalisierung auf *unsichtbare* Daten.
  * **Evidenz:** Nur die Performance auf dem Test-Set liefert einen wissenschaftlich haltbaren Beweis für die Qualität des Modells.

**Code Snippet (Python):**

```python
from sklearn.model_selection import train_test_split

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train ONLY on training data
model.fit(X_train, y_train)

# Evaluate ONLY on test data
score = model.score(X_test, y_test)
```

**Speaker Notes (German):**
Wissenschaftliche Integrität ist hier entscheidend. Wenn Sie Ihr Modell auf den Trainingsdaten testen, betrügen Sie sich selbst (Data Leakage). Wir nutzen `train_test_split`, um Daten zurückzuhalten. Nur wenn das Modell das Gewicht von Vögeln korrekt vorhersagt, die es *nie zuvor gesehen* hat, ist es nützlich.

**Image Prompt:** A dataset represented as a cake being cut with a knife. The larger piece is labeled "Training (For Eating/Learning)", the smaller slice is put in a separate box labeled "Test (For Later Review)".

-----

**Slide 3: Statsmodels (Statistische Inferenz)**

**Body Text (German):**

  * **Prediction vs. Inference:**
      * `scikit-learn`: Fokus auf **Vorhersage** (Wie genau ist der Wert?).
      * `statsmodels`: Fokus auf **Erklärung** (Warum beeinflusst X das Y? Ist der Effekt signifikant?).
  * **OLS (Ordinary Least Squares):** Bietet detaillierte statistische Auswertungen inkl. p-Values, Konfidenzintervallen und Standardfehlern.
  * **Anwendung:** Nutzen Sie dies, um wissenschaftliche Hypothesen zu prüfen (z.B. "Hat die Flügellänge einen signifikanten Einfluss auf das Gewicht?").

**Code Snippet (Python):**

```python
import statsmodels.api as sm

# Add constant (Intercept) manually for statsmodels
X_with_const = sm.add_constant(X)

# Fit OLS model
ols_model = sm.OLS(y, X_with_const).fit()

# Print comprehensive statistical summary
print(ols_model.summary())
```

**Speaker Notes (German):**
Manchmal reicht eine Vorhersage nicht; wir wollen Beweise. `Statsmodels` liefert uns den klassischen statistischen Output, den Sie aus R oder SPSS kennen. Hier sehen wir p-Werte und R² im Detail. Das beantwortet die Frage: Ist der Zusammenhang zwischen Flügel und Gewicht Zufall oder statistisch signifikant? Scikit-learn schweigt dazu meist.

**Image Prompt:** A magnifying glass hovering over a regression line, revealing mathematical formulas and p-values underneath, contrasting with a crystal ball (prediction).

-----

**Slide 4: Metriken & Evaluation**

**Body Text (German):**

  * **MSE (Mean Squared Error):** Der Durchschnitt der quadrierten Fehler. Bestraft große Abweichungen (Ausreißer) stark. Einheit: Quadrierte Zielvariable (schwer zu interpretieren).
  * **RMSE (Root MSE):** Die Wurzel aus MSE. Einheit entspricht wieder der Zielvariable (z.B. "Gramm").
  * **R² (Coefficient of Determination):** Gibt an, wie viel Prozent der Varianz im Gewicht durch die Flügellänge erklärt werden (0 bis 1).

**Code Snippet (Python):**

```python
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print(f"Error: +/- {rmse:.2f}g")
print(f"Explained Variance (R2): {r2:.2f}")
```

**Speaker Notes (German):**
Wie falsch liegen wir? Der `RMSE` sagt uns: "Unsere Vorhersage liegt durchschnittlich um 1.5 Gramm daneben." Das ist für Biologen verständlich. Der `R²` sagt uns: "Unser Modell erklärt 85% der Gewichtsschwankungen." Wenn der R² niedrig ist, fehlen uns wichtige Faktoren (z.B. Fett-Score oder Tageszeit), und die Flügellänge allein reicht nicht aus.

**Image Prompt:** A dartboard showing scatter. High R² / Low MSE is a tight grouping near the center. Low R² / High MSE is darts scattered all over the wall.

-----

**Slide 5: Advanced: Pipelines & Overfitting**

**Body Text (German):**

  * **Overfitting:** Wenn das Modell das "Rauschen" in den Trainingsdaten auswendig lernt, statt den Trend zu verstehen. Es versagt bei neuen Daten.
  * **Pipelines:** Verbinden Preprocessing (z.B. Scaling) und Modeling in einem Objekt.
      * Verhindert Daten-Lecks (Scaler wird nur auf Train-Set gefittet).
      * Macht den Code sauberer und reproduzierbar.

**Code Snippet (Python):**

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Pipeline: First Scale data, then apply Regression
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Fit pipeline (scales automatically)
pipe.fit(X_train, y_train)

# Predict (scales input automatically using train stats)
pipe.predict(X_test)
```

**Speaker Notes (German):**
Für die Profis: Rohdaten in ein Modell zu werfen, ist gefährlich. Oft müssen Daten skaliert werden. Wenn Sie Skalierung und Training trennen, riskieren Sie Fehler. Eine `Pipeline` kapselt beides. Sie rufen nur einmal `fit` auf, und die Pipeline kümmert sich um die korrekte Reihenfolge. Das schützt auch vor Overfitting, da Testdaten nicht versehentlich die Skalierung beeinflussen.

**Image Prompt:** A factory assembly line (Pipeline) inside a transparent tunnel, protecting the product from outside contamination (Data Leakage) until it's finished.

-----

**Slide 6: Lab Preparation**

**Body Text (German):**

  * **Szenario:** Wir entwickeln ein Modell, um das Gewicht von Vögeln basierend auf biometrischen Maßen zu schätzen (fehlende Daten imputieren).
  * **Aufgabe 1 (Setup):** Laden Sie den Datensatz. Definieren Sie `X` (Wing Length) und `y` (Weight).
  * **Aufgabe 2 (Split):** Teilen Sie die Daten in 80% Training und 20% Test.
  * **Aufgabe 3 (Modeling):** Trainieren Sie eine `LinearRegression`. Treffen Sie Vorhersagen für das Test-Set.
  * **Aufgabe 4 (Advanced):**
      * Berechnen Sie RMSE und R². Interpretieren Sie das Ergebnis: Ist das Modell brauchbar?
      * Nutzen Sie `statsmodels`, um zu prüfen, ob der Koeffizient signifikant ist (p \< 0.05).

**Code Snippet (Python):**

```python
# Lab Starter Hint
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# X must be 2D dataframe/array
X = df[['wing_len']] 
y = df['weight']

# X_train, X_test, ... = train_test_split(...)
```

**Speaker Notes (German):**
Sie sind jetzt Data Scientists. Ihr Ziel ist es, fehlende Gewichtsdaten in unserer Datenbank durch Schätzungen zu ersetzen. Aber Vorsicht: Blindes Vertrauen ist schlecht. Ich erwarte von den Anfängern eine funktionierende Vorhersage. Von den Experten erwarte ich eine kritische Analyse mittels Metriken: Ist die Flügellänge überhaupt ein guter Prädiktor, oder raten wir nur?

**Image Prompt:** A split screen: Left side shows a bird on a scale (Ground Truth), Right side shows a computer screen displaying a predicted number, with a ruler measuring the difference (Error).
