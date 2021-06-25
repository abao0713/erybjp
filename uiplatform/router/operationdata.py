# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         operationdata.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/25
#----------------------------
import time

from flask_restful import Resource, fields, marshal_with, reqparse
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import InvalidRequestError

from config import Config
from extensions import db
from uiplatform.models.elemodel import UielementInfo, Uicaseinfo, Uiresultinfo
from flask_restful import Api,marshal_with
from serialization import model_to_dict

# 1.创建蓝图对象，url_prefix可以给蓝图添加统一的前缀url
from uiplatform.services.ali_dingtalk import DingtalkRobot

manage = Blueprint('uiplatfrom', __name__)
# 2.创建蓝图对应的api对象
restfulapi = Api(manage)
# 元素相关的视图------------------------------------------------


class CaseInfo(Resource):

    def get(self):
        """
        根据id返回查询的数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, help='用例id')
        parser.add_argument('cur_page', type=int, help='当前属于第几页')
        parser.add_argument('pagesize', type=int, help='每页显示的数量')
        args = parser.parse_args()
        if args.get("id"):
            paginates = Uicaseinfo.query.filter(Uicaseinfo.id == args.get("id"), Uiresultinfo.is_deleted == 0).paginate(
                page=args.get("cur_page"), per_page=args.get("pagesize", 3), error_out=False)
        else:
            paginates = Uicaseinfo.query.filter(
                                                  Uicaseinfo.is_deleted == 0).paginate(
                page=args.get("cur_page"), per_page=args.get("pagesize", 3), error_out=False)
        result = paginates.items
        json_data = model_to_dict(result)

        return jsonify(code=200, msg="ok", cur_page=paginates.page, page=paginates.pages, data=json_data)

    def post(self):
        """
        新增数据结果保存表数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='用例名称')
        parser.add_argument('description', type=str, help='用例详细描述')
        parser.add_argument('type', type=str, help='用例类型')
        parser.add_argument('deptid', type=str, required=True, help='部门id')
        parser.add_argument('function_type', type=str, required=True, help='用例方法名称')
        parser.add_argument('page_class_type', type=str, required=True, help='用例需要的对象类')
        parser.add_argument('source_url', type=str, required=True, help='用例对象的项目地址')
        parser.add_argument('devices_type', type=str, required=True, help='设备类型')
        parser.add_argument('update_by', required=True, type=str, help='更新人')
        parser.add_argument('create_by', required=True, type=str, help='创建人')
        args = parser.parse_args()
        model = Uicaseinfo()
        model.name = args.get("name")
        model.description = args.get("description")
        model.type = args.get("type")
        model.deptid = args.get("deptid")
        model.function_type = args.get("function_type")
        model.page_class_type = args.get("page_class_type")
        model.source_url = args.get("source_url")
        model.devices_type = args.get("devices_type")
        model.update_by = args.get("update_by")
        model.create_by = args.get("create_by")
        model.save()
        return jsonify(code=200, msg="ok", data='')


restfulapi.add_resource(CaseInfo, '/case')


class CaseElement(Resource):

    def get(self):
        """
        根据id返回查询的数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, help='每次运行唯一标识')
        parser.add_argument('cur_page', type=int, help='当前属于第几页')
        parser.add_argument('pagesize', type=int, help='每页显示的数量')
        args = parser.parse_args()
        if args.get("id"):
            paginates = UielementInfo.query.filter(UielementInfo.id == args.get("id"), UielementInfo.is_deleted == 0).paginate(
                page=args.get("cur_page"), per_page=args.get("pagesize", 3), error_out=False)
        else:
            paginates = UielementInfo.query.filter(
                UielementInfo.is_deleted == 0).paginate(
                page=args.get("cur_page"), per_page=args.get("pagesize", 3), error_out=False)
        result = paginates.items
        json_data = model_to_dict(result)

        return jsonify(code=200, msg="ok", cur_page=paginates.page, page=paginates.pages, data=json_data)

    def post(self):
        """
        新增数据结果保存表数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str, help='测试类型')
        parser.add_argument('remark', type=str, help='元素描述')
        parser.add_argument('assert_text', type=str, help='断言信息')
        parser.add_argument('key', type=str, required=True, help='定位方法')
        parser.add_argument('name', type=str, help='定位描述')
        parser.add_argument('value',required=True,  type=str, help='定位方法对应的元素信息')
        parser.add_argument('page_class',required=True,  type=str, help='页面对象类名称')
        parser.add_argument('index', required=True,  type=int, help='索引，巡检传0')
        parser.add_argument('parent_id', required=True, type=int, help='测试用例的id')
        parser.add_argument('create_by', required=True, type=str, help='创建人')
        parser.add_argument('update_by', required=True, type=str, help='更新人')
        args = parser.parse_args()
        model = UielementInfo()
        model.type = args.get("type")
        model.remark = args.get("remark")
        model.assert_text = args.get("assert_text")
        model.key = args.get("key")
        model.name = args.get("name")
        model.value = args.get("value")
        model.page_class = args.get("page_class")
        model.index = args.get("index")
        model.parent_id = args.get("parent_id")
        model.create_by = args.get("create_by")
        model.create_by = args.get("update_by")
        model.save()
        return jsonify(code=200, msg="ok", data='')


restfulapi.add_resource(CaseElement, '/element')


class CaseResult(Resource):
    def get(self):
        """
        根据id返回查询的数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('session_id', type=str,  help='每次运行唯一标识')
        parser.add_argument('cur_page', type=int, help='当前属于第几页')
        parser.add_argument('pagesize', type=int, help='每页显示的数量')
        args = parser.parse_args()
        
        # paginates = Uiresultinfo.query.join(Uicaseinfo, Uiresultinfo.case_id == Uicaseinfo.id).add_entity(Uicaseinfo).filter(
        #     Uiresultinfo.session_id == args.get("session_id")).paginate(page=args.get("cur_page"), per_page=args.get("pagesize"), error_out=False)
        if args.get("session_id"):
            paginates = Uiresultinfo.query.filter(Uiresultinfo.session_id == args.get("session_id"), Uiresultinfo.is_deleted == 0).paginate(
                page=args.get("cur_page"), per_page=args.get("pagesize", 3), error_out=False)
        else:
            paginates = Uiresultinfo.query.filter(
                                                  Uiresultinfo.is_deleted == 0).paginate(
                page=args.get("cur_page"), per_page=args.get("pagesize", 3), error_out=False)
        result = paginates.items
        case_dict_data = {}
        for re in result:
            re_data = Uicaseinfo.query.filter(Uicaseinfo.id == re.case_id).all()
            re_data_new = model_to_dict(re_data)
            case_dict_data[str(re.case_id)] = re_data_new
        json_data = model_to_dict(result)
        for json_new in json_data:
            json_new.update(case_dict_data[str(json_new["case_id"])][0])
            if "png" in json_new["fail_pic"]:
                json_new["fail_pic"] = Config.HOST+"data/picture/"+json_new["fail_pic"]

        return jsonify(code=200, msg="ok", cur_page=paginates.page, page=paginates.pages, data=json_data)

    def post(self):
        """
        新增数据结果保存表数据
        """
        parser = reqparse.RequestParser()
        parser.add_argument('result', type=str, required=True, help='测试结果')
        parser.add_argument('consume_time', type=str)
        parser.add_argument('version', type=str)
        parser.add_argument('function_type', type=str, required=True)
        parser.add_argument('title', type=str)
        parser.add_argument('current_url', type=str)
        parser.add_argument('fail_result', type=str)
        parser.add_argument('fail_pic', type=str)
        parser.add_argument('session_id', required=True, type=str)
        args = parser.parse_args()
        model = Uiresultinfo()
        caseinfo_model = Uicaseinfo.query.filter(Uicaseinfo.function_type == args.get("function_type")).first()
        model.result = args.get("result")
        model.consume_time = args.get("consume_time")
        model.version = args.get("version")
        model.case_id = caseinfo_model.id
        model.function_type = args.get("function_type")
        model.title = caseinfo_model.name
        model.current_url = caseinfo_model.source_url
        model.fail_result = args.get("fail_result")
        model.fail_pic = args.get("fail_pic")
        model.session_id = args.get("session_id")
        model.save()
        if args.get("result") == "failed":
            test_name = args.get("function_type")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            url = Config.HOST+"data/picture/" + args.get("fail_pic")
            print(url)
            text = f"#### 巡检异常预警\n> 本次在运行测试用例{test_name}时探针检测失败判定页面打开失败,截图如下![screenshot]({url})\n >\n> ###### {cur_time}提示，详情点击查看 [预警截图]({url}) \n"
            print(text)
            DingtalkRobot().send_markdown("巡检异常预警", text, [])
        return jsonify(code=200, msg="ok", data='')



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



    def patch(self):
        pass
    def delete(self):
        '''
                根据ID删除元素信息表数据
                :return:
            '''
        parser = reqparse.RequestParser()

# 3.添加类视图
restfulapi.add_resource(CaseResult, '/result')
