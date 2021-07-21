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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="ID")
    type = db.Column(db.String(30), comment="定位方式")
    assert_text = db.Column(db.String(225), comment="断言表达式")
    key = db.Column(db.String(30), comment="定位方法")
    name = db.Column(db.String(50), comment="信息描述")
    value = db.Column(db.Text, comment="元素信息")
    page_class = db.Column(db.String(200), comment="对象类名称")
    index = db.Column(db.Integer, comment="定位方法的显示顺序")
    parent_id = db.Column(db.Integer, comment="用例信息表的id")
    version = db.Column(db.Integer, default=1, comment="版本迭代次数")



class Uicaseinfo(BaseModel):
    """
    用例信息表
    """
    __tablename__ = "tbl_uicase"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="ID")
    name = db.Column(db.String(30), comment="用例名称")
    description = db.Column(db.String(30), comment="用例描述信息")
    type = db.Column(db.String(30), comment="定位方式")
    deptid = db.Column(db.String(50), comment="部门唯一码")
    version = db.Column(db.String(200), comment="版本迭代次数")
    function_type = db.Column(db.String(200), comment="用例函数名称")
    class_type = db.Column(db.String(200), comment="用例函数所在的类")
    file_info = db.Column(db.String(200), comment="用例函数所在的文件名称")
    page_class_type = db.Column(db.String(200), comment="用例函数使用到的页面对象类")
    source_url = db.Column(db.Text, default=1, comment="用例对应的项目url")
    devices_type = db.Column(db.Integer, default=1, comment="1手机，2网页，3远程手机")


class Uiresultinfo(BaseModel):
    """
    用例执行结果表
    """
    __tablename__ = "tbl_uiresult"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="ID")
    case_id = db.Column(db.Integer, comment="用例id")
    result = db.Column(db.String(30), comment="用例执行结果passed,fail,skiped")
    fail_result = db.Column(db.Text, default='', comment="失败时存储的错误结果")
    fail_pic = db.Column(db.String(220), default='', comment="失败时的截图")
    title = db.Column(db.String(220), default='', comment="网页标题")
    function_type = db.Column(db.String(20), comment="用例函数名称")
    session_id = db.Column(db.String(200), comment="运行唯一值")
    current_url = db.Column(db.Text, comment="项目url")
    consume_time = db.Column(db.Integer, comment="用例执行耗时")
    version = db.Column(db.String(20), comment="版本迭代次数")



