import os

cortex_app_path = '/home/unitx/cortex/cortex_src/ui/release/'
chromedriver_path = '/home/unitx/下载/chromedriver_linux64/'
start_cortex_command = './CorteX.AppImage --remote-debugging-port=9222'
start_optix_command = './OptiX.AppImage --remote-debugging-port=9222'
start_chromedriver_command = './chromedriver'


def start_app_debug():
    try:
        os.chdir(cortex_app_path)
        os.system(start_cortex_command)
        print("已开启调试模式...")
    except Exception as e:
        print("启动xcortex失败！并抛出异常：\n" + str(e))


def start_chromedriver():
    try:
        os.chdir(chromedriver_path)
        os.system(start_chromedriver_command)
    except Exception as e:
        print("启动chromedriver失败！并抛出异常：\n" + str(e))


if __name__ == '__main__':
    start_chromedriver()
    start_app_debug()