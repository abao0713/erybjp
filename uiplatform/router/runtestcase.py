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
from uiplatform.utils.business.ttest_course_puchase_h5_web import PurchasePacket
from uiplatform.utils.common.comsrc import UploadPicture
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


@user.route('/jenkins/check', methods=["post"])
def jenkins_check():
    arg = request.get_json()
    jen = TestJenkinsCompare()
    num = str(time.time()*100000).split(".")[0]
    servername_list = arg.get("servername_list")
    Thread(target=lambda: jen.aliding_jenkins(servername_list, num)).start()
    return jsonify(code=200, msg="ok", data=num)

@user.route('/uicase/autotest', methods=["post"])
def testcase_run():
    arg = request.get_json()
    # 查询指定目录下文件夹
    pass

@user.route('/buy/testpacket',methods=["get"])
def test_purchase_packet():
    '''购买非0元体验课 '''
    buy = PurchasePacket()
    message = buy.purse_price_not_zero()
    exce_result = {"message":"非0体验课购买成功"}
    if message == exce_result:
        return jsonify(code=200,success=True,message=message["message"])
    elif "图片验证码" in message:
        return jsonify(code=500,success=False,message=message["message"])
    else:
        buy.sendding_buy_testpacket()
        return jsonify(code=500,success=False,message=message["message"])

@user.route('/upload/onepicture',methods=["POST"])
def upload_picture():
    upload = UploadPicture()
    arg = request.get_json()
    pictureName = arg.get("picturename")
    print(pictureName)
    result = upload.upload_one_picture(pictureName)
    if isinstance(pictureName,str):
        if pictureName in result:
            return jsonify(code=200,success=True,picturename=result)
        else:
            return jsonify(code=500,success=False,message=result["message"])
    else:
        return jsonify(code=500, success=False, message=result["message"])
