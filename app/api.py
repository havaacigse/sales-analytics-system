from pathlib import Path
from fastapi import APIRouter
import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
DB = BASE_DIR / "db" / "sales.db"



# top products
@router.get(
    "/top-products",
    tags=["Analytics"],
    summary="En Çok Satan 5 Ürün",
    description="Toplam satış miktarına göre en çok satan 5 ürünü listeler."
)
def top_products():

    conn = sqlite3.connect(DB)

    df = pd.read_sql_query("""
    SELECT p.product_name, SUM(o.sales) as total_sales
    FROM orders_new o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_sales DESC
    LIMIT 5
    """, conn)

    conn.close()

    return df.to_dict(orient="records")


# monthly sales
@router.get(
    "/monthly-sales",
    tags=["Reporting"],
    summary="Aylık Satış Raporu",
    description="Aylara göre toplam satış miktarını döndürür."
)
def monthly_sales():

    conn = sqlite3.connect(DB)

    df = pd.read_sql_query("""
    SELECT order_date, sales FROM orders_new
    """, conn)

    conn.close()

    df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)
    df["month"] = df["order_date"].dt.to_period("M")

    result = (
        df.groupby("month")["sales"]
        .sum()
        .reset_index()
    )

    result["month"] = result["month"].astype(str)

    return result.to_dict(orient="records")


# prediction endpoint
@router.get(
    "/prediction",
    tags=["Machine Learning"],
    summary="Satış Tahmini Yap",
    description="Geçmiş aylık satışlara bakarak gelecek ayın tahmini satış değerini hesaplar."
)
def get_sales_prediction():

    conn = sqlite3.connect(DB)

    df = pd.read_sql_query("""
    SELECT order_date, sales FROM orders_new
    """, conn)

    conn.close()

    df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)
    df["month"] = df["order_date"].dt.to_period("M")

    monthly = df.groupby("month")["sales"].sum().reset_index()
    monthly["month_index"] = np.arange(len(monthly))

    X = monthly[["month_index"]]
    y = monthly["sales"]

    model = LinearRegression()
    model.fit(X, y)

    next_month = np.array([[len(monthly)]])
    pred = model.predict(next_month)

    return {"next_month_prediction": float(round(pred[0], 2))}
