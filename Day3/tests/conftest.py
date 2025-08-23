import os, pytest, requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.core.config import settings
from src.api.todos_api import TodosAPI

@pytest.fixture(scope="session")
def api_base_url():
    return settings.api_base_url

@pytest.fixture(scope="session")
def ui_base_url():
    return settings.ui_base_url

@pytest.fixture(scope="session")
def http_session():
    # tùy biến headers, auth, proxies... nếu cần
    s = requests.Session()
    yield s
    s.close()

@pytest.fixture(scope="session")
def todos_client(api_base_url, http_session):
    return TodosAPI(base_url=api_base_url, session=http_session, timeout=settings.timeout)

# --- UI (có thể tạm skip hôm nay nếu chỉ luyện API)
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    if settings.headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(settings.timeout)
    yield driver
    driver.quit()
