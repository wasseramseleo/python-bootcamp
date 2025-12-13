# LAB 04 DETAILS:

* **Lab Title/Topic:** Unstrukturierte Daten
* **Learning Objectives:**
    * Textinhalte aus Word- und PDF-Dokumenten extrahieren.
    * Advanced: Tabellen aus PDFs extrahieren und automatisierte Word-Reports generieren.
* **Context & Slide Summary:** 
    - Libraries für Word (python-docx)
    - Libraries für PDF (pypdf o.ä.)

# ACTION:
Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).

-----

## `Lab_04_Angabe.md`

# Lab 04: Unstrukturierte Daten (Word & PDF)

### Szenario

Die Kreditabteilung erhält Anträge als Word-Dokumente und Kontoauszüge von Fremdbanken als PDF. Bisher wurden diese manuell abgetippt. Ihr Ziel ist es, den Namen des Antragstellers aus dem Word-Dokument und die Transaktionstabelle aus dem PDF automatisch zu extrahieren.

### Voraussetzungen

1.  **Libraries installieren:** Öffnen Sie Ihr Terminal/Command Prompt und installieren Sie:

    ```bash
    pip install python-docx pypdf pdfplumber reportlab
    ```

    *(Hinweis: `reportlab` benötigen wir nur, um das Test-PDF zu erstellen.)*

2.  **Test-Dateien generieren:**
    Führen Sie VOR Beginn des Labs bitte dieses Python-Skript einmalig aus, um die Dateien `antrag.docx` und `bank_statement.pdf` in Ihrem Ordner zu erzeugen:

    ```python
    # setup_lab04.py
    from docx import Document
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    # 1. Word Dokument erstellen
    doc = Document()
    doc.add_heading('Kreditantrag #2024-99', 0)
    doc.add_paragraph('Antragsteller: Max Mustermann')
    doc.add_paragraph('Kunde bittet um Kreditprüfung für Immobilienkauf.')
    doc.add_paragraph('Gewünschte Summe: 500.000 EUR')
    doc.save('antrag.docx')

    # 2. PDF mit Tabelle erstellen
    c = canvas.Canvas("bank_statement.pdf", pagesize=A4)
    c.drawString(100, 800, "Fremdbank Kontoauszug - 2024")
    c.drawString(100, 780, "Transaktionsübersicht:")
    # Einfache visuelle Tabelle (Text-basiert für pypdf, strukturiert für pdfplumber)
    y = 750
    data = [["Datum", "Beschreibung", "Betrag"],
            ["2024-01-01", "Gehalt", "3500.00"],
            ["2024-01-05", "Miete", "-1200.00"],
            ["2024-01-10", "Supermarkt", "-150.50"]]

    for row in data:
        line = f"{row[0]}   {row[1]}   {row[2]}"
        c.drawString(100, y, line)
        y -= 20
    c.save()
    print("Setup fertig: 'antrag.docx' und 'bank_statement.pdf' erstellt.")
    ```

-----

### Basis Aufgabe

Ziel ist das Extrahieren von reinem Text aus beiden Formaten.

**Anforderungen:**

1.  **Word lesen:**
      * Importieren Sie `Document` aus `docx`.
      * Öffnen Sie `antrag.docx`.
      * Iterieren Sie über alle Paragraphen (`doc.paragraphs`) und suchen Sie die Zeile, die mit "Antragsteller:" beginnt.
      * Geben Sie den Namen des Antragstellers auf der Konsole aus (z.B. "Gefundener Name: Max Mustermann").
2.  **PDF Text lesen:**
      * Importieren Sie `PdfReader` aus `pypdf`.
      * Laden Sie `bank_statement.pdf`.
      * Extrahieren Sie den Text der ersten Seite (`pages[0].extract_text()`).
      * Prüfen Sie mittels `if`, ob das Wort "Gehalt" im Text vorkommt, und geben Sie eine Erfolgsmeldung aus.

-----

### Bonus Herausforderung

Ziel ist die tabellarische Extraktion aus PDFs (oft sehr schwierig) und das automatische Schreiben eines Word-Reports.

**Anforderungen:**

1.  **PDF Tabelle parsen (pdfplumber):**
      * `pypdf` liefert nur "flachen" Text. Nutzen Sie `import pdfplumber`.
      * Öffnen Sie das PDF mit `pdfplumber.open(...)`.
      * Versuchen Sie, den Inhalt zeilenweise zu lesen. Da unser generiertes PDF sehr einfach ist, iterieren Sie über `page.extract_text().split('\n')`.
      * **Ziel:** Filtern Sie die Zeilen heraus, die ein Datum (Format YYYY-MM-DD) enthalten, und speichern Sie diese in einer Liste von Dictionaries (Keys: Date, Desc, Amount).
2.  **Word Report generieren:**
      * Erstellen Sie mit `python-docx` ein *neues* Word-Dokument `genehmigung.docx`.
      * Fügen Sie eine Überschrift "Kreditentscheidung" hinzu.
      * Fügen Sie einen Satz hinzu: "Basierend auf der Prüfung von [Name aus Teil 1] und dem Gehaltseingang wurde der Kredit genehmigt."
      * Speichern Sie das Dokument.

-----

## `Lab_04_Lösung.md`

# Lösung Lab 04

### Lösungsansatz

  * **Word (`python-docx`):** Die Bibliothek strukturiert Dokumente als Baum aus Paragraphen und "Runs" (Textstücke mit gleicher Formatierung). Für einfache Textsuche reicht die Iteration über `paragraphs`.
  * **PDF (`pypdf` vs `pdfplumber`):** PDFs sind layout-basiert, nicht struktur-basiert. `pypdf` ist gut für reinen Textdump. `pdfplumber` (oder spezialisierte Tools) sind nötig, um Tabellenstrukturen visuell zu erkennen. Im Bonus nutzen wir String-Parsing, da echte Tabellen-Erkennung in PDFs oft komplex ist.

-----

### Code: Basis Aufgabe

```python
from docx import Document
from pypdf import PdfReader

def analyze_documents():
    print("--- 1. Word Analyse ---")
    # Word Dokument laden
    try:
        doc = Document('antrag.docx')
        applicant_name = "Unbekannt"
        
        for para in doc.paragraphs:
            text = para.text
            # Einfaches String-Parsing
            if text.startswith("Antragsteller:"):
                # Split am Doppelpunkt und Whitespace entfernen
                applicant_name = text.split(":")[1].strip()
                print(f"Gefundener Name: {applicant_name}")
                
    except Exception as e:
        print(f"Fehler beim Lesen von Word: {e}")

    print("\n--- 2. PDF Analyse ---")
    # PDF laden
    try:
        reader = PdfReader("bank_statement.pdf")
        page = reader.pages[0]
        pdf_text = page.extract_text()
        
        # Auf Konsole ausgeben zur Kontrolle
        # print(pdf_text) 
        
        if "Gehalt" in pdf_text:
            print("BONITÄTS-CHECK: Gehaltseingang gefunden ✅")
        else:
            print("BONITÄTS-CHECK: Warnung - Kein Gehalt gefunden ❌")

if __name__ == "__main__":
    analyze_documents()
```

-----

### Code: Bonus Herausforderung

```python
import pdfplumber
from docx import Document
import re

def advanced_processing():
    # Daten-Container
    extracted_transactions = []
    applicant_name = "Max Mustermann" # Annahme aus Teil 1, oder erneut auslesen

    print("--- Bonus: PDF Table Parsing ---")
    
    with pdfplumber.open("bank_statement.pdf") as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        
        # Wir parsen den Text Zeile für Zeile
        lines = text.split('\n')
        
        for line in lines:
            # Suche nach Zeilen, die mit einem Datum starten (Simple Regex)
            # Format: 2024-xx-xx
            if re.match(r'\d{4}-\d{2}-\d{2}', line):
                parts = line.split() # Split bei Leerzeichen
                # Vorsicht: Das ist brüchig und hängt vom PDF Layout ab!
                # parts[0] = Datum, parts[1] = Text, parts[2] = Betrag
                if len(parts) >= 3:
                    tx = {
                        "date": parts[0], 
                        "desc": parts[1], 
                        "amount": parts[-1]
                    }
                    extracted_transactions.append(tx)

    print(f"Extrahierte Transaktionen: {len(extracted_transactions)}")
    for tx in extracted_transactions:
        print(tx)

    print("\n--- Bonus: Word Report Generierung ---")
    
    report = Document()
    report.add_heading('Kreditentscheidung', 0)
    
    # Text zusammenbauen
    p = report.add_paragraph('Basierend auf der Prüfung von ')
    p.add_run(applicant_name).bold = True
    p.add_run(' und den folgenden Transaktionen:')
    
    # Tabelle im Word erstellen
    table = report.add_table(rows=1, cols=3)
    # Header
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Datum'
    hdr_cells[1].text = 'Beschreibung'
    hdr_cells[2].text = 'Betrag'
    
    # Daten füllen
    for tx in extracted_transactions:
        row_cells = table.add_row().cells
        row_cells[0].text = tx["date"]
        row_cells[1].text = tx["desc"]
        row_cells[2].text = tx["amount"]

    report.add_paragraph('\nEntscheidung: GENEHMIGT')
    
    report.save('genehmigung.docx')
    print("Report 'genehmigung.docx' wurde erstellt.")

if __name__ == "__main__":
    advanced_processing()
```
