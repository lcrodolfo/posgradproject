import pytest
from pages.register_page import RegisterPage
from utils.logger import get_detailed_logger
from pages.login_page import LoginPage

logger = get_detailed_logger(__name__)

@pytest.mark.register
@pytest.mark.positive
@pytest.mark.tc_id("TC06")
def test_TC06_register_valid_credentials(driver):
    logger.info("===== Starting test: test_TC06_register_valid_credentials =====")
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.click_newUser()
    logger.info("Filling registration form with valid credentials")
    register_page.fill_register_Form("Rodolfo", "Cassimiro","rcassimiro2", "Test123@")
    register_page.submit_register_Form()
    logger.info("Submitted registration form with valid credentials")
    #asserting that the CAPTCHA message is displayed after registration
    assert register_page.get_success_message()
 
@pytest.mark.login_after_registration
@pytest.mark.positive
@pytest.mark.tc_id("TC07")    
def test_TC07_login_after_registration(driver):
    logger.info("===== Starting test: test_TC07_login_after_registration =====")
    login_Page = LoginPage(driver)
    login_Page.open()
    logger.info("Filling login form with newly registered credentials")
    #Using valid credentials created previosuly to access as the site contains captcha and it is not possible to bypass it
    #But in test envs we would need to use the credentials created in the previous test (TC06) to validate the registration process end to end
    login_Page.fill_login_Form("rcassimiro4", "Test123@")
    logger.info("Submitted login form with newly registered credentials")
    login_Page.submit_login_Form()
    assert login_Page.login_successful()
    
@pytest.mark.register
@pytest.mark.negative
@pytest.mark.tc_id("TC08")
def test_TC08_register_empty_fields_validation(driver):
    logger.info("===== Starting test: test_TC08_register_empty_fields_validation =====")
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.click_newUser()
    logger.info("Submitting registration form with empty fields")
    register_page.submit_register_Form()            
    assert register_page.is_first_name_empty() and register_page.is_last_name_empty() and register_page.is_username_empty() and register_page.is_password_empty()

@pytest.mark.register_negative
@pytest.mark.tc_id("TC09")
@pytest.mark.parametrize(
    "first_name, last_name, username, password, validator", 
    [
    ("Rodolfo", "", "rcassimiro4", "Test123@", "is_last_name_empty"),  # Empty last name
    ("", "Cassimiro", "rcassimiro5", "Test123@", "is_first_name_empty"),  # Empty first name
    ("Rodolfo", "Cassimiro", "", "Test123@", "is_username_empty"),  # Empty username
    ("Rodolfo", "Cassimiro", "rcassimiro6", "", "is_password_empty")  # Empty password
    ],
    ids=["TC09.1 - Empty last name", "TC09.2 - Empty first name", "TC09.3 - Empty username", "TC09.4 - Empty password"]
)
def test_TC09_register_empty_fields_validation(driver, first_name, last_name, username, password, validator, request):
    test_name = request.node.name

    logger.info(f"===== Starting test: {test_name} =====")
    logger.info(f"Input data -> first: '{first_name}', last: '{last_name}', user: '{username}', password: '{password}'")

    register_page = RegisterPage(driver)
    register_page.open()
    register_page.click_newUser()
    
    register_page.fill_register_Form(first_name, last_name, username, password)
    register_page.submit_register_Form()    
    
    logger.info(f"Validating field using: {validator}")        
    
    result = getattr(register_page, validator)()

    logger.info(f"Validation result: {result}")

    assert result, f"Expected validation for {validator}"
