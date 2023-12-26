from selenium.webdriver.common.by import By


class HardwareSettingLocs:
    # /html/body/div/div/div/div[2]/div/button[2]
    el_OK_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/button[2]')
    el_refresh_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div/button[1]')

    el_div_selector_locator = (By.CSS_SELECTOR, '.MuiSelect-root.MuiSelect-select.MuiSelect-selectMenu.MuiInputBase'
                                                '-input.MuiInput-input')
    el_div_hardware_setting_locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div')
    el_li_hardware_setting_item_locator = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root'
                                                            '.Mui-selected.MuiMenuItem-gutters.MuiListItem-gutters'
                                                            '.MuiListItem-button.Mui-selected')
