import os
import subprocess

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import socket


cortex_path = "/home/unitx/cortex/cortex_src/ui/release/CorteX.AppImage"
optix_path = "/home/unitx/optix/optix_src/ui/release/OptiX.AppImage"


def start(app_path="cortex"):
    # 启动electron应用，比如CorteX
    options = webdriver.ChromeOptions()
    if app_path == "cortex":
        options.binary_location = cortex_path
    elif app_path == "optix":
        options.binary_location = optix_path
    else:
        print("choose a correctly app_path")
    driver = webdriver.remote.webdriver.WebDriver(
        command_executor='http://localhost:9515',
        options=options
    )
    return driver