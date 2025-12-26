def backtest(df, setups):
    results = []

    for s in setups:
        for j in range(s["index"], len(df)):
            low = df["Low"].iloc[j]
            high = df["High"].iloc[j]

            if low <= s["stop"]:
                results.append(-1)
                break
            elif high >= s["target"]:
                results.append(2)
                break

    return results
