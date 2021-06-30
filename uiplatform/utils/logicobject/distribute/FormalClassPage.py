# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 11:03
# @Author  : Baymax
# @FileName: FormalClassPage.py
# @Software: PyCharm

from uiplatform.utils import Element, Page


class FormalClassPage(Page, Element):
    url = "https://test-lbk-mobile.codemao.cn/"
    advanced_course_url = "https://test-lbk-mobile.codemao.cn/integration/order?id=2130"
    switch_account_url = "https://test-lbk-mobile.codemao.cn/integration/order?id=16&termId=2842&prePageName=/"
    switch_account = Element(class_name="switch__1C9HK")
    apply_button = Element(class_name="active_button__1ST4M")
    certain_pay_button = Element(class_name="active_button__1ST4M")
    immediate_pay_button = Element(class_name="button__TWz7N")
    wechat_pay_check_button = Element(class_name="selected_icon__oli_V")
    ali_pay_check_button = Element(class_name="un_selected_icon__3oi63")
    common_pay_button = Element(class_name="button__1U5Py")
    has_payment_check = Element(class_name="payment_success__ZxqZf")
    has_payment_check_text = "已支付完成"
    ali_continue_pay = Element(class_name="v2021-btn")
    ali_continue_pay_text = "继续付款"

    certain_pay_click = Element(class_name="button__TWz7N")
    perfect_info = Element(class_name="dec__2EsPV")
    perfect_info_text = "dec__2EsPV"

