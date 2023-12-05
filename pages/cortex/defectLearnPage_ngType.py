import logging
import time
from datetime import datetime

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageLocators.cortex.commonLocs import CommonLocs
from pageLocators.cortex.defectLearnLocs import DefectLearnLocs
from utils.basePage import BasePage
from utils.common import login


class DefectLearnPage_NGTYPE(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def check_version(self, version):
        self.wait_element_clickable_and_click(CommonLocs.el_btn_nav_locator)
        el_div_version = self.wait_element_presence(CommonLocs.el_div_version_locator)
        text_version = el_div_version.get_attribute('innerHTML')
        logging.info(f'CorteX Version is {text_version}')
        assert text_version == version
        pyautogui.click(800, 10)

    def create_ng_type(self, ng_type_name):
        # 点击ng type管理按钮
        self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_ng_type_manager_locator)
        time.sleep(0.05)
        # 点击创建ng type按钮
        self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_create_ng_type_locator)
        # 输入ng type名称
        self.clear_text(DefectLearnLocs.el_ipt_ng_type_name_locator)
        self.enter_text(DefectLearnLocs.el_ipt_ng_type_name_locator, ng_type_name)
        # 点击创建
        self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_confirm_ng_type_locator)
        logging.info(f'create defect type：{ng_type_name}')
        time.sleep(0.5)
        # ActionChains(self.driver).move_by_offset(0, 800).click().perform()
        pyautogui.click(0, 800)

    def delete_ng_type(self, name=''):
        # 点击ng type管理按钮
        self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_ng_type_manager_locator)
        # 获取ng type列表
        row_ng_list = self.location_elements(DefectLearnLocs.el_row_ng_type_locator)
        if name != '':
            # 在列表中查找对应名字的ng type
            for row_ng in row_ng_list:
                ng_type_name = row_ng.find_element(By.TAG_NAME, 'div').get_attribute('innerHTML')
                if name == ng_type_name:
                    self.driver.execute_script("arguments[0].scrollIntoView();", row_ng)
                    self.screen_shot("get ng type name before delete")
                    # 获取ng type删除按钮
                    btn_list = row_ng.find_elements(*DefectLearnLocs.el_button_locator)
                    btn_delete_ng_type = btn_list[-1]
                    # 点击删除按钮
                    btn_delete_ng_type.click()
                    # 确认删除ng type
                    self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_confirm_locator)
                    self.screen_shot("get ng type name after delete")
            print("无法获取该ng type")
        else:
            self.screen_shot("get ng type list")
            # 依次删除
            for row_ng in row_ng_list:
                time.sleep(0.05)
                btn_list = row_ng.find_elements(*DefectLearnLocs.el_button_locator)
                # 获取ng type删除按钮
                btn_delete_ng_type = btn_list[-1]
                # 点击删除按钮
                btn_delete_ng_type.click()
                # 确认删除ng type
                self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_confirm_locator)
            self.screen_shot("get ng type list after delete")

    def edit_ng_type(self, new_name, old_name):
        # 点击ng type管理按钮
        # self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_ng_type_manager_locator)
        # 获取ng type列表
        row_ng_list = self.location_elements(DefectLearnLocs.el_row_ng_type_locator)
        if old_name != '':
            # 在列表中查找对应名字的ng type
            # TODO 优化1: 可以用算法进行匹配而非遍历
            # TODO 优化2: 可以封装成函数重复利用
            for row_ng in row_ng_list:
                ng_type_name = row_ng.find_element(By.TAG_NAME, 'div').get_attribute('innerHTML')
                if old_name == ng_type_name:
                    # 滑动到制定位置并截屏
                    self.driver.execute_script("arguments[0].scrollIntoView();", row_ng)
                    self.screen_shot("get ng type name before edit")
                    # 获取ng type编辑按钮
                    btn_list = row_ng.find_elements(*DefectLearnLocs.el_button_locator)
                    btn_delete_ng_type = btn_list[0]
                    # 点击编辑按钮
                    btn_delete_ng_type.click()
                    # 输入新名字
                    self.clear_text(DefectLearnLocs.el_ipt_ng_type_name_locator)
                    self.enter_text(DefectLearnLocs.el_ipt_ng_type_name_locator, new_name)
                    # 点击更新名字按钮
                    time.sleep(0.05)
                    self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_confirm_ng_type_locator)
                    # 确认更新ng type
                    self.wait_element_clickable_and_click(DefectLearnLocs.el_btn_confirm_locator)
                    # 截屏
                    time.sleep(0.05)
                    self.screen_shot("get ng type name after edit")
                    print("edited ng type successfully")
                    return True
            print("no ng type name %s" % old_name)


if __name__ == '__main__':
    for i in range(2):
        ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-1]
        print(ts)
