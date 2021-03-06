# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         conftest.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/27
#----------------------------
import os

import pytest
import requests
from config import Config, config
from uiplatform.utils.common.Driver import _capture_screenshot


driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--seid",
        action="store",
        default="定时任务",
        type=str,
        help="本次运行时的唯一标识",
    )


@pytest.fixture(scope="session", autouse=True)
def seid(request):
    return request.config.getoption("--seid")

# 用例失败时截图
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    outcome = yield
    report = outcome.get_result()
    fail_pic = ""
    fail_result = ""
    if item.funcargs.get("seid") is None:
        seid = 0
    else:
        seid = item.funcargs.get("seid")
    if report.when == "call" or (report.when == "setup" and report.skipped):
        result = report.outcome
        consume_time = report.duration
        version = 1
        function_type = item.name

        if report.outcome == 'failed':
            fail_result = report.capstderr
            fail_pic = _capture_screenshot(path="uiplatform/utils/data/picture")
        # 多进程是这里访问数据库会出错
        json_data = {
            "result":result,"consume_time":consume_time,"version":version,"function_type":function_type,"fail_pic":fail_pic,
            "fail_result":fail_result,"session_id":seid
        }
        try:
            config_name = Config.FLASK_ENV
            print(config[config_name].HOST+"result")
            f = requests.post(url=config[config_name].HOST+"result", data=json_data)
            print(f.json())
        except Exception as e:
            print("内部接口没有启动")
            print(e)
        # model.save()


#
# @pytest.fixture(autouse=True)
# def app():
#     global app_driver
#     # APP定义运行环境
#     desired_caps = {
#         'deviceName': 'YAL_AL10',
#         'automationName': 'appium',
#         'platformName': 'Android',
#         'platformVersion': '10.0',
#         'appPackage': 'cn.codemao.android.kids.lite',
#         'appActivity': '.module.main.view.MainActivity',
#     }
#     app_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     return app_driver
#
#
# @pytest.fixture(autouse=True)
# def app_close():
#     yield app_driver
#     app_driver.quit()


