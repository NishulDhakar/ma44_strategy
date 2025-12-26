from data import load_data
from indicators import add_ema
from strategy import find_long_setups
from report import report
from backtest import backtest

symbol = "AAPL"
year = 2024

df = load_data(symbol, year)

df.columns = df.columns.get_level_values(0)

df = add_ema(df)

setups = find_long_setups(df)
results = backtest(df, setups)

report(results)
