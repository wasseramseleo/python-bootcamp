class BankAccount:
  """
  Stellt ein Bankkonto dar, das (intern) eine Liste von Transaktionen hält.
  Diese Klasse ist ein "Iterable".
  """

  def __init__(self, owner: str, account_number: str):
    self.owner = owner
    self.account_number = account_number
    self.__transactions = []

  def deposit(self, amount: float):
    self.__transactions.append(f"DEPOSIT: {amount} EUR")

  def withdraw(self, amount: float):
    self.__transactions.append(f"WITHDRAW: {amount} EUR")

  def get_transactions(self) -> list:
    return self.__transactions.copy()

  def __iter__(self):
    """
    Gibt ein Iterator-Objekt zurück.
    Dies macht BankAccount zu einem "Iterable".
    """
    print("LOG: BankAccount.__iter__ aufgerufen. Erzeuge neuen Iterator.")
    return AccountHistoryIterator(self.__transactions)


class AccountHistoryIterator:
  """
  Dies ist der "Iterator". Er hält den Zustand der Iteration.
  """

  def __init__(self, transactions: list):
    self._transactions = transactions
    self._index = 0  # Zustand (Wo bin ich?)

  def __iter__(self):
    """Iteratoren geben sich selbst zurück."""
    return self

  def __next__(self):
    """Gibt das nächste Element zurück oder löst StopIteration aus."""
    if self._index >= len(self._transactions):
      # Ende der Liste erreicht
      print("LOG: AccountHistoryIterator.StopIteration ausgelöst.")
      raise StopIteration
    else:
      # Daten zurückgeben und Index für nächsten Aufruf erhöhen
      current_transaction = self._transactions[self._index]
      self._index += 1
      return current_transaction