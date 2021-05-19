# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         app.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------
import pytest
from uiplatform.utils.common.Driver import app

from uiplatform.utils.logicobject.apptest import CalculatorPage


def calculator(app):
    page = CalculatorPage(app)
    page.number_1.click()
    page.add.click()
    page.number_2.click()
    page.eq.click()
if __name__ == '__main__':
    pytest.main()