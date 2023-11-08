from pages.optix.hardwareSettingPage import HardwareSettingPage
from utils import start_software
from utils.basePage import BasePage


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
        sequence_name = "ui_test_01"
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        HardwareSettingPage(driver).create_sequence(sequence_name)
        BasePage(driver).screen_shot("create_sequence")
        driver.quit()

    def test_create_cc(self):
        cc_name = "ui_test_02"
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        HardwareSettingPage(driver).create_capture(cc_name)
        BasePage(driver).screen_shot("create_capture")
        driver.quit()

    def test_add_1cc_to_sequence(self):
        driver = start_software.start("optix")
        HardwareSettingPage(driver).config_hardware_setting()
        BasePage(driver).screen_shot("add_cc_to_sequence1")
        HardwareSettingPage(driver).add_cc_to_sequence("", 1, True)
        BasePage(driver).screen_shot("add_cc_to_sequence2")
        # driver.quit()
