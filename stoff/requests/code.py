import urllib.request
import json

# Umständlich, nicht intuitiv, fehleranfällig
try:
    with urllib.request.urlopen("https://api.example.com") as response:
        data = json.loads(response.read().decode())
except urllib.error.HTTPError as e:
    print(f"Fehler: {e.code}")


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