import json

from upbit import Upbit
from trade_algo import *

upbit = Upbit()
tickers = json.loads(open("tickers.json", "r").read())["tickers"]

auth_token = upbit.get_authorization_token()
upbit.set_authorization_token(auth_token)


target_price = volatility_breakout_strategy()
if target_price != False:
    upbit.buy_target_price(target_price)


while True:
    accounts = upbit.get_accounts()  # 내 계좌
    print("주문 가능 금액: ", accounts["balance"])

    candles = [upbit.get_minute_candle_by_ticker(ticker) for ticker in tickers]
