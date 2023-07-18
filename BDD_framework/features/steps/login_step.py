from behave import given, when, then
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#class TestOrangeHRM(unittest.TestCase):
            
testorange_hrm = unittest.TestCase()


@given(u'User has launched Chrome Browser')
def step_launch_chrome(self):
    opts=webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(options=opts)
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)   


@when(u'the User has navigate to the Orange HRM login page')
def step_navigate_to_orangeHRM(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 


@then(u'the User should see the login options')
def step_validate_login_page(self):
    login_text = self.driver.find_element(By.TAG_NAME, "h5").text
   # testorange_hrm.assertEqual("Login", login_text, "Not in Login page")
    assert "Login" == login_text  
    
@then(u'the browser should close')
def step_close_browser(self):
    self.driver.quit()

@given(u'User has navigated to Orange HRM login page')
def step_navigated_to_orange_hrm(self):
    webdriver.ChromeOptions()
    #opts.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    


@when(u'the User enters valid username and password')
def step_enter_login_and_pwrd(self):
    self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    

@then(u'the User should successfully login')
def step_login_success(self):
    dashboard_url = self.driver.current_url
    testorange_hrm.assertIn("/dashboard/index", dashboard_url,  "Test case 2 fail")
    

@when(u'the User enters valid "{username}" and "{password}"')
def step_username_pwrd_parameter(self, username, password):
    self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        

   
    
    
    
            
