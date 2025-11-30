import pandas as pd


# Wir importieren die Funktion aus Teil 1 oder nutzen den Code erneut
# Hier simulieren wir, dass df_result bereitsteht:
# df_result = clean_and_merge()

def advanced_analysis(df):
    print("\n--- BONUS: Time Series & Pivot ---")

    # 1. Setup Datetime Index
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    # 2. Resampling (Wochen-Aggregation)
    # 'W' = Weekly frequency. Wir summieren die Beträge pro Woche.
    weekly_stats = df['amount'].resample('W').sum()

    print("Wöchentliches Volumen:")
    print(weekly_stats)

    # 3. Pivot Table
    # Zeigt multidimensionale Zusammenhänge
    pivot = pd.pivot_table(
        df,
        values='amount',
        index='region',
        columns='type',
        aggfunc='mean'
    )

    print("\nDurchschnittlicher Betrag (Pivot nach Region & Typ):")
    print(pivot)


if __name__ == "__main__":
    # Um dieses Skript standalone lauffähig zu machen, müssen wir Teil 1 kurz wiederholen
    # oder die Daten neu laden. Der Einfachheit halber:
    try:
        tx = pd.read_csv('transactions_dirty.csv').fillna(0)
        cu = pd.read_csv('customers.csv')
        full_df = pd.merge(tx, cu, on='account_id', how='left')
        advanced_analysis(full_df)
    except FileNotFoundError:
        print("Bitte zuerst das Setup-Skript aus der Angabe ausführen!")
