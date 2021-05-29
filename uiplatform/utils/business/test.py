# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         test.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/28
#----------------------------
from uiplatform.utils import BaseAssert
from uiplatform.utils.logicobject.H5NormalPage import PartnerPage



def test_partnerpage(browser):
    page = PartnerPage(browser)
    page.get(page.url)
    ele = page.search_element
    BaseAssert().assert_text_in_elem("立即登录", ele, mode="accurate")



