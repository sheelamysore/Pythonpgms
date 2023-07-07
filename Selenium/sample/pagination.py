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
table_rows = driver.find_elements(By.XPATH, "//table[@id = 'productTable']//tr")

print(type(table_rows))
rows = len(table_rows)
table_cols = driver.find_elements(By.XPATH, "//table[@id = 'productTable']//th")
cols = len(table_cols)
for i in range(2, rows+1):
   for j in range(1, cols+1):  
     data_table = driver.find_element(By.XPATH, "//table[@id = 'productTable']//tr[" + str(i) + "]/td[" + str(j) + "]")
     
     print(data_table.text)