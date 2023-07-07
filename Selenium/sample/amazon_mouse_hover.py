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
driver.get("https://www.amazon.in/")

prime = driver.find_element(By.XPATH, "//a[@href = '/prime?ref_=nav_cs_primelink_nonmember']")
actions = ActionChains(driver)
actions.move_to_element(prime).perform()

prime_link = driver.find_element(By.XPATH, "//a[@href = '/prime?ref=in-pr-tryprime-unrec-multi-benefit']")
actions.click(prime_link).perform()