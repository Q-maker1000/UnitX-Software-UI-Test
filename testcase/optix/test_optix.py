import datetime
import logging
import time

import pytest

from pages.optix.hardwareSettingPage import HardwareSettingPage
from pages.optix.hardwareSettingPage_v2 import HardwareSettingPage_v2, PatternSelect, ConfigType
from utils import start_software
from utils.basePage import BasePage

ts = datetime.date.today().strftime("%Y-%m-%d")
SEQUENCE_LIST = ['ui-test-seq-01', 'ui-test-seq-02', 'ui-test-seq-03']
CC_LIST = ['ui-test-c1', 'ui-test-c2', 'ui-test-c3', 'ui-test-c4', 'ui-test-c5', 'ui-test-c6']
path = '/home/unitx/Pictures/ui-test'
# SEQUENCE_LIST = []

driver = start_software.start("optix")
hardwareSettingPage = HardwareSettingPage(driver)
hardwareSettingPage2 = HardwareSettingPage_v2(driver)


class TestDefectNetwork:

    def teardown_class(self):
        time.sleep(15)
        driver.quit()

    def test_version(self):
        hardwareSettingPage.check_version("v4.0.6")

    def test_hardware_config(self):
        hardwareSettingPage.config_hardware_setting()

    def test_create_sequence(self):
        # hardwareSettingPage.config_hardware_setting()
        for n in range(3):
            hardwareSettingPage2.create_sequence(SEQUENCE_LIST[n])

    def test_create_cc(self):
        # hardwareSettingPage.config_hardware_setting()
        for _ in CC_LIST:
            hardwareSettingPage2.create_cc(_)
            hardwareSettingPage2.set_cc_exposure(_, 14)
            hardwareSettingPage2.set_cc_pattern_v4(_, PatternSelect.OUTERMOST_BY_RING)

    def test_add_to_sequence(self):
        # hardwareSettingPage.config_hardware_setting()

        for i in range(6):
            hardwareSettingPage2.add_cc_to_seq(CC_LIST[i], SEQUENCE_LIST[int(i/2)])

    def test_save_image_with_compute(self):
        # hardwareSettingPage.config_hardware_setting()
        for _ in SEQUENCE_LIST:
            hardwareSettingPage2.save_image_in_seq_page(_, path, 5)

    def test_save_image_without_compute(self):
        # hardwareSettingPage.config_hardware_setting()
        for _ in SEQUENCE_LIST:
            hardwareSettingPage2.save_image_in_seq_page(_, path, True, True, 5)

    def test_upload_to_controller(self):
        # hardwareSettingPage.config_hardware_setting()
        for index, item in enumerate(SEQUENCE_LIST):
            hardwareSettingPage2.upload_to_controller(index, item)