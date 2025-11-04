class BankAccount:
  """
  Stellt ein Bankkonto dar. (Version für Type Hinting)
  """

  # 1. Klassen-Attribute annotiert
  owner: str
  account_number: str
  _balance: float

  def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0) -> None:
    # 2. __init__ Parameter annotiert (Return-Type ist None)
    self.owner = owner
    self.account_number = account_number
    self._balance = initial_balance

  def deposit(self, amount: float) -> bool:
    # 3. 'amount' (float) und Return-Type (bool) annotiert
    if amount > 0:
      self._balance += amount
      return True
    return False

  def withdraw(self, amount: float) -> bool:
    # 4. 'amount' (float) und Return-Type (bool) annotiert
    if 0 < amount <= self._balance:
      self._balance -= amount
      return True
    return False

  def get_balance(self) -> float:
    # 5. Return-Type (float) annotiert
    return self._balance

  def get_owner_name(self) -> str:
    # 6. Return-Type (str) annotiert
    return self.owner


def find_account_by_number(accounts: list[BankAccount], number: str) -> BankAccount | None:
  # 7. Vollständig annotiert (moderne Syntax list[T] und T | None)

  for acc in accounts:
    if acc.account_number == number:
      return acc
  return None
