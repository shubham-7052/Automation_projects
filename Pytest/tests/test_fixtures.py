from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestFictures:
    @pytest.fixture(scope="function")
    def driver(self):
        print("Launching browser")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com")
        yield driver
        driver.quit()

    # def test_google_title(self, driver):
    #     assert "Google" in driver.title
        
    #     wait = WebDriverWait(driver, 10)
    #     ele = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Search by voice']")))
    #     action = ActionChains(driver)
    #     action.move_to_element(ele).perform()
    #     time.sleep(1)
    #     print("TEST 1 PASSES")

    def test_google_search(self, driver):
        main_window = driver.current_window_handle
        driver.switch_to.new_window('window')
        driver.get("https://www.google.com")
        time.sleep(5)
        driver.switch_to.new_window('tab')
        driver.get("https://www.google.com")
        time.sleep(5)
        driver.execute_script("window.open('https://www.facebook.com');")
        time.sleep(5)
        handles = driver.window_handles
        print(f"Window handles - {handles}")
        driver.switch_to.window(main_window)
        time.sleep(5)
        driver.switch_to.window(handles[2]) 
        time.sleep(5)
        driver.close()
        time.sleep(10)
        

        # for handle in handles:
        #     if handle != main_window:
        #         driver.switch_to.window(handle)
        #         print(f"Current window handle - {driver.current_window_handle}")
        #         time.sleep(5)
        #         if driver.title == "Facebook - log in or sign up":
        #             print("Facebook is opened in one of the tabs")
        #             break
        # time.sleep(15)
        print("TEST 2 PASSES")

"""
4️⃣ Handling Complex UI Elements
✅ Alerts:
driver.switch_to.alert.accept()
✅ Frames:
driver.switch_to.frame("frame_id")
driver.switch_to.default_content()
✅ Multiple Tabs:
driver.switch_to.window(driver.window_handles[1])
"""
