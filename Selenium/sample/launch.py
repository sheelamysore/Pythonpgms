import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://selenium.dev")
time.sleep(2000)
#driver.quit()
