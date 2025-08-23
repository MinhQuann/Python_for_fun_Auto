import pytest
from src.ui.pages.login_page import LoginPage

pytestmark = pytest.mark.ui

SUCCESS = "You logged into a secure area!"
INVALID = "Your username is invalid!"

@pytest.mark.smoke
def test_login_success(driver, ui_base_url):
    lp = LoginPage(driver)
    lp.open_page(ui_base_url)
    lp.login("tomsmith", "SuperSecretPassword!")
    assert SUCCESS in lp.flash()

def test_login_invalid_user(driver, ui_base_url):
    lp = LoginPage(driver)
    lp.open_page(ui_base_url)
    lp.login("wrong", "SuperSecretPassword!")
    assert INVALID in lp.flash()
