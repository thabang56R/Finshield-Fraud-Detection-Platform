# Architecture

FinShield is a production-style fraud detection platform designed for fintech fraud use cases.

## Section 4 Scope
- ingestion and cleaning
- offline feature engineering
- realtime feature engineering
- YAML-driven fraud rules
- weighted rule scoring
- supervised fraud model training
- saved model artifacts
- supervised model inference API

## High-Level Flow

Raw Transactions  
→ Validation  
→ Cleaning  
→ Batch Feature Engineering  
→ Training Dataset  
→ Preprocessing Pipeline  
→ Logistic Regression Baseline  
→ XGBoost Classifier  
→ Saved Artifacts  
→ Realtime Feature Builder  
→ Rules Engine / Model Inference  
→ Fraud Scoring API

## Saved Artifacts
- logistic_regression_model.joblib
- xgboost_model.joblib
- model_metadata.json
