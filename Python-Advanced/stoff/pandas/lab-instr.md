# LAB DETAILS:

* **Lab Title/Topic:** Lab 13: Daten-Analyse mit Pandas
* **Learning Objectives:**
  * Students know how to do read data from a csv source
  * Students understand inpection, selection, basic filtering and analysis (groupby)
* **Context & Slide Summary:**
  * **DataFrame (2D):** Die primäre Datenstruktur. Eine Tabelle.
  * **Series (1D):** Eine einzelne Spalte.
  * **I/O:** `pd.read_csv()` (und andere) sind der Startpunkt.
  * **Inspektion:** `df.head()`, `df.info()`, `df.describe()` sind obligatorisch.
  * **Selektion:**
      * Spalten: `df[['Col_A', 'Col_B']]`
      * Zeilen: `.loc` (Label) oder `.iloc` (Position).
  * **Filtern (Evidenz):** Boolean Indexing (Masking) ist der Standard (`df[df['age'] > 30]`).
  * **Analyse (Kern):** `groupby()` (Split-Apply-Combine) ist das mächtigste Werkzeug zur Aggregation von Daten.


# ACTION:

Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Basis Aufgabe + Bonus Herausforderung, and two-file format).
Dont use emojis in the instructions. The heading for core task is "Angabe" and for bonus challenge its "Bonus-Herausforderung". Also create a csv with sample data