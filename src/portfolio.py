from src.crypto import Crypto

class Portfolio:

    def __init__(self):
        self.assets = {}
        self.portfolioValue = 0

    def __add__(self, crypto, tokens):
        totalValue = tokens * crypto.price
        self.assets[crypto.symbol] = {
            "Crypto": crypto,
            "tokens": tokens,
            "totalValue": totalValue
        }
        self.portfolioValue += totalValue

    def setStartValue(self, value):
        self.startValue = value

    def update(self, newData):
        for asset in self.assets:
            # subtract old asset value from total portfolio value
            self.portfolioValue -= asset.totalValue
            id = asset.Crypto.id
            asset.Crypto.update(newData[id]["usd"], newData[id]["usd_market_cap"])
            asset.totalValue = asset.tokens * asset.Crypto.price
            # add the updated asset value to portfolio total value
            self.portfolioValue += asset.totalValue

    def toString(self):
        valueChange = round((self.portfolioValue/self.startValue * 100)-100,2)
        portfolio = "[Portfolio]\ntotal portfolio value: {0} $\n".format(self.portfolioValue)
        portfolio += "change: {0}%\n".format(valueChange)
        for asset in self.assets:
            portfolio+= "{0}: {1}%\n".format(asset.Cryto.name, round(asset.totalValue/self.portfolioValue*100, 2))
            portfolio+= "\tamount: {0} {1}\n".format(asset.tokens, asset.Cryto.symbol)
            portfolio+= "\ttotal value: {0} $".format(asset.totalValue)

        return portfolio