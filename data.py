import yfinance as yf

def load_data(symbol, year):
    return get_data(symbol, year)

def get_data(symbol, year):
    return yf.download(
        symbol,
        start=f"{year}-01-01",
        end=f"{year}-12-31"
    )