import pandas as pd


def analyze_transactions():
    # 1. Laden
    print("Lade Daten...")
    df = pd.read_csv('big_transactions.csv')

    # 2. Inspektion
    print("\n--- Info ---")
    print(df.info())
    print("\n--- Head ---")
    print(df.head())

    # 3. Filterung
    # Filter: Nur USD
    usd_mask = df['currency'] == 'USD'
    usd_transactions = df[df['currency'] == 'USD']

    # Filter: Große Abhebungen (> 2000 UND type == withdrawal)
    # Beachten Sie die Klammern () bei mehreren Bedingungen & operator
    risk_mask = (df['amount'] > 2000.00) & (df['type'] == 'withdrawal')
    large_withdrawals = df[(df['amount'] > 2000.00) & (df['type'] == 'withdrawal')]

    # 4. Reporting
    count = large_withdrawals['amount'].count()
    total_amount = large_withdrawals['amount'].sum()

    print("\n--- Report ---")
    print(f"Anzahl USD Transaktionen: {len(usd_transactions)}")
    print(f"Anzahl Risiko-Abhebungen: {count}")
    print(f"Summe Risiko-Beträge: {total_amount:,.2f}")


if __name__ == "__main__":
    analyze_transactions()
