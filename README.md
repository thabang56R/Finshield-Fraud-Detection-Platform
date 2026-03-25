# FinShield Fraud Detection Platform

A production-style fraud detection platform for fintech use cases, built with Python, FastAPI, machine learning, and MLOps principles.

## Vision

FinShield aims to simulate how real fintech fraud systems are structured in practice: reliable data ingestion, validation, feature engineering, model pipelines, API scoring, monitoring, and explainability.

## Section 1 Completed

- production-ready project structure
- config management
- logging
- ingestion and validation pipeline
- FastAPI starter service
- feature engineering starter modules
- unit, integration, and API tests
- Docker and GitHub Actions CI

## Stack

- Python
- FastAPI
- Pandas
- Scikit-learn
- XGBoost
- Great Expectations
- Pytest
- Docker
- GitHub Actions

## Run locally

```bash
pip install -e .[dev]
pytest
python pipelines/data_validation.py
uvicorn apps.api.main:app --reload
```
