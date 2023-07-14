
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOrangeHRM(unittest.TestCase):


    def test_navigation(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=opts)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_text = self.driver.find_element(By.TAG_NAME, "h5").text
        self.assertEqual("Login", login_text, "Not in Login page")
        
    def test_login(self):
        self.test_navigation()
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        dashboard_url = self.driver.current_url
        self.assertIn("/dashboard/index", dashboard_url,  "Test case 2 fail")
    

if __name__ == "__main__":
    import sys;sys.argv = ['', 'TestOrangeHRM.test_login'] #- classname.methodname
    unittest.main()