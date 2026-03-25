# Architecture

FinShield is a production-style fraud detection platform designed for fintech fraud use cases.

## Section 2 Scope

- ingestion and cleaning
- offline feature engineering
- realtime feature engineering
- customer velocity features
- customer behavior features
- merchant risk features
- geo and device features
- starter API for feature preview

## High-Level Flow

Raw Transactions  
→ Validation  
→ Cleaning  
→ Batch Feature Engineering  
→ Training Dataset  
→ Realtime Feature Builder  
→ Fraud Scoring API  
→ Monitoring

## Feature Families

### Time Features

- transaction hour
- day of week
- weekend flag
- night flag

### Velocity Features

- customer transaction count in 1 day
- customer transaction count in 7 days
- customer transaction count in 30 days
- customer amount sums in 1, 7, 30 day windows

### Customer Behavior Features

- previous transaction count
- previous average amount
- previous amount std
- amount deviation
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
