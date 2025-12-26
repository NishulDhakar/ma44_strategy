def capital_calculator(results, initial_capital, risk_per_trade):
    capital = initial_capital
    equity_curve = []

    for r in results:
        pnl = r * risk_per_trade
        capital += pnl
        equity_curve.append(capital)

    return {
        "final_capital": capital,
        "total_pnl": capital - initial_capital,
        "equity_curve": equity_curve
    }
