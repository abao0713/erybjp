# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         BaseModel.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------


from sqlalchemy import func
from extensions import db


class BaseModel(db.Model):
    __abstract__ = True  ## 声明当前类为抽象类，被继承，调用不会被创建
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_by = db.Column(db.String(64), comment="创建者")
    created_at = db.Column(db.TIMESTAMP(True), comment="创建时间", nullable=False, server_default=func.now())
    update_by = db.Column(db.String(64), comment="更新者")
    updated_at = db.Column(db.TIMESTAMP(True), comment="更新时间", nullable=False, server_default=func.now(),
                           onupdate=func.now())
    remark = db.Column(db.String(500), comment="备注")
