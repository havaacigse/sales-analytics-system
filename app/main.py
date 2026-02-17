from fastapi import FastAPI
from app.api import router   # ÖNEMLİ: app.api olacak

app = FastAPI(
    title="Sales Analytics API",
    description="Satış verileri analiz ve tahmin servisi",
    version="1.0.0"
)

app.include_router(router)
