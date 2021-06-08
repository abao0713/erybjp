# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         免费赠课首页
# Description:
# Author:       蒋照
# Date:         2021/6/2
# ----------------------------
import pytest, time
from selenium import webdriver

from config import basedir
from uiplatform.utils.logicobject.H5NormalPage import *
from uiplatform.utils.common.BaseAssert import BaseAssert
from uiplatform.services.ali_dingtalk import alidingcheck
from selenium.common.exceptions import NoSuchElementException
from uiplatform.utils.business.driver_tst import browser, browser_close


@pytest.mark.test
class TestGiveLession:
    """免费赠课首页测试用例"""

    # 赠课首页邀请按钮,文本校验
    def test_invite_button_text(self, browser, browser_close):
        page = GiveLessonPage(browser)
        page.get(page.url_code)
        invite_button = page.search_yaoqing_button
        # BaseAssert().assert_text_in_elem("邀请明细", invite_button)
        # BaseAssert().assert_text_in_page('邀请明细', page)
        try:
            # invite_button = page.search_yaoqing_button
            # BaseAssert().assert_text_in_elem('邀请明细', invite_button)
            # BaseAssert().assert_text_in_elem_attribute('邀请明细', invite_button, 'data-element')
            BaseAssert().assert_mutil_in_list(["邀请明细"], invite_button.get_attribute('data-element'))
        except(NoSuchElementException,AssertionError):
            print("页面元素找不到返回失败")
        GiveLessonPage(browser_close)

    #  未登录情况下赠课首页邀请按钮,点击跳转URL校验
    def test_invite_button_url(self, browser, browser_close):
        page = GiveLessonPage(browser)
        page.get(page.url_code)
        page.search_yaoqing_button.click()
        time.sleep(3)
        skip = browser.current_url  # 获取跳转页面的URL
        skip_url = [skip[0:48]]
        try:
            login = 'https://lbk-mobile.codemao.cn/children-day/login'
            # print(skip_url)
            # print(type(skip_url))
            BaseAssert().assert_mutil_in_list(login, skip_url)
        except(NoSuchElementException,AssertionError):
            print("页面元素找不到返回失败")
        except(TypeError):
            print("类型错误")
        GiveLessonPage(browser_close)



if __name__ == '__main__':
    pytest.main(["-n 3", "test_givelesson.py::TestGiveLession"])
