from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()  # This automatically finds ChromeDriver if it's in PATH

# Step 2: Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# Step 3: Find username & password fields and enter details
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

# Step 4: Click the login button
driver.find_element(By.ID, "submit").click()

# Step 5: Wait to see result
time.sleep(3)

# Step 6: Print confirmation message
print("✅ Login Successful!")

# Step 7: Close the browser
driver.quit()
