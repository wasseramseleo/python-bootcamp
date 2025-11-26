## Folie 1: Das Problem (Iteratoren sind aufwändig)

**Titel:** Das Problem: Iteratoren sind "Boilerplate"

**Rückblick (aus dem letzten Kapitel):**
Um einen Iterator als Klasse zu bauen, brauchen wir viel Code:

  * `__init__()` zum Initialisieren des Zustands.
  * `__iter__()` muss `self` zurückgeben.
  * `__next__()` muss die Logik enthalten, den Zustand (State) verwalten UND `StopIteration` manuell auslösen.

<!-- end list -->

```python
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current_count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count >= self.max_count:
            raise StopIteration
        # ... (Logik) ...
```

**Kritik:** Das ist komplex und unübersichtlich für eine einfache Sequenz.

-----

## Folie 2: Die Lösung: Generator-Funktionen (`yield`)

**Titel:** Die Lösung: Generator-Funktionen

**Konzept:** Eine Funktion, die `yield` statt `return` verwendet.

**Was passiert?**

1.  Sobald Python das `yield`-Schlüsselwort in einer Funktion (einem `def`-Block) sieht, wird diese *nicht* wie eine normale Funktion behandelt.
2.  Der Aufruf der Funktion führt den Code **nicht** aus.
3.  Stattdessen gibt der Aufruf sofort ein **Generator-Objekt** zurück.
4.  Dieses Generator-Objekt ist *automatisch* ein voll funktionsfähiger Iterator (es implementiert `__iter__` und `__next__` für uns).

<!-- end list -->

```python
def fibonacci_generator(max_count):
    """
    Ein Generator, der Fibonacci-Zahlen 'yielded' (ergibt).
    """
    print("Generator wird gestartet...")
    count = 0
    a, b = 0, 1
    while count < max_count:
        yield a # 3. Hier pausiert die Funktion
        a, b = b, a + b
        count += 1
    print("Generator ist am Ende.")

# 1. Aufruf erzeugt nur das Generator-Objekt.
# (Der print()-Befehl oben wird NICHT ausgeführt)
fib_gen = fibonacci_generator(5)

print(type(fib_gen))
# Output: <class 'generator'>
```

-----

## Folie 3: Die Magie von `yield`: Pause & Resume

**Titel:** Die Magie von `yield`: "Pause & Resume"

`yield` ist der entscheidende Unterschied zu `return`:

  * `return`: Beendet die Funktion endgültig.
  * `yield`: Gibt einen Wert zurück (wie `return`), aber **friert den Zustand der Funktion ein** (Pause). Alle lokalen Variablen (`count`, `a`, `b`) bleiben erhalten.

Beim nächsten Aufruf von `next()` auf dem Generator wird die Funktion *exakt nach dem `yield`* fortgesetzt (Resume).

```python
fib_gen = fibonacci_generator(3) # 'fib_gen' ist jetzt ein Iterator

# 2. next() startet den Code bis zum ersten 'yield'
print(f"Ergebnis 1: {next(fib_gen)}")
# Output:
# Generator wird gestartet...
# Ergebnis 1: 0

# 4. next() setzt den Code nach 'yield a' fort
print(f"Ergebnis 2: {next(fib_gen)}")
# Output:
# Ergebnis 2: 1

print(f"Ergebnis 3: {next(fib_gen)}")
# Output:
# Ergebnis 3: 1

# 5. Die Schleife endet, die Funktion terminiert.
# next() löst automatisch StopIteration aus.
print(next(fib_gen))
# Output:
# Generator ist am Ende.
# Traceback (most recent call last):
#   ...
# StopIteration
```

-----

## Folie 4: Evidenz: Klasse vs. Generator

**Titel:** Evidenz: Der "Pythonic Way"

Generatoren sind syntaktischer Zucker für das Iterator-Protokoll. Sie sind fast immer die bessere Wahl.

| Feature | Klasse (Iterator) | Funktion (Generator) |
| :--- | :--- | :--- |
| **Code** | `__init__`, `__iter__`, `__next__` | Nur die `def`-Funktion |
| **State** | Manuell in `self` (z.B. `self.count`) | Automatisch (lokale Variablen) |
| **Ende** | `StopIteration` manuell auslösen | Automatisch bei Funktionsende |
| **Lesbarkeit**| Gering (Logik auf 3 Methoden verteilt) | Hoch (Logik ist linear) |

**Kritische Aussage (Evidence):** Der Generator-Ansatz (rechts) ist kürzer, sauberer und vermeidet den gesamten Boilerplate-Code der Klasse, während er exakt dasselbe Ziel (einen "lazy" Iterator) erreicht.

```python
# Links: Klasse (aus Folie 1)
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current_count = 0
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_count >= self.max_count:
            raise StopIteration
        self.current_count += 1
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val
```

```python
# Rechts: Generator (Elegant)
def fibonacci_generator(max_count):
    count = 0
    a, b = 0, 1
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1
```

-----

## Folie 5: Zusammenfassung: Generatoren

**Titel:** Key Takeaways

  * **Zweck:** Der einfachste Weg, "lazy" Iteratoren zu erstellen.
  * **Syntax:** Eine Funktion (`def`), die `yield` verwendet.
  * **`yield`:** Pausiert die Funktion, speichert den Zustand und gibt einen Wert zurück.
  * **Vorteil (Speicher):** Identisch zu Iteratoren. Es wird immer nur ein Element "on demand" berechnet (Lazy Evaluation).
  * **Vorteil (Lesbarkeit):** Deutlich sauberer und kürzer als eine Iterator-Klasse.
  * **Nutzung:** Ideal für Daten-Streaming, das Lesen großer Dateien (Zeile für Zeile) oder die Erzeugung von potenziell unendlichen Sequenzen.