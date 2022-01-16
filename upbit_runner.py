from upbit import Upbit
from trade_algo import *

upbit = Upbit()

auth_token = upbit.get_authorization_token()
upbit.set_authorization_token(auth_token)

# 내 계좌
accounts = upbit.get_accounts()

target_price = volatility_breakout_strategy()
if target_price != False:
    upbit.buy_target_price(target_price)
