# Day 1 notes

## Data engineering vocabulary
- ETL: transform before loading. ELT: load raw first, transform after.
- Data lake: cheap file storage. Data warehouse: structured tables for fast queries.
- OLAP: analysis over lots of history (this project). OLTP: running an app.

## Finance data
- OHLCV = Open, High, Low, Close, Volume.
- Daily return = today's close / yesterday's close - 1. Returns compound, so they cannot simply be added.
- Use Adj Close for returns because it corrects for dividends and splits.

## Data source
- Yahoo Finance via the yfinance library. Unofficial, for learning only. Raw data is not committed to GitHub.

## Observations
- Yahoo returns a partial row for the current day while the market is open (low volume).
- Pipeline rule: load completed days only, or re-run after market close and overwrite.
