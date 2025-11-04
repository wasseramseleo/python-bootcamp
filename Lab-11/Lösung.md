# Lab 11: DocStrings & Dokumentation - Lösung

## Erläuterung der Lösung

### Angabe & Bonus

Die Lösung implementiert den **Google Style** für Docstrings. Dieser Stil wird von vielen Tools (IDEs, Sphinx) bevorzugt, da er durch Sektionen wie `Args:`, `Returns:` und `Raises:` maschinenlesbar ist.

1.  **Unterschied (Kommentar vs. Docstring):**

      * Ein Kommentar (`#`) erklärt *wie* oder *warum* der Code etwas tut (z.B. `# Prüfen, ob Saldo ausreicht`). Er ist für Entwickler, die den Code lesen.
      * Ein Docstring (`"""..."""`) erklärt *was* der Code tut (z.B. "Hebt Geld ab."). Er ist für Benutzer (Consumer) der Funktion/Klasse und für Tools.

2.  **Struktur (Angabe):**

      * **`__init__`**: Der Docstring beschreibt jeden Parameter unter `Args:`. IDEs verwenden dies, um beim Tippen von `BankAccount(...)` Hilfe anzuzeigen.
      * **`withdraw`**: Dies ist das vollständigste Beispiel:
          * `Args:` Beschreibt die Eingabe.
          * `Returns:` Beschreibt die Ausgabe (das `bool`).
          * `Raises:` Beschreibt den `ValueError`, den wir hinzugefügt haben. Eine IDE warnt den Benutzer nun, dass diese Funktion einen `ValueError` auslösen kann und er ihn mit `try...except` behandeln sollte.

3.  **Struktur (Bonus):**

      * **Modul-Docstring (Zeile 1):** Muss die *allererste* Zeile in der Datei sein. Dient als Übersicht für das gesamte Modul.
      * **Klassen-Docstring (unter `class BankAccount`):** Beschreibt den Zweck der Klasse. Die `Attributes:`-Sektion listet die öffentlichen Instanzvariablen auf, die ein Benutzer sicher abfragen kann (z.B. `acc.owner`).
      * **`help()`**: Der `help()`-Aufruf demonstriert, *warum* wir das tun. Python parst diese Docstrings und generiert eine saubere, lesbare Dokumentationsseite.

## Python-Code: Vollständige Lösung (Angabe & Bonus)

```python
"""
Modul: bank_account

Dies ist der Modul-Docstring (Bonus-Aufgabe).
Er enthält die Kerndatenmodelle für die Banking-App, 
insbesondere die BankAccount-Klasse.
"""

import time

class BankAccount:
    """
    Repräsentiert ein einzelnes Bankkonto eines Kunden (Bonus-Aufgabe).

    Dies ist der Klassen-Docstring. Er erklärt den Zweck der Klasse.
    IDEs wie VS Code zeigen dies als Tooltip an, wenn man über
    den Klassennamen 'BankAccount' hovert.

    Attributes:
        owner (str): Der vollständige Name des Kontoinhabers.
        account_number (str): Die eindeutige Kontonummer.
        _balance (float): Der private Kontostand.
    """

    def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0) -> None:
        """
        Initialisiert eine neue Instanz eines BankAccount (Angabe 4).

        Args:
            owner (str): Der vollständige Name des Kontoinhabers.
            account_number (str): Die eindeutige Kontonummer.
            initial_balance (float, optional): Der Startsaldo des Kontos. 
                Standardwert ist 0.0.
        """
        self.owner = owner
        self.account_number = account_number
        self._balance = initial_balance
        
        # Ein normaler Kommentar (wird von 'help()' ignoriert)
        # Wir validieren den initial_balance hier zur Vereinfachung nicht.

    def deposit(self, amount: float) -> bool:
        """
        Zahlt einen positiven Betrag auf das Konto ein.
        (Dies ist ein simpler, einzeiliger Docstring)
        """
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """Hebt einen Betrag vom Konto ab, falls gedeckt (Angabe 3).

        Diese Methode prüft, ob der Betrag positiv ist und ob
        ausreichend Deckung auf dem Konto vorhanden ist.

        Args:
            amount (float): Der Betrag, der abgehoben werden soll. 
                Muss positiv sein.

        Returns:
            bool: True, wenn die Abhebung erfolgreich war (d.h. Deckung
                war ausreichend). False, wenn die Deckung nicht ausreichte.

        Raises:
            ValueError: Wenn der angegebene 'amount' 0 oder negativ ist 
                (Angabe 2).
        """
        
        # Aufgabe 2: Logik-Anpassung und 'Raises'
        if amount <= 0:
            raise ValueError("Abhebungsbetrag muss positiv sein.")
            
        if self._balance >= amount:
            self._balance -= amount
            return True
        else:
            # Nicht genügend Deckung
            return False

    def get_balance(self) -> float:
        """Gibt den aktuellen Kontostand zurück."""
        return self._balance


# --- Bonus-Aufgabe 3: Überprüfung mit help() ---

print("--- Bonus: Ausgabe von help(BankAccount.withdraw) ---")
# help() liest den Docstring und formatiert ihn:
help(BankAccount.withdraw)

print("\n--- Bonus: Ausgabe von help(BankAccount) ---")
# help() auf der Klasse fasst ALLE Docstrings zusammen:
help(BankAccount)
```