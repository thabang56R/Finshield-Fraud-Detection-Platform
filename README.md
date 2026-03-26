# FinShield Fraud Detection Platform

A production-style fraud detection platform for fintech use cases, built with Python, FastAPI, machine learning, and MLOps principles.

## Vision
FinShield aims to simulate how real fintech fraud systems are structured in practice: reliable data ingestion, validation, feature engineering, model pipelines, API scoring, monitoring, and explainability.

## Completed So Far

### Section 1
- production-ready project structure
- config management
- logging
- ingestion and validation pipeline
- FastAPI starter service
- tests
- Docker and CI

### Section 2
- offline batch fraud feature engineering
- realtime feature generation
- customer velocity features
- customer behavior features
- merchant risk features
- geo and device risk features
- feature preview API endpoint

### Section 3
- YAML-configurable fraud rules engine
- weighted rule scoring
- explainable triggered reasons
- rule-based approve / review / block decisions
- API endpoints for rules evaluation and scoring

### Section 4
- supervised fraud model training pipeline
- logistic regression baseline
- XGBoost primary classifier
- evaluation metrics
- saved model artifacts
- supervised model inference endpoint

### Section 5
- Isolation Forest anomaly detection
- saved anomaly artifacts
- anomaly inference endpoint
- normalized anomaly scoring
- anomaly-based review recommendation

## Stack
- Python
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Pytest
- Docker
- GitHub Actions

## Modeling Overview

### Supervised Models
- Logistic Regression baseline
- XGBoost classifier

### Anomaly Model
- Isolation Forest

### Inputs
- amount
- time-based features
- velocity features
- customer behavior features
- merchant risk features
- geo/device features

### Outputs
#### Supervised
- fraud probability
- binary fraud prediction

#### Anomaly
- raw anomaly score
- normalized anomaly score
- anomaly recommendation

## Run locally

```bash
pip install -e .[dev]
pytest
python pipelines/training_pipeline.py
python pipelines/evaluation_pipeline.py
python pipelines/scoring_pipeline.py
python -m uvicorn apps.api.main:app --reload

API Docs

http://127.0.0.1:8000/docs

Main Endpoints

Realtime features

POST /features/realtime

Rules evaluation

POST /rules/evaluate

Rule-based scoring

POST /score/rules

Sample scoring payload

{
  "transaction_id": "txn_live_005",
  "customer_id": "cust_002",
  "merchant_id": "mrch_002",
  "amount": 12000.0,
  "currency": "ZAR",
  "country": "ZA",
  "device_type": "desktop",
  "ip_address": "196.10.1.2",
  "timestamp": "2026-03-21 10:30:00"
}