from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

# 1. 设置 Appium Desired Capabilities
desired_caps = {
    "platformName": "iOS",
    "platformVersion": "17.6.1",
    "deviceName": "iPhone 14",
    "app": "/path/to/MyObservatory.app", # 替换为 MyObservatory app 的路径
    "automationName": "XCUITest", # 使用 XCUITest 自动化框架
    "bundleId": "com.yourcompany.MyObservatory", # 替换为 MyObservatory app 的 bundle ID
}

# 2. 启动 Appium 驱动
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# 3. 等待 app 启动
sleep(5)

# 4. 点击左上角目录页面
menu_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Menu")
menu_button.click()

# 5. 点击预报及警告服务
forecast_button = driver.find_element(MobileBy.XPATH, "//XCUIElementTypeButton[@name='预报及警告服务']")
forecast_button.click()

# 6. 选择 9 天预报
nine_day_forecast_button = driver.find_element(MobileBy.XPATH, "//XCUIElementTypeButton[@name='9 天预报']")
nine_day_forecast_button.click()

# 7. (可选) 验证 9 天预报页面是否显示
sleep(2)
try:
    driver.find_element(MobileBy.XPATH, "//XCUIElementTypeStaticText[@name='9 天预报']")
    print("9 天预报页面显示成功")
except:
    print("9 天预报页面显示失败")

# 8. 结束 Appium 驱动
driver.quit()