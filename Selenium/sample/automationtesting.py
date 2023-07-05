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
window_before = driver.current_window_handle

'''3. Enter Name'''
# driver.find_element(By.ID, "name").send_keys("Vivek")
name_txtbx=driver.find_element(By.ID, "name")
name_txtbx.send_keys("Tester")

phone = driver.find_element(By.ID, "phone")
phone.send_keys("9999999999")

name_email = driver.find_element(By.XPATH, "//input[@id = 'email']")
name_email.send_keys("abc@gmail.com")

gender_clickbx=driver.find_element(By.XPATH, "//input[@id = 'male']")
gender_clickbx.click()

day_clickbx=driver.find_element(By.XPATH, "//input[@id = 'monday']")
day_clickbx.click()

country_dropdown=Select(driver.find_element(By.XPATH, "//select[@id = 'country' and @class = 'form-control']"))
time.sleep(5)
country_dropdown.select_by_visible_text("Germany")

# driver.find_element(By.XPATH, "//select[@id = 'country' and @class = 'form-control']/option[text()='United Kingdom']").click() 
# driver.find_element(By.XPATH, "//select[@id = 'colors' and @class = 'form-control']/option[text()='Yellow']").click() 

wiki_txtbx = driver.find_element(By.XPATH, "//input[@class = 'wikipedia-search-input']")
wiki_txtbx.send_keys("Selenium")

wiki_searchbx = driver.find_element(By.XPATH, "//input[@class = 'wikipedia-search-button']")
wiki_searchbx.click()



wiki_clicklink = driver.find_element(By.XPATH, "//a[contains(@href, '/wiki/Selenium') and @target = '_blank' and text()='Selenium']")
wiki_clicklink.click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.find_element(By.XPATH,"//a[contains(., 'History')]").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'History')]"))).click()
#//input[@class='text_field calendar_field hasDatepicker']

#driver.getwindowhandles

