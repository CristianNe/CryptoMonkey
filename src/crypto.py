class Crypto:

    def __init__(self, cryptoData):
        # cryptoData cointains a JSON object with the following data
        # {id: String,
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
        # }
        self.name = cryptoData["name"]
        self.symbol = cryptoData["symbol"]
        self.price = cryptoData["current_price"]
        self.marketCap = cryptoData["market_cap"]

    def update(self, price, marketCap):
        self.price = price
        self.marketCap = marketCap
