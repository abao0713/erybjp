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
class  TestJenkinsCompare:
     def setUp(self):
         global driver
         driver = browser_driver("chrome",headless=False,is_mobile=False, is_remote=True)
         logger.info('driver驱动器已获取成功')
     def tearDown(self):
         time.sleep(10)
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
                 print(new_staging_bulid_num,"staging编号")
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
                 print(new_production_built_data,"="*10)
                 return "#"+new_production_built_data
         logger.info(f'{servername}不存在production环境')

     def test_staging_production_compare(self,servername_list:list):
         self.setUp()
         self.test_login_page()
         check = []
         for servername in servername_list:
             print(servername)
             staging_num = self.test_staging_server(servername)
             production_num = self.test_production_server(servername)
             print(staging_num,production_num,"是否相等呢")
             if staging_num == production_num:
                 logger.info(f"测试验收通过，{servername}的staging与线上编号{staging_num}<>{production_num}保持一致")
             else:
                 logger.critical(f"测试未通过，请检查服务{servername}的staging与线上的编号{staging_num}！={production_num}")
                 check.append({servername: f"staging最新构建编号{staging_num}不等于生产环境构建参数{production_num}"})
         self.tearDown()
         return check


     def aliding_jenkins(self,servername_list,num):
         jen = TestJenkinsCompare()
         data = jen.test_staging_production_compare(servername_list)
         text = f"检测唯一标识码{num}结果通知{data}，请注意查收！"
         DingtalkRobot().send_markdown("jenkins服务占用检测结果通知", text, [])




if  __name__  == "__main__":
    jen = TestJenkinsCompare()
    a = jen.test_staging_production_compare(["codemaster_codecamp_marketing"])
    print(a)



