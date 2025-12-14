# Lab 04: Unstrukturierte Daten (Word & PDF)

### Szenario
Die Kreditabteilung erhält Anträge als Word-Dokumente und Kontoauszüge von Fremdbanken als PDF. Bisher wurden diese manuell abgetippt. Ihr Ziel ist es, den Namen des Antragstellers aus dem Word-Dokument und die Transaktionstabelle aus dem PDF automatisch zu extrahieren und in einem neuen Report zusammenzufassen.

### Voraussetzungen
* Bibliotheken: `python-docx`, `pypdf`, `pdfplumber` (installiert via `pip`).
* Dateien: `antrag.docx` und `bank_statement.pdf` (werden im Setup-Code erstellt).

---

### Basis Aufgabe (Text Extraktion)

Ziel ist das Extrahieren von Information aus unstrukturiertem Text, analog zur Extraktion der Vogelarten im Theorie-Block.

**Anforderungen:**

1.  **Word lesen (Antragsteller finden):**
    * Importieren Sie `Document` aus `docx`.
    * Öffnen Sie `antrag.docx`.
    * Iterieren Sie über alle Paragraphen (`doc.paragraphs`).
    * Suchen Sie den Paragraphen, der den Text "Antragsteller:" enthält.
    * Extrahieren und bereinigen Sie den Namen (alles nach dem Doppelpunkt).

2.  **PDF lesen (Keywords checken):**
    * Importieren Sie `PdfReader` aus `pypdf`.
    * Laden Sie `bank_statement.pdf`.
    * Extrahieren Sie den Rohtext der ersten Seite.
    * Prüfen Sie, ob das kritische Keyword "Gehalt" (Salary) im Text vorkommt und geben Sie das Ergebnis auf der Konsole aus.

---

### Bonus Herausforderung (Tabellen & Reporting)

Ziel ist die strukturierte Extraktion von Tabellendaten aus PDFs und das Generieren eines formatierten Word-Reports mit Tabelle (wie im "Annual Ringing Report" Beispiel).

**Anforderungen:**

1.  **PDF Tabelle parsen (pdfplumber):**
    * Nutzen Sie `pdfplumber`, um die Struktur der PDF-Seite zu lesen.
    * Verwenden Sie `page.extract_table()` (gibt eine Liste von Listen zurück), wie in den Folien gezeigt.
    * Iterieren Sie über die Zeilen. Filtern Sie die Header-Zeile ("Date") und leere Zeilen heraus.
    * Speichern Sie alle Zeilen, die eine "Gutschrift" (Credit) oder "Gehalt" beinhalten, in einer Liste `salary_data`.

2.  **Word Report generieren:**
    * Erstellen Sie ein neues `Document`.
    * Fügen Sie eine Überschrift "Kredit-Prüfbericht" hinzu.
    * **Tabelle erstellen:** Erstellen Sie eine Word-Tabelle (`add_table`) mit den gefundenen Gehaltsdaten.
    * Setzen Sie die Header der Tabelle manuell (z.B. "Datum", "Beschreibung", "Betrag").
    * Befüllen Sie die Tabelle mittels Loop mit den Daten aus Schritt 1.
    * Speichern Sie das Ergebnis als `report_genehmigung.docx`.
```
