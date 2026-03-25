import pandas as pd

from src.common.constants import REQUIRED_TRANSACTION_COLUMNS
from src.common.logger import logger


def read_csv_data(file_path: str) -> pd.DataFrame:
    logger.info(f"Reading data from {file_path}")
    df = pd.read_csv(file_path)
    logger.info(f"Loaded dataset with shape: {df.shape}")
    return df


def validate_required_columns(df: pd.DataFrame) -> None:
    missing_columns = [col for col in REQUIRED_TRANSACTION_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Running basic cleaning")
    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["is_fraud"] = pd.to_numeric(df["is_fraud"], errors="coerce").fillna(0).astype(int)

    df = df.dropna(subset=["transaction_id", "customer_id", "merchant_id", "amount", "timestamp"])
    df = df.drop_duplicates(subset=["transaction_id"])

    logger.info(f"Dataset shape after cleaning: {df.shape}")
    return df