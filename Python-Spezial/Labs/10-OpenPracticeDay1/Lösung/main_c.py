import requests

BASE_URL = "http://127.0.0.1:5000/credit-score"
customer_ids = ["CUST-001", "CUST-002", "CUST-X"]

print(f"Frage API ab: {BASE_URL}")

for cid in customer_ids:
    url = f"{BASE_URL}/{cid}"

    try:
        response = requests.get(url)

        # Check auf HTTP Status 200 (OK)
        if response.status_code == 200:
            data = response.json()  # JSON dekodieren
            print(f"Kunde {cid}: Rating {data['rating']}, Limit {data['limit']} EUR")
        elif response.status_code == 404:
            print(f"Kunde {cid}: Nicht gefunden (404)")
        else:
            print(f"Kunde {cid}: Unerwarteter Fehler {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("FEHLER: Konnte Server nicht erreichen. Läuft 'mock_server.py'?")
        break
