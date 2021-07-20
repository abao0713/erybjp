import time
from faker import Faker  # 随机数
from selenium import webdriver
from random import choice

url_home = 'https://test-lbk-operational.codemao.cn/packages'
# 跳转到登录页面
url_login = 'https://test-internal-account.codemao.cn/login'
admin_css = '[placeholder~=用户名]'
pwd_css = '[placeholder~=密码]'
submit_login_button = '.ant-btn'
adm_pwd = 'rc-tabs-0-tab-2'

# 跳转 https://test-lbk-operational.codemao.cn/packages/add
# add_package_button_css = 'ant-btn ant-btn-primary'
# add_package_button_class = 'ant-btn ant-btn-primary'
add_package_button_xpath = '//*[@id="root"]/div/section/div[2]/main/div[2]/div/section[1]/div/div[1]/a/button'
package_new_name_css = '[placeholder ~=请输入课程名称，限制20个字以内 ]'
package_new_name_id = 'name'
# content_list = '#contentType'  # 主要内容类型,包含编程课，艺术课，数学课,工程思维
content_list = '#contentType>.ant-radio-wrapper'  # 主要内容类型,包含编程课，艺术课，数学课,工程思维
teaching_platform = '[title ~= 教学平台]>.ant-radio-wrapper'  # NEMO KIDS IDE BOX2
businessType_css = '#businessType'  # 业务类型
attribute_css = '#attribute'  # 课包属性
submit_add_package = '.ant-btn ant-btn-primary'

driver = webdriver.Chrome('/Users/zhao/Documents/UIselemium/chromedriver')
driver.get(url_login)
driver.find_element_by_id(adm_pwd).click()
driver.find_element_by_css_selector(admin_css).send_keys("wb-jiangzhao@codemao.cn")
driver.find_element_by_css_selector(pwd_css).send_keys("codemao123456")
driver.find_element_by_css_selector(submit_login_button).click()
time.sleep(4)
driver.get(url_home)
time.sleep(2)
# driver.find_element_by_class_name(add_package_button_class).click()
# driver.find_element_by_css_selector('#root > div > section > div.ant-layout > main > div:nth-child(2) > div > section:nth-child(2) > div > div:nth-child(1) > a > button').click()
driver.find_element_by_xpath(add_package_button_xpath).click()
print(driver.current_url)

# 切换到新窗口
# 获得打开的第一个窗口句柄
window_1 = driver.current_window_handle
print('句柄为' + window_1)
# 获得打开的所有的窗口句柄
windows = driver.window_handles
for current_window in windows:
    if current_window != window_1:
        driver.close()
        driver.switch_to.window(current_window)

package_name = 'UI自动化测试课包' + time.asctime()
time.sleep(2)
print(driver.current_url)  # 可以判断切换的窗口
# driver.find_element_by_id(package_new_name_id).send_keys(package_name)
driver.find_element_by_css_selector(package_new_name_css).send_keys(package_name)
# content_type = driver.find_element_by_css_selector(content_list)
# content_lists = content_type.find_elements_by_css_selector('.ant-radio-wrapper')
content_lists = driver.find_elements_by_css_selector(content_list)


# print(content_lists.text)
# for element in content_lists:
#     element_text = element.text
#     # 获取元素文本
#     element_value = element.find_element_by_css_selector('.ant-radio > input').get_attribute('value')
#     print(element)
#     print(f"课包类型为{element_text},所对应的值是{element_value}")
#
# # 随机选择
# package_type = choice(content_lists)
# package_type.click()
# print(f"所选择的课包内容类型为{package_type.text}")


def type_value(elements, a, get_attribute):
    for element in elements:
        element_text = element.text
        # 获取元素文本
        element_value = element.find_element_by_css_selector(a).get_attribute(get_attribute)
        print(element)
        # print()
        print(f"课包类型为{element_text},所对应的值是{element_value}")
    return


print(type_value(content_lists, '.ant-radio > input', 'value'))
