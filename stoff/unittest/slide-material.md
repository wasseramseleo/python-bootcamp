Hier sind die Inhalte für die Slides zum Thema Unit-Testing mit `pytest`.

-----

## Folie 1: Titel

**Titel:** Unit-Tests mit `pytest`
**Untertitel:** Code-Qualität durch modernes, "Pythonic" Testing

-----

## Folie 2: Warum Unit-Tests? (Kritik am manuellen Testen)

**Titel:** 🧪 Warum Unit-Tests? (Das Problem)

Manuelles Testen (z.B. Skript starten, `print()`-Ausgaben prüfen) ist:

  * **Langsam:** Erfordert manuelle Interaktion.
  * **Fehleranfällig:** Man vergisst, Edge Cases zu prüfen.
  * **Nicht wiederholbar:** Ein Kollege kann den Test nicht exakt gleich ausführen.
  * **Blockierend:** Verhindert sicheres Refactoring.

**Kritische Evidenz (Evidence):**
Jede Zeile Code, die Sie schreiben, ist eine potenzielle Fehlerquelle ("Liability"). **Tests sind das Sicherheitsnetz (Safety Net)**, das beweist, dass Ihr Code (und zukünftiges Refactoring) funktioniert.

**Unit-Test (Definition):** Ein automatisierter Test, der die kleinste isolierte Einheit (eine Funktion oder Methode) prüft.

-----

## Folie 3: Kritik: `pytest` vs. `unittest` (Standard-Bibliothek)

**Titel:** Evidenz: Warum `pytest` (und nicht `unittest`)?

`unittest` ist in Python eingebaut, aber `pytest` ist der De-facto-Standard in der Industrie.

| Feature | `unittest` (Standard-Bibliothek) | `pytest` (Third-Party) |
| :--- | :--- | :--- |
| **Boilerplate** | **Hoch.** Man muss von `TestCase` erben. | **Keins.** Einfache `test_...` Funktionen. |
| **Asserts** | Umständlich (`self.assertEqual(a, b)`) | Nativ (`assert a == b`) |
| **Fehlermeldung** | Limitiert (`AssertionError: X != Y`) | **Überlegen.** Zeigt *genau*, was ungleich ist ("Magic Asserts"). |
| **Setup/Cleanup** | `setUp()`, `tearDown()` Methoden | **Fixtures** (Flexibler, wiederverwendbar) |

**Evidenz (Beispiel):**

```python
# unittest (Umständlich)
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
```

```python
# pytest (Pythonic, sauber)
# (Keine Imports, keine Klasse nötig)

def test_add():
    assert add(2, 3) == 5
```

-----

## Folie 4: `pytest`-Grundlagen: Discovery & `assert`

**Titel:** Grundlagen: Test Discovery & `assert`

**1. Test Discovery (Auffinden):**
Wie findet `pytest` Ihre Tests? (Standard-Konventionen):

  * Sucht nach Dateien namens `test_*.py` oder `*_test.py`.
  * Innerhalb dieser Dateien, sucht nach:
      * Funktionen namens `test_*()`.
      * Klassen namens `Test*` (die *kein* `__init__` haben dürfen).

**2. Das `assert`-Statement:**
Der Kern von `pytest`. `pytest` "überschreibt" das normale `assert`, um detaillierte Berichte zu geben.

```python
# in test_string_utils.py

def test_capitalize():
    assert "hello".capitalize() == "Hello"

def test_type_error():
    # Testet, ob der erwartete Fehler auftritt
    with pytest.raises(TypeError):
        "string" + 5
```

-----

## Folie 5: Evidenz: "Magic Asserts" (Introspektion)

**Titel:** Evidenz: Die "Magic Asserts" von `pytest`

**Problem:** Warum ist ein Test fehlgeschlagen?

**`unittest`:**
`AssertionError: {'a': 1, 'b': 2} != {'a': 1, 'b': 99}` (Man muss manuell vergleichen).

**`pytest` (Introspektion):**
`pytest` analysiert den `assert`-Befehl und zeigt den Unterschied.

```bash
$ pytest
...
>   assert {'a': 1, 'b': 2} == {'a': 1, 'b': 99}
E   AssertionError: assert {'a': 1, 'b': 2} == {'a': 1, 'b': 99}
E     Omitting 1 identical items
E     Differing items:
E     {'b': 2} != {'b': 99}
```

**Kritische Folgerung:** `pytest` reduziert die Zeit für das Debugging von Tests drastisch, da der Fehler sofort ersichtlich ist.

-----

## Folie 6: 💡 Das Kernkonzept: Fixtures (Setup & Teardown)

**Titel:** Fixtures: Setup & Cleanup (`@pytest.fixture`)

**Problem:** Viele Tests benötigen denselben Setup-Code (z.B. eine DB-Verbindung, ein User-Objekt, ein temporäres Verzeichnis).

**Lösung: Fixtures.** Eine Funktion, die mit `@pytest.fixture` markiert ist und Daten "bereitstellt" (via `return` oder `yield`).

Tests "fordern" Fixtures an, indem sie sie als Argumente benennen (Dependency Injection).

```python
import pytest

@pytest.fixture
def empty_user_db():
    """Stellt eine leere In-Memory-DB bereit."""
    db = setup_database()
    yield db # 1. Test läuft hier...
    db.cleanup() # 2. ...Teardown (wird garantiert ausgeführt)

# --- Nutzung ---

def test_add_user(empty_user_db): # Fixture wird hier "injiziert"
    db = empty_user_db
    db.add_user("alice")
    assert db.count() == 1
```

**Vorteil:** Trennt das *Setup* (die Fixture) sauber von der *Test-Logik*. Extrem wiederverwendbar.

-----

## Folie 7: Parametrisierung (Testing von Edge Cases)

**Titel:** Parametrisierung (`@pytest.mark.parametrize`)

**Problem:** Wie testet man eine Funktion mit 10 verschiedenen Eingaben (Gültige Daten, ungültige Daten, `None`, 0, ...)?

**Schlechte Lösung:** 10 fast identische `test_...`-Funktionen kopieren.

**Beste Lösung (DRY): `@pytest.mark.parametrize`**
Erlaubt es, *eine* Testfunktion mit *mehreren* Datensätzen laufen zu lassen.

```python
def is_valid_email(email):
    # ... Logik ...
    pass

@pytest.mark.parametrize("email_input, expected_result", [
    ("test@mail.com", True),       # Fall 1
    ("user.name@sub.domain.org", True),  # Fall 2
    ("invalid-mail", False),     # Fall 3 (Edge Case)
    ("", False),                  # Fall 4 (Edge Case)
    (None, False),                # Fall 5 (Edge Case)
])
def test_email_validation(email_input, expected_result):
    assert is_valid_email(email_input) == expected_result
```

**Evidenz:** `pytest` führt 5 separate Tests aus. Wenn "invalid-mail" fehlschlägt, werden die anderen 4 trotzdem als "PASS" angezeigt.

-----

## Folie 8: Isolation & Mocking (`pytest-mock`)

**Titel:** Isolation durch "Mocking" (Externe Systeme ersetzen)

**Problem:** Ein **Unit-Test** muss *isoliert* sein. Wenn `test_payment()` eine *echte* externe API (z.B. Stripe, PayPal) aufruft, ist das:

1.  **Langsam** (Netzwerk-Latenz).
2.  **Unzuverlässig** (Die API kann down sein).
3.  **Teuer** (kann Geld kosten).
4.  **Kein Unit-Test** (sondern ein Integrationstest).

**Lösung: Mocking.** Das Ersetzen von externen Abhängigkeiten (wie `requests.post`) durch "Attrappen" (Mocks).

**Tool:** Das `pytest-mock` Plugin (stellt die `mocker`-Fixture bereit).

```python
# test_payment_service.py

def test_charge_user(mocker): # 'mocker' Fixture anfordern
    
    # Ersetze 'requests.post' durch einen Mock,
    # der ein Fake-JSON zurückgibt
    mocker.patch("requests.post", 
                 return_value=MockResponse(status_code=200))

    # Führe den Test aus
    result = payment_service.charge_user("user_123", 100)
    
    # Teste *unseren* Code, nicht die API
    assert result == "SUCCESS" 
```

-----

## Folie 9: Ausführung & Testabdeckung (Coverage)

**Titel:** Ausführung (CLI) & Coverage

**Ausführung (Kommandozeile):**

```bash
# Alle Tests ausführen (sucht rekursiv)
$ pytest

# "Verbose" (Zeigt jeden Testnamen an)
$ pytest -v

# Führe nur Tests aus, die "user" im Namen haben
$ pytest -k "user"

# Stoppe beim ersten Fehler und öffne den Debugger
$ pytest -x --pdb
```

**Testabdeckung (Coverage):**
"Welche Zeilen meines Codes wurden von *keinem* Test berührt?"

**Tool:** `pytest-cov` (ein Plugin)

```bash
# Führe Tests aus UND messe die Abdeckung für 'my_package'
$ pytest --cov=my_package

# Erzeuge einen HTML-Report (zeigt Zeile für Zeile, was fehlt)
$ pytest --cov=my_package --cov-report=html
```

**Evidenz:** Coverage-Reports sind essenziell, um "blinde Flecken" (ungetestete `if/else`-Zweige) im Code zu finden.