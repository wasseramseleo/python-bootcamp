import pandas as pd

# 1. Daten erstellen
data = {
    'Datum': ['2024-01-01', '2024-01-02', '2024-01-02'],
    'Empfänger': ['Alpha GmbH', 'Beta AG', 'Alpha GmbH'],
    'Betrag': [1000, 250, 500]
}
df = pd.DataFrame(data)

# Aggregation für Sheet 2
df_summary = df.groupby('Empfänger')['Betrag'].sum().reset_index()

# 2. Export in mehrere Sheets
# Dazu brauchen wir den ExcelWriter Context Manager
output_file = 'financial_report.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Rohdaten', index=False)
    df_summary.to_excel(writer, sheet_name='Zusammenfassung', index=False)

print(f"Datei '{output_file}' erfolgreich erstellt.")

# 3. Import spezifischer Sheets
print("\n--- Check: Lese Zusammenfassung ---")
df_check = pd.read_excel(output_file, sheet_name='Zusammenfassung')
print(df_check)
