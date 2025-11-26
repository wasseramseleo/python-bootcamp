Hier sind die Inhalte für die Slides zum Thema `uv`.

-----

## Folie 1: Titel

Titel: ⚡️ `uv`: Blazing Fast Python Tooling
Untertitel: Die all-in-one Toolchain (ersetzt `pip`, `venv`, `pip-tools` & mehr)

-----

## Folie 2: Das Problem: Python-Tooling (Fragmentierung)

Titel: Das Problem: Das "fragmentierte" Ökosystem

Vor `uv` brauchte man für ein Projekt ein Dutzend Tools:

  * Umgebung: `python -m venv` oder `virtualenv`
  * Installation: `pip`
  * Abhängigkeiten (statisch): `requirements.txt`
  * Locking (Reproduzierbarkeit): `pip-tools` (z.B. `pip-compile`)
  * Projekt-Metadaten: `setup.py` / `pyproject.toml`
  * Ausführung: `source .venv/bin/activate`

Kritik (Evidence): Dieser Prozess ist langsam (besonders Dependency Resolution), inkonsistent und verwirrend (zB. der Unterschied zwischen `requirements.txt` und `pyproject.toml` `dependencies`).

Die `uv`-Lösung: Ein einziges, extrem schnelles Binary (in Rust geschrieben), das all diese Aufgaben übernimmt.

-----

## Folie 3: 1. Konfigurations-Datei (`pyproject.toml`)

Titel: Konfiguration: `pyproject.toml` als "Single Source of Truth"

`uv` setzt (wie moderne Python-Tools) voll auf `pyproject.toml`.

Evidenz: `requirements.txt` wird nicht mehr für die *Definition* von Abhängigkeiten benötigt. Alles lebt in `pyproject.toml`.

```toml
# pyproject.toml

[project]
name = "my_app"
version = "0.1.0"
requires-python = ">=3.10"

# 1. Haupt-Abhängigkeiten (ersetzt requirements.txt)
dependencies = [
    "fastapi>=0.100.0",
    "sqlalchemy[asyncio]",
]

# 2. Optionale Abhängigkeiten (für dev, test, etc.)
[project.optional-dependencies]
test = [
    "pytest",
    "pytest-mock",
]
dev = [
    "mypy",
    "ruff",
]
```

-----

## Folie 4: 2. Dependency Management (Umgebungen)

Titel: Dependencies: Environments & Installation

1. Virtuelle Umgebung erstellen (ersetzt `python -m venv`)

```bash
# Erstellt ein .venv im aktuellen Verzeichnis
$ uv venv
```

2. Abhängigkeiten installieren (ersetzt `pip install -r`)
Der "Sync"-Befehl `uv pip sync` ist der Standard-Workflow. Er liest `pyproject.toml` und installiert die Abhängigkeiten.

```bash
# Installiert [project.dependencies]
$ uv pip sync

# Installiert Haupt- UND optionale 'test'-Dependencies
$ uv pip sync --extra test
```

3. Neue Pakete hinzufügen (ersetzt `poetry add` / `npm install`)
`uv` kann `pyproject.toml` für Sie bearbeiten (Experimentell, aber sehr nützlich):

```bash
# Installiert 'requests' UND fügt es zu [project.dependencies] hinzu
$ uv pip install requests
```

-----

## Folie 5: 3. Production Code (Reproduzierbarkeit & Locking)

Titel: Production: Locking für reproduzierbare Builds

Problem: `uv pip sync` installiert die *neuesten* Versionen, die `pyproject.toml` entsprechen. Für die Produktion brauchen wir exakt dieselben Versionen wie im Test (Reproducible Builds).

Lösung: "Locking" (ersetzt `pip-compile`)

Schritt 1: Lock-Datei generieren
`uv` liest `pyproject.toml` und löst alle Abhängigkeiten auf.

```bash
# Generiert eine 'requirements.lock' mit exakten Versionen
$ uv pip compile -o requirements.lock
```

Schritt 2: Aus Lock-Datei installieren
In der Produktion (z.B. im Dockerfile) wird nur die Lock-Datei verwendet.

```bash
# In Dockerfile:
COPY requirements.lock .

# Installiert NUR die exakten Versionen aus der Lock-Datei
# --production = Ignoriert 'dev'/'test'-Extras
$ uv pip sync --production -r requirements.lock
```

Evidenz: Dies ist 10-100x schneller als `pip-compile` und garantiert identische Umgebungen.

-----

## Folie 6: 4. Tests ausführen (`uv run`)

Titel: Tests ausführen mit `uv run`

Problem: Man muss `source .venv/bin/activate` aufrufen oder den Pfad (`.venv/bin/pytest`) kennen.

Lösung: `uv run`
`uv` führt Befehle *innerhalb* der verwalteten virtuellen Umgebung aus.

```bash
# 1. Sicherstellen, dass die Umgebung + Test-Extras installiert sind
$ uv pip sync --all-extras

# 2. Tests ausführen (ohne 'source activate')
$ uv run pytest

# 3. Linter ausführen
$ uv run ruff check .
$ uv run mypy src/
```

Evidenz: `uv run` vereinfacht CI-Pipelines (Continuous Integration) drastisch, da keine `activate`-Skripte benötigt werden.

-----

## Folie 7: 5. Build & Install (Das Paket bauen)

Titel: Build & Install (Lokale Pakete)

1. Das Paket "bauen" (ersetzt `python -m build`)
`uv` kann Ihr Projekt (definiert in `pyproject.toml`) in ein distributierbares Paket (Wheel) bauen.

```bash
# Liest pyproject.toml und erstellt das Paket
$ uv pip build

# Ergebnis:
# dist/my_app-0.1.0-py3-none-any.whl
```

2. Lokal "installieren" (ersetzt `pip install -e .`)
Um den Code im `src`-Ordner für die lokale Entwicklung verfügbar zu machen:

```bash
# Installiert das Projekt in der aktuellen Umgebung
# im "Editable"-Modus
$ uv pip install -e .
```

-----

## Folie 8: 6. Deployment-Workflow (Zusammenfassung)

Titel: Zusammenfassung: `uv` im Deployment-Workflow

Ein typischer CI/CD-Prozess mit `uv`:

1. Lokale Entwicklung:

  * `uv venv`
  * `uv pip install -e . --all-extras` (Editable-Installation)

2. CI-Pipeline (z.B. GitHub Actions)

  * `uv venv`
  * `uv pip sync --all-extras`
  * `uv run mypy`
  * `uv run pytest`

3. Build-Artefakt erstellen (optional, für PyPI)

  * `uv pip build`
  * `twine upload dist/*` (Hinweis: `twine` wird noch benötigt)

4. Deployment (z.B. Docker-Image)

  * `uv pip compile --production -o requirements.lock`
  * (Im Dockerfile): `uv pip sync --production -r requirements.lock`