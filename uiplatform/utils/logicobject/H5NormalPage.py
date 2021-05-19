# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         H5NormalPage.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------


from uiplatform.utils import Element
from ..common.BrowserPage import Page



class PartnerPage(Page):
    """分銷"""
    search_input = Element(id_="kw")
    search_button = Element(id_='su')


