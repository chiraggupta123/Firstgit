import time

from selenium import webdriver
driver = webdriver.Chrome("/Users/chiraggupta/Desktop/Driverss/chromedriver")
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("chirag");
driver.find_element_by_id("password").send_keys("Hello");
driver.find_element_by_xpath("//i[@class=\"fa fa-2x fa-sign-in\"]").click();
time.sleep(3)
print("Hello");
print("Hii")
driver.quit()