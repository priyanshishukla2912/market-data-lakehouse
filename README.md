# Market Data Lakehouse

A finance data engineering project: ingest NSE stock prices, model them, check data quality, orchestrate with Airflow and analyse them. Built step by step as a 25-day learning project.

## Status
Day 1 of 25: project setup and first raw data pull for 10 NSE stocks.

## Planned pipeline
Ingest -> raw Parquet -> transform -> star schema -> quality checks -> Airflow -> analysis dashboard -> AWS

## Run it
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python ingestion/pull_prices.py

## Data
Yahoo Finance via the yfinance library, for educational purposes only. Raw data files are not stored in this repository.
