from __future__ import annotations

import json

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

from features.batch_features import build_batch_features
from src.common.config import load_yaml_config
from src.common.logger import logger
from src.common.paths import MODEL_ARTIFACTS_DIR, PROCESSED_DATA_DIR, RAW_DATA_DIR
from src.data.ingestion import basic_cleaning, read_csv_data, validate_required_columns
from src.models.evaluate import evaluate_classifier
from src.models.preprocessing import get_feature_columns
from src.models.train import train_models


def run_training_pipeline() -> dict:
    logger.info("Training pipeline started")

    config = load_yaml_config("model.yaml")
    target_col = config["model"]["target"]
    random_state = int(config["model"]["random_state"])
    test_size = float(config["model"]["test_size"])
    threshold = float(config["training"]["probability_threshold"])

    raw_file_path = RAW_DATA_DIR / "transactions_sample.csv"
    processed_file_path = PROCESSED_DATA_DIR / "transactions_features.csv"

    df = read_csv_data(str(raw_file_path))
    validate_required_columns(df)
    df = basic_cleaning(df)

    features_df = build_batch_features(df)
    features_df.to_csv(processed_file_path, index=False)

    feature_config = get_feature_columns()
    selected_features = feature_config["numeric"] + feature_config["categorical"]

    X = features_df[selected_features].copy()
    y = features_df[target_col].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        shuffle=False,
        random_state=random_state,
    )

    trained = train_models(X_train=X_train, y_train=y_train, random_state=random_state)

    baseline_metrics = evaluate_classifier(trained.baseline_pipeline, X_test, y_test, threshold=threshold)
    primary_metrics = evaluate_classifier(trained.primary_pipeline, X_test, y_test, threshold=threshold)

    joblib.dump(trained.baseline_pipeline, MODEL_ARTIFACTS_DIR / "logistic_regression_model.joblib")
    joblib.dump(trained.primary_pipeline, MODEL_ARTIFACTS_DIR / "xgboost_model.joblib")

    metadata = {
        "baseline_model": config["training"]["baseline_model"],
        "primary_model": config["training"]["primary_model"],
        "target": target_col,
        "threshold": threshold,
        "feature_columns": selected_features,
        "baseline_metrics": baseline_metrics,
        "primary_metrics": primary_metrics,
    }

    with open(MODEL_ARTIFACTS_DIR / "model_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    logger.info(f"Saved processed training features to: {processed_file_path}")
    logger.info(f"Saved model artifacts to: {MODEL_ARTIFACTS_DIR}")
    logger.info("Training pipeline completed")

    return metadata


if __name__ == "__main__":
    result = run_training_pipeline()
    print(json.dumps(result, indent=2))