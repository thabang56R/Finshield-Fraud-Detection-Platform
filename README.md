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

## Stack
- Python
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Great Expectations
- Pytest
- Docker
- GitHub Actions

## Rule Engine Overview

Each rule includes:
- name
- description
- condition
- weight
- action

Example:

```yaml
- name: foreign_high_amount
  description: Foreign transaction combined with a high amount
  condition: "is_foreign_transaction == 1 and is_high_amount == 1"
  weight: 35
  action: "block"

  Decision Bands

- approve: low rule score, no serious rule triggered

- review: medium risk score or suspicious combinations

- block: high score or block-level rules triggered

Run locally

pip install -e .[dev]
pytest
python pipelines/training_pipeline.py
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
  "transaction_id": "txn_live_003",
  "customer_id": "cust_002",
  "merchant_id": "mrch_002",
  "amount": 12000.0,
  "currency": "ZAR",
  "country": "ZA",
  "device_type": "desktop",
  "ip_address": "196.10.1.2",
  "timestamp": "2026-03-21 10:30:00"
}