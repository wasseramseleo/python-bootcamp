# Lab 05: Datenbankzugriff mit SQLAlchemy

### Szenario
CSV-Dateien sind für dauerhafte Bankdaten ungeeignet. Wir migrieren nun auf eine relationale Datenbank (SQLite). Ihre Aufgabe ist es, die Basis-Tabellenstruktur zu erstellen und anschließend das moderne ORM (Object Relational Mapper) zu nutzen, um neue Daten objektorientiert zu speichern.

### Voraussetzungen
* Installation: `pip install sqlalchemy`

---

### Basis Aufgabe

Ziel ist der Umgang mit der `Engine` und das **sichere** Ausführen von SQL-Befehlen mittels Parametern (gegen SQL-Injection), wie in Sektion 4 des Theorie-Codes gezeigt.

**Anforderungen:**

1.  **Engine & Setup:**
    * Importieren Sie `create_engine` und `text` aus `sqlalchemy`.
    * Erstellen Sie eine Engine für die Datei `sqlite:///bank.db`.
    * Öffnen Sie eine Verbindung (`engine.connect()`).

2.  **Tabelle erstellen:**
    * Nutzen Sie `conn.execute()` und `text()`, um eine Tabelle `accounts` anzulegen.
    * Spalten: `id` (INTEGER PRIMARY KEY), `owner` (TEXT), `balance` (FLOAT).
    * Fügen Sie via SQL (`INSERT`) zwei Test-Konten ein (z.B. "Alice" mit 100.0, "Bob" mit 50.0).
    * *Wichtig:* Führen Sie `conn.commit()` aus, um die Änderungen zu speichern.

3.  **Sichere Abfrage (Parameterized Query):**
    * Dies ist der wichtigste Teil: Schreiben Sie eine `SELECT` Abfrage, die ein Konto anhand des `owner` Namens sucht.
    * **Verbot:** Nutzen Sie keine f-Strings (`f"WHERE owner = '{name}'"`).
    * **Gebot:** Nutzen Sie die sichere Syntax aus dem Theorie-Code (`text("... :name")`) und übergeben Sie den Suchbegriff als Dictionary beim `execute` Aufruf.
    * Geben Sie das Ergebnis auf der Konsole aus.

---

### Bonus Herausforderung

Ziel ist die Nutzung des ORM Modells (SQLAlchemy 2.0 Style) für das Einfügen von Daten, anstatt rohes SQL zu schreiben.

**Anforderungen:**

1.  **Model Definition:**
    * Importieren Sie `DeclarativeBase`, `Mapped`, `mapped_column` und `Session`.
    * Erstellen Sie eine `Base` Klasse.
    * Definieren Sie eine Klasse `Transaction`, die auf die Tabelle `transactions` mappt.
    * Attribute (mit Type Hints):
        * `id`: `int` (Primary Key)
        * `amount`: `float`
        * `purpose`: `str`

2.  **Daten Speichern:**
    * Nutzen Sie den `Session(engine)` Context Manager.
    * Erstellen Sie ein neues `Transaction` Objekt (z.B. "Salary", 2500.00).
    * Fügen Sie es der Session hinzu (`add`) und speichern Sie es (`commit`).
    * *Hinweis:* SQLAlchemy erstellt die Tabelle `transactions` automatisch, wenn Sie `Base.metadata.create_all(engine)` vor der Session ausführen (oder Sie erstellen sie manuell analog zu Teil 1).
```
