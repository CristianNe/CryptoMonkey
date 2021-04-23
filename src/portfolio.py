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

    def show(self):
        valueChange = round((self.portfolioValue/self.startValue * 100)-100,2)
        portfolio = "[Portfolio]\ntotal portfolio value: {0} $\n".format(self.portfolioValue)
        portfolio += "change: {0}%\n".format(valueChange)
        for asset in self.assets:
            portfolio+= "{0}: {1}%\n".format(asset.Cryto.name, round(asset.totalValue/self.portfolioValue*100, 2))
            portfolio+= "\tamount: {0} {1}\n".format(asset.tokens, asset.Cryto.symbol)
            portfolio+= "\ttotal value: {0} $".format(asset.totalValue)

        return portfolio