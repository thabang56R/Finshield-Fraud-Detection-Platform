# Architecture

FinShield is a production-style fraud detection platform designed for fintech fraud use cases.

## Section 3 Scope
- ingestion and cleaning
- offline feature engineering
- realtime feature engineering
- YAML-driven fraud rules
- weighted rule scoring
- rule-based risk decisions
- explainable reasons
- API endpoints for rule evaluation and scoring

## High-Level Flow

Raw Transactions  
→ Validation  
→ Cleaning  
→ Batch Feature Engineering  
→ Realtime Feature Builder  
→ Rules Engine  
→ Rule Score + Reasons  
→ Decision: Approve / Review / Block  
→ Monitoring

## Rules Engine Design

Rules are stored in YAML and contain:
- name
- description
- condition
- weight
- action

The engine evaluates each condition against realtime engineered features and produces:
- triggered rules
- total rule score
- rule-level explanations
- final decision
