def get_user_data(user_id):
  # ... komplexe Logik ...
  if user_id == 0:
    return None  # Gibt 'None' zurück

  return {"name": "Alice", "id": user_id}  # Gibt 'dict' zurück


# Was ist 'user' hier? Ein dict? Oder None?
user = get_user_data(request.id)

# Dieser Code stürzt AB, wenn user_id == 0 ist
print(user["name"])
# AttributeError: 'NoneType' object is not subscriptable





# Wir brauchen 'Optional' aus dem 'typing'-Modul
from typing import Optional


def get_user_data(user_id: int) -> Optional[dict]:
  """Holt User-Daten. Kann None zurückgeben, wenn nicht gefunden."""

  if user_id == 0:
    return None  # Erwartet (gemäß 'Optional')

  return {"name": "Alice", "id": user_id}  # Erwartet (gemäß 'dict')


# IDEs und Tools verstehen das jetzt
user = get_user_data(0)

# print(user["name"]) # <-- IDE/Tool warnt uns hier!


def add(a: int, b: int) -> int:
  """Diese Funktion erwartet 'int'."""
  return a + b


# --- KEIN FEHLER! ---
# Dieser Code läuft (leider) problemlos durch,
# obwohl er die Annotationen verletzt.
result = add("Hallo ", "Welt")

print(result)
# Output: Hallo Welt


# 'list' und 'dict' direkt verwenden
def process_data(data: list[str]) -> dict[str, int]:
    ...
    return {"count": len(data)}


from typing import List, Dict

# 'List' und 'Dict' (Großbuchstabe) aus typing
def process_data(data: List[str]) -> Dict[str, int]:
    ...
    return {"count": len(data)}