from selenium.webdriver.common.by import By


class LabelLocs:
    # 图片列表元素
    el_image_list_locator = (By.XPATH, '//*[@id="file-side-bar-image-names-section"]/div[1]/div/div')
    # 幕布
    el_canvas_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[3]/div[2]/div/canvas')
    el_canvas_trained_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div/canvas')
    # label按钮
    el_btn_label_locator = (By.XPATH, '//*[@id="toggle-labeler-button"]')
    # SAVE按钮
    el_btn_save_locator = (By.XPATH, '//*[@id="save-label-button"]')
    # 预处理按钮
    el_btn_pre_process_locator = (By.XPATH, '//*[@id="preprocess-toolbar-icon-button"]')
    # 预处理表单
    el_form_pre_process_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[3]/form')
    # 预处理保存按钮
    el_btn_save_pre_process_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[3]/form/div['
                                                 '2]/button[1]')

    el_ng_type_selector_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/div')

    el_ng_type_ul_locator = (By.XPATH, '/html/body/div[4]/div[3]/ul')

    el_ng_type_span_locator = (By.CSS_SELECTOR, '.MuiTypography-root.MuiListItemText-primary.MuiTypography-body1'
                                                '.MuiTypography-displayBlock')
    el_btn_cancel_locator = (By.XPATH, '//*[@id="cancel-label-button"]')
    el_div_images_locator = (By.XPATH, '//*[@id="file-side-bar-image-names-section"]/div[1]/div/div')

    el_btn_remove_image_locator = (By.XPATH, '//*[@id="discard-image-button"]')

    el_img_image_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div/img[1]')
