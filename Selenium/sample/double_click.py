from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

'''1. launching the chrome browser with detach option and maximising the window'''
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(10)

'''2. Navigating to target URL'''
driver.get("https://testautomationpractice.blogspot.com/")

dblclick = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction1()']")
actions = ActionChains(driver)
# actions.double_click(dblclick).perform()
#actions.perform()
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
#actions.drag_and_drop(source, target).perform()

source = driver.find_element(By.XPATH, "//span[@class = 'ui-slider-handle ui-corner-all ui-state-default']")
#actions.drag_and_drop_by_offset(source, 100, 0).perform()

actions.scroll_to_element(source).perform()