from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

APPS_DIR = ROOT_DIR / "apps"
CONFIGS_DIR = ROOT_DIR / "configs"
DATA_DIR = ROOT_DIR / "data"
DOCS_DIR = ROOT_DIR / "docs"
FEATURES_DIR = ROOT_DIR / "features"
MODELS_DIR = ROOT_DIR / "models"
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
PIPELINES_DIR = ROOT_DIR / "pipelines"
SRC_DIR = ROOT_DIR / "src"
TESTS_DIR = ROOT_DIR / "tests"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SAMPLES_DATA_DIR = DATA_DIR / "samples"

MODEL_ARTIFACTS_DIR = MODELS_DIR / "artifacts"
LOGS_DIR = ROOT_DIR / "logs"

for directory in [
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    SAMPLES_DATA_DIR,
    MODEL_ARTIFACTS_DIR,
    LOGS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)