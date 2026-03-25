import pandas as pd


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["transaction_hour"] = df["timestamp"].dt.hour
    df["transaction_dayofweek"] = df["timestamp"].dt.dayofweek
    df["is_weekend"] = df["transaction_dayofweek"].isin([5, 6]).astype(int)
    return df