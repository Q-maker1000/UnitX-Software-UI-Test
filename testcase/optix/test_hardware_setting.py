import datetime

from pages.optix.hardwareSettingPage import HardwareSettingPage
from utils import start_software
from utils.basePage import BasePage

ts = datetime.date.today().strftime("%Y-%m-%d")
PREFIX = "ui_test_v3110_001_"
SEQUENCE_LIST = []
CC_LIST = []


class TestDefectNetwork:

    def test_version(self):
        driver = start_software.start("optix")
        HardwareSettingPage(driver).check_version("v3.11.0")
        BasePage(driver).screen_shot("check_version")
        driver.quit()

    def test_hardware_config(self):
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        BasePage(driver).screen_shot("config_hardware_setting")
        driver.quit()

    def test_create_sequence(self):
        sequence_name = PREFIX + ts
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        for n in range(2):
            HardwareSettingPage(driver).create_sequence(sequence_name + str(n))
            SEQUENCE_LIST.append(sequence_name + str(n))
        driver.quit()

    def test_create_cc(self):
        cc_name = PREFIX + ts
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        HardwareSettingPage(driver).create_capture(cc_name, 3)
        driver.quit()

    def test_add_1cc_to_sequence(self):
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()

        HardwareSettingPage(driver).add_cc_to_sequence(SEQUENCE_LIST[0], 0, False)
        # HardwareSettingPage(driver).add_cc_to_sequence('ui_test_v3110_03_2023-11-090', 0, False)

        driver.quit()

    def test_add_multi_cc_to_sequence(self):
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        HardwareSettingPage(driver).add_cc_to_sequence(SEQUENCE_LIST[1], 1, True)
        print("SEQUENCE_LIST:"+SEQUENCE_LIST[1])
        driver.quit()

    def test_save_image_without_compute(self):
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        HardwareSettingPage(driver).save_image(SEQUENCE_LIST[0], 0, 3)
        driver.quit()

    def test_save_image_with_compute(self):
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        HardwareSettingPage(driver).save_image(SEQUENCE_LIST[1], 0, 3, True)
        driver.quit()

    def test_upload_to_controller(self):
        # cc_name1 = "ui_test_09"
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        HardwareSettingPage(driver).upload_to_controller(SEQUENCE_LIST[0], 9)
        driver.quit()