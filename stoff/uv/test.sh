# Erstellt ein .venv im aktuellen Verzeichnis
$ uv venv

# Installiert [project.dependencies]
$ uv pip sync

# Installiert Haupt- UND optionale 'test'-Dependencies
$ uv pip sync --extra test

# Installiert 'requests' UND fügt es zu [project.dependencies] hinzu
$ uv pip install requests


# Generiert eine 'requirements.lock' mit exakten Versionen
$ uv pip compile -o requirements.lock


# Im Dockerfile:
COPY requirements.lock .

# Installiert NUR die exakten Versionen aus der Lock-Datei
# --production = Ignoriert 'dev'/'test'-Extras
$ uv pip sync --production -r requirements.lock


# 1. Sicherstellen, dass die Umgebung + Test-Extras installiert sind
$ uv pip sync --all-extras

# 2. Tests ausführen (ohne 'source activate')
$ uv run pytest

# 3. Linter ausführen
$ uv run ruff check .
$ uv run mypy src/


# Liest pyproject.toml und erstellt das Paket
$ uv pip build

# Ergebnis:
# dist/my_app-0.1.0-py3-none-any.whl

$ uv pip install -e .