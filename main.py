from search_currnet_price import *

import time

coin = SearchCurrentPrice('KRW', 'BTC')
while True:
    # 현재 가격 조회
    coin.get_price()
    time.sleep(1)