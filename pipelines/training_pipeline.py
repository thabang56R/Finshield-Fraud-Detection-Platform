import pandas as pd

from features.batch_features import build_batch_features
from src.common.logger import logger
from src.common.paths import PROCESSED_DATA_DIR, RAW_DATA_DIR
from src.data.ingestion import basic_cleaning, read_csv_data, validate_required_columns


def run_training_pipeline() -> pd.DataFrame:
    logger.info("Training pipeline started")

    raw_file_path = RAW_DATA_DIR / "transactions_sample.csv"
    processed_file_path = PROCESSED_DATA_DIR / "transactions_features.csv"

    df = read_csv_data(str(raw_file_path))
    validate_required_columns(df)
    df = basic_cleaning(df)

    features_df = build_batch_features(df)
    features_df.to_csv(processed_file_path, index=False)

    logger.info(f"Saved processed training features to: {processed_file_path}")
    logger.info("Training pipeline completed")

    return features_df


if __name__ == "__main__":
    run_training_pipeline()