import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
desired_cap = {
"os" : "OS X",
"os_version" : "Big Sur",
"browser" : "Chrome",
"browser_version" : "latest",
"browserstack.local" : "false",
"browserstack.selenium_version" : "3.14.0"
}
driver = webdriver.Remote(
    command_executor='https://chiraggupta_1Swh8i:TFyzx8ev4ztpJ6Lh4ckx@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window    
driver.find_element_by_id("username").send_keys("chirag");
driver.find_element_by_id("password").send_keys("Hello");
driver.find_element_by_xpath("//i[@class=\"fa fa-2x fa-sign-in\"]").click();
time.sleep(3)
driver.quit()

    