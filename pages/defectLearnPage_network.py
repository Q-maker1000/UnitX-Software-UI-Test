import json
import re
import time
from datetime import datetime

import requests
from selenium.webdriver.common.by import By

from config.global_params import Cookie
from pageLocators.commonLocs import CommonLocs
from pageLocators.defectLearnLocs import DefectLearnLocs
from pageLocators.labelLocs import LabelLocs
from pages.labelPage import LabelPage
from utils.basePage import BasePage
from utils.common import login


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
        # 5.判断network是否存在
        self.is_exist_network(name, 'create network')

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
        el_network_list = self.location_elements(DefectLearnLocs.el_network_list_locator)
        for el_network in el_network_list:
            el_network_name = el_network.find_element(*DefectLearnLocs.el_h2_locator)
            network_name = el_network_name.get_attribute("innerHTML")
            if name == network_name:
                return el_network
        return None

    def is_exist_network(self, name, message=''):
        self.driver.refresh()
        target = DefectLearnPage_Network(driver).find_network_by_name(name)
        if target is not None:
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # 6. 截图
            self.screen_shot(message)
        else:
            print("no network exist!")

    def import_image(self, dir, name, cookie):
        headers = {
            'Content-type': 'application/json',
            'Cookie': cookie,  ## 这里也可以设置cookie
            'Origin': 'file://'
        }
        url = "http://127.0.0.1:10000/api/v1/network/import_images"
        data = {
            "dir": dir,
            "network_name": name
        }
        json_data = json.dumps(data)
        res = requests.post(url=url, data=json_data, headers=headers)
        self.is_exist_network(name, 'import image')
        return res

    def delete_network(self, name='all'):
        el_network = ""
        if name != 'all':
            # 定位network
            try:
                el_network = self.find_network_by_name(name)
                self.driver.execute_script("arguments[0].scrollIntoView();", el_network)
                self.screen_shot("get network before delete")
            except:
                print("no network exist!")
            # 定位删除按钮
            el_network_header = el_network.find_element(*DefectLearnLocs.el_network_header_locator)
            btn_delete_network_list = el_network_header.find_elements(*DefectLearnLocs.el_button_locator)
            btn_delete_network = btn_delete_network_list[-1]
            # 点击删除按钮
            btn_delete_network.click()
            # 确认删除
            btn_confirm_delete_network = self.location_element(DefectLearnLocs.el_btn_confirm_locator)
            self.click(btn_confirm_delete_network)
            btn_confirm_delete_network = self.location_element(DefectLearnLocs.el_btn_confirm_locator)
            self.click(btn_confirm_delete_network)
            time.sleep(0.5)
            self.screen_shot("get network after delete")
        else:
            network_list = self.list_network()
            for network in network_list:
                el_network_header = network.find_element(*DefectLearnLocs.el_network_header_locator)
                btn_delete_network_list = el_network_header.find_elements(*DefectLearnLocs.el_button_locator)
                btn_delete_network = btn_delete_network_list[-1]
                # 点击删除按钮
                time.sleep(0.5)
                btn_delete_network.click()
                # 确认删除
                btn_confirm_delete_network = self.location_element(DefectLearnLocs.el_btn_confirm_locator)
                self.click(btn_confirm_delete_network)
                btn_confirm_delete_network = self.location_element(DefectLearnLocs.el_btn_confirm_locator)
                self.click(btn_confirm_delete_network)

    def go_label_page(self, name):
        network_bottom_enable_btn_list = self.get_enable_btn_in_network_bottom(name)
        if len(network_bottom_enable_btn_list) == 0:
            print("no image in label, please import image!")
            return False
        btn_label = network_bottom_enable_btn_list[0]
        # 判断是否获取label标签
        span_label = btn_label.find_element(*DefectLearnLocs.el_span_locator).get_attribute("innerHTML")
        if span_label == "Label":
            # 若获取标签, 进行点击
            self.wait_element_clickable_and_click(btn_label)
            return True
        # 若没获取标签, 提示请导入新照片
        else:
            print("no image in label, please import image!")
            return False

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

    def wait_training(self, name):
        # 获取network_bottom
        time.sleep(3)
        driver.refresh()
        network = self.find_network_by_name(name)
        network_bottom = network.find_element(*DefectLearnLocs.el_network_bottom_locator)
        # 获取第四个div
        div_list = network_bottom.find_elements(*DefectLearnLocs.el_row_network_bottom_locator)
        print(div_list)
        for d in div_list:
            print(d.get_attribute("outerHTML"))
        # 获取tag_name为i的内容
        str_i = div_list[3].find_element(*CommonLocs.el_i_locator).get_attribute("innerHTML")
        print(div_list[3].get_attribute("outerHTML"))
        print(str_i)
        # 判断是否包含remaining
        if "remaining" in str_i:
            # 包含, 获取数字
            # 以.为切割
            print(00000)
            str_i_list = str_i.split(".")
            # 获取第二段数字
            remain_time = re.findall("r'/d+'", str_i_list[1])
            print(remain_time[0] + 1)
            # 截图
            self.screen_shot("network was training")
            # 设置time.sleep(数字加1)
            time.sleep(remain_time[0] + 1)
            print("training will completed")
            # 结束返回True
            return True
        else:
            print("baocuo")
        # else:
        #     # 循环执行本函数,次数3次,3次后无法匹配remaining返回false
        #     for n in range(4):
        #         time.sleep(3)
        #         self.wait_training(network)
        #     # 截图
        #     self.screen_shot("can not get training time")
        #     print("can not get training time")
        #     five_min = 5*60
        #     time.sleep(five_min)
        #     return False


if __name__ == '__main__':
    driver = login()
    # ts = int(time.time())
    ts = datetime.now().strftime("%Y-%m-%d-%s")
    network_n = 'a_v3105_' + str(ts)
    # network_n = 'a_test-ui_' + str(ts)
    # network_n = 'a_test-ui_2023-10-20-1697794650'

    # 删除network
    # DefectLearnPage_Network(driver).delete_network()


    # 查找模型并返回模型元素
    # network_name = 'a_test-ui_01'
    # network = DefectLearnPage_Network(driver).find_network_by_name(network_name)
    # print(network)


    # 创建模型并导入图片
    # for i in range(1):
    #     print(network_n)
    #     DefectLearnPage_Network(driver).create_network(network_n)
    #     time.sleep(1)
    # cookie = Cookie
    # # path = "/home/unitx/图片/CATL-image"
    # path = "/home/unitx/图片/20230912-c2"
    # res = DefectLearnPage_Network(driver).import_image(path, network_n, cookie)
    # print(res)
    # DefectLearnPage_Network(driver).delete_network(network_name)

    # 从头训练

    # 预处理
    # DefectLearnPage_Network(driver).create_network(network_n)
    # network1 = DefectLearnPage_Network(driver).find_network_by_name(network_n)
    # print(network1.get_attribute("outerHTML"))
    # cookie = Cookie
    # path = "/home/unitx/图片/20230912-c2"
    # res = DefectLearnPage_Network(driver).import_image(path, network_n, cookie)
    # print(res)
    # DefectLearnPage_Network(driver).go_label_page(network_n)
    # DefectLearnPage_Network(driver).pre_process(0, 2448, 0, 2048, 2448, 2048)
    # LabelPage(driver).labeling(5)
    # DefectLearnPage_Network(driver).select_btn_in_network_bottom(network_n, "Train From Scratch")
    DefectLearnPage_Network(driver).wait_training("a_test-ui_2023-10-23-1698032640")

    time.sleep(10)
    driver.quit()






