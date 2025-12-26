def find_long_setups(df):
    setups = []

    for i in range(2, len(df)):
        if (
            df["Close"].iloc[i-1] > df["ema44"].iloc[i-1]
            and df["High"].iloc[i-1] > df["High"].iloc[i-2]
        ):
            entry = df["High"].iloc[i-2]
            stop = df["Low"].iloc[i-2]
            target = entry + (entry - stop) * 2

            setups.append({
                "index": i,
                "entry": entry,
                "stop": stop,
                "target": target
            })

    return setups
