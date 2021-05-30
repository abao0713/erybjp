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


user = Blueprint('user', __name__)
cur_dir = os.path.dirname(__file__).split('server')[0]


@user.route('/ui_test/run', methods=["POST"])
def run_test():
    args = request.json()

    result = request.form
    try:
        if 'cmd' not in result:
            raise Exception('请传入cmd参数')
        else:
            cmd = result['cmd']
    except Exception as e:
        return str(e)
    print(cmd)
    cmd = unquote(cmd)
    print(cmd)
    valid_re_list = [r'run_.*\.py', r'batch_run_.*\.py']
    for valid_re in valid_re_list:
        if re.findall(valid_re, cmd):
            cmd = re.sub('python ', f'python {cur_dir}', cmd)  # 执行命令加入路径
            print(cmd)
            Thread(target=lambda: os.system('start ' + cmd)).start()
            return '命令已下发'
    else:
        return '不支持该命令，请重新输入(当前仅支持%s)' % str(valid_re_list)



@user.route('/ui_test/test', methods=["GET"])
def run_only_test():
    pytest.main(["uiplatform/utils/business/test_check_web.py::TestHinfo"])
    return jsonify(code=200, msg="ok", data='')

@user.route('/ui_test/test1', methods=["GET"])
def run_only_test01():
    pytest.main(["uiplatform/utils/business/test_check_web.py::TestHinfo1"])
    return jsonify(code=200, msg="ok", data='')
@user.route('/ui_test/t', methods=["GET"])
def run_po_test():
    Config.IS_MOBILE = not Config.IS_MOBILE
    Config.HEADLESS = not Config.HEADLESS
    return jsonify(code=200, msg="ok", data='')
