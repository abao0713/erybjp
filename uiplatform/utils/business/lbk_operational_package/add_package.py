import time
from faker import Faker  # 随机数
from selenium import webdriver
from random import choice
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import logging


def checkout_windows(window,driver):

    for current_window in driver.window_handles:
        if current_window != window:
            driver.switch_to.window(current_window)


def type_value(elements, css, get_attribute, type_name='课包类型'):
    for element in elements:
        element_text = element.text
        # 获取元素文本
        element_value = element.find_element_by_css_selector(css).get_attribute(get_attribute)
        print(f"{type_name}为{element_text},所对应的值是{element_value}", end=';')
        if element == elements[-1]:
            print('')
    Select_attribute = choice(elements)
    Select_attribute.click()
    logging.info(f"所选择的{type_name}类型为{Select_attribute.text}")
    return Select_attribute

def go_url():
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
    teaching_platform = '#platform>.ant-radio-wrapper'  # NEMO KIDS IDE BOX2
    businessType_css = '#businessType>.ant-radio-wrapper'  # 业务类型
    attribute_css = '#attribute>.ant-radio-wrapper'  # 课包属性
    submit_add_package = "#rc-tabs-0-panel-BASE > div > div > div > button"

    # 章节配置
    zhangjiepeizhi_id = 'rc-tabs-1-tab-CHAPTER'
    add_zhangjieUrl_button = '#rc-tabs-1-panel-CHAPTER > div > a'
    # 跳转到url:https://test-lbk-operational.codemao.cn/packages/edit/chapters-config?packageId=
    add_zhangjie_button = '.content__1gKnH > button'  # 添加章节按钮
    zhangjie_sortTitle_id = 'list_0_sortTitle'  # 章节序列号
    zhangjie_name_id = 'list_0_name'  # 章节名称
    add_zhangjie_img_id = 'list_0_backgroundUrl'  # 上传文件
    img = '/Users/zhao/Documents/UIselemium/头像.jpg'
    add_zhangjie_button_css_OK = 'div:nth-child(2) > div > div > div > section > button'

    driver = webdriver.Chrome('/Users/zhao/Documents/UIselemium/chromedriver')
    driver.get(url_login)
    # 清除缓存
    cookies = driver.get_cookies()
    print(f"main: cookies = {cookies}")
    driver.delete_all_cookies()

    driver.find_element_by_id(adm_pwd).click()
    driver.find_element_by_css_selector(admin_css).send_keys("wb-jiangzhao@codemao.cn")
    driver.find_element_by_css_selector(pwd_css).send_keys("codemao123456")
    driver.find_element_by_css_selector(submit_login_button).click()
    time.sleep(4)
    driver.implicitly_wait(5)
    driver.get(url_home)
    # time.sleep(2)
    # driver.find_element_by_class_name(add_package_button_class).click()
    # driver.find_element_by_css_selector('#root > div > section > div.ant-layout > main > div:nth-child(2) > div > section:nth-child(2) > div > div:nth-child(1) > a > button').click()
    driver.find_element_by_xpath(add_package_button_xpath).click()
    print(driver.current_url)

    # 切换到新窗口
    # 获得打开的第一个窗口句柄
    window_1 = driver.current_window_handle
    print('句柄为' + window_1)

    # 获得打开的所有的窗口句柄
    # windows = driver.window_handles
    # for current_window in windows:
    #     if current_window != window_1:
    #         driver.close()
    #         driver.switch_to.window(current_window)


    checkout_windows(window_1,driver)
    package_name = 'Auto测试' + time.strftime('%H:%M:%S', time.localtime())
    print(package_name)
    # time.sleep(2)
    print(driver.current_url)  # 可以判断切换的窗口
    # driver.find_element_by_id(package_new_name_id).send_keys(package_name)
    driver.find_element_by_css_selector(package_new_name_css).send_keys(package_name)
    # content_type = driver.find_element_by_css_selector(content_list)
    # content_lists = content_type.find_elements_by_css_selector('.ant-radio-wrapper')
    content_lists = driver.find_elements_by_css_selector(content_list)
    teaching_platform_list = driver.find_elements_by_css_selector(teaching_platform)
    businessType_list = driver.find_elements_by_css_selector(businessType_css)
    attribute_list = driver.find_elements_by_css_selector(attribute_css)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s -- [line:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d.%H:%M:%S')

    # print(content_lists.text)
    # for element in content_lists:
    #     element_text = element.text
    #     # 获取元素文本
    #     element_value = element.find_element_by_css_selector('.ant-radio > input').get_attribute('value')
    #     print(element)
    #     print(f"课包类型为{element_text},所对应的值是{element_value}")
    #
    # for element in teaching_platform_list:
    #     element_text = element.text
    #     # 获取元素文本
    #     element_value = element.find_element_by_css_selector('.ant-radio > input').get_attribute('value')
    #     print(element)
    #     print(f"课包类型为{element_text},所对应的值是{element_value}")

    # # 随机选择
    # package_type = choice(content_lists)
    # package_type.click()
    # print(f"所选择的课包内容类型为{package_type.text}")


    # def random(elements):
    #     package_type = choice(elements)
    #     package_type.click()
    #     print(f"所选择的参数是{package_type.text}")
    #     return package_type
    # print(type_value(content_lists, '.ant-radio > input', 'value', '课包类型'))
    # type_value(content_lists, '.ant-radio > input', 'value', '课包类型')
    # type_value(teaching_platform_list, '.ant-radio > input', 'value', '教学平台')
    # type_value(businessType_list, '.ant-radio > input', 'value', '业务类型')
    # type_value(attribute_list, '.ant-radio > input', 'value', '课包属性')
    try:
        type_value(content_lists, '.ant-radio > input', 'value', '课包类型')
        type_value(teaching_platform_list, '.ant-radio > input', 'value', '教学平台')
        type_value(businessType_list, '.ant-radio > input', 'value', '业务类型')
        type_value(attribute_list, '.ant-radio > input', 'value', '课包属性')
        driver.find_element_by_css_selector(submit_add_package).click()
    except NoSuchElementException:
        print(f"找不到{submit_add_package}元素")
        driver.quit()
    except StaleElementReferenceException:
        print(f"元素属性在页面不存在")
        driver.quit()

    driver.find_element_by_id(zhangjiepeizhi_id).click()
    logging.info('切换章节成功')
    driver.find_element_by_css_selector(add_zhangjieUrl_button).click()
    logging.info('页面跳转至添加章节页面')
    window_zhangjie = driver.current_window_handle
    checkout_windows(window_zhangjie,driver)
    logging.info('获取添加章节页面句柄成功，跳转至章节页面')
    driver.find_element_by_css_selector(add_zhangjie_button).click()
    logging.info('点击添加按钮成功,出现章节弹框')
    driver.find_element_by_id(zhangjie_sortTitle_id).send_keys('1')
    driver.find_element_by_id(zhangjie_name_id).send_keys('Ui自动化章节测试' + str(time.time()))
    driver.find_element_by_id(add_zhangjie_img_id).send_keys(img)
    logging.info('添加章节名称+序列号+图片成功')
    time.sleep(2)
    driver.find_element_by_css_selector(add_zhangjie_button_css_OK).click()
    logging.info('提交章节信息成功')
    driver.switch_to.window(driver.window_handles[1])
    driver.refresh()
    logging.info('切换到原新增课包页面，并且刷新')

if __name__ == '__main__':
    go_url()