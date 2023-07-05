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
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//button[@onclick='myFunctionConfirm()']").click()

driver.switch_to.alert.accept()
test_confirm = driver.find_element(By.ID, 'demo')
confirm_msg = test_confirm.text
if confirm_msg == 'You pressed OK!':
    print("test passed")
else:    
    print("test fail")
    
driver.find_element(By.XPATH, "//button[@onclick='myFunctionConfirm()']").click()

driver.switch_to.alert.dismiss()
test_confirm = driver.find_element(By.ID, 'demo')
confirm_msg = test_confirm.text
if confirm_msg == 'You pressed Cancel!':
    print("test passed")
else:    
    print("test fail")    

# driver.find_element(By.XPATH, "//button[@onclick='myFunctionPrompt()']").click()
# time.sleep(5)
# driver.switch_to.alert.send_keys("Tester")
# driver.switch_to.alert.accept()
# driver.current_url
# driver.title

