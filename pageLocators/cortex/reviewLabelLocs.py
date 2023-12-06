from selenium.webdriver.common.by import By


class ReviewLabelLocs:
    el_div_images_list_locator = (By.XPATH, '//*[@id="file-side-bar-image-names-section"]/div[1]/div/div')
    el_btn_remove_locator = (By.XPATH, '//*[@id="remove-label-button"]')
    el_btn_delete_label_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div[10]/div/button')
    el_canvas_review_page_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/canvas')
    el_btn_save_locator = (By.XPATH, '//*[@id="save-label-button"]')
    el_btn_move_to_valid_locator = (By.XPATH, '//*[@id="move-to-validation-set-button"]')
    el_btn_move_to_train_locator = (By.XPATH, '//*[@id="move-to-train-set-button"]')
    el_btn_to_valid_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[1]/div/button[3]')
    el_btn_confirm_locator = (By.XPATH, '//*[@id="common-component-dialog-confirm"]')
    el_btn_to_train_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[1]/div/button[2]')
    el_div_existing_label_list_locator = (By.CSS_SELECTOR, '.existing-label-wrapper')
    el_dive_existing_label_selector_locator = (By.CSS_SELECTOR, '.MuiSelect-root.MuiSelect-select.MuiSelect'
                                                                '-selectMenu.MuiInputBase-input.MuiInput-input')
    el_ul_existing_label_selector_locator = (By.XPATH, '//*[@id="menu-"]/div[3]/ul')
    el_btn_label_with_infer_locator = (By.XPATH, '//*[@id="label-with-inference-results-button"]')