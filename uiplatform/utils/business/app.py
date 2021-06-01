# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         app.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------
import pytest

from config import basedir
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    driver = None
    browser_name = "chrome"
    headless = True
    is_mobile = True
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        # 無頭
        if bool(headless):
            options.add_argument('--headless')
        # options.add_argument(f'--proxy-server={ProxyServer.proxy.proxy}')
        if bool(is_mobile):
            options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 6/7/8'})
        options.add_experimental_option('useAutomationExtension', False)
        chrome_driver = basedir + "\\" + r"uiplatform\utils\data\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    return driver


@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()