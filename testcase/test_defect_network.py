import logging
import time
from datetime import datetime

import pyautogui

from config.global_params import CorteXParams
from pages.cortex.defectLearnPage_network import DefectLearnPage_Network, LeftBtn, TopBtn
from pages.cortex.defectLearnPage_ngType import DefectLearnPage_NGTYPE
from pages.cortex.labelPage import LabelPage
from pages.cortex.reviewLabelPage import ReviewLabelPage
from utils.common import login

driver = login()

name_pre = "ui_test_"
ng_type_name_list = []
network_name_list = []

defectLearnPage_NGTYPE = DefectLearnPage_NGTYPE(driver)
defectLearnPage_Network = DefectLearnPage_Network(driver)
labelPage = LabelPage(driver)
reviewLabelPage = ReviewLabelPage(driver)

network_name = 'ui_test_2023-12-01_10-58-56-3156'


def check_review_label(name):
    defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.REVIEW_LABELS_INDEX)
    time.sleep(1)
    defectLearnPage_Network.screen_shot(f'{name} review label 1')
    reviewLabelPage.select_last_image()
    time.sleep(1)
    defectLearnPage_Network.screen_shot(f'{name} review label 2')
    labelPage.back_to_learn_defect_page()


def check_label_infer(name):
    defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.LABEL_INDEX)
    time.sleep(1)
    defectLearnPage_Network.screen_shot(f'{name} label 1')
    labelPage.select_last_image()
    time.sleep(1)
    defectLearnPage_Network.screen_shot(f'{name} label 2')
    labelPage.back_to_learn_defect_page()


class TestDefectNetwork:

    def test_check_version(self):
        defectLearnPage_NGTYPE.check_version(CorteXParams.VERSION)

    def test_create_network(self):
        network_name = name_pre + datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-2]
        defectLearnPage_Network.create_network(network_name)
        network_name_list.append(network_name)

    def test_create_ng_type(self):
        for i in range(4):
            ng_type_name = name_pre + datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-2]
            defectLearnPage_NGTYPE.create_ng_type(ng_type_name)
            ng_type_name_list.append(ng_type_name)

    def test_import_image_to_label(self):
        # network_name = network_name_list[0]
        defectLearnPage_Network.import_images(CorteXParams.IMAGE_PATH_1, network_name)
        time.sleep(1)
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.LABEL_INDEX)
        defectLearnPage_Network.pre_process(0, 2448, 0, 2048, 960, 803)
        labelPage.labeling(5)

    def test_train_from_scratch_1(self):
        check_review_label('test_train_from_scratch_1')
        defectLearnPage_Network.select_left_network_btn(network_name_list[0], LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_1(self):
        # network_name = network_name_list[0]
        defectLearnPage_Network.is_train_end(network_name)
        check_label_infer('test_check_if_reasonable_1')

    def test_add_label_with_same_ng_type_2(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.LABEL_INDEX)
        labelPage.labeling(5, 'label_02')
        check_review_label('test_add_label_with_same_ng_type_2')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_INCREMENTAL_INDEX)

    def test_check_if_reasonable_2(self):
        network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_label_infer('test_check_if_reasonable_2')

    def test_add_additional_ng_type_3(self):
        # network_name = network_name_list[0]
        # ng_type_name = 'NG:' + ng_type_name_list[1]
        ng_type_name = 'NG:ui_test_2023-12-01_10-58-58-7519'

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.LABEL_INDEX)
        labelPage.select_ng_type(ng_type_name)
        labelPage.labeling(5, 'label_03')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_INCREMENTAL_INDEX)

        pyautogui.press('enter')

    def test_train_from_scratch_add_ng_type_3(self):
        network_name = network_name_list[0]

        check_review_label('test_train_from_scratch_add_ng_type_3')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_3(self):
        network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_label_infer('test_check_if_reasonable_3')

    def test_clone_network(self):
        network_name = network_name_list[0]
        defectLearnPage_Network.clone_network(network_name)
        driver.quit()

    def test_full_resolution_and_train_from_scratch(self):
        network_name = network_name_list[0]

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.LABEL_INDEX)
        defectLearnPage_Network.pre_process(0, 2448, 0, 2048, 2448, 2048)
        labelPage.back_to_learn_defect_page()
        check_review_label('test_full_resolution_and_train_from_scratch')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_4(self):
        network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_review_label('test_check_if_reasonable_4')

    def test_restore_original_resolution_and_train_from_scratch(self):
        network_name = network_name_list[0]

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.LABEL_INDEX)
        defectLearnPage_Network.pre_process(0, 2448, 0, 2048, 960, 803)
        labelPage.back_to_learn_defect_page()
        check_review_label('test_restore_original_resolution_and_train_from_scratch')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_5(self):
        network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_review_label('test_check_if_reasonable_5')

    def test_restore_original_resolution_and_add_new_ng_type(self):
        network_name = network_name_list[0]
        ng_type_name = 'NG:' + ng_type_name_list[2]
        # ng_type_name = 'NG:ui_test_2023-12-01_13-06-27-5519'

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.LABEL_INDEX)
        labelPage.select_ng_type(ng_type_name)
        labelPage.labeling(5, 'label_04')
        check_review_label('test_restore_original_resolution_and_add_new_ng_type')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_6(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_review_label('test_check_if_reasonable_6')

    def test_remove_a_ng_type_all_images(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.REVIEW_LABELS_INDEX)
        reviewLabelPage.remove_last_image(5)
        check_review_label('test_remove_a_ng_type_all_images')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_7(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_review_label('test_check_if_reasonable_7')

    def test_remove_image_from_train_set(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.REVIEW_LABELS_INDEX)
        reviewLabelPage.remove_last_image()
        check_review_label('test_remove_image_from_train_set')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_8(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_review_label('test_check_if_reasonable_8')

    def test_change_image_label(self):
        # network_name = network_name_list[0]
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.REVIEW_LABELS_INDEX)
        reviewLabelPage.update_image(3)
        check_review_label('test_change_image_label')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_9(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_review_label('test_check_if_reasonable_9')

    def test_move_label_to_validation(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.REVIEW_LABELS_INDEX)
        reviewLabelPage.move_last_image_to_validation(2)
        check_review_label('test_move_label_to_validation')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

    def test_check_if_reasonable_10(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_review_label('test_check_if_reasonable_10')

    def test_move_label_to_train_and_train_increment(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.REVIEW_LABELS_INDEX)
        reviewLabelPage.move_last_image_to_train(2)
        check_review_label('test_move_label_to_train_and_train_increment')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_INCREMENTAL_INDEX)

    def test_check_if_reasonable_11(self):
        # network_name = network_name_list[0]

        defectLearnPage_Network.is_train_end(network_name)
        check_review_label('test_check_if_reasonable_11')

    def test_move_one_ng_type_all_image_to_valid(self):
        # network_name = network_name_list[1]

        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.REVIEW_LABELS_INDEX)
        reviewLabelPage.move_last_image_to_validation(5)
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_INCREMENTAL_INDEX)

    def test_check_if_block_12(self):
        time.sleep(1)
        defectLearnPage_Network.screen_shot('test_check_if_block_12')
        time.sleep(0.5)
        pyautogui.press('enter')

    def test_model_version_infer_and_valid_result(self):
        check_review_label('test_model_version_infer_and_valid_result')
        check_label_infer('test_model_version_infer_and_valid_result')

        defectLearnPage_Network.valid_result(network_name)
        time.sleep(1)
        defectLearnPage_Network.screen_shot('valid result')
        labelPage.back_to_learn_defect_page()

    def test_model_version_and_train_incremental(self):
        defectLearnPage_Network.select_last_model_version(network_name)
        check_review_label('test_model_version_and_train_incremental')
        defectLearnPage_Network.select_left_network_btn(network_name, LeftBtn.TRAIN_INCREMENTAL_INDEX)

    def test_check_if_reasonable_13(self):
        defectLearnPage_Network.is_train_end(network_name)
        check_label_infer('test_check_if_reasonable_13')

    def test_delete_ng_type(self):
        # ng_name = ng_type_name_list[0]
        ng_name = 'ui_test_2023-12-01_15-07-29-5100'
        defectLearnPage_NGTYPE.delete_ng_type(ng_name)

    # def test_check_ng_type_if_present(self):
    #
    # def test_train_after_delete_ng_type(self):
    #
    # def test_check_if_reasonable_14(self):
    #     defectLearnPage_Network.is_train_end(network_name)
    #     check_label_infer('test_check_if_reasonable_14')

    def test_some(self):
        network = 'test-valid'
        # defectLearnPage_Network.select_left_network_btn(network, LeftBtn.REVIEW_LABELS_INDEX)
        # reviewLabelPage.select_ng_type_to_label()

        # defectLearnPage_Network.select_left_network_btn(network, LeftBtn.LABEL_INDEX)
        # labelPage.label_with_infer()

        defectLearnPage_Network.select_left_network_btn(network, LeftBtn.REVIEW_LABELS_INDEX)
        reviewLabelPage.move_last_image_to_validation(10)
        defectLearnPage_Network.select_left_network_btn(network, LeftBtn.TRAIN_FROM_SCRATCH_INDEX)

        # defectLearnPage_Network.select_left_network_btn(network, LeftBtn.LABEL_INDEX)
        # defectLearnPage_Network.pre_process(0, 4128, 0, 3008, 1600, 1165)
        # labelPage.labeling(75, 'label_02')

