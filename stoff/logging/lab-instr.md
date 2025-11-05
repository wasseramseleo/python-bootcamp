# LAB DETAILS:

* **Lab Title/Topic:** Lab 14: Logging
* **Learning Objectives:**
  * Students know how to log in large scale projects
  * Students understand getLogger, exception logging
* **Context & Slide Summary:**

* **Problem:** `print()` ist für die Produktion ungeeignet. Es bietet keine Level-Steuerung, keinen Kontext (Zeit, Modul) und ist blockierend.

* **Regel 1: App konfiguriert, Library loggt**
    * Die **Applikation** (z.B. `main.py`) konfiguriert das Logging *einmalig*, idealerweise über `logging.config.dictConfig()`.
    * **Module/Libraries** konfigurieren *niemals* (kein `basicConfig`!). Sie holen sich nur ihren Logger.

* **Regel 2: `getLogger(__name__)` verwenden**
    * In Modulen *immer* einen spezifischen Logger verwenden: `log = logging.getLogger(__name__)`.
    * *Niemals* die globalen Funktionen (z.B. `logging.error()`) direkt nutzen.

* **Regel 3: Exceptions korrekt loggen**
    * Loggen Sie Exceptions *immer* mit `log.exception(...)` oder `log.error(..., exc_info=True)`.
    * Ein `log.error(f"{e}")` ist **falsch**, da es den kritischen **Stack Trace** verliert.

* **Regel 4: Structured Logging (JSON)**
    * Für moderne, verteilte Systeme (ELK, Datadog) ist Structured Logging (JSON) dem reinen Text vorzuziehen.
    * Es macht Log-Daten (z.B. `user_id`, `trace_id`) maschinell durchsuchbar und auswertbar.
# ACTION:

Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Core Task + Bonus Challenge, and two-file format).
Dont use emojis in the instructions. The heading for core task is "Angabe" and for bonus challenge its "Bonus-Herausforderung".