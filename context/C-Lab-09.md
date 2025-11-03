1.  **Das `re`-Modul:** Die primäre Schnittstelle in Python. Die wichtigsten Funktionen für Übungen sind:
    * `re.search(pattern, string)`: Findet das **erste** Vorkommen (irgendwo im String) und gibt ein **Match Object** (oder `None`) zurück. Dies ist die häufigste Funktion.
    * `re.findall(pattern, string)`: Findet **alle** Vorkommen und gibt eine **Liste von Strings** zurück.
    * `re.sub(pattern, replacement, string)`: Findet und ersetzt Vorkommen.

2.  **Raw Strings (WICHTIG):** Übungen sollten die Verwendung von **Raw Strings (`r"..."`)** erzwingen. Dies verhindert Konflikte zwischen Pythons Escape-Sequenzen (z.B. `\n`) und Regex-Metazeichen (z.B. `\d`).

3.  **Das Match Object:** Das Ergebnis von `re.search()`. Übungen müssen den korrekten Umgang damit prüfen:
    * Immer mit `if match:` prüfen (da das Ergebnis `None` sein kann).
    * `match.group(0)` (oder `match.group()`) liefert den **gesamten** gefundenen Text.

4.  **Metazeichen (Die Bausteine):**
    * **Zeichenklassen:** `\d` (Ziffer), `\w` (Wortzeichen), `\s` (Whitespace) und ihre Gegenteile (`\D`, `\W`, `\S`).
    * **Wildcard:** `.` (beliebiges Zeichen).
    * **Anker:** `^` (String-Anfang), `$` (String-Ende).
    * **Sets `[...]`:** Zum Definieren spezifischer Zeichenmengen (z.B. `[aeiou]`, `[a-zA-Z]`, `[^0-9]` für "nicht-Ziffer").

5.  **Quantifiers (Wie oft?):**
    * `+` (1 oder öfter)
    * `*` (0 oder öfter)
    * `?` (0 oder 1 Mal / optional)
    * `{n,m}` (Spezifische Anzahl, z.B. `\d{4}` für eine 4-stellige Zahl).

6.  **Gruppen `()` (Das WICHTIGSTE Konzept):**
    * Der primäre Zweck von Gruppen (Klammern) ist das **Extrahieren (Capturing)** von *Teilen* des Musters.
    * Übungen sollten das Extrahieren von Daten (z.B. Benutzername und Domain aus einer E-Mail) testen.
    * `match.group(1)` liefert den Text der ersten Klammer.
    * `match.group(2)` liefert den Text der zweiten Klammer.

7.  **Performance (Fortgeschritten):**
    * **`re.compile()`:** Übungen können das Kompilieren eines Musters vor einer Schleife demonstrieren, um Performance zu gewinnen (wenn das Muster oft wiederverwendet wird).
    * **`re.finditer()`:** Als speichereffiziente (lazy) Alternative zu `re.findall()`, da es einen Iterator über Match Objects statt einer vollen Liste zurückgibt.