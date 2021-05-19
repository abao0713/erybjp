# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         apptest.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------

from uiplatform.utils import Page, Element


class CalculatorPage(Page):
    number_1 = Element(id_="com.android.calculator2:id/digit_1")
    number_2 = Element(id_="com.android.calculator2:id/digit_2")
    add = Element(id_="com.android.calculator2:id/op_add")
    eq = Element(id_="com.android.calculator2:id/eq")

