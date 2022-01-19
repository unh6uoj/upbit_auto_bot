import json
import os
from urllib.parse import urlencode
import uuid
import hashlib
from wsgiref import headers
from black import re

import requests
import jwt
import pydotenv


dotenv = pydotenv.Environment()


class Upbit:
    def __init__(self):
        self.authorization_token = ""
        self.server_url = "https://api.upbit.com"

    # 인증 토큰 받기
    def get_authorization_token(self):
        payload = {
            "access_key": dotenv["ACCESS_KEY"],
            "nonce": str(uuid.uuid4()),
        }
        jwt_token = jwt.encode(payload, dotenv["SECRET_KEY"])
        authorization_token = "Bearer {}".format(jwt_token)

        return authorization_token

    # 인증 토큰 부여
    def set_authorization_token(self, token):
        self.authorization_token = token

    # 내 계좌 조회
    def get_accounts(self):
        url = f"{self.server_url}/v1/accounts"

        headers = {"Authorization": self.authorization_token}

        response = requests.get(url, headers=headers)

        return response.status_code, response.json()

    # 분 캔들 조회
    def get_minute_candle(self, ticker):
        url = f"{self.server_url}/v1/candles/minutes/1"

        headers = {
            "Authorization": self.authorization_token,
        }

        params = {"market": ticker}

        response = requests.get(url, headers=headers, params=params)

        return response.status_code, response.json()

    # 지정가 매수
    def buy_target_price(self, ticker, volume, price):
        url = f"{self.server_url}/v1/orders"

        headers = {"Authorization": self.authorization_token}

        data = {
            "market": ticker,
            "side": "bid",
            "volume": volume,
            "price": price,
            "ord_type": "limit",
        }

        response = requests.post(url, headers=headers, data=data)

        return response.status_code, response.json()

    # 지정가 매도
    def sell_target_price(self, ticker, volume, price):
        url = f"{self.server_url}/v1/orders"

        headers = {"Authorization": self.authorization_token}

        data = {
            "market": ticker,
            "side": "ask",
            "volume": volume,
            "price": price,
            "ord_type": "limit",
        }

        response = requests.post(url, headers=headers, data=data)

        return response.status_code, response.json()

    # 주문 목록 가져오기
    def get_orders(self, state):
        url = f"{self.server_url}/v1/orders"

        headers = {"Authorization": self.authorization_token}

        params = {"state": state}

        response = requests.get(url, headers=headers, params=params)

        return response.status_code, response.json()

    # 주문 삭제하기
    def delete_order(self, uuid):
        url = f"{self.server_url}/v1/orders"

        headers = {"Authorization": self.authorization_token}

        data = {"uuid": uuid}

        response = requests.delete(url, headers=headers, data=data)

        return response.status_code, response.json()
