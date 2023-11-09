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

    el_exposure_input_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[1]/input')
    el_exposure_selector_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[4]/div/div/div[1]/span')

    el_sequence_selector_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div')
    el_sequence_list_locator = (By.XPATH, '/html/body/div[4]/div[3]')
    el_sequence_update_btn_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[4]/div/div[1]/button')

    el_cc_exist_list_locator = (By.XPATH, '/html/body/div[4]/div[3]')
    el_cc_list_locator = (By.CSS_SELECTOR, '.MuiListItemText-root.MuiListItemText-dense')
    el_cc_selector_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/div/div')
    el_cc_sequence_selected_li_locator = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.Mui'
                                                           '-selected.MuiMenuItem-gutters.MuiListItem-gutters'
                                                           '.MuiListItem-button.Mui-selected')

    el_select_folder_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[5]/div[2]/div/div[1]')
    el_save_image_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[5]/div[3]/button')
    el_save_in_max_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[5]/div[1]/label[1]')
    el_save_in_min_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[5]/div[1]/label[2]')
