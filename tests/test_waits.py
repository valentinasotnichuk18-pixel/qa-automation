import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://the-internet.herokuapp.com'


def test_implicit_wait_limitation(driver):
    driver.implicitly_wait(10)
    driver.get(f'{BASE_URL}/dynamic_loading/1')
    driver.find_element(By.CSS_SELECTOR, '#start button').click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, 'finish')))
    finish = driver.find_element(By.ID, 'finish')
    assert finish.is_displayed()


def test_explicit_wait_element_visible(driver):
    driver.get(f'{BASE_URL}/dynamic_loading/1')
    driver.find_element(By.CSS_SELECTOR, '#start button').click()
    finish = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, 'finish')))
    assert 'Hello World!' in finish.text


def test_explicit_wait_element_clickable(driver):
    driver.get(f'{BASE_URL}/login')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, '#login button').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.flash.success')))
    assert 'secure area' in driver.find_element(By.CSS_SELECTOR, '.flash.success').text.lower()
