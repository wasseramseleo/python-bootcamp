**Input Data:**

  * **Topic Title:** 2. Modularisierung & Best Practices
  * **Content Points:**
    - Funktionen & Module
    - pip & Environments
    - Skript-Struktur (PEP 8)
  * **Lab Objectives:**
    * Code in Funktionen kapseln und externe Libraries importieren.
    * Advanced: Eigene Module erstellen, if __name__ == "__main__" verstehen, Exception Handling (try/except).

----

Here are the slides for **Topic 2: Modularisierung & Best Practices**, tailored to the Bird Ringing domain.

-----

**Slide 1: Funktionen & Kapselung**

**Body Text (German):**

  * **DRY-Prinzip:** "Don't Repeat Yourself". Wenn Sie Code mehrfach kopieren, gehört er in eine Function.
  * **Parameter & Return:** Funktionen akzeptieren Inputs (Argumente) und geben Ergebnisse zurück. Vermeiden Sie globale Variablen innerhalb von Funktionen (Side Effects).
  * **Docstrings:** Dokumentieren Sie *was* die Funktion tut direkt unter der Definition (`"""..."""`).
  * **Default Arguments:** Parameter können Standardwerte haben, was die Flexibilität erhöht.

**Code Snippet (Python):**

```python
def calculate_condition_index(weight_g: float, wing_len_mm: float) -> float:
    """
    Calculates bird body condition index using scaled mass index concept.
    """
    if wing_len_mm == 0:
        return 0.0
    return weight_g / wing_len_mm

# Usage
index = calculate_condition_index(18.5, 74.0)
```

**Speaker Notes (German):**
Wir verlassen nun den linearen Code. Funktionen sind Bausteine. Stellen Sie sich vor, Sie berechnen den Gesundheitsindex eines Vogels an zehn verschiedenen Stellen im Code. Ändert sich die Formel, müssen Sie zehn Stellen ändern. Mit einer Function ändern Sie es nur einmal an zentraler Stelle. Beachten Sie den Docstring und die Type Hints – das ist der Standard für professionelle Softwareentwicklung.

**Image Prompt:** An illustration comparing a messy pile of loose wires (unstructured code) to a neat modular plug-and-play connector system (functions).

-----

**Slide 2: Module & Imports**

**Body Text (German):**

  * **Standard Library:** Python kommt "batteries included". Module wie `math`, `datetime` oder `os` sind sofort verfügbar.
  * **Import-Strategien:**
      * `import module`: Importiert das ganze Modul (Namespace bleibt sauber).
      * `from module import function`: Importiert spezifische Teile (kürzerer Aufruf, aber Vorsicht vor Namenskonflikten).
  * **Eigene Module:** Jede `.py` Datei ist ein Modul und kann von anderen Dateien importiert werden.

**Code Snippet (Python):**

```python
import math
from datetime import datetime

def get_banding_timestamp():
    # Returns current time in ISO format
    return datetime.now().isoformat()

# Using standard library math
wing_area = math.pi * (5.2 ** 2) 
```

**Speaker Notes (German):**
Niemand schreibt alles von null. Python hat eine riesige Standardbibliothek. Wenn wir Beringungsdaten mit Zeitstempeln versehen wollen, nutzen wir `datetime`. Ein Modul ist technisch gesehen einfach nur eine Datei, die Python-Code enthält. Sie können Ihren Code logisch aufteilen: Eine Datei für Datenbank-Logik, eine für Berechnungen.

**Image Prompt:** A diagram showing a "Main Script" connecting to several external boxes labeled "Math", "Datetime", and "Custom Tools", illustrating dependency.

-----

**Slide 3: pip & Virtual Environments**

**Body Text (German):**

  * **PyPI (Python Package Index):** Das Repository für externe Libraries (z.B. `pandas` für Datenanalyse, `requests` für API-Calls).
  * **Virtual Environments (`venv`):** Erstellt isolierte Umgebungen für Projekte.
      * *Problem:* Projekt A braucht Library Version 1.0, Projekt B braucht Version 2.0.
      * *Lösung:* Jedes Projekt hat sein eigenes Environment.
  * **Best Practice:** Niemals global installieren, immer in ein Environment.

**Code Snippet (Python):**

```bash
# Terminal / Command Line commands (not Python code)

# 1. Create environment
python -m venv .venv

# 2. Activate environment (Windows)
.venv\Scripts\activate

# 3. Install package
pip install pandas
```

**Speaker Notes (German):**
Dies ist oft die größte Hürde für Anfänger, aber essenziell. Ein "Virtual Environment" ist wie ein separater Rucksack für jede Exkursion. Für die Watvogel-Zählung brauchen Sie Gummistiefel (Library A), für die Greifvogel-Beringung Kletterausrüstung (Library B). Wenn Sie alles in einen Rucksack (Global Python) stopfen, wird es Chaos geben. Nutzen Sie `venv`.

**Image Prompt:** Visual comparison: One messy toolbox overflowing with incompatible tools vs. several neat, labeled toolkits containing only what is needed for specific tasks.

-----

**Slide 4: Skript-Struktur & Entry Points**

**Body Text (German):**

  * **PEP 8:** Der Style Guide für Python Code (4 Leerzeichen Einrückung, Leerzeilen zwischen Funktionen, Importe ganz oben).
  * **Main Guard:** `if __name__ == "__main__":`
      * Dieser Block wird *nur* ausgeführt, wenn das Skript direkt gestartet wird.
      * Er wird *nicht* ausgeführt, wenn das Skript als Modul importiert wird.
  * **Struktur:** Imports -\> Konstanten -\> Klassen/Funktionen -\> Main Block.

**Code Snippet (Python):**

```python
import sys

DEFAULT_SPECIES = "Unknown"

def main():
    print("Starting ringing session...")
    # Main logic calls here

if __name__ == "__main__":
    # Entry point
    main()
```

**Speaker Notes (German):**
Struktur ist Disziplin. Gewöhnen Sie sich den `if __name__ == "__main__":` Block an. Warum? Wenn Sie Ihre Berechnungsfunktionen später in einem anderen Skript wiederverwenden (importieren) wollen, verhindert dieser Block, dass das Skript sofort losläuft und Code ausführt, den Sie gar nicht wollten. Es trennt "Definition" von "Ausführung".

**Image Prompt:** A structural blueprint of a building (script) showing distinct zones: Foundation (Imports), Rooms (Functions), and the Front Door (Main Execution Block).

-----

**Slide 5: Exception Handling (Advanced Focus)**

**Body Text (German):**

  * **Robustheit:** Code darf bei fehlerhaften Daten (z.B. Gewicht = 0) nicht abstürzen.
  * **Try / Except:** Fängt Fehler ab und definiert eine alternative Behandlung.
  * **EAFP:** "It's easier to ask for forgiveness than permission". In Python probiert man es oft einfach (`try`) und fängt den Fehler, statt vorher alles zu prüfen (`if`).

**Code Snippet (Python):**

```python
raw_weight = "18.5g" # Malformed data (string with unit)

try:
    # Try to convert to float
    weight = float(raw_weight)
except ValueError as e:
    # Handle the specific error
    print(f"Error reading scale: {e}")
    weight = None
```

**Speaker Notes (German):**
Für die Fortgeschrittenen: Echte Daten sind schmutzig. Vielleicht tippt jemand "18g" statt "18" ein. Ohne Error Handling stürzt Ihr Programm ab (Crash). Mit `try/except` fangen Sie den Fehler, loggen ihn ("Waage nicht lesbar") und das Programm läuft weiter. Das ist der Unterschied zwischen einem Hobby-Skript und einem Produktionstool.

**Image Prompt:** A car airbag deploying. The car hits a bump (Error), but the driver is protected by the airbag (Exception Handling) and doesn't fly through the windshield.

-----

**Slide 6: Lab Preparation**

**Body Text (German):**

  * **Ziel:** Refactoring des Codes aus Lab 1 in saubere Funktionen.
  * **Aufgabe 1 (Funktionen):** Schreiben Sie eine Funktion `check_migration(weight, species)`, die `True` zurückgibt, wenn das Gewicht über einem Schwellenwert liegt.
  * **Aufgabe 2 (Module):** Lagern Sie diese Funktion in eine Datei `bird_logic.py` aus und importieren Sie sie in `main.py`.
  * **Aufgabe 3 (Advanced):**
      * Verwenden Sie `try/except` beim Einlesen von Benutzereingaben (`input()`).
      * Strukturieren Sie das Skript mit `if __name__ == "__main__":`.

**Code Snippet (Python):**

```python
# Lab Structure Hint
# file: main.py
import bird_logic

def run_session():
    try:
        data = float(input("Enter weight: "))
        if bird_logic.check_migration(data):
            print("Ready for migration")
    except ValueError:
        print("Please enter numbers only.")
```

**Speaker Notes (German):**
Wir räumen auf. Zerteilen Sie Ihren Code. Die Einsteiger erstellen einfache Funktionen im selben File. Die Fortgeschrittenen erstellen zwei Files: Ein `main.py` (das Programm) und ein `bird_logic.py` (die Bibliothek). Versuchen Sie absichtlich, Fehler zu provozieren (Buchstaben statt Zahlen eingeben) und fangen Sie diese ab.

**Image Prompt:** A split screen showing a messy desk being organized into labeled drawers and folders, representing the refactoring process.
