from pathlib import Path

from pipelines.training_pipeline import run_training_pipeline
from src.common.paths import MODEL_ARTIFACTS_DIR


def test_training_pipeline_saves_artifacts():
    metadata = run_training_pipeline()

    assert "baseline_metrics" in metadata
    assert "primary_metrics" in metadata

    assert (MODEL_ARTIFACTS_DIR / "logistic_regression_model.joblib").exists()
    assert (MODEL_ARTIFACTS_DIR / "xgboost_model.joblib").exists()
    assert (MODEL_ARTIFACTS_DIR / "model_metadata.json").exists()