import plotly.express as px
import pandas as pd

df = pd.read_csv("portfolio_data.csv")

# Sunburst Charts benötigen keine explizite Vor-Aggregation (groupby),
# Plotly macht das intern, wenn wir 'values' angeben.

fig = px.sunburst(
    df,
    path=['customer_region', 'asset_class'], # Die Hierarchie (Innen -> Außen)
    values='amount',                         # Was bestimmt die Größe?
    title='Global Asset Allocation (Region -> Class)',
    color='amount',                          # Optional: Färbung nach Volumen
    color_continuous_scale='RdBu'            # Farbskala
)

fig.show()