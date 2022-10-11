import time
from selenium import webdriver
desired_cap = {
    "os_version": "14",
    "device": "iPhone 11 Pro Max",
    "real_mobile": "true",
    "browserstack.appium_version": "1.21.0",
    "unhandledPromptBehavior": "ignore",
}
driver = webdriver.Remote(
    command_executor='http://chiraggupta_1Swh8i:TFyzx8ev4ztpJ6Lh4ckx@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver.get("https://dev.toms.com/on/demandware.store/Sites-toms-us-Site?qaSource=auto")
driver.execute_script('browserstack_executor: {\"action\": \"sendBasicAuth\", \"arguments\": {\"username\":\"storefront\", \"password\": \"toms2020\", \"timeout\": \"10000\"}}')
time.sleep(10)
driver.quit()
