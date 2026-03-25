from fastapi import FastAPI

from src.common.config import settings

app = FastAPI(
    title="FinShield Fraud Detection API",
    version="0.1.0",
    description="Production-style fraud detection platform for fintech",
)


@app.get("/")
def root():
    return {
        "message": "FinShield Fraud Detection API is running",
        "environment": settings.app_env,
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "finshield-api",
        "environment": settings.app_env,
    }