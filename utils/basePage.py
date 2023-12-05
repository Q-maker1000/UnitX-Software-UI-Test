import logging
import os
import time
from datetime import datetime
from logging import Handler

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    title = None

    def __init__(self, driver):
        self.driver = driver
        # 等待页面标题出现
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.title_contains(self.title)
            )
        except:
            logging.error("你的操作可能不在当前页面中，可能会引发异常{}".format(self.title))

    # 查找元素
    def location_element(self, locator):
        try:
            el = self.driver.find_element(*locator)
            return el
        except AttributeError:
            # 如果找不到元素，截图
            self.screen_shot()
            logging.error("元素找不到：{}".format(locator))

    # 查找元素
    def location_elements(self, locator):
        try:
            el = self.driver.find_elements(*locator)
            return el
        except AttributeError:
            # 如果找不到元素，截图
            self.screen_shot()
            logging.error("元素找不到：{}".format(locator))

    # 元素找不到时截图
    def screen_shot(self, t=''):
        time.sleep(0.04)
        # path = config.IMG_PATH
        if t == "":
            title = t
        else:
            title = "_" + t
        path = '/home/unitx/A-1000/UnitX-Software-UI-Test/image/screenshots'
        ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        if not os.path.exists(path):
            os.mkdir(path)
        filename = os.path.join(path, ts + title + ".png")
        self.driver.save_screenshot(filename)

    # 等待元素可被点击
    def wait_element_clickable(self, locator, timeout=15, poll=0.5):
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            return el
        except:
            self.screen_shot()
            logging.error("元素找不到{}".format(locator))

    # 等待元素可被点击,然后点击
    def wait_element_clickable_and_click(self, locator, timeout=15, poll=0.5):
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            el.click()
        except:
            self.screen_shot()
            logging.error("元素找不到{}".format(locator))

    # 点击元素
    def click(self, locator):
        # 当元素可被点击时再点击
        self.wait_element_clickable(locator).click()
        return self

    # 等待元素被加载
    def wait_element_presence(self, locator, timeout=15, poll=0.5):
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.presence_of_element_located(locator)
            )
            return el
        except:
            self.screen_shot()
            logging.error("元素找不到{}".format(locator))

    def wait_elements_presence(self, locator, timeout=10, poll=0.5):
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.presence_of_all_elements_located(locator)
            )
            return el
        except:
            self.screen_shot()
            logging.error("元素找不到{}".format(locator))

    # 输入文字内容
    def enter_text(self, locator, value=''):
        # 当元素被加载出来在输入字符
        self.wait_element_presence(locator).send_keys(value)
        return self

    # 清空输入框内容
    def clear_text(self, locator):
        # 当元素被加载出来在输入字符
        el = self.wait_element_presence(locator)
        el.send_keys(Keys.CONTROL + 'a')
        el.send_keys(Keys.DELETE)
        return self

    def clear_and_enter_text(self, el, value):
        # 全选
        el.send_keys(Keys.CONTROL + 'a')
        # 输入内容
        el.send_keys(value)
        return self
