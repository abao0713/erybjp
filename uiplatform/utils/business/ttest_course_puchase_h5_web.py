# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         BrowserPage.py
# Description:  测试环境进行购买体验课测试
# Author:       wanyiliu
# Date:         2021/7/22
#----------------------------
import time

from selenium.webdriver.common.by import By

from  uiplatform.utils.logicobject.H5NormalPage import TestCource
import requests
from requests.cookies import  RequestsCookieJar
from uiplatform.utils.common.BaseLoggers import logger
from uiplatform.utils.common.Driver import browser_driver
from uiplatform.utils.common.BaseAssert import BaseAssert
import os
from uiplatform.services.ali_dingtalk import DingtalkRobot


# png = os.path.join(os.path.abspath("../"),f"data\picture\{str(time.time()*100000).split('.')[0]}.png") #失败之后截图
png = os.path.join(os.path.abspath("../"),r"data\picture\testpacketbuy.png") #失败之后截图


class  PurchasePacket:
    def __init__(self):
        self.login_data = self.login()  #获取登录token

    def login(self):
        '''登录接口获取token'''
        res = requests.post(url=TestCource.login_url, json=TestCource.login_request_body)
        if res.json()["token"]:
            logger.info('测试环境登录接口返回token成功')
            return res.json()['token']
        else:
            raise Exception('登录接口报错')

    def delete_order(self):
        '''删除订单记录'''
        token = self.login_data
        headers = {"Authorization": f"Token {token}"}
        TestCource.delete_order_cookie = {"cookies": f"monkey_token={token}"}
        headers.update(TestCource.delete_order_cookie)
        logger.info(f'请求头为:{headers}')
        res = requests.post(url=TestCource.delete_order_url,
                            json=TestCource.delete_order_request_body,
                            headers=headers)
        if isinstance(res.json()["tbl_order"], int):
            logger.info('删除订单记录成功')
        else:
            raise Exception("删除订单记录失败，请检查删除接口")

    def get_phone_code(self,timeout=5):
        '''获取验证码
        timeout即点击验证码按钮之后，多久获取验证码输入
        '''
        token = self.login_data
        headers = {"Authorization": f"Token {token}"}
        TestCource.delete_order_cookie = {"cookies": f"monkey_token={token}"}
        headers.update(TestCource.delete_order_cookie)
        res = requests.post(url=TestCource.get_phone_code_url, json=TestCource.code_request_body, headers=headers)
        code = res.json()['code']
        for i in range(timeout):
            try:
                if not code:
                    raise Exception("获取code为空，请注意查看")
                elif  isinstance(int(code), int):
                      logger.info(f'获取验证码成功为{code}')
                      return int(code)
                else:
                    raise Exception('获取验证码接口报错，请检查接口')
            except Exception as e:
                print(e)
                time.sleep(1)

    def  setUp(self):
        global driver
        driver = browser_driver(browser_name="chrome",headless=False,is_mobile=True,is_remote=True)
        driver.maximize_window()

    def tearDowm(self):
        driver.quit()

    def purse_price_not_zero(self):
        '''购买非0元体验课成功'''
        error = [] #报错之后的错误信息
        self.setUp()
        self.delete_order()
        course = TestCource(driver=driver)
        course.get(TestCource.test_url_not_zero)
        course.phone_ele = "18664939036"
        course.code_button_ele.click()
        try:
            '''图形验证码功能暂时未完成'''
            png_code = driver.find_element(By.CSS_SELECTOR,"#tcaptcha_iframe_drag")
            driver.switch_to.frame(png_code)
            logger.critical('图片验证码存在，造成阻塞，请等待一段时间重新运行或手动执行')
            error.append("图片验证码存在，请等待一段时间重新运行或手动执行")
            return {"message":"图片验证码存在，请等待一段时间重新运行或手动执行"}
            # #选择拖动滑块的节点
            # slide_element = driver.find_element_by_css_selector("#tcaptcha_drag_thumb")
            # #获取滑块图片的节点
            # slideBlock_ele = driver.find_element_by_css_selector("#slideBlock")
            # #获取缺口背景图片节点
            # slideBg = driver.find_element_by_css_selector("#slideBg")[1]
        except Exception as e:
            logger.info('图片验证码不存在，可以正常运行')
        finally:
            if not error:
                course.code_ele = self.get_phone_code()
                course.pay_button_ele.click()
                driver.implicitly_wait(10)
                BaseAssert().assert_text_in_elem("微信支付",course.pay_type_ele[0],mode="accurate")
                try:
                    if "微信支付" ==  course.pay_type_ele[0].text:
                        logger.info('存在微信支付选项，体验课购买成功')
                        driver.save_screenshot(png)

                    elif "支付包支付" == course.pay_type_ele[2].text:
                        logger.info('存在支付宝支付选项，体验课购买成功')
                    else:
                        driver.save_screenshot(png)
                        raise Exception("体验课购买失败")
                except Exception as e:
                    return {"message":"体验课购买失败,请通知开发修改bug"}
                self.tearDowm()
                return {"message":"非0体验课购买成功"}
    def sendding_buy_testpacket(self):
        title = "巡检异常预警"
        url = "http://172.16.26.119:6851/data/picture/testpacketbuy.png"  #报错页面
        mark_text = "本次在运行测试用例test_packet_buy_h5_web时探针检测失败判定页面打开失败,截图如下![screenshot](http://172.16.26.119:6851/data/picture/162461447116295.png)"
        DingtalkRobot().send_markdown(msg=title,mark_text=mark_text,is_at_all=True,at_mobiles=[])


if  __name__ == "__main__":
    start = time.time()
    PurchasePacket().purse_price_not_zero()
    end = time.time()
    print(end-start)