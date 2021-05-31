import pyupbit

class SearchCurrentPrice():
    def __init__(self, currency, ticker):
        self.currency = currency
        self.ticker = ticker

    def get_price(self):
        price = pyupbit.get_current_price(self.currency+'-'+self.ticker)

        print(price)