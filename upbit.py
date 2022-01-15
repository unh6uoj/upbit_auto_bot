import json
import os
from urllib.parse import urlencode
import uuid
import hashlib

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
        payload = {"access_key": dotenv["ACCESS_KEY"], "nonce": str(uuid.uuid4())}
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

    # 최근 체결 내역
    def get_trade_info(self, ticker):
        url = f"{self.server_url}/v1/trades/ticks"

        m = hashlib.sha512()
        m.update(urlencode({"market": ticker}).encode())
        query_string = m.hexdigest()

        headers = {"Accept": "application/json", "query_hash": {query_string}}

        response = requests.get(url, headers=headers)

        return response.status_code, response.json()
