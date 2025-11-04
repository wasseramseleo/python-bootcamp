# Lab 11: DocStrings & Dokumentation

## Lernziele

In diesem Lab lernen Sie, wie man Python-Code professionell dokumentiert, sodass er von Menschen und Werkzeugen (wie IDEs oder Sphinx) gleichermaßen verstanden wird.

  * Den Unterschied zwischen Kommentaren (`#`) und Docstrings (`"""..."""`) verstehen.
  * Docstrings an der korrekten Stelle (Modul, Klasse, Funktion) platzieren.
  * Strukturierte Docstrings (Google Style) schreiben, um Argumente, Rückgabewerte und Fehler zu beschreiben.
  * Verstehen, wie Tools (z.B. `help()` oder IDE-Tooltips) diese Docstrings nutzen.

## Szenario

Wir verwenden die `BankAccount`-Klasse aus den vorherigen Labs. Ein neuer Entwickler wurde dem Team hinzugefügt, aber er kann die Klasse nicht effektiv nutzen. Wenn er in seiner IDE über `account.withdraw(...)` fährt, erhält er keine Hilfe. Er weiß nicht, welche Argumente erwartet werden, was die Methode zurückgibt oder welche Fehler sie auslösen kann.

Ihre Aufgabe ist es, die Klasse mit professionellen Docstrings nachzurüsten, um die "Developer Experience" (DX) zu verbessern.

### Angabe

**Ziel:** Fügen Sie den Kernmethoden der `BankAccount`-Klasse strukturierte Google Style Docstrings hinzu.

1.  **Vorbereitung:** Starten Sie mit der folgenden Kopiervorlage.
2.  **`withdraw`-Methode anpassen:**
      * Modifizieren Sie die `withdraw`-Methode. Sie soll nicht mehr `False` zurückgeben, wenn der Betrag ungültig ist (z.B. negativ). Stattdessen soll sie in diesem Fall einen `ValueError` auslösen (z.B. `raise ValueError("Abhebungsbetrag muss positiv sein.")`).
3.  **`withdraw`-Methode dokumentieren:**
      * Fügen Sie der `withdraw`-Methode einen vollständigen **Google Style Docstring** hinzu.
      * Der Docstring muss die folgenden Sektionen enthalten:
          * Eine Kurzbeschreibung (z.B. "Hebt einen Betrag vom Konto ab, falls gedeckt.").
          * `Args:` (Sollte `amount (float)` beschreiben).
          * `Returns:` (Sollte das `bool` beschreiben, das angibt, ob die Abhebung erfolgreich war).
          * `Raises:` (Sollte den `ValueError` beschreiben, den Sie in Schritt 2 hinzugefügt haben).
4.  **`__init__`-Methode dokumentieren:**
      * Fügen Sie der `__init__`-Methode einen Google Style Docstring hinzu.
      * Er muss die Sektion `Args:` enthalten und die Parameter `owner`, `account_number` und `initial_balance` beschreiben.

**Kopiervorlage (bitte vervollständigen):**

```python
# (Hier fehlt der Modul-Docstring - Bonus)

class BankAccount:
    # (Hier fehlt der Klassen-Docstring - Bonus)

    def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0) -> None:
        # TODO: Fügen Sie hier den __init__ Docstring ein (Aufgabe 4)
        
        self.owner = owner
        self.account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount: float) -> bool:
        """Eine einfache, einzeilige Docstring-Demo."""
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        # TODO: Fügen Sie hier den Docstring ein (Aufgabe 3)
        
        # TODO: Passen Sie die Logik an (Aufgabe 2)
        if amount <= 0:
            # Sollte einen Fehler auslösen
            print("Fehler: Betrag ungültig.")
            return False
            
        if self._balance >= amount:
            self._balance -= amount
            return True
        else:
            # Nicht genügend Deckung
            return False

    def get_balance(self) -> float:
        """Gibt den aktuellen Kontostand zurück."""
        return self._balance

```

-----

### Bonus-Herausforderung

**Ziel:** Fügen Sie Dokumentation auf Modul- und Klassenebene hinzu und überprüfen Sie Ihre Arbeit mit `help()`.

1.  **Modul-Docstring:**
      * Fügen Sie ganz oben in der Datei (vor allen `import`-Anweisungen oder Code) einen Modul-Docstring (`"""..."""`) hinzu.
      * Er soll beschreiben, was die *gesamte Datei* (das Modul) enthält (z.B. "Kern-Datenmodell für die Banking-App.").
2.  **Klassen-Docstring:**
      * Fügen Sie direkt unter der Zeile `class BankAccount:` einen Docstring hinzu.
      * Er soll beschreiben, was die Klasse *repräsentiert* (z.B. "Repräsentiert ein einzelnes Bankkonto...").
      * Fügen Sie auch eine `Attributes:`-Sektion hinzu, die die öffentlichen Attribute (z.B. `owner`) beschreibt.
3.  **Überprüfung:**
      * Importieren Sie Ihre Klasse in einer Python-Konsole (oder am Ende Ihres Skripts).
      * Führen Sie `help(BankAccount)` aus. Beobachten Sie, wie Python Ihre Modul-, Klassen- und Methoden-Docstrings zu einer Hilfeseite zusammenfügt.
      * Führen Sie `help(BankAccount.withdraw)` aus, um gezielt die Dokumentation Ihrer modifizierten Methode anzuzeigen.
