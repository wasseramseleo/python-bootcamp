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
    print("SUCCESS: Ihr System ist bereit für den Kurs!")
else:
    print("FAIL: Bitte überprüfen Sie die Installation.")