"""--------------1-------------------"""
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

"""--------------2-------------------"""
from sklearn.model_selection import train_test_split

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train ONLY on training data
model.fit(X_train, y_train)

# Evaluate ONLY on test data
score = model.score(X_test, y_test)

"""--------------3-------------------"""
import statsmodels.api as sm

# Add constant (Intercept) manually for statsmodels
X_with_const = sm.add_constant(X)

# Fit OLS model
ols_model = sm.OLS(y, X_with_const).fit()

# Print comprehensive statistical summary
print(ols_model.summary())

"""--------------4-------------------"""
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print(f"Error: +/- {rmse:.2f}g")
print(f"Explained Variance (R2): {r2:.2f}")

"""--------------5-------------------"""
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
