from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging

#Launch Chrome browser and navigate to google.com
def test_launch_chrome_browser():
    driver = webdriver.Chrome()
    time.sleep(5)
    driver.quit()
    # driver.get("https://www.google.com")
    # time.sleep(5)
    # assert "Google" in driver.title
    # driver.quit()



#Launch firefox browser and navigate to google.com
def test_launch_firefox_browser():
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()

#Launch Edge browser and navigate to google.com
def test_launch_edge_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(5)
    assert "Google" in driver.title
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    ele = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    ele.send_keys("Selenium")
    atrr = ele.get_attribute("rows") 
    logging.info(f"Selenium is entered in the search box - {atrr}")
    print(f"Selenium is entered in the search box - {atrr}")
    ele.send_keys(Keys.ENTER)
    time.sleep(50)
    time.sleep(5)
    driver.back()
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    driver.quit()

