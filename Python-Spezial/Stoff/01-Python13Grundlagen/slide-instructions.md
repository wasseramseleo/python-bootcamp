**Input Data:**

  * **Topic Title:** 1. Python 13 Grundlagen
  * **Content Points:**
    - Syntax & Variablen
    - Listen, Dictionaries, Tuples
    - Kontrollstrukturen (Loops, If)
  * **Lab Objectives:**
    * Syntax verstehen und einfache Datenspeicherungen in Listen/Dicts durchführen.
    * Advanced: List Comprehensions nutzen, Generatoren verstehen und Type Hinting anwenden.

----

Here are the slides for **Topic 1: Python 13 Grundlagen**, tailored to the Bird Ringing domain and your specific formatting constraints.

-----

**Slide 1: Syntax, Variablen & Datentypen**

**Body Text (German):**

  * **Dynamische Typisierung:** Python erkennt Datentypen automatisch zur Laufzeit; eine explizite Deklaration ist nicht zwingend, aber Type Hinting (seit Python 3.5) wird für professionelle Projekte dringend empfohlen.
  * **Lesbarkeit:** Durch strikte Indentierung (Einrückung) wird der Code strukturiert. Klammern `{}` wie in C oder Java entfallen meist.
  * **Namenskonventionen:** Variablen werden in `snake_case` geschrieben.

**Code Snippet (Python):**

```python
# Basic assignment (Dynamic Typing)
species_name = "Parus major"  # Kohlmeise
wing_length_mm = 74.5
is_migratory = False

# Type Hinting (Modern Standard)
ring_number: str = "AX-92831"
body_mass_g: float = 18.2
```

**Speaker Notes (German):**
Willkommen zu Python. Wir starten direkt mit der Syntax. Im Gegensatz zu statischen Sprachen müssen wir den Typ hier nicht zwingend angeben, Python "errät" ihn (Duck Typing). Sehen Sie sich den Code an: Wir erfassen Basisdaten einer Kohlmeise (*Parus major*). Für die erfahrenen Entwickler unter Ihnen: Nutzen Sie Type Hints (wie im unteren Block). Das hat keinen Einfluss auf die Runtime, hilft aber massiv bei der statischen Code-Analyse und IDE-Support.

**Image Prompt:** A clean comparison graphic showing a snippet of C++ code with curly braces vs. clean Python code with indentation, highlighting the visual simplicity.

-----

**Slide 2: Listen & Tuples (Sequences)**

**Body Text (German):**

  * **List (Mutable):** Eine veränderbare Sequenz von Elementen. Ideal für Datensätze, die während der Laufzeit wachsen oder sich ändern (z.B. gefangene Vögel pro Stunde).
  * **Tuple (Immutable):** Eine unveränderbare Sequenz. Schneller und speichereffizienter. Muss für Daten genutzt werden, die konstant bleiben sollen (Datenintegrität).
  * **Indexing:** Zugriff erfolgt 0-basiert. Negative Indizes erlauben Zugriff von hinten (`-1` ist das letzte Element).

**Code Snippet (Python):**

```python
# List: Mutable collection of daily captures
captured_birds = ["Blaumeise", "Kohlmeise", "Rotkehlchen"]
captured_birds.append("Amsel")  # List can grow

# Tuple: Immutable capture site coordinates (Lat, Lon)
site_coords = (48.2082, 16.3738)
# site_coords[0] = 49.000  # This would raise a TypeError
```

**Speaker Notes (German):**
Hier ist eine kritische Unterscheidung: `Lists` vs. `Tuples`. Nutzen Sie Listen, wenn Sie Vögel nacheinander fangen und die Liste erweitern müssen. Nutzen Sie Tuples für feste Daten wie die GPS-Koordinaten des Fangstandorts. Ein Tuple kann technisch nicht verändert werden – das schützt Ihre Referenzdaten vor versehentlichem Überschreiben.

**Image Prompt:** A visual metaphor: An open cardboard box (List) where items can be added/removed vs. a sealed glass display case (Tuple) containing fixed items.

-----

**Slide 3: Dictionaries (Key-Value Stores)**

**Body Text (German):**

  * **Mapping:** Speichert Daten als Key-Value-Paare. Keys müssen unveränderbar (immutable) und einzigartig sein (oft Strings oder Zahlen).
  * **Performance:** Bietet extrem schnelle Lookups (O(1) Komplexität), ideal um spezifische Attribute eines Vogels abzurufen.
  * **Anwendung:** Dictionaries sind das Standardformat für strukturierte Daten in Python (ähnlich JSON).

**Code Snippet (Python):**

```python
# Dictionary representing a single bird's biometric record
bird_record = {
    "ring_id": "H77-201",
    "species": "Erithacus rubecula",  # Rotkehlchen
    "fat_score": 3,
    "wing_length": 72.0
}

# Accessing data efficiently
print(f"Fat Score: {bird_record['fat_score']}")
```

**Speaker Notes (German):**
Das `Dictionary` ist das Arbeitspferd von Python. Stellen Sie es sich als digitalen Karteikasten vor. Wir nutzen es hier für den Datensatz eines einzelnen Rotkehlchens. Der Zugriff über den Key `"fat_score"` ist sofortig, egal wie groß das Dictionary ist. Für die Anfänger: Das ist sehr ähnlich zu JSON-Objekten.

**Image Prompt:** A diagram showing a "Key" (labelled 'ring\_id') fitting into a lock to instantly reveal the "Value" (labelled 'H77-201').

-----

**Slide 4: Kontrollstrukturen (Flow Control)**

**Body Text (German):**

  * **If/Elif/Else:** Standardmäßige bedingte Logik. Bedingung muss `True` ergeben.
  * **For Loop:** Iteriert direkt über Elemente einer Sequenz (nicht über einen Index wie in C).
  * **Scope:** Variablen, die in `if`-Blöcken oder Loops definiert werden, sind oft noch außerhalb sichtbar (im Gegensatz zu vielen anderen Sprachen). Vorsicht mit dem Scope.

**Code Snippet (Python):**

```python
daily_weights = [18.5, 19.2, 17.8, 21.0]

for weight in daily_weights:
    if weight > 20.0:
        status = "High reserves"
    elif weight < 18.0:
        status = "Underweight"
    else:
        status = "Normal"
    
    # Logic to log status...
```

**Speaker Notes (German):**
Logiksteuerung. Beachten Sie den `for`-Loop: Wir iterieren direkt über die Gewichte (`weight in daily_weights`), wir hantieren nicht mit `i` oder Zählern. Das macht Python-Code weniger fehleranfällig für "Off-by-one"-Fehler. Das Einrücken definiert, was zum Loop oder zum If-Block gehört. Fehlt die Einrückung, gehört der Code nicht dazu.

**Image Prompt:** A flowchart showing a bird measurement going through a diamond-shaped decision box (If weight \> 20) branching into two distinct paths.

-----

**Slide 5: Advanced Concepts (Expert Track)**

**Body Text (German):**

  * **List Comprehensions:** Eine prägnante Syntax, um Listen basierend auf existierenden Listen zu erstellen. Pythonischer und oft schneller als klassische Loops.
  * **Generators:** Verwenden `()` statt `[]` oder `yield`. Erzeugen Werte "lazy" (bei Bedarf), was bei großen Datensätzen (z.B. Millionen von Migrationsdaten) RAM spart.
  * **Type Hinting & Docstrings:** Essenziell für Wartbarkeit in Teams.

**Code Snippet (Python):**

```python
raw_data = [18.5, 19.2, 17.8, 21.0]

# List Comprehension: Convert all to integers (rounding down)
int_weights = [int(w) for w in raw_data]

# Generator Expression: Memory efficient for large datasets
# Calculates potential energy only when iterated over
energy_gen = (w * 0.5 for w in raw_data) 

def process_bird(ring: str) -> bool:
    """Validates ring format."""
    return len(ring) == 6
```

**Speaker Notes (German):**
Diese Slide ist für die Fortgeschrittenen. Statt eines Loops über fünf Zeilen nutzen wir eine *List Comprehension* (Zeile 4), um Daten in einer Zeile zu transformieren. Das ist "Pythonic". Zeile 8 zeigt einen *Generator*: Wenn wir Millionen von Datensätzen haben, berechnet dieser Ausdruck die Werte erst, wenn wir sie abrufen, und spart so Arbeitsspeicher. Nutzen Sie Type Hints (Zeile 10), um Schnittstellen klar zu definieren.

**Image Prompt:** A split screen visual: Left side shows a bulky machine (standard loop), right side shows a sleek, streamlined laser processing line (List Comprehension).

-----

**Slide 6: Lab Preparation**

**Body Text (German):**

  * **Szenario:** Wir simulieren die Erfassung von Beringungsdaten.
  * **Aufgabe 1 (Basics):** Erstellen Sie eine Liste von Vögeln (Strings) und ein Dictionary für einen spezifischen Vogel mit Messwerten.
  * **Aufgabe 2 (Logic):** Iterieren Sie über eine Liste von Gewichten und kategorisieren Sie diese (If/Else).
  * **Aufgabe 3 (Advanced):** Nutzen Sie eine List Comprehension, um eine Liste von Flügel-Längen von `mm` in `cm` umzurechnen. Typisieren Sie Ihre Variablen.
  * **Transfer:** Überlegen Sie beim Coden, wie diese Strukturen (Liste vs. Dict) Ihre echten Geschäftsdaten abbilden würden.

**Code Snippet (Python):**

```python
# Lab Starter Hint
# Target structure implies: List of Dictionaries
flock_data = [
    {"id": "A1", "weight": 18},
    {"id": "A2", "weight": 19}
]
```

**Speaker Notes (German):**
Jetzt sind Sie dran. Öffnen Sie Ihre IDE. Wir bauen einen einfachen Datenspeicher. Einsteiger konzentrieren sich darauf, Syntaxfehler zu vermeiden und Dictionaries zu verstehen. Die Profis unter Ihnen: Ich erwarte Type Hints und mindestens eine List Comprehension in Ihrer Lösung. Versuchen Sie, die Logik abstrakt zu halten, damit Sie sie gedanklich auf Ihren eigenen Business-Kontext übertragen können.

**Image Prompt:** An image of a laptop screen displaying a Python IDE with code, next to a bird ringing notebook and calipers, bridging the digital and physical worlds.
