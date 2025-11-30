import pandas as pd
import numpy as np

# Wir simulieren 100.000 Datensätze
count = 100_000
print(f"Generiere {count} Transaktionen...")

data = {
    'transaction_id': np.arange(count),
    'amount': np.random.uniform(1.0, 5000.0, count).round(2),
    'currency': np.random.choice(['EUR', 'USD', 'GBP'], count),
    'type': np.random.choice(['deposit', 'withdrawal', 'payment'], count)
}

df = pd.DataFrame(data)
df.to_csv('big_transactions.csv', index=False)
print("Fertig: 'big_transactions.csv' erstellt.")