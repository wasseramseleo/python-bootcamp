import json
import re

INPUT_JSON = 'app_log.json'


def extract_references():
    # 1. JSON Load
    try:
        with open(INPUT_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Datei {INPUT_JSON} nicht gefunden.")
        return

    print(f"Processing Batch: {data.get('batch_id')}")
    print("-" * 30)

    # Regex Muster kompilieren (effizienter bei vielen Durchläufen)
    # Erklärung:
    # ref:\s+  -> Suche nach "ref:" gefolgt von Leerzeichen
    # (TX-\d+) -> Gruppe 1: "TX-" gefolgt von einer oder mehreren Ziffern
    pattern = re.compile(r"ref:\s+(TX-\d+)")

    transactions = data.get('transactions', [])

    for tx in transactions:
        internal_id = tx['id']
        details = tx['details']

        # 2. Regex Search
        match = pattern.search(details)

        if match:
            # group(1) greift auf den Teil in der Klammer (TX-...) zu
            external_ref = match.group(1)
        else:
            external_ref = "NO_ID_FOUND"

        # 4. Output
        print(f"Internal ID: {internal_id} | External Ref: {external_ref}")


if __name__ == "__main__":
    extract_references()