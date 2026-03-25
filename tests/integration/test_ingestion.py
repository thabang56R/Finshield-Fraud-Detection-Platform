from src.common.paths import RAW_DATA_DIR
from src.data.ingestion import basic_cleaning, read_csv_data, validate_required_columns


def test_ingestion_pipeline():
    df = read_csv_data(str(RAW_DATA_DIR / "transactions_sample.csv"))
    validate_required_columns(df)
    cleaned_df = basic_cleaning(df)

    assert not cleaned_df.empty
    assert "transaction_id" in cleaned_df.columns
    assert "amount" in cleaned_df.columns