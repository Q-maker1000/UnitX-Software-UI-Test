from selenium.webdriver.common.by import By


class CommonLocs:
    # 返回按钮
    el_go_back_locator = (By.XPATH, '//*[@id="go-back-button"]')
    # 输入框
    el_input_locator = (By.TAG_NAME, 'input')
    el_btn_locator = (By.TAG_NAME, 'button')
    el_li_locator = (By.TAG_NAME, 'li')
    el_span_locator = (By.TAG_NAME, 'span')
    # 获取div元素
    el_div_locator = (By.TAG_NAME, 'div')
    # 获取i元素
    el_i_locator = (By.TAG_NAME, 'i')
    # 删除network确认按钮
    el_btn_confirm_locator = (By.XPATH, '//*[@id="common-component-dialog-confirm"]')

    el_btn_nav_locator = (By.XPATH, '/html/body/div/div/header/div/button[1]')
    el_div_version_locator = (By.XPATH, '/html/body/div[2]/div[3]/div/div')

    el_cortex_input_locator = (By.CSS_SELECTOR, '.MuiInputBase-input.MuiInput-input')