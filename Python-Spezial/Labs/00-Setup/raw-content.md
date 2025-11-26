# LAB 00 DETAILS:

* **Lab Title/Topic:** IDE & Python Setup
* **Lab Objectives:**
  * Participant tests their setup to be able to complete all labs without setup/environment issues.

# ACTION:
Generate **ONE** markdown file (Instructions) for this lab.
Participants are free to use either pip or uv throughout the course. Therefore write two separate Instructions for either choice.
They will create the venv in the project root once in this task and use it throughout the labs.
the labs are separate python packages inside the projext root (PROJECT_ROOT/Lab-XX/Lab_XX_Angabe.md).


-----

Hier ist die Anleitung für Lab 00.

### Design-Entscheidung

Da `uv` bereits installiert ist, biete ich es als **Pfad B (High-Performance)** an. Es ist deutlich schneller und vermeidet viele der typischen Berechtigungs-Probleme unter Windows. `pip` bleibt **Pfad A (Standard)** für diejenigen, die beim Bekannten bleiben wollen.

Wir richten das Virtual Environment (`.venv`) im **Root-Verzeichnis** ein, damit alle folgenden Labs (die in Unterordnern liegen) darauf zugreifen können.

-----

## `Lab_00_Angabe.md`

# Lab 00: Setup & Environment Check

### Szenario

Willkommen im "PyBank" Dev-Team! Bevor wir mit der Verarbeitung von Finanzdaten beginnen, müssen wir sicherstellen, dass Ihre lokale Entwicklungsumgebung (IDE) korrekt konfiguriert ist und alle notwendigen Bibliotheken installiert sind.

### Ziel

Einrichtung eines **Virtual Environments** im Projekt-Root und Installation aller Abhängigkeiten für den gesamten Kurs.

-----

### Schritt 1: Projekt-Struktur

1.  Erstellen Sie einen neuen Ordner auf Ihrem Computer, z.B. `PyBank_Course`.
2.  Öffnen Sie diesen Ordner in Ihrer IDE (VS Code oder PyCharm) als **Project Root**.

### Schritt 2: Environment erstellen

Wählen Sie **einen** der beiden Wege (Standard oder Modern/Schnell).

#### Weg A: Standard (pip)

Nutzen Sie diesen Weg, wenn Sie den klassischen Python-Workflow bevorzugen.

1.  **Terminal öffnen:** Öffnen Sie das Terminal in Ihrer IDE.
2.  **Venv erstellen:**
    ```bash
    python -m venv .venv
    ```
3.  **Aktivieren:**
      * **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
      * **Windows (CMD):** `.venv\Scripts\activate.bat`
      * **Mac/Linux:** `source .venv/bin/activate`
        *(Hinweis: In VS Code sollten Sie gefragt werden, ob Sie dieses Environment für den Workspace nutzen wollen. Klicken Sie auf "Ja".)*
4.  **Installation:**
    Kopieren Sie diesen Befehl, um alle Pakete für Lab 01-09 zu installieren:
    ```bash
    pip install pandas numpy sqlalchemy plotly scikit-learn python-docx pypdf pdfplumber reportlab
    ```

#### Weg B: Modern (uv)

Nutzen Sie diesen Weg für extrem schnelle Installationen. `uv` ist ein moderner Ersatz für pip/venv, geschrieben in Rust.

1.  **Terminal öffnen:** Öffnen Sie das Terminal in Ihrer IDE.
2.  **Venv erstellen:**
    ```bash
    uv venv
    ```
3.  **Aktivieren:**
      * Gleicher Schritt wie oben (Windows: `.venv\Scripts\activate`, Mac: `source .venv/bin/activate`).
      * *Alternativ können Sie Befehle auch ohne Aktivierung via `uv run` ausführen, aber für die IDE-Integration ist die Aktivierung empfohlen.*
4.  **Installation:**
    Nutzen Sie `uv pip`, um die Pakete in das erstellte venv zu laden:
    ```bash
    uv pip install pandas numpy sqlalchemy plotly scikit-learn python-docx pypdf pdfplumber reportlab
    ```

-----

### Schritt 3: Verifikation (Check Script)

Erstellen Sie im Hauptordner eine Datei `check_env.py` mit folgendem Inhalt, um zu testen, ob Python und alle Libraries korrekt geladen werden.

```python
import sys
import importlib

# Liste der Module, die wir im Kurs brauchen
required_modules = [
    'pandas', 'numpy', 'sqlalchemy', 'plotly', 
    'sklearn', 'docx', 'pypdf', 'pdfplumber', 'reportlab'
]

print(f"--- PyBank Environment Check ---")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Executable: {sys.executable}")
print("-" * 30)

all_success = True

for lib in required_modules:
    try:
        importlib.import_module(lib)
        print(f"[OK] {lib:<15} erfolgreich geladen.")
    except ImportError as e:
        print(f"[!!] FEHLER: {lib} konnte nicht geladen werden. ({e})")
        all_success = False

print("-" * 30)
if all_success:
    print("SUCCESS: Ihr System ist bereit für den Kurs! 🚀")
else:
    print("FAIL: Bitte überprüfen Sie die Installation.")
```

**Ausführen:**

```bash
python check_env.py
```

-----

### Bonus Herausforderung: Requirements Freeze

Um sicherzustellen, dass Ihre Kollegen exakt die gleichen Versionen nutzen, erstellen Sie eine Datei, die den aktuellen Zustand festhält.

1.  **Freeze:** Erstellen Sie eine `requirements.txt`.
      * Via pip: `pip freeze > requirements.txt`
      * Via uv: `uv pip freeze > requirements.txt`
2.  **Check:** Öffnen Sie die Textdatei und prüfen Sie, ob Bibliotheken wie `pandas` darin gelistet sind.