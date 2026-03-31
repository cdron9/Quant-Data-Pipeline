# Quant Data Pipeline

A market data pipeline that pulls, cleans, and visualizes historical stock price data using the Yahoo Finance API.

Built as Project 1 of a self-directed quant finance curriculum.

---

## What it does

- Pulls historical OHLCV (Open, High, Low, Close, Volume) data for any ticker via yfinance
- Inspects and validates data quality by checking for nulls and structural integrity
- Visualizes closing price with 20 and 50 day moving averages
- Visualizes daily volume alongside price action on a shared time axis

---

## How to run

1. Clone the repo
2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Run:
```bash
   python main.py
```

---

## What I learned

- The **data pipeline pattern** — pull, inspect, clean, analyze
- How market data is structured as **OHLCV bars** — the fundamental unit of price data
- How to work with **pandas DataFrames** — shape, head, tail, null checking
- How **moving averages** smooth price noise and reveal underlying trend
- The **death cross and golden cross** — MA20/MA50 crossover signals
- How **volume spikes** can precede price moves as a sentiment indicator
- Virtual environments and reproducible Python project structure
