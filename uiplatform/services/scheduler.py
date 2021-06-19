# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         scheduler.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/21
#----------------------------
import socket

import pytest

from uiplatform.utils.common.BaseLoggers import logger


def h5check_job():
    pytest.main(["uiplatform/utils/business/cycle_check/test_check_web.py"])
    logger.info("定时任务启动")
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(ip)
