Hier sind die Inhalte für die Slides zum Thema Docstrings.

-----

## Folie 1: Titel

Titel: Docstrings
Untertitel: Die API Ihres Codes definieren (PEP 257)

-----

## Folie 2: Was ist ein Docstring? (Und was nicht?)

Titel: Was ist ein Docstring? (Der kritische Unterschied)

Ein Docstring ist ein String-Literal, das als allererste Anweisung in einem Modul, einer Klasse, einer Funktion oder einer Methode steht.

```python
def my_function():
    """
    DAS ist der Docstring.
    Er wird zum __doc__-Attribut.
    """
    
    # DAS ist nur ein Kommentar.
    # Er wird vom Interpreter ignoriert.
    pass
```

Kritischer Unterschied (Evidence-based):

  * `#` Kommentare (Comments): Sind für Entwickler (Maintainer). Sie erklären das *WARUM* oder *WIE* der Implementierung.
  * `"""` Docstrings: Sind für Benutzer (Consumer). Sie erklären das *WAS* – wie man die Funktion benutzt (die API).

Evidenz: Docstrings sind Metadaten und zur Laufzeit verfügbar:
`print(my_function.__doc__)`

-----

## Folie 3: Wer liest Docstrings? (Spoiler: Tools\!)

Titel: Der Nutzen: Wer liest Docstrings?

Gute Docstrings sind keine "nette Geste", sondern eine technische Notwendigkeit für Tools.

1. Die `help()`-Funktion (Built-in)

`help()` parst und formatiert den Docstring.

2. IDEs & Editoren (z.B. VS Code, PyCharm)
IDEs nutzen Docstrings, um Tooltips (Hover-Infos) und Autovervollständigung (Auto-Complete) für Argumente bereitzustellen.

3. Dokumentations-Generatoren (z.B. Sphinx)
Tools wie Sphinx scannen den Code, extrahieren die Docstrings und generieren daraus automatisch eine vollständige HTML-Webseite (z.B. die offizielle Python-Doku).

Kritische Folgerung: Ein schlecht formatierter Docstring führt zu nutzlosen Tooltips und kaputter Auto-Dokumentation.

-----

## Folie 4: Der Standard: PEP 257 (Basis-Konventionen)

Titel: PEP 257: Die Basis-Konventionen

1. Einzeilige Docstrings (One-Liners)
Für offensichtliche Funktionen. Endet mit einem Punkt.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

(Aussage ist imperativ: "Return...", nicht "Returns...")

2. Mehrzeilige Docstrings
Für komplexe Funktionen.

```python
def complex_function(arg1, arg2):
    """Zusammenfassung in einem Satz (imperativ).

    Eine Leerzeile trennt die Zusammenfassung vom Detail.
    
    Hier folgt eine detailliertere Beschreibung der Logik,
    der Randbedingungen oder der Nutzungsszenarien.
    """
    pass
```

-----

## Folie 5: Fortgeschrittene Formate (Google & NumPy Style)

Titel: Fortgeschrittene Formate (Für Tools lesbar)

Damit Tools Argumente, Rückgabewerte und Fehler verstehen, hat sich ein Standard-Layout etabliert. Die zwei populärsten sind Google Style und NumPy Style.

Beispiel: Google Style (Sehr lesbar und weit verbreitet)

```python
from my_exceptions import ItemNotFoundError

def get_item(item_id: int, include_details: bool = False) -> dict:
    """Holt einen Artikel aus der Datenbank basierend auf seiner ID.

    Args:
        item_id (int): Die primäre ID des Artikels, der gesucht wird.
        include_details (bool, optional): 
            Wenn True, werden zusätzliche Details mitgeladen. 
            Defaults to False.

    Returns:
        dict: Ein Dictionary mit den Artikeldaten.

    Raises:
        ItemNotFoundError: Wenn keine Artikel mit der 'item_id' 
                            gefunden wurde.
    """
    if item_id == 404:
        raise ItemNotFoundError(f"Item {item_id} nicht gefunden.")
    
    data = {"id": item_id, "name": "Beispiel"}
    if include_details:
        data["details"] = "Weitere Infos..."
    return data
```

-----

## Folie 6: Zusammenfassung

Titel: Key Takeaways

  * API vs. Implementierung: Docstrings definieren die API (für den Nutzer), Kommentare erklären die Implementierung (für den Maintainer).
  * Metadaten: Docstrings sind über `func.__doc__` zur Laufzeit verfügbar.
  * Tooling (Evidence): Der primäre Wert liegt in der maschinellen Lesbarkeit durch IDEs (Tooltips) und Sphinx (Auto-Doku).
  * Format ist entscheidend: Nutzen Sie PEP 257 und ein Standardformat (z.B. Google Style oder NumPy Style), damit Tools die Argumente (`Args`), Rückgabewerte (`Returns`) und Fehler (`Raises`) parsen können.