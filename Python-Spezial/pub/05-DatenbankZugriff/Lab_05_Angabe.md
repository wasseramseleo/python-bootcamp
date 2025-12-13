# Lab 05: Datenbankzugriff mit SQLAlchemy

### Szenario

CSV-Dateien sind für dauerhafte Bankdaten ungeeignet. Wir migrieren nun auf eine relationale Datenbank (SQLite für diesen Workshop). Sie sollen eine Tabelle für Konten (`accounts`) anlegen und Transaktionen sicher speichern.

### Voraussetzungen

  * Installation von SQLAlchemy:
    ```bash
    pip install sqlalchemy
    ```
  * *(Optional)* Ein SQLite Viewer Tool, um die Datei `bank.db` später zu inspizieren.

-----

### Basis Aufgabe

Ziel ist das Herstellen einer Verbindung und das Ausführen von "Raw SQL" über Python.

**Anforderungen:**

1.  **Engine erstellen:**
      * Importieren Sie `create_engine` und `text` aus `sqlalchemy`.
      * Erstellen Sie eine Engine für eine lokale Datei: `sqlite:///bank.db`.
2.  **Verbindung & Setup:**
      * Öffnen Sie eine Verbindung (`engine.connect()`).
      * Führen Sie ein SQL-Statement aus, um eine Tabelle `accounts` zu erstellen (Spalten: `id` (INTEGER PK), `owner` (TEXT), `balance` (FLOAT)).
      * *Hinweis:* Vergessen Sie bei Datenänderungen (CREATE, INSERT) nicht, `connection.commit()` aufzurufen.
3.  **Daten einfügen:**
      * Fügen Sie 2-3 Beispiel-Konten per SQL `INSERT` ein.
4.  **Daten lesen:**
      * Führen Sie ein `SELECT * FROM accounts` aus.
      * Iterieren Sie über das Ergebnis und geben Sie den Besitzer und Kontostand aus.

-----

### Bonus Herausforderung

Ziel ist die Nutzung des ORM (Object Relational Mapper) für objektorientierten Datenbankzugriff und Sicherheits-Best-Practices.

**Anforderungen:**

1.  **ORM Setup:**
      * Nutzen Sie `declarative_base` (oder `DeclarativeBase` ab v2.0), um eine Basisklasse zu erstellen.
      * Definieren Sie eine Python-Klasse `Transaction`, die auf eine Tabelle `transactions` mappt.
      * Spalten: `id` (PK), `amount` (Float), `currency` (String), `purpose` (String).
2.  **Bulk Insert:**
      * Erstellen Sie eine Liste von 100 `Transaction`-Objekten (nutzen Sie eine Schleife und Zufallswerte oder Dummy-Daten).
      * Speichern Sie alle Objekte auf einmal in die Datenbank (`session.add_all(...)` und `commit`).
3.  **Sicherheit (Parameterized Query):**
      * Schreiben Sie eine Abfrage, die Transaktionen filtert, wo die Währung "USD" ist.
      * **Wichtig:** Nutzen Sie keine String-Concatenation (`"WHERE currency = '" + var + "'"`), sondern die sicheren Filter-Methoden des ORM oder Parameter-Binding, um SQL Injection zu verhindern.
