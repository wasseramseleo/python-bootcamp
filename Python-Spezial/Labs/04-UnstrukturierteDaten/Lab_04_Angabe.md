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

### Teil 1: Basis Aufgabe

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

### Teil 2: Bonus Herausforderung

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
