import pandas as pd

# Liest eine CSV-Datei und leitet Spaltentypen/Header ab
df = pd.read_csv("sales_data.csv")

# Andere gängige Formate:
# df = pd.read_excel("report.xlsx")
# df = pd.read_json("api_response.json")
# df = pd.read_sql("SELECT * FROM users", db_connection)

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000 entries, 0 to 999
# Data columns (total 3 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   UserID     1000 non-null   int64
#  1   Product    950 non-null    object  <-- 50 fehlende Werte!
#  2   Price      1000 non-null   float64


# Syntax: df['Spaltenname']

# 1. Eine einzelne Spalte auswählen -> Ergibt eine Series
users = df['UserID']
# print(type(users)) # <class 'pandas.core.series.Series'>

# 2. Mehrere Spalten auswählen -> Ergibt einen DataFrame
# (Beachten Sie die doppelte Klammer: df[[list_of_names]])
user_data = df[['UserID', 'Product']]
# print(type(user_data)) # <class 'pandas.core.frame.DataFrame'>

df = pd.DataFrame({'age': [22, 45, 30], 'city': ['BER', 'NYC', 'BER']})

# 1. Die Bedingung (erzeugt eine Series [False, True, False])
mask = df['age'] > 40

# 2. Anwenden der Maske
# Pandas gibt nur die Zeilen zurück, bei denen die Maske True war.
old_users = df[mask]
# print(old_users) # Zeigt nur den 45-jährigen User

# --- Kombinierte Bedingungen ---
# & (und), | (oder). Klammern () sind zwingend!
mask_complex = (df['age'] > 25) & (df['city'] == 'BER')

users_berlin = df[mask_complex]
# print(users_berlin) # Zeigt nur den 30-jährigen User






# Frage: "Was ist der Durchschnittspreis pro Produktkategorie?"
# df hat Spalten: 'Category', 'Price'

# 1. Split (nach 'Category')
# 2. Apply (mean() auf 'Price')
# 3. Combine
avg_price_per_category = df.groupby('Category')['Price'].mean()

# Frage: "Wie viele Sales pro Stadt und Kategorie?"
sales_count = df.groupby(['City', 'Category'])['SalesID'].count()