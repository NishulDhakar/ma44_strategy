# MA-44 Breakout Strategy Analyzer

A rule-based trading strategy analyzer built in Python to evaluate 44-EMA breakout setups on historical price data.

The system identifies long and short trade setups using price action around a 44-period moving average, applies fixed risk–reward rules, and reports overall strategy performance for a given symbol and year.

This project focuses on deterministic logic, risk management, and explainability rather than prediction or machine learning.

---

## Project Architecture

```bash

Market Data (Yahoo Finance)
        |
        v
+------------------------+
|      Data Loader       |
|      (yfinance)       |
+------------------------+
        |
        v
+------------------------+
|   Indicator Engine     |
|     - 44 EMA           |
+------------------------+
        |
        v
+------------------------+
|   Strategy Engine      |
|   - Breakout Rules     |
|   - Entry / SL / TP    |
+------------------------+
        |
        v
+------------------------+
|   Backtest Engine      |
|   - Trade Simulation   |
|   - R Multiple Calc    |
+------------------------+
        |
        v
+------------------------+
|  Performance Report    |
|   - Win / Loss         |
|   - Win Rate           |
|   - Net R              |
+------------------------+

```
---

## Strategy Logic

- Trend filter using 44 EMA
- Long: Buy on break of previous candle high when price is above EMA
- Short: Sell on break of previous candle low when price is below EMA
- Stop-loss at opposite candle extreme
- Target based on fixed risk–reward (1:2 or 1:3)

---

## Output Metrics

- Total trade setups
- Winning and losing trades
- Win rate
- Net R multiple

---

## Tech Stack

- Python
- pandas
- numpy
- yfinance

---

## Run

```bash
python3 run.py

