from pathlib import Path

# The 10 stocks we start with. ".NS" marks NSE stocks on Yahoo Finance.
TICKERS = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "ITC.NS", "SBIN.NS", "BHARTIARTL.NS", "LT.NS",
]

START_DATE = "2020-01-01"
# yfinance treats the end date as exclusive. The last complete trading day
# is 2026-11-06, so we stop before 2026-11-09.
END_DATE = "2026-11-09"

RAW_DIR = Path("data/raw")
LOG_DIR = Path("logs")
