# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         operationdata.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/25
#----------------------------

from flask_restful import Resource, fields, marshal_with, reqparse
from flask import Blueprint, request
from uiplatform.models.elemodel import UielementInfo,Uicaseinfo
from flask import current_app as app
from flask_restful import Api,marshal_with
from serialization import model_to_dict

# 1.创建蓝图对象，url_prefix可以给蓝图添加统一的前缀url
manage = Blueprint('eleinfo', __name__)
# 2.创建蓝图对应的api对象
restfulapi = Api(manage)
# 元素相关的视图------------------------------------------------


class EleResource(Resource):
    def get(self):
        """
        根据id返回查询的数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()
        token = request.headers["Authorization"]
        user = verify_token(token)
        id = args.get("id")
        if user is not None:
            if id :
                model = Dept.query.get(id)
                if model:
                    data = model_to_dict(model)
                    return SUCCESS(data=data)
                else:
                    return ID_NOT_FOUND()
            else:
                model = Dept.query.all()
                if model:
                    data = model_to_dict(model)
                    return SUCCESS(data=data)
                else:
                    return ID_NOT_FOUND()
        else:
            AUTH_ERR()

    def post(self):
        """
        新增元素信息表数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('dept_name', type=str, required=True,help='部门名称必填')
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('leader', type=str, required=True)
        parser.add_argument('order_num', type=str, required=True)
        parser.add_argument('parent_id', type=str, required=True)
        parser.add_argument('phone', type=str, required=True)
        parser.add_argument('remark', type=str, required=True)
        parser.add_argument('status', type=str, required=True)
        args = parser.parse_args()
        token = request.headers["Authorization"]
        user = verify_token(token)
        if args.get("dept_name"):
            try:
                is_exist = Dept.query.filter(Dept.dept_name == args["dept_name"], Dept.parent_id == args["parent_id"]).first()
                if is_exist:
                    return CREATE_ERROR(msg="同级别该部门名称已存在")
                model = Dept()
                model.dept_name = args.get("dept_name")
                model.parent_id = args.get("parent_id")
                model.leader = args.get("leader")
                model.email = args.get("email")
                model.order_num = args.get("order_num")
                model.phone = args.get("phone")
                model.remark = args.get("remark")
                model.status = args.get("status")
                model.create_by = user.get('name')
                model.save()
                return SUCCESS()
            except Exception as e:
                app.logger.error(f"新建部门失败:{e}")
                return CREATE_ERROR()
        pass
    def put(self):
        '''
            PUT方法更新元素信息表数据
            :return:
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True, help='id必填')
        parser.add_argument('dept_name', type=str, required=True, help='部门名称必填')
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('leader', type=str, required=True)
        parser.add_argument('order_num', type=str, required=True)
        parser.add_argument('parent_id', type=str, required=True)
        parser.add_argument('phone', type=str, required=True)
        parser.add_argument('remark', type=str, required=True)
        parser.add_argument('status', type=str, required=True)
        args = parser.parse_args()
        token = request.headers["Authorization"]
        user = verify_token(token)
        if args is None or user is None:
            return NO_PARAMETER()
        id = args.get("id")
        if request.method == "PUT":
            dept_name = args.get("dept_name")
            email = args.get("email")
            leader = args.get("leader")
            order_num = args.get("order_num")
            parent_id = args.get("parent_id")
            phone = args.get("phone")
            remark = args.get("remark")
            status = args.get("status")
            if id and dept_name:
                model = Dept.query.get(id)
                if model:
                    try:
                        token = request.headers["Authorization"]
                        user = verify_token(token)
                        model.dept_name = dept_name
                        model.parent_id = parent_id
                        model.leader = leader
                        model.email = email
                        model.order_num = order_num
                        model.phone = phone
                        model.status = status
                        model.remark = remark
                        model.update_by = user['name']
                        model.update()
                        return SUCCESS()
                    except Exception as e:
                        app.logger.error(f"更新部门失败:{e}")
                        return UPDATE_ERROR()
                else:
                    return ID_NOT_FOUND()
            else:
                return NO_PARAMETER()


    def patch(self):
        pass
    def delete(self):
        '''
                根据ID删除元素信息表数据
                :return:
            '''
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True, help='id必填')
        args = parser.parse_args()
        token = request.headers["Authorization"]
        user = verify_token(token)
        if args is None or user is None:
            return NO_PARAMETER()
        id = args.get("id")
        if id:
            try:
                parent = Dept.query.filter_by(parent_id=id).all()
                if parent:
                    return DELETE_ERROR(msg="该部门下存在子部门，无法删除！")
                role = Role_Dept.query.filter_by(dept_id=id).all()
                if role:
                    return DELETE_ERROR(msg="该部门已与角色关联，无法删除！")
                model = Dept.query.get(id)
                if model:
                    model.delete()
                    return SUCCESS()
                else:
                    return ID_NOT_FOUND()
            except Exception as e:
                app.logger.error(f"删除岗位失败:{e}")
                return DELETE_ERROR()
        else:
            return PARAMETER_ERR()


# 3.添加类视图
restfulapi.add_resource(EleResource, '/element')


class CaseResource(Resource):
    def get(self):
        """
        根据id返回查询的数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()
        token = request.headers["Authorization"]

    def post(self):
        """
        新增元素信息表数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('dept_name', type=str, required=True, help='部门名称必填')
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('leader', type=str, required=True)
        parser.add_argument('order_num', type=str, required=True)
        parser.add_argument('parent_id', type=str, required=True)
        parser.add_argument('phone', type=str, required=True)
        parser.add_argument('remark', type=str, required=True)
        parser.add_argument('status', type=str, required=True)

    def put(self):
        '''
            PUT方法更新元素信息表数据
            :return:
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True, help='id必填')
        parser.add_argument('dept_name', type=str, required=True, help='部门名称必填')
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('leader', type=str, required=True)
        parser.add_argument('order_num', type=str, required=True)
        parser.add_argument('parent_id', type=str, required=True)
        parser.add_argument('phone', type=str, required=True)
        parser.add_argument('remark', type=str, required=True)
        parser.add_argument('status', type=str, required=True)
        args = parser.parse_args()
        token = request.headers["Authorization"]
        user = verify_token(token)
        if args is None or user is None:
            return NO_PARAMETER()


    def patch(self):
        pass
    def delete(self):
        '''
                根据ID删除元素信息表数据
                :return:
            '''
        parser = reqparse.RequestParser()

# 3.添加类视图
restfulapi.add_resource(CaseResource, '/element')


