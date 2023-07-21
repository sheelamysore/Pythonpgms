import time
from selenium import webdriver


driver = webdriver.Edge()

driver.get("http://selenium.dev")
time.sleep(2000)

