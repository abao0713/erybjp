# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         conftest.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/27
#----------------------------
import os

import pytest, time
import requests

from uiplatform.utils.common.Driver import _capture_screenshot

driver = None

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
    if report.when == "setup":
        if report.outcome == 'skipped':
            # 用例如果是跳过记录为skiped
            result = 'skiped'
    if report.when == "call":
        result = report.outcome
        consume_time = report.duration
        version = 1
        function_type = item.name
        if report.outcome == 'failed':
            fail_result = report.capstdout
            fail_pic = _capture_screenshot(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            # alidingcheck(filename, cur_time, page=item.funcargs.get("browser").current_url)

        # 多进程是这里访问数据库会出错
        json_data = {
            "result":result,"consume_time":consume_time,"version":version,"function_type":function_type,"fail_pic":fail_pic,
            "fail_result":fail_result
        }
        requests.post(url="http://127.0.0.1:5000/result",data=json_data)
        # model.save()
    print('测试报告：%s' % report)


# def _capture_screenshot(path, filename=None):
#     global driver
#     if filename is None:
#         filename = str(time.time()*100000).split(".")[0] + ".png"
#     file_path = os.path.join(path, filename)
#     driver.save_screenshot(file_path)
#     return filename

#
# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     global driver
#     if driver is None:
#         browser_name = Config.BROWSER_NAME
#         headless = Config.HEADLESS
#         is_mobile = Config.IS_MOBILE
#         if browser_name == "chrome":
#             options = webdriver.ChromeOptions()
#             # 無頭
#             if bool(headless):
#                 options.add_argument('--headless')
#             # options.add_argument(f'--proxy-server={ProxyServer.proxy.proxy}')
#             if bool(is_mobile):
#                 options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 6/7/8'})
#             options.add_experimental_option('useAutomationExtension', False)
#             chrome_driver = basedir + "\\" + r"uiplatform\utils\data\chromedriver.exe"
#             driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
#     return driver
#
#
# @pytest.fixture(scope="session", autouse=True)
# def browser_close():
#     yield driver
#     driver.quit()

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


