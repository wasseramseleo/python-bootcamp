from typing import Callable, Any

# Wir definieren einen "Type Alias" für unsere komplexe Transaktion
# Dies macht den Code viel lesbarer
TransactionData = dict[str, str | float | Any]
# (Any hinzugefügt, falls dicts variieren, aber str | float ist präziser für die Angabe)
TransactionDataPrecise = dict[str, str | float]


# 1. Callback-Handler (jetzt auch annotiert)
def simple_deposit_handler(tx_data: TransactionDataPrecise) -> bool:
  """
  Ein Beispiel-Handler, der nur DEPOSIT-Transaktionen verarbeitet.
  """
  # Wir können 'type' sicher abrufen, aber mypy würde warnen,
  # wenn 'type' nicht im dict[str, str | float] enthalten wäre.
  if tx_data.get('type') == 'DEPOSIT' and isinstance(tx_data.get('amount'), float):
    print(f"Verarbeite Einzahlung: {tx_data['amount']}")
    return True
  return False


# 2. Die Hauptfunktion (vollständig annotiert)
def process_batch(
    transactions: list[TransactionDataPrecise],
    handler: Callable[[TransactionDataPrecise], bool]
) -> None:
  """
  Verarbeitet einen Stapel von Transaktionen mit einem
  Callback-Handler.
  """
  print(f"\n--- Verarbeite Batch mit Handler: {handler.__name__} ---")
  processed_count = 0
  for tx in transactions:
    if handler(tx):
      processed_count += 1

  print(f"Verarbeitung abgeschlossen. {processed_count} Transaktionen verarbeitet.")


# --- Test-Code (Bonus) ---
print("--- Bonus-Herausforderung Test ---")

transactions_batch: list[TransactionDataPrecise] = [
  {'id': 'T1', 'type': 'DEPOSIT', 'amount': 100.0},
  {'id': 'T2', 'type': 'WITHDRAW', 'amount': 50.0},  # Wird ignoriert
  {'id': 'T3', 'type': 'DEPOSIT', 'amount': 300.0}
]

# Übergabe der Handler-Funktion an die process_batch-Funktion
process_batch(transactions_batch, simple_deposit_handler)


# --- Was würde mypy fangen? ---
# (Dieser Code wird nicht ausgeführt, dient nur der Demonstration)

def invalid_handler(tx: TransactionDataPrecise) -> str:
  # Falscher RÜCKGABEWERT (str statt bool)
  return "Processed"


def test_mypy():
  # mypy würde hier einen Fehler melden:
  # Argument 2 to "process_batch" has incompatible type
  # "Callable[[TransactionDataPrecise], str]";
  # expected "Callable[[TransactionDataPrecise], bool]"
  #
  # process_batch(transactions_batch, invalid_handler)
  pass