# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_check_web.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/28
#----------------------------
from uiplatform.utils import BaseAssert
from uiplatform.utils.logicobject.H5NormalPage import PartnerPage, LbkMobilePage, MonthSharePage, InvitationPage, \
    GiveLessonPage, GivequanPage, LessonOrderPage, CommunityPage, MorderPage, BaiDu
import pytest
from uiplatform.utils.common.Driver import browser,browser_close, browser1
# from uiplatform.utils.common.Driver import  browser,browser1,browser_close
@pytest.mark.usefixtures("browser")
class TestHinfo:
    """落地页巡检测试用例"""

    def test_partnerpage(self, browser, browser_close):
        page = PartnerPage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即88登录", ele, mode="accurate")
        PartnerPage(browser_close)


    def test_lbkmobilepage(self, browser, browser_close):
        page = LbkMobilePage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即报名", ele)

        # LbkMobilePage(browser_close)

    def test_monthmharepage(self, browser, browser_close):
        page = MonthSharePage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("规则", ele)
        # MonthSharePage(browser_close)


    def test_invitationpage(self, browser, browser_close):
        page = InvitationPage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("规则说明", ele)
        # InvitationPage(browser_close)


    def test_giveLessonpage(self, browser, browser_close):
        page = GiveLessonPage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("请登录", ele)
        page.get(page.url2)
        ele_new = page.search_element
        BaseAssert().assert_text_in_elem("请登录", ele_new)
        # GiveLessonPage(browser_close)


    def test_givequanpage(self, browser, browser_close):
        page = GivequanPage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("你的好友", ele)
        # GivequanPage(browser_close)

    # 定制课落地页龚绍来提供
    def test_lessonorderpage(self, browser, browser_close):
        page = LessonOrderPage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("确认支付", ele)
        # LessonOrderPage(browser_close)


    def test_communitypage(self, browser, browser_close):
        page = CommunityPage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("确认支付", ele)
        # CommunityPage(browser_close)

    def test_morderpage(self, browser, browser_close):
        page = MorderPage(browser)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即免费领取", ele)
        # MorderPage(browser_close)

@pytest.mark.usefixtures("browser1")
class TestHinfo1:
    def test_fr(self, browser1):
        page = BaiDu(browser1)
        page.get(page.url)
        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即预约", ele)
