import random
from pycoingecko import CoinGeckoAPI
from src.crypto import Crypto
from src.portfolio import Portfolio


class Monkey():

    def __init__(self):
        self.budget = 0
        self.portfolioList = {}
        self.portfolio = Portfolio()
        self.coingecko = CoinGeckoAPI()

    def createPortfolio(self, numberOfAssets=None):
        if numberOfAssets is None:
            numberOfAssets = random.randint(1,25)
        #Get Coins
        coinList = self.coingecko.get_coins_markets(
            vs_currency="usd",
            order="market_cap_desc",
            per_page="250",
            page="1",
            sparkline="false"
        )
        for i in range(numberOfAssets):
            if i < numberOfAssets - 1:
                self.buyRandomCrypto(coinList)
            else:
                self.buyRandomCrypto(coinList, blowRestOfBudget=True)

        self.showPortfolio()

    def buyRandomCrypto(self, coinList, blowRestOfBudget=False):
        #coinList cointains a list of JSON objects of coins with the following data
        #{ id: String,
        #  symbol: String,
        #  name: String,
        #  image: String,
        #  current_price: Decimal,
        #  market_cap: Decimal,
        #  market_cap_rank: Decimal,
        #  fully_diluted_valuation: Decimal,
        #  total_volume: Decimal,
        #  high_24h: 55474,
        #  low_24h: 47882,
        #  price_change_24h: Decimal,
        #  price_change_percentage_24h: Decimal,
        #  market_cap_change_24h: Decimal,
        #  market_cap_change_percentage_24h: Decimal,
        #  circulating_supply: Decimal,
        #  total_supply: Decimal,
        #  max_supply: Decimal,
        #  ath: Decimal,
        #  ath_change_percentage: Decimal,
        #  ath_date: DateString,
        #  atl: Decimal,
        #  atl_change_percentage: Decimal,
        #  atl_date: DateString,
        #  roi: null,
        #  last_updated: DateString
        #}
        crypto = self.pickRandomCrypto(coinList)

        if blowRestOfBudget is True:
            amountToBuyInPercent = 1
        else:
            amountToBuyInPercent = round(random.random(), 2)
        boughtCrypto, tokens = self.buyCrypto(crypto, amountToBuyInPercent)

        self.portfolio.add(boughtCrypto, tokens) #crypto will be a json; ToDO: build parse function in new portfolio class

    #takes in Json list of cryptos and returns a Crypto object
    def pickRandomCrypto(self, coinList):
        satisfiesCriteria = False
        pick = None
        while(satisfiesCriteria is False):
            pick = random.choice(coinList)
            satisfiesCriteria = self.checkCriteria(pick)
        assert pick is not None, "You didn't pick anything, fool!"
        crypto = Crypto(pick)

        return crypto

    def buyCrypto(self, crypto, amountInPercent):
        moneyToBeSpent = self.budget * amountInPercent
        tokens = moneyToBeSpent / crypto.price
        self.budget -= moneyToBeSpent

        return crypto, tokens

    def checkCriteria(self, crypto):
        #ToDo: extract markets and ticker symbol from crypto object
        symbol = crypto["symbol"].lower()
        marketData = self.coingecko.get_coin_by_id(
            id=crypto["id"],
            localization="false",
            tickers="true",
            marketData="false",
            community_data="false",
            developer_data="false",
            sparkline="false"
        )
        markets = []
        for market in marketData["ticker"]:
            markets.append(market["market"]["name"].lower())

        return self.exchangeTest(markets) and self.isNotStablecoin(symbol)

    def exchangeTest(self, available):
        allowedExchanges = ["binance", "coinbase", "coinbase pro" "ftx", "kraken", "ftx.us", "kucoin", "huobi global"]
        for exchange in available:
            if exchange in allowedExchanges:
                return True

    def isNotStablecoin(self, symbol):
        prohibitedTickers = ["usdc", "usdt", "ust", "tusd", "dai", "pax"]

        return symbol not in prohibitedTickers

    def showPortfolio(self):
        self.updatePortfolio()
        portfolio = self.portfolio.show()
        self.postPortfolio(portfolio)

    def updatePortfolio(self):
        assetIds = []
        for asset in self.portfolio.assets:
            assetIds.append(asset.Crypto.id)
        currentMarketData = self.coingecko.get_price(ids=assetIds, vs_currencies="usd", include_market_cap=True)
        self.portfolio.update(currentMarketData)





