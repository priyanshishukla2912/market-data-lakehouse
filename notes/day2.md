# Day 2 notes

## What I built
- Moved the settings (tickers, dates, folders) into `ingestion/config.py`, so every script reads them from one place.
- Added logging to `ingestion/pull_prices.py`. It now writes a time-stamped record of each run to `logs/ingestion.log`, and one failing stock is logged and skipped instead of crashing the run.
- Wrote `transform/day2_returns.py`: loads all 10 stocks, builds one table of Adj Close prices, and computes daily and cumulative returns.
- Made a chart of cumulative returns for TCS, RELIANCE and HDFCBANK (`notes/cumulative_returns.png`).

## Key concepts
- **Daily return** = today's price / yesterday's price - 1.
- **Cumulative return** = (1 + r1) x (1 + r2) x ... x (1 + rn) - 1. Returns compound, so they cannot be added. Example: +10%, -10%, +10% gives 8.9%, not 10%.
- **Floating-point noise:** computers store decimals in binary, so (1.1 x 0.9 x 1.1 - 1) printed 0.08900000000000019. Compare numbers with a tolerance, not equality.
- **Volatility** = how much a stock's daily return swings (standard deviation of daily returns).
- **Close vs Adj Close in yfinance:** Close is adjusted for splits but not dividends. Adj Close is adjusted for both. Over these years the gap comes from dividends only.
- **Adjustment factor** = Close / Adj Close. It is flat between dividends and steps at each ex-dividend date.
- **Sanity check:** I calculated cumulative return two ways and they agreed (difference about 1.4e-14).

## Results (Jan 2020 to 6 Nov 2026, Adj Close)

| Stock | Total return % | Avg daily % | Daily std % |
|---|---|---|---|
| BHARTIARTL | 392.4 | 0.108 | 1.68 |
| LT | 248.8 | 0.089 | 1.74 |
| SBIN | 236.0 | 0.090 | 1.92 |
| ICICIBANK | 205.2 | 0.082 | 1.82 |
| RELIANCE | 96.4 | 0.055 | 1.76 |
| INFY | 95.0 | 0.055 | 1.78 |
| ITC | 67.7 | 0.042 | 1.54 |
| TCS | 37.2 | 0.031 | 1.57 |
| HDFCBANK | 32.3 | 0.030 | 1.61 |
| HINDUNILVR | 15.4 | 0.019 | 1.46 |

## Observations
1. **Best and worst:** Bharti Airtel did best (392.4%) and Hindustan Unilever did worst (15.4%). HUL also had the lowest daily swings (1.46%). The best performer was not the riskiest, since SBIN had the highest volatility (1.92%) but ranked third. Higher risk did not automatically mean higher return.
2. **The chart (TCS, RELIANCE, HDFCBANK):** all three fell sharply in early 2020. HDFC Bank dropped lowest, to about -40%. Reliance and TCS recovered fastest and peaked near 130% around 2024. Then both fell back, and TCS dropped the most (to roughly +10% in 2026) before bouncing at the end. HDFC Bank recovered slowly and never went above about 65%.
3. **Biggest single-day moves:**
   - Biggest gain: Reliance +14.72% on 2020-03-25.
   - Biggest drop: ICICI Bank -17.85% on 2020-03-23 (L&T -16.27% and SBI -13.46% the same day).
   - Most of the extreme days fall in March 2020, the COVID crash. Another big drop is SBI -14.40% on 2024-06-04.
4. **Dividends:** TCS's factor changed on 29 dates, about 4 a year (quarterly dividends). Most steps are 0.2% to 0.7%. A few are bigger (2023-01-16: 2.22%, 2025-01-17: 1.81%, 2026-01-16: 1.79%). The factor was 1.1901 on the first day and 1.0 on the last day.
5. **Why Adj Close matters:** TCS's plain price rose about 15% (2167.60 to 2498.50), but its return including dividends is 37.2%. About 22 points came from dividends.

## To verify (not checked yet)
- 2024-06-04 was general election results day, which probably explains SBI's -14.40% drop.
- The three larger dividend steps may be special dividends. Check TCS's dividend history.

## What I learned
- Raw data needs checking against the source (NSE) before I trust it.
- A calculation should be checked a second way (my two cumulative-return methods agreed).
- Config files and logs make a pipeline easier to run and debug.