# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         driver_tst.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------
import os
import time

import pytest
import platform
from config import basedir
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    driver = None
    browser_name = "chrome"
    headless = False
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
        if "Windows" in platform.system():
            chrome_driver = basedir + "\\" + r"uiplatform\utils\data\chromedriver.exe"
        elif "Linux" in platform.system():
            chrome_driver = basedir + "//" + r"uiplatform/utils/data/chromedriver"
        else:
            chrome_driver = basedir + "//" + r"uiplatform/utils/data/chromedriver_mac"
        driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    return driver


@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()



def _capture_screenshot(path, filename=None):
    if filename is None:
        filename = str(time.time()*100000).split(".")[0] + ".png"
    file_path = os.path.join(path, filename)
    driver.save_screenshot(file_path)
    return filename