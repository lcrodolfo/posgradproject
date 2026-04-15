from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL
from utils.logger import get_detailed_logger

logger = get_detailed_logger(__name__)

class ProfilePage:
    def __init__(self,driver):
        self.driver = driver
    
    #LOCATORS
    profile_header = (By.XPATH, "//*[contains(text(),'Books')]")
    logout_button = (By.XPATH, "//button[text()='Logout']")
    delete_account_button = (By.XPATH, "//button[text()='Delete Account']")
    go_book_store_button = (By.ID, "gotoStore")
    delete_all_books_button = (By.XPATH, "//button[text()='Delete All Books']")
    ok_delete_button = (By.ID, "closeSmallModal-ok") 
    cancel_delete_button = (By.ID, "closeSmallModal-cancel")
    search_box = (By.ID, "searchBox")
    search_button = (By.XPATH, "//input[@id='searchBox']/following-sibling::button")
    
    
    
    #ACTIONS
    def click_logout(self):
        logger.debug("Clicking on Logout button")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_button)).click()

    def go_to_book_store(self):
        logger.debug("Navigating to Book Store")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.go_book_store_button)).click()
     
   
    def search_book(self, book_name):
        logger.debug(f"Searching for book: {book_name}")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_box)).send_keys(book_name)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button)).click()
    
    def go_to_book_details(self, book_name):
        logger.debug(f"Navigating to book details for: {book_name}")
        book_locator = (By.XPATH, f"//a[text()='{book_name}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(book_locator)).click()
        
    def add_book_to_profile(self, book_name):
        logger.info(f"Adding book '{book_name}' to profile")
        book_locator = (By.XPATH, f"//a[contains(text(), '{book_name}')]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(book_locator)).click()
        add_button = (By.XPATH, "//button[text()='Add To Your Collection']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(add_button)).click()
        
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        logger.info(f"Alert text: {alert.text}")
        if alert_text == "Book added to your collection.":
            logger.info(f"Book '{book_name}' added to profile successfully")
            alert.accept()
        else:             
            logger.warning(f"Unexpected alert message: {alert_text}")       
               
    def go_back_to_profile(self):
        logger.debug("Navigating back to profile page")
        profile_locator = (By.XPATH, "//span[text()='Profile']") 
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(profile_locator)).click()
        
    #VALIDATIONS
    def is_profile_page(self):
        logger.info("Checking if user is on profile page")
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.profile_header))).is_displayed()
    
    def is_logged_out(self):
        logger.info("Checking if user is logged out")
        return WebDriverWait(self.driver, 10).until(EC.url_contains("/login"))
    
    def is_still_logged_in(self):
        logger.info("Checking if user is still logged in")
        return WebDriverWait(self.driver, 10).until(EC.url_contains("/profile"))
    
    def is_account_deleted(self):
        logger.info("Checking if account is deleted")
        return WebDriverWait(self.driver, 10).until(EC.url_contains("/login"))
    
    def is_on_book_store(self):
        logger.info("Checking if user is on book store page")
        return WebDriverWait(self.driver, 10).until(EC.url_contains("/books"))
    
    
    def is_book_in_collection(self, book_name):
        logger.info(f"Checking if book '{book_name}' is in user's collection")
        book_locator = (By.XPATH, f"//a[text()='{book_name}']")
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((book_locator))).is_displayed()
    
    def is_book_not_in_collection(self, book_name):
        logger.info(f"Checking if book '{book_name}' is not in user's collection")

        book_locator = (By.XPATH, f"//a[text()='{book_name}']")
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((book_locator)))
            return False
        except:
            return True
        
    def is_book_details_page(self, book_name):
        logger.info(f"Checking if user is on book details page for: {book_name}")
        book_details_header = (By.XPATH, f"//label[text()='{book_name}']")
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((book_details_header))).is_displayed()