import pytest
from test.pages.login_page import LoginPage
from test.ultils.waits import wait_for_url_contains
from test.ultils.screenshot import take_screenshot
from test.pages.dashboard_page import DashboardPage

@pytest.mark.smoke
def test_login_success(driver, config):
    page = LoginPage(driver, timeout=config["explicit_wait"]).open_login(config["base_url"])
    page.login_as("crmxvtb2.0@basebs.com", "12345678x@X")
    print(config["username"])
    print(config["password"])
    # Sau khi login thành công, trang chuyển hướng đến dashboard
    wait_for_url_contains(driver, "ucrm", timeout=config["explicit_wait"])
    assert "ucrm" in driver.current_url
    dashboard_page = DashboardPage(driver, timeout=config["explicit_wait"])
    dashboards = dashboard_page.get_all_dashboards()
    expected = ['CÀI ĐẶT TÀI KHOẢN', 'CÀI ĐẶT ĐỐI TƯỢNG', 'TỰ ĐỘNG HÓA', 'CẤU HÌNH THÔNG BÁO', 'CẤU HÌNH EMAIL', 'SMS', 'CONSOLIDATED SETTING', 'TÍCH HỢP', 'HỆ THỐNG']
    assert expected == dashboards
    # Capture screenshot khi test pass
    take_screenshot(driver, "login_success")

@pytest.mark.regression
def test_login_with_wrong_password_shows_error(driver, config):
    page = LoginPage(driver, timeout=config["explicit_wait"]).open_login(config["base_url"])
    page.login_as("wrong@email.com", "wrongpass")
    err = page.get_error()
    assert "Sai thông tin đăng nhập" in err or "Invalid credentials" in err or "Tài khoản không tồn tại" in err
    # Capture screenshot khi test pass
    take_screenshot(driver, "login_wrong_password")

@pytest.mark.regression
def test_login_with_wrong_username_shows_error(driver, config):
    page = LoginPage(driver, timeout=config["explicit_wait"]).open_login(config["base_url"])

@pytest.mark.regression
@pytest.mark.parametrize("username2,password2", [
    ("", ""), ("admin", ""), ("", "admin")
])
def test_login_with_empty_fields(driver, config, username2, password2):
    page = LoginPage(driver, timeout=config["explicit_wait"]).open_login(config["base_url"])
    page.login_as(username2, password2)
    err = page.get_error()
    assert err != ""  # có thông báo lỗi
    # Capture screenshot khi test pass
    take_screenshot(driver, f"login_empty_fields_{username2}_{password2}")


def test_required_errors_present(driver, config):
    page = LoginPage(driver, timeout=config["explicit_wait"]).open_login(config["base_url"])
    page.login_as("", "")
    errors = page.all_error_texts(min_count=2)
    print(errors)
    expected = {"Nhập email", "Nhập mật khẩu"}
    assert expected.issubset(set(errors))
    take_screenshot(driver, "required_errors_present")