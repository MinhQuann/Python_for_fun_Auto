from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def wait_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def fill(self, locator, text: str):
        el = self.wait_visible(locator)
        el.clear()
        el.send_keys(text)

    def click(self, locator):
        self.wait_visible(locator).click()

    def text_of(self, locator) -> str:
        return self.wait_visible(locator).text
