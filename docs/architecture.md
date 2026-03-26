# Architecture

FinShield is a production-style fraud detection platform designed for fintech fraud use cases.

## Section 5 Scope
- ingestion and cleaning
- offline feature engineering
- realtime feature engineering
- YAML-driven fraud rules
- weighted rule scoring
- supervised fraud model training
- anomaly model training
- saved model artifacts
- supervised and anomaly inference APIs

## High-Level Flow

Raw Transactions  
→ Validation  
→ Cleaning  
→ Batch Feature Engineering  
→ Training Dataset  
→ Preprocessing Pipeline  
→ Logistic Regression Baseline  
→ XGBoost Classifier  
→ Isolation Forest  
→ Saved Artifacts  
→ Realtime Feature Builder  
→ Rules Engine / Model Inference / Anomaly Inference  
→ Fraud Scoring API

## Saved Artifacts
- logistic_regression_model.joblib
- xgboost_model.joblib
- isolation_forest_model.joblib
- model_metadata.json
- anomaly_metadata.json