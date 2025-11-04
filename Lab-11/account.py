"""
Modul: bank_account

Dies ist der Modul-Docstring (Bonus-Aufgabe).
Er enthält die Kerndatenmodelle für die Banking-App,
insbesondere die BankAccount-Klasse.
"""

import time


class BankAccount:
  """
  Repräsentiert ein einzelnes Bankkonto eines Kunden (Bonus-Aufgabe).

  Dies ist der Klassen-Docstring. Er erklärt den Zweck der Klasse.
  IDEs wie VS Code zeigen dies als Tooltip an, wenn man über
  den Klassennamen 'BankAccount' hovert.

  Attributes:
      owner (str): Der vollständige Name des Kontoinhabers.
      account_number (str): Die eindeutige Kontonummer.
      _balance (float): Der private Kontostand.
  """

  def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0) -> None:
    """
    Initialisiert eine neue Instanz eines BankAccount (Angabe 4).

    Args:
        owner (str): Der vollständige Name des Kontoinhabers.
        account_number (str): Die eindeutige Kontonummer.
        initial_balance (float, optional): Der Startsaldo des Kontos.
            Standardwert ist 0.0.
    """
    self.owner = owner
    self.account_number = account_number
    self._balance = initial_balance

    # Ein normaler Kommentar (wird von 'help()' ignoriert)
    # Wir validieren den initial_balance hier zur Vereinfachung nicht.

  def deposit(self, amount: float) -> bool:
    """
    Zahlt einen positiven Betrag auf das Konto ein.
    (Dies ist ein simpler, einzeiliger Docstring)
    """
    if amount > 0:
      self._balance += amount
      return True
    return False

  def withdraw(self, amount: float) -> bool:
    """Hebt einen Betrag vom Konto ab, falls gedeckt (Angabe 3).

    Diese Methode prüft, ob der Betrag positiv ist und ob
    ausreichend Deckung auf dem Konto vorhanden ist.

    Args:
        amount (float): Der Betrag, der abgehoben werden soll.
            Muss positiv sein.

    Returns:
        bool: True, wenn die Abhebung erfolgreich war (d.h. Deckung
            war ausreichend). False, wenn die Deckung nicht ausreichte.

    Raises:
        ValueError: Wenn der angegebene 'amount' 0 oder negativ ist
            (Angabe 2).
    """

    # Aufgabe 2: Logik-Anpassung und 'Raises'
    if amount <= 0:
      raise ValueError("Abhebungsbetrag muss positiv sein.")

    if self._balance >= amount:
      self._balance -= amount
      return True
    else:
      # Nicht genügend Deckung
      return False

  def get_balance(self) -> float:
    """Gibt den aktuellen Kontostand zurück."""
    return self._balance