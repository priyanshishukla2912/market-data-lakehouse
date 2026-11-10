import logging

import pandas as pd
import yfinance as yf

import config

config.RAW_DIR.mkdir(parents=True, exist_ok=True)
config.LOG_DIR.mkdir(parents=True, exist_ok=True)

# Log to a file AND to the terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(config.LOG_DIR / "ingestion.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("ingestion")


def pull_one(ticker):
    """Download one stock's daily prices from Yahoo Finance."""
    df = yf.download(
        ticker,
        start=config.START_DATE,
        end=config.END_DATE,
        auto_adjust=False,   # keep both Close and Adj Close
        progress=False,
    )
    # Newer yfinance versions return two-level column names. Flatten them.
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df


for ticker in config.TICKERS:
    try:
        df = pull_one(ticker)
        if df.empty:
            log.warning("%s: no rows returned", ticker)
            continue
        df.to_csv(config.RAW_DIR / f"{ticker}.csv")
        log.info(
            "%s: %d rows saved (%s to %s)",
            ticker, len(df), df.index.min().date(), df.index.max().date(),
        )
    except Exception as exc:
        log.error("%s: failed - %s", ticker, exc)
