from selenium.webdriver.common.by import By

from pageLocators.cortex.ArchiveLocs import ArchiveLocs
from pageLocators.cortex.commonLocs import CommonLocs
from pages.cortex.defectLearnPage_network import DefectLearnPage_Network
from utils.basePage import BasePage


class HeaderRightBTN:
    DELETE = 0
    RESTORE_NETWORK = 1


class ArchivePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.defectLearnPage_Network = DefectLearnPage_Network(driver)

    def select_right_network_btn(self, name, index):
        el_network = self.defectLearnPage_Network.find_network_by_name(name)
        el_network_header = el_network.find_element(*ArchiveLocs.el_div_network_header_locator)
        el_div_network_header_right_btn = el_network_header.find_element(*ArchiveLocs.el_div_network_header_right_btn_locator)
        el_btn_network_header_right_btn_list = el_div_network_header_right_btn.find_elements(*CommonLocs.el_btn_locator)
        el_btn = el_btn_network_header_right_btn_list[index]
        el_btn.click()






