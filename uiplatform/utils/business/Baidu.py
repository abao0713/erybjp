# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         Baidu.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------
from ..logicobject.Baidudupage import baidu_page

def baidu(text):
    baidu_page.input.clear()
    baidu_page.input.set_text(text)
    baidu_page.button.click()

