# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         BaseAssert.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/18
#----------------------------
import os
from assertpy import assert_that

class BaseAssert:
    def assert_text_in_page(self, text, page):
        """判断文本在页面中存在，支持多个文本"""
        if not isinstance(text, list):
            text = [text]
        for i in text:
            assert_that(page).contains(i)


    def assert_text_not_in_page(self, text, page):
        """判断文本在页面中不存在，支持多个文本"""
        if not isinstance(text, list):
            text = [text]
        for i in text:
            assert_that(page).does_not_contain(i)

    # 没有问题的方法
    def assert_text_in_elem(self, text, elem, mode='vague'):
        """
        判断元素包含文本，支持多个文本，支持模糊/精确匹配
        :param text: 待校验文本
        :param elem: 待校验元素
        :param mode: 校验模式，只支持vague/accurate
        :return:
        """
        page = elem.text
        if not text:
            pass
        if mode not in ('vague', 'accurate'):
            raise Exception('mode: 校验模式，只支持part/all')
        if not isinstance(text, list):
            text = [text]
        if mode == 'vague':
            for i in text:
                assert i in page, f"字符{i}存在于字符{page}"
        else:
            if isinstance(page, str):
                assert text[0] == page, f"字符{text[0]}等于字符{page}"
            else:
                assert text[0] == str(page), f"字符{text[0]}等于字符{page}"


    def assert_text_not_in_elem(self, text, elem, mode='part'):
        """
        判断元素不包含文本，支持多个文本，支持模糊/精确匹配
        :param text: 待校验文本
        :param elem: 待校验元素
        :param mode: 校验模式，只支持part/all
        :return:
        """
        page = elem.text
        if not text:
            pass
        if mode not in ('vague', 'accurate'):
            raise Exception('mode: 校验模式，只支持part/all')
        if not isinstance(text, list):
            text = [text]
        if mode == 'vague':
            for i in text:
                assert_that(page).contains(i)
        else:
            if isinstance(page, str):
                assert_that(page).is_not_equal_to(text[0])
            else:
                assert_that(str(page)).is_not_equal_to(text[0])


    def assert_mutil_in_list(self, expect_list, actual_list):
        """
        多值校验
        :param expect_list: 预期值列表，
        :param actual_list:
        :return:
        """
        if not isinstance(expect_list, list):
            expect_list = [expect_list]
        for i in expect_list:
            try:
                assert_that(actual_list).contains(i)
            except AssertionError as ex:
                print(ex)


