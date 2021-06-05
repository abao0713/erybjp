# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         Driver.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------
import platform
import pytest, time, os
from config import basedir,Config
from selenium import webdriver
from config import basedir


driver = None


def browser_driver(browser_name, headless=True, is_mobile=True):
    global driver
    driver = None
    if driver is None:
        # browser_name = Config.BROWSER_NAME
        # headless = Config.HEADLESS
        # is_mobile = Config.IS_MOBILE
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            # 無頭
            if bool(headless):
                options.add_argument('--headless')
            # options.add_argument(f'--proxy-server={ProxyServer.proxy.proxy}')
            if bool(is_mobile):
                options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 6/7/8'})
            options.add_experimental_option('useAutomationExtension', False)
            if "Windows" in platform.system():
                chrome_driver = basedir + "\\" + r"uiplatform\utils\data\chromedriver.exe"
            elif "Linux" in platform.system():
                chrome_driver = basedir + "//" + r"uiplatform/utils/data/chromedriver"
            else:
                chrome_driver = basedir + "//" + r"uiplatform/utils/data/chromedriver_mac"
            driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
            print(driver.session_id)
            if not bool(is_mobile):
                driver.maximize_window()
    return driver


#
# @pytest.fixture(scope="module", autouse=True)
# def browser_close():
#     yield driver
#     driver.quit()

def _capture_screenshot(path, filename=None):
    if filename is None:
        filename = str(time.time()*100000).split(".")[0] + ".png"
    file_path = os.path.join(path, filename)
    driver.save_screenshot(file_path)
    return filename



@pytest.fixture(scope="module")
def app():
    global app_driver
    # APP定义运行环境
    desired_caps = {
        'deviceName': 'YAL_AL10',
        'automationName': 'appium',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'appPackage': 'cn.codemao.android.kids.lite',
        'appActivity': '.module.main.view.MainActivity',
    }
    app_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return app_driver


@pytest.fixture(scope="module")
def app_close():
    yield app_driver
    app_driver.quit()
