Hier sind die Inhalte für die Slides zum Thema Logging.

-----

## Folie 1: Titel

**Titel:** Logging in Python
**Untertitel:** Professionelles Logging für Diagnose und Skalierbarkeit

-----

## Folie 2: Das Problem: Warum `print()` in der Produktion versagt

**Titel:** Das Problem: Warum `print()` versagt

`print()` ist das Werkzeug der Wahl für das Debugging... im Entwicklungs-Modus.

**Kritik (Evidence-based):** In einer Produktionsumgebung (z.B. einem Webserver, einer Datenpipeline) scheitert `print()`:

  * **Keine Kontrolle:** Man kann nicht "nur Fehler" anzeigen (`print` ist "all or nothing").
  * **Kein Kontext:** Woher kam die Nachricht? (Zeit, Modul, Prozess-ID).
  * **Kein Ziel:** `print` geht nach `stdout`. Was, wenn der Service als Hintergrund-Daemon läuft? Die Nachrichten gehen ins Leere (`/dev/null`).
  * **Performance:** `print` ist blockierend (I/O) und kann in Schleifen die Anwendung massiv verlangsamen.

**Lösung:** Das `logging`-Modul. Es trennt die *Erzeugung* einer Nachricht von ihrer *Verarbeitung*.

-----

## Folie 3: Basics Recap 1: Die Log Levels

**Titel:** Basics: Log Levels (Die Dringlichkeit)

Levels erlauben es, die Ausführlichkeit (Verbosity) zur Laufzeit zu steuern, **ohne den Code zu ändern**.

| Level | `logging`-Funktion | Nutzung (Wann?) |
| :--- | :--- | :--- |
| **DEBUG** | `logging.debug()` | Detaillierte Infos, nur zur Diagnose (z.B. Variablen-Werte). |
| **INFO** | `logging.info()` | Bestätigung, dass Dinge wie erwartet laufen (z.B. "Service gestartet"). |
| **WARNING** | `logging.warning()` | Etwas Unerwartetes, aber die App läuft weiter (z.B. "Cache nicht gefunden"). |
| **ERROR** | `logging.error()` | Ein ernstes Problem; die Funktion konnte nicht ausgeführt werden. |
| **CRITICAL** | `logging.critical()` | Ein fataler Fehler; die gesamte Anwendung muss ggf. stoppen. |

**Kritische Evidenz:** Der Logger wird auf ein Level (z.B. `INFO`) gesetzt. Alle Nachrichten *darunter* (z.B. `DEBUG`) werden ignoriert und verursachen **keinen Performance-Overhead**.

-----

## Folie 4: Basics Recap 2: `basicConfig` (Der Schnellstart)

**Titel:** Basics: `logging.basicConfig()`

Für kleine Skripte ist `basicConfig` der schnellste Weg, das Logging zu aktivieren.

**WICHTIG:** `basicConfig` funktioniert **nur einmal**. Es konfiguriert den "Root"-Logger.

```python
import logging

# Konfiguration muss VOR dem ersten logging-Aufruf erfolgen!
logging.basicConfig(
    level=logging.DEBUG, # Ab welchem Level anzeigen?
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log" # Optional: in eine Datei loggen
)

logging.debug("Detail-Info")
logging.info("Service gestartet")
logging.warning("Passwort ist schwach")
```

**Output (in `app.log`):**

```
2025-11-03 21:50:15,123 - DEBUG - Detail-Info
2025-11-03 21:50:15,123 - INFO - Service gestartet
2025-11-03 21:50:15,124 - WARNING - Passwort ist schwach
```

-----

## Folie 5: Problem: `basicConfig` in Großprojekten (Don't\!)

**Titel:** Problem: `basicConfig` in Großprojekten

`basicConfig` ist eine **globale** Konfiguration (Singleton).

**Problem (Evidence):**
Stellen Sie sich ein großes Projekt mit 50 Modulen (Libraries) vor.

  * Modul `A` (z.B. `requests`) will loggen.
  * Modul `B` (Ihre App) will loggen.

Wenn *irgendein* Modul (auch `requests`) `logging.warning()` aufruft, *bevor* Sie `basicConfig` konfiguriert haben, wird die Default-Konfiguration "eingerastet".

**Ihr `basicConfig`-Aufruf wird danach ignoriert.**

**Kritische Folgerung:** Libraries (Module) dürfen **niemals** `basicConfig` aufrufen. Nur die **Applikation** (der Haupteinstiegspunkt, `main.py`) darf das Logging *einmal* konfigurieren.

-----

## Folie 6: Best Practice 1: `getLogger(__name__)`

**Titel:** Best Practice 1: `getLogger(__name__)`

**Regel:** Verwenden Sie **niemals** die Root-Funktionen (wie `logging.warning(...)`) direkt in Modulen. Holen Sie sich immer einen **modul-spezifischen Logger**.

Der Python-Standard dafür ist `__name__`.

```python
# In my_package/utils.py
import logging

# 1. Hole einen Logger, der nach dem Modul benannt ist
# (z.B. "my_package.utils")
log = logging.getLogger(__name__)

def do_something(data):
    # 2. Logge über die Instanz, nicht global
    log.info(f"Führe etwas aus mit {data}")
    if not data:
        log.warning("Keine Daten übergeben!")
```

**Vorteile (Evidence):**

  * **Granularität:** Sie können `my_package.utils` auf `DEBUG` setzen, während der Rest der App auf `INFO` bleibt.
  * **Kontext:** Der Logger-Name (`%(name)s`) im Log-Format zeigt, woher die Nachricht kam.

-----

## Folie 7: Best Practice 2: Exceptions loggen (mit `exc_info`)

**Titel:** Best Practice 2: Exceptions korrekt loggen

Ein häufiger Fehler ist das manuelle Loggen von Exceptions.

**FALSCH (Kritischer Fehler):**

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # PROBLEM: Man sieht nur die Nachricht, nicht WO der Fehler war.
    # Der Stack Trace fehlt!
    log.error(f"Ein Fehler ist aufgetreten: {e}")
```

**RICHTIG (Evidence-based):**
Verwenden Sie `logging.exception()` oder `exc_info=True`.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # 1. log.exception() (bevorzugt, da kürzer)
    # Loggt auf ERROR-Level und hängt automatisch den Stack Trace an
    log.exception("Divisions-Fehler bei der Berechnung.")

    # 2. Alternative (flexibleres Level)
    log.warning("Divisions-Fehler", exc_info=True)
```

**Nutzen:** Nur so sehen Sie im Log *exakt*, in welcher Zeile (`10 / 0`) der Fehler auftrat.

-----

## Folie 8: Best Practice 3: Konfiguration (App vs. Library)

**Titel:** Best Practice 3: App konfiguriert, Library loggt

Die Trennung von Verantwortung ist entscheidend für skalierbare Projekte.

  * **Die Library / Das Modul (z.B. `payment.py`)**

      * Kennt nur seinen Logger (`log = getLogger(__name__)`).
      * Ruft `log.info()`, `log.warning()` etc. auf.
      * **Weiß nichts** über Handler, Formate oder Level. (Sollte eine `NullHandler` setzen, um Warnungen zu vermeiden, wenn die App nicht konfiguriert).

  * **Die Applikation (z.B. `main.py` oder `server.py`)**

      * Ruft **keine** `log.info()`-Befehle auf (außer im eigenen Modul).
      * **Definiert** das Setup: Sollen Logs in eine Datei? Zur Konsole? Im JSON-Format? Welches Level (`INFO` oder `DEBUG`)?

-----

## Folie 9: Best Practice 4: `dictConfig` (Die robuste Konfiguration)

**Titel:** Best Practice 4: `logging.config.dictConfig()`

`basicConfig` ist zu simpel. Für reale Anwendungen (z.B. Webserver) brauchen Sie mehr Kontrolle.

**Konzept:** Sie definieren das Setup als Python-Dictionary.

  * **Formatters:** Wie sieht die Nachricht aus (z.B. mit Zeitstempel, Modulname).
  * **Handlers:** Wohin geht die Nachricht (z.B. `console`, `file`, `sentry`, `syslog`).
  * **Loggers:** Welcher Logger (z.B. `my_package.utils`) nutzt welchen Handler und welches Level.

<!-- end list -->

```python
# In main.py (stark vereinfacht)
from logging.config import dictConfig

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': { # Ein Handler namens 'console'
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        'my_package': { # Alle Logger in 'my_package'
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'requests': { # Logger von Drittanbietern
            'level': 'WARNING', # (requests soll "leise" sein)
            'handlers': ['console'],
        },
    },
}

dictConfig(LOGGING_CONFIG) # Einmal anwenden
```

-----

## Folie 10: Best Practice 5: Structured Logging (JSON)

**Titel:** Best Practice 5: Structured Logging (JSON)

**Problem:** Traditionelle Logs sind Text – für Menschen lesbar, für Maschinen schwer zu parsen.
`2025-11-03 21:55:00 - app.users - ERROR - User 123 login failed`

**Kritik (Evidence):** In großen Systemen (Microservices, Kubernetes) werden Logs nicht mehr manuell per `grep` durchsucht. Sie werden an zentrale Systeme (ELK Stack, Datadog, Splunk) gesendet. Diese Systeme brauchen strukturierte Daten.

**Lösung: Structured Logging (z.B. JSON)**
Anstatt eines Strings wird ein JSON-Objekt geloggt.

```python
# Verwendung einer Library wie 'python-json-logger'
import logging
from pythonjsonlogger import jsonlogger

# ... (Handler konfigurieren, um jsonlogger.JsonFormatter zu nutzen) ...

# Code
log = logging.getLogger("app.users")
log.error("Login fehlgeschlagen", extra={
    "user_id": 123,
    "login_attempt": 5,
    "ip_address": "192.168.1.10"
})
```

**Output (Maschinenlesbar):**

```json
{
  "timestamp": "2025-11-03...",
  "level": "ERROR",
  "name": "app.users",
  "message": "Login fehlgeschlagen",
  "user_id": 123,
  "login_attempt": 5,
  "ip_address": "192.168.1.10"
}
```

**Vorteil:** Ermöglicht komplexes Filtern im Log-System (z.B. "Zeige alle Errors für user\_id 123").