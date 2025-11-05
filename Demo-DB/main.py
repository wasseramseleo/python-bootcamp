import sqlite3

# 1. Verbinden (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# 2. SQL ausführen (Schema definieren)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT
    )
""")

# 3. WICHTIG: Parameterisierung (Schutz vor SQL-Injection!)
# NIEMALS f-strings für Werte verwenden!
user_name = "Alice"
cursor.execute("INSERT INTO users (name) VALUES (?)", (user_name,))

# 4. Transaktion abschließen
conn.commit()

# 5. Daten abfragen
for row in cursor.execute("SELECT id, name FROM users"):
    print(row) # Output: (1, 'Alice')




# Wir haben eine Klasse
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# SQL gibt uns ein Tupel
cursor.execute("SELECT id, name FROM users WHERE id = 1")
row = cursor.fetchone() # -> (1, 'Alice')

# Manuelle Konvertierung (Boilerplate-Code)
if row:
    user_obj = User(id=row[0], name=row[1])


conn.close()