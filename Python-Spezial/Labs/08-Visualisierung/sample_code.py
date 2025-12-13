"""--------------1-------------------"""
import plotly.express as px
import pandas as pd

# Load prepared data
df = pd.read_csv("clean_ringing_data.csv")
# df = pd.read_csv("clean_ringing_data_phenology.csv")

# Basic workflow: One-liner command -> interactive figure
fig = px.scatter(df, x="wing_length_mm", y="weight_g")
fig.show() # Opens in browser/notebook

"""--------------2-------------------"""
fig = px.scatter(
    df,
    x="wing_length_mm",
    y="weight_g",
    color="species",     # Different color per species
    size="fat_score",    # Larger points = more fat reserves
    hover_data=['ring_id', 'date'], # Extra info in tooltip
    title="Morphometric Analysis: Wing vs. Weight"
)
fig.show()

"""--------------3-------------------"""
# Pre-aggregated data (e.g., from groupby)
top_species = df['species'].value_counts().nlargest(10).reset_index()
top_species.columns = ['species', 'count']

fig = px.bar(
    top_species,
    x="count",
    y="species",
    orientation='h', # Horizontal bars
    text="count",    # Display values on bars
    title="Top 10 Most Captured Species"
)
fig.update_traces(textposition='outside') # Style text labels
fig.show()

"""--------------4-------------------"""
# Assuming 'date' is datetime and counts are aggregated daily
fig = px.line(
    daily_counts_df,
    x="date",
    y="captures",
    color="year", # Compare different years
    markers=True, # Add markers to line points
    title="Migration Phenology (Daily Captures)"
)
# Customize x-axis ticks
fig.update_xaxes(dtick="M1", tickformat="%b") # Ticks every Month, format "Jan", "Feb"...
fig.show()

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
