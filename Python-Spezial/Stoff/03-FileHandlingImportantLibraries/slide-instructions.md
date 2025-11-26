**Input Data:**

* **Topic Title:** 3. File Handling & Wichtige Libraries
* **Content Points:**
  - open() für txt
  - json & csv Module
  - datetime & re (regex)

* **Lab Objectives:**
* CSV/Excel/JSON Dateien öffnen, lesen und wieder schreiben. Timestamps im iso format mittels datetime modul parsen.
* Advanced: Context Manager (with) beherrschen, Encoding-Fehler beheben, komplexe JSON-Strukturen parsen. Textmuster mit
  re filtern.

-----

Here are the slides for **Topic 3: File Handling & Wichtige Libraries**, focusing on data persistence and parsing within the Bird Ringing domain.

-----

**Slide 1: File I/O & Context Managers**

**Body Text (German):**

  * **Der `open()` Befehl:** Der klassische Weg, um Dateien zu öffnen. Modi: `'r'` (read), `'w'` (write - überschreibt!), `'a'` (append).
  * **Der Context Manager (`with`):** **Best Practice.** Er garantiert, dass die Datei automatisch geschlossen wird, selbst wenn Fehler auftreten. Das verhindert Resource Leaks und korrupte Dateien.
  * **Encoding:** Geben Sie immer `encoding='utf-8'` an, um Probleme mit Umlauten oder Sonderzeichen zu vermeiden.

**Code Snippet (Python):**

```python
# Reading raw field notes
log_file = "field_notes_2024.txt"

# The 'with' statement ensures the file closes safely
with open(log_file, mode='r', encoding='utf-8') as f:
    content = f.read()
    # File is open here

# File is automatically closed here
print(f"Read {len(content)} characters.")
```

**Speaker Notes (German):**
Wir arbeiten mit Dateien. Die wichtigste Regel: Nutzen Sie *immer* das `with`-Statement. Ohne `with` müssen Sie `.close()` manuell aufrufen. Wenn Ihr Programm vor dem Schließen abstürzt, bleibt die Datei blockiert oder Daten gehen verloren. Das ist in automatisierten Pipelines fatal. Achten Sie zudem explizit auf UTF-8 Encoding, sonst machen Sonderzeichen Probleme.

**Image Prompt:** A diagram illustrating a safety latch (the `with` block) that automatically locks (closes file) as soon as the user steps out of the zone.

-----

**Slide 2: CSV Verarbeitung**

**Body Text (German):**

  * **Standard:** CSV (Comma Separated Values) ist das Austauschformat Nr. 1 für Tabellendaten.
  * **`csv` Modul:** Bietet robustere Parser als einfaches String-Splitting (behandelt z.B. Kommas innerhalb von Textfeldern korrekt).
  * **DictReader:** Liest Zeilen direkt in Dictionaries ein, wobei die Header-Zeile als Keys dient. Das macht den Code lesbarer und robuster gegen Spaltenverschiebungen.

**Code Snippet (Python):**

```python
import csv

# Reading ringing data
with open('capture_data.csv', mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Access by column name, not index
        print(f"Bird ID: {row['Ring_ID']} - Weight: {row['Weight']}")
```

**Speaker Notes (German):**
Excel-Export ist Standard. Versuchen Sie nicht, CSV-Dateien per Hand mit `split(',')` zu parsen – das scheitert, sobald ein Kommentarfeld ein Komma enthält. Nutzen Sie das `csv` Modul. Besonders `DictReader` ist wertvoll: Wenn sich die Spaltenreihenfolge in der Input-Datei ändert, funktioniert Ihr Code weiterhin, da er Spaltennamen statt Indizes verwendet.

**Image Prompt:** A visual transformation: A messy text block of comma-separated values flowing through a funnel and emerging as neatly organized cards (Dictionaries).

-----

**Slide 3: JSON & Serialisierung**

**Body Text (German):**

  * **JSON (JavaScript Object Notation):** Das Standardformat für Web-APIs und NoSQL-Datenbanken. Es bildet Python-Datentypen (Lists, Dicts, Strings, Numbers) fast 1:1 ab.
  * **Workflow:**
      * `json.dump()`: Speichert Python-Objekte in eine Datei.
      * `json.load()`: Lädt Daten aus einer Datei in Python-Objekte.
  * **Nesting:** JSON erlaubt tiefe Verschachtelungen (z.B. Liste von Messwerten innerhalb eines Vogel-Objekts).

**Code Snippet (Python):**

```python
import json

bird_data = {
    "species": "Ciconia ciconia", # Weißstorch
    "rings": ["H8812", "GPS-Tracker-09"],
    "measurements": {"bill": 180, "wing": 590}
}

# Serialization (Writing to disk)
with open('stork_data.json', 'w') as f:
    json.dump(bird_data, f, indent=4)
```

**Speaker Notes (German):**
Wenn CSV flach ist, ist JSON tief. Es ist ideal für hierarchische Daten, wie z.B. ein Storch, der mehrere Ringe und komplexe GPS-Logs hat. Mit `json.dump` und `indent=4` erzeugen Sie menschenlesbare Dateien. Das ist essenziell für Debugging und Datenaustausch mit modernen Web-Services.

**Image Prompt:** A tree structure diagram showing a root object branching out into nested attributes, symbolizing the hierarchical nature of JSON compared to flat CSV tables.

-----

**Slide 4: Datetime Handling**

**Body Text (German):**

  * **ISO 8601 (`YYYY-MM-DD`):** Das einzig vernünftige Format für Datenaustausch. Vermeiden Sie lokale Formate wie `DD.MM.YYYY` in Rohdaten.
  * **Parsing:** `datetime.strptime()` wandelt Strings in Zeit-Objekte um.
  * **Rechnen:** Mit `datetime` Objekten können Sie rechnen (z.B. `capture_time - release_time = duration`).

**Code Snippet (Python):**

```python
from datetime import datetime, timedelta

raw_date = "2024-05-12 14:30:00"
# Parse string to object
capture_time = datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")

# Calculate release time (20 mins later)
release_time = capture_time + timedelta(minutes=20)

print(f"Release ISO: {release_time.isoformat()}")
```

**Speaker Notes (German):**
Zeit ist schwierig. Schaltjahre, Zeitzonen, Formate. Rechnen Sie nie manuell an Strings herum. Nutzen Sie das `datetime` Modul. Wir parsen hier einen Zeitstempel und addieren 20 Minuten Bearbeitungszeit. Nutzen Sie für Speicherformate immer ISO 8601 (`.isoformat()`), damit ihre Daten international und maschinenlesbar bleiben.

**Image Prompt:** A clock interface showing a string being fed in, gears turning inside (parsing), and a calculated time object coming out.

-----

**Slide 5: Advanced Regex (Expert Track)**

**Body Text (German):**

  * **Regular Expressions (`re`):** Mächtiges Tool zur Mustererkennung in Strings.
  * **Use Case:** Extrahieren von Ring-IDs aus unstrukturierten Kommentaren oder Validierung von Eingabeformaten.
  * **Wichtige Funktionen:**
      * `re.search()`: Sucht das erste Vorkommen.
      * `re.findall()`: Findet alle Vorkommen.
      * `re.sub()`: Ersetzt Muster (Suchen & Ersetzen).

**Code Snippet (Python):**

```python
import re

notes = "Bird spotted with ring AX-9921 near the lake, maybe AX-9922 too."

# Pattern: 2 Letters, hyphen, 4 Digits
pattern = r"[A-Z]{2}-\d{4}"

found_rings = re.findall(pattern, notes)
# Result: ['AX-9921', 'AX-9922']
```

**Speaker Notes (German):**
Dies ist für die fortgeschrittenen Teilnehmer. Manchmal erhalten Sie Daten als Freitext. Regex ist wie ein Skalpell für Strings. Im Code definieren wir ein Muster: Zwei Großbuchstaben, Bindestrich, vier Zahlen. `findall` extrahiert sofort alle passenden Ringnummern aus dem Notizblock-Text. Regex ist kryptisch, aber extrem effizient.

**Image Prompt:** A magnifying glass hovering over a page of blurred text, bringing only the specific codes matching the pattern (e.g., AX-9921) into sharp focus / color.

-----

**Slide 6: Lab Preparation**

**Body Text (German):**

  * **Szenario:** Migration bestehender Papier-Daten (CSV) in eine moderne NoSQL-Struktur (JSON).
  * **Aufgabe 1 (File I/O):** Öffnen Sie eine bereitgestellte CSV-Datei mit Vogeldaten (`DictReader`).
  * **Aufgabe 2 (Transformation):** Fügen Sie jeder Zeile einen aktuellen Zeitstempel hinzu (nutzen Sie `datetime`).
  * **Aufgabe 3 (Output):** Speichern Sie die gesamte Liste als neue JSON-Datei ab.
  * **Aufgabe 4 (Expert - Regex):** Die CSV enthält eine Spalte "Notizen" mit versteckten Ring-Codes. Extrahieren Sie diese mit `re` in ein neues Feld.

**Code Snippet (Python):**

```python
# Lab Hint: Structure
data_list = []
with open('input.csv', 'r') as f_in:
    # Read data...
    # Transform data...
    pass

with open('output.json', 'w') as f_out:
    # Dump data...
    pass
```

**Speaker Notes (German):**
Wir bauen eine kleine ETL-Pipeline (Extract, Transform, Load). Sie lesen CSV, manipulieren Daten mit `datetime` und speichern als JSON. Das ist ein klassischer Data-Engineering-Task. Die Experten filtern zusätzlich mittels Regex Informationen aus Textfeldern. Achten Sie darauf, Dateien sauber mit `with` zu schließen.

**Image Prompt:** A schematic diagram of a factory conveyor belt: Raw material (CSV) enters left, robots (Python scripts) modify it (add timestamp), and packaged boxes (JSON) exit right.

