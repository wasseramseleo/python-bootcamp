# Demo: IDE Einführung & Python Basics
# Ziel: Berechnung des Zinseszins (Compound Interest) für ein Sparkonto.

def calculate_future_value(principal, rate, years):
    """
    Berechnet den Endwert einer Investition.
    Formel: PV * (1 + r)^n
    """
    # Berechnung
    result = principal * (1 + rate) ** years
    return result

# Hauptprogramm (Entry Point)
if __name__ == "__main__":
    # 1. Variablen definieren
    start_capital = 1000.0  # Startkapital in EUR
    interest_rate = 0.05    # 5% Zinsen
    duration = 10           # Laufzeit in Jahren

    # 2. Funktion aufrufen
    final_amount = calculate_future_value(start_capital, interest_rate, duration)

    # 3. Ergebnis ausgeben
    print(f"--- Finanzbericht ---")
    print(f"Startkapital: {start_capital} EUR")
    print(f"Laufzeit:     {duration} Jahre")
    print(f"Endkapital:   {final_amount:.2f} EUR")