import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print("sample test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://profile.w3schools.com/")
time.sleep(1)

driver.find_element("name", "email").send_keys("dropbox6393@gmail.com")
time.sleep(2)
driver.find_element("name", "current-password").send_keys("PassWord@123")
time.sleep(2)

submit_button = driver.find_element_by_css_selector('input[type="submit"]')

try:
    redirect_url = "https://my-learning.w3schools.com/"
    WebDriverWait(driver, 10).until(EC.url_contains(redirect_url))
    print("Redirected to the next page:", driver.current_url)
except TimeoutException as e:
    print("TimeoutException:", e)
    print("Current URL:", driver.current_url)
    time.sleep(20)
finally:
    driver.quit()
