class Crypto:

    def __init__(self, name, ticker, price, marketcap):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.marketcap = marketcap

    def setPrice(self, price):
        self.price = price