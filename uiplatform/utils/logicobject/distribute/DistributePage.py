# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 11:10
# @Author  : Baymax
# @FileName: DistributePage.py
# @Software: PyCharm
import time

from uiplatform.utils import Element, Page
import requests

SEARCH_PARTNER_NAME = "Hhhhhhhhh"


class DistributePage(Page, Element):
    """分销者落地页对象"""
    # url = "https://partner.codemao.cn/entry"
    url_index = "https://test-growing.codemao.cn/lbk-partner/entry"

    # 分销个人详情URL
    url_partner_info = "https://test-growing.codemao.cn/lbk-partner/partner-info"

    # 分销者首页
    search_element_login_button = Element(xpath="//a[contains(text(),'立即登录')]")
    search_element_login_button_text = "立即登录"

    search_element_apply_button = Element(xpath="//a[contains(text(),'立即申请')]")
    search_element_apply_button_text = "立即申请"

    search_element_commit_button = Element(class_name="lbk-button-long__3ZL42")
    search_element_commit_button_text = "提交申请"
    commit_url = "https://test-growing.codemao.cn/lbk-partner/application"

    # 登录页面 手机号、获取验证码按钮、登录按钮
    login_page_phone = Element(class_name="tel__1qgoB")
    login_page_get_code_button = Element(class_name="get_code__2jk1L")
    login_page_password = Element(xpath="//div[contains(text(),'短信验证码')]")
    login_page_login_button = Element(class_name="login_btn__9l3Tj")

    # 分销个人详情页面
    # 活动规则按钮
    rule_button = Element(class_name="rule__2uDe9")
    rule_text = "活动规则"
    rule_page_assert = Element(class_name="header__2Q6nc")
    # 活动规则左上角 X 按钮
    close_click = Element(class_name="close__3i-U5")

    # 我的客户
    my_client_button = Element(xpath="//div[contains(text(),'我的客户')]")
    all_clues = Element(xpath="//div[contains(text(),'全部')]")
    all_clues_text = "全部"
    # 线索
    number_of_clue = Element(xpath="//div[contains(text(),'线索数')]")
    number_of_clue_text = "线索数"

    finish_class_clue = Element(xpath="//div[contains(text(),'线索完课')]")
    finish_class_clue_text = "线索完课"

    big_class_clue = Element(xpath="//div[contains(text(),'购买大课')]")
    big_class_clue_text = "购买大课"

    refunded_clue = Element(xpath="//div[contains(text(),'已退费')]")
    refunded_clue_text = "已退费"

    # 搜索客户
    search_client_input = Element(xpath="//div[contains(text(),'购买大课')]")
    search_client_button = Element(xpath="//div[contains(text(),'已退费')]")

    # 我的伙伴
    my_partner_button = Element(xpath="//div[contains(text(),'我的伙伴')]")
    search_partner_name_input = Element(xpath="//*[@id='root']/div/div[1]/div/div/input")
    search_partner_name_button = Element(class_name="search__3vLua")
    next_level = Element(class_name="next-item__1SO30")
    next_level_text = "你的下级"

    # 推广课程
    promotion_courses_button = Element(xpath="//a[contains(text(),'推广课程')]")
    promotion_courses_text = "推广课程"

    src_lesson = Element(xpath="//*[@id='root']/div/img[1]")
    src_lesson_text = "生成专属邀请码"
    code_button = Element(class_name="btn__3Qrii")

    invite_words = Element(class_name="share_btn__20oOG")
    invite_words_text = "点击复制邀请语，宝贝获得更多人鼓励"

    # 邀请伙伴
    invite_partner_button = Element(xpath="//a[contains(text(),'邀请伙伴')]")
    save_poster = Element(class_name="notice__2wvZG")
    save_poster_text = "长按保存海报"


if __name__ == '__main__':
    print(round(time.time()))
    print(round(time.time()*1000))


