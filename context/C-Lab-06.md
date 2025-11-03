### 1. `lambda`-Funktionen (Voraussetzung)

* **Zweck:** Dienen als anonyme "Wegwerf-Funktionen".
* **Syntax:** `lambda argumente: expression`
* **Kontext für Übungen:** `lambda`s sind das "Werkzeug", das als erstes Argument an `map` und `filter` übergeben wird, um die Logik "inline" zu definieren.

### 2. `map(function, iterable)`

* **Konzept:** 1:1-Transformation (Eins-zu-Eins-Transformation).
* **Zweck:** Wendet die `function` auf **jedes** Element des `iterable` an.
* **Rückgabewert:** Ein **Iterator** (lazy). Das Ergebnis muss oft mit `list()` materialisiert werden.
* **Kernaussage:** Die Anzahl der Elemente in der Ausgabe ist gleich der Anzahl der Elemente in der Eingabe.
* **Übungskontext:**
    * Umwandlung von Datentypen (z.B. `str`-Liste in `int`-Liste).
    * Mathematische Operationen auf Listen (z.B. alle Zahlen verdoppeln, quadrieren).
    * Datenextraktion (z.B. den Namen aus einer Liste von Dictionaries holen).

### 3. `filter(function, iterable)`

* **Konzept:** N:M-Selektion (Auswahl).
* **Zweck:** Filtert ein Iterable. Es behält nur die Elemente, für die die `function` (das Prädikat) `True` zurückgibt.
* **Rückgabewert:** Ein **Iterator** (lazy).
* **Kernaussage:** Die Anzahl der Elemente in der Ausgabe ist kleiner oder gleich der Anzahl in der Eingabe.
* **Übungskontext:**
    * Herausfiltern von Daten basierend auf einer Bedingung (z.B. nur gerade Zahlen behalten, nur Strings mit mehr als 5 Zeichen).
    * Bereinigen von Listen (z.B. `None`-Werte oder Leerstrings entfernen).

### 4. `functools.reduce(function, iterable)`

* **Konzept:** N:1-Aggregation (Reduktion).
* **Zweck:** Reduziert ein Iterable auf einen **einzigen Wert**, indem die `function` kumulativ angewendet wird.
* **Wichtige Details:**
    * Muss aus `functools` importiert werden.
    * Die `function` muss **zwei Argumente** annehmen: den `accumulator` (Zwischenergebnis) und das `current_element`.
* **Rückgabewert:** Ein einzelner Wert (nicht-lazy).
* **Übungskontext:**
    * Aggregations-Aufgaben (z.B. die Summe oder das Produkt einer Liste berechnen).
    * Auffinden eines "besten" Elements (z.B. den längsten String in einer Liste finden).
    * Zusammenführen von Daten (z.B. alle Listen in einer Liste zu einer flachen Liste zusammenfügen).

### Wichtige Abgrenzung für Übungen

* Übungen sollten den **Unterschied zu List Comprehensions** betonen.
* `[x * 2 for x in numbers]` ist oft "pythonischer" als `list(map(lambda x: x * 2, numbers))`.
* `[x for x in numbers if x % 2 == 0]` ist oft "pythonischer" als `list(filter(lambda x: x % 2 == 0, numbers))`.
* `reduce` ist oft schwerer lesbar als eine `for`-Schleife oder ein Built-in (wie `sum()`). Übungen sollten dies kontrastieren.