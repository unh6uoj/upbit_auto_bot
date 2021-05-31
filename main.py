from search_currnet_price import *

import time

coin = SearchCurrentPrice('KRW', 'BTC')
while True:
    coin.get_price()
    time.sleep(1)