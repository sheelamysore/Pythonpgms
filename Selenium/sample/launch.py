import time
from selenium import webdriver
from webbrowser import BaseBrowser


driver = webdriver.Chrome()

driver.get("http://selenium.dev")
time.sleep(2000)
#driver.quit()
BaseBrowser