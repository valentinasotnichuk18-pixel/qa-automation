# QA Automation Framework

Test automation framework built from scratch in Python while transitioning into QA engineering. Covers UI automation with Selenium (Page Object Model), API testing, and pytest practices.

## Tech stack

- Python 3.14
- pytest
- Selenium WebDriver 4 + webdriver-manager
- requests

## Structure

qa_automation/
├── pages/ # Page Object Model
│ ├── base_page.py # Base class: waits, common actions
│ └── login_page.py # Login page locators and methods
├── tests/
│ ├── conftest.py # pytest fixtures (driver setup/teardown)
│ ├── test_login_pom.py # UI login tests using POM
│ ├── test_selenium_basic.py # Selenium basics: locators, interactions
│ ├── test_waits.py # Explicit waits practice
│ ├── test_api.py # API tests with requests
│ ├── test_jsonplaceholder.py # CRUD tests for JSONPlaceholder API
│ ├── test_crud.py # CRUD test scenarios
│ ├── test_auth.py # Auth API tests (positive and negative)
│ └── test_calculator.py # Unit tests with parametrization
└── calculator.py # Practice module under test


## What is covered

- Page Object Model pattern for maintainable UI tests
- Explicit waits (WebDriverWait, expected_conditions)
- API testing: status codes, response body validation, positive and negative cases
- Parametrized tests with pytest.mark.parametrize
- Fixtures for setup and teardown

## How to run

python -m venv venv
venv\Scripts\activate
pip install pytest selenium webdriver-manager requests
python -m pytest tests/ -v


## Author

Valentyna Sotnichuk — Manual QA / Junior QA Automation in progress
[GitHub](https://github.com/valentinasotnichuk18-pixel)
