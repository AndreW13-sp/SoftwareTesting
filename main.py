from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook


def write_to_excel(test_case, description, expected_output, result):
    wb = Workbook()
    sheet = wb.active
    sheet.append(["Test Case", "Description", "Expected Output", "Pass/Fail"])
    sheet.append([test_case, description, expected_output, result])
    wb.save("test_results.xlsx")


print("Sample test case started")

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open the W3Schools login page
    driver.get("https://profile.w3schools.com/")

    # Wait for the login page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

    # Enter login credentials
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("dropbox6393@gmail.com")

    password_input = driver.find_element(By.NAME, "current-password")
    password_input.send_keys("PassWord@123")

    # Find and click the submit button using class name
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "Button_primary__d2Jt3"))
    )
    submit_button.click()

    # Wait for the redirect to the dashboard after login
    redirect_url = "https://my-learning.w3schools.com/"
    WebDriverWait(driver, 10).until(EC.url_contains(redirect_url))

    # Test Case 1: Redirected to the dashboard after successful login
    if redirect_url in driver.current_url:
        print("Redirected to the dashboard after successful login")
        write_to_excel("TC1", "Login to W3Schools profile", "Redirected to dashboard", "Pass")
    else:
        print("Unexpected redirect or login failed. Current URL:", driver.current_url)
        write_to_excel("TC1", "Login to W3Schools profile", "Redirected to dashboard", "Fail")

except TimeoutException as e:
    print("TimeoutException occurred:", e)
    print("Current URL:", driver.current_url)

except Exception as ex:
    print("An unexpected error occurred:", ex)

finally:
    # Quit the WebDriver session
    driver.quit()
