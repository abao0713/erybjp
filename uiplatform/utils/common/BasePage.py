# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         BasePage.py.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/12
#----------------------------

import platform
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from .exceptions import PageElementError, PageSelectException
from .exceptions import FindElementTypesError
from .BaseLoggers import logger
from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
from uiplatform.utils.data.config_object import Browser


LOCATOR_LIST = {
    # selenium
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
    # appium
    'ios_uiautomation': MobileBy.IOS_UIAUTOMATION,
    'ios_predicate': MobileBy.IOS_PREDICATE,
    'ios_class_chain': MobileBy.IOS_CLASS_CHAIN,
    'android_uiautomator': MobileBy.ANDROID_UIAUTOMATOR,
    'android_viewtag': MobileBy.ANDROID_VIEWTAG,
    'android_data_matcher': MobileBy.ANDROID_DATA_MATCHER,
    'android_view_matcher': MobileBy.ANDROID_VIEW_MATCHER,
    'windows_uiautomation': MobileBy.WINDOWS_UI_AUTOMATION,
    'accessibility_id': MobileBy.ACCESSIBILITY_ID,
    'image': MobileBy.IMAGE,
    'custom': MobileBy.CUSTOM,
}


class PageObject(object):
    """
    Page Object pattern.
    """

    def __init__(self, driver, url=None):
        """
        :param driver: `selenium.webdriver.WebDriver` Selenium webdriver instance
        :param url: `str`
        Root URI to base any calls to the ``PageObject.get`` method. If not defined
        in the constructor it will try and look it from the webdriver object.
        """
        self.driver = driver
        self.root_uri = url if url else getattr(self.driver, 'url', None)

    def get(self, uri, headless=True, browser_name='chrome', is_mobile=True):
        """
        :param uri:  URI to GET, based off of the root_uri attribute.
        """
        root_uri = self.root_uri or ''
        self.driver.get(root_uri + uri)
        self.driver.implicitly_wait(4)


class Element(object):
    """
    元素对象
    """

    def __init__(self, timeout=5, describe="undefined", index=0, **kwargs):
        self.timeout = timeout
        self.index = index
        self.desc = describe
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        self.kwargs = kwargs
        self.k, self.v = next(iter(kwargs.items()))

        if self.k not in LOCATOR_LIST.keys():
            raise FindElementTypesError("Element positioning of type '{}' is not supported.".format(self.k))

    def __get__(self, instance, owner):
        if instance is None:
            return None

        Browser.driver = instance.driver
        return self

    def __set__(self, instance, value):
        self.__get__(instance, instance.__class__)
        self.send_keys(value)

    @func_set_timeout(0.5)
    def __elements(self, key, vlaue):
        elems = Browser.driver.find_elements(by=key, value=vlaue)
        return elems

    def __find_element(self, elem):
        """
        Find if the element exists.
        """
        for i in range(self.timeout):
            try:
                elems = self.__elements(elem[0], elem[1])
            except FunctionTimedOut:
                elems = []

            if len(elems) == 1:
                # app.logger.info("✅ Find element: {by}={value} ".format(by=elem[0], value=elem[1]))
                logger.info("✅ Find element: {by}={value} ".format(by=elem[0], value=elem[1]))
                break
            elif len(elems) > 1:
                logger.info("❓ Find {n} elements through: {by}={value}".format(
                    n=len(elems), by=elem[0], value=elem[1]))
                break
            else:
                sleep(1)
        else:
            error_msg = "❌ Find 0 elements through: {by}={value}".format(by=elem[0], value=elem[1])
            logger.error(error_msg)
            print(error_msg)
            raise NoSuchElementException(error_msg)

    def __get_element(self, by, value):
        """
        根据传入的定位方式获取到页面对象供后续调用
        """

        # selenium
        if by == "id_":
            self.__find_element((By.ID, value))
            elem = Browser.driver.find_elements_by_id(value)[self.index]
        elif by == "name":
            self.__find_element((By.NAME, value))
            elem = Browser.driver.find_elements_by_name(value)[self.index]
        elif by == "class_name":
            self.__find_element((By.CLASS_NAME, value))
            elem = Browser.driver.find_elements_by_class_name(value)[self.index]
        elif by == "tag":
            self.__find_element((By.TAG_NAME, value))
            elem = Browser.driver.find_elements_by_tag_name(value)[self.index]
        elif by == "link_text":
            self.__find_element((By.LINK_TEXT, value))
            elem = Browser.driver.find_elements_by_link_text(value)[self.index]
        elif by == "partial_link_text":
            self.__find_element((By.PARTIAL_LINK_TEXT, value))
            elem = Browser.driver.find_elements_by_partial_link_text(value)[self.index]
        elif by == "xpath":
            self.__find_element((By.XPATH, value))
            elem = Browser.driver.find_elements_by_xpath(value)[self.index]
        elif by == "css":
            self.__find_element((By.CSS_SELECTOR, value))
            elem = Browser.driver.find_elements_by_css_selector(value)[self.index]

        # appium
        elif by == "ios_uiautomation":
            self.__find_element((MobileBy.IOS_UIAUTOMATION, value))
            elem = Browser.driver.find_elements_by_ios_uiautomation(value)[self.index]
        elif by == "ios_predicate":
            self.__find_element((MobileBy.IOS_PREDICATE, value))
            elem = Browser.driver.find_elements_by_ios_predicate(value)[self.index]
        elif by == "ios_class_chain":
            self.__find_element((MobileBy.IOS_CLASS_CHAIN, value))
            elem = Browser.driver.find_elements_by_ios_class_chain(value)[self.index]
        elif by == "android_uiautomator":
            self.__find_element((MobileBy.ANDROID_UIAUTOMATOR, value))
            elem = Browser.driver.find_elements_by_android_uiautomator(value)[self.index]
        elif by == "android_viewtag":
            self.__find_element((MobileBy.ANDROID_VIEWTAG, value))
            elem = Browser.driver.find_elements_by_android_viewtag(value)[self.index]
        elif by == "android_data_matcher":
            self.__find_element((MobileBy.ANDROID_DATA_MATCHER, value))
            elem = Browser.driver.find_elements_by_android_data_matcher(value)[self.index]
        elif by == "accessibility_id":
            self.__find_element((MobileBy.ACCESSIBILITY_ID, value))
            elem = Browser.driver.find_elements_by_accessibility_id(value)[self.index]
        elif by == "android_view_matcher":
            self.__find_element((MobileBy.ANDROID_VIEW_MATCHER, value))
            elem = Browser.driver.find_elements_by_android_view_matcher(value)[self.index]
        elif by == "windows_uiautomation":
            self.__find_element((MobileBy.WINDOWS_UI_AUTOMATION, value))
            elem = Browser.driver.find_elements_by_windows_uiautomation(value)[self.index]
        elif by == "image":
            self.__find_element((MobileBy.IMAGE, value))
            elem = Browser.driver.find_elements_by_image(value)[self.index]
        elif by == "custom":
            self.__find_element((MobileBy.CUSTOM, value))
            elem = Browser.driver.find_elements_by_custom(value)[self.index]
        else:
            raise FindElementTypesError(
                "Please enter the correct targeting elements")
        if Browser.show is True:
            try:
                style_red = 'arguments[0].style.border="2px solid #FF0000"'
                style_blue = 'arguments[0].style.border="2px solid #00FF00"'
                style_null = 'arguments[0].style.border=""'

                for _ in range(2):
                    Browser.driver.execute_script(style_red, elem)
                    sleep(0.1)
                    Browser.driver.execute_script(style_blue, elem)
                    sleep(0.1)
                Browser.driver.execute_script(style_blue, elem)
                sleep(0.5)
                Browser.driver.execute_script(style_null, elem)
            except WebDriverException:
                pass

        return elem

    def clear(self):
        """清空输入框中涉及到的文本，基本每次输入都需要调用此方法"""
        elem = self.__get_element(self.k, self.v)
        logger.info("clear element: {}".format(self.desc))
        elem.clear()

    def send_keys(self, value):
        """
        输入信息value
        """
        elem = self.__get_element(self.k, self.v)
        logger.info("🖋 input element: {}".format(self.desc))
        print("🖋 input element: {}".format(self.desc))
        elem.send_keys(value)

    def click(self):
        """点击操作"""
        elem = self.__get_element(self.k, self.v)
        logger.info("🖱 click element: {}".format(self.desc))
        print("🖱 click element: {}".format(self.desc))
        elem.click()

    def submit(self):
        """表单提交操作"""
        elem = self.__get_element(self.k, self.v)
        logger.info("submit element: {}".format(self.desc))
        elem.submit()

    @property
    def tag_name(self):
        """此元素的``tagName``属性"""
        elem = self.__get_element(self.k, self.v)
        return elem.tag_name

    @property
    def text(self):
        """元素本身对应的内容显示"""
        elem = self.__get_element(self.k, self.v)
        return elem.text

    @property
    def size(self):
        """获取元素尺寸"""
        elem = self.__get_element(self.k, self.v)
        return elem.size

    def get_property(self, name):
        """
        可以获取元素属性
        """
        elem = self.__get_element(self.k, self.v)
        return elem.get_property(name)

    def get_attribute(self, name):
        """可以获取元素属性"""
        elem = self.__get_element(self.k, self.v)
        return elem.get_attribute(name)

    def is_displayed(self):
        """针对用户此元素是否隐藏"""
        elem = self.__get_element(self.k, self.v)
        return elem.is_displayed()

    def is_selected(self):
        """
        检查元素是否被选中，单选框，复选框
        """
        elem = self.__get_element(self.k, self.v)
        return elem.is_selected()

    def is_enabled(self):
        """返回元素是否是enabled."""
        elem = self.__get_element(self.k, self.v)
        return elem.is_enabled()

    def switch_to_frame(self):
        """
        selenium API
        进入到frame
        """
        elem = self.__get_element(self.k, self.v)
        Browser.driver.switch_to.frame(elem)

    def move_to_element(self):
        """
        selenium API
        将鼠标移到元素的中间
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).move_to_element(elem).perform()

    def click_and_hold(self):
        """
        selenium API
        在元素上按住鼠标左键。
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).click_and_hold(elem).perform()

    def double_click(self):
        """
        selenium API
        在元素上按住鼠标左键。
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).double_click(elem).perform()

    def context_click(self):
        """
        selenium API
        点击元素上面
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).context_click(elem).perform()

    def drag_and_drop_by_offset(self, x, y):
        """
        selenium API
        按住源元素上的鼠标左键，
            然后移动到目标偏移并释放鼠标按钮。
        :param x: X offset to move to.
        :param y: Y offset to move to.
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).drag_and_drop_by_offset(elem, xoffset=x, yoffset=y).perform()

    def refresh_element(self, timeout=10):
        """
        selenium API
        页面刷新
        """
        try:
            timeout_int = int(timeout)
        except TypeError:
            raise ValueError("Type 'timeout' error, must be type int() ")

        elem = self.__get_element(self.k, self.v)
        for i in range(timeout_int):
            if elem is not None:
                try:
                    elem
                except StaleElementReferenceException:
                    Browser.driver.refresh()
                else:
                    break
            else:
                sleep(1)
        else:
            raise TimeoutError("stale element reference: element is not attached to the page document.")

    def select_by_value(self, value):
        """
        下拉框通过值来定位
        """
        select_elem = self.__get_element(self.k, self.v)
        Select(select_elem).select_by_value(value)

    def select_by_index(self, index):
        """
        下拉框通过索引来定位
        """
        select_elem = self.__get_element(self.k, self.v)
        Select(select_elem).select_by_index(index)

    def select_by_visible_text(self, text):
        """
        selenium API
        通过页面显示的值来定位
        """
        select_elem = self.__get_element(self.k, self.v)
        Select(select_elem).select_by_visible_text(text)

    def set_text(self, keys):
        """
        appium API
        输入文本
        """
        elem = self.__get_element(self.k, self.v)
        elem.set_text(keys)
        return self

    @property
    def location_in_view(self):
        """
        appium API
        获取元素相对于视图的位置。
        返回：
        dict：元素相对于视图的位置
        """
        elem = self.__get_element(self.k, self.v)
        return elem.location_in_view()

    def set_value(self, value):
        """
        appium API
        在应用程序中设置此元素的值
        """
        elem = self.__get_element(self.k, self.v)
        elem.set_value(value)
        return self

    def input(self, text=""):
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(text)

    def enter(self):
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.ENTER)

    def select_all(self):
        elem = self.__get_element(self.k, self.v)
        if platform.system().lower() == "darwin":
            elem.send_keys(Keys.COMMAND, "a")
        else:
            elem.send_keys(Keys.CONTROL, "a")

    def cut(self):
        elem = self.__get_element(self.k, self.v)
        if platform.system().lower() == "darwin":
            elem.send_keys(Keys.COMMAND, "x")
        else:
            elem.send_keys(Keys.CONTROL, "x")

    def copy(self):
        elem = self.__get_element(self.k, self.v)
        if platform.system().lower() == "darwin":
            elem.send_keys(Keys.COMMAND, "c")
        else:
            elem.send_keys(Keys.CONTROL, "c")

    def paste(self):
        elem = self.__get_element(self.k, self.v)
        if platform.system().lower() == "darwin":
            elem.send_keys(Keys.COMMAND, "v")
        else:
            elem.send_keys(Keys.CONTROL, "v")

    def backspace(self):
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.BACKSPACE)

    def delete(self):
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.DELETE)

    def tab(self):
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.TAB)

    def space(self):
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.SPACE)


class Elements(object):
    """
    返回元素对象供使用
    """

    def __init__(self, context=False, describe="undefined", **kwargs):
        self.describe = describe
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        self.k, self.v = next(iter(kwargs.items()))
        try:
            self.locator = (LOCATOR_LIST[self.k], self.v)
        except KeyError:
            raise FindElementTypesError("Element positioning of type '{}' is not supported. ".format(self.k))
        self.has_context = bool(context)

    def find(self, context):
        try:
            elems = context.find_elements(*self.locator)
        except NoSuchElementException:
            elems = []
        logger.info("✨ Find {n} elements through: {by}={value}, describe:{desc}".format(
            n=len(elems), by=self.k, value=self.v, desc=self.describe))
        return elems

    def __get__(self, instance, owner, context=None):
        if not instance:
            return None

        if not context and self.has_context:
            return lambda ctx: self.__get__(instance, owner, context=ctx)

        if not context:
            context = instance.driver

        return self.find(context)

    def __set__(self, instance, value):
        if self.has_context:
            raise PageElementError("Sorry, the set descriptor doesn't support elements with context.")
        elems = self.__get__(instance, instance.__class__)
        if not elems:
            raise PageElementError("Can't set value, no elements found")
        [elem.send_keys(value) for elem in elems]


class PageSelect(object):
    """
    Processing select drop-down selection box
    """

    def __init__(self, select_elem, value=None, text=None, index=None):
        if value is not None:
            Select(select_elem).select_by_value(value)
        elif text is not None:
            Select(select_elem).select_by_visible_text(text)
        elif index is not None:
            Select(select_elem).select_by_index(index)
        else:
            raise PageSelectException('"value" or "text" or "index" options can not be all empty.')


class PageWait(object):
    def __init__(self, elem, timeout=3):
        """
        等待元素可见
        """
        # 如果定义元素时没有找到元素，此处将继续查找元素，直至超时；
        if not page_exist(elem):
            elem = WebDriverWait(driver=elem.context, timeout=int(timeout - 0),
                                 poll_frequency=0.5).until(presence_of_element_located(elem.locator))

        # 找到元素后，才开始判断是否可见；
        for i in range(timeout):
            try:
                if elem.is_displayed():
                    break
                else:
                    sleep(1)
            except:
                sleep(1)
        else:
            raise TimeoutError("超时，元素不可见")


class PageWaitDisappear(object):
    def __init__(self, elem, timeout=3):
        """
        等待元素消失
        """
        try:
            PageWait(elem)  # 指定时间内未出现，则判断元素不可见；若出现了，则循环等待判断元素不可见；
        except:
            return

        for i in range(timeout):
            try:
                if elem.is_displayed():
                    sleep(1)
                else:
                    return
            except:
                break
        else:
            raise TimeoutError('超时，元素仍可见')


def page_exist(elem):
    """返回元素是否存在"""
    if type(elem).__name__ == 'WebElement':
        return True
    else:
        return False