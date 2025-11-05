# LAB DETAILS:

* **Lab Title/Topic:** Lab 12: Requests
* **Learning Objectives:**
  * Students know how to do basic requests (GET/POST)
  * Students understand how to handle errors and execute multiple requests in a session
* **Context & Slide Summary:**
  * **`requests`** ist der "Human-Friendly" Standard für HTTP in Python.
  * **Basics:**
      * `requests.get(url)`
      * `requests.post(url, json=payload)`
      * `response.json()` (Für APIs)
  * **Robustheit (Evidenz für Prod-Code):**
      * **IMMER** `response.raise_for_status()` (in `try...except`) verwenden, um 4xx/5xx-Fehler abzufangen.
      * **IMMER** `timeout=...` setzen, um Hängenbleiben zu verhindern.
  * **Performance & State (Best Practice):**
      * **IMMER** `requests.Session()` verwenden, wenn Sie mehr als eine Anfrage an dieselbe API senden (Cookie-Handling, Connection Pooling).

# ACTION:

Generate the two markdown files (Instructions and Solution) for this lab, following all rules from our setup prompt (domain theme, continuity, Core Task + Bonus Challenge, and two-file format).
Dont use emojis in the instructions. The heading for core task is "Angabe" and for bonus challenge its "Bonus-Herausforderung". Also generate a mini flask backend which hosts the necessary endpoints for this exercise