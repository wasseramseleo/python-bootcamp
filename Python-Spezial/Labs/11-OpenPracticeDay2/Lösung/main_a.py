import pandas as pd
import matplotlib.pyplot as plt # Optional für schnelle visuelle Prüfung

# Daten laden
df = pd.read_csv("portfolio_data.csv", parse_dates=["date"])

# 1. Tägliche Aggregation
# Wir summieren alle Transaktionen pro Tag
daily_vol = df.groupby("date")["amount"].sum().to_frame(name="daily_amount")

# 2. Rolling Window (Gleitender Durchschnitt)
# min_periods=1 sorgt dafür, dass wir auch am Anfang (Tag 1-6) schon Werte haben
daily_vol["7d_moving_avg"] = daily_vol["daily_amount"].rolling(window=7, min_periods=1).mean()

# 3. Volatilität (Prozentuale Änderung)
daily_vol["daily_change_pct"] = daily_vol["daily_amount"].pct_change()

print(daily_vol.head(10))

# Optional: Kurzer Plot zur Kontrolle
# daily_vol[["daily_amount", "7d_moving_avg"]].plot(title="Daily Vol vs 7-Day Trend")
# plt.show()