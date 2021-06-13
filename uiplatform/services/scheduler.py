# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         scheduler.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/21
#----------------------------
import pytest

from uiplatform.utils.common.BaseLoggers import logger


def h5check_job():
    pytest.main(["-n 9", "uiplatform/utils/business/test_check_web.py"])
    logger.info("定时任务启动")
