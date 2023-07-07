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

driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH, "//input[@id = 'RESULT_TextField-0']").send_keys("tester")
#driver.find_element(By.XPATH, "//input[@type = 'radio' and @id= 'RESULT_RadioButton-1_0']").click()
driver.find_element(By.XPATH, "//label[@for = 'RESULT_RadioButton-1_0']").click()
driver.find_element(By.XPATH, "//input[@class='text_field calendar_field hasDatepicker']").send_keys("07/03/2023")
driver.find_element(By.XPATH, "//select[@id = 'RESULT_RadioButton-3']").click()
#text() = 'Mukesh' ] //table[@name = 'BookTable'] //table[@name = 'BookTable']//tr[4]/td[3]

#//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[2]
#driver.find_elements(by, value)