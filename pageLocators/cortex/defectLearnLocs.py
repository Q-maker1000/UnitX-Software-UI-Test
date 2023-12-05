from selenium.webdriver.common.by import By


class DefectLearnLocs:

    # ===============================缺陷管理元素===============================
    # ng type管理按钮
    el_btn_ng_type_manager_locator = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/button[1]')
    # 创建ng type按钮 /html/body/div[2]/div[3]/div/div/button
    el_btn_create_ng_type_locator = (By.XPATH, '/html/body/div[2]/div[3]/div/div/button')
    # ng type输入框
    el_ipt_ng_type_name_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/div/form/div/div[2]/div/input')
    # 新建ng type确认按钮
    el_btn_confirm_ng_type_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/div/form/button')
    # 获取ng type元素
    el_row_ng_type_locator = (By.CSS_SELECTOR, '.ng-row')
    # 获取ng type删除按钮
    el_btn_delete_ng_type_locator = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[2]/button[2]')

    # ===============================模型相关元素===============================
    # 新建network按钮
    el_btn_create_network_locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/button[3]')
    # network名称输入框
    el_ipt_network_name_locator = (By.XPATH, '/html/body/div[2]/div[3]/div/div/form/div/div[2]/div/input')
    # 新建network设置按钮
    el_btn_create_network_config_locator = (By.XPATH, '/html/body/div[2]/div[3]/div/div/form/button')
    # network元素列表
    el_network_list_locator = (By.CSS_SELECTOR, '.MuiPaper-root.MuiCard-root.margin-top2')
    # network头部
    el_network_header_locator = (By.CSS_SELECTOR, '.flex-row.space-between')
    # network底部
    el_network_bottom_locator = (By.CSS_SELECTOR, '.margin-top2')
    # network信息
    el_network_information_locator = (By.CSS_SELECTOR, '.right-status')
    # network bottom 行元素
    el_row_network_bottom_locator = (By.CSS_SELECTOR, '.flex-row')
    el_btn_network_config_btn_list_locator = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiButton-root.MuiButton-text')
    el_left_btn_list_locator = (By.CSS_SELECTOR, '.uiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-fullWidth')
    el_input_clone_network_locator = (By.XPATH, '/html/body/div[2]/div[3]/div/div/form/div/div[2]/div/input')
    el_btn_clone_network_locator = (By.XPATH, '//*[@id="Clone-form-accept"]')
    el_div_model_version_selector_locator = (By.XPATH, './div[1]/div[1]/div/div[2]/div')
    el_span_model_version_locator = (By.XPATH, './span')

    # # ===============================通用元素===============================
    # 删除network确认按钮
    el_btn_confirm_locator = (By.XPATH, '//*[@id="common-component-dialog-confirm"]')
    # 获取标签为h2的元素
    el_h2_locator = (By.TAG_NAME, 'h2')
    # 获取button元素
    el_button_locator = (By.TAG_NAME, 'button')
    # 获取div元素
    el_div_locator = (By.TAG_NAME, 'div')
    # 获取span元素
    el_span_locator = (By.TAG_NAME, 'span')