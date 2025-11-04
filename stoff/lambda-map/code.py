# Datei-Handler in Python sind Iteratoren
with open("massive_log_file.log", "r") as f:
  # 'f' ist ein Iterator.
  # 'f.readline()' (oder __next__) wird bei jedem Schleifendurchlauf aufgerufen.

  for line in f:
    # Es ist immer nur EINE Zeile gleichzeitig im Speicher!
    process(line)

# Ergebnis: Verarbeitung einer 100 GB Datei mit < 1 MB RAM.