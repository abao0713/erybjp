# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         Driver.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------


import pytest
from selenium import webdriver
from config import basedir


def config_browser():
    pass


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    options = webdriver.ChromeOptions()
    # 無頭
    options.add_argument('--headless')
    options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 6/7/8'})
    a=basedir
    chrome_driver = basedir+"\\"+r"uiplatform\utils\data\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    return driver


@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
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


@pytest.fixture(autouse=True)
def app_close():
    yield app_driver
    app_driver.quit()
