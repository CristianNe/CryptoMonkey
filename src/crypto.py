class Crypto:

    def __init__(self, name, ticker, price, marketCap):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.marketCap = marketCap

    def update(self, price, marketCap):
        self.price = price
        self.marketCap = marketCap
