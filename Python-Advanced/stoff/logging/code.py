import logging

# 1. Hole einen Logger, der nach dem Modul benannt ist
# (z.B. "my_package.utils")
log = logging.getLogger(__name__)

def do_something(data):
    # 2. Logge über die Instanz, nicht global
    log.info(f"Führe etwas aus mit {data}")
    if not data:
        log.warning("Keine Daten übergeben!")

# Falsch
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # PROBLEM: Man sieht nur die Nachricht, nicht WO der Fehler war.
    # Der Stack Trace fehlt!
    log.error(f"Ein Fehler ist aufgetreten: {e}")

# Richtig
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # 1. log.exception() (bevorzugt, da kürzer)
    # Loggt auf ERROR-Level und hängt automatisch den Stack Trace an
    log.exception("Divisions-Fehler bei der Berechnung.")

    # 2. Alternative (flexibleres Level)
    log.warning("Divisions-Fehler", exc_info=True)


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

