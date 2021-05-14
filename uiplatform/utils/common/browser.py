# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         browser.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/12
#----------------------------


import os.path
from configparser import ConfigParser
import logging
from selenium import webdriver

from logs.Log import MyLog
#logger = MyLog.get_log().get_logger(logger="BrowserEngine")
#logger = Log(="BrowserEngine").getlog()

log = MyLog.get_log(logger="BrowserEngine")
Logger = log.get_logger()

class BrowserEngine():
    """
    后续调用直接
    """
    dir = os.path.dirname(os.path.abspath(__file__))  # 注意相对路径获取方法
    dir_base = os.path.dirname(dir)
    chrome_driver_path = (dir_base + '/datafile/chromedriver.exe').replace("\\","/")
    ie_driver_path = (dir_base + '/datafile/IEDriverServer.exe').replace("\\","/")
    firefox_driver = (dir_base + '/datafile/geckodriver.exe').replace("\\","/")

    def __init__(self, driver):
        self.driver = driver

        # read the browser type from config_file.ini file, return the driver

    def open_browser(self, driver):
        config = ConfigParser()
        #file_path1 = os.path.dirname(os.getcwd()) + '/config_file/config.ini'
        proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        configPath = os.path.join(proDir, "config_file\config.ini")
        config.read(configPath)
        browser = config.get("browserType", "browserName")
        Logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        Logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            Logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            Logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            Logger.info("Starting IE browser.")

        driver.get(url)
        Logger.info("Open url: %s" % url)
        driver.maximize_window()
        Logger.info("Maximize the current window.")
        driver.implicitly_wait(5)
        Logger.info("Set implicitly wait 5 seconds.")
        return driver

    def quit_browser(self):
        Logger.info("Now, Close and quit the browser.")
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        Logger.info("Click forward on current page.")

    def back(self):
        self.driver.back()
        Logger.info("Click back on current page.")
