import requests
import json

# Umständlich, nicht intuitiv, fehleranfällig
try:
    with urllib.request.urlopen("https://api.example.com") as response:
        data = json.loads(response.read().decode())
except urllib.error.HTTPError as e:
    print(f"Fehler: {e.code}")



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



# Sendet als application/x-www-form-urlencoded
payload = {'username': 'alice', 'pass': '123'}
r = requests.post("https://httpbin.org/post", data=payload)


# Setzt den `Content-Type: application/json` Header automatisch
payload = {'username': 'alice', 'role': 'admin'}
r = requests.post("https://api.example.com/users", json=payload)

print(r.json())

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

with requests.Session() as s:

  # 2. Login (Server setzt ein Cookie)
  login_data = {'username': 'user', 'pass': 'pass'}
  s.post("https://example.com/login", data=login_data)

  # 3. Nächste Anfrage (sendet das Cookie automatisch mit)
  # Wir sind jetzt eingeloggt
  response = s.get("https://example.com/dashboard")

  print(response.text)

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