import os
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot(driver, test_name, folder="screenshots"):
    """
    Chụp screenshot và lưu vào thư mục screenshots
    """
    # Tạo thư mục screenshots nếu chưa có
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Tạo tên file với timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(folder, filename)
    
    try:
        # Chụp screenshot
        driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"Failed to take screenshot: {e}")
        return None

def take_screenshot_on_failure(driver, test_name):
    """
    Chụp screenshot khi test fail
    """
    return take_screenshot(driver, f"FAILED_{test_name}")

def take_screenshot_on_success(driver, test_name):
    """
    Chụp screenshot khi test pass
    """
    return take_screenshot(driver, f"PASSED_{test_name}")

def take_screenshot_for_allure(driver, test_name, allure_dir="allure-results"):
    """
    Chụp screenshot cho Allure report
    """
    # Tạo thư mục allure-results nếu chưa có
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)
    
    # Tạo tên file cho Allure
    filename = f"{test_name}.png"
    filepath = os.path.join(allure_dir, filename)
    
    try:
        # Chụp screenshot
        driver.save_screenshot(filepath)
        print(f"Allure screenshot saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"Failed to take Allure screenshot: {e}")
        return None
