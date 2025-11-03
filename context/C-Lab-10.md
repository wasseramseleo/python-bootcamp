1.  **Zweck (Das "Warum"):**
    * Der Nutzen liegt **nicht** in der Laufzeit (Python ignoriert die Hints).
    * Der Nutzen liegt in der **statischen Analyse** *vor* der Ausführung.
    * **Tools (wie `mypy`)** lesen die Hints und finden Typ-Fehler (z.B. `str` an eine Funktion übergeben, die `int` erwartet).
    * Sie dienen als **exzellente Dokumentation** (verbessern IDE-Autocomplete und Lesbarkeit).

2.  **Syntax (Das "Wie"):**
    * **Variablen:** `variable_name: type` (z.B. `age: int = 30`).
    * **Funktionen (Wichtig):** `def func(argument: ArgType) -> ReturnType:` (z.B. `def add(a: int, b: int) -> int:`).

3.  **Wichtige Stolperfalle (Das "Was-nicht"):**
    * Übungen müssen klarstellen, dass Type Annotations **keine Laufzeitfehler** (Runtime Errors) auslösen. Python erzwingt die Typen nicht.
    * `add("a", "b")` läuft in einer `def add(a: int, b: int) -> int:`-Funktion (ohne `mypy`) problemlos durch (und gibt `"ab"` zurück).

4.  **Komplexe Typen (Das `typing`-Modul & Moderne Syntax):**
    * Übungen sollten sich auf die **moderne Syntax (Python 3.10+)** konzentrieren, da sie sauberer ist:
    * **Container:** `list[int]`, `dict[str, float]`, `set[tuple[int, int]]`.
    * **Unions (Oder):** `int | str` (statt `Union[int, str]`).
    * **Optionale Werte (Wichtig):** `str | None` (statt `Optional[str]`). Dies ist essenziell für Funktionen, die `None` zurückgeben könnten (z.B. `def find_user(id) -> User | None:`).

5.  **Spezialtypen:**
    * `Any`: Eine "Wildcard", die den Type Checker effektiv anweist, "hier nicht zu prüfen". (Sollte vermieden werden).
    * `Callable`: Zum Annotieren von Funktionen, die als Argumente übergeben werden (Callbacks). Syntax: `Callable[[Arg1Type, Arg2Type], ReturnType]`.