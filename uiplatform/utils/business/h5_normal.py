# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         h5_normal.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------
import pytest, time
from selenium import webdriver

from config import basedir
from uiplatform.utils.logicobject.H5NormalPage import *
from uiplatform.utils.common.BaseAssert import BaseAssert
from uiplatform.services.ali_dingtalk import alidingcheck
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        browser_name = "chrome"
        headless = False
        is_mobile = False
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            # 無頭
            if bool(headless):
                options.add_argument('--headless')
            # options.add_argument(f'--proxy-server={ProxyServer.proxy.proxy}')
            if bool(is_mobile):
                options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 6/7/8'})
            options.add_experimental_option('useAutomationExtension', False)
            chrome_driver = basedir + "\\" + r"uiplatform\utils\data\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    return driver


@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()



class TestHinfo:
    """落地页巡检测试用例"""

    def test_partnerpage(self, browser,browser_close):
        page = PartnerPage(browser)
        page.get(page.url)

        ele = page.search_element
        BaseAssert().assert_text_in_elem("立即登录", ele, mode="accurate")
        # except (NoSuchElementException, AssertionError):
        #     print("页面元素找不到返回失败")
            # filename = page.screenshots(path="uiplatform/utils/data/picture")
            # cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            # alidingcheck(filename, cur_time, page=page.url)
        PartnerPage(browser_close)


    def test_lbkmobilepage(self, browser, browser_close):
        page = LbkMobilePage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem("立即报名", ele)
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time)
        LbkMobilePage(browser_close)

    def test_monthmharepage(self, browser, browser_close):
        page = MonthSharePage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem("规则", ele)
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time)
        MonthSharePage(browser_close)


    def test_invitationpage(self, browser, browser_close):
        page = InvitationPage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem("规则说明", ele)
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time)
        InvitationPage(browser_close)


    def test_giveLessonpage(self, browser, browser_close):
        page = GiveLessonPage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem("请登录", ele)
            page.get(page.url2)
            ele = page.search_element
            BaseAssert().assert_text_in_elem("请登录", ele)
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time)
        GiveLessonPage(browser_close)


    def test_givequanpage(self, browser, browser_close):
        page = GivequanPage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem("你的好友", ele)
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time)
        GivequanPage(browser_close)

    # 定制课落地页龚绍来提供
    def test_lessonorderpage(self, browser, browser_close):
        page = LessonOrderPage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem("确认支付", ele)
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time)
        LessonOrderPage(browser_close)


    def test_communitypage(self, browser, browser_close):
        page = CommunityPage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem("确认支付", ele)
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time)
        CommunityPage(browser_close)

    def test_morderpage(self, browser, browser_close):
        page = MorderPage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem("立即免费领取", ele)
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time)
        MorderPage(browser_close)


if __name__ == '__main__':
    pytest.main(["-n 5"])
