# 🛡️ FinShield Fraud Detection Platform

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Classifier-red)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-blue)
![Pytest](https://img.shields.io/badge/Pytest-Tested-success?logo=pytest)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-black?logo=githubactions)
![Status](https://img.shields.io/badge/Status-Production--Style%20Learning%20Project-purple)

> 🚀 A production-style fraud detection platform for fintech use cases, built with **Python**, **FastAPI**, **machine learning**, **rules engines**, **anomaly detection**, and **MLOps**.

---

## ✨ Vision

FinShield is designed to simulate how **modern fintech fraud detection systems** are built in real-world environments.

Instead of training a single notebook model, this project combines:

- 🧠 **supervised fraud classification** for known fraud patterns
- 🕵️ **anomaly detection** for unknown suspicious behavior
- 📏 **rules-based scoring** for interpretable business logic
- ⚖️ **hybrid scoring** for final risk decisions
- 📡 **FastAPI endpoints** for real-time fraud scoring
- 📊 **monitoring, audit logging, and MLflow tracking** for operational credibility

The goal is to make this repo feel like a **serious portfolio-grade fintech ML system** rather than a simple beginner project.

---

## 🧩 Project Description

Fraud detection in fintech is not solved with one model alone.

Real systems usually combine:

- historical behavior analysis
- merchant and device intelligence
- hand-crafted fraud rules
- probabilistic models
- anomaly scoring
- explainable decisioning
- monitoring and audit trails

FinShield follows that same pattern.

It ingests transaction history, builds fraud features, trains supervised and unsupervised models, evaluates rules, combines all signals into a final score, and exposes the results through a real-time API.

---

## 🎯 What This Project Solves

FinShield helps answer questions like:

- Is this transaction suspicious based on past behavior?
- Does it break known fraud rules?
- Does it look abnormal compared to normal activity?
- Should it be **approved**, **reviewed**, or **blocked**?
- Why did the system make that decision?

---

## 🏗️ Architecture

```text
Raw Transaction Data
        │
        ▼
Data Validation + Cleaning
        │
        ▼
Batch Feature Engineering
        │
        ├── Customer Behavior Features
        ├── Velocity Features
        ├── Merchant Risk Features
        ├── Time Features
        └── Geo / Device Features
        │
        ▼
Training Pipelines
        │
        ├── Logistic Regression Baseline
        ├── XGBoost Supervised Model
        └── Isolation Forest Anomaly Model
        │
        ▼
Saved Model Artifacts
        │
        ▼
Realtime Feature Builder
        │
        ▼
Fraud Intelligence Layers
        │
        ├── Rules Engine
        ├── Supervised Model Inference
        └── Anomaly Detection Inference
        │
        ▼
Hybrid Fraud Scoring Engine
        │
        ▼
Decision Output
        ├── Approve ✅
        ├── Review ⚠️
        └── Block ⛔
        │
        ▼
Operational Layer
        ├── FastAPI Endpoints
        ├── Audit Logs
        ├── Monitoring Reports
        └── MLflow Experiment Tracking

## 🧠 Core Fraud Detection Concepts Used

### 📈 1. Feature Engineering
Fraud models are only as good as the features they consume.

This project engineers rich behavioral and contextual features such as:

- ⏰ Transaction time features (hour, weekend, night flags)
- ⚡ Customer transaction velocity (1d, 7d, 30d)
- 💰 Rolling spend behavior
- 📊 Amount deviation from customer history
- 🏪 Merchant historical fraud rate
- 📱 New device indicator
- 🌍 Foreign transaction flag

---

### 📏 2. Rules Engine
Rules provide fast, interpretable fraud logic based on domain knowledge.

Example rules include:

- 💸 High transaction amount
- 📱 New device + large spend
- 🔁 Rapid repeat activity
- 🏪 Merchant fraud hotspot
- 🌍 Foreign high-value transaction

📌 Rules are stored in **YAML configuration** and can be modified without changing code.

---

### 🧠 3. Supervised Learning
The supervised model learns from labeled fraud data and predicts fraud probability.

**Implemented models:**
- Logistic Regression (baseline)
- XGBoost (primary classifier)

---

### 🕵️ 4. Anomaly Detection
The anomaly model detects unusual or unseen patterns without relying on labels.

**Implemented model:**
- Isolation Forest

---

### ⚖️ 5. Hybrid Risk Scoring
The final fraud score combines multiple intelligence layers:

- 📏 Rule-based score
- 🧠 Supervised model probability
- 🕵️ Anomaly score

This reflects how real-world fraud systems blend rules and machine learning.

---

### 📡 6. Real-Time Scoring
Transactions are scored in real time using FastAPI endpoints.

- ⚡ Low-latency inference
- 🔄 On-the-fly feature generation
- 🌐 API-based decisioning

---

### 📊 7. Monitoring and Auditability
The platform includes production-style observability features:

- 📈 MLflow experiment tracking
- 🧾 Prediction audit logs
- 📉 Drift report generation
- 📦 Model metadata storage

---

## 🔥 Key Features

- ✅ Production-style Python project structure  
- ✅ Configurable fraud rules engine (YAML-driven)  
- ✅ Supervised fraud model training (Logistic + XGBoost)  
- ✅ Anomaly detection pipeline (Isolation Forest)  
- ✅ Hybrid risk scoring engine  
- ✅ FastAPI real-time serving layer  
- ✅ Model metadata endpoint  
- ✅ Monitoring and drift reporting  
- ✅ Audit logging for predictions  
- ✅ MLflow experiment tracking  
- ✅ Unit, integration, and API tests  
- ✅ Docker + GitHub Actions CI  

🗂️ Project Structure

finshield-fraud-detection-platform/
├── apps/
│   ├── api/
│   │   └── main.py
│   ├── monitoring/
│   │   └── monitor.py
│   └── training/
│       └── train.py
│
├── configs/
│   ├── base.yaml
│   ├── features.yaml
│   ├── model.yaml
│   └── rules.yaml
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── samples/
│
├── docs/
│   ├── api.md
│   ├── architecture.md
│   ├── model-card.md
│   └── runbook.md
│
├── features/
│   ├── batch_features.py
│   └── realtime_features.py
│
├── models/
│   ├── anomaly/
│   ├── supervised/
│   └── artifacts/
│
├── pipelines/
│   ├── data_validation.py
│   ├── training_pipeline.py
│   ├── scoring_pipeline.py
│   └── evaluation_pipeline.py
│
├── src/
│   ├── common/
│   ├── data/
│   ├── models/
│   ├── monitoring/
│   ├── rules/
│   └── scoring/
│
├── tests/
│   ├── api/
│   ├── integration/
│   └── unit/
│
├── logs/
├── reports/
├── mlruns/
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── pyproject.toml
└── README.md

🧪 Fraud Intelligence Layers
🟦 Rules Engine

The rules engine assigns weighted fraud scores based on business logic.

Example rules:

high_amount
foreign_high_amount
rapid_repeat_activity
merchant_fraud_hotspot
new_device_high_amount
🟩 Supervised Model

The supervised model predicts the probability that a transaction is fraudulent.

Current models:

Logistic Regression
XGBoost
🟪 Anomaly Model

The anomaly model captures suspicious behavior not seen in training labels.

Current model:

Isolation Forest
🟥 Hybrid Engine

The hybrid engine combines all three signals into a final fraud score.

Example formula:

final_score =
0.30 * normalized_rule_score
+ 0.45 * model_probability
+ 0.25 * anomaly_score

Then scaled to a 0–100 risk score.

🚦 Decisioning Logic
Final Score	Decision
0–39	Approve ✅
40–69	Review ⚠️
70–100	Block ⛔
🧾 API Endpoints
Core service
GET /
GET /health
Feature generation
POST /features/realtime
Rules
POST /rules/evaluate
POST /score/rules
Models
POST /score/model
POST /score/anomaly
Hybrid scoring
POST /score/hybrid
Operations
GET /model/info
GET /monitoring/report
📦 Example Hybrid Scoring Payload
{
  "transaction_id": "txn_live_006",
  "customer_id": "cust_002",
  "merchant_id": "mrch_002",
  "amount": 12000.0,
  "currency": "ZAR",
  "country": "ZA",
  "device_type": "desktop",
  "ip_address": "196.10.1.2",
  "timestamp": "2026-03-21 10:30:00"
}
🧠 Example Hybrid Response
{
  "message": "Hybrid fraud score generated successfully",
  "result": {
    "transaction_id": "txn_live_006",
    "rule_score": 95,
    "fraud_probability": 0.84,
    "anomaly_score": 0.78,
    "final_score": 84.55,
    "decision": "block",
    "top_reasons": [
      "high_amount",
      "merchant_fraud_hotspot",
      "high_model_probability",
      "high_anomaly_score"
    ]
  }
}
🛠️ Tech Stack
Backend
Python
FastAPI
Pydantic
Data / ML
Pandas
NumPy
Scikit-learn
XGBoost
Monitoring / MLOps
MLflow
Loguru
JSON audit logs
Quality / Engineering
Pytest
Docker
GitHub Actions
🚀 Getting Started
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/finshield-fraud-detection-platform.git
cd finshield-fraud-detection-platform
2. Create and activate virtual environment
Windows PowerShell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
python -m pip install --upgrade pip
python -m pip install -e .[dev]
4. Run tests
pytest
5. Train models
python pipelines/training_pipeline.py
6. Generate evaluation metadata
python pipelines/evaluation_pipeline.py
7. Run scoring pipeline
python pipelines/scoring_pipeline.py
8. Start the API
python -m uvicorn apps.api.main:app --reload
9. Open Swagger docs
http://127.0.0.1:8000/docs
🧰 Makefile Commands
make install
make test
make train
make evaluate
make score
make monitor
make run-api
📊 Monitoring and MLOps
📈 MLflow

Experiment tracking artifacts are stored in:

mlruns/
🧾 Audit Log

Prediction audit events are written to:

Open Swagger docs
http://127.0.0.1:8000/docs
🧰 Makefile Commands
make install
make test
make train
make evaluate
make score
make monitor
make run-api
📊 Monitoring and MLOps
📈 MLflow

Experiment tracking artifacts are stored in:

mlruns/
🧾 Audit Log

Prediction audit events are written to:

logs/prediction_audit.jsonl
📉 Drift Report

Monitoring reports are saved in:

reports/drift_report.json
🗃️ Model Artifacts

Artifacts are saved in:

models/artifacts/

Generated files include:

logistic_regression_model.joblib
xgboost_model.joblib
isolation_forest_model.joblib
model_metadata.json
anomaly_metadata.json
🧪 Testing

This project includes:

unit tests
integration tests
API endpoint tests

Run all tests with:

pytest
📘 Documentation

Additional project docs live in:

docs/api.md
docs/architecture.md
docs/model-card.md
docs/runbook.md

🛣️ Roadmap
✅ Completed
project scaffolding
feature engineering
rules engine
supervised model
anomaly detection
hybrid engine
FastAPI scoring
monitoring outputs
audit logging
MLflow tracking
🔜 Future Enhancements
feature store integration
model calibration
cost-based threshold tuning
SHAP explainability
database-backed audit storage
Redis caching
streaming fraud events
advanced drift detection
dashboard for fraud monitoring

📜 License

This project is for educational and portfolio use.
Add your preferred license here, for example:

MIT License
👨‍💻 Author

Thabang Rakeng













⭐ Final Note

FinShield is built to showcase what a modern fraud detection platform can look like when engineering, ML, and MLOps are combined thoughtfully.

If you found this useful, give the repo a ⭐