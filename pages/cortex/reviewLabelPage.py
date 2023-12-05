import logging

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageLocators.cortex.commonLocs import CommonLocs
from pageLocators.cortex.reviewLabelLocs import ReviewLabelLocs
from pages.cortex.labelPage import LabelPage
from utils.basePage import BasePage


class ReviewLabelPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def select_last_image(self, number=1):
        el_div_images_list = self.wait_element_presence(ReviewLabelLocs.el_div_images_list_locator)
        el_images_list = el_div_images_list.find_elements(By.XPATH, './div')
        # el_images_list = self.list_image()
        logging.debug(f'len(el_images_list):{len(el_images_list)}')
        el_images_list[-number].click()

    def remove_last_image(self, count=1):
        self.select_last_image()
        for i in range(count):
            self.click(ReviewLabelLocs.el_btn_remove_locator)
        self.click(CommonLocs.el_go_back_locator)

    def update_image(self, count):
        for i in range(count):
            self.select_last_image(i+1)
            self.click(ReviewLabelLocs.el_btn_delete_label_locator)
            self.label_05()
        self.click(CommonLocs.el_go_back_locator)

    def label_05(self):
        # 获取幕布
        canvas = self.wait_element_presence(ReviewLabelLocs.el_canvas_review_page_locator)
        # 打标签操作-鼠标点击
        (ActionChains(self.driver).click(canvas)
         .send_keys('z')
         .move_by_offset(0, -210).click()
         .move_by_offset(0, -100).click()
         .move_by_offset(100, 0).click()
         .move_by_offset(0, 100).click()
         # 键盘保存操作
         .send_keys('s')
         .perform())
        # 点击SAVE按钮保存
        self.wait_element_clickable_and_click(ReviewLabelLocs.el_btn_save_locator)

    def move_last_image_to_validation(self, count):
        self.click(ReviewLabelLocs.el_btn_to_valid_locator)
        el_images_list_init = self.list_image()

        self.click(ReviewLabelLocs.el_btn_to_train_locator)

        self.select_last_image(1)
        for i in range(count):
            self.click(ReviewLabelLocs.el_btn_move_to_valid_locator)
            self.click(ReviewLabelLocs.el_btn_confirm_locator)
            pyautogui.press('up')

        self.click(ReviewLabelLocs.el_btn_to_valid_locator)
        el_images_list_end = self.list_image()
        logging.debug(f'len(el_images_list_end) - len(el_images_list_init) = {len(el_images_list_end)} - {len(el_images_list_init)}')
        assert len(el_images_list_end) - len(el_images_list_init) == count
        self.click(CommonLocs.el_go_back_locator)

    def list_image(self):
        el_div_images_list = self.wait_element_presence(ReviewLabelLocs.el_div_images_list_locator)
        el_images_list = el_div_images_list.find_elements(By.XPATH, './div')
        return el_images_list

    def move_last_image_to_train(self, count):
        self.click(ReviewLabelLocs.el_btn_to_train_locator)
        el_images_list_init = self.list_image()

        self.click(ReviewLabelLocs.el_btn_to_valid_locator)

        self.select_last_image(1)
        for i in range(count):
            self.click(ReviewLabelLocs.el_btn_move_to_train_locator)
            self.click(ReviewLabelLocs.el_btn_confirm_locator)
            pyautogui.press('up')

        self.click(ReviewLabelLocs.el_btn_to_train_locator)
        el_images_list_end = self.list_image()

        logging.debug(
            f'len(el_images_list_end) - len(el_images_list_init) = {len(el_images_list_end)} - {len(el_images_list_init)}')
        assert len(el_images_list_end) - len(el_images_list_init) == count
        self.click(CommonLocs.el_go_back_locator)