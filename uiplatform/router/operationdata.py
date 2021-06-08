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

from extensions import db
from uiplatform.models.elemodel import UielementInfo, Uicaseinfo, Uiresultinfo
from flask import current_app as app
from flask_restful import Api,marshal_with
from serialization import model_to_dict


# 1.创建蓝图对象，url_prefix可以给蓝图添加统一的前缀url
from uiplatform.services.ali_dingtalk import DingtalkRobot

manage = Blueprint('uiplatfrom', __name__)
# 2.创建蓝图对应的api对象
restfulapi = Api(manage)
# 元素相关的视图------------------------------------------------


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
        
        paginates = Uiresultinfo.query.join(Uicaseinfo, Uiresultinfo.case_id == Uicaseinfo.id).add_entity(Uicaseinfo).filter(
            Uiresultinfo.session_id == args.get("session_id")).paginate(page=args.get("cur_page"), per_page=args.get("pagesize"), error_out=False)
        # paginates = Uiresultinfo.query.join(Uicaseinfo, Uiresultinfo.case_id == Uicaseinfo.id).add_entity(
        #     Uicaseinfo).filter(
        #     Uiresultinfo.session_id == args.get("session_id")).all()
        result = paginates.items
        json_data = model_to_dict(result)
        return jsonify(code=200, msg="ok", cur_page=paginates.page, page=paginates.pages, data=json_data)

    def post(self):
        """
        新增元素信息表数据
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
            url = "http://127.0.0.1:5000/data/picture/" + args.get("fail_pic")
            print(url)
            text = f"#### 巡检异常预警\n> 本次在运行测试用例{test_name}时探针检测失败判定页面打开失败,截图如下![screenshot]({url})\n >\n> ###### {cur_time}提示，详情点击查看 [预警截图]({url}) \n"
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
