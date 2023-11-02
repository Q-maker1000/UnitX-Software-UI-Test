import time

from selenium.webdriver import ActionChains

from pageLocators.commonLocs import CommonLocs
from pageLocators.labelLocs import LabelLocs
from utils.basePage import BasePage


class LabelPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def labeling(self, image_num=1):
        # 获取图片列表
        image_list = self.location_elements(LabelLocs.el_image_list_locator)
        # 判断照片是否存在
        total = len(image_list)
        if total != 0:
            # 若存在,循环以下操作(打标操作)
            for i in range(image_num):
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
                self.screen_shot("get ng label")
                self.wait_element_clickable_and_click(LabelLocs.el_btn_save_locator)
            # 返回主页
            self.wait_element_clickable_and_click(CommonLocs.el_go_back_locator)
        # 若不存在,提示请导入新照片
        else:
            print("no image in label, please import image!")

    # def labeling(self):

    # def select_ng_type(self):
        # 获取ng type下拉框

        # 点击ng type下拉框

        # 获取ng type列表元素

        # 循环遍历获取其中一个元素

        # 点击该ng type

if __name__ == '__main__':
    for i in range(1):
        print(i)