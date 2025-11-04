## Folie 2: Das Problem (Warum Iteratoren?)

**Titel:** Warum brauchen wir Iteratoren?

**Problem:** Was passiert hier bei 1 Milliarde Einträgen?

```python
def get_all_logs():
    all_entries = db.query("SELECT * FROM logs") # 1 Milliarde Zeilen
    return all_entries

# RAM-Problem: Versucht, 1 Milliarde Objekte *sofort* in den Speicher zu laden.
logs = get_all_logs()
for log in logs:
    # Verarbeitung beginnt erst, NACHDEM alles geladen ist
    process(log)
```

**Kernpunkt:** Direkte Materialisierung von großen Datensätzen im Speicher ist ineffizient und oft unmöglich.

-----

## Folie 3: Die Lösung: Das Iterator-Protokoll

**Titel:** Das Iterator-Protokoll

Python löst dies durch "Lazy Evaluation" (verzögerte Auswertung).

Ein **Iterator** ist ein Objekt, das zwei Methoden implementiert:

1.  `__iter__()`

      * Muss den Iterator selbst zurückgeben (`return self`).
      * Wird (implizit) von `for`-Schleifen aufgerufen.

2.  `__next__()`

      * Gibt das **nächste** Element der Sequenz zurück.
      * Wenn keine Elemente mehr vorhanden sind, löst es die `StopIteration` Exception aus.

**Kernaussage:** Ein Iterator ist ein "Zustandsbehaftetes Objekt" (Stateful). Er merkt sich, wo er in der Sequenz steht.

-----

## Folie 4: `iter()` und `next()` Funktionen

**Titel:** `iter()` und `next()`

Python bietet zwei Built-in-Funktionen, um manuell mit dem Protokoll zu arbeiten:

```python
my_list = [10, 20, 30]

# 1. iter() holt den Iterator von einem Iterable
my_iterator = iter(my_list) 

print(type(my_list))     # <class 'list'>
print(type(my_iterator)) # <class 'list_iterator'>

# 2. next() ruft __next__ auf, um das nächste Element zu holen
print(next(my_iterator)) # Output: 10
print(next(my_iterator)) # Output: 20
print(next(my_iterator)) # Output: 30

# 3. Das Ende der Sequenz
print(next(my_iterator)) # Löst StopIteration aus
```

Die `for`-Schleife ist nur syntaktischer Zucker für genau diesen Vorgang (inkl. automatischem Abfangen von `StopIteration`).

-----

## Folie 5: Iterable vs. Iterator (Kritischer Unterschied\!)

**Titel:** Iterable vs. Iterator

Dies ist die häufigste Fehlerquelle\!

  * **Iterable (Iterierbar):**

      * Ein Objekt, von dem man einen Iterator **bekommen** kann.
      * Implementiert nur `__iter__()`.
      * Beispiele: `list`, `tuple`, `dict`, `set`, `str`.
      * Man kann immer wieder `iter()` darauf aufrufen und erhält einen *neuen* Iterator (beginnt von vorn).

  * **Iterator:**

      * Das Objekt, das die Arbeit macht (das Zählen/Abrufen).
      * Implementiert `__iter__()` **und** `__next__()`.
      * Ist "Stateful" (hat einen Zustand) und **erschöpft sich** (Exhaustible).
      * Ein Iterator ist *auch* ein Iterable (da er `__iter__` hat), aber nicht umgekehrt\!

<!-- end list -->

```python
# list ist ein Iterable
my_list = [1, 2]

# iterator_1 ist ein Iterator
iterator_1 = iter(my_list) 
print(next(iterator_1)) # 1

# iterator_2 ist ein *neuer*, unabhängiger Iterator
iterator_2 = iter(my_list) 
print(next(iterator_2)) # 1 (beginnt von vorn)

print(next(iterator_1)) # 2 (iterator_1 war bei Position 1)
```

-----

## Folie 6: Der Vorteil: Speicher-Effizienz

**Titel:** Lazy Evaluation & Speicher-Effizienz

Iteratoren laden Daten "on demand" (bei Bedarf) – erst wenn `next()` aufgerufen wird.

**Beispiel: Log-Datei lesen (Problem von Folie 2 gelöst)**

```python
# Datei-Handler in Python sind Iteratoren
with open("massive_log_file.log", "r") as f:
    # 'f' ist ein Iterator.
    # 'f.readline()' (oder __next__) wird bei jedem Schleifendurchlauf aufgerufen.
    
    for line in f:
        # Es ist immer nur EINE Zeile gleichzeitig im Speicher!
        process(line)

# Ergebnis: Verarbeitung einer 100 GB Datei mit < 1 MB RAM.
```

**Kernaussage:** Iteratoren entkoppeln die *Definition* einer Sequenz von der *Berechnung* ihrer Elemente.

-----

## Folie 7: Eigene Iteratoren bauen (Klassen-Ansatz)

**Titel:** Implementierung eines Iterators

Ein Iterator, der die ersten *n* Fibonacci-Zahlen generiert, ohne sie alle vorab zu berechnen.

```python
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current_count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        # Der Iterator ist... er selbst.
        return self

    def __next__(self):
        if self.current_count >= self.max_count:
            raise StopIteration
        
        self.current_count += 1
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val

# Nutzung:
fibo_seq = FibonacciIterator(5)

# 'fibo_seq' ist sowohl Iterable als auch Iterator
for num in fibo_seq:
    print(num)

# Output:
# 0
# 1
# 1
# 2
# 3
```

-----

## Folie 8: Zusammenfassung

**Titel:** Key Takeaways

  * **Zweck:** Effiziente Verarbeitung von Sequenzen (potenziell unendlich), indem Elemente *lazy* (bei Bedarf) erzeugt werden.
  * **Protokoll:** `__iter__` (gibt Iterator) und `__next__` (gibt nächstes Element oder `StopIteration`).
  * **Iterable (z.B. `list`):** Kann einen Iterator bereitstellen (via `iter()`).
  * **Iterator:** Das "laufende" Objekt, das sich den Zustand merkt und sich erschöpft.
  * **`for`-Loop:** Ist syntaktischer Zucker für das `iter()`/`next()`-Protokoll.
  * **Hauptvorteil:** Drastisch reduzierter Speicherverbrauch (RAM). Ermöglicht die Verarbeitung von Streams oder unendlichen Sequenzen.