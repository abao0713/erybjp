# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 19:09
# @Author  : Baymax
# @FileName: AddCookies.py
# @Software: PyCharm
from uiplatform.utils.common.BaseApi import BaseApi

# 设置登录态的Token,需要分别设置 domain、name、value
COOKIES = {
    "domain": ".codemao.cn",
    # "name": "test-authorization",
    # "value": BaseApi().get_user_token()
}


def judge_env(cookies, env="test"):
    # if not env:
    #     raise ValueError("in judge_env method: env params error")
    if env == "test":
        cookies['name'] = str("test-{0}").format("authorization")
        cookies['value'] = BaseApi().get_user_token(env)

    elif env == "staging":
        cookies['name'] = str("staging-{0}").format("authorization")
        cookies['value'] = BaseApi().get_user_token(env)
    else:
        cookies['name'] = "authorization"
        cookies['value'] = BaseApi().get_user_token(env)
    return cookies


class AddCookies:
    """

    """
    def add_cookies_and_visit_url(self, class_page, driver, url, env="test"):
        page = class_page(driver=driver)
        page.get(url)

        # 给driver添加cookie
        page.delete_all_cookie()
        cookies = judge_env(COOKIES, env)
        page.add_cookies(cookies)
        page.get(url)
        return page
