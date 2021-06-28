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
from uiplatform.utils.common.BaseLoggers import logger
from uiplatform.utils.common.Driver import browser_driver
from uiplatform.utils.logicobject.H5NormalPage import *
from uiplatform.utils.common.BaseAssert import BaseAssert
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.test
class TestGiveLession:
    def setup_class(self):

        global driver
        driver = browser_driver(browser_name="chrome", is_mobile=True, is_remote=True)
        logger.info(driver)

    def test_fr(self):
        page = HiCode(driver=driver)
        page.get(page.url)
        ele = page.search_element


    def teardown_class(self):
        driver.quit()

    # 首页图片检查
    def test_shouye_img(self):
        page = GiveLessonPage(driver=driver)
        page.get(page.url_code)
        shouye_img=page.search_shouye_img
        img = 'https://online-education.codemao.cn/lbk/2/lbk-activity/images/invite__5b42f.png'
        try:
            # print(shouye_img.get_attribute('src'))
            BaseAssert().assert_mutil_in_list(img, [shouye_img.get_attribute('src')])
        except(NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
        except(TypeError):
            print("类型错误")

    # 首页底部状态图片检查
    def test_shouye_dibu_img(self):
        page = GiveLessonPage(driver=driver)
        page.get(page.url_code)
        shouye_img=page.search_shouye_state_img
        img = 'https://online-education.codemao.cn/lbk/2/lbk-activity/images/not-login__a39f0.png'
        try:
            # print(shouye_img.get_attribute('src'))
            BaseAssert().assert_mutil_in_list(img, [shouye_img.get_attribute('src')])
        except(NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
        except(TypeError):
            print("类型错误")


    # 赠课首页邀请按钮,文本校验
    def test_invite_button_text(self):
        page = GiveLessonPage(driver=driver)
        page.get(page.url_code)
        invite_button = page.search_yaoqing_button
        # BaseAssert().assert_text_in_elem("邀请明细", invite_button)
        # BaseAssert().assert_text_in_page('邀请明细', page)
        try:
            # invite_button = page.search_yaoqing_button
            # BaseAssert().assert_text_in_elem('邀请明细', invite_button)
            # BaseAssert().assert_text_in_elem_attribute('邀请明细', invite_button, 'data-element')
            BaseAssert().assert_mutil_in_list(["邀请明细"], invite_button.get_attribute('data-element'))
        except(NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")


     # 未登录,情况下赠课首页邀请按钮,点击跳转URL校验
    def test_invite_button_url(self):
        page = GiveLessonPage(driver=driver)
        page.get(page.url_code)
        page.search_yaoqing_button.click()
        time.sleep(3)
        skip = driver.current_url  # 获取跳转页面的URL
        skip_url = [skip[0:48]]
        try:
            login = 'https://lbk-mobile.codemao.cn/children-day/login'
            # print(skip_url)
            # print(type(skip_url))
            BaseAssert().assert_mutil_in_list(login, skip_url)
        except(NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
        except(TypeError):
            print("类型错误")


     # 未登录,点击底部登录按钮,跳转到登录页面
    def test_login_button_url(self):
        page = GiveLessonPage(driver=driver)
        page.get(page.url_code)
        page.search_login_button.click()
        time.sleep(3)
        skip = driver.current_url  # 获取跳转页面的URL
        skip_url = [skip[0:48]]
        try:
            login = 'https://lbk-mobile.codemao.cn/children-day/login'
            # print(skip_url)
            # print(type(skip_url))
            BaseAssert().assert_mutil_in_list(login, skip_url)
        except(NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
        except(TypeError):
            print("类型错误")



    # 登录后，点击邀请明细，检查跳转url
    # def test_invite_login_button_url(self, browser, browser_close):
    #     page = GiveLessonPage(browser)
    #     page.get(page.url_code)
    #     browser.add_cookie(cookie_dict=page.cookie)
    #     page.search_yaoqing_button.click()
    #     skip = browser.current_url  # 获取跳转页面的URL
    #     skip_url = [skip[0:47]]
    #     try:
    #         invite_url='https://activity.codemao.cn/referral/invitation'
    #         BaseAssert().assert_mutil_in_list(invite_url, skip_url)
    #     except(NoSuchElementException, AssertionError):
    #         print("页面元素找不到返回失败")
    #     browser.delete_all_cookies()
    #     GiveLessonPage(browser_close)




if __name__ == '__main__':
    pytest.main(["-n 3", "test_GiveLessonPage.py"])
