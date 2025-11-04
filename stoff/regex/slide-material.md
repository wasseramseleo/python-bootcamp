Hier sind die Inhalte für die Slides zum Thema Regular Expressions.

-----

## Folie 1: Titel

**Titel:** Regular Expressions (Regex)
**Untertitel:** Die "Mini-Sprache" zur Mustererkennung in Texten

-----

## Folie 2: Das Problem: Grenzen von String-Methoden

**Titel:** Das Problem: Warum `str.find()` nicht ausreicht

String-Methoden sind schnell, aber limitiert. Sie suchen nach **literalem** Text.

**Die Herausforderung (Beispiele):**

  * Wie findet man "Error 404" ODER "Error 500"?
  * Wie extrahiert man *jede* E-Mail-Adresse aus einem Text?
  * Wie validiert man eine Telefonnummer, die `(123) 456-7890` oder `123-456-7890` sein könnte?

**Kritik (Evidence):**
Methoden wie `.find()`, `.startswith()` oder `.endswith()` versagen, sobald der zu findende Text einem **Muster** (Pattern) folgt, statt exakt gleich zu sein.

-----

## Folie 3: Die Lösung: Das `re`-Modul

**Titel:** Das `re`-Modul & Raw Strings

**Definition:**
Eine "Regular Expression" (Regex) ist eine Sequenz von Zeichen, die ein Suchmuster definiert. Python stellt dafür das `re`-Modul bereit.

**WICHTIG (Best Practice): Raw Strings `r""`**
Verwenden Sie **IMMER** Raw Strings (`r"..."`) für Regex-Pattern.

**Warum?**
Regex verwendet Backslashes (`\`) für spezielle Sequenzen (z.B. `\d` für Ziffer). Python-Strings verwenden `\` ebenfalls (z.B. `\n` für Zeilenumbruch).

  * Normaler String: `"\\d"` (Man muss den Backslash "escapen")
  * Raw String: `r"\d"` (Python interpretiert den Backslash nicht)

<!-- end list -->

```python
import re

text = "Der Preis ist 100€."

# re.search() findet das ERSTE Vorkommen im gesamten String
# r"\d+" bedeutet "eine oder mehrere Ziffern (\d)"
match = re.search(r"\d+", text)

if match:
    print(f"Treffer gefunden: {match.group(0)}")
    # Output: Treffer gefunden: 100
```

-----

## Folie 4: Die Kernfunktionen des `re`-Moduls

**Titel:** Die wichtigsten `re`-Funktionen

  * `re.search(pattern, string)`

      * Sucht nach dem **ersten** Vorkommen des Musters *irgendwo* im String.
      * Gibt ein **Match Object** zurück (oder `None`).

  * `re.match(pattern, string)`

      * Sucht nach dem Muster **nur am Anfang** des Strings.
      * (Achtung: Häufige Fehlerquelle\! Meistens will man `re.search()`).

  * `re.findall(pattern, string)`

      * Findet **alle** Vorkommen (die nicht überlappen).
      * Gibt eine **Liste von Strings** zurück.

  * `re.sub(pattern, replacement, string)`

      * Sucht alle Vorkommen und **ersetzt** sie.

-----

## Folie 5: Das Match Object

**Titel:** Das Match Object (Das Ergebnis von `search`)

Wenn `re.search()` (oder `match`) erfolgreich ist, erhalten Sie ein **Match Object**. Dies ist der Beweis und enthält alle Details zum Treffer.

```python
text = "User: alice, ID: 123"
match = re.search(r"ID: \d+", text)

if match:
    # .group() oder .group(0): Der gesamte Text des Treffers
    print(f"Gefunden: {match.group()}") # Output: Gefunden: ID: 123
    
    # .start() / .end(): Die Indizes im Originalstring
    print(f"Start-Index: {match.start()}") # Output: Start-Index: 12
    print(f"End-Index: {match.end()}")   # Output: End-Index: 18
```

**Kritik (Evidence):** `re.search()` gibt `None` zurück, wenn nichts gefunden wird. Prüfen Sie das Ergebnis **immer** mit `if match:`, bevor Sie `.group()` aufrufen, sonst riskieren Sie einen `AttributeError`.

-----

## Folie 6: Regex-Basissyntax (Metacharacters)

**Titel:** Wichtige Metacharactere (Die Bausteine)

| Zeichen          | Bedeutung                                                  | Beispiel                               |
|:-----------------|:-----------------------------------------------------------|:---------------------------------------|
| `.`              | Jedes Zeichen (außer Zeilenumbruch)                        | `r"h.t"` passt auf "hot", "hat", "h t" |
| `\d`             | Ziffer (Digit) `[0-9]`                                     | `r"\d\d"` passt auf "12", "99"         |
| `\w`             | "Wort"-Zeichen (Alphanumerisch + `_`)                      | `r"\w+"` passt auf "Python\_3"         |
| `\s`             | "Whitespace" (Leerzeichen, Tab, `\n`)                      | `r"Preis\s+\d"` passt auf "Preis 100"  |
| `\D`, `\W`, `\S` | Das Gegenteil (Nicht-Ziffer, Nicht-Wort, Nicht-Whitespace) | `r"\D+"` passt auf "Hallo\!"           |
| `^`              | Anfang des Strings                                         | `r"^Hallo"`                            |
| `$`              | Ende des Strings                                           | `r"Welt$"`                             |

-----

## Folie 7: Regex-Basissyntax (Quantifiers & Sets)

**Titel:** Quantifiers (Wie oft?) & Sets (Welche?)

**Quantifiers (Wie oft?):**

  * `*` : 0 oder öfter
  * `+` : 1 oder öfter
  * `?` : 0 oder 1 Mal (optional)
  * `{n}` : Genau *n* Mal (z.B. `\d{4}` für 4 Ziffern)
  * `{n,m}` : Mindestens *n*, maximal *m* Mal

**Character Sets `[...]` (Welche Zeichen?):**

  * `[abc]` : Entweder 'a', 'b' oder 'c'
  * `[a-z]` : Irgendein Kleinbuchstabe (Range)
  * `[a-zA-Z0-9]` : Alphanumerisch
  * `[^abc]` : Jedes Zeichen **außer** 'a', 'b', 'c' (Negation mit `^`)

**Beispiel:**
`r"Error [45]\d{2}"` passt auf "Error 404", "Error 451", "Error 500", "Error 503", aber nicht "Error 601".

-----

## Folie 8: Das Wichtigste: Gruppen `()` zur Extraktion

**Titel:** Gruppen `()` zur Datenextraktion

**Zweck:** Regex wird erst durch Gruppen (`()`) mächtig. Sie erlauben das **Extrahieren** von *Teilen* des Musters.

```python
text = "Bestellung 45A von kunde_otto@mail.de"
pattern = r"(\w+)@([\w\.-]+)" # (Name)@(Domain)

match = re.search(pattern, text)

if match:
    print(f"Gesamter Match: {match.group(0)}") # 'kunde_otto@mail.de'
    
    # Gruppen-Zugriff (1-basiert)
    print(f"Username: {match.group(1)}") # 'kunde_otto'
    print(f"Domain: {match.group(2)}") # 'mail.de'
    
    print(f"Alle Gruppen: {match.groups()}") # ('kunde_otto', 'mail.de')
```

**Kernaussage:** `match.group(0)` ist der gesamte Treffer. `match.group(1)` ist die erste `(`-Klammer.

-----

## Folie 9: Performance I: `re.findall()` vs. `re.finditer()`

**Titel:** Effizienz bei vielen Treffern

  * `re.findall(pattern, string)`

      * Sucht *alles* und gibt eine **Liste von Strings** zurück.
      * `r"(\d+)"` auf `"1 2 3"` -\> `['1', '2', '3']`
      * **Problem (Evidence):** Materialisiert alle Treffer sofort im Speicher. Ein Speicherfresser (Memory Hog) bei großen Dateien (z.B. Logfiles).

  * `re.finditer(pattern, string)`

      * Gibt einen **Iterator** über **Match Objects** zurück.
      * **Vorteil (Evidence):** "Lazy Evaluation". Verarbeitet Treffer nacheinander. (Bindet an Lektion über Iteratoren/Generatoren an).

<!-- end list -->

```python
# Best Practice für große Datenmengen
for match in re.finditer(r"ERROR: (.*)", logfile_content):
    # Es ist immer nur ein Match im Speicher
    print(f"Fehler gefunden: {match.group(1)}")
```

-----

## Folie 10: Performance II: `re.compile()`

**Titel:** Effizienz bei wiederholter Nutzung

**Problem:** Wenn Sie ein Regex-Pattern in einer Schleife verwenden, muss Python das Pattern *jedes Mal neu parsen und kompilieren*.

```python
# SCHLECHT (langsam):
for line in many_lines:
    # Regex wird 1000x neu kompiliert
    match = re.search(r"(\d{4}-\d{2}-\d{2})", line)
```

**Lösung (Best Practice): `re.compile()`**
Kompilieren Sie das Pattern *einmal* vor der Schleife.

```python
# GUT (schnell):
# 1. Einmal kompilieren
date_pattern = re.compile(r"(\d{4}-\d{2}-\d{2})")

for line in many_lines:
    # 2. Das kompilierte Objekt wiederverwenden
    match = date_pattern.search(line)
```

**Kritik (Evidence):** `re.compile()` ist essenziell für Performance, wenn dasselbe Pattern häufig auf unterschiedliche Strings angewendet wird (z.B. Parser, Linter, Log-Analyse).