## Folie 2: Das Problem: Redundanter Code (Cross-Cutting Concerns)

**Titel:** Das Problem: Wiederholender Code

Stellen Sie sich vor, Sie möchten messen, wie lange zwei verschiedene Funktionen dauern:

```python
import time

def process_data():
    start_time = time.perf_counter() # --- SETUP ---
    
    # EIGENTLICHE LOGIK
    print("Starte Datenverarbeitung...")
    _ = [x**2 for x in range(10_000_000)]
    
    end_time = time.perf_counter() # --- TEARDOWN ---
    print(f"process_data dauerte {end_time - start_time:.4f}s")

def fetch_web_data():
    start_time = time.perf_counter() # --- SETUP (Identisch) ---
    
    # EIGENTLICHE LOGIK
    print("Starte Web-Download...")
    time.sleep(2) # Simuliert Download
    
    end_time = time.perf_counter() # --- TEARDOWN (Identisch) ---
    print(f"fetch_web_data dauerte {end_time - start_time:.4f}s")
```

**Problem (Evidence):** Das Setup/Teardown (Logging, Timing, Caching, Authentifizierung) wird in *jede* Funktion kopiert. Dies verletzt das **DRY-Prinzip** (Don't Repeat Yourself) und ist ein Wartungsalptraum.

-----

## Folie 3: Das Konzept: Higher-Order Functions

**Titel:** Das Konzept: Was ist ein Decorator?

**Definition:**
In Python sind Funktionen "First-Class Citizens". Das bedeutet:

  * Man kann sie Variablen zuweisen.
  * Man kann sie als Argumente an andere Funktionen übergeben.
  * Man kann sie *aus* anderen Funktionen zurückgeben.

**Higher-Order Function (Funktion höherer Ordnung):**
Eine Funktion, die eine andere Funktion als Argument entgegennimmt ODER eine Funktion zurückgibt.

**Ein Decorator ist...**
...eine Funktion, die eine andere Funktion (`func`) entgegennimmt, sie um zusätzliche Funktionalität "einhüllt" (`wrapper`), und die neue, "eingehüllte" Funktion zurückgibt.

`Decorator(func) -> wrapper`

-----

## Folie 4: Syntax 1: Das "klassische" Verständnis

**Titel:** Decorator-Syntax (Manuell)

So funktioniert ein Decorator "unter der Haube".

```python
# 1. Der DECORATOR (eine Higher-Order Function)
def timer_decorator(func_to_wrap):
    
    # 2. Der "WRAPPER" (die neue Funktion)
    def wrapper_function():
        start_time = time.perf_counter()
        
        func_to_wrap() # 3. AUFRUF DER ORIGINALFUNKTION
        
        end_time = time.perf_counter()
        print(f"{func_to_wrap.__name__} dauerte {end_time - start_time:.4f}s")
    
    # 4. Der Decorator gibt den Wrapper zurück
    return wrapper_function

# --- Nutzung ---

def process_data():
    """Eine Funktion, die dekoriert werden soll."""
    print("Starte Datenverarbeitung...")
    _ = [x**2 for x in range(10_000_000)]

# 5. Manuelle "Dekoration"
# Wir ersetzen die alte Funktion durch die neue Wrapper-Funktion
process_data = timer_decorator(process_data)

# 6. Aufruf des Wrappers
process_data() 
```

-----

## Folie 5: Syntax 2: Das `@`-Symbol (Syntactic Sugar)

**Titel:** Das `@`-Symbol ("Pie-Syntax")

Das `@`-Symbol ist reiner "Syntactic Sugar" (syntaktischer Zucker) für den Prozess auf der vorherigen Folie.

```python
# Dieser Code:
@timer_decorator
def process_data():
    """Eine Funktion, die dekoriert werden soll."""
    print("Starte Datenverarbeitung...")
    _ = [x**2 for x in range(10_000_000)]

# ...ist exakt dasselbe wie dieser Code:
def process_data():
    """Eine Funktion, die dekoriert werden soll."""
    print("Starte Datenverarbeitung...")
    _ = [x**2 for x in range(10_000_000)]
    
process_data = timer_decorator(process_data)
```

**Vorteil (Evidence):** Das `@`-Symbol ist deklarativ, sauber und trennt die Aspekte (Timing-Logik vs. Business-Logik) klar voneinander.

-----

## Folie 6: Das Problem: Verlorene Metadaten

**Titel:** Fortgeschrittenes Problem: Verlorene Metadaten

Unser `timer_decorator` hat einen kritischen Fehler, der in großen Projekten zum Problem wird.

```python
@timer_decorator
def process_data():
    """Das ist der Docstring für process_data."""
    pass

print(process_data.__name__)
print(process_data.__doc__)
```

**Erwarteter Output:**
`process_data`
`Das ist der Docstring für process_data.`

**Tatsächlicher Output (FALSCH):**
`wrapper_function`
`None`

**Problem (Evidence):** Wir haben `process_data` durch `wrapper_function` ersetzt. Die Metadaten (Name, Docstring, Typ-Hinweise) der Originalfunktion gehen verloren. Dies bricht Debugging-Tools, Help-Funktionen (`help(process_data)`) und die Introspektion.

-----

## Folie 7: Die Lösung: `functools.wraps`

**Titel:** Die Lösung: `functools.wraps`

Python löst dieses Problem mit einem eigenen Decorator: `@wraps`.

`@wraps` (aus dem `functools`-Modul) wird *innerhalb* unseres Decorators auf den *Wrapper* angewendet. Es kopiert alle Metadaten (`__name__`, `__doc__`, etc.) von der Originalfunktion (`func_to_wrap`) auf die `wrapper_function`.

**Der korrekte, robuste Decorator:**

```python
import time
from functools import wraps # 1. Importieren

def timer_decorator(func_to_wrap):
    
    @wraps(func_to_wrap) # 2. @wraps auf den Wrapper anwenden
    def wrapper_function(*args, **kwargs): # 3. *args, **kwargs (WICHTIG!)
        """Der Docstring des Wrappers (wird ersetzt)."""
        start_time = time.perf_counter()
        
        result = func_to_wrap(*args, **kwargs) # 4. Argumente weiterleiten
        
        end_time = time.perf_counter()
        print(f"{func_to_wrap.__name__} dauerte {end_time - start_time:.4f}s")
        return result # 5. Rückgabewert zurückgeben
    
    return wrapper_function
```

*(Anmerkung: `*args, **kwargs` und `return result` wurden hinzugefügt, damit der Decorator universell für JEDE Funktion funktioniert, unabhängig von ihren Argumenten oder Rückgabewerten.)*

-----

## Folie 8: Zusammenfassung

**Titel:** Key Takeaways

  * **Zweck:** Fügen wiederverwendbare Funktionalität (Logging, Caching, Timing, Auth) zu existierenden Funktionen hinzu, ohne deren Code zu ändern (**DRY**).
  * **Konzept:** Decorators sind "Higher-Order Functions".
  * **Syntax:** `@my_decorator` ist syntaktischer Zucker für `my_func = my_decorator(my_func)`.
  * **Implementierung:** Ein Decorator ist eine Funktion, die eine `wrapper`-Funktion *definiert* und *zurückgibt*.
  * **Best Practice (Evidence):** Verwenden Sie **immer** `@functools.wraps` auf Ihrem Wrapper, um Metadaten zu erhalten.
  * **Best Practice:** Verwenden Sie `*args, **kwargs` im Wrapper, um Argumente flexibel an die Originalfunktion durchzureichen.