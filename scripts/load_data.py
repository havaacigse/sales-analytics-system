import pandas as pd
import sqlite3

df = pd.read_csv("data/Superstore.csv")

conn = sqlite3.connect("db/sales.db")

df.to_sql("orders", conn, if_exists="append", index=False)

conn.close()

print("Data successfully loaded!")

