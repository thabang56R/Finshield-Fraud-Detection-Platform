from fastapi import FastAPI
from pydantic import BaseModel

from features.realtime_features import build_realtime_features
from src.common.config import settings
from src.common.paths import RAW_DATA_DIR
from src.data.ingestion import basic_cleaning, read_csv_data

app = FastAPI(
    title="FinShield Fraud Detection API",
    version="0.2.0",
    description="Production-style fraud detection platform for fintech",
)


class TransactionPayload(BaseModel):
    transaction_id: str
    customer_id: str
    merchant_id: str
    amount: float
    currency: str
    country: str
    device_type: str
    ip_address: str
    timestamp: str


@app.get("/")
def root():
    return {
        "message": "FinShield Fraud Detection API is running",
        "environment": settings.app_env,
        "version": "0.2.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "finshield-api",
        "environment": settings.app_env,
    }


@app.post("/features/realtime")
def preview_realtime_features(payload: TransactionPayload):
    history_df = read_csv_data(str(RAW_DATA_DIR / "transactions_sample.csv"))
    history_df = basic_cleaning(history_df)

    features = build_realtime_features(
        payload=payload.model_dump(),
        customer_history=history_df,
        merchant_history=history_df,
    )

    return {
        "message": "Realtime features generated successfully",
        "features": features,
    }