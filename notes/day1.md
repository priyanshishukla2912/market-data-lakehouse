# Day 1 notes
data collection path : NSE (official) → Yahoo Finance → yfinance → our CSV file
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

## NSE cross-check
- 2020-01-01 to 2020-01-03: yfinance OHLC and close match NSE official data exactly (e.g. 2020-01-02 close 2157.65). Volume matches after converting lakh to units.
- NSE CLOSE is the official close (weighted average of last 30 minutes); LTP is the last traded price. yfinance matched CLOSE.
- 2026-11-06: yfinance close 2498.50 vs NSE prev. close 2498.80 (diff 0.30). Small gap, reason not confirmed.
- 2026-11-09 partial row: open/high/low matched NSE; close was provisional (2455.20 vs final 2475.40) because it was pulled mid-session.
- Conclusion: yfinance is accurate on the rows checked, but recent days can differ slightly, so quality checks are still needed.
