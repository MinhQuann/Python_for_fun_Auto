from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT   = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH    = (By.ID, "flash")

    def open_page(self, base_url: str):
        self.open(f"{base_url}/login")

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def flash(self) -> str:
        return self.text_of(self.FLASH)
