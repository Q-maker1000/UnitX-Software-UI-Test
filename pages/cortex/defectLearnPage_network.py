import json
import logging
import re
import time
from datetime import datetime

import pyautogui
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageLocators.cortex.commonLocs import CommonLocs
from pageLocators.cortex.defectLearnLocs import DefectLearnLocs
from pageLocators.cortex.labelLocs import LabelLocs
from utils.basePage import BasePage
from utils.common import login


class LeftBtn:
    LABEL_INDEX = 0
    REVIEW_LABELS_INDEX = 1
    TRAIN_FROM_SCRATCH_INDEX = 2
    TRAIN_INCREMENTAL_INDEX = 3
    CANCEL_INDEX = 4


class TopBtn:
    IMPORT_IMAGES = 0
    DEPLOY = 1
    SETTING = 2
    CLONE = 3
    EXPORT = 4
    ARCHIVE = 5


class DefectLearnPage_Network(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def create_network(self, name):
        # ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # 1. 点击新建network按钮
        self.click(DefectLearnLocs.el_btn_create_network_locator)
        # 2. 清除输入框内容
        self.clear_text(DefectLearnLocs.el_ipt_network_name_locator)
        # 3. 输入network名称
        self.enter_text(DefectLearnLocs.el_ipt_network_name_locator, name)
        # 4. 点击新建network设置按钮
        self.click(DefectLearnLocs.el_btn_create_network_config_locator)
        logging.info(f'create network: {name}')
        time.sleep(1)
        # 5.判断network是否存在
        network = self.find_network_by_name(name)
        logging.info(network)
        assert network is not None

    def list_network(self):
        time.sleep(1)
        el_network_list = self.location_elements(DefectLearnLocs.el_network_list_locator)
        # network_name_list = []
        # for el_name in el_network_name_list:
        #     name = el_name.get_attribute('innerHTML')
        #     network_name_list.append(name)
        return el_network_list

    def find_network_by_name(self, name=''):
        # 每个network元素的列表
        el_network_list = self.wait_elements_presence(DefectLearnLocs.el_network_list_locator)
        for el_network in el_network_list:
            el_network_name = el_network.find_element(*DefectLearnLocs.el_h2_locator)
            network_name = el_network_name.get_attribute("innerHTML")
            logging.debug(f'check network name: {network_name}')
            if name == network_name:
                logging.debug(f'find network is {network_name}')
                return el_network
        logging.error(f'cannot find network name is {name}')
        return None

    def import_images(self, path, network_name):
        el_network = self.find_network_by_name(network_name)
        el_network_header = el_network.find_element(*DefectLearnLocs.el_network_header_locator)
        el_network_config_btn_list = el_network_header.find_elements(*DefectLearnLocs.el_btn_network_config_btn_list_locator)
        for btn in el_network_config_btn_list:
            logging.debug(btn.get_attribute('outerHTML'))
        el_network_config_btn_list[1].click()

        try:
            time.sleep(1)
            # subprocess.run(["xdotool", "type", path])
            pyautogui.typewrite(path, interval=0.1)
            time.sleep(0.3)
            # subprocess.run(["xdotool", "key", "Return"])
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
        except subprocess.CalledProcessError:
            logging.error('something was wrong in subprocess')

    def select_btn_in_network_bottom(self, name, button):
        # 获取network底部按钮列表
        network_bottom_enable_btn_list = self.get_enable_btn_in_network_bottom(name)
        # 遍历判断是否是预期按钮
        for btn in network_bottom_enable_btn_list:
            span_label = btn.find_element(*DefectLearnLocs.el_span_locator).get_attribute("innerHTML")
            print(span_label)
            if span_label == button:
                self.wait_element_clickable_and_click(btn)
                self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_confirm_locator)
                return True
        print("train from scratch btn not found!")
        return False

    def get_enable_btn_in_network_bottom(self, name):
        # 获取该模型底部元素
        network = self.find_network_by_name(name)
        network_bottom = network.find_element(*DefectLearnLocs.el_network_bottom_locator)
        # 获取label标签
        network_bottom_enable_btn_list = network_bottom.find_elements(By.CSS_SELECTOR, 'button[tabindex="0"]')
        logging.info(network_bottom_enable_btn_list)
        return network_bottom_enable_btn_list

    def pre_process(self, x_start=0, x_end=2464, y_start=0, y_end=2056, re_w=960, re_h=800):
        # 获取预处理按钮并点击
        self.wait_element_clickable_and_click(LabelLocs.el_btn_pre_process_locator)
        # 获取预处理表单
        form_pre_process = self.wait_element_presence(LabelLocs.el_form_pre_process_locator)
        # 获取6个输入框
        input_list = form_pre_process.find_elements(*CommonLocs.el_input_locator)
        # 截图
        self.screen_shot("before edit pre_process")
        # 将六个值存入列表,并输入输入框
        value_list = [x_start, x_end, y_start, y_end, re_w, re_h]
        i = 0
        for ipt in input_list:
            # print(ipt.get_attribute('outerHTML'))
            print(value_list[i])
            self.clear_and_enter_text(ipt, value_list[i])
            i = i + 1
        # 截图
        time.sleep(0.3)
        self.screen_shot("after edit pre_process")
        # 点击保存按钮
        self.wait_element_clickable_and_click(LabelLocs.el_btn_save_pre_process_locator)
        # 确定保存
        self.wait_element_clickable_and_click(CommonLocs.el_btn_confirm_locator)

    def select_left_network_btn(self, name, index):
        # 获取该模型底部元素
        network = self.find_network_by_name(name)
        network_bottom = network.find_element(*DefectLearnLocs.el_network_bottom_locator)
        el_left_btn_list = network_bottom.find_elements(*CommonLocs.el_btn_locator)
        # for btn in el_left_btn_list:
        #     logging.debug(btn.get_attribute("innerHTML"))
        el_btn = el_left_btn_list[index]
        if el_btn.is_enabled():
            el_btn.click()
            logging.debug(f"click left btn({index})")
            if index == 2 or index == 3:
                logging.debug(f"confirm to train({index})")
                self.wait_element_clickable_and_click(CommonLocs.el_btn_confirm_locator)
        else:
            logging.error(f'This network left btn({index}) could not click')

    def is_train_end(self, name):
        # 获取该模型底部元素
        network = self.find_network_by_name(name)
        network_bottom = network.find_element(*DefectLearnLocs.el_network_bottom_locator)
        el_left_btn_list = network_bottom.find_elements(*CommonLocs.el_btn_locator)
        el_btn = el_left_btn_list[LeftBtn.CANCEL_INDEX]

        while True:
            logging.info(f'network is training wait 30s try again')
            time.sleep(30)
            if not el_btn.is_enabled():
                logging.info(f'the network was finished the trained')
                break

    def select_top_network_btn(self, name, top_btn):
        # 获取该模型底部元素
        network = self.find_network_by_name(name)
        el_network_header = network.find_element(*DefectLearnLocs.el_network_header_locator)
        el_top_network_btn_div = el_network_header.find_elements(By.XPATH, './div')[1]
        el_top_network_btn_list = el_top_network_btn_div.find_elements(*CommonLocs.el_btn_locator)
        # for i in el_top_network_btn_list:
        #     logging.info(i.get_attribute('outerHTML'))
        if top_btn == TopBtn.CLONE:
            el_top_network_btn_list[top_btn].click()

    def clone_network(self, name):
        self.select_top_network_btn(name, TopBtn.CLONE)
        el_input = self.wait_element_presence(DefectLearnLocs.el_input_clone_network_locator)
        self.clear_text(DefectLearnLocs.el_input_clone_network_locator)
        self.enter_text(DefectLearnLocs.el_input_clone_network_locator, f'{name}_clone')
        self.click(DefectLearnLocs.el_btn_clone_network_locator)
        network = self.find_network_by_name(name)
        logging.info(network)
        assert network is not None

    def valid_result(self, name):
        network = self.find_network_by_name(name)
        el_network_header = network.find_element(*DefectLearnLocs.el_network_header_locator)
        a = el_network_header.find_element(By.TAG_NAME, 'a')
        a.click()
        # logging.info(a.get_attribute('outerHTML'))

    def select_last_model_version(self, name, number=2):
        network = self.find_network_by_name(name)
        el_div_model_version_selector = network.find_element(*DefectLearnLocs.el_div_model_version_selector_locator)
        el_div_model_version_selector.click()
        el_li_model_version_list = self.wait_elements_presence(CommonLocs.el_li_locator)
        model_version_text = el_li_model_version_list[number-1].find_element(*CommonLocs.el_span_locator).text
        el_li_model_version_list[number-1].click()
        self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_confirm_locator)
        el_span_model_version = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
            expected_conditions.presence_of_element_located((By.XPATH, f'//*[@id="model-versions-{name}"]/span'))
        ).get_attribute('innerHTML')
        logging.info(f'model_version_text, el_span_model_version:{model_version_text, el_span_model_version}')
        assert model_version_text == el_span_model_version







