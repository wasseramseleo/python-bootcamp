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
