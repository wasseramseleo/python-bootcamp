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
