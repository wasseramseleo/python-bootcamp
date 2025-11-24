**Input Data:**
Create 1-2 Slides highlighting the key-takeaways from the topics of day 1.

* **Topic Title:** Recap Tag 1
* **Content Points:**
    - Python 13 Grundlagen
    - Modularisierung & Best Practices
    - File Handling & Wichtige Libraries
    - Unstrukturierte Daten (Docs)
    - Datenbankzugriff

-----

Here are the summary slides for Day 1, consolidating the key learnings from the first five topics.

-----

**Slide 1: Recap Tag 1 – Fundamente & Datenfluss**

**Body Text (German):**

  * **Core Data Structures:** Wir nutzen `Lists` für Sequenzen (gefangene Vögel) und `Dictionaries` für strukturierte Datensätze (Vogel-Attribute).
  * **Clean Code:**
      * **Modularisierung:** Logik gehört in Funktionen (DRY-Prinzip) und Module.
      * **Type Hinting:** Erhöht die Lesbarkeit und IDE-Support (`def func(x: int) -> str:`).
  * **File I/O:** Der **Context Manager** (`with open(...)`) ist nicht verhandelbar. Er garantiert Datensicherheit beim Lesen/Schreiben von CSV und JSON.

**Code Snippet (Python):**

```python
# The "Day 1 Stack": Structuring, Processing, Saving
def save_capture(bird_data: dict, filename: str) -> None:
    """Appends a bird record to a JSON log safely."""
    import json
    
    # Context Manager handles opening/closing
    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(bird_data, f)
        f.write('\n') # Newline for JSONL format

record = {"species": "Parus major", "ring": "AX-99", "weight": 18.5}
save_capture(record, "daily_log.json")
```

**Speaker Notes (German):**
Lassen Sie uns Tag 1 Revue passieren. Wir haben gelernt, wie wir Python "sprechen": Wir nutzen Dictionaries statt loser Variablen und kapseln Logik in Funktionen. Das wichtigste Takeaway für die Praxis: Wenn Sie Dateien anfassen – egal ob CSV für den Export oder JSON für APIs – nutzen Sie immer den `with`-Block. Das ist Ihre Lebensversicherung gegen korrupte Daten.

**Image Prompt:** A composite schematic: Puzzle pieces labeled "List", "Dict", and "Function" being assembled into a secure box labeled "File System" via a key labeled "with".

-----

**Slide 2: Recap Tag 1 – Integration & Persistenz**

**Body Text (German):**

  * **Legacy Data:** Python ist der "Klebstoff". Wir nutzen Libraries wie `python-docx` und `pypdf`, um wertvolle Daten aus reinen Layout-Formaten zu befreien.
  * **SQLAlchemy:** Der Industriestandard für Datenbanken. Die `Engine` verwaltet Verbindungen effizient.
  * **Security First:** Bei Datenbank-Abfragen nutzen wir **Parameter**, niemals String-Verkettung, um SQL-Injection zu verhindern.

**Code Snippet (Python):**

```python
from sqlalchemy import text

# Pattern: Extract -> Transform -> Load (ETL)
def check_ring_in_db(engine, ring_id: str):
    # 1. Secure Query (Parameterized)
    query = text("SELECT * FROM captures WHERE ring_id = :rid")
    
    with engine.connect() as conn:
        result = conn.execute(query, {"rid": ring_id}) # Safe!
        return result.fetchone()

# Imagine 'ring_id' came from a PDF extraction earlier
found = check_ring_in_db(my_engine, "AX-9921")
```

**Speaker Notes (German):**
Im zweiten Teil haben wir die "Sandbox" verlassen. Wir haben gesehen, dass Daten oft unstrukturiert (PDF/Word) vorliegen und extrahiert werden müssen. Sobald die Daten sauber sind, gehören sie in eine Datenbank. Das wichtigste Takeaway hier: Sicherheit. Egal ob Junior oder Senior Developer – wer SQL-Strings mit `+` zusammenbaut, gefährdet das Projekt. Nutzen Sie Parameter, wie im Code gezeigt.

**Image Prompt:** A bridge connecting two islands. Left Island: "Chaos" (stacks of papers, PDFs). Right Island: "Order" (structured Database servers). Python is the secure bridge between them.
