# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         baidu.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------

from uiplatform.utils import BaiduPage
import pytest
from uiplatform.utils.business.driver_tst import browser, browser_close

@pytest.mark.skipif()
class TestBaidu:
    """百度搜索测试用例"""

    def test_baidu_search_case1(self, browser, browser_close):
        page = BaiduPage(browser)
        page.get("https://www.baidu.com")
        page.search_input = "selenium"
        page.search_button.click()
        page.screenshots(path="uiplatform/utils/data/picture")
        page.get("http://www.51testing.com/html/60/n-3724060-2.html")
        page.screenshots(path="uiplatform/utils/data/picture")
        BaiduPage(browser_close)
        page.switch_to_parent_frame()


if __name__ == '__main__':
    pytest.main()