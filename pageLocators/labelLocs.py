from selenium.webdriver.common.by import By


class LabelLocs:
    # 图片列表元素
    el_image_list_locator = (By.XPATH, '//*[@id="file-side-bar-image-names-section"]/div[1]/div/div')
    # 幕布
    el_canvas_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[3]/div[2]/div/canvas')
    # label按钮
    el_btn_label_locator = (By.XPATH, '//*[@id="toggle-labeler-button"]')
    # SAVE按钮
    el_btn_save_locator = (By.XPATH, '//*[@id="save-label-button"]')
    # 预处理按钮
    el_btn_pre_process_locator = (By.XPATH, '//*[@id="preprocess-toolbar-icon-button"]')
    # 预处理表单
    el_form_pre_process_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[3]/form')
    # 预处理保存按钮
    el_btn_save_pre_process_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[3]/form/div[2]/button[1]')
