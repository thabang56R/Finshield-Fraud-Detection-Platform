# Model Card

## Model Purpose
FinShield now uses two machine learning layers:
- supervised fraud classification
- anomaly detection for unseen suspicious behavior

## Models Implemented
- Logistic Regression baseline
- XGBoost primary classifier
- Isolation Forest anomaly detector

## Input Features
- transaction amount
- time features
- customer velocity features
- customer behavior features
- merchant risk features
- geo/device features

## Outputs
### Supervised model
- fraud probability
- binary fraud prediction

### Anomaly model
- raw anomaly score
- normalized anomaly score
- anomaly review recommendation

## Training Setup
- time-aware split using non-shuffled train/test split
- baseline threshold: 0.5
- anomaly review threshold from config

## Limitations
- trained on a small demo dataset
- anomaly score is not yet fused with supervised probability
- no delayed chargeback labels yet
- no concept drift handling yet

## Next Improvements
- hybrid score fusion
- calibration
- threshold tuning by cost
- MLflow tracking
- drift monitoring