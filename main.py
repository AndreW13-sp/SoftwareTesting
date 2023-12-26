import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Starting the automated test case...")

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    print("Navigating to the W3Schools login page...")
    # Open the W3Schools login page
    driver.get("https://profile.w3schools.com/")

    # Wait for the login page to load
    print("Waiting for the login page to load...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

    print("Entering login credentials...")
    # Enter login credentials
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("dropbox6393@gmail.com")

    password_input = driver.find_element(By.NAME, "current-password")
    password_input.send_keys("PassWord@123")

    print("Submitting the login form...")
    # Find and click the submit button using class name
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "Button_primary__d2Jt3"))
    )
    submit_button.click()

    print("Waiting for the redirect after login...")
    # Wait for the redirect to the dashboard after login
    redirect_url = "https://my-learning.w3schools.com/"
    WebDriverWait(driver, 10).until(EC.url_contains(redirect_url))

    # Check if redirected to the expected page after login
    if redirect_url in driver.current_url:
        print("Successfully logged in! Redirected to the dashboard.")
    else:
        print("Unexpected redirect or login failed. Current URL:", driver.current_url)

except TimeoutException as e:
    print("TimeoutException occurred:", e)
    print("Current URL:", driver.current_url)

except Exception as ex:
    print("An unexpected error occurred:", ex)

finally:
    # Quit the WebDriver session
    print("Quitting the WebDriver session...")
    driver.quit()
