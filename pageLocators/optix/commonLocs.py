from selenium.webdriver.common.by import By


class CommonLocs:
    el_nav_locator = (By.XPATH, '//*[@id="root"]/div/header/div/button[1]')
    el_version_locator = (By.XPATH, '/html/body/div[2]/div[3]/div[2]')

    el_path_locator = (By.TAG_NAME, 'path')
    el_span_locator = (By.TAG_NAME, 'span')
    el_li_locator = (By.TAG_NAME, 'li')
    el_em_locator = (By.TAG_NAME, 'em')
