from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

# 设置 Appium Desired Capabilities
desired_caps = {
    "platformName": "iOS",
    "platformVersion": "17.6.1",
    "deviceName": "iPhone 14",
    "app": "/path/to/MyObservatory.app",
    "automationName": "XCUITest", 
    "bundleId": "com.yourcompany.MyObservatory", 
}

# start Appium
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(5)


menu_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Menu")
menu_button.click()

# click the Forecast button
forecast_button = driver.find_element(MobileBy.XPATH, "//XCUIElementTypeButton[@name='Forecast & Warning Services']")
forecast_button.click()

# chose 9-day forecase
nine_day_forecast_button = driver.find_element(MobileBy.XPATH, "//XCUIElementTypeButton[@name='9-Day Forecast']")
nine_day_forecast_button.click()

time.sleep(2)
try:
    driver.find_element(MobileBy.XPATH, "//XCUIElementTypeStaticText[@name='9-Day Forecast']")
    print("get the 9 days forecast success!")
except:
    print("get the 9 days forecast failed!")

driver.quit()