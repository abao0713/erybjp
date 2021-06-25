import pytest, time
from selenium import webdriver

from config import basedir
from uiplatform.utils.logicobject.H5NormalPage import *
from uiplatform.utils.common.BaseAssert import BaseAssert
from uiplatform.services.ali_dingtalk import alidingcheck
from selenium.common.exceptions import NoSuchElementException
from uiplatform.utils.business.driver_tst import browser, browser_close
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         免费赠课首页
# Description:
# Author:       蒋照
# Date:         2021/6/25
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

    # 未登录时点击页面中部按钮跳转到登录页面
    def test_invite_button1_url(self, browser, browser_close):
        page = GivequanPage(browser)
        page.get(page.url)
        page.search_lingqu1_element.click()
        time.sleep(3)
        skip = browser.current_url  # 获取跳转页面的URL
        skip_url = [skip[0:48]]
        try:
            login = 'https://lbk-mobile.codemao.cn/children-day/login'
            BaseAssert().assert_mutil_in_list(login, skip_url)
        except(NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
        except(TypeError):
            print("类型错误")
        finally:
             GiveLessonPage(browser_close)

    # 未登录时点击页面底部按钮跳转到登录页面
    def test_invite_button2_url(self, browser, browser_close):
        page = GivequanPage(browser)
        page.get(page.url)
        page.search_lingqu2_element.click()
        time.sleep(3)
        skip = browser.current_url  # 获取跳转页面的URL
        skip_url = [skip[0:48]]
        try:
            login = 'https://lbk-mobile.codemao.cn/children-day/login'
            BaseAssert().assert_mutil_in_list(login, skip_url)
        except(NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
        except(TypeError):
            print("类型错误")
        finally:
             GiveLessonPage(browser_close)

    # 未登录时点击页面底部按钮图片校验
    def test_dibubutton_img(self, browser, browser_close):
        page = GivequanPage(browser)
        page.get(page.url)
        img = 'https://online-education.codemao.cn/lbk/2/lbk-activity/images/free-btn__35bf9.png'
        # BaseAssert().assert_text_in_elem("邀请明细", invite_button)
        # BaseAssert().assert_text_in_page('邀请明细', page)
        try:
            # invite_button = page.search_yaoqing_button
            # BaseAssert().assert_text_in_elem('邀请明细', invite_button)
            # BaseAssert().assert_text_in_elem_attribute('邀请明细', invite_button, 'data-element')
            BaseAssert().assert_mutil_in_list(img, [page.search_lingqu2_element.get_attribute('src')])
        except(NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
        GiveLessonPage(browser_close)



if __name__ == '__main__':
    pytest.main(["-n 3", "test_GivequanPage.py.py"])
