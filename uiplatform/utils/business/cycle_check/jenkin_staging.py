# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         jenkin_staging.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/6/18
#----------------------------
import pytest

from uiplatform.utils.common.BaseLoggers import logger
from uiplatform.utils.common.Driver import browser_driver
from uiplatform.utils.logicobject.jenkins_dingding.JenstaPage import JenStaging


class TestJenSta:

    def setup_class(self):
        global driver
        driver = browser_driver(browser_name="chrome", is_mobile=False)
        logger.info(driver)

    def test_sta_jen(self):
        """
        识别jenkins构建是否占用
        :return:
        """
        page = JenStaging(driver=driver)
        page.get(page.url)
        page.user_input.clear()
        page.user_input="yuanbaojun"

if __name__ == '__main__':
    pytest.main(["jenkin_staging.py"])