import io
import logging

import cv2
import pyautogui
import pytesseract

from PIL import Image
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

    def label_with_infer(self, count=1):
        el_images_list = self.list_images()
        if count == 0:
            count = len(el_images_list)
        for i in range(count):
            self.wait_element_clickable_and_click(ReviewLabelLocs.el_btn_label_with_infer_locator)
            self.wait_element_clickable_and_click(ReviewLabelLocs.el_btn_save_locator)
        self.back_to_learn_defect_page()

    def remove_last_image(self, count=1):
        for i in range(count):
            self.wait_element_clickable_and_click(LabelLocs.el_btn_remove_image_locator)
        self.back_to_learn_defect_page()

    def remove_oldest_image(self, count=1):
        el_images_list = self.list_images()
        el_images_list[-1].click()
        for i in range(count):
            self.wait_element_clickable_and_click(LabelLocs.el_btn_remove_image_locator)
        self.back_to_learn_defect_page()

    def label_with_dl(self):
        # 获取label按钮并点击
        self.wait_element_clickable_and_click(LabelLocs.el_btn_label_locator)
        # 定位包含照片的元素
        el_image = self.location_element(LabelLocs.el_img_image_locator)

        # 截取包含字母的照片区域
        location = el_image.location
        size = el_image.size

        # 截取图像
        screenshot = self.driver.save_screenshot("screenshot.png")
        # screenshot = self.driver.get_screenshot_as_png()
        # image_on_app = Image.open(io.BytesIO(screenshot))
        # region = image_on_app.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
        # # 将截图保存到本地（可选）
        # region.save("screenshot.png")

        # 计算图像在页面上的坐标
        img_x = location['x']
        img_y = location['y']

        screenshot = cv2.imread("screenshot.png")
        letter_roi = screenshot[img_y:img_y + size['height'], img_x:img_x + size['width']]
        gray_letter = cv2.cvtColor(letter_roi, cv2.COLOR_BGR2GRAY)
        # 获取轮廓
        _, binary_image = cv2.threshold(gray_letter, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours, _)

        # 创建ActionChains对象
        actions = ActionChains(self.driver)

        # 在每个轮廓上模拟鼠标点击
        for contour in contours:
            for point in contour:
                x, y = point[0]
                # 在图像内的坐标位置模拟点击
                actions.move_to_element_with_offset(el_image, img_x + x, img_y + y)
                actions.click()

        # 执行鼠标点击操作
        actions.perform()

    def get_pygui_loc(self):
        x, y = pyautogui.position()
        print(x, y)

    def label_3row_3col(self):
        # 获取label按钮并点击
        self.wait_element_clickable_and_click(LabelLocs.el_btn_label_locator)
        # 获取幕布
        canvas = self.wait_element_presence(LabelLocs.el_img_image_locator)# 获取label按钮并点击
        logging.info(f'get canvas')
        # 打标签操作-鼠标点击
        (ActionChains(self.driver).click(canvas)
         .send_keys('z')
         .move_by_offset(-67, 85).click()
         .move_by_offset(185, 2).click()
         .move_by_offset(2,  -189).click()
         .move_by_offset(-184, -1).click()
         # 键盘保存操作
         .send_keys('s')
         .perform())
        logging.info(f'finish 03 label in a image')
        # 点击SAVE按钮保存
        self.wait_element_clickable_and_click(LabelLocs.el_btn_save_locator)