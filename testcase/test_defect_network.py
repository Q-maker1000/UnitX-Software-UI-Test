import logging
import time
from datetime import datetime

from config.global_params import Cookie
from pages.defectLearnPage_network import DefectLearnPage_Network
from pages.defectLearnPage_ngType import DefectLearnPage_NGTYPE
from pages.labelPage import LabelPage
from utils.common import login


class TestDefectNetwork:

    def test_create_ng_type(self):
        driver = login()
        ts = datetime.now().strftime("%s")
        type_name_pre = "test_ui"
        DefectLearnPage_NGTYPE(driver).create_ng_type(type_name_pre + ts, 1)
        driver.quit()

    def test_update_ng_type(self):
        driver = login()
        ts = datetime.now().strftime("%s")
        type_name_pre_old = "test_ui_old"
        ng_type_list = DefectLearnPage_NGTYPE(driver).create_ng_type(type_name_pre_old + ts, 2)
        for ng_type in ng_type_list:
            DefectLearnPage_NGTYPE(driver).edit_ng_type(ng_type + "-new", ng_type)

    def test_delete_ng_type(self):
        driver = login()
        ts = datetime.now().strftime("%s")
        type_name_pre_old = "test_ui_del"
        ng_type_list = DefectLearnPage_NGTYPE(driver).create_ng_type(type_name_pre_old + ts, 2)
        for ng_type in ng_type_list:
            DefectLearnPage_NGTYPE(driver).delete_ng_type(ng_type)

    def test_create_network_and_train(self):
        driver = login()
        ts = datetime.now().strftime("%Y-%m-%d-%s")
        network_n = 'z_test-ui_' + ts
        DefectLearnPage_Network(driver).create_network(network_n)
        cookie = Cookie
        path = "/home/unitx/图片/20230912-c2"
        res = DefectLearnPage_Network(driver).import_image(path, network_n, cookie)
        print(res)
        DefectLearnPage_Network(driver).go_label_page(network_n)
        DefectLearnPage_Network(driver).pre_process(0, 2448, 0, 2048, 2448, 2048)
        LabelPage(driver).labeling(5)
        network = DefectLearnPage_Network(driver).find_network_by_name(network_n)
        DefectLearnPage_Network.wait_training(network)

    def test_log(self):
        logger = logging.getLogger("TestLog")
        logger.debug("This is a debug message.")
        logger.info("This is a info message.")
        logger.warning("This is a warning message.")
        logger.error("This is a error message.")
        logger.critical("This is a critical message.")
