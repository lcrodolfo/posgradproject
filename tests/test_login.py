from pages.login_page import LoginPage
import pytest
from utils.logger import get_detailed_logger

logger = get_detailed_logger(__name__)

@pytest.mark.login
@pytest.mark.success
@pytest.mark.tc_id("TC01")
def test_TC01_login_valid_credentials(driver):
    logger.info("===== Starting test: test_TC01_login_valid_credentials =====")
    login_page = LoginPage(driver)
    login_page.open()
    logger.info("Filling login form with valid credentials")
    login_page.fill_login_Form("rcassimiro4", "Test123@")
    login_page.submit_login_Form()
    logger.info("Submitted login form with valid credentials")
    assert login_page.login_successful()
    logger.info("Login successful, test passed")

@pytest.mark.login
@pytest.mark.negative
@pytest.mark.tc_id("TC02")
def test_TC02_login_invalid_credentials(driver):
    logger.info("===== Starting test: test_TC02_login_invalid_credentials =====")
    login_page = LoginPage(driver)
    login_page.open()
    logger.info("Filling login form with invalid credentials")
    login_page.fill_login_Form("invalid_user", "invalid_pass")
    login_page.submit_login_Form()
    logger.info("Submitted login form with invalid credentials")
    assert login_page.get_error_message(); 
    
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.tc_id("TC03")
def test_TC03_password_empty_validation(driver):
    logger.info("===== Starting test: test_TC03_password_empty_validation =====")
    login_page = LoginPage(driver)
    login_page.open()
    logger.info("Filling login form with empty password")
    login_page.fill_login_Form("test2", "")
    logger.info("Submitted login form with empty password")
    login_page.submit_login_Form()
    assert login_page.is_password_empty()

@pytest.mark.login
@pytest.mark.negative
@pytest.mark.tc_id("TC04")
def test_TC04_username_empty_validation(driver):
    logger.info("===== Starting test: test_TC04_username_empty_validation =====")
    login_page = LoginPage(driver)
    login_page.open()
    logger.info("Filling login form with empty username")
    login_page.fill_login_Form("", "Test123@")
    logger.info("Submitted login form with empty username")
    login_page.submit_login_Form()
    
    assert login_page.is_username_empty()
    
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.tc_id("TC05")
def test_TC05_username_and_password_empty_validation(driver):
    logger.info("===== Starting test: test_TC05_username_and_password_empty_validation =====")
    login_page = LoginPage(driver)
    login_page.open()
    logger.info("Filling login form with empty username and password")
    login_page.fill_login_Form("", "")
    logger.info("Submitted login form with empty username and password")
    login_page.submit_login_Form()
    
    assert login_page.is_username_empty() and login_page.is_password_empty()    
    
