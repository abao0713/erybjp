# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 11:05
# @Author  : Baymax
# @FileName: test_formal_class_page_check_web.py
# @Software: PyCharm

import time
import pytest
from uiplatform.utils import BaseAssert
from uiplatform.utils.common.Driver import browser_driver
from uiplatform.utils.common.BaseLoggers import logger
from uiplatform.utils.logicobject.distribute.FormalClassPage import FormalClassPage
from uiplatform.utils.common.AddCookies import AddCookies


@pytest.mark.usefixtures("seid")
class TestFormalClassPage:

    def setup_class(self):
        global driver
        driver = browser_driver(browser_name="chrome", headless=False, is_remote=True)
        logger.info("前置处理类处理完成")

    def teardown_class(self):
        driver.quit()

    # wechat 支付
    def test_wechat_pay_formal_class(self):
        page = AddCookies().add_cookies_and_visit_url(FormalClassPage, driver, FormalClassPage.url)
        page.apply_button.click()
        page.certain_pay_button.click()
        page.immediate_pay_button.click()
        page.common_pay_button.click()
        time.sleep(5)
        BaseAssert().assert_text_in_elem(page.has_payment_check_text, page.has_payment_check, mode="accurate")
        page.has_payment_check.click()

    # ali 支付
    def test_ali_pay_formal_class(self):
        page = AddCookies().add_cookies_and_visit_url(FormalClassPage, driver, FormalClassPage.url)
        page.apply_button.click()
        page.certain_pay_button.click()
        page.immediate_pay_button.click()
        page.ali_pay_check_button.click()
        page.common_pay_button.click()
        page.ali_continue_pay.click()
        BaseAssert().assert_text_in_elem(page.ali_continue_pay_text, page.ali_continue_pay, mode="accurate")

    # 购买小火箭进阶课课包
    def test_buy_advanced_course(self):
        page = AddCookies().add_cookies_and_visit_url(FormalClassPage, driver, FormalClassPage.advanced_course_url)
        page.certain_pay_click.click()
        BaseAssert().assert_text_in_elem(page.perfect_info_text, page.perfect_info, mode="accurate")

    def test_switch_account(self):
        page = AddCookies().add_cookies_and_visit_url(FormalClassPage, driver, FormalClassPage.url)
        page.apply_button.click()
        page.certain_pay_button.click()
        page.switch_account.click()


