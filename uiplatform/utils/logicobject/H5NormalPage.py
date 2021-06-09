# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         H5NormalPage.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/19
# ----------------------------


from uiplatform.utils import Element
from ..common.BrowserPage import Page


class PartnerPage(Page):
    """分销者落地页对象"""
    url = "https://partner.codemao.cn/entry"
    search_element = Element(xpath="//a[contains(text(),'立即登录')]")


class LbkMobilePage(Page):
    """体验课或拓展课落地页"""
    url = "https://lbk-mobile.codemao.cn/product?utm_source=h5jiulianjie&utm_term=shorturl&utm_content=default"
    search_element = Element(xpath="//div[contains(text(),'立即报名')]")


class MonthSharePage(Page):
    """月月分享落地页"""
    url = "https://activity.codemao.cn/referral/month-share"
    search_element = Element(xpath="//div[contains(text(),'规则')]")


class InvitationPage(Page):
    """家长转介绍奖励落地页"""
    url = "https://activity.codemao.cn/referral/invitation"
    search_element = Element(xpath="//div[contains(text(),'规则说明')]")


class GiveLessonPage(Page):
    """免费赠课落地页"""

    # cookie = {'name': 'authorization',
    #           'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxMTIwNzM0NiwiaXNzIjoiQXV0aCBTZXJ2aWNlIiwicGlkIjoiOUNZdGd6MTAiLCJleHAiOjE2MjcxMjU0MjQsImlhdCI6MTYyMzIzNzQyNCwianRpIjoiZjE2ZTMzODUtNmRmZi00NzhjLTlhMzQtZDQ0ZDJiOGI5MzA4In0.Zu31TOQg4c6qKu-2vebRbDlB_Mc8v1kpciSzoGhLkVM',
    #           # 'domain': 'codecamp-marketing-web.codemao.cn'
    #           }
    url_code = "https://activity.codemao.cn/referral/give-lessons?courseType=code"
    url_steam = "https://activity.codemao.cn/referral/give-lessons?courseType=stean"
    # 页面公共元素
    search_touxiang_button = Element(xpath="/html[1]/body[1]/div[1]/div[1]/div[1]", describe='头像')  # 头像栏位
    search_yaoqing_button = Element(class_name='invite-details__331Cc', describe='邀请按钮')  # 邀请按钮
    search_gonglv_button = Element(class_name='rules__2hZTP',describe='攻略按钮')  # 攻略按钮
    search_shouye_img = Element(xpath="//body/div[@id='root']/div[1]/img[3]") #首页图片
    search_shouye_state_img = Element(xpath="//body/div[@id='root']/div[1]/div[3]/img[1]") #首页状态图片
    # 登录前按钮
    search_element = Element(class_name='login-text__15JbF')
    search_login_button = Element(xpath="//body/div[@id='root']/div[1]/div[4]/div[1]", describe='底部登录按钮')
    # 登录后按钮


class GivequanPage(Page):
    """免费赠课-领券落地页"""
    url = "https://activity.codemao.cn/referral/zengke?utm_source=freegift&activityCode=CA0001&courseType=steam&utm_term=default&utm_content=default&shareID=12762488&avatar=https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLSUgn8iam94KZicFVxicg255hFe247KlgCN575YpXUibZ3SM5afD3L7oD9VawCnu5q2zgDbtsCIic2Vicg/132&nickname=%E7%85%A7"
    search_element = Element(xpath="//p[contains(text(),'你的好友')]")


# 定制课落地页龚绍来提供
class LessonOrderPage(Page):
    """付费落地页"""
    url = "https://marketing.codemao.cn/lesson-order/order?id=10"
    search_element = Element(xpath="//button[contains(text(),'确认支付')]")


class CommunityPage(Page):
    """社群进线落地页"""
    url = "https://marketing.codemao.cn/community/order?sku=219702020001 "
    search_element = Element(xpath="//button[contains(text(),'确认支付')]")


class HiorderPage(Page):
    """PC落地页"""
    url = "https://hi.codemao.cn/ "
    search_element = Element(xpath="//a[contains(text(),'立即登录')]")


class MorderPage(Page):
    """免费落地页"""
    url = "https://m.codemao.cn/v9/"
    search_element = Element(xpath="//button[contains(text(),'立即免费领取')]")


class HiCode(Page):
    """免费落地页"""
    url = "https://hi.codemao.cn/"
    search_element = Element(xpath="//*[@id='root']/div/div[2]/div/div[6]/div/div[2]/div/div[4]")
