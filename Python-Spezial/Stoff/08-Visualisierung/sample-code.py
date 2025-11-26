"""--------------1-------------------"""
import plotly.express as px
import pandas as pd

# Load prepared data
df = pd.read_csv("clean_ringing_data_phenology.csv")

"""--------------5-------------------"""
fig = px.histogram(
    df,
    x="wing_length_mm",
    color="sex",
    facet_col="species", # Creates separate plot for each species
    facet_col_wrap=1,    # Max 3 plots per row
    title="Wing Length Distribution per Species & Sex",
    template="plotly_white"
)

# Adjust layout labels globally
fig.update_layout(yaxis_title="Count", xaxis_title="Wing Length (mm)")

# Save as standalone HTML file
fig.write_html("ringing_analysis_report.html")
