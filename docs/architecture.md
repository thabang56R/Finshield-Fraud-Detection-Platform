# Architecture

FinShield is a production-style fraud detection platform designed for fintech fraud use cases.

## Section 6 Scope
- ingestion and cleaning
- offline feature engineering
- realtime feature engineering
- YAML-driven fraud rules
- weighted rule scoring
- supervised fraud model training
- anomaly model training
- hybrid score fusion
- unified hybrid scoring API

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
→ Rules Engine + Model Inference + Anomaly Inference  
→ Hybrid Weighted Score  
→ Decision: Approve / Review / Block  
→ Fraud Scoring API

## Hybrid Final Score

The final score blends:
- rules score
- supervised fraud probability
- anomaly score

Example:

`final_score = (0.30 * rules) + (0.45 * model) + (0.25 * anomaly)`