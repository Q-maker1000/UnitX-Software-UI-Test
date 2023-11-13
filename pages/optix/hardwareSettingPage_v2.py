import pyautogui
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
        el_selector_li_list = self.location_elements(HomeLocs.el_selector_li_list_locator)
        found_match = False
        for li in el_selector_li_list:
            el_em = li.find_element(*CommonLocs.el_em_locator)
            text = el_em.get_attribute('innerHTML')
            if name == text:
                li.click()
                found_match = True
                break
        if not found_match:
            print(f"{name}不存在！")
        return len(el_selector_li_list)

    def to_config(self, name='', config_type=ConfigType.SEQUENCE):
        if config_type == ConfigType.CAPTURE:
            self.wait_element_clickable_and_click(HomeLocs.el_create_cc_locator)
            if name:
                return self.select_config_by_name(name)
        elif config_type == ConfigType.SEQUENCE:
            if not name:
                self.wait_element_clickable_and_click(HomeLocs.el_sequence_back_btn_locator)
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
        # 断言-点击进入一次
        self.to_config(name, ConfigType.SEQUENCE)

    def create_cc(self, cc_name):
        # 进入cc config页面
        self.to_config('', ConfigType.CAPTURE)
        # 设置名称
        el_cc_name_input = self.location_element(HomeLocs.el_cc_name_input_locator)
        self.clear_and_enter_text(el_cc_name_input, cc_name)
        # 点击创建按钮
        self.wait_element_clickable_and_click(HomeLocs.el_create_cc_btn_locator)

        # 返回seq config页面
        self.to_config('', ConfigType.SEQUENCE)

    def set_cc_exposure(self, cc_name, exposure):
        # 进入cc config页面
        self.to_config(cc_name, ConfigType.CAPTURE)

        # 设置曝光
        el_exposure_selector = self.location_element(HomeLocs.el_exposure_selector_locator)
        exposure_values = el_exposure_selector.find_elements(*CommonLocs.el_span_locator)
        exposure_values[exposure].click()

        # 更新设置
        self.click(HomeLocs.el_cc_update_btn_locator)
        # 截图断言
        self.screen_shot('set_cc_exposure')
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

        # 选中最外图案（倒数第2-5个元素）
        elif pattern_select == PatternSelect.ALL_BY_RING:
            self.click(HomeLocs.el_pattern_ring_mode_locator)
            for i in range(0, len(el_pattern_path_list), 4):
                el_pattern_path_list[i].click()

        # 选中第2个外圈左上/右下（倒数第6个和倒数第8个元素）
        elif pattern_select == PatternSelect.BY_NORMAL:
            el_pattern_path_list[-6].click()
            el_pattern_path_list[-8].click()

        # 更新设置
        self.click(HomeLocs.el_cc_update_btn_locator)
        # 截图断言
        self.screen_shot('set_cc_pattern_v4')
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


if __name__ == '__main__':
    driver = start_software.start("optix")
    hardwareSettingPage2 = HardwareSettingPage_v2(driver)
    hardwareSettingPage = HardwareSettingPage(driver)

    hardwareSettingPage.config_hardware_setting()
    hardwareSettingPage2.to_config('c3', ConfigType.CAPTURE)
    hardwareSettingPage2.to_config()



