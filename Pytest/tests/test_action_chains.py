from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import logging
import pytest

class TestActionchains:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_hover_over_element(self, driver):
        driver.get("https://www.blazemeter.com/")
        action = ActionChains(driver)
        wait = WebDriverWait(driver,10)
        ele = wait.until(EC.visibility_of_element_located((By.XPATH,'//button[contains(text(), "Support & Services")]')))
        action.move_to_element(ele).perform()
        time.sleep(5)
        action.context_click(ele).perform()
        time.sleep(5)
        for i in range(5):
            action.double_click(ele).perform()
        time.sleep(5)

    def test_keyboard_actions(self, driver):
        driver.get("https://www.google.com")
        action = ActionChains(driver)
        wait = WebDriverWait(driver,10)
        ele = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
        ele.send_keys("Selenium")
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        copied_text = pyperclip.paste()
        logging.info(f"Copied text from search box - {copied_text}")
        print(f"Copied text from search box - {copied_text}")
        time.sleep(5)