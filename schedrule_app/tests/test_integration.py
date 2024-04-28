from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class LoginTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Use any webdriver you prefer
        self.browser.implicitly_wait(5)   # Implicit wait to wait for elements to load

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
        
        # unter username and password
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
        
        # Check logout 
        logout_link = self.browser.find_element(by=By.LINK_TEXT, value="Logout")
        self.assertIsNotNone(logout_link)
        
        # Click the logout link
        logout_link.click()
        
        # Wait for the page to load
        time.sleep(2)
        
        # Check login
        login_link = self.browser.find_element(by=By.LINK_TEXT, value="Login")
        self.assertIsNotNone(login_link)
        
class NavbarTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Use any webdriver you prefer
        self.browser.implicitly_wait(5)   # Implicit wait to wait for elements to load

    def tearDown(self):
        self.browser.quit()

    def test_click_events_tab(self):
        # Open the browser and navigate to the home page
        self.browser.get('http://127.0.0.1:8000/')
        
        # Click on the "Events" tab
        events_tab = self.browser.find_element(by=By.LINK_TEXT, value="Events")
        events_tab.click()
        
        # Wait for the page to load
        time.sleep(2)
        
        # Check if the URL has changed to the events page
        self.assertIn("events", self.browser.current_url)
        
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class EventLinkTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Use any webdriver you prefer
        self.browser.implicitly_wait(5)   # Implicit wait to wait for elements to load

    def tearDown(self):
        self.browser.quit()

    def test_event_link(self):
        # Open the browser and navigate to the home page
        self.browser.get('http://127.0.0.1:8000/')
        
        # Find the first link on the home page following the specified convention
        event_link = self.browser.find_element(by=By.XPATH, value="//li/a[contains(@href, '/events/')]")
        
        # Get the href attribute of the link
        href = event_link.get_attribute('href')
        
        # Click on the link
        event_link.click()
        
        # Wait for the page to load
        time.sleep(2)
        
        # Check if the current URL matches the event detail page URL format
        self.assertIn('/events/', self.browser.current_url)
        
class LoginPageTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Use any webdriver you prefer
        self.browser.implicitly_wait(5)   # Implicit wait to wait for elements to load

    def tearDown(self):
        self.browser.quit()

    def test_login_page(self):
        # Open the browser and navigate to the create event page
        self.browser.get('http://127.0.0.1:8000/events/create/')
        
        # Find the username and password input fields
        username_input = self.browser.find_element(by=By.NAME, value="username")
        password_input = self.browser.find_element(by=By.NAME, value="password")
        
        # Check if the login form is present
        self.assertIsNotNone(username_input)
        self.assertIsNotNone(password_input)