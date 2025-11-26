1.  **Das Iterator-Protokoll:** Übungen sollten das Verständnis des Protokolls testen. Ein Objekt ist ein **Iterator**, wenn es zwei Methoden implementiert:
    * `__iter__()`: Muss den Iterator selbst zurückgeben (`return self`).
    * `__next__()`: Gibt das nächste Element zurück. Wenn die Sequenz erschöpft ist, muss die `StopIteration`-Exception ausgelöst werden.

2.  **Iterable vs. Iterator (Wichtiger Unterschied):**
    * Ein **Iterable** (z.B. `list`, `tuple`, `str`) ist ein Objekt, von dem man (mit `iter()`) einen Iterator *bekommen* kann. Es implementiert `__iter__()`.
    * Ein **Iterator** ist das "zustandsbehaftete" Objekt, das `__next__()` implementiert und sich merkt, wo es sich in der Sequenz befindet. Ein Iterator ist *erschöpfbar* (kann nur einmal durchlaufen werden).

3.  **Implementierung (Klassen-Ansatz):**
    * Übungen sollten das manuelle Erstellen einer Iterator-Klasse beinhalten.
    * Dies erfordert die Implementierung von `__init__` (zur Initialisierung des Zustands, z.B. `self.count = 0`), `__iter__` und `__next__`.
    * Besonderes Augenmerk liegt auf der korrekten Zustandsverwaltung (z.B. Inkrementieren eines Zählers) und dem korrekten Auslösen von `StopIteration` in der `__next__`-Methode.

4.  **Verbrauch/Nutzen:**
    * Übungen sollten den Unterschied zwischen `for`-Schleifen (die `StopIteration` automatisch abfangen) und der manuellen Nutzung von `next()` (wo der Fehler sichtbar wird) demonstrieren.
    * Der Aspekt der **Speichereffizienz** (z.B. Verarbeitung einer "simulierten" großen Datenmenge) sollte im Fokus stehen.