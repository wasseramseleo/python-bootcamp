import plotly.io as pio

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
