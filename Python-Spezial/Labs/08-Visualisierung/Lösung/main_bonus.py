import plotly.io as pio
import pandas as pd
import numpy as np
import plotly.express as px

# Reproduzierbare Daten erzeugen
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=100)

df = pd.DataFrame({
    "date": np.repeat(dates, 3),  # 3 Transaktionen pro Tag
    "region": np.random.choice(["EU", "US", "ASIA"], 300),
    "type": np.random.choice(["deposit", "withdrawal", "payment"], 300),
    "amount": np.random.uniform(10, 500, 300)
})

# Withdrawal/Payment negativ machen
df.loc[df["type"] != "deposit", "amount"] *= -1

print("Daten geladen. Zeilen:", len(df))
# 1. Advanced Scatter mit Faceting
# Facet Col erstellt automatisch Subplots für jede Region
fig_complex = px.scatter(
    df,
    x="date",
    y="amount",
    color="type",           # Unterschiedliche Farben für Transaktionstypen
    facet_col="region",     # Ein Diagramm pro Region (Nebeneinander)
    title="Transaktionsanalyse: Typenverteilung nach Region",
    template="plotly_dark", # Dark Mode
    hover_data=["amount"]   # Extra Info im Tooltip
)

# 2. Layout Anpassungen (Range Slider)
# update_xaxes wendet die Einstellung auf alle Subplots an
fig_complex.update_xaxes(rangeslider_visible=True)

# Überschrift zentrieren
fig_complex.update_layout(title_x=0.5)

fig_complex.show()

# 3. Export
# Dies erzeugt eine eigenständige HTML Datei (kann per E-Mail verschickt werden)
fig_complex.write_html("dashboard.html")
print("Dashboard erfolgreich als 'dashboard.html' gespeichert.")
