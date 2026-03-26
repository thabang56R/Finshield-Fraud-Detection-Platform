# Model Card

## Model Purpose
This supervised model predicts the probability that a transaction is fraudulent based on engineered behavioral, merchant, time, and device features.

## Models Implemented
- Logistic Regression baseline
- XGBoost primary classifier

## Input Features
- transaction amount
- time features
- customer velocity features
- customer behavior features
- merchant risk features
- geo/device features

## Output
- fraud probability
- binary fraud prediction

## Training Setup
- time-aware split using non-shuffled train/test split
- baseline threshold: 0.5

## Limitations
- trained on a small demo dataset
- not yet calibrated for real production thresholds
- no delayed chargeback labels yet
- no concept drift handling yet

## Next Improvements
- threshold tuning by business cost
- calibration
- class imbalance tuning
- cross-validation
- MLflow tracking
