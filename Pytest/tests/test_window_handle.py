from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class TestWindowHandle:

    @pytest.fixture(scope = 'class')
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_switch_between_tabs(self, driver):
        driver.get("https://www.google.com")
        driver.execute_script("window.open('https://www.bing.com');")
        time.sleep(2)
        driver.execute_script("window.open('https://www.yahoo.com');")
        time.sleep(2)
        print(f"Current window handle - {driver.current_window_handle}")
        handles = driver.window_handles
        print(f"Window handles - {handles}")
        driver.switch_to.window(handles[2])
        print(f"Current window handle - {driver.current_window_handle}")
        time.sleep(2)
        driver.switch_to.window(handles[1])
        print(f"Current window handle - {driver.current_window_handle}")
        time.sleep(2)
        print(f"Webdriver : {WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))}")
        time.sleep(2)
        

