def my_function():
  """
  DAS ist der Docstring.
  Er wird zum __doc__-Attribut.
  """

  # DAS ist nur ein Kommentar.
  # Er wird vom Interpreter ignoriert.
  pass

def add(a, b):
  """Return the sum of a and b."""
  return a + b

def complex_function(arg1, arg2):
  """Zusammenfassung in einem Satz (imperativ).

  Eine Leerzeile trennt die Zusammenfassung vom Detail.

  Hier folgt eine detailliertere Beschreibung der Logik,
  der Randbedingungen oder der Nutzungsszenarien.
  """
  pass


from my_exceptions import ItemNotFoundError


def get_item(item_id: int, include_details: bool = False) -> dict:
  """Holt einen Artikel aus der Datenbank basierend auf seiner ID.

  Args:
      item_id (int): Die primäre ID des Artikels, der gesucht wird.
      include_details (bool, optional):
          Wenn True, werden zusätzliche Details mitgeladen.
          Defaults to False.

  Returns:
      dict: Ein Dictionary mit den Artikeldaten.

  Raises:
      ItemNotFoundError: Wenn keine Artikel mit der 'item_id'
                          gefunden wurde.
  """
  if item_id == 404:
    raise ItemNotFoundError(f"Item {item_id} nicht gefunden.")

  data = {"id": item_id, "name": "Beispiel"}
  if include_details:
    data["details"] = "Weitere Infos..."
  return data