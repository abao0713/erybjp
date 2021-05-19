# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         elemodel.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------
from sqlalchemy import UniqueConstraint

from uiplatform.models.BaseModel import BaseModel
from extensions import db


class UielementInfo(BaseModel):
    """
    元素信息表
    """
    __tablename__ = "tbl_uielement_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="用户ID")
    type = db.Column(db.String(30), comment="定位方式")
    type_name = db.Column(db.String(30), comment="登录账号")
    key = db.Column(db.String(30), comment="定位方法")
    name = db.Column(db.String(50), comment="信息描述")
    value = db.Column(db.String(20), comment="元素信息")
    index = db.Column(db.Integer, comment="定位方法的显示顺序")
    userid = db.Column(db.String(20), comment="用户唯一")
    parent_id = db.Column(db.Integer, comment="父id")
    version = db.Column(db.Integer, default=1, comment="版本迭代次数")
    is_deleted = db.Column(db.Integer, default=0, comment="是否删除 0：否，1：是")
    __table_args__ = (
        UniqueConstraint('type', 'key'),  # 定位方式和定位方法唯一
    )
