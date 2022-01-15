from upbit import Upbit

upbit = Upbit()

auth_token = upbit.get_authorization_token()
upbit.set_authorization_token(auth_token)

accounts = upbit.get_accounts()
_, r = upbit.get_trade_info("KRW-BTC")
print(r)
