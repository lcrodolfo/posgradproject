from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL
from utils.logger import get_detailed_logger

logger = get_detailed_logger(__name__)

#Register page for the demoqa website, contains all the locators and actions related to the registration process.
class RegisterPage:
    def __init__(self,driver):
        self.driver = driver
    
    #LOCATORS
    new_user_button = (By.ID, "newUser")
    first_name_input = (By.ID, "firstname")
    last_name_input = (By.ID, "lastname")
    username_input = (By.ID, "userName")
    password_input = (By.ID, "password")
    register_button = (By.ID, "register")
    success_message = (By.XPATH, "//*[contains(text(),'Please verify reCaptcha to register!')]")
    back_to_login_button = (By.ID, "gotologin")
    
    #OPENING DEMOQA LOGIN PAGE
    def open(self):
        logger.debug("Opening register page")
        self.driver.get(f"{BASE_URL}login")
    
    #ACTIONS
    def click_newUser(self):
        logger.debug("Clicking on New User button")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.new_user_button)).click()

    def fill_register_Form(self, first_name, last_name, username, password):
        logger.debug("Filling first name")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.first_name_input)).send_keys(first_name)
        logger.debug("Filling last name")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.last_name_input)).send_keys(last_name)
        logger.debug("Filling username")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.username_input)).send_keys(username)
        logger.debug("Filling password")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_input)).send_keys(password)
    
    def submit_register_Form(self):
        logger.debug("Submitting registration form")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.register_button)).click()
        
    def back_to_login(self):
        logger.debug("Returning to login page")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.back_to_login_button)).click()
        
    
    #VALIDATIONS
    def get_success_message(self):
        logger.debug("Getting success message")
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.success_message))).text
    
    def is_password_empty(self):
        logger.info("Checking if password field is highlighted as empty")
        element = self.driver.find_element(*self.password_input)
        return "is-invalid" in element.get_attribute("class")
    
    def is_username_empty(self):
        logger.info("Checking if username field is highlighted as empty")
        element = self.driver.find_element(*self.username_input)
        return "is-invalid" in element.get_attribute("class")
    def is_first_name_empty(self):
        logger.info("Checking if first name field is highlighted as empty")
        element = self.driver.find_element(*self.first_name_input)
        return "is-invalid" in element.get_attribute("class")
    def is_last_name_empty(self):
        logger.info("Checking if last name field is highlighted as empty")
        element = self.driver.find_element(*self.last_name_input)
        return "is-invalid" in element.get_attribute("class")
    