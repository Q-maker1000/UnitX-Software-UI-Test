from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def start():
    # 启动electron应用，比如postman.exe
    options = webdriver.ChromeOptions()
    options.binary_location = "/home/unitx/cortex/cortex_src/ui/release/CorteX.AppImage"
    driver = webdriver.remote.webdriver.WebDriver(
        command_executor='http://localhost:9515',
        options=options
    )
    return driver
