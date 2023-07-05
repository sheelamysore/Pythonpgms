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
driver.get("https://demo.automationtesting.in/Resizable.html")

#resizable = driver.find_element(By.XPATH, "//div[contains(@class, 'ui-resizable-handle ui-resizable-se ui-']")
resizable = driver.find_element(By.XPATH, "//div[@class = 'ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(resizable, 60, 80).perform()

interactions = driver.find_element(By.XPATH, "//a[@href = 'Interactions.html']")
actions.move_to_element(interactions).perform()
time.sleep(5)
draganddrop = driver.find_element(By.XPATH, "//a[@class = 'dropdown-toggle' and @href = 'Interactions.html']")
#actions.move_to_element(draganddrop).perform()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(draganddrop))
actions.move_to_element(draganddrop).perform()
static = driver.find_element(By.XPATH, "//a[@href = 'Static.html']")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(static)).click()

#actions.move_to_element(interactions).move_to_element(draganddrop).click(static).perform()

