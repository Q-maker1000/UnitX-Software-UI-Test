import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageLocators.cortex.commonLocs import CommonLocs
from pageLocators.cortex.labelLocs import LabelLocs
from pageLocators.cortex.reviewLabelLocs import ReviewLabelLocs
from utils.basePage import BasePage


class LabelPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def labeling(self, image_num=1, choice='label_01'):
        # 获取图片列表
        image_list = self.location_elements(LabelLocs.el_image_list_locator)
        # 判断照片是否存在
        total = len(image_list)
        logging.info(f'total:{total}')
        if total != 0:
            # 若存在,循环以下操作(打标操作)
            for i in range(image_num):
                if choice == 'label_01':
                    self.label_01()
                elif choice == 'label_02':
                    self.label_02()
                elif choice == 'label_03':
                    self.label_03()
                elif choice == 'label_04':
                    self.label_04()
                elif choice == 'label_05':
                    self.label_05()
                else:
                    logging.error('No label pattern u choose!')
                    raise Exception
            # 返回主页
            self.wait_element_clickable_and_click(CommonLocs.el_go_back_locator)
        # 若不存在,提示请导入新照片
        else:
            logging.error("no image in label, please import image!")

    # def labeling(self):
    def label_01(self):
        # 获取label按钮并点击
        self.wait_element_clickable_and_click(LabelLocs.el_btn_label_locator)
        # 获取幕布
        canvas = self.wait_element_presence(LabelLocs.el_canvas_locator)
        # print(canvas)
        # 打标签操作-鼠标点击
        (ActionChains(self.driver).click(canvas).
         move_by_offset(0, 100).click()
         .move_by_offset(100, 0).click()
         # 键盘保存操作
         .send_keys('s')
         .perform())
        # 点击SAVE按钮保存
        self.wait_element_clickable_and_click(LabelLocs.el_btn_save_locator)

    def label_02(self):
        # 获取label按钮并点击
        self.wait_element_clickable_and_click(LabelLocs.el_btn_label_locator)
        # 获取幕布
        canvas = self.wait_element_presence(LabelLocs.el_canvas_locator)
        # 打标签操作-鼠标点击
        (ActionChains(self.driver).click(canvas)
         .send_keys('z')
         .move_by_offset(0, 100).click()
         .move_by_offset(0, 100).click()
         .move_by_offset(100, 0).click()
         .move_by_offset(0, -100).click()
         # 键盘保存操作
         .send_keys('s')
         .perform())
        # 点击SAVE按钮保存
        self.wait_element_clickable_and_click(LabelLocs.el_btn_save_locator)

    def label_03(self):
        # 获取label按钮并点击
        self.wait_element_clickable_and_click(LabelLocs.el_btn_label_locator)
        # 获取幕布
        canvas = self.wait_element_presence(LabelLocs.el_canvas_trained_locator)
        logging.info(f'get canvas')
        # 打标签操作-鼠标点击
        (ActionChains(self.driver).click(canvas)
         .send_keys('z')
         .move_by_offset(0, 210).click()
         .move_by_offset(0, 100).click()
         .move_by_offset(100, 0).click()
         .move_by_offset(0, -100).click()
         # 键盘保存操作
         .send_keys('s')
         .perform())
        logging.info(f'finish 03 label in a image')
        # 点击SAVE按钮保存
        self.wait_element_clickable_and_click(LabelLocs.el_btn_save_locator)

    def label_04(self):
        # 获取label按钮并点击
        self.wait_element_clickable_and_click(LabelLocs.el_btn_label_locator)
        # 获取幕布
        canvas = self.wait_element_presence(LabelLocs.el_canvas_trained_locator)
        # 打标签操作-鼠标点击
        (ActionChains(self.driver).click(canvas)
         .send_keys('z')
         .move_by_offset(0, -100).click()
         .move_by_offset(0, -100).click()
         .move_by_offset(100, 0)
         .move_by_offset(0, 100)
         .click()
         # 键盘保存操作
         .send_keys('s')
         .perform())
        # 点击SAVE按钮保存
        self.wait_element_clickable_and_click(LabelLocs.el_btn_save_locator)

    def label_05(self):
        # 获取label按钮并点击
        # self.wait_element_clickable_and_click(LabelLocs.el_btn_label_locator)
        # 获取幕布
        canvas = self.wait_element_presence(LabelLocs.el_canvas_review_page_locator)
        # 打标签操作-鼠标点击
        (ActionChains(self.driver).click(canvas)
         .send_keys('z')
         .move_by_offset(0, -210).click()
         .move_by_offset(0, -100).click()
         .move_by_offset(100, 0)
         .move_by_offset(0, 100)
         .click()
         # 键盘保存操作
         .send_keys('s')
         .perform())
        # 点击SAVE按钮保存
        self.wait_element_clickable_and_click(LabelLocs.el_btn_save_locator)

    def select_ng_type(self, ng_type):
        # 获取ng type下拉框
        self.wait_element_clickable_and_click(LabelLocs.el_btn_label_locator)
        self.wait_element_clickable_and_click(LabelLocs.el_ng_type_selector_locator)
        el_ng_type_ul = self.wait_element_presence(LabelLocs.el_ng_type_ul_locator)
        el_ng_type_li_list = el_ng_type_ul.find_elements(*CommonLocs.el_li_locator)

        # 点击ng type下拉框
        for li in el_ng_type_li_list:
            # logging.info(li.get_attribute('outerHTML'))
            ng_type_span = li.find_element(*LabelLocs.el_ng_type_span_locator)
            name = ng_type_span.get_attribute('innerHTML')
            logging.debug(f'ng type: {name}')
            if name == ng_type:
                li.click()
                logging.info(f'select ng type: {name}')
                break

        self.click(LabelLocs.el_btn_cancel_locator)

    def back_to_learn_defect_page(self):
        self.wait_element_clickable_and_click(CommonLocs.el_go_back_locator)

    def select_last_image(self, number=1):
        el_images_list = self.list_images()
        logging.debug(f'len(el_images_list):{len(el_images_list)}')
        el_images_list[-number].click()

    def list_images(self):
        el_div_images = self.wait_element_presence(LabelLocs.el_div_images_locator)
        el_images_list = el_div_images.find_elements(By.XPATH, './div')
        return el_images_list

    def label_with_infer(self):
        el_images_list = self.list_images()
        count = len(el_images_list)
        for i in range(count):
            self.wait_element_clickable_and_click(ReviewLabelLocs.el_btn_label_with_infer_locator)
            self.wait_element_clickable_and_click(ReviewLabelLocs.el_btn_save_locator)
