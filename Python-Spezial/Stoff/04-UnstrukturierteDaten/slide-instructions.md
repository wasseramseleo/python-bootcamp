**Input Data:**

* **Topic Title:** 4. Unstrukturierte Daten (Docs)
* **Content Points:**
    - Libraries für Word (python-docx)
    - Libraries für PDF (pypdf o.ä.)
* **Lab Objectives:**
    * Textinhalte aus Word- und PDF-Dokumenten extrahieren.
    * Advanced: Tabellen aus PDFs extrahieren und automatisierte Word-Reports generieren.

-----

Here are the slides for **Topic 4: Unstrukturierte Daten (Docs)**.

-----

**Slide 1: Word-Automatisierung (python-docx)**

**Body Text (German):**

  * **Struktur:** `.docx` Dateien sind technisch gesehen gezippte XML-Dateien. Die Library `python-docx` abstrahiert dies in `Document`, `Paragraph` und `Run` Objekte.
  * **Reading:** Zugriff erfolgt meist iterativ über alle Paragraphen. Formatierungen (Fett, Kursiv) sind in sogenannten "Runs" gespeichert.
  * **Anwendung:** Ideal zum Auslesen von standardisierten Protokollen, die von Freiwilligen als Word-Datei eingereicht wurden.

**Code Snippet (Python):**

```python
from docx import Document

# Load the field report
doc = Document('ringing_protocol_2024.docx')

full_text = []
for para in doc.paragraphs:
    # Extract only text, ignore style for now
    if "Species:" in para.text:
        full_text.append(para.text)

print(f"Extracted {len(full_text)} lines.")
```

**Speaker Notes (German):**
Wir beginnen mit Word. `python-docx` ist der Standard. Wichtig zu verstehen: Ein Word-Dokument ist eine Hierarchie. Ein `Document` enthält `Paragraphs`, und diese enthalten `Runs` (Textstücke mit gleicher Formatierung). Wenn Sie nur den reinen Text wollen, iterieren Sie über `doc.paragraphs`. Das ist robust genug, um Daten aus manuell ausgefüllten Berichten zu kratzen.

**Image Prompt:** A diagram showing the hierarchy of a Word document: Document -\> Paragraphs -\> Runs -\> Text, illustrating how the library parses the file.

-----

**Slide 2: Word-Reports Generieren**

**Body Text (German):**

  * **Writing:** `python-docx` kann neue Dokumente erstellen, Bilder einfügen und Tabellen generieren.
  * **Templating:** Für komplexe Layouts ist es effizienter, ein "Template-Dokument" zu laden (mit Kopfzeilen/Logos) und nur den Inhalt dynamisch zu ergänzen.
  * **Business Value:** Automatisierte Erstellung von behördlichen Beringungsberichten ("Ring Fund Report") auf Knopfdruck.

**Code Snippet (Python):**

```python
from docx import Document

doc = Document() # Creates new blank doc
doc.add_heading('Annual Ringing Report', 0)

# Add a table with data
data = [('A12', 'Blue Tit'), ('B99', 'Robin')]
table = doc.add_table(rows=1, cols=2)

# Set header
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Ring ID'
hdr_cells[1].text = 'Species'

# Fill rows
for ring_id, species in data:
    row_cells = table.add_row().cells
    row_cells[0].text = ring_id
    row_cells[1].text = species

doc.save('report_output.docx')
```

**Speaker Notes (German):**
Daten lesen ist gut, Berichte schreiben ist besser. Statt Copy-Paste in Word zu machen, generieren wir den jährlichen Behördenbericht per Skript. Im Code sehen Sie, wie wir eine Tabelle dynamisch aufbauen. Profi-Tipp: Erstellen Sie ein leeres Word-Doc mit Ihrem Firmenlogo und laden Sie dieses als Basis (`Document('template.docx')`), statt das Layout im Code zu bauen.

**Image Prompt:** An automated assembly line where raw data enters on one side and perfectly formatted, stamped paper documents exit on the other.

-----

**Slide 3: PDF Text Extraktion (pypdf)**

**Body Text (German):**

  * **Die Herausforderung:** PDF ist ein Layout-Format, kein Daten-Format. Es gibt keine logische Struktur wie "Absätze" oder "Tabellen", nur Buchstaben an Koordinaten.
  * **pypdf:** Eine robuste Library zum Lesen, Splitten und Mergen von PDFs.
  * **Text Extraction:** `extract_text()` versucht, den visuellen Textfluss in einen String zu rekonstruieren. Das Ergebnis ist oft unstrukturiert (Header vermischen sich mit Content).

**Code Snippet (Python):**

```python
from pypdf import PdfReader

reader = PdfReader("scientific_paper_v1.pdf")
page = reader.pages[0]

# Extract text content
raw_text = page.extract_text()

# Basic filtering
if "Parus major" in raw_text:
    print("Found mention of Great Tit on page 1")
```

**Speaker Notes (German):**
PDFs sind schwieriger. Ein PDF weiß nicht, was ein Satz ist; es weiß nur, dass ein Buchstabe an Position X,Y steht. `pypdf` leistet gute Arbeit beim Extrahieren von reinem Text, z.B. wenn Sie nach Keywords in wissenschaftlichen Papers suchen. Erwarten Sie aber keine perfekte Formatierung – Tabellen werden oft zu Buchstabensalat.

**Image Prompt:** A visual metaphor showing a neatly laid out newspaper (PDF) being put through a shredder, resulting in a pile of text strips (extracted string) where structure is lost but content remains.

-----

**Slide 4: Tabellen aus PDFs (Advanced Track)**

**Body Text (German):**

  * **Problem:** `pypdf` scheitert oft an Tabellenlayouts.
  * **Lösung (`pdfplumber`):** Eine spezialisierte Library, die Linien und Abstände im PDF analysiert, um Tabellenstrukturen visuell zu erkennen.
  * **Visual Debugging:** `pdfplumber` erlaubt es, die erkannten Bounding-Boxes grafisch darzustellen, um die Extraktionslogik zu verfeinern.

**Code Snippet (Python):**

```python
import pdfplumber

# Opening a PDF containing morphometric tables
with pdfplumber.open("data_sheet.pdf") as pdf:
    first_page = pdf.pages[0]
    
    # Extract table structure
    # Returns a list of lists (rows/columns)
    table_data = first_page.extract_table()

    for row in table_data:
        # Filter out None values or empty rows
        if row and row[0] != "Date":
            print(f"Date: {row[0]}, Count: {row[1]}")
```

**Speaker Notes (German):**
Für die Experten: Wenn Sie Tabellen aus PDFs brauchen, nehmen Sie `pdfplumber`. Es ist langsamer als `pypdf`, aber viel präziser. Es "sieht" die Linien im Dokument und rekonstruiert die Zellen. Das ist der einzige verlässliche Weg, um z.B. Fangstatistiken aus alten PDF-Scans zu retten, ohne OCR zu nutzen.

**Image Prompt:** A digital overlay on a PDF document highlighting table rows and columns with neon bounding boxes, visualizing how the software identifies grid structures.

-----

**Slide 5: Lab Preparation**

**Body Text (German):**

  * **Szenario:** Ein "Legacy Data Rescue" Projekt. Alte Bestandsdaten liegen nur als PDF und Word vor.
  * **Aufgabe 1 (Word):** Lesen Sie ein Beringungs-Protokoll (.docx) ein und extrahieren Sie den Namen des Beobachters (z.B. Zeile startend mit "Observer:").
  * **Aufgabe 2 (PDF):** Nutzen Sie `pypdf`, um den reinen Text eines Reports zu extrahieren und zählen Sie, wie oft die Spezies "Parus major" vorkommt.
  * **Aufgabe 3 (Advanced - Report):**
      * Extrahieren Sie eine Tabelle aus einem PDF (`pdfplumber`).
      * Generieren Sie basierend darauf eine *neue* Word-Datei (`python-docx`), die diese Daten als sauber formatierte Tabelle enthält.

**Code Snippet (Python):**

```python
# Lab Workflow Hint
# 1. Read PDF
import pdfplumber
data = []
with pdfplumber.open("source.pdf") as pdf:
    data = pdf.pages[0].extract_table()

# 2. Write Word
from docx import Document
doc = Document()
# ... loop over data and fill doc.add_table()
```

**Speaker Notes (German):**
Wir spielen Daten-Archäologie. Die Einsteiger konzentrieren sich auf das Finden von Strings in Word-Dateien. Die Fortgeschrittenen bauen eine Konvertierungs-Pipeline: Daten aus PDF-Tabellen befreien und in ein sauberes Word-Dokument überführen. Das ist eine sehr häufige Anforderung in Unternehmen, um "tote Daten" wieder nutzbar zu machen.

**Image Prompt:** A split screen: Left side shows a dusty stack of PDF/Paper files, right side shows a clean, modern Word document icon being generated via a Python script connection.
