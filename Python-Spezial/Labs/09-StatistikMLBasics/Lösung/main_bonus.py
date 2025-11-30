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
