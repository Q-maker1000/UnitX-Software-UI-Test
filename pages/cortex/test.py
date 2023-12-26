from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import cv2
import pytesseract

# 初始化Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://your_website.com")

# 定位图像元素
img_element = driver.find_element_by_css_selector("your_img_selector")

# 获取图像在页面上的位置信息
img_location = img_element.location
img_size = img_element.size

# 截取图像
screenshot = driver.save_screenshot("screenshot.png")

# 计算图像在页面上的坐标
img_x = img_location['x']
img_y = img_location['y']

# 读取截图
screenshot = cv2.imread("screenshot.png")

# 截取图像中的字母区域（这里假设字母区域的位置已知）
letter_roi = screenshot[img_y:img_y + img_size['height'], img_x:img_x + img_size['width']]

# 将字母区域转换为灰度图像
gray_letter = cv2.cvtColor(letter_roi, cv2.COLOR_BGR2GRAY)

# 使用Tesseract进行字符识别
text = pytesseract.image_to_string(gray_letter)

# 获取轮廓
_, binary_image = cv2.threshold(gray_letter, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 创建ActionChains对象
actions = ActionChains(driver)

# 在每个轮廓上模拟鼠标点击
for contour in contours:
    for point in contour:
        x, y = point[0]
        # 在图像内的坐标位置模拟点击
        actions.move_to_element_with_offset(img_element, img_x + x, img_y + y)
        actions.click()

# 执行鼠标点击操作
actions.perform()

# 关闭浏览器
driver.quit()
