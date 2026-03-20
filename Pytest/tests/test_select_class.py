from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TestSelectClass:

    @pytest.fixture(scope="class",autouse=True)
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get("https://blazedemo.com")
        yield driver
        driver.quit()

    def test_select_class(self, driver):
        driver.get("https://blazedemo.com")
        wait = WebDriverWait(driver,10)
        ele = wait.until(EC.visibility_of_element_located((By.NAME,'fromPort')))
        select = Select(ele)
        

        default_option = select.first_selected_option.text
        print(f"Default selected option in departure city dropdown - {default_option}")
        time.sleep(5)
        options = select.options
        print("All options in departure city dropdown - ")
        for option in options:
            print(option.text)
        time.sleep(5)
        assert select.is_multiple == None, "Departure city dropdown allows multiple selection, but it should not"
        select.select_by_value("San Diego")
        time.sleep(5)
        departure_city = wait.until(EC.visibility_of_element_located((By.NAME,'toPort')))
        select = Select(departure_city)
        select.select_by_visible_text("London")
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="Find Flights"]'))).click()
        time.sleep(5)


