# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         temple.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/25
#----------------------------
import jinja2

__TEMPLATE__ = jinja2.Template(
    """# NOTE: start_up{{ cur_time }}
# FROM: {{ testcase_path }}

{% if pagetype %}
from uiplatform.utils import Element
from ..common.BrowserPage import Page

{% for class_name in class_list %}
class {{ class_name }}(Page):       
        url = {{url}}
        {% for key, value in my_dict.items() %}
            search_element = Element(key=value)
        {% endfor %}
{% endfor %}
{% else %}
import pytest, time
from uiplatform.utils.common.Driver import browser, browser_close
from uiplatform.utils.logicobject.{{H5NormalPage}} import *
from uiplatform.utils.common.BaseAssert import BaseAssert
from uiplatform.services.ali_dingtalk import alidingcheck
from selenium.common.exceptions import NoSuchElementException


class TestHinfo:
    {% for class_name in class_list %}
    def test_{{class_name}}(self, browser, browser_close):
        page = PartnerPage(browser)
        page.get(page.url)
        try:
            ele = page.search_element
            BaseAssert().assert_text_in_elem({{assert_text}}, ele, mode="accurate")
        except (NoSuchElementException, AssertionError):
            print("页面元素找不到返回失败")
            filename = page.screenshots(path="uiplatform/utils/data/picture")
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            alidingcheck(filename, cur_time, page=page.url)
        PartnerPage(browser_close)

    {% endfor %}


if __name__ == "__main__":
    {{ class_name }}().test_start()

"""
)


