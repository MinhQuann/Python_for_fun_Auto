from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ultils.waits import (
    wait_for_element_to_be_visible,
    wait_for_element_to_be_clickable,
    wait_for_url_contains,
    Locator,
)

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.find_element(locator).click()
    
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    