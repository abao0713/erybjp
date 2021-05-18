# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         Baidudupage.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------
from uiplatform.utils import Element
from ..common.BrowserPage import Page



class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    search_input = Element(id_="kw")
    search_button = Element(id_='su')


