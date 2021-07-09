#__author__:wanyiliu

import time

# import pytest
from selenium.webdriver.common.keys import Keys

from uiplatform.services.ali_dingtalk import DingtalkRobot
from uiplatform.utils import BaseAssert
from uiplatform.utils.logicobject.H5NormalPage import Jenkins, LbkMobilePage, MonthSharePage, InvitationPage, \
    GiveLessonPage, GivequanPage, LessonOrderPage, CommunityPage, MorderPage, HiCode
from uiplatform.utils.common.Driver import browser_driver
from uiplatform.utils.common.BaseLoggers import logger
from selenium import webdriver
from multiprocessing import Pool,Manager


class  TestJenkinsCompare:
     def setUp(self):
         global driver
         driver = browser_driver("chrome",headless=False,is_mobile=False, is_remote=True)
         logger.info('driver驱动器已获取成功')
     def tearDown(self):
         driver.quit()

     def test_login_page(self):
         '''登录jenkins，进入其首页'''
         page = Jenkins(driver=driver)
         self.page = page
         self.page.get(page.url_login)
         driver.maximize_window()
         driver.implicitly_wait(5)
         self.page.username_element = "wanyiliu"
         self.page.password_element = "wanyiliu@codemao.cn"
         driver.implicitly_wait(5)
         self.page.button_element.click()
         self.page.get(page.host)

     def test_staging_server(self,servername):
         '''获取staging环境服务的最新编号'''
         self.page.ele_search = servername
         time.sleep(2)
         ele_server_gather = self.page.ele_server_gather
         for servername_env_data in ele_server_gather:
             if "staging".lower() in servername_env_data.text.lower():
                 logger.info(f'{servername}存在staging环境')
                 servername_env_data.click()
                 self.page.ele_search.send_keys(Keys.ENTER)
                 new_staging_bulid_num = self.page.new_staging_bulid_element.text
                 print(new_staging_bulid_num,f"{servername}的staging编号")
                 return new_staging_bulid_num
         logger.info(f'{servername}不存在staging环境')

     def test_production_server(self,servername):
         '''获取线上环境服务的最新编号对应staging的构建编号'''
         self.page.ele_search = servername
         time.sleep(2)
         ele_server_gather = self.page.ele_server_gather
         for servername_env_data in ele_server_gather:
             if "production".lower() in servername_env_data.text.lower():
                 logger.info(f'{servername}存在production环境')
                 servername_env_data.click()
                 self.page.ele_search.send_keys(Keys.ENTER)
                 new_production_bulid_num = self.page.new_production_built_element.text
                 print(new_production_bulid_num)
                 self.page.new_production_built_element.click()
                 driver.implicitly_wait(5)
                 self.page.product_para_element.click()
                 new_production_built_data = self.page.new_production_built_data.get_attribute("value")
                 return "#"+new_production_built_data
         logger.info(f'{servername}不存在production环境')

     def test_staging_production_compare(self,servername:str,server_error_list):
         '''
         server_error_list:如果单独调用则写个列表即可，如果是直接并行调用aliding_jenkins则不用管
         '''
         self.setUp()
         self.test_login_page()
         print(servername)
         staging_num = self.test_staging_server(servername)
         production_num = self.test_production_server(servername)
         print(staging_num,production_num,"staging与线上参数对比")
         if staging_num == production_num:
             logger.info(f"测试验收通过，{servername}的staging与线上编号参数{staging_num}<>{production_num}保持一致")
         else:
             logger.critical(f"测试未通过，请检查服务{servername}的staging与线上的编号参数{staging_num}！={production_num}")
             server_error_list.append({servername: f"staging最新构建编号{staging_num}不等于生产环境构建参数{production_num}"})
         self.tearDown()
         return server_error_list


     def aliding_jenkins(self,servername_list,num):
         start_time = time.time()
         manage = Manager()
         self.server_error_list = manage.list()
         pool = Pool(processes=len(servername_list))
         for i in range(len(servername_list)):
             pool.apply_async(self.test_staging_production_compare,
                              (servername_list[i], self.server_error_list))
         pool.close()
         pool.join()
         end_time = time.time()
         logger.info(f"校验对比耗时：{end_time-start_time}")
         if len(self.server_error_list)>0:
             text = "检测唯一标识码{}结果通知{}，请注意查收！".format(num,self.server_error_list)
             DingtalkRobot().send_markdown("jenkins服务占用检测结果通知", text, [])
         else:
             logger.info("jenkins服务占用检测结果为服务无占用问题")





if  __name__  == "__main__":
    TestJenkinsCompare().aliding_jenkins(["codemaster_codecamp_service",'lbk_web_customer',"lbk_activity","lbk_web_admin"],11111)
