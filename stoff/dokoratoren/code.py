import time


def process_data():
  start_time = time.perf_counter()  # --- SETUP ---

  # EIGENTLICHE LOGIK
  print("Starte Datenverarbeitung...")
  _ = [x ** 2 for x in range(10_000_000)]

  end_time = time.perf_counter()  # --- TEARDOWN ---
  print(f"process_data dauerte {end_time - start_time:.4f}s")


def fetch_web_data():
  start_time = time.perf_counter()  # --- SETUP (Identisch) ---

  # EIGENTLICHE LOGIK
  print("Starte Web-Download...")
  time.sleep(2)  # Simuliert Download

  end_time = time.perf_counter()  # --- TEARDOWN (Identisch) ---
  print(f"fetch_web_data dauerte {end_time - start_time:.4f}s")


# 1. Der DECORATOR
def timer_decorator(func_to_wrap):
  # 2. Der WRAPPER
  def wrapper_function():
    start_time = time.perf_counter()

    func_to_wrap()  # 3. AUFRUF DER ORIGINALFUNKTION

    end_time = time.perf_counter()
    print(f"{func_to_wrap.__name__} dauerte {end_time - start_time:.4f}s")

  # 4. Der Decorator gibt den Wrapper zurück
  return wrapper_function


# --- Nutzung ---

def process_data():
  """Eine Funktion, die dekoriert werden soll."""
  print("Starte Datenverarbeitung...")
  _ = [x ** 2 for x in range(10_000_000)]


# 5. Manuelle "Dekoration"
# Wir ersetzen die alte Funktion durch die neue Wrapper-Funktion
process_data = timer_decorator(process_data)

# 6. Aufruf des Wrappers
process_data()


# Dieser Code:
@timer_decorator
def process_data():
  """Eine Funktion, die dekoriert werden soll."""
  print("Starte Datenverarbeitung...")
  _ = [x ** 2 for x in range(10_000_000)]


# Equivalent
def process_data():
  """Eine Funktion, die dekoriert werden soll."""
  print("Starte Datenverarbeitung...")
  _ = [x ** 2 for x in range(10_000_000)]


process_data = timer_decorator(process_data)

import time
from functools import wraps  # 1. Importieren


@timer_decorator
def process_data():
    """Das ist der Docstring für process_data."""
    pass

print(process_data.__name__)
print(process_data.__doc__)

def timer_decorator(func_to_wrap):
  @wraps(func_to_wrap)  # 2. @wraps auf den Wrapper anwenden
  def wrapper_function(*args, **kwargs):  # 3. *args, **kwargs (WICHTIG!)
    """Der Docstring des Wrappers (wird ersetzt)."""
    start_time = time.perf_counter()

    result = func_to_wrap(*args, **kwargs)  # 4. Argumente weiterleiten

    end_time = time.perf_counter()
    print(f"{func_to_wrap.__name__} dauerte {end_time - start_time:.4f}s")
    return result  # 5. Rückgabewert zurückgeben

  return wrapper_function


@timer_decorator
def process_data():
    """Das ist der Docstring für process_data."""
    pass

print(process_data.__name__)
print(process_data.__doc__)