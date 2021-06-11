# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         runtestcase.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------
import traceback
from time import strftime
from random import randint
from flask import Blueprint, jsonify, request
from sqlalchemy import text
import pytest, re, os
from urllib.parse import unquote
from threading import Thread
from config import basedir,Config
import uuid


user = Blueprint('user', __name__)
cur_dir = os.path.dirname(__file__).split('server')[0]


@user.route('/ui_test/test', methods=["GET"])
def run_only_test():
    session_id= uuid.uuid1()
    pares = f"--seid={session_id}"
    lista = ["uiplatform/utils/business/test_check_web.py::TestHinfo"]
    lista.append(pares)
    pytest.main(lista)
    return jsonify(code=200, msg="ok", data={"session_id":session_id})


@user.route('/ui_test/test1', methods=["GET"])
def run_only_test01():
    session_id = uuid.uuid1()
    pares = f"--seid={session_id}"
    lista = ["uiplatform/utils/business/test_check_web.py::TestHinfo1"]
    lista.append(pares)
    pytest.main(lista)
    return jsonify(code=200, msg="ok", data={"session_id": session_id})


@user.route('/ui_test/t', methods=["GET"])
def run_po_test():
    Config.IS_MOBILE = not Config.IS_MOBILE
    Config.HEADLESS = not Config.HEADLESS
    return jsonify(code=200, msg="ok", data='')
