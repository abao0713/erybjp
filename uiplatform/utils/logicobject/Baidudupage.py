# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         Baidudupage.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------

from ..common.BasePage import Element
from ..common.Browser import Page


class BaiduPage(Page):
    # 百度查詢
    input = Element(id="kw",describe="頁面輸入框")
    button = Element(id="su")



driver = None
url = "https://www.baidu.com/"
baidu_page = BaiduPage(driver, url=url)