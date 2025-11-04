import os
from lazy_transaction_reader import LazyTransactionReader

# --- Setup: Erstellen einer Dummy-Logdatei ---
log_filename = "test_tx.log"
dummy_data = """
DEPOSIT: 1000.50
WITHDRAW: 50.00
WITHDRAW: 120.25
DEPOSIT: 300.00
SYSTEM:FEE: 5.00
WITHDRAW: 80.00
"""

try:
  with open(log_filename, "w") as f:
    f.write(dummy_data.strip())
except IOError as e:
  print(f"Setup fehlgeschlagen: {e}")
  # Beenden, wenn wir die Datei nicht schreiben können

# --- Beispiel-Nutzung (Bonus) ---
print("\n--- Bonus-Herausforderung Test 1 (alle Transaktionen) ---")
try:
  # 1. Alle Transaktionen lesen
  all_tx_reader = LazyTransactionReader(log_filename)
  for line in all_tx_reader:
    print(f"  Gelesene Zeile: {line}")
  # Beachte: Die Datei sollte jetzt automatisch geschlossen sein.

except FileNotFoundError:
  pass  # Fehler wurde bereits im Konstruktor behandelt

print("\n--- Bonus-Herausforderung Test 2 (nur 'DEPOSIT') ---")
try:
  # 2. Nur Einzahlungen (DEPOSIT) filtern
  deposit_reader = LazyTransactionReader(log_filename, filter_keyword="DEPOSIT")

  print(f"Nächstes Element (manuell): {next(deposit_reader)}")
  print(f"Nächstes Element (manuell): {next(deposit_reader)}")

  # Test auf StopIteration
  try:
    next(deposit_reader)
  except StopIteration:
    print("  Erwartete StopIteration! Der Filter-Iterator ist erschöpft.")

except FileNotFoundError:
  pass

# Aufräumen
if os.path.exists(log_filename):
  os.remove(log_filename)
