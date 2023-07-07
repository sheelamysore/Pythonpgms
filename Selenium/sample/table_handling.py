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
table_rows = driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr")
print(type(table_rows))
rows = len(table_rows)
table_col = driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//th")
cols = len(table_col)


for i in range(2, rows+1):
   for j in range(1, cols+1):  
     data_table = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr[" + str(i) + "]/td[" + str(j) + "]")
     #row_data = table_rows[i].text 
     #cell_value = table_col[j].text 
     if j == 4:
         bookname = data_table.text
    
       
     if data_table.text == "Amod":
         print("bookname is", bookname)
         
      #print("row num is", str(i) +  "col num is", str(j))
     #print(j)
     # print(cell_value)
     # if cell_value == "Author":
     #    print("Author")
     
