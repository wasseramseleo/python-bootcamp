# LAB DETAILS:

* **Lab Title/Topic:** Lab 11: DocString
* **Learning Objectives:**
  * Students know how to document codebases
  * Students understand documentation best practises for large scale projects
* **Context & Slide Summary:**
  1.  **Definition (Was es ist):** Ein Docstring ist ein String-Literal (`"""..."""` oder `'''...'''`), das als **allererste Anweisung** (vor jeglichem Code) in einem Definitionsblock steht.
      * *Übungskontext:* Testen, ob der Docstring an der korrekten Position platziert wird und über `funktion.__doc__` abrufbar ist.

  2.  **Unterschied zu Kommentaren (Was es nicht ist):**
      * **Kommentare (`#`):** Sind für **Maintainer (Entwickler)**. Sie erklären das *WARUM* oder *WIE* der Implementierung (z.B. `# Workaround für Bug X`). Sie werden vom Interpreter ignoriert.
      * **Docstrings (`"""..."""`):** Sind für **Consumer (Benutzer/Tools)**. Sie erklären das *WAS* (z.B. "Was macht die Funktion? Was sind die Parameter?").
      * *Übungskontext:* Verständnis dieses fundamentalen Unterschieds prüfen.

  3.  **Maschinenlesbarkeit (Der wahre Zweck):**
      * Der primäre Wert von Docstrings liegt darin, dass **Tools** sie parsen:
          * **IDEs (VS Code, PyCharm):** Generieren Tooltips (Hover-Infos) und Autovervollständigung für Argumente.
          * **`help()`-Funktion:** `help(meine_funktion)` formatiert den Docstring.
          * **Dokumentations-Generatoren (Sphinx):** Scannen den Code und erstellen automatisch HTML-Dokumentationen.
      * *Übungskontext:* Ein schlecht formatierter Docstring "bricht" diese Tools, was in einer Übung simuliert werden kann.

  4.  **Strukturierte Formate (Der Kern der Übungen):**
      * Übungen müssen das Schreiben von *strukturierten* Docstrings testen, da Tools diese parsen.
      * **Google Style (bevorzugt) oder NumPy Style** sind die Standards.
      * Eine Übung muss die korrekte Verwendung der spezifischen Sektionen prüfen:
          * `Args:` (oder `Parameters:`): Zur detaillierten Beschreibung jedes Arguments (Name, Typ, Beschreibung).
          * `Returns:` (oder `Yields:`): Zur Beschreibung des Rückgabewerts (Typ, Bedeutung).
          * `Raises:` (oder `Exceptions:`): Zur Nennung der spezifischen Exceptions, die die Funktion auslösen kann (z.B. `Raises: ValueError: Wenn ID < 0 ist.`).
      
# ACTION:

Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis-Aufgabe + Bonus Challenge, and two-file format).
Dont use emojis in the instructions. The heading for Basis-Aufgabe is "Angabe" and for bonus challenge its "Bonus-Herausforderung"