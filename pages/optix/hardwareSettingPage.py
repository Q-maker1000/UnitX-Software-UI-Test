import datetime
import os
import pyautogui
from selenium.webdriver import ActionChains, Keys

from pageLocators.optix.hardwareSettingLocs import HardwareSettingLocs
from pageLocators.optix.homeLocs import HomeLocs
from utils import start_software
from pageLocators.optix.commonLocs import CommonLocs
from utils.basePage import BasePage


class HardwareSettingPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def check_version(self, version):
        self.wait_element_clickable_and_click(CommonLocs.el_nav_locator)
        el_version = self.wait_element_presence(CommonLocs.el_version_locator)
        version_text = el_version.get_attribute("innerHTML")
        assert version_text == version

    def config_hardware_setting(self):
        self.wait_element_clickable_and_click(HardwareSettingLocs.el_OK_locator)

    def create_sequence(self, name):
        # 点击添加按钮
        self.wait_element_clickable_and_click(HomeLocs.el_add_sequence_btn_locator)

        # 清除并输入名字
        el_sequence_name_input = self.location_element(HomeLocs.el_sequence_name_input_locator)
        self.clear_and_enter_text(el_sequence_name_input, name)

        # 点击创建按钮
        self.wait_element_clickable_and_click(HomeLocs.el_create_sequence_btn_locator)

    def create_capture(self, name, exposure=19, is_ring=True, controller_version="v4"):
        self.wait_element_clickable_and_click(HomeLocs.el_create_cc_locator)

        # 设置名称
        el_cc_name_input = self.location_element(HomeLocs.el_cc_name_input_locator)
        self.clear_and_enter_text(el_cc_name_input, name)

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

    def select_pattern_v4(self):
        el_select_light_form = self.location_element(HomeLocs.el_select_light_form_locator)
        light_list = el_select_light_form.find_elements(*CommonLocs.el_path_locator)
        # 最外圈元素 (倒数2,3,4,5个)
        outermost_light_circle = light_list[-2]
        outermost_light_circle.click()

    def add_cc_to_sequence(self, sequence_name="", sequence_index=0, is_all_cc=False):
        # 选择序列
        if sequence_name == "":
            self.wait_element_clickable_and_click(HomeLocs.el_sequence_selector_locator)
            el_sequence_list = self.location_element(HomeLocs.el_sequence_list_locator)
            sequence_list = el_sequence_list.find_elements(*CommonLocs.el_li_locator)
            sequence_list[sequence_index].click()
        # 添加cc
        cc_exist_list = self.get_cc_exist_list()

        if is_all_cc:
            exist_cc_count = len(cc_exist_list)
            for i in range(exist_cc_count-1):
                cc_exist_list[0].click()
                cc_exist_list = self.get_cc_exist_list()

        cc_exist_list[0].click()

        # 更新设置
        self.wait_element_clickable_and_click(HomeLocs.el_sequence_update_btn_locator)

    def get_cc_exist_list(self):
        self.wait_element_clickable_and_click(HomeLocs.el_add_exist_cc_locator)
        el_cc_exist_list = self.location_element(HomeLocs.el_cc_exist_list_locator)
        cc_exist_list = el_cc_exist_list.find_elements(*CommonLocs.el_li_locator)
        return cc_exist_list

    def save_image_without_compute(self, count=1):
        # 创建存放图片文件夹
        today = datetime.date.today()
        ts = today.strftime("%Y-%m-%d")
        folder_path = "/home/unitx/optix/optix_src/0_image-" + ts
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # 选择folder路径
        self.wait_element_clickable_and_click(HomeLocs.el_select_folder_locator)

        # 使用pyautogui来处理系统窗口
        file_path = "/path/to/file.txt"
        pyautogui.write(file_path)
        pyautogui.press('enter')

        ActionChains(self.driver).send_keys(Keys.UP).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

        # for i in range(count):
        #     self.wait_element_clickable_and_click(HomeLocs.el_save_image_locator)


if __name__ == '__main__':
    driver = start_software.start("optix")
    HardwareSettingPage(driver).config_hardware_setting()
    HardwareSettingPage(driver).save_image_without_compute()
