Hier sind die Inhalte für die Slides zum Thema `requests`.

-----

## Folie 1: Titel

**Titel:** 🌐 HTTP-Anfragen mit `requests`
**Untertitel:** Von den Basics zu robusten API-Clients

-----

## Folie 2: Das Problem: `urllib` (Warum `requests`?)

**Titel:** Warum `requests`? (Das "HTTP for Humans"-Prinzip)

Pythons eingebaute `urllib` ist mächtig, aber umständlich und nicht "Pythonic".

**Kritik (Evidenz): `urllib` (Legacy-Ansatz)**

```python
import urllib.request
import json

# Umständlich, nicht intuitiv, fehleranfällig
try:
    with urllib.request.urlopen("https://api.example.com") as response:
        data = json.loads(response.read().decode())
except urllib.error.HTTPError as e:
    print(f"Fehler: {e.code}")
```

**Lösung: `requests` (De-facto-Standard)**
`requests` (eine Drittanbieter-Bibliothek) abstrahiert diese Komplexität.

```bash
$ pip install requests # (oder uv pip install requests)
```

-----

## Folie 3: Basics 1: `GET`-Anfrage & Das `Response`-Objekt

**Titel:** Basics: `GET` & Das `Response`-Objekt

`requests.get()` ist die häufigste Funktion. Sie holt Daten.

```python
import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)

# --- Das 'Response'-Objekt ---

# 1. Status-Code
print(f"Status: {response.status_code}")

# 2. Inhalt (Roh-Text, z.B. für HTML)
print(response.text) 

# 3. Inhalt (Bytes, z.B. für Bilder)
print(response.content)

# 4. JSON (Der häufigste Fall für APIs)
# Parst den JSON-Text automatisch in ein Python-dict
data = response.json()
print(f"Name: {data['name']}")
```

-----

## Folie 4: Basics 2: `POST` & Daten senden

**Titel:** Basics: `POST` & Daten senden

Um Daten an einen Server zu senden (z.B. ein Formular ausfüllen, einen neuen User erstellen).

**Fall 1: Formular-Daten (`data=...`)**
(Sendet als `application/x-www-form-urlencoded`)

```python
payload = {'username': 'alice', 'pass': '123'}
r = requests.post("https://httpbin.org/post", data=payload)
```

**Fall 2: JSON-Daten (`json=...`) (Der moderne Standard)**
(Setzt den `Content-Type: application/json` Header automatisch)

```python
payload = {'username': 'alice', 'role': 'admin'}
r = requests.post("https://api.example.com/users", json=payload)

print(r.json()) # Zeigt die Antwort des Servers
```

-----

## Folie 5: Fortgeschritten 1: Fehlerbehandlung (Kritisch\!)

**Titel:** Fortgeschritten: Fehlerbehandlung (HTTP-Status)

**Das häufigste "Gotcha":** `requests` löst bei 4xx- oder 5xx-Fehlern **keine** Exception aus\!

```python
# Server antwortet mit "404 Not Found"
response = requests.get("https://api.github.com/invalid-url")

print(response.status_code) # Output: 404

# KRITISCHER FEHLER:
# Dies stürzt ab (AttributeError), da 404 kein JSON zurückgibt
# data = response.json() 
```

**Lösung (Best Practice): `response.raise_for_status()`**
Diese Methode prüft den `status_code` und löst eine `HTTPError`-Exception aus, wenn der Code 4xx (Client Error) oder 5xx (Server Error) ist.

```python
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get("https://api.github.com/invalid-url")
    
    # Erzwinge eine Exception bei schlechtem Status
    response.raise_for_status() 

    data = response.json()
    
except HTTPError as http_err:
    print(f"HTTP-Fehler aufgetreten: {http_err}")
except Exception as err:
    print(f"Anderer Fehler: {err}")
```

-----

## Folie 6: Fortgeschritten 2: Timeouts (Nie ohne\!)

**Titel:** Fortgeschritten: Timeouts (Produktions-Code)

**Das Problem:** Standardmäßig wartet `requests` **unbegrenzt** auf eine Antwort. Wenn der Server hängt, hängt Ihr Skript für immer.

**Lösung (Best Practice): Setzen Sie IMMER ein `timeout`.**

```python
from requests.exceptions import Timeout

try:
    # Timeout (in Sekunden)
    # (Connect-Timeout, Read-Timeout)
    response = requests.get(
        "https://api.example.com/slow-endpoint", 
        timeout=5.0 
    )
    
except Timeout:
    print("Der Request ist abgelaufen (Timeout).")
```

**Evidenz:** Jede `requests`-Anfrage im Produktionscode *muss* einen Timeout-Wert haben, um die Stabilität der Anwendung zu gewährleisten.

-----

## Folie 7: Fortgeschritten 3: `requests.Session()` (Der Profi-Weg)

**Titel:** Fortgeschritten: `requests.Session()`

**Problem:** `requests.get()` und `requests.post()` sind "One-Shot"-Funktionen.

1.  **Performance:** Jede Anfrage baut eine neue TCP-Verbindung auf (langsam).
2.  **Zustand (State):** Cookies (z.B. für einen Login) werden nicht automatisch zwischen Anfragen geteilt.

**Lösung: Das `Session`-Objekt.**
Eine `Session` verwaltet **Cookie-Persistenz** und nutzt **Connection Pooling**.

```python
# 1. Session-Objekt erstellen (am besten mit 'with')
with requests.Session() as s:
    
    # 2. Login (Server setzt ein Cookie)
    login_data = {'username': 'user', 'pass': 'pass'}
    s.post("https://example.com/login", data=login_data)

    # 3. Nächste Anfrage (sendet das Cookie automatisch mit)
    # Wir sind jetzt eingeloggt
    response = s.get("https://example.com/dashboard")
    
    print(response.text)
```

**Evidenz:** Für jede Interaktion mit einer API (mehr als 1 Aufruf) ist die Verwendung einer `Session` die Best Practice.

-----

## Folie 8: Fortgeschritten 4: Header & Authentifizierung

**Titel:** Fortgeschritten: Header & Authentifizierung

**Szenario:** Wie sendet man einen API-Key (z.B. Bearer-Token)?

**Lösung: Der `headers`-Parameter.**

```python
api_key = "my-secret-token-123"

# Header definieren (Standard-Weg für API-Keys)
headers = {
    "Authorization": f"Bearer {api_key}",
    "User-Agent": "MyAwesomeApp/1.0"
}

# Session verwenden UND Header setzen
with requests.Session() as s:
    s.headers.update(headers)
    
    # Jede Anfrage von 's' sendet diese Header jetzt
    r = s.get("https://api.example.com/secure/data")
```

**Alternative (HTTP Basic Auth):**
Für einfache `username:password`-Authentifizierung.

```python
# (Sendet 'Authorization: Basic ...' Header automatisch)
response = requests.get(
    url, 
    auth=('my_username', 'my_password')
)
```

-----

## Folie 9: Zusammenfassung

**Titel:** Key Takeaways

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