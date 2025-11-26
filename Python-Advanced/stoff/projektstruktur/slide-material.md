## Folie 1: Titel

Titel: 🏗️ Code-Struktur für große Projekte
Untertitel: Skalierbare, wartbare und testbare Python-Anwendungen bauen

-----

## Folie 2: Das Problem: Wenn "einfach" fehlschlägt

Titel: Das Problem: Wenn "einfache" Strukturen versagen

Für ein Skript oder eine kleine App mag das ausreichen:

```
my_project/
├── main.py
├── utils.py
├── models.py
├── test_main.py
└── requirements.txt
```

Kritik (Evidence-based): Bei 50+ Modulen führt dies zu Chaos:

  * Massiver Root-Ordner: Code, Tests, Konfiguration und Dokumentation liegen auf einer Ebene.
  * Import-Ambiguität: `import utils` – meinen wir das installierte Paket oder die lokale Datei?
  * "Gott"-Module: `utils.py` und `models.py` wachsen auf tausende Zeilen an und alles importiert von dort (Hohe Kopplung / High Coupling).
  * Zirkuläre Imports: Werden fast unvermeidlich, da alles miteinander verknüpft ist.

-----

## Folie 3: Lösung 1: Das `src`-Layout (Wiederholung)

Titel: Best Practice 1: Das `src`-Layout

Trennen Sie installierbaren Code (`src`) vom Rest des Projekts (Tests, Doku, Konfig).

```
my_project/
├── .venv/
├── .git/
├── pyproject.toml   # Projekt-Definition (Dependencies)
├── README.md
├── src/             # <- HIER lebt der Code
│   └── my_app/      # Das eigentliche Python-Package
│       ├── __init__.py
│       ├── main.py    # (z.B. der App-Einstiegspunkt)
│       ├── users/
│       └── payments/
├── tests/           # <- Tests sind klar getrennt
│   ├── test_users.py
│   └── test_payments.py
└── docs/
```

Vorteile (Evidenz):

1.  Löst Import-Probleme: `import my_app` funktioniert nur, wenn das Paket (aus `src`) "installierbar" ist (z.B. via `pip install -e .`).
2.  Sauberes Deployment: Build-Tools (wie `uv` oder `build`) wissen, dass sie nur `src/my_app` verpacken müssen, nicht die Tests.

-----

## Folie 4: Lösung 2: Modul-Struktur (Feature vs. Typ)

Titel: Best Practice 2: Struktur nach "Feature" (Domain)

Schlechte Struktur (nach Typ):
Führt zu hoher Kopplung. `views.py` muss `models.py` und `utils.py` importieren. Eine Änderung in `models.py` bricht potenziell alles.

```
src/my_app/
├── models.py    # (Alle 20 DB-Modelle)
├── views.py     # (Alle 50 API-Endpunkte)
├── serializers.py
└── utils.py
```

Gute Struktur (nach Feature / "Bounded Context"):
Jedes Feature ist ein eigenes Mini-Paket. Änderungen am "payment"-Modell beeinträchtigen das "user"-Modul nicht.

```
src/my_app/
├── __init__.py
├── core/            # (z.B. DB-Verbindung, Auth)
├── users/           # FEATURE 1
│   ├── __init__.py
│   ├── models.py    # (Nur User-Modelle)
│   ├── views.py     # (Nur User-Endpunkte)
│   └── services.py  # (Business-Logik)
└── payments/        # FEATURE 2
    ├── __init__.py
    ├── models.py
    ├── views.py
    └── services.py
```

Evidenz: Dies ist Low Coupling, High Cohesion (Lose Kopplung, Hoher Zusammenhalt). Es ist das Kernprinzip von Microservices, aber auf Modulebene angewendet.

-----

## Folie 5: Lösung 3: Konfigurations-Management

Titel: Best Practice 3: Konfiguration (Statisch vs. Dynamisch)

Problem: Wie verwaltet man DB-Passwörter, API-Keys und Settings (`DEBUG = True`)?
NIEMALS hartcodiert in `.py`-Dateien\! (Sicherheitsrisiko, unflexibel).

Lösung: Trennung der Konfiguration

1. Statische Konfiguration (Projekt-Definition): `pyproject.toml`

  * Was: Abhängigkeiten (`dependencies`), Projekt-Name, Build-Tools.
  * Wer: Wird vom *Entwickler* definiert und in Git eingecheckt.

2. Dynamische Konfiguration (Environment-Variablen)

  * Was: Secrets (API-Keys, DB-Passwörter), Host-Namen, `DEBUG`-Flag.
  * Wer: Wird von der *Umgebung* (Server, Docker, Entwickler-Maschine) bereitgestellt.

Workflow (Evidenz):

1.  Entwickler speichern lokale Secrets in einer `.env`-Datei (z.B. `DB_PASS="secret"`).
2.  Diese `.env`-Datei ist IMMER in der `.gitignore`\!
3.  Die App lädt diese Variablen zur Laufzeit (z.B. mit `python-dotenv` oder `pydantic-settings`).

<!-- end list -->

```python
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Liest automatisch aus Environment-Variablen (oder .env)
    db_url: str
    debug_mode: bool = False

# App lädt Settings *nur* aus der Umgebung
settings = Settings()
db = connect(settings.db_url)
```

-----

## Folie 6: Lösung 4: Das "Circular Import"-Problem lösen

Titel: Lösung 4: Zirkuläre Imports (Problem & Lösung)

Problem (Erinnerung):

  * `users/services.py` braucht Infos aus `payments` -\> `from ..payments import services`
  * `payments/services.py` muss den User prüfen -\> `from ..users import services`
  * Ergebnis: `ImportError` (Circular Dependency)

Evidenz: Dieses Problem ist ein Symptom für schlechtes Design. Es bedeutet, dass zwei Module zu viel voneinander wissen.

Lösung 1 (Refactoring):

  * Gemeinsame Abhängigkeiten in ein "neutrales" Modul auslagern (z.B. `core/models.py`).

Lösung 2 (Fortgeschritten): Dependency Inversion

  * Module dürfen nicht voneinander abhängen, sondern von Abstraktionen.
  * Anstatt dass `A` `B` importiert, "injiziert" (`inject`) die Hauptanwendung (`main.py`) eine Instanz von `B` in `A`.

<!-- end list -->

```python
# A (users) hängt NICHT mehr von B (payments) ab
class UserService:
    def __init__(self, payment_service_interface):
        # 'A' kennt nur die Abstraktion, nicht die Implementierung
        self.payments = payment_service_interface 

# main.py (baut die App zusammen)
from users.services import UserService
from payments.services import StripePaymentService

# Dependency Injection:
payment_service = StripePaymentService()
user_service = UserService(payment_service_interface=payment_service)
```

-----

## Folie 7: Zusammenfassung

Titel: Key Takeaways

  * Skalierung scheitert an Kopplung: Große Projekte werden langsam und fehleranfällig, wenn alles miteinander verknüpft ist.
  * `src`-Layout: Trennt installierbaren Code (`src`) sauber von Tests und Konfiguration.
  * Struktur nach Feature (Domain): (z.B. `users/`, `payments/`) statt nach Typ (`models.py`, `views.py`). Fördert "Low Coupling".
  * Konfiguration (Evidenz): Trennen Sie statische Konfig (`pyproject.toml`) von dynamischer/geheimer Konfig (Environment-Variablen).
  * Circular Imports: Sind ein Design-Fehler. Lösen durch Refactoring oder Dependency Inversion (Abstraktionen).