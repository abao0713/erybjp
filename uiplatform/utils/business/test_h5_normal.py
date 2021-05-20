# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         test_h5_normal.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------
import pytest
from uiplatform.utils.common.Driver import browser, browser_close
from uiplatform.utils.logicobject.H5NormalPage import *
from uiplatform.utils.common.BaseAssert import BaseAssert

@pytest.mark.test
class TestHinfo:
    """落地页巡检测试用例"""

    def test_partnerpage(self, browser, browser_close):
        page = PartnerPage(browser)
        page.get(page.url)
        ele = page.search_element
        if BaseAssert().assert_text_in_elem("立即登录", ele):
            print("tong")
        page.screenshots(path="uiplatform/utils/data/picture")
        PartnerPage(browser_close)


    def test_lbkmobilepage(self, browser, browser_close):
        page = LbkMobilePage(browser)
        page.get(page.url)
        ele = page.search_element
        if BaseAssert().assert_text_in_elem("立即报名", ele):
            print("tong")
        page.screenshots(path="uiplatform/utils/data/picture")
        LbkMobilePage(browser_close)

    def test_monthmharepage(self, browser, browser_close):
        page = MonthSharePage(browser)
        page.get(page.url)
        ele = page.search_element
        if BaseAssert().assert_text_in_elem("规则", ele):
            print("tong")
        page.screenshots(path="uiplatform/utils/data/picture")
        MonthSharePage(browser_close)


    def test_invitationpage(self, browser, browser_close):
        page = InvitationPage(browser)
        page.get(page.url)
        ele = page.search_element
        if BaseAssert().assert_text_in_elem("规则说明", ele):
            print("tong")
        page.screenshots(path="uiplatform/utils/data/picture")
        InvitationPage(browser_close)


    def test_giveLessonpage(self, browser, browser_close):
        page = GiveLessonPage(browser)
        page.get(page.url)
        ele = page.search_element
        if BaseAssert().assert_text_in_elem("请登录", ele):
            print("tong")
        page.get(page.url2)
        ele = page.search_element
        if BaseAssert().assert_text_in_elem("请登录", ele):
            print("tong")
        page.screenshots(path="uiplatform/utils/data/picture")
        GiveLessonPage(browser_close)


    def test_givequanpage(self, browser, browser_close):
        page = GivequanPage(browser)
        page.get(page.url)
        ele = page.search_element
        if BaseAssert().assert_text_in_elem("你的好友", ele):
            print("tong")
        page.screenshots(path="uiplatform/utils/data/picture")
        GivequanPage(browser_close)



if __name__ == '__main__':
    pytest.main(["--html=report.html"])
