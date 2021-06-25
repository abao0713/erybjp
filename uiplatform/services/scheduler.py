# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         scheduler.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/21
#----------------------------
import socket
import time
from threading import Thread
import pytest
from uiplatform.utils.common.BaseLoggers import logger


def h5check_job():
    logger.info("定时任务启动")
    session_id = str(time.time()*100000).split(".")[0]
    pares = f"--seid={session_id}"
    lista = ["uiplatform/utils/business/cycle_check/test_check_web.py"]
    lista.append(pares)
    Thread(target=lambda: pytest.main(lista)).start()
