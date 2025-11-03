### 1. SQLite (Die Basis)

* **Zweck:** Eine serverlose, in Python integrierte (`import sqlite3`) Datenbank.
* **Konzept:** Die gesamte Datenbank ist nur **eine einzige Datei** (z.B. `app.db`).
* **Einsatz:** Ideal für lokale Anwendungen, Prototyping und Tests.

### 2. Ansatz 1: Rohes SQL (mit `sqlite3`)

* **Zweck:** Der Low-Level-Ansatz, bei dem SQL-Befehle manuell als Strings geschrieben werden.
* **Workflow:** `connect` -> `cursor` -> `execute` -> `commit` / `fetchone` -> `close`.
* **Kritischer Punkt 1 (für Übungen): SQL-Injection.**
    * Übungen müssen den **korrekten** Einsatz von Parameterisierung (`?`-Platzhalter) testen.
    * `cursor.execute("INSERT ... VALUES (?)", (var,))`
    * Und den **falschen** (gefährlichen) Einsatz von f-Strings für Werte ablehnen.
* **Kritischer Punkt 2 (für Übungen): "Object-Relational Impedance Mismatch" (ORIM).**
    * Python denkt in **Objekten** (`class User`), SQL liefert **Tupel/Reihen** (`(1, 'Alice')`).
    * Übungen sollten diesen "Mismatch" aufzeigen, indem sie die manuelle, fehleranfällige Konvertierung (Boilerplate-Code) von Tupeln in Klasseninstanzen erfordern.

### 3. Ansatz 2: ORM (Object-Relational Mapper)

* **Zweck:** Eine Abstraktionsschicht (ein "Übersetzer"), die das ORIM-Problem löst.
* **Bibliothek:** **SQLAlchemy** (der De-facto-Standard).
* **Kernkonzept (für Übungen): Das "Mapping".**
    * Eine Python-**Klasse** (`class User`) wird auf eine SQL-**Tabelle** (`TABLE users`) gemappt.
    * Ein Klassen-**Attribut** (`user.name`) wird auf eine Tabellen-**Spalte** (`COLUMN name`) gemappt.
    * Ein **Objekt** (`user_obj`) repräsentiert eine **Reihe** (Row).
* **Vorteile (für Übungen zu demonstrieren):**
    * **Kein SQL mehr:** Man schreibt Python-Methoden (`session.query(User).filter_by(...)`).
    * **Wartbarkeit:** Das Schema wird nur in der Python-Klasse definiert.
    * **Sicherheit:** ORMs verhindern SQL-Injection automatisch (eingebaut).
    * **Datenbank-Abstraktion:** Der Code ist (fast) identisch, egal ob SQLite oder PostgreSQL verwendet wird.