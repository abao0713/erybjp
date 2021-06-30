# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 20:52
# @Author  : Baymax
# @FileName: BaseApi.py
# @Software: PyCharm
import json

import requests
GET_USER_TOKEN_TEST_URL = "https://test-api.codemao.cn/tiger/v3/app/accounts/login"
GET_USER_TOKEN_STAGING_URL = "https://staging-api.codemao.cn/tiger/v3/app/accounts/login"
GET_USER_TOKEN_URL = "https://api.codemao.cn/tiger/v3/app/accounts/login"
GET_USER_HEADERS = {"Content-Type": "application/json"}
# 16977889930
JSON_BODY = {"pid": "og8TobPh", "identity": "15817199417", "password": "123456"}


class BaseApi:
    get_user_token_url = GET_USER_TOKEN_URL
    headers = GET_USER_HEADERS
    json_body = JSON_BODY

    def get_user_token(self, env="test"):
        if env == "test":
            self.get_user_token_url = GET_USER_TOKEN_TEST_URL
        if env == "staging":
            self.get_user_token_url = GET_USER_TOKEN_STAGING_URL
        if env == "product":
            self.get_user_token_url = GET_USER_TOKEN_URL
        # else:
        #     raise ValueError("in get_user_token method: env params error")
        response = requests.post(url=self.get_user_token_url, json=self.json_body, headers=self.headers)
        response = response.json()
        return response['auth']['token']

