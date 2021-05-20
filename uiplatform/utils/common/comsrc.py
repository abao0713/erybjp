# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         comsrc.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/20
#----------------------------
from flask import jsonify

from uiplatform.models.elemodel import UielementInfo
from serialization import model_to_dict


def get_element_info(parent_id):
    element_db = UielementInfo.query.filter(UielementInfo.parent_id == parent_id, UielementInfo.type == "selenium").order_by(UielementInfo.index).all()
    json_data = model_to_dict(element_db)
    return json_data







