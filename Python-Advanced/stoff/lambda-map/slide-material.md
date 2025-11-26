## Folie 1: Recap ⚡ Lambda-Funktionen

Titel: Recap: `lambda`-Funktionen (Anonyme Funktionen)

Zweck: "Wegwerf-Funktionen" für einfache, einmalige Operationen.

Syntax:

```python
lambda arguments: expression
```

  * Anonym: Sie haben keinen Namen (kein `def`).
  * Beschränkt: Nur *eine* Anweisung (expression), kein `return` (das Ergebnis der Expression wird implizit zurückgegeben).
  * Nützlich: Perfekt als Argumente für Higher-Order Functions (wie `map`, `filter`, `sorted`).

Beispiel:

```python
# Traditionelle Funktion
def double(x):
    return x * 2

# Lambda-Äquivalent
double_lambda = lambda x: x * 2

# Nutzung
print(double_lambda(5)) # Output: 10
```

-----

## Folie 2: `map()` – 1:1 Transformation

Titel: `map(function, iterable)`

Zweck: Wendet eine Funktion auf *jedes* Element eines Iterables an.

Konzept (1:1 Transformation):
`[x, y, z]` -> `[f(x), f(y), f(z)]`

Beispiel: Alle Zahlen in einer Liste verdoppeln.

```python
numbers = [1, 2, 3, 4]

# Nutzung mit lambda
doubled_iterator = map(lambda x: x * 2, numbers)

# WICHTIG: map() ist "lazy"
print(doubled_iterator)
# Output: <map object at 0x...>

# Um das Ergebnis zu materialisieren:
doubled_list = list(doubled_iterator)
print(doubled_list)
# Output: [2, 4, 6, 8]
```

Kernaussage: `map` gibt einen Iterator zurück, keinen `list`. Die Berechnung erfolgt erst beim Zugriff (lazy evaluation).

-----

## Folie 3: `filter()` – N:M Selektion

Titel: `filter(function, iterable)`

Zweck: Filtert Elemente aus einem Iterable, basierend auf einer Bedingung.

Konzept (Bedingte Selektion):
Die Funktion muss `True` oder `False` zurückgeben. Nur Elemente, für die sie `True` zurückgibt, bleiben erhalten.

Beispiel: Nur gerade Zahlen aus einer Liste behalten.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Die lambda-Funktion ist das Prädikat (Bedingung)
even_iterator = filter(lambda x: x % 2 == 0, numbers)

# WICHTIG: filter() ist ebenfalls "lazy"
print(even_iterator)
# Output: <filter object at 0x...>

# Materialisierung:
even_list = list(even_iterator)
print(even_list)
# Output: [2, 4, 6]
```

-----

## Folie 4: Kritik: `map`/`filter` vs. List Comprehensions

Titel: `map`/`filter` vs. List Comprehensions

In modernem Python-Code sind `map` und `filter` oft weniger lesbar als List Comprehensions.

`map`-Beispiel:

```python
# map (funktionaler Stil)
doubled = list(map(lambda x: x * 2, numbers))

# List Comprehension (Pythonic)
doubled_comp = [x * 2 for x in numbers]
```

`filter`-Beispiel:

```python
# filter (funktionaler Stil)
even = list(filter(lambda x: x % 2 == 0, numbers))

# List Comprehension (Pythonic)
even_comp = [x for x in numbers if x % 2 == 0]
```

Kritische Anmerkung: List Comprehensions sind meistens der bevorzugte ("Pythonic") Weg. Sie sind deklarativer und oft schneller, da der Overhead der `lambda`-Aufrufe entfällt.

-----

## Folie 5: `functools.reduce()` – N:1 Aggregation

Titel: `functools.reduce(function, iterable)`

Zweck: Reduziert (aggregiert) ein Iterable auf einen einzigen Wert durch wiederholte Anwendung einer Funktion.

WICHTIG: `reduce` ist nicht mehr "built-in". Es muss importiert werden!

```python
from functools import reduce
```

Konzept (Kumulative Faltung):
Die Funktion muss *zwei* Argumente nehmen:

1.  `accumulator` (der bisherige Zwischenwert)
2.  `current_element` (das aktuelle Element)

Beispiel: Summe aller Zahlen in einer Liste.
`[1, 2, 3, 4]`

```python
from functools import reduce

numbers = [1, 2, 3, 4]

# 1. (acc=1, el=2) -> 3
# 2. (acc=3, el=3) -> 6
# 3. (acc=6, el=4) -> 10
total = reduce(lambda acc, el: acc + el, numbers)

print(total)
# Output: 10
```

-----

## Folie 6: Kritik & Nutzung von `reduce()`

Titel: Wann (und wann nicht) `reduce()`?

`reduce` ist extrem mächtig, aber oft schwer zu lesen und "un-pythonisch".

Kritik: Guido van Rossum (Pythons Erfinder) hat `reduce` absichtlich aus den Built-ins in `functools` verschoben, um den Gebrauch einzudämmen.

Regel 1: Verwende `reduce` NICHT für einfache Operationen!

```python
# SCHLECHT (schwer lesbar)
total = reduce(lambda acc, el: acc + el, numbers)

# GUT (klar, schnell, built-in)
total = sum(numbers)
```

(Das Gleiche gilt für `min()`, `max()`, `all()`, `any()`).

Regel 2: Verwende `reduce` nur, wenn die Logik komplex kumulativ ist.

Beispiel: Ein "Deep-Get" für verschachtelte Dictionaries.

```python
# Finde data['a']['b']['c'] sicher
path = ['a', 'b', 'c']
data = {'a': {'b': {'c': 42}}}

# Sicherer Zugriff, bricht bei 'None' ab
reduce(lambda d, k: d.get(k) if d else None, path, data)
# Output: 42
```

(Selbst das ist oft klarer als `for`-Schleife lösbar).