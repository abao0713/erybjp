# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         run_testcase.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------
import traceback
from time import strftime
from random import randint
from flask import Blueprint, jsonify, request
from sqlalchemy import text
import pytest
user = Blueprint('user', __name__)



# @user.route('/ui_test/run', methods=["POST"])
# def test_adjjdjf():
#     # pytest命令参数
#     args = request.get_json()
#     dir_time = strftime('%Y%m%d_%H%M%S')
#     session_id = f'{dir_time}_{randint(10, 99)}'
#     try:
#         report_file = rf'uiplatform/utils/data/report/{session_id}/{dir_time}/report.html'
#         pytest_args = [rf'--html={report_file}', '--self-contained-html', f'--reruns=1']
#
#         # 使用testsuite.yaml定义的用例运行
#         parent_case_dir = rf'{product_path}/testcase/web/'
#         if args.testsuite:
#             suite_path = f'{parent_case_dir}{args.testsuite}'
#             for testcase in get_yaml(suite_path)['testcase']:
#                 if isinstance(testcase, list):
#                     testcase = testcase[0]
#                 pytest_args.append(parent_case_dir + testcase)  # 加入用例参数
#         # 指定用例目录或用例文件运行
#         elif dir:
#             dir_list = dir.split(' ')
#             for d in dir_list:
#                 each_case_dir = parent_case_dir + d
#                 pytest_args.append(each_case_dir)
#         # 不定义testsuite和dir，使用默认目录运行
#         else:
#             pytest_args.append(parent_case_dir)
#         # 添加用例标记
#         if mark:
#             pytest_args.append(f'-m {mark}')
#         # 运行
#         print(pytest_args)
#         pytest.main(pytest_args)
#     except:
#         traceback.print_exc()
#     finally:
#     # 单个运行完成后，立即发送报告
#         pass
#     return jsonify(code=200, msg="ok", data='')

@user.route('/ui_test/element_info', methods=["GET"])
def test_adjjdjf():
    pytest.main(["uiplatform/utils/business/"])
    return jsonify(code=200, msg="ok", data='')
