import logging
import os
import time

import pyautogui
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageLocators.optix.commonLocs import CommonLocs
from pageLocators.optix.homeLocs import HomeLocs
from pages.optix.hardwareSettingPage import HardwareSettingPage
from utils import start_software
from utils.basePage import BasePage


class PatternSelect:
    ALL_BY_RING = 'all_by_ring'
    OUTERMOST_BY_RING = 'outermost_by_ring'
    BY_NORMAL = 'by_normal'

class ConfigType:
    SEQUENCE = 'sequence'
    CAPTURE = 'capture'

class HardwareSettingPage_v2(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def select_config_by_name(self, name):
        self.wait_element_clickable_and_click(HomeLocs.el_selector_locator)
        el_ul_selector_list = self.location_element(HomeLocs.el_ul_selector_list_locator)
        el_selector_li_list = el_ul_selector_list.find_elements(*CommonLocs.el_li_locator)
        found_match = False
        for li in el_selector_li_list:
            el_em = li.find_element(*CommonLocs.el_em_locator)
            text = el_em.get_attribute('innerHTML')
            # logging.info(f'seq:{text}')
            if name == text:
                li.click()
                logging.info(f'select config item name: {name}')
                found_match = True
                break
        if not found_match:
            logging.error(f"{name}不存在！")
        return len(el_selector_li_list)

    def to_config(self, name='', config_type=ConfigType.SEQUENCE):
        time.sleep(0.3)
        if config_type == ConfigType.CAPTURE:
            self.wait_element_clickable_and_click(HomeLocs.el_create_cc_locator)
            # logging.info(f'go to cc config')
            if name:
                return self.select_config_by_name(name)
        elif config_type == ConfigType.SEQUENCE:
            if not name:
                self.wait_element_clickable_and_click(HomeLocs.el_sequence_back_btn_locator)
                # logging.info(f'go to seq config')
            else:
                return self.select_config_by_name(name)

    def create_sequence(self, name):
        # 点击添加按钮
        self.wait_element_clickable_and_click(HomeLocs.el_add_sequence_btn_locator)
        # 清除并输入名字
        el_sequence_name_input = self.location_element(HomeLocs.el_sequence_name_input_locator)
        self.clear_and_enter_text(el_sequence_name_input, name)
        # 点击创建按钮
        self.wait_element_clickable_and_click(HomeLocs.el_create_sequence_btn_locator)
        logging.info(f'create a seq named: {name}')
        # 断言-点击进入一次
        time.sleep(0.3)
        self.select_config_by_name(name)

    def create_cc(self, cc_name):
        # 进入cc config页面
        self.to_config('', ConfigType.CAPTURE)
        # 设置名称
        el_cc_name_input = self.location_element(HomeLocs.el_cc_name_input_locator)
        self.clear_and_enter_text(el_cc_name_input, cc_name)
        # 点击创建按钮
        self.wait_element_clickable_and_click(HomeLocs.el_create_cc_btn_locator)
        logging.info(f'create cc named: {cc_name}')
        # 返回seq config页面
        self.to_config('', ConfigType.SEQUENCE)

    def set_cc_exposure(self, cc_name, exposure):
        # 进入cc config页面
        self.to_config(cc_name, ConfigType.CAPTURE)

        # 设置曝光
        el_exposure_selector = self.location_element(HomeLocs.el_exposure_selector_locator)
        exposure_values = el_exposure_selector.find_elements(*CommonLocs.el_span_locator)
        exposure_values[exposure].click()
        logging.info(f'update cc:{cc_name} set exposure = {exposure}')

        # 更新设置
        self.click(HomeLocs.el_cc_update_btn_locator)
        # 返回seq_config页面
        self.to_config('', ConfigType.SEQUENCE)

    def set_cc_pattern_v4(self, cc_name, pattern_select=PatternSelect.OUTERMOST_BY_RING):
        # 进入cc config页面
        self.to_config(cc_name, ConfigType.CAPTURE)

        # 获取pattern path 元素
        el_pattern_path_list = self.location_elements(HomeLocs.el_pattern_path_list_locator)
        self.click(HomeLocs.el_pattern_edit_mode_locator)

        # 选中最外图案（倒数第2-5个元素）
        if pattern_select == PatternSelect.OUTERMOST_BY_RING:
            self.click(HomeLocs.el_pattern_ring_mode_locator)
            el_pattern_path_list[-2].click()

        # 选中所有图案（倒数第2-5个元素）
        elif pattern_select == PatternSelect.ALL_BY_RING:
            self.click(HomeLocs.el_pattern_ring_mode_locator)
            for i in range(0, len(el_pattern_path_list), 4):
                el_pattern_path_list[i].click()

        # 选中第2个外圈左上/右下（倒数第6个和倒数第8个元素）
        elif pattern_select == PatternSelect.BY_NORMAL:
            el_pattern_path_list[-6].click()
            el_pattern_path_list[-8].click()

        logging.info(f'update cc:{cc_name} set pattern = {pattern_select}')

        # 更新设置
        self.click(HomeLocs.el_cc_update_btn_locator)
        # 返回seq_config页面
        self.to_config('', ConfigType.SEQUENCE)

    def delete_config(self, name, config_type=ConfigType.SEQUENCE, is_del_all=False):
        num = 0
        if config_type == ConfigType.SEQUENCE:
            num = self.to_config(name, ConfigType.SEQUENCE)
            if is_del_all:
                for n in range(num):
                    self.location_elements(HomeLocs.el_btn_list_locator)[1].click()
                    pyautogui.press('space')
            else:
                self.location_elements(HomeLocs.el_btn_list_locator)[1].click()
                pyautogui.press('space')
        elif config_type == ConfigType.CAPTURE:
            num = self.to_config(name, ConfigType.CAPTURE)
            if is_del_all:
                for n in range(num):
                    self.location_elements(HomeLocs.el_btn_list_locator)[2].click()
                    pyautogui.press('space')
            else:
                self.location_elements(HomeLocs.el_btn_list_locator)[2].click()
                pyautogui.press('space')


        # 断言
        el_tip = WebDriverWait(self.driver, timeout=2, poll_frequency=0.5).until(
            EC.presence_of_element_located(HomeLocs.el_tip_locator)
        )
        tip = el_tip.find_element(By.XPATH, './/div/div').text
        assert tip == 'Success: Sequence deleted'

    def select_exist_cc(self, cc_name):
        self.wait_element_clickable_and_click(HomeLocs.el_add_exist_cc_locator)
        el_cc_exist_list = self.location_element(HomeLocs.el_cc_exist_list_locator)
        cc_exist_list = el_cc_exist_list.find_elements(*CommonLocs.el_li_locator)
        for _ in cc_exist_list:
            cc_name_text = _.find_element(*CommonLocs.el_em_locator).get_attribute('innerHTML')
            if cc_name_text == cc_name:
                _.click()
                logging.info(f'select exist cc: {cc_name}')

    def add_cc_to_seq(self, cc_name, seq_name):
        self.select_config_by_name(seq_name)
        self.select_exist_cc(cc_name)
        time.sleep(0.2)
        self.wait_element_clickable_and_click(HomeLocs.el_sequence_update_btn_locator)
        self.select_cc_in_seq_page(cc_name)
        logging.info(f'add cc:{cc_name} to seq:{seq_name}')

    def select_cc_in_seq_page(self, cc_name):
        el_div_cc_list = self.location_element(HomeLocs.el_div_cc_list_in_seq_locator)
        el_li_list = el_div_cc_list.find_elements(*CommonLocs.el_li_locator)

        # logging.info(f'el_li_list.size: {len(el_li_list)}')
        for _ in el_li_list:
            cc_name_text = _.find_element(*CommonLocs.el_span_locator).get_attribute('innerHTML')
            if cc_name_text == cc_name:
                _.click()
                logging.info(f'select cc:{cc_name}')
                break

    def save_image_in_seq_page(self, seq_name, path, count=1, is_min_exposure=False, is_max_exposure=False):
        if not os.path.exists(path):
            os.mkdir(path)
            logging.info(f'{path} not exist and create it.')

        self.select_config_by_name(seq_name)

        el_div_cc_list = self.location_element(HomeLocs.el_div_cc_list_in_seq_locator)
        el_li_list = el_div_cc_list.find_elements(*CommonLocs.el_li_locator)
        cc_count_in_seq = len(el_li_list)

        count_compute = 0
        if is_min_exposure:
            count_compute += 1
        if is_max_exposure:
            count_compute += 1

        self.click(HomeLocs.el_div_choose_saving_image_folder_path)
        time.sleep(0.8)

        pyautogui.typewrite(path, interval=0.05)
        time.sleep(0.3)

        pyautogui.press('enter')
        time.sleep(0.5)

        image_count_init = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        time.sleep(0.5)

        if is_min_exposure:
            self.click(HomeLocs.el_save_in_max_locator)
        if is_max_exposure:
            self.click(HomeLocs.el_save_in_min_locator)

        for _ in range(count):
            self.click(HomeLocs.el_save_image_locator)

        time.sleep(0.5)
        image_count_end = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        logging.info(f'image_count_init:{image_count_init} - image_count_end:{image_count_end}')
        logging.info(f'save {(image_count_end - image_count_init)} images')

        if not is_max_exposure and not is_min_exposure:
            assert cc_count_in_seq == (image_count_end - image_count_init)
        else:
            assert count_compute == (image_count_end - image_count_init)

    def upload_to_controller(self, seq_name, io):
        self.select_config_by_name(seq_name)
        el_io_input = self.location_element(HomeLocs.el_io_input_locator)
        self.clear_and_enter_text(el_io_input, io)
        self.click(HomeLocs.el_io_upload_btn_locator)

        try:
            el_tip = WebDriverWait(self.driver, timeout=2, poll_frequency=0.5).until(
                EC.presence_of_element_located(HomeLocs.el_tip_locator)
            )
        except TimeoutException:
            self.wait_element_clickable_and_click(HomeLocs.el_confirm_btn_locator)
            el_tip = self.wait_element_presence(HomeLocs.el_tip_locator)
        tip = el_tip.find_element(By.XPATH, './/div/div').text
        assert tip == f'Success: Sequence uploaded to hardware io: {io}'


