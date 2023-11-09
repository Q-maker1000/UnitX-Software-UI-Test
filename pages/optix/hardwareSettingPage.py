import datetime
import os
import time

import pyautogui
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageLocators.optix.hardwareSettingLocs import HardwareSettingLocs
from pageLocators.optix.homeLocs import HomeLocs
from utils import start_software
from pageLocators.optix.commonLocs import CommonLocs
from utils.basePage import BasePage


def count_files_in_folder(folder_path):
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)
    return file_count


class HardwareSettingPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def check_version(self, version):
        self.wait_element_clickable_and_click(CommonLocs.el_nav_locator)
        el_version = self.wait_element_presence(CommonLocs.el_version_locator)
        version_text = el_version.get_attribute("innerHTML")
        assert version_text == version

    def config_hardware_setting(self):
        for i in range(3):
            el_OK_btn = self.wait_element_presence(HardwareSettingLocs.el_OK_locator)
            if el_OK_btn.is_enabled():
                self.wait_element_clickable_and_click(HardwareSettingLocs.el_OK_locator)
                break
            else:
                self.click(HardwareSettingLocs.el_refresh_locator)

    def create_sequence(self, name):
        # 点击添加按钮
        self.wait_element_clickable_and_click(HomeLocs.el_add_sequence_btn_locator)
        # 清除并输入名字
        el_sequence_name_input = self.location_element(HomeLocs.el_sequence_name_input_locator)
        self.clear_and_enter_text(el_sequence_name_input, name)

        # 点击创建按钮
        self.wait_element_clickable_and_click(HomeLocs.el_create_sequence_btn_locator)

        # 断言名字
        self.click(HomeLocs.el_sequence_selector_locator)
        el_sequence_selected_li = self.wait_element_presence(HomeLocs.el_cc_sequence_selected_li_locator)
        el_sequence_name = el_sequence_selected_li.find_element(*CommonLocs.el_em_locator)
        sequence_name = el_sequence_name.get_attribute('innerHTML')
        el_sequence_selected_li.click()
        assert sequence_name == name

    def create_capture(self, name, count=1, exposure=19, is_ring=True, controller_version="v4"):
        self.wait_element_clickable_and_click(HomeLocs.el_create_cc_locator)

        for c in range(count):
            # 设置名称
            el_cc_name_input = self.location_element(HomeLocs.el_cc_name_input_locator)
            self.clear_and_enter_text(el_cc_name_input, name+str(c))

            # 调节曝光
            el_exposure_selector = self.location_element(HomeLocs.el_exposure_selector_locator)
            exposure_values = el_exposure_selector.find_elements(*CommonLocs.el_span_locator)
            exposure_values[exposure].click()

            # 选择模式
            self.click(HomeLocs.el_pattern_edit_mode_locator)
            if is_ring:
                self.click(HomeLocs.el_pattern_ring_mode_locator)
            else:
                self.click(HomeLocs.el_pattern_normal_mode_locator)

            # 选择图案
            if controller_version == 'v4':
                self.select_pattern_v4()

            self.wait_element_clickable_and_click(HomeLocs.el_create_cc_btn_locator)

            # 断言(这边采用截图方式断言),因为需要断言的地方太多了.需要的话后续补上
            self.wait_element_clickable_and_click(HomeLocs.el_cc_selector_locator)
            el_cc_selected_li = self.wait_element_presence(HomeLocs.el_cc_sequence_selected_li_locator)
            el_cc_name = el_cc_selected_li.find_element(*CommonLocs.el_em_locator)
            cc_name = el_cc_name.get_attribute('innerHTML')
            # 断言名字
            assert cc_name == name+str(c)
            # 剩下的截图断言
            el_cc_selected_li.click()
            time.sleep(1)
            self.screen_shot("create_capture")
            self.click(HomeLocs.el_cc_new_btn_locator)

    def select_pattern_v4(self):
        el_select_light_form = self.location_element(HomeLocs.el_select_light_form_locator)
        light_list = el_select_light_form.find_elements(*CommonLocs.el_path_locator)
        # 最外圈元素 (倒数2,3,4,5个)
        outermost_light_circle = light_list[-2]
        outermost_light_circle.click()

    def add_cc_to_sequence(self, sequence_name="", sequence_index=0, is_all_cc=False):
        # TODO 这里可以封装
        # 选择序列
        if sequence_name == "":
            self.wait_element_clickable_and_click(HomeLocs.el_sequence_selector_locator)
            el_sequence_list = self.location_element(HomeLocs.el_sequence_list_locator)
            sequence_list = el_sequence_list.find_elements(*CommonLocs.el_li_locator)
            sequence_list[sequence_index].click()
        else:
            self.wait_element_clickable_and_click(HomeLocs.el_sequence_selector_locator)
            el_sequence_list = self.wait_element_presence(HomeLocs.el_sequence_list_locator)
            el_sequence_li_list = el_sequence_list.find_elements(*CommonLocs.el_li_locator)
            for i in el_sequence_li_list:
                seq_name = i.find_element(*CommonLocs.el_em_locator).text
                if seq_name == sequence_name:
                    i.click()

        # 获取sequence原有cc数(包含两个按钮所以要 -2)
        cc_count_old = len(self.location_elements(HomeLocs.el_cc_list_locator))-2

        # 添加cc
        cc_exist_list = self.get_cc_exist_list()
        # 添加前exist_cc列表中的cc数
        exist_cc_count = len(cc_exist_list)

        if is_all_cc:
            for i in range(exist_cc_count-1):
                cc_exist_list[0].click()
                cc_exist_list = self.get_cc_exist_list()

        cc_exist_list[0].click()

        # 更新设置
        self.click(HomeLocs.el_sequence_update_btn_locator)
        self.screen_shot('add cc')

        # 获取更新后cc数
        cc_count_new = len(self.location_elements(HomeLocs.el_cc_list_locator)) - 2
        assert (cc_count_new - cc_count_old) != 0

        if is_all_cc:
            assert (cc_count_new - cc_count_old) == exist_cc_count
        else:
            assert (cc_count_new - cc_count_old) == 1

    def get_cc_exist_list(self):
        self.wait_element_clickable_and_click(HomeLocs.el_add_exist_cc_locator)
        el_cc_exist_list = self.location_element(HomeLocs.el_cc_exist_list_locator)
        cc_exist_list = el_cc_exist_list.find_elements(*CommonLocs.el_li_locator)
        return cc_exist_list

    def save_image(self, sequence_name='', sequence_index=0, count=1, is_compute=False):
        # 创建存放图片文件夹
        today = datetime.date.today()
        ts = today.strftime("%Y-%m-%d")
        folder_path = "/home/unitx/Qian/pytest-ui/utils/0_image-" + ts
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # 选择序列
        if sequence_name == "":
            self.wait_element_clickable_and_click(HomeLocs.el_sequence_selector_locator)
            el_sequence_list = self.location_element(HomeLocs.el_sequence_list_locator)
            sequence_list = el_sequence_list.find_elements(*CommonLocs.el_li_locator)
            sequence_list[sequence_index].click()
        else:
            self.wait_element_clickable_and_click(HomeLocs.el_sequence_selector_locator)
            el_sequence_list = self.wait_element_presence(HomeLocs.el_sequence_list_locator)
            el_sequence_li_list = el_sequence_list.find_elements(*CommonLocs.el_li_locator)
            for i in el_sequence_li_list:
                seq_name = i.find_element(*CommonLocs.el_em_locator).text
                if seq_name == sequence_name:
                    print("11111111111111111111111111111111111111111")
                    i.click()
                    break

        # 选择folder路径
        self.wait_element_clickable_and_click(HomeLocs.el_select_folder_locator)

        # 使用pyautogui来处理系统窗口
        pyautogui.press('up')
        pyautogui.typewrite("0_image-" + ts)
        time.sleep(0.3)
        pyautogui.press('enter')
        pyautogui.press('enter')

        # 勾选 max 和 min 复选框
        if is_compute:
            self.click(HomeLocs.el_save_in_max_locator)
            self.click(HomeLocs.el_save_in_min_locator)

        # 获取cc数量
        cc_count = len(self.location_elements(HomeLocs.el_cc_list_locator)) - 2
        assert cc_count != 0

        # 记录初始文件数量
        initial_count = count_files_in_folder(folder_path)

        # 点击保存
        for i in range(count):
            time.sleep(0.3)
            self.wait_element_clickable_and_click(HomeLocs.el_save_image_locator)

        # 再次检查文件数量
        time.sleep(1)
        new_count = count_files_in_folder(folder_path)
        # 计算增加量
        file_increase = new_count - initial_count
        if is_compute:
            print(f'new_count:{new_count}, initial_count:{initial_count}, 2*count:{2 * count}')
            assert file_increase == 2 * count
        else:
            print(f'new_count:{new_count}, initial_count:{initial_count}, 2*count:{cc_count * count}')
            assert file_increase == cc_count * count

    def upload_to_controller(self, name, io_id):
        self.wait_element_clickable_and_click(HomeLocs.el_sequence_selector_locator)
        el_sequence_list = self.wait_element_presence(HomeLocs.el_sequence_list_locator)
        el_sequence_li_list = el_sequence_list.find_elements(*CommonLocs.el_li_locator)
        for i in el_sequence_li_list:
            sequence_name = i.find_element(*CommonLocs.el_em_locator).text
            if sequence_name == name:
                i.click()
                break
        el_io_input = self.location_element(HomeLocs.el_io_input_locator)
        io_input = el_io_input.get_attribute('value')
        self.clear_and_enter_text(el_io_input, io_id)
        self.click(HomeLocs.el_io_upload_btn_locator)

        try:
            el_tip = WebDriverWait(self.driver, timeout=2, poll_frequency=0.5).until(
                EC.presence_of_element_located(HomeLocs.el_tip_locator)
            )
        except TimeoutException:
            print("11111111111111")
            self.wait_element_clickable_and_click(HomeLocs.el_confirm_btn_locator)
            el_tip = self.wait_element_presence(HomeLocs.el_tip_locator)

        tip = el_tip.find_element(By.XPATH, './/div/div').text
        self.screen_shot("upload_controller")
        assert tip == f'Success: Sequence uploaded to hardware io: {io_id}'


if __name__ == '__main__':
    # cc_name1 = "ui_test_09"
    driver = start_software.start("optix")
    HardwareSettingPage(driver).config_hardware_setting()
    HardwareSettingPage(driver).upload_to_controller("ui_test_v3110_001_2023-11-091", 9)
    driver.quit()