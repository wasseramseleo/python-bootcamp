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
    except Exception as e:
        print(f"Fehler beim Lesen von Word: {e}")

if __name__ == "__main__":
    analyze_documents()
