import re

text = "Der Preis ist 100€."

# re.search() findet das ERSTE Vorkommen im gesamten String
# r"\d+" bedeutet "eine oder mehrere Ziffern (\d)"
match = re.search(r"\d+", text)

if match:
    print(f"Treffer gefunden: {match.group(0)}")
    # Output: Treffer gefunden: 100



text = "User: alice, ID: 123"
match = re.search(r"ID: \d+", text)

if match:
  # .group() oder .group(0): Der gesamte Text des Treffers
  print(f"Gefunden: {match.group()}")  # Output: Gefunden: ID: 123

  # .start() / .end(): Die Indizes im Originalstring
  print(f"Start-Index: {match.start()}")  # Output: Start-Index: 12
  print(f"End-Index: {match.end()}")  # Output: End-Index: 18





text = "Bestellung 45A von kunde_otto@mail.de"
pattern = r"(\w+)@([\w\.-]+)"  # (Name)@(Domain)

match = re.search(pattern, text)

if match:
  print(f"Gesamter Match: {match.group(0)}")  # 'kunde_otto@mail.de'

  # Gruppen-Zugriff (1-basiert)
  print(f"Username: {match.group(1)}")  # 'kunde_otto'
  print(f"Domain: {match.group(2)}")  # 'mail.de'

  print(f"Alle Gruppen: {match.groups()}")  # ('kunde_otto', 'mail.de')

# Best Practice für große Datenmengen
for match in re.finditer(r"ERROR: (.*)", logfile_content):
    # Es ist immer nur ein Match im Speicher
    print(f"Fehler gefunden: {match.group(1)}")

# Langsam:
for line in many_lines:
    # Regex wird 1000x neu kompiliert
    match = re.search(r"(\d{4}-\d{2}-\d{2})", line)


# Schnell:
date_pattern = re.compile(r"(\d{4}-\d{2}-\d{2})")

for line in many_lines:
    # 2. Das kompilierte Objekt wiederverwenden
    match = date_pattern.search(line)