## Folie 2: Das Problem: Datenpersistenz

**Titel:** Warum brauchen wir Datenbanken?

**Das Problem:**
Variablen (Listen, Dictionaries) existieren nur im RAM (Arbeitsspeicher). Wenn das Skript endet, sind die Daten **verloren**.

  * **Ansatz 1: Dateien (JSON, CSV):**

      * Einfach zu schreiben, ABER:
      * Sehr schwer, Daten *selektiv* zu lesen (z.B. "Finde alle User aus Berlin, die älter als 30 sind").
      * Nicht "Thread-Safe" (Probleme bei gleichzeitigem Zugriff).

  * **Ansatz 2: Datenbanken (DBs):**

      * Speziell für das Speichern, Abfragen und Verwalten von Daten konzipiert.

**Warum `SQLite`?**

  * **In Python integriert:** `import sqlite3` (keine Installation nötig).
  * **Serverlos:** Die gesamte Datenbank ist nur **eine einzige Datei** (z.B. `meine_app.db`).
  * **Ideal für:** Lokale Anwendungen, Prototyping, Caching, Tests.

-----

## Folie 3: Ansatz 1: Rohes SQL (Das `sqlite3`-Modul)

**Titel:** Ansatz 1: Rohes SQL mit `sqlite3`

Dies ist der "Low-Level"-Ansatz. Wir schreiben SQL-Befehle als Strings.

```python
import sqlite3

# 1. Verbinden (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# 2. SQL ausführen (Schema definieren)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT
    )
""")

# 3. WICHTIG: Parameterisierung (Schutz vor SQL-Injection!)
# NIEMALS f-strings für Werte verwenden!
user_name = "Alice"
cursor.execute("INSERT INTO users (name) VALUES (?)", (user_name,))

# 4. Transaktion abschließen
conn.commit()

# 5. Daten abfragen
for row in cursor.execute("SELECT id, name FROM users"):
    print(row) # Output: (1, 'Alice')

conn.close()
```

-----

## Folie 4: Kritik an Rohem SQL (Das "Impedance Mismatch")

**Titel:** Kritik an Rohem SQL

**Das Problem (Evidence):** Python denkt in **Objekten** (`class User`), relationale Datenbanken denken in **Tabellen/Reihen**. Dies nennt man das "Object-Relational Impedance Mismatch".

**Beispiel: Manuelle Konvertierung**

```python
# Wir haben eine Klasse
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# SQL gibt uns ein Tupel
cursor.execute("SELECT id, name FROM users WHERE id = 1")
row = cursor.fetchone() # -> (1, 'Alice')

# Manuelle Konvertierung (Boilerplate-Code)
if row:
    user_obj = User(id=row[0], name=row[1])
```

**Nachteile (Evidence-based):**

  * **Viel Boilerplate:** Manuelle Konvertierung von Tupeln zu Objekten (und umgekehrt).
  * **"Stringly-Typed":** SQL-Befehle sind nur Strings. Die IDE kann sie nicht prüfen (Tippfehler\!).
  * **Wartungsalptraum:** Ändert sich das Schema (neue Spalte), muss man *jeden* SQL-String im Code finden und anpassen.
  * **Sicherheitsrisiko:** Man muss **manuell** an den Schutz vor SQL-Injection (via `?`) denken.

-----

## Folie 5: Ansatz 2: Der Object-Relational Mapper (ORM)

**Titel:** Ansatz 2: Der Object-Relational Mapper (ORM)

**Konzept:** Ein ORM ist eine Abstraktionsschicht (ein Übersetzer), die dieses "Mismatch"-Problem löst.

Ein ORM "mappt" (verbindet) zwei Welten:

| Python-Welt (Objekte) | Datenbank-Welt (Relational) |
| :--- | :--- |
| `class User` | `TABLE users` |
| `user_obj = User(name="Bob")` | `ROW (2, 'Bob')` |
| `user_obj.name` | `COLUMN name` |

**Populärste Bibliothek:** **SQLAlchemy** (Der De-facto-Standard in Python).

**Vorteil:** Wir schreiben (fast) kein SQL mehr. Wir interagieren nur noch mit Python-Objekten und -Methoden.

-----

## Folie 6: ORM-Beispiel (SQLAlchemy)

**Titel:** Beispiel: SQLAlchemy (Moderner Stil 2.0)

**1. Definition (Die "Models" / Das Schema)**

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

# Die Klasse IST die Tabelle
class User(Base):
    __tablename__ = "users"
    
    # Die Attribute SIND die Spalten (mit Type Annotations)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str | None] # Optional[str] (Py 3.10+)
```

**2. Nutzung (Die "Session" / Abfragen)**

```python
# (Engine- und Session-Setup... wird vom ORM erledigt)

# --- INSERT ---
new_user = User(name="Bob", email="bob@mail.com")
session.add(new_user)

# --- SELECT ---
# Kein SQL! Nur Python-Objekte und Methoden.
# IDE kann dies automatisch vervollständigen!
user = session.query(User).filter_by(name="Bob").first()

if user:
    print(f"Gefunden: {user.name} (ID: {user.id})")

session.commit()
```

-----

## Folie 7: Kritischer Vergleich: Raw SQL vs. ORM

**Titel:** Kritischer Vergleich: Raw SQL vs. ORM

| Feature         | Raw SQL (`sqlite3`)                                                        | ORM (`SQLAlchemy`)                                             |
|:----------------|:---------------------------------------------------------------------------|:---------------------------------------------------------------|
| **Kontrolle**   | **Maximal.** 100% Kontrolle über das SQL.                                  | **Abstrahiert.** Man vertraut dem ORM (meistens gut).          |
| **Performance** | **Potenziell am schnellsten** (für SQL-Experten).                          | **Sehr gut.** Minimaler Overhead, oft vernachlässigbar.        |
| **Entwicklung** | Langsam. Viel Boilerplate-Code (Konvertierung).                            | **Extrem schnell.** Fokus auf Business-Logik.                  |
| **Wartbarkeit** | **Schwer.** Schema-Änderungen erfordern Suchen & Ersetzen von SQL-Strings. | **Einfach.** Modell (`class`) ändern, ORM generiert neues SQL. |
| **Sicherheit**  | Manuell. **Hohes Risiko** für SQL-Injection bei Fehlern.                   | **Hoch.** Parameterisierung ist standardmäßig eingebaut.       |
| **DB-Wechsel**  | **Unmöglich.** SQL ist an Dialekt (SQLite) gebunden.                       | **Einfach.** (z.B. von SQLite zu PostgreSQL wechseln).         |

-----

## Folie 8: Zusammenfassung

**Titel:** Key Takeaways

  * **`sqlite3`:** Perfekt für lokale Daten, Tests, Prototyping. Serverlos, in Python integriert.
  * **Raw SQL (Ansatz 1):** Bietet totale Kontrolle, ist aber fehleranfällig (**SQL-Injection**) und schwer wartbar (das "Impedance Mismatch"-Problem).
  * **ORM (Ansatz 2):** Löst das Mismatch-Problem durch Abstraktion (`class` -\> `TABLE`).
  * **Kritische Entscheidung (Evidence):** ORMs (wie SQLAlchemy) tauschen einen kleinen Performance-Overhead gegen enorme Gewinne bei **Entwicklungsgeschwindigkeit**, **Wartbarkeit** und **Sicherheit** (Schutz vor Injection).