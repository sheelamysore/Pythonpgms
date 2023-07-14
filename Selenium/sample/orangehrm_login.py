from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''1. launching the chrome browser with detach option and maximising the window'''
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(10)

'''2. Navigating to target URL'''
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH,"//aside[@class = 'oxd-sidepanel']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("Admin")
driver.find_element(By.XPATH, "//span[text()='Admin']").click()
    
    
    
    
