import pandas as pd
import sqlite3


csv_path = "tell me abpout"
db_path = "C:/Users/marya/Downloads/laptop_data.db"


df = pd.read_csv(csv_path)


conn = sqlite3.connect(db_path)
df.to_sql("laptops", conn, if_exists="replace", index=False)
conn.close()

print("✅ CSV converted to SQLite database successfully!")
print(f"📂 Database saved at: {db_path}")
