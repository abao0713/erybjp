# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         JenstaPage.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/6/18
#----------------------------

from uiplatform.utils import Element
from uiplatform.utils.common.BrowserPage import Page


class JenStaging(Page):
    url = "https://jenkins.codemao.cn/login"
    user_input = Element(id_="j_username")
    password_input = Element(xpath="//body/div[1]/div[1]/form[1]/div[2]/input[1]")
    longin = Element(xpath="//body/div[1]/div[1]/form[1]/div[3]/input[1]")
