# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         Driver.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------


import pytest
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    chrome_driver = r"D:\AutoTest\erybjp\uiplatform\utils\data\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)
    return driver


@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
