# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         run_testcase.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------

from flask import Blueprint
from sqlalchemy import text
import pytest
user = Blueprint('user', __name__)
@user.route('/ui_test/run', methods=["POST"])
def test_adjjdjf():
    pytest.main(["uiplatform/utils/business/"])
    return {}

