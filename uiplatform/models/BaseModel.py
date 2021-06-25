# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         BaseModel.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/19
#----------------------------


from sqlalchemy import func
from sqlalchemy.exc import InvalidRequestError

from extensions import db


class BaseModel(db.Model):
    __abstract__ = True  ## 声明当前类为抽象类，被继承，调用不会被创建
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_by = db.Column(db.String(64), default='', comment="创建者")
    created_at = db.Column(db.TIMESTAMP(True), comment="创建时间", nullable=False, server_default=func.now())
    update_by = db.Column(db.String(64), default='', comment="更新者")
    updated_at = db.Column(db.TIMESTAMP(True), comment="更新时间", nullable=False, server_default=func.now(),
                           onupdate=func.now())
    remark = db.Column(db.String(500), default='', comment="备注")
    is_deleted = db.Column(db.Integer, default=0, comment="是否删除 0：否，1：是")

    def save(self):
        '''
        新增数据
        :return:
        '''
        db.session.add(self)
        try:
            db.session.commit()
        except InvalidRequestError:
            db.session.rollback()


    def update(self):
        '''
        更新数据
        :return:
        '''
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        '''
        删除数据
        :return:
        '''
        db.session.delete(self)
        db.session.commit()

    def save_all(self, data):
        '''
        保存多条数据
        :param data:
        :return:
        '''
        db.session.execute(
            self.__table__.insert(),
            data
        )
        db.session.commit()