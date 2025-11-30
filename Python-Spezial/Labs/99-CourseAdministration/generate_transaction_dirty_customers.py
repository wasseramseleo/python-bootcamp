import pandas as pd
import numpy as np

# 1. Stammdaten (Kunden)
customers = pd.DataFrame({
    'account_id': [101, 102, 103, 104, 105],
    'name': ['Alice Corp', 'Bob Ltd', 'Charlie Inc', 'Dave Co', 'Eve Ent'],
    'region': ['EU', 'US', 'EU', 'US', 'ASIA']
})
customers.to_csv('customers.csv', index=False)

# 2. Transaktionsdaten (mit Fehlern)
dates = pd.date_range(start='2024-01-01', periods=20, freq='D')
data = {
    'date': dates,
    'account_id': np.random.choice([101, 102, 103, 999], 20), # 999 existiert nicht in customers
    'amount': np.random.uniform(-500, 2000, 20),
    'type': np.random.choice(['deposit', 'withdrawal'], 20)
}
df = pd.DataFrame(data)

# Wir bauen "Schmutz" ein (Missing Values)
df.loc[0, 'amount'] = np.nan
df.loc[5, 'amount'] = np.nan
df.to_csv('transactions_dirty.csv', index=False)

print("Setup fertig: CSV-Dateien erstellt.")