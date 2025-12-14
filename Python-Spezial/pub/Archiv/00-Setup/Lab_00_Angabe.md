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

Wählen Sie **einen** der drei Wege (Standard, Modern oder Anaconda).

#### Option A: pip

Nutzen Sie diesen Weg, wenn Sie den klassischen Python-Workflow bevorzugen und Python direkt installiert haben.

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
    Kopieren Sie diesen Befehl, um alle Pakete zu installieren:
    ```bash
    pip install pandas numpy sqlalchemy plotly scikit-learn python-docx pypdf pdfplumber reportlab
    ```

#### Option B: uv

Nutzen Sie diesen Weg für extrem schnelle Installationen. `uv` ist ein moderner Ersatz für pip/venv (geschrieben in Rust) und bereits vorinstalliert.

1.  **Terminal öffnen:** Öffnen Sie das Terminal in Ihrer IDE.
2.  **Venv erstellen:**
    ```bash
    uv venv
    ```
3.  **Aktivieren:**
      * Gleicher Schritt wie oben (Windows: `.venv\Scripts\activate`, Mac: `source .venv/bin/activate`).
4.  **Installation:**
    Nutzen Sie `uv pip`, um die Pakete in das erstellte venv zu laden:
    ```bash
    uv pip install pandas numpy sqlalchemy plotly scikit-learn python-docx pypdf pdfplumber reportlab
    ```

#### Option C: Anaconda

Nutzen Sie diesen Weg, wenn Sie die **Anaconda Distribution** oder Miniconda verwalten und bevorzugen.

1.  **Terminal öffnen:** Nutzen Sie den "Anaconda Prompt" (Windows) oder Ihr Terminal (Mac/Linux).
2.  **Environment erstellen:**
    Wir erstellen ein neues Environment namens `pybank` mit einer aktuellen Python-Version.
    ```bash
    conda create --name pybank python=3.11 -y
    ```
3.  **Aktivieren:**
    ```bash
    conda activate pybank
    ```
4.  **Installation:**
    Um sicherzustellen, dass wir exakt dieselben Paket-Versionen wie die anderen Teilnehmer nutzen (und um Probleme mit fehlenden Paketen in Conda-Channels zu vermeiden), nutzen wir `pip` innerhalb des Conda-Environments:
    ```bash
    pip install pandas numpy sqlalchemy plotly scikit-learn python-docx pypdf pdfplumber reportlab
    ```

-----

### Schritt 3: Verifikation

Stellen Sie sicher, dass Ihr Environment aktiviert ist (bei Conda sehen Sie `(pybank)` vor der Zeile), und führen Sie das Skript aus:

```bash
# Im Ordner /00-Setup
python check_env.py
```
