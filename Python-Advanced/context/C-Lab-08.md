1.  **Zweck (Das "Warum"):**

      * Dient der Einhaltung des **DRY-Prinzips** (Don't Repeat Yourself).
      * Wird verwendet, um wiederkehrende Logik (sog. "Cross-Cutting Concerns") aus Business-Funktionen auszulagern.
      * **Typische Beispiele für Übungen:** Logging (z.B. "Funktion X wurde aufgerufen"), Timing (z.B. "Funktion X dauerte 0.5s"), Caching, Authentifizierungs-Checks (z.B. "Ist der User Admin?").

2.  **Mechanismus (Das "Wie"):**

      * Ein Dekorator ist eine Funktion (z.B. `my_decorator`), die eine Funktion (`func`) als Parameter akzeptiert.
      * *Innerhalb* des Dekorators wird eine neue Funktion (meist `wrapper` genannt) definiert.
      * Der `wrapper` enthält die Zusatzlogik (z.B. Zeitmessung davor/danach) und **ruft in der Mitte die Originalfunktion `func` auf**.
      * Der Dekorator gibt die `wrapper`-Funktion zurück.

3.  **Syntax (Das `@`-Symbol):**

      * Das `@my_decorator`-Symbol (Syntactic Sugar) ist nur eine Kurzschreibweise.
      * Eine Übung sollte den Zusammenhang zwischen der `@`-Syntax und der manuellen Zuweisung verdeutlichen:

    <!-- end list -->

    ```python
    @my_decorator
    def say_hello():
        pass

    # IST IDENTISCH ZU:

    def say_hello():
        pass
    say_hello = my_decorator(say_hello)
    ```

4.  **Wichtige Stolpersteine (Kern der Übungen):**

      * **Problem 1: Argumente:** Ein einfacher `wrapper()` schlägt fehl, wenn die dekorierte Funktion Argumente entgegennimmt (z.B. `say_hello(name)`).
          * **Lösung:** Der Wrapper muss `*args` und `**kwargs` verwenden, um flexibel alle Argumente an die Originalfunktion `func(*args, **kwargs)` durchzureichen.
      * **Problem 2: Rückgabewerte:** Ein Wrapper, der `func()` nur aufruft, "verschluckt" den Rückgabewert der Originalfunktion.
          * **Lösung:** Der Wrapper muss den Rückgabewert auffangen und zurückgeben: `result = func(*args, **kwargs)` und `return result`.
      * **Problem 3: Metadaten (Kritisch):** Der Dekorator ersetzt die Originalfunktion (`say_hello`) durch den `wrapper`. Das bedeutet, Metadaten wie der Name (`__name__`) oder der Docstring (`__doc__`) gehen verloren (es wird "wrapper" angezeigt). Das bricht Debugging und `help()`.
          * **Lösung:** Die **`@functools.wraps(func)`**-Dekoration muss auf die *innere* `wrapper`-Funktion angewendet werden. Dies kopiert alle Metadaten von `func` auf den `wrapper`.