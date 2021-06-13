# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         temple.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/25
#----------------------------
import os
import time

import jinja2
from serialization import model_to_dict
from uiplatform.models.elemodel import UielementInfo, Uicaseinfo
from uiplatform.utils.common.BaseLoggers import logger

__TEMPLATEPAGE__ = jinja2.Template(
    """# NOTE: start_up{{ cur_time }}
# FROM: yuanbaojun

from uiplatform.utils import Element
from uiplatform.utils.common.BrowserPage import Page
{% for class_dict in class_list %}
    {% for key, value in class_dict.items() %}
class {{ key }}(Page):       
        url = "{{value[2]}}"
        search_element = Element({{value[0]}}="{{value[1]}}")
    {% endfor %}       
{% endfor %}
""")

__TEMPLATECASE__ = jinja2.Template(
    """# NOTE: start_up{{ cur_time }}
# FROM: yuanbaojun
import pytest
from uiplatform.utils import BaseAssert
from uiplatform.utils.logicobject.cycle_check.page_cycle_auto import *
from uiplatform.utils.common.Driver import browser_driver
from uiplatform.utils.common.BaseLoggers import logger


@pytest.mark.usefixtures("seid")
class TestAutoCycle:
    
    {% if devicetype %}
    def setup_class(self):

        global driver
        driver = browser_driver(browser_name="chrome")
        logger.info("前置处理类处理完成")
    {% else %}
    def setup_class(self):

        global driver
        driver = browser_driver(browser_name="chrome", is_mobile=False)
        logger.info(driver)
    
    {% endif %}
    def teardown_class(self):
        driver.quit()
   
       
    {% for class_name in test_class_list %}
        {% for key, value in class_name.items() %}
    def {{key}}(self):
        page = {{value[0]}}(driver=driver)
        page.get(page.url)
        ele = page.search_element
        {% endfor %}
    {% endfor %}


"""
)


def auto_check_tem(case_id_list):
    sign = {
        "page": True,
        "business1": True,
        "business2": True
    }
    if isinstance(case_id_list, list):
        page_class_list = []
        test_class1_list = []
        test_class2_list = []
        case_device1 = []
        case_device2 = []
        case_device3 = []
        for case_id in case_id_list:
            pageobject_result = UielementInfo.query.filter(UielementInfo.index == 0, UielementInfo.parent_id == case_id, UielementInfo.is_deleted == 0).first()
            pageobject_json_data = model_to_dict(pageobject_result)
            business_result = Uicaseinfo.query.filter(Uicaseinfo.id == case_id, Uicaseinfo.is_deleted == 0).first()
            business_json_data = model_to_dict(business_result)
            data_dict = {
                pageobject_json_data["page_class"]: [pageobject_json_data["key"], pageobject_json_data["value"], business_json_data["source_url"]]
            }
            page_class_list.append(data_dict)

            # 只做数据渲染时的隔离
            if business_json_data["devices_type"] == 1:
                case_device1.append(case_id)
                data_dict1 = {
                    business_json_data["function_type"]: [business_json_data["page_class_type"]]
                }
                test_class1_list.append(data_dict1)
            elif business_json_data["devices_type"] == 2:
                case_device2.append(case_id)
                data_dict2 = {
                    business_json_data["function_type"]: [business_json_data["page_class_type"]]
                }
                test_class2_list.append(data_dict2)
            else:
                case_device3.append(case_id)
        # 生成页面类
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data = {
            "cur_time": cur_time,
            "class_list": page_class_list

        }
        content_page = __TEMPLATEPAGE__.render(data)
        dir_path_page = "uiplatform/utils/logicobject/cycle_check/page_cycle_auto.py"
        if dir_text_create(dir_path_page=dir_path_page, content=content_page):
            sign["page"] = False

        if len(case_device1) > 0:
            data1 = {
                "cur_time": cur_time,
                "test_class_list": test_class1_list,
                "devicetype": True
            }
            content_case1 = __TEMPLATECASE__.render(data1)
            dir_path_page = "uiplatform/utils/business/cycle_check/test_cycle_mobile.py"
            if dir_text_create(dir_path_page=dir_path_page, content=content_case1):
                sign["business1"] = False
        if len(case_device2) > 0:
            data2 = {
                "cur_time": cur_time,
                "test_class_list": test_class2_list,
                "devicetype": False
            }
            content_case2 = __TEMPLATECASE__.render(data2)
            dir_path_page = "uiplatform/utils/business/cycle_check/test_cycle_web.py"
            if dir_text_create(dir_path_page=dir_path_page, content=content_case2):
                sign["business2"] = False

        if len(case_device3) > 0:
            pass
    else:
        logger.info("The input parameter of function is not in list format")
    return sign


def dir_text_create(dir_path_page, content):
    """
    :param dir_path_page: 文件路径
    :param content: 写入内容
    :return:
    """
    sign = False
    dir_path = os.path.dirname(dir_path_page)
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(dir_path_page, "w", encoding="utf-8") as f:
            f.write(content)
        return sign
    except Exception as e:
        logger.info(e)
        return True



if __name__ == '__main__':
    a = [1]
    f = auto_check_tem(a)

