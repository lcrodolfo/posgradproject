import pytest
from pages.profile_page import ProfilePage
from pages.register_page import RegisterPage
from utils.logger import get_detailed_logger
from pages.login_page import LoginPage

logger = get_detailed_logger(__name__)

@pytest.mark.profile_logout
@pytest.mark.positive
@pytest.mark.tc_id("TC10")
def test_TC10_profile_logout(driver):
    logger.info("===== Starting test: test_TC10_profile_logout =====")
    login_page = LoginPage(driver)
    login_page.open()
    logger.info("Filling login form with valid credentials")
    login_page.fill_login_Form("rcassimiro4", "Test123@")
    login_page.submit_login_Form()
    logger.info("Submitted login form with valid credentials")
    assert login_page.login_successful()    
    profile_page = ProfilePage(driver)
    profile_page.click_logout()
    
    assert profile_page.is_logged_out()
    
@pytest.mark.profile_logout
@pytest.mark.positive
@pytest.mark.tc_id("TC11")
def test_TC11_go_to_books_store_from_profile(driver):
    logger.info("===== Starting test: test_TC11_go_to_books_store_from_profile =====")
    login_page = LoginPage(driver)
    login_page.open()
    logger.info("Filling login form with valid credentials")
    login_page.fill_login_Form("rcassimiro4", "Test123@")
    login_page.submit_login_Form()
    logger.info("Submitted login form with valid credentials")
    assert login_page.login_successful()    
    profile_page = ProfilePage(driver)
    logger.info("Navigating to book store from profile page")
    profile_page.go_to_book_store()
    
    assert profile_page.is_on_book_store()
@pytest.mark.profile_logout
@pytest.mark.positive
@pytest.mark.tc_id("TC12")
def test_TC12_add_book_from_profile(driver):
    logger.info("===== Starting test: test_TC12_add_book_from_profile =====")
    login_page = LoginPage(driver)
    login_page.open()
    logger.info("Filling login form with valid credentials")
    login_page.fill_login_Form("rcassimiro4", "Test123@")
    login_page.submit_login_Form()
    logger.info("Submitted login form with valid credentials")
    assert login_page.login_successful()    
    profile_page = ProfilePage(driver)
    logger.info("Navigating to book store from profile page")
    profile_page.go_to_book_store()
    
    assert profile_page.is_on_book_store()
    
    book_name = "Git Pocket Guide"
    logger.info(f"Adding book '{book_name}' to profile from book store")
    profile_page.add_book_to_profile(book_name)
    logger.info(f"Navigating back to profile page")
    profile_page.go_back_to_profile()
    logger.info(f"Checking if book '{book_name}' is in user's collection")
    assert profile_page.is_profile_page()
    assert profile_page.is_book_in_collection(book_name)