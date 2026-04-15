from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from utils.logger import get_results_logger, get_detailed_logger, LOG_DIR

#loggers
results_logger = get_results_logger()
detailed_logger = get_detailed_logger("RESULT")

#summary of test results to be logged at the end of the test session
test_results_summary = {
    "passed": 0,
    "failed": 0
}

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        # pegar TC ID se existir
        tc_id = None
        for marker in item.iter_markers(name="tc_id"):
            tc_id = marker.args[0]

        test_name = item.name
        label = f"{tc_id} - {test_name}" if tc_id else test_name
        
        driver = item.funcargs.get("driver", None)

        if rep.passed:
            results_logger.info(f"{label} PASSED")
            detailed_logger.info(f"{label} PASSED")
            test_results_summary["passed"] += 1

        elif rep.failed:
            results_logger.error(f"{label} FAILED")
            detailed_logger.error(f"{label} FAILED")
            test_results_summary["failed"] += 1
            
            #Screenshot on failure
            if driver:
                try:
                    screenshot_name = f"{tc_id}_{test_name}.png" if tc_id else f"{test_name}.png"
                    screenshot_path = f"{LOG_DIR}/{screenshot_name}"

                    driver.save_screenshot(screenshot_path)

                    results_logger.error(f"Screenshot saved: {screenshot_path}")
                    detailed_logger.error(f"Screenshot saved: {screenshot_path}")

                except Exception as e:
                    results_logger.error(f"Failed to take screenshot: {e}")
                    detailed_logger.error(f"Failed to take screenshot: {e}")

#Summary of test results at the end of the test session
def pytest_sessionfinish(session, exitstatus):
    total = test_results_summary["passed"] + test_results_summary["failed"]
    passed = test_results_summary["passed"]
    failed = test_results_summary["failed"]

    success_rate = (passed / total * 100) if total > 0 else 0
    failure_rate = (failed / total * 100) if total > 0 else 0

    results_logger.info("===== TEST SUMMARY =====")
    results_logger.info(f"Total: {total}")
    results_logger.info(f"Passed: {passed}")
    results_logger.info(f"Failed: {failed}")
    results_logger.info(f"Success Rate: {success_rate:.2f}%")
    results_logger.info(f"Failure Rate: {failure_rate:.2f}%")