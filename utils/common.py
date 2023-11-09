from selenium.webdriver.common.by import By

from utils import start_software


def login():
    driver = start_software.start()
    driver.implicitly_wait(5)
    # 获取元素
    ipt_username = driver.find_element(By.ID, 'username-input-field')
    ipt_password = driver.find_element(By.ID, 'password-input-field')
    btn_login = driver.find_element(By.ID, 'login-button')
    # 输入帐号密码并登录
    ipt_username.send_keys('admin')
    ipt_password.send_keys('1234')
    btn_login.click()
    return driver

if __name__ == '__main__':
    driver = start_software.start("optix")