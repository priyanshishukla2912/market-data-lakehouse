from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # draw straight to image files, no window needed
import matplotlib.pyplot as plt
import pandas as pd

RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 1. Load every CSV; keep only Adj Close, one column per stock
series = {}
for path in sorted(RAW_DIR.glob("*.csv")):
    ticker = path.stem  # "TCS.NS.csv" -> "TCS.NS"
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
    series[ticker] = df["Adj Close"]
prices = pd.DataFrame(series)
print("prices table shape (days, stocks):", prices.shape)
print("missing values:", int(prices.isna().sum().sum()))

# 2. Daily and cumulative returns
daily = prices.pct_change(fill_method=None).iloc[1:]   # first day has no return
cumulative = (1 + daily).cumprod() - 1

# 3. Sanity check: two methods must agree (up to floating-point noise)
direct = prices.iloc[-1] / prices.iloc[0] - 1
max_diff = (cumulative.iloc[-1] - direct).abs().max()
print("largest difference between the two methods:", max_diff)

# 4. Summary per stock
summary = pd.DataFrame({
    "total_return_%": (cumulative.iloc[-1] * 100).round(1),
    "avg_daily_%": (daily.mean() * 100).round(3),
    "daily_std_%": (daily.std() * 100).round(2),
})
print()
print(summary.sort_values("total_return_%", ascending=False))

# 5. Save the results (data/ is git-ignored)
daily.to_csv(OUT_DIR / "daily_returns.csv")
cumulative.to_csv(OUT_DIR / "cumulative_returns.csv")

# 6. Plot three stocks
fig, ax = plt.subplots(figsize=(10, 5))
(cumulative[["TCS.NS", "RELIANCE.NS", "HDFCBANK.NS"]] * 100).plot(ax=ax)
ax.set_title("Cumulative return since Jan 2020 (Adj Close)")
ax.set_ylabel("Cumulative return (%)")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("notes/cumulative_returns.png", dpi=150)
print("\nsaved notes/cumulative_returns.png")

# 7. The biggest single-day moves across all stocks
moves = daily.stack(future_stack=True)
print("\n5 biggest daily gains (%):")
print((moves.nlargest(5) * 100).round(2))
print("\n5 biggest daily drops (%):")
print((moves.nsmallest(5) * 100).round(2))
