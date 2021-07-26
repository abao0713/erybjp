# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 11:10
# @Author  : Baymax
# @FileName: DistributePage.py
# @Software: PyCharm


import time
import pytest
from uiplatform.utils import BaseAssert
from uiplatform.utils.logicobject.distribute.DistributePage import DistributePage, SEARCH_PARTNER_NAME
from uiplatform.utils.common.Driver import browser_driver
from uiplatform.utils.common.BaseLoggers import logger
from uiplatform.utils.common.AddCookies import AddCookies


@pytest.mark.usefixtures("seid")
class TestDistribute:
    """分销落地页巡检测试用例"""

    def setup_class(self):
        global driver
        driver = browser_driver(browser_name="chrome", headless=False)
        logger.info("前置处理类处理完成")

    def teardown_class(self):
        driver.quit()

    # 立即登录页面
    def test_login(self):
        page = DistributePage(driver=driver)
        page.get(page.url_index)
        ele = page.search_element_login_button
        BaseAssert().assert_text_in_elem(page.search_element_login_button_text, ele, mode="accurate")

    # 立即申请
    def test_apply_user(self):
        page = DistributePage(driver=driver)
        page.get(page.url_index)
        ele = page.search_element_apply_button
        BaseAssert().assert_text_in_elem(page.search_element_apply_button_text, ele, mode="accurate")
        page.search_element_apply_button.click()
        ele = page.search_element_commit_button
        BaseAssert().assert_text_in_elem(page.search_element_commit_button_text, ele, mode="accurate")

    # 个人详细页面--活动规则
    def test_activity_rule_page(self):
        page = AddCookies().add_cookies_and_visit_url(DistributePage, driver, DistributePage.url_partner_info)
        # 点击活动规则
        page.rule_button.click()
        BaseAssert().assert_text_in_elem(page.rule_text, page.rule_page_assert, mode="accurate")
        page.close_click.click()

    # 我的客户
    def test_my_client_page(self):
        page = AddCookies().add_cookies_and_visit_url(DistributePage, driver, DistributePage.url_partner_info)
        page.my_client_button.click()
        page.all_clues.click()
        BaseAssert().assert_text_in_elem(page.all_clues_text, page.all_clues, mode="accurate")

        page.number_of_clue.click()
        BaseAssert().assert_text_in_elem(page.number_of_clue_text, page.number_of_clue, mode="accurate")

        page.finish_class_clue.click()
        BaseAssert().assert_text_in_elem(page.finish_class_clue_text, page.finish_class_clue, mode="accurate")

        page.big_class_clue.click()
        BaseAssert().assert_text_in_elem(page.big_class_clue_text, page.big_class_clue, mode="accurate")

        page.refunded_clue.click()
        BaseAssert().assert_text_in_elem(page.refunded_clue_text, page.refunded_clue, mode="accurate")

    # 推广课程
    def test_popularize_lesson(self):
        page = AddCookies().add_cookies_and_visit_url(DistributePage, driver, DistributePage.url_partner_info)
        BaseAssert().assert_text_in_elem(page.promotion_courses_text, page.promotion_courses_button, mode="accurate")
        page.promotion_courses_button.click()
        page.src_lesson.click()
        page_source = page.get_page_source()
        BaseAssert().assert_text_in_page(page.src_lesson_text, page_source)
        page.code_button.click()
        BaseAssert().assert_text_in_elem(page.invite_words_text, page.invite_words, mode="accurate")

    # 我的伙伴
    def test_my_partner_page(self):
        page = AddCookies().add_cookies_and_visit_url(DistributePage, driver, DistributePage.url_partner_info)
        page.my_partner_button.click()
        page.search_partner_name_input.send_keys(SEARCH_PARTNER_NAME)
        page.search_partner_name_button.click()
        page_source = page.get_page_source()
        time.sleep(2)
        BaseAssert().assert_text_in_page(SEARCH_PARTNER_NAME, page_source)
        page.next_level.click()

    # 邀请伙伴
    def test_invite_partner(self):
        page = AddCookies().add_cookies_and_visit_url(DistributePage, driver, DistributePage.url_partner_info)
        page.invite_partner_button.click()
        BaseAssert().assert_text_in_elem(page.save_poster_text, page.save_poster, mode="accurate")

    def test_commit(self):
        pass








