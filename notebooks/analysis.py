import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


conn = sqlite3.connect("db/sales.db")

df = pd.read_sql_query("""
SELECT order_date, sales
FROM orders_new
""", conn)

conn.close()

print("VERI CEKILDI")

df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)
df["month"] = df["order_date"].dt.to_period("M")

#aylik satis hesabi 
monthly_sales = (
    df.groupby("month")["sales"]
    .sum()
    .reset_index()
)

monthly_sales["month"] = monthly_sales["month"].astype(str)

print(monthly_sales.head())

#grafik
plt.figure()
plt.plot(monthly_sales["month"], monthly_sales["sales"])
plt.xticks(rotation=90)
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig("monthly_sales.png")

print("GRAFIK OLUSTU: monthly_sales.png")


#tahmin 
monthly_sales["month_index"] = np.arange(len(monthly_sales))

X = monthly_sales[["month_index"]]
y = monthly_sales["sales"]

model = LinearRegression()
model.fit(X, y)

next_month = np.array([[len(monthly_sales)]])
prediction = model.predict(next_month)

print("\nTAHMIN EDILEN GELECEK AY SATIS:")
print(round(prediction[0], 2))
