# LAB DETAILS:

* **Lab Title/Topic:** Lab 15: Unittests mit pytest
* **Learning Objectives:**
  * Students know how to do basic unit testing
  * Students understand fixtures, parametrize, and basic mocking
* **Context & Slide Summary:**

* **Problem:** Manuelles Testen ist langsam, fehleranfällig und nicht skalierbar. Unit-Tests sind das **Sicherheitsnetz (Safety Net)** für Refactoring.

* **Evidenz: `pytest` > `unittest`**
    * `pytest` ist der De-facto-Industriestandard.
    * Es gewinnt durch:
        1.  **Weniger Code:** Einfache `test_...` Funktionen statt `TestCase`-Klassen.
        2.  **Native Asserts:** `assert a == b` statt `self.assertEqual(a, b)`.
        3.  **Magic Asserts:** `pytest` zeigt bei Fehlern *genau*, *was* ungleich war (z.B. `{'b': 2} != {'b': 99}`), was das Debugging von Tests massiv beschleunigt.

* **Kernkonzept 1: Fixtures (`@pytest.fixture`)**
    * Die Best Practice für **Setup & Cleanup** (z.B. DB-Verbindungen, Test-Objekte).
    * Fixtures werden per "Dependency Injection" (als Funktionsargument) angefordert und sind wiederverwendbar.

* **Kernkonzept 2: Parametrisierung (`@pytest.mark.parametrize`)**
    * Die DRY-Lösung ("Don't Repeat Yourself") zum Testen von **Edge Cases**.
    * Führt *eine* Testfunktion mit *vielen* verschiedenen Eingabedaten aus und meldet jeden Fall separat.

* **Kernkonzept 3: Isolation & Mocking (`pytest-mock`)**
    * Ein Unit-Test *muss* isoliert sein. Externe APIs, Datenbanken oder das Netzwerk werden "gemockt" (durch Attrappen ersetzt).
    * **Zweck:** Macht Tests schnell, zuverlässig und unabhängig von externen Systemen.

# ACTION:

Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Core Task + Bonus Challenge, and two-file format).
Dont use emojis in the instructions. The heading for core task is "Angabe" and for bonus challenge its "Bonus-Herausforderung".