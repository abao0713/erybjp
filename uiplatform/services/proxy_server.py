# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         proxy_server.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/27
#----------------------------


from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.chrome.options import Options
from config import basedir


class ProxyServer:
    proxy_driver = basedir + "\\" + r"uiplatform\utils\data\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"
    # server = Server(proxy_driver)
    # server.start()
    # proxy = server.create_proxy()