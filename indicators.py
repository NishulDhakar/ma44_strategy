def add_ema(df, period=44):
    df["ema44"] = df["Close"].ewm(span=period).mean()
    return df
