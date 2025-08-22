import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from ultils.screenshot import take_screenshot_on_failure, take_screenshot_for_allure

load_dotenv()  # đọc .env

def _build_chrome(headless: bool):
    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

@pytest.fixture(scope="session")
def config():
    return {
        "base_url": os.getenv("BASE_URL", "https://portal.basebs.net/ucrm/home"),
        "browser": os.getenv("BROWSER", "chrome").lower(),
        "headless": os.getenv("HEADLESS", "true").lower() == "true",
        "implicit_wait": int(os.getenv("IMPLICIT_WAIT", "0")),
        "explicit_wait": int(os.getenv("EXPLICIT_WAIT", "10")),
        "username": os.getenv("USERNAME", "crmxvtb2.0@basebs.com"),
        "password": os.getenv("PASSWORD", "12345678x@X"),
    }

@pytest.fixture
def driver(config):
    if config["browser"] == "chrome":
        drv = _build_chrome(config["headless"])
    else:
        raise RuntimeError("Hiện demo chỉ cấu hình Chrome.")

    if config["implicit_wait"] > 0:
        drv.implicitly_wait(config["implicit_wait"])
    yield drv
    drv.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook để capture screenshot khi test fail và tạo Allure report
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Chỉ capture khi test fail
    if rep.when == "call" and rep.failed:
        try:
            # Lấy driver từ fixture
            driver = item.funcargs.get("driver")
            if driver:
                test_name = item.name
                # Chụp screenshot cho thư mục screenshots
                screenshot_path = take_screenshot_on_failure(driver, test_name)
                if screenshot_path:
                    rep.sections.append(("Screenshot", f"Screenshot saved: {screenshot_path}"))
                
                # Chụp screenshot cho Allure
                allure_screenshot = take_screenshot_for_allure(driver, test_name)
                if allure_screenshot:
                    # Thêm screenshot vào Allure report
                    rep.sections.append(("Allure Screenshot", f"Allure screenshot: {allure_screenshot}"))
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
