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