import random
class Monkey():

    def __init__(self):
        self.budget = 0
        self.portfolio = {}

    def createPortfolio(self, numberOfAssets=None):
        if numberOfAssets is None:
            numberOfAssets = random.randint(1,25)
        for i in range(numberOfAssets):
            if i == numberOfAssets - 1:
                self.buyRandomCrypto(blowRestOfBudget=True)
            self.buyRandomCrypto()

        self.showPortfolio()

    def buyRandomCrypto(self, blowRestOfBudget=False):
        # ToDo: Define Criteria
        # must be available on Binance, Coinbase or FTX
        # must not be a stable coin
        crypto = self.pickRandomCrypto()

        if blowRestOfBudget is True:
            amountToBuyInPercent = 1
        else:
            amountToBuyInPercent = random.random()
        crypto = self.buyCrypto(crypto, amountToBuyInPercent)

        self.portfolio.add(crypto) #crypto will be a json; ToDO: build parse function in new portfolio class

    def buyCrypto(self, crypto, amountInPercent):
        moneyToBeSpent = self.budget * amountInPercent
        tokens = moneyToBeSpent / crypto.price
        crypto["tokens"] = tokens
        self.budget -= moneyToBeSpent

        return crypto

    def pickRandomCrypto(self):
        #ToDo: send get request to coingecko
        #pick Crypto #rng
        coinlist = {}
        satisfiesCriteria = False
        pick = None
        while(satisfiesCriteria is False):
            pick = random.choice(coinlist)
            satisfiesCriteria = self.checkCriteria(pick)

        assert pick is not None, "You didn't pick anything, fool!"
        return pick

    def checkCriteria(self, crypto):
        market = []
        ticker = ""
        return self.exchangeTest(market) and self.isNotStablecoin(ticker)

    def exchangeTest(self, available):
        allowedExchanges = ["binance", "coinbase", "ftx", "kraken"]
        for exchange in available:
            if exchange in allowedExchanges:
                return True

    def isNotStablecoin(self, ticker):
        prohibitedTickers = ["usdc", "usdt", "ust", "tusd", "dai", "pax"]
        return ticker not in prohibitedTickers





