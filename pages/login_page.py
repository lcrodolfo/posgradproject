from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL
from utils.logger import get_detailed_logger

logger = get_detailed_logger(__name__)

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
       

    #LOCATORS
    username_input = (By.ID, "userName")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login")
    error_message = (By.XPATH, "//*[contains(text(),'Invalid username or password!')]")
    
    
    #OPENING DEMOQA LOGIN PAGE
    def open(self):
        logger.debug("Opening login page")
        self.driver.get(f"{BASE_URL}login")
    
    #ACTIONS
    def fill_login_Form(self, username, password):
        logger.debug("Filling username ")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.username_input)).send_keys(username)
        logger.debug("Filling password")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_input)).send_keys(password)
    
    def submit_login_Form(self):
        logger.debug("Submitting login form")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
        
    
    #VALIDATIONS
    def get_error_message(self):
        logger.info("Checking error message")
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.error_message))).text
    
    def login_successful(self):
        logger.info("Checking if login was successful")
        return WebDriverWait(self.driver, 10).until(EC.url_contains("/profile"))
    
    def is_password_empty(self):
        logger.info("Checking if password field is highlighted as empty")
        element = self.driver.find_element(*self.password_input)
        return "is-invalid" in element.get_attribute("class")
    
    def is_username_empty(self):
        logger.info("Checking if username field is highlighted as empty")
        element = self.driver.find_element(*self.username_input)
        return "is-invalid" in element.get_attribute("class")