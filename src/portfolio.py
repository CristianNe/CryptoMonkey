from src.crypto import Crypto

class Portfolio:

    def __init__(self):
        self.assets = {}
        self.portfolioValue = 0

    def __add__(self, crypto):
        name = crypto.name
        ticker = crypto.ticker
        price = float(crypto.price)
        marketCap = crypto.marketCap
        tokens = float(crypto.tokens)
        totalValue = tokens * price
        self.assets[ticker] = {
            "Crypto": Crypto(name, ticker, price, marketCap),
            "tokens": tokens,
            "totalValue": totalValue
        }
        self.portfolioValue += totalValue
