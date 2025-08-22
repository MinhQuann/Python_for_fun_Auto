import pytest
from test.pages.login_page import LoginPage
from test.data.user import BASE_URL, VALID_USER, INVALID_USER
from test.ultils.waits import wait_for_url_contains
from test.ultils.screenshot import take_screenshot

@pytest.mark.smoke
def test_login_success(driver, config):
    page = LoginPage(driver, timeout=config["explicit_wait"]).open_login(BASE_URL)
    page.login_as(VALID_USER["username"], VALID_USER["password"])
    # Sau khi login thành công, trang chuyển hướng đến dashboard
    wait_for_url_contains(driver, "ucrm", timeout=config["explicit_wait"])
    assert "ucrm" in driver.current_url
    # Capture screenshot khi test pass
    take_screenshot(driver, "login_success")

@pytest.mark.regression
def test_login_with_wrong_password_shows_error(driver, config):
    page = LoginPage(driver, timeout=config["explicit_wait"]).open_login(BASE_URL)
    page.login_as(INVALID_USER["username"], INVALID_USER["password"])
    err = page.get_error()
    assert "Sai thông tin đăng nhập" in err or "Invalid credentials" in err or "Tài khoản không tồn tại" in err
    # Capture screenshot khi test pass
    take_screenshot(driver, "login_wrong_password")

@pytest.mark.regression
@pytest.mark.parametrize("username,password", [
    ("", ""), ("admin", ""), ("", "admin")
])
def test_login_with_empty_fields(driver, config, username, password):
    page = LoginPage(driver, timeout=config["explicit_wait"]).open_login(BASE_URL)
    page.login_as(username, password)
    err = page.get_error()
    assert err != ""  # có thông báo lỗi
    # Capture screenshot khi test pass
    take_screenshot(driver, f"login_empty_fields_{username}_{password}")

def test_password_required(login_page: LoginPage):
    # Giả sử bạn đã submit form trống để trigger lỗi
    # login_page.submit()
    assert login_page.password_error_text() == "Nhập mật khẩu"

def test_required_errors_present(login_page: LoginPage):
    # login_page.submit()
    errors = login_page.all_error_texts(min_count=2)
    expected = {"Nhập email", "Nhập mật khẩu"}
    assert expected.issubset(set(errors))