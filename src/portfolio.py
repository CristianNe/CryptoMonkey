from src.crypto import Crypto

class Portfolio:
    def __init__(self):
        self.assets = {}

    def __add__(self, crypto):
        name = crypto.name
        ticker = crypto.ticker
        price = float(crypto.price)
        marketcap = crypto.marketcap
        tokens = float(crypto.tokens)
        totalValue = tokens * price
        self.assets[ticker] = {
            "Crypto": Crypto(name, ticker, price, marketcap),
            "tokens": tokens,
            "totalValue": totalValue
        }
