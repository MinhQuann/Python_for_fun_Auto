from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from ultils.waits import (
    wait_for_element_to_be_visible,
    Locator,
)

class LoginPage(BasePage):

    # Locators
    BTN_OUTSIDE = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    USERNAME_INPUT = (By.ID, "basic_email")
    PASSWORD_INPUT = (By.ID, "basic_pass")
    LOGIN_BUTTON = (By.XPATH, "//*[@class='ant-btn ant-btn-primary']")
    PASSWORD_HELP: Locator  = (By.ID, "basic_pass_help")
    PASSWORD_ERROR_IN_HELP: Locator = (By.CSS_SELECTOR, "#basic_pass_help .ant-form-item-explain-error")
    ALL_ERRORS: Locator = (By.CSS_SELECTOR, "div.ant-form-item-explain-error")


    # Actions
    def open_login(self, base_url):
        self.driver.get(base_url)
        return self
    
    def login_as(self, username, password):
        self.click(self.BTN_OUTSIDE)
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)


    def get_password_help(self)->str:
        help_box = wait_for_element_to_be_visible(self.driver, self.PASSWORD_HELP)
        err_el = help_box.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error")
        WebDriverWait(self.driver, self.timeout).until(lambda d: err_el.is_displayed() and err_el.text.strip() != "")
        return err_el.text.strip()

        # --- List-based: gom toàn bộ lỗi để assert set expected ---
    def all_error_texts(self, min_count: int = 1) -> list[str]:
        """
        Trả về list tất cả error text đang hiển thị (đã strip, bỏ rỗng).
        min_count: số lượng tối thiểu mong đợi (giúp tránh lấy quá sớm).
        """
        def _ready(d):
            els = d.find_elements(*self.ALL_ERRORS)
            texts = [e.text.strip() for e in els if e.is_displayed() and e.text.strip()]
            return texts if len(texts) >= min_count else False

        return WebDriverWait(self.driver, self.timeout).until(_ready)

    def get_error(self):
        """Lấy error message đầu tiên"""
        error_elements = self.find_elements(self.ALL_ERRORS)
        if error_elements:
            return error_elements[0].text.strip()
        return ""

    def is_error_displayed(self):
        """Kiểm tra có error message nào hiển thị không"""
        return len(self.find_elements(self.ALL_ERRORS)) > 0

    def password_error_text(self):
        """Lấy text của password error"""
        password_errors = self.find_elements(self.PASSWORD_ERROR_IN_HELP)
        if password_errors:
            return password_errors[0].text.strip()
        return ""



