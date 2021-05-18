# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         test_baidu.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------

from uiplatform.utils import BaiduPage
import pytest
from uiplatform.utils.common.Driver import browser

@pytest.mark.test1
class TestBaidu:
    """百度搜索测试用例"""

    def test_baidu_search_case1(self, browser):
        page = BaiduPage(browser)
        page.get("https://www.baidu.com")
        page.search_input = "selenium"
        page.search_button.click()


if __name__ == '__main__':
    pytest.main()