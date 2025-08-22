from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from typing import Tuple

Locator = Tuple[str, str]

def wait_for_url_contains(driver, fragment: str, timeout: int = 10):
    WebDriverWait(driver, timeout).until(expected_conditions.url_contains(fragment))

def wait_for_element_to_be_clickable(driver, locator, timeout: int = 10):
    WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

def wait_for_element_to_be_visible(driver, locator, timeout: int = 10):
    WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))