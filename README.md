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

## Feature Engineering

### Time Features

- transaction hour
- transaction day of week
- weekend flag
- night transaction flag

### Velocity Features

- customer transaction counts over 1, 7, and 30 day windows
- customer amount sums over 1, 7, and 30 day windows

### Customer Behavior Features

- previous transaction count
- average historical amount
- historical amount standard deviation
- current amount deviation
- amount z-score
- minutes since previous transaction

### Merchant Risk Features

- previous merchant transaction count
- previous merchant fraud count
- previous merchant fraud rate
- previous merchant average amount

### Geo and Device Features

- foreign transaction flag
- high amount flag
- new device for customer flag

## Run locally

```bash
pip install -e .[dev]
pytest
python pipelines/training_pipeline.py
python -m uvicorn apps.api.main:app --reload
```
