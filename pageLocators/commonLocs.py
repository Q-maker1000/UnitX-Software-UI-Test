from selenium.webdriver.common.by import By


class CommonLocs:
    # 返回按钮
    el_go_back_locator = (By.XPATH, '//*[@id="go-back-button"]')
    # 输入框
    el_input_locator = (By.TAG_NAME, 'input')
    # 获取div元素
    el_div_locator = (By.TAG_NAME, 'div')
    # 获取i元素
    el_i_locator = (By.TAG_NAME, 'i')
    # 删除network确认按钮
    el_btn_confirm_locator = (By.XPATH, '//*[@id="common-component-dialog-confirm"]')