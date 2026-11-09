from pathlib import Path

import pandas as pd
import yfinance as yf

# The 10 stocks we will start with. ".NS" tells Yahoo Finance these are NSE stocks.
TICKERS = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "ITC.NS", "SBIN.NS", "BHARTIARTL.NS", "LT.NS",
]

# Where the raw files will be saved. Path makes this work on Mac and Windows.
OUT_DIR = Path("data/raw")
OUT_DIR.mkdir(parents=True, exist_ok=True)

for ticker in TICKERS:
    # auto_adjust=False keeps BOTH "Close" and "Adj Close" columns
    df = yf.download(ticker, start="2020-01-01", auto_adjust=False, progress=False)

    # Newer yfinance versions return two-level column names. Flatten them.
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.to_csv(OUT_DIR / f"{ticker}.csv")
    print(f"{ticker}: {len(df)} rows saved")