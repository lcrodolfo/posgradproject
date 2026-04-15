#   Selenium Automation Project (Python + Pytest)

## Overview

This project is a web automation framework built using Python, Selenium WebDriver, and Pytest.
It follows best practices such as Page Object Model (POM),  and custom logging & reporting.

The automation covers scenarios from the DemoQA website, including login, registration, and book store interactions.

https://demoqa.com/


## Project Structure

```
project-root/
│
├── pages/                # Page Object Model classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── register_page.py
│   └── book_store_page.py
│
├── tests/                # Test cases
│   ├── test_login.py
│   ├── test_register.py
│   └── test_book_store.py
│
├── utils/                # Utilities (loggers)
│   └── logger.py
│
├── logs/                 # Execution logs (generated automatically)
│   └── run_<timestamp>/
│
├── conftest.py           # Fixtures, hooks, reporting
├── pytest.ini            # Pytest configuration (markers)
├── requirements.txt
└── README.md
```

---

## Tech Stack

* Python 3.x
* Selenium WebDriver
* Pytest
* WebDriver Manager
* Logging (Python logging module)

---

## How to Install

1. Clone the repository:

```bash
git clone https://github.com/lcrodolfo/posgradproject
cd project-root
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run Tests

Run all tests:

```bash
pytest -v
```
Run a specific test:

```bash
pytest tests/test_login.py::test_login_valid_credentials -v
```

Run by keyword:

```bash
pytest -k "TC01" -v
pytest -k "TC02" -v
and on..
```

---

## Test Markers

Defined in `pytest.ini`:

* `login` → login tests
* `success` → main tests
* `negative` → negative scenarios
* `tc_id(id)` → test case identifier


```python
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.tc_id(TC01)
```

Run by marker:

```bash
pytest -m login -v
```

---

##  Framework Design

### Page Object Model (POM)

Each page contains:

* locators
* actions
* validations

Example:

```python
class LoginPage:
    def login(self, username, password):
        ...
```

---

## 🪵 Logging System

Each test execution generates:

```
logs/run_<timestamp>/
├── detailed.log   # step-by-step execution
├── results.log    # PASS / FAIL summary
├── *.png          # screenshots on failure
```
## Screenshot on Failure

Screenshots are automatically captured when a test fails:

```text
TC09_test_register FAILED
Screenshot saved: logs/run_xxx/test.png
```

---

## Test Summary

At the end of execution:

```
===== TEST SUMMARY =====
Total: X
Passed: X
Failed: X
Success Rate: XX%
```

---

## Best Practices Used

* Page Object Model
* Explicit waits (no sleep)
* Data-driven testing
* Logging and reporting
* Reusable methods
* Clean test structure

---

## 👨‍💻 Author

Rodolfo Cassimiro

---
