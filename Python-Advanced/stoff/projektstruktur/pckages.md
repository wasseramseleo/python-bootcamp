Hier sind die Inhalte für die Slides zum Thema Packages.

-----

## Folie 1: Titel

**Titel:** Python Packages & Projektstruktur
**Untertitel:** Skalierbare Projekte bauen und veröffentlichen

-----

## Folie 2: Vom Modul zum Package

**Titel:** Vom Modul zum Package

**1. Das Modul (Module)**
Ein Modul ist einfach eine Python-Datei (`.py`).

```
project/
  main.py
  utils.py
```

```python
# main.py
import utils
utils.do_something()
```

**2. Das Problem (Skalierung)**
Was passiert, wenn `utils.py` 10.000 Zeilen lang wird oder wir 50 verschiedene Util-Dateien brauchen? Die Struktur geht verloren.

**3. Das Package (Paket)**
Ein Package ist ein **Ordner**, der (mindestens) eine `__init__.py`-Datei enthält.

```
project/
  main.py
  my_package/
      __init__.py
      utils.py
      database.py
```

```python
# main.py
from my_package import utils
from my_package.database import connect_db

utils.do_something()
```

-----

## Folie 3: Die Rolle von `__init__.py` (Das Tor zum Paket)

**Titel:** Die Rolle von `__init__.py`

Diese Datei wird **automatisch ausgeführt**, wenn das Package importiert wird.

**Historisch (Python 2):** Zwingend erforderlich, um einen Ordner als Package zu markieren.
**Modern (Python 3.3+):** Technisch optional ("Namespace Packages").

**ABER (Best Practice für große Projekte):** Verwenden Sie es **immer**.

**Zweck 1: Die "Öffentliche API" definieren (Abstraktion)**
Sie können Funktionen aus internen Modulen "nach oben" holen, um dem Nutzer eine saubere Schnittstelle zu geben.

```python
# in my_package/utils.py
def _internal_helper(): # Führt "_" -> Intern
    pass
def public_function(): # Öffentlich
    pass
```

```python
# in my_package/__init__.py
from .utils import public_function
# _internal_helper wird NICHT importiert

# Der Nutzer importiert jetzt sauber:
from my_package import public_function
# (Er muss 'utils.py' gar nicht kennen!)
```

**Zweck 2:** Initialisierungs-Code (z.B. Logging-Setup).

-----

## Folie 4: Absolute vs. Relative Imports

**Titel:** Absolute vs. Relative Imports

**Absolute Imports (Bevorzugt in Anwendungscode)**
Immer vom "Root" des Projekts (dem Verzeichnis, das Python "sieht").

```python
# in main.py
from my_package.utils import helper
```

  * **Pro:** Eindeutig, immer klar, woher der Code kommt.
  * **Con:** Schwerer zu ändern (wenn `my_package` umbenannt wird).

**Relative Imports (Bevorzugt *innerhalb* eines Packages)**
Relativ zur aktuellen Datei.

```python
# in my_package/database.py
# (braucht eine Funktion aus my_package/utils.py)

# "." bedeutet: aus dem aktuellen Verzeichnis
from .utils import helper 

# ".." bedeutet: ein Verzeichnis nach oben
from ..other_package import foo 
```

  * **Pro:** Macht das Package selbst-enthalten und leicht verschiebbar.

**Best Practice (Evidence):**

  * **Applikation** (`main.py`): Absolute Imports.
  * **Package-Intern:** Relative Imports.

-----

## Folie 5: Best Practice (Großprojekte): Das `src`-Layout

**Titel:** Projektstruktur: Das `src`-Layout

**Problem:** Wenn `my_package` im Root-Ordner liegt, ist oft unklar, ob es als "installiertes" Paket oder als "lokaler Ordner" importiert wird. Dies führt zu Import-Fehlern (`ImportError`), sobald das Projekt installiert wird.

**Lösung (Evidence-based):** Trennen Sie den installierbaren Code (`src`) vom Rest (Tests, Doku, Configs).

```
my_app/
├── pyproject.toml   # Projekt-Definition (siehe Folie 7)
├── README.md
├── .venv/
├── src/             # Der "Source"-Ordner
│   └── my_package/  # DAS ist der Paket-Code
│       ├── __init__.py
│       └── utils.py
└── tests/           # Tests sind KLAR getrennt
    └── test_utils.py
```

**Vorteile:**

1.  **Keine Import-Ambiguität:** `import my_package` funktioniert garantiert nur, wenn das Paket (im `src`-Ordner) korrekt installiert/gefunden wird.
2.  **Saubere Installation:** Build-Tools wissen, dass nur der Inhalt von `src` in das finale Paket gehört (nicht die Tests).

-----

## Folie 6: Das Alptraum-Problem: Circular Imports

**Titel:** Alptraum-Szenario: Circular Imports (Zirkelbezüge)

Dies ist das häufigste Skalierungs-Problem in großen Python-Projekten.

**Problem:**

1.  Datei `a.py` importiert etwas aus `b.py`.
2.  Datei `b.py` importiert etwas aus `a.py`.

<!-- end list -->

```python
# a.py
from b import func_b # <-- 2. Python lädt b.py

def func_a():
    return "Hello from A"

# b.py
from a import func_a # <-- 3. Python lädt a.py (erneut)

def func_b():
    return "Hello from B"
```

**Ergebnis (Evidence):**
`ImportError: cannot import name 'func_a' from partially initialized module 'a'`

Python lädt `a`, pausiert `a`, um `b` zu laden. `b` versucht, `a` zu laden, aber `a` ist noch nicht fertig initialisiert (`func_a` existiert noch nicht).

**Lösungen:**

1.  **Refactoring (Beste Lösung):** Die gemeinsame Abhängigkeit in eine dritte Datei (`c.py`) auslagern.
2.  **Lazy Import (Workaround):** Import *innerhalb* der Funktion, nicht auf Modulebene.

-----

## Folie 7: Projekt-Definition: `pyproject.toml`

**Titel:** Projekt-Definition: `pyproject.toml`

**WICHTIG:** `setup.py` und `requirements.txt` sind veraltet (Legacy).
**`pyproject.toml` (PEP 518/621)** ist der neue, einheitliche Standard.

Diese Datei definiert *alles*: Metadaten, Abhängigkeiten (Dependencies) und Build-Tools.

```toml
# pyproject.toml

[build-system]
# Sagt Tools (pip, uv), WIE das Paket gebaut wird
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
# Metadaten des Projekts
name = "my_package"
version = "0.1.0"
authors = [{ name = "A. Neumann", email = "a@mail.com" }]
description = "Ein Beispiel-Paket."

# Abhängigkeiten (ersetzt requirements.txt)
dependencies = [
    "requests>=2.0",
    "sqlalchemy",
]
```

-----

## Folie 8: Veröffentlichen (mit `uv` im Workflow)

**Titel:** Publishing-Workflow (mit `uv` & `twine`)

`uv` (von Astral) ist ein extrem schneller Ersatz für `pip`, `venv` und `pip-tools`.
(Stand 2025: `uv` selbst veröffentlicht (published) *noch* nicht, aber verwaltet die Umgebung dafür.)

**Workflow (Kurzfassung):**

**Schritt 1: Virtuelle Umgebung (mit `uv`)**
Erstellt eine isolierte Umgebung (ersetzt `python -m venv`).

```bash
$ uv venv
# ... .venv wird erstellt (extrem schnell)
```

**Schritt 2: Build-Tools installieren (mit `uv`)**
Wir brauchen `build` (zum Bauen) und `twine` (zum Hochladen).

```bash
$ uv pip install build twine
```

**Schritt 3: Paket bauen (mit `build`)**
Liest `pyproject.toml` und erstellt das Paket.

```bash
$ python -m build
# Erzeugt .whl und .tar.gz im 'dist/'-Ordner
```

**Schritt 4: Veröffentlichen (mit `twine`)**
Lädt die gebauten Dateien zu PyPI (Python Package Index).

```bash
$ twine upload dist/*
# (Fragt nach PyPI-Benutzername/Passwort oder API-Token)
```

**Kernaussage:** `uv` macht die Umgebungs-Verwaltung (Schritt 1 & 2) drastisch schneller und einfacher.