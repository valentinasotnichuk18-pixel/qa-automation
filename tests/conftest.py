import sys
import os
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# --- API fixtures ---
BASE_URL_API = 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope='session')
def base_url():
    return BASE_URL_API

@pytest.fixture(scope='module')
def posts_response(base_url):
    return requests.get(f'{base_url}/posts')

@pytest.fixture(scope='module')
def single_post_response(base_url):
    return requests.get(f'{base_url}/posts/1')

# --- Selenium fixtures ---
BASE_URL_UI = 'https://the-internet.herokuapp.com'

@pytest.fixture(scope='function')
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
