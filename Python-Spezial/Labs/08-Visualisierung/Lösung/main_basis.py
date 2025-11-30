import pandas as pd
import numpy as np
import plotly.express as px

# --- DATEN GENERIERUNG (wie in Angabe) ---
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=100)
df = pd.DataFrame({
    "date": np.repeat(dates, 3),
    "region": np.random.choice(["EU", "US", "ASIA"], 300),
    "type": np.random.choice(["deposit", "withdrawal", "payment"], 300),
    "amount": np.random.uniform(10, 500, 300)
})
df.loc[df["type"] != "deposit", "amount"] *= -1
# -----------------------------------------

# 1. Balkendiagramm (Aggregation nötig)
# Wir gruppieren, um eine Zeile pro Region zu haben
df_grouped = df.groupby("region", as_index=False)["amount"].sum()

fig_bar = px.bar(
    df_grouped,
    x="region",
    y="amount",
    title="Gesamtvolumen pro Region",
    color="region" # Optional: Färbt die Balken unterschiedlich
)
fig_bar.show()

# 2. Liniendiagramm (Kumulativ)
# Wir sortieren erst sicherheitshalber nach Datum
df_sorted = df.sort_values("date")
# Wir berechnen den "Laufenden Kontostand"
df_sorted["running_balance"] = df_sorted["amount"].cumsum()

fig_line = px.line(
    df_sorted,
    x="date",
    y="running_balance",
    title="Entwicklung des Bank-Gesamtsaldos (YTD)",
    markers=True # Punkte auf der Linie anzeigen
)
fig_line.show()
