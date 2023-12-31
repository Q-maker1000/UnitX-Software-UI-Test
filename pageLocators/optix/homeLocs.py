from selenium.webdriver.common.by import By


class HomeLocs:
    el_add_sequence_btn_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/button')
    el_sequence_name_input_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/input')
    el_create_sequence_btn_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[4]/div/div/button')
    el_add_exist_cc_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[3]/div/div[2]')
    el_create_cc_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[3]/div/div[3]')

    el_cc_name_input_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[3]/div/div/input')
    el_create_cc_btn_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[6]/div/div/button')
    el_select_light_form_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[5]/div[2]/div')

    el_pattern_edit_mode_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[5]/div[1]/div/div')
    el_pattern_ring_mode_locator = (By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')
    el_pattern_normal_mode_locator = (By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]')
    el_pattern_path_list_locator = (By.CSS_SELECTOR, '.rv-xy-plot__series.rv-xy-plot__series--arc-path')

    el_exposure_input_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[1]/input')
    el_exposure_selector_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[4]/div/div/div[1]/span')

    el_sequence_selector_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div')
    el_sequence_list_locator = (By.XPATH, '/html/body/div[4]/div[3]')
    el_sequence_update_btn_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[4]/div/div[1]/button')
    el_sequence_back_btn_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/button')

    el_cc_exist_list_locator = (By.XPATH, '/html/body/div[4]/div[3]')
    el_cc_new_btn_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/button')
    el_cc_update_btn_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[7]/div/div[1]/button')
    el_cc_list_locator = (By.CSS_SELECTOR, '.MuiListItemText-root.MuiListItemText-dense')
    el_cc_selector_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/div/div')
    el_cc_sequence_selected_li_locator = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.Mui'
                                                           '-selected.MuiMenuItem-gutters.MuiListItem-gutters'
                                                           '.MuiListItem-button.Mui-selected')

    el_selector_locator = (By.CSS_SELECTOR, '.MuiSelect-root.MuiSelect-select.MuiSelect-selectMenu.MuiSelect-outlined'
                                            '.MuiInputBase-input.MuiOutlinedInput-input')
    el_selector_li_list_locator = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root'
                                                    '.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button')
    el_btn_list_locator = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton'
                                              '-containedPrimary.MuiButton-fullWidth')

    el_select_folder_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[5]/div[2]/div/div[1]')
    el_save_image_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[5]/div[3]/button')
    el_save_in_max_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[5]/div[1]/label[1]')
    el_save_in_min_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[5]/div[1]/label[2]')

    el_io_input_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[6]/div/div[1]/input')
    el_io_upload_btn_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[6]/div/div[2]/button')
    el_confirm_btn_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/button[1]')

    el_tip_locator = (By.CSS_SELECTOR, '.MuiSnackbar-root.MuiSnackbar-anchorOriginTopCenter')

    el_ul_selector_list_locator = (By.XPATH, '//*[@id="menu-"]/div[3]/ul')
    el_div_cc_list_in_seq_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[3]/div/div[1]')

    el_div_choose_saving_image_folder_path = (By.CSS_SELECTOR, '.MuiBox-root.jss32')
