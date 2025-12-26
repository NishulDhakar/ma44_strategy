from data import load_data
from indicators import add_ema
from strategy import find_long_setups
from backtest import backtest
from report import report
from capital import capital_calculator

symbol = "SUZLON.NS"
year = 2024

INITIAL_CAPITAL = 1_000_000    
RISK_PER_TRADE = 10_000       

df = load_data(symbol, year)
df.columns = df.columns.get_level_values(0)
df = add_ema(df)

setups = find_long_setups(df)
results = backtest(df, setups)

report(results)

capital_stats = capital_calculator(
    results,
    INITIAL_CAPITAL,
    RISK_PER_TRADE
)

print("\nCapital Summary")
print("----------------")
print("Initial Capital :", INITIAL_CAPITAL)
print("Final Capital   :", capital_stats["final_capital"])
print("Total PnL       :", capital_stats["total_pnl"])
