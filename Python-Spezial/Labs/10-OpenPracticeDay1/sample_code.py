"""--------------1-------------------"""
# The "Day 1 Stack": Structuring, Processing, Saving
def save_capture(bird_data: dict, filename: str) -> None:
  """Appends a bird record to a JSON log safely."""
  import json

  # Context Manager handles opening/closing
  with open(filename, 'a', encoding='utf-8') as f:
    json.dump(bird_data, f)
    f.write('\n')  # Newline for JSONL format


record = {"species": "Parus major", "ring": "AX-99", "weight": 18.5}
save_capture(record, "daily_log.json")

"""--------------2-------------------"""
from sqlalchemy import text

# Pattern: Extract -> Transform -> Load (ETL)
def check_ring_in_db(engine, ring_id: str):
  # 1. Secure Query (Parameterized)
  query = text("SELECT * FROM captures WHERE ring_id = :rid")

  with engine.connect() as conn:
    result = conn.execute(query, {"rid": ring_id})  # Safe!
    return result.fetchone()


# Imagine 'ring_id' came from a PDF extraction earlier
found = check_ring_in_db(my_engine, "AX-9921")