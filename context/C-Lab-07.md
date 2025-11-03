1.  **Das `yield`-Schlüsselwort:** Das Kernkonzept. Sobald eine Funktion das `yield`-Schlüsselwort enthält, wird sie zu einer **Generator-Funktion**.
2.  **Keine normale Ausführung:** Der Aufruf einer Generator-Funktion (z.B. `my_gen = gen_func()`) führt den Code **nicht** aus. Er gibt sofort ein **Generator-Objekt** zurück.
3.  **Automatisch ein Iterator:** Dieses Generator-Objekt implementiert automatisch das Iterator-Protokoll (d.h. `__iter__()` und `__next__()`). Man muss diese nicht manuell schreiben.
4.  **"Pause & Resume"-Mechanismus:**
    * `yield` ist der entscheidende Unterschied zu `return`.
    * Wenn `next()` auf dem Generator aufgerufen wird, läuft der Code bis zum ersten `yield`.
    * `yield` gibt den Wert zurück und **friert den Zustand der Funktion ein** (Pause). Alle lokalen Variablen (`a`, `b`, `count`, etc.) bleiben im Speicher erhalten.
    * Beim nächsten `next()`-Aufruf wird die Funktion **exakt nach dem `yield`** fortgesetzt (Resume).
5.  **Automatisches `StopIteration`:** Wenn die Generator-Funktion ihr Ende erreicht (oder ein `return` trifft), wird bei der nächsten Anforderung von `next()` automatisch `StopIteration` ausgelöst.
6.  **Evidenz (Klasse vs. Generator):** Übungen sollten den Kontrast herausstellen. Generatoren ersetzen den gesamten "Boilerplate"-Code (die `__init__`, `__iter__`, `__next__`-Methoden einer Klasse) durch eine einzige, lineare Funktion.
7.  **Speichereffizienz:** Der Nutzen ist identisch zu Iteratoren – Daten werden "on demand" erzeugt, nicht alle auf einmal im Speicher gehalten.