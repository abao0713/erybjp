# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_check_web.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/28
#----------------------------

import pytest
from uiplatform.utils import BaseAssert
from uiplatform.utils.logicobject.H5NormalPage import PartnerPage, LbkMobilePage, MonthSharePage, InvitationPage, \
    GiveLessonPage, GivequanPage, LessonOrderPage, CommunityPage, MorderPage, HiCode
from uiplatform.utils.common.Driver import browser_driver

@pytest.mark.usefixtures("seid")
class TestHinfo:
    """落地页巡检测试用例"""
    def setup_class(self):

        global driver
        driver = browser_driver(browser_name="chrome")

    def teardown_class(self):
        driver.quit()

    def test_partnerpage(self):
        page = PartnerPage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即88登录", ele, mode="accurate")



    def test_lbkmobilepage(self):
        page = LbkMobilePage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即报名", ele)

        # LbkMobilePage(browser_close)

    def test_monthmharepage(self):
        page = MonthSharePage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("规则", ele)
        # MonthSharePage(browser_close)


    def test_invitationpage(self):
        page = InvitationPage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("规则说明", ele)
        # InvitationPage(browser_close)


    def test_giveLessonpage(self):
        page = GiveLessonPage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("请登录", ele)
        page.get(page.url2)
        ele_new = page.search_element
        BaseAssert().assert_text_in_elem("请登录", ele_new)
        # GiveLessonPage(browser_close)


    def test_givequanpage(self):
        page = GivequanPage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("你的好友", ele)
        # GivequanPage(browser_close)

    # 定制课落地页龚绍来提供
    def test_lessonorderpage(self):
        page = LessonOrderPage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("确认支付", ele)
        # LessonOrderPage(browser_close)


    def test_communitypage(self):
        page = CommunityPage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("确认支付", ele)
        # CommunityPage(browser_close)

    def test_morderpage(self):
        page = MorderPage(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即免费领取", ele)
        # MorderPage(browser_close)


class TestHinfo1:

    def setup_class(self):

        global driver
        driver = browser_driver(browser_name="chrome", headless=False, is_mobile=False)

    def test_fr(self):
        page = HiCode(driver=driver)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即预约", ele)

    def teardown_class(self):
        driver.quit()







