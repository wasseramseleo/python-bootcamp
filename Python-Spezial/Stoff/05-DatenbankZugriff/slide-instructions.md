**Input Data:**

* **Topic Title:** 5. Datenbankzugriff
* **Content Points:**
    - SQLAlchemy Basics
    - Connection Strings
    - SQL-Queries ausführen
* **Lab Objectives:**
    * Verbindung zu einer DB herstellen und ein einfaches SELECT Statement ausführen. (Sqlite)
    * Advanced: ORM-Konzepte verstehen, sichere parametrisierte Queries schreiben und Bulk-Inserts durchführen.

-----

Here are the slides for **Topic 5: Datenbankzugriff**, focusing on SQLAlchemy within the Bird Ringing context.

-----

**Slide 1: SQLAlchemy Übersicht**

**Body Text (German):**

  * **Der Standard:** SQLAlchemy ist das meistgenutzte SQL Toolkit für Python. Es abstrahiert die Unterschiede zwischen verschiedenen Datenbanken (PostgreSQL, MySQL, SQLite, Oracle).
  * **Architektur:**
      * **Core:** Erlaubt das Senden von reinem SQL (nah an der Datenbank).
      * **ORM (Object Relational Mapper):** Mapped Python-Klassen auf Datenbank-Tabellen (nah am objektorientierten Code).
  * **Engine:** Der zentrale Einstiegspunkt, der den Dialekt verwaltet und den Connection Pool bereitstellt.

**Code Snippet (Python):**

```python
from sqlalchemy import create_engine

# The Engine is the starting point for any SQLAlchemy application
# It's a "home base" for the actual database connections
engine = create_engine("sqlite:///bird_ringing.db")
```

**Speaker Notes (German):**
Wir verlassen nun die lokalen Dateien und gehen zu Datenbanken über. SQLAlchemy ist hier der Industriestandard. Es besteht aus zwei Teilen: Dem "Core" (für direktes SQL) und dem "ORM" (für fortgeschrittene Objekt-Modellierung). Die `Engine` ist unser Motor: Wir konfigurieren sie einmal und sie kümmert sich im Hintergrund um Verbindungsdetails und Pooling.

**Image Prompt:** A layered architecture diagram showing "Python Code" on top, "SQLAlchemy ORM/Core" in the middle acting as a translator, and various Database icons (Postgres, SQLite, MySQL) at the bottom.

-----

**Slide 2: Connection Strings & Verbindungsaufbau**

**Body Text (German):**

  * **URL Schema:** Verbindungsdaten folgen immer dem Muster: `dialect+driver://username:password@host:port/database`.
  * **SQLite:** Eine serverlose Datei-basierte Datenbank. Ideal für Entwicklung und lokale Analysen. Connection String: `sqlite:///dateiname.db`.
  * **Connection Management:** Verbindungen werden aus der Engine bezogen. Nutzen Sie auch hier Context Manager (`with`), um Verbindungen sauber zu schließen.

**Code Snippet (Python):**

```python
# Connection String Examples:
# PostgreSQL: postgresql+psycopg2://scott:tiger@localhost/mydatabase
# SQLite (Relative path): sqlite:///field_data.db

from sqlalchemy import create_engine

engine = create_engine("sqlite:///field_data.db")

# Establish a connection
with engine.connect() as connection:
    print("Connection established successfully.")
```

**Speaker Notes (German):**
Um mit der DB zu sprechen, brauchen wir eine Adresse. Das ist der "Connection String". Im Lab nutzen wir SQLite, da es keine Installation erfordert – die Datenbank ist einfach eine Datei auf Ihrer Festplatte. Im Enterprise-Umfeld tauschen Sie später einfach diesen String gegen eine PostgreSQL-Adresse aus, ohne Ihren restlichen Code ändern zu müssen.

**Image Prompt:** A visual breakdown of a URL string, labelling the parts: "Protocol" (sqlite), "User/Pass", "Host", and "Database Name", similar to dissecting a biological taxonomy.

-----

**Slide 3: SQL Queries ausführen (Core)**

**Body Text (German):**

  * **Raw SQL:** Mit der `text()` Funktion können Sie klassische SQL-Statements schreiben.
  * **Execution:** `connection.execute()` sendet den Befehl an die DB.
  * **Result Proxy:** Das Ergebnis ist ein Iterator. Man kann darüber loopen oder via `.fetchall()` alle Zeilen laden.
  * **Tuple-Access:** Jede Zeile verhält sich wie ein Tuple (Zugriff per Index) oder wie ein Mapping (Zugriff per Spaltenname).

**Code Snippet (Python):**

```python
from sqlalchemy import text

query_str = "SELECT species, wing_length FROM captures WHERE wing_length > 70"

with engine.connect() as conn:
    # Execute raw SQL
    result = conn.execute(text(query_str))
    
    for row in result:
        # Access by column name
        print(f"Species: {row.species}, Wing: {row.wing_length}")
```

**Speaker Notes (German):**
Hier sehen wir den "Core"-Ansatz. Wir schreiben SQL, wie wir es kennen: `SELECT * FROM...`. Das ist für Analysten oft der schnellste Weg. Beachten Sie, dass wir das SQL in `text()` verpacken müssen. Das Ergebnis iterieren wir Zeile für Zeile durch. Das ist speicherschonend, selbst wenn die Datenbank Millionen von Vögeln enthält.

**Image Prompt:** A terminal screen showing a glowing SQL command entering a pipeline and rows of data coming out the other end strictly aligned.

-----

**Slide 4: Parameterized Queries (Security)**

**Body Text (German):**

  * **Gefahr:** SQL Injection ist die häufigste Sicherheitslücke im Web. Bauen Sie SQL-Strings **niemals** mit `f-strings` oder `+` zusammen\!
  * **Lösung:** Nutzen Sie Parameter (`:param_name`). SQLAlchemy und der Treiber kümmern sich um das Escaping von gefährlichen Zeichen.
  * **Best Practice:** Betrachten Sie User-Input (z.B. Suche nach Ringnummer) immer als "untrusted".

**Code Snippet (Python):**

```python
# DANGEROUS - DO NOT DO THIS:
# sql = f"SELECT * FROM birds WHERE ring = '{user_input}'"

# SECURE Approach:
search_ring = "AX-9921'; DROP TABLE birds; --" # Malicious input

query = text("SELECT * FROM birds WHERE ring_number = :ring")

with engine.connect() as conn:
    # Pass parameters as a dictionary
    result = conn.execute(query, {"ring": search_ring})
    # The DB treats the input strictly as a value, not executable code.
```

**Speaker Notes (German):**
Das ist die wichtigste Slide für Ihre Sicherheit. Wenn ein User eine Ringnummer eingibt, könnte er versuchen, Ihre Datenbank zu löschen (SQL Injection). Im Code-Beispiel sehen Sie einen Angriffsversuch. Indem wir `:ring` als Platzhalter nutzen und die Daten separat übergeben (Zeile 10), wird der Angriff neutralisiert. Tun Sie das immer, ohne Ausnahme.

**Image Prompt:** A shield barrier deflecting malicious code bullets (labelled "DROP TABLE") while letting safe data packets pass through to the database server.

-----

**Slide 5: ORM Basics (Advanced Track)**

**Body Text (German):**

  * **Konzept:** Tabellen werden als Python-Klassen definiert (`Models`). Zeilen sind Instanzen dieser Klassen.
  * **Deklarativ:** Sie beschreiben die Struktur der Tabelle im Python-Code (`DeclarativeBase`).
  * **Session:** Statt `connection` nutzen wir eine `Session`. Sie verwaltet Transaktionen ("Unit of Work") und speichert Änderungen erst beim `commit()`.

**Code Snippet (Python):**

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class Bird(Base):
    __tablename__ = "bird_inventory"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    species: Mapped[str]
    weight: Mapped[float]

# Usage
with Session(engine) as session:
    # Create object instead of writing INSERT SQL
    new_bird = Bird(species="Blackbird", weight=95.2)
    session.add(new_bird)
    session.commit() # Saves to DB
```

**Speaker Notes (German):**
Experten nutzen meist das ORM. Statt SQL zu schreiben, definieren wir eine Klasse `Bird`. Wollen wir einen Vogel speichern, erstellen wir ein `Bird`-Objekt und übergeben es der `Session`. Kein `INSERT INTO...` nötig. Das macht den Code extrem sauber und wartbar, besonders bei komplexen Beziehungen zwischen Tabellen.

**Image Prompt:** A split screen: Left side shows raw SQL text, Right side shows a neat Python Class diagram, with an arrow indicating they map to the same underlying data structure.

-----

**Slide 6: Lab Preparation**

**Body Text (German):**

  * **Szenario:** Wir verbinden unsere Anwendung mit der zentralen Beringungs-Datenbank (`ringing.db`).
  * **Aufgabe 1 (Setup):** Erstellen Sie eine `Engine` für die bereitgestellte SQLite-Datei.
  * **Aufgabe 2 (Select):** Führen Sie eine `SELECT` Query aus, die alle Vögel anzeigt, die schwerer als 20g sind. Geben Sie die Ergebnisse aus.
  * **Aufgabe 3 (Security):** Schreiben Sie ein Skript, das den Benutzer nach einer Ringnummer fragt und diese **sicher** (parametrisiert) abfragt.
  * **Aufgabe 4 (Advanced - ORM):**
      * Definieren Sie ein `Bird` Model.
      * Nutzen Sie eine Session, um 100 simulierte Vögel (Bulk) in die Datenbank zu schreiben.

**Code Snippet (Python):**

```python
# Lab Starter Hint
from sqlalchemy import create_engine, text

# Connect to the provided lab database
engine = create_engine("sqlite:///lab_data.db")

# Test connection
with engine.connect() as conn:
    print("Database reachable.")
```

**Speaker Notes (German):**
Sie erhalten eine fertige `sqlite`-Datei von mir. Ihre Aufgabe ist es, eine Verbindung herzustellen und Daten abzufragen. Die Anfänger konzentrieren sich auf sauberes SQL und das Vermeiden von Injection. Die Profis unter Ihnen möchte ich sehen, wie Sie ein ORM-Model aufsetzen und Massendaten-Inserts durchführen.

**Image Prompt:** A computer screen showing a successfully established connection icon (green checkmark) linked to a database cylinder icon labeled "Lab Data".
