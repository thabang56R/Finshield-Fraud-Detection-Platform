from features.realtime_features import build_realtime_features
from src.common.logger import logger
from src.common.paths import RAW_DATA_DIR
from src.data.ingestion import basic_cleaning, read_csv_data
from src.scoring.risk_engine import FraudRiskEngine


def run_scoring_pipeline() -> dict:
    logger.info("Scoring pipeline started")

    history_df = read_csv_data(str(RAW_DATA_DIR / "transactions_sample.csv"))
    history_df = basic_cleaning(history_df)

    sample_payload = {
        "transaction_id": "txn_live_001",
        "customer_id": "cust_002",
        "merchant_id": "mrch_002",
        "amount": 12000.0,
        "currency": "ZAR",
        "country": "ZA",
        "device_type": "desktop",
        "ip_address": "196.10.1.2",
        "timestamp": "2026-03-21 10:30:00",
    }

    realtime_features = build_realtime_features(
        payload=sample_payload,
        customer_history=history_df,
        merchant_history=history_df,
    )

    risk_engine = FraudRiskEngine()
    risk_result = risk_engine.score(realtime_features)

    logger.info(f"Realtime features generated: {realtime_features}")
    logger.info(f"Risk result generated: {risk_result}")
    logger.info("Scoring pipeline completed")

    return risk_result


if __name__ == "__main__":
    result = run_scoring_pipeline()
    print(result)