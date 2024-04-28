from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class LoginTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Use any webdriver you prefer
        self.browser.implicitly_wait(10)   # Implicit wait to wait for elements to load

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        # Open the browser and navigate to the login page
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        
        # Find the username and password input fields and enter credentials
        username_input = self.browser.find_element(by=By.NAME, value="username")
        password_input = self.browser.find_element(by=By.NAME, value="password")
        
        username_input.send_keys('Jeff1')
        password_input.send_keys('Sp3ctrum')
        
        # Submit the form
        submit_button = self.browser.find_element(by=By.XPATH, value="//input[@type='submit']")
        submit_button.click()
        # Wait for the page to load
        time.sleep(2)
        
        logout_link = self.browser.find_element(by=By.LINK_TEXT, value="Logout")
        self.assertIsNotNone(logout_link)
        
    def test_logout(self):
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        
        # Find the username and password input fields and enter credentials
        username_input = self.browser.find_element(by=By.NAME, value="username")
        password_input = self.browser.find_element(by=By.NAME, value="password")
        
        username_input.send_keys('Jeff1')
        password_input.send_keys('Sp3ctrum')
        
        # Submit the form
        submit_button = self.browser.find_element(by=By.XPATH, value="//input[@type='submit']")
        submit_button.click()
        # Wait for the page to load
        time.sleep(2)
        
        logout_link = self.browser.find_element(by=By.LINK_TEXT, value="Logout")
        self.assertIsNotNone(logout_link)
        
        # Check if the navbar has the "Logout" link
        logout_link = self.browser.find_element(by=By.LINK_TEXT, value="Logout")
        self.assertIsNotNone(logout_link)
        
        # Click the logout link
        logout_link.click()
        
        # Wait for the page to load
        time.sleep(2)
        
        # Check if the navbar now has the "Login" link
        login_link = self.browser.find_element(by=By.LINK_TEXT, value="Login")
        self.assertIsNotNone(login_link)
        
