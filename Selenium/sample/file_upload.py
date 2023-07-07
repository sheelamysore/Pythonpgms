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

more = driver.find_element(By.XPATH, "//a[@href = '#' and @class = 'dropdown-toggle']")
actions = ActionChains(driver)
actions.move_to_element(more).perform()

file_upload = driver.find_element(By.XPATH, "//a[@href = 'FileUpload.html']")
actions.click(file_upload).perform()

browse_file = driver.find_element(By.XPATH, "//input[@id = 'input-4']")
actions.send_keys(r"C:\Users\sheel\OneDrive\Desktop\Zoom\abc.txt").perform()

