"""--------------1-------------------"""
import pandas as pd

# The "Day 2 Workflow": Load, Clean, Aggregate
df = pd.read_csv("raw_migration_data.csv")

# 1. Clean: Remove invalid weights
clean_df = df[df['weight_g'] > 0].copy()

# 2. Vectorized Calc: BMI (No loop!)
clean_df['bmi'] = clean_df['weight_g'] / clean_df['wing_len_mm']

# 3. Aggregate: Stats per Species
report = clean_df.groupby('species')['bmi'].mean()

"""--------------2-------------------"""
from sklearn.linear_model import LinearRegression
import plotly.express as px

# 1. Model: Learn relationship (Wing -> Weight)
model = LinearRegression().fit(X_train, y_train)

# 2. Visualize: Compare Truth vs. Prediction
fig = px.scatter(
    x=y_test,
    y=model.predict(X_test),
    labels={'x': 'True Weight', 'y': 'Predicted Weight'},
    title="Model Accuracy: The closer to diagonal, the better"
)
fig.show()

