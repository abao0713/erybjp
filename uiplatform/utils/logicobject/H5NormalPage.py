# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         H5NormalPage.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/19
# ----------------------------


from uiplatform.utils import Element
from uiplatform.utils.common import Elements
from uiplatform.utils.common.BrowserPage import Page


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
    # 未登录时展示元素
    search_lingqu1_element = Element(xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]",describe='页面中间领取按钮')
    search_lingqu2_element = Element(xpath="/html[1]/body[1]/div[1]/div[1]/div[3]/img[1]",describe='底部领取按钮')

class  lbk_operational(Page):
    """运营后台-新增课包"""
    url_home = 'https://test-lbk-operational.codemao.cn/packages'
    #跳转到登录页面
    url_login = 'https://test-internal-account.codemao.cn/login'
    admin_css = '[placeholder~=用户名]'
    pwd_css = '[placeholder~=密码]'
    submit_login_button = '.ant-btn'
    adm_pwd = 'rc-tabs-0-tab-2'

    # 跳转 https://test-lbk-operational.codemao.cn/packages/add
    # add_package_button_css = 'ant-btn ant-btn-primary'
    # add_package_button_class = 'ant-btn ant-btn-primary'
    add_package_button_xpath = '//*[@id="root"]/div/section/div[2]/main/div[2]/div/section[1]/div/div[1]/a/button'
    package_new_name_css = '[placeholder ~=请输入课程名称，限制20个字以内 ]'
    content_list = '#contentType'  # 主要内容类型,包含编程课，艺术课，数学课,工程思维
    teaching_platform = '[title ~= 教学平台]'  # NEMO KIDS IDE BOX2
    businessType_css = '#businessType'  # 业务类型
    attribute_css = '#attribute'  # 课包属性
    submit_add_package = '.ant-btn ant-btn-primary'





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
    search_element = Element(xpath="//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]")

class  Jenkins(Page):
       url_login = "https://jenkins.codemao.cn/login"  #登录页
       host = "https://jenkins.codemao.cn" #jenkins的域名,用于登录之后重定向
       username_element = Element(css = "#j_username") #登录用户名
       password_element = Element(css = "input[name='j_password']")#登录密码
       button_element = Element(css = ".submit-button") #登录按钮
       ele_search = Element(css = "form[role='search'] #search-box") #服务搜索框
       ele_server_gather = Elements(css = '.yui-ac-bd>ul>li')  #各个环境服务集合
       new_staging_bulid_element = Element(css='.build-search-row+tr [class="pane build-name"]') #staging环境服务最新构建编号
       new_production_built_element = Element(css='.build-search-row+tr [class="pane build-name"]') #production环境服务最新构建编号
       product_para_element = Element(css="a[title='Parameters']")
       new_production_built_data = Element(css = '.pane>tbody:nth-of-type(2) .setting-input')
