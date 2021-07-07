# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         runtestcase.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------
import time

from flask import Blueprint, jsonify, request
import pytest, os
import uuid
from threading import Thread
from uiplatform.utils.business.cycle_check.temple import auto_check_tem
from uiplatform.utils.business.cycle_check.test_jenkins_stage_production import TestJenkinsCompare
from uiplatform.utils.common.BaseLoggers import logger

user = Blueprint('user', __name__)
cur_dir = os.path.dirname(__file__).split('server')[0]


@user.route('/ui_test/test', methods=["GET"])
def run_only_test():
    session_id= uuid.uuid1()
    pares = f"--seid={session_id}"
    lista = ["uiplatform/utils/business/cycle_check/test_check_web.py::TestHinfo"]
    lista.append(pares)
    Thread(target=lambda: pytest.main(lista)).start()
    return jsonify(code=200, msg="ok", data={"session_id":session_id})


@user.route('/ui_test/test3', methods=["GET"])
def run_only_test3():
    session_id= uuid.uuid1()
    pares = f"--seid={session_id}"
    lista = ["-n 3","uiplatform/utils/business/cycle_check/test_check_web.py::TestHinfo"]
    lista.append(pares)
    Thread(target=lambda: pytest.main(lista)).start()
    return jsonify(code=200, msg="ok", data={"session_id":session_id})


@user.route('/ui_test/test1', methods=["GET"])
def run_only_test01():
    session_id = uuid.uuid1()
    pares = f"--seid={session_id}"
    lista = ["uiplatform/utils/business/cycle_check/test_check_web.py::TestHinfo1"]
    lista.append(pares)
    Thread(target=lambda: pytest.main(lista)).start()
    return jsonify(code=200, msg="ok", data={"session_id": session_id})


@user.route('/auto', methods=["put"])
def run_auto_init():
    res_data = request.get_json()
    case_id_list = res_data.get("case_id_list")
    # case_id_list = [1, 2]
    auto_check_tem(case_id_list)
    return jsonify(code=200, msg="ok", data="5262")

@user.route('/auto/run', methods=["GET"])
def run_auto():
    session_id = uuid.uuid1()
    logger.info("Page base class generation completed")

    pares1 = f"--seid={session_id}"
    lista1 = ["uiplatform/utils/business/cycle_check/test_cycle_mobile.py"]
    lista1.append(pares1)
    pytest.main(lista1)
    logger.info("testcase mobile class generation completed")

    pares = f"--seid={session_id}"
    lista = ["uiplatform/utils/business/cycle_check/test_cycle_web.py"]
    lista.append(pares)
    pytest.main(lista)
    logger.info("testcase web class generation completed")


    return jsonify(code=200, msg="ok", data={"session_id": session_id})


@user.route('/henkins/check', methods=["post"])
def jenkins_check():
    arg = request.get_json()
    jen = TestJenkinsCompare()
    num = str(time.time()*100000).split(".")[0]
    servername_list = arg.get("servername_list")
    Thread(target=lambda: jen.aliding_jenkins(servername_list, num)).start()
    return jsonify(code=200, msg="ok", data=num)

