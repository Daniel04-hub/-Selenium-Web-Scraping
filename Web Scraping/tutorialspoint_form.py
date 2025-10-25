from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Helper function to type like a human
def type_like_human(element, text, delay=0.2):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# Start Chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
time.sleep(4)

# Step 3: Name
driver.find_element(By.ID, "name").send_keys("Naveen Daniel")
time.sleep(1)

# Step 4: Email
driver.find_element(By.ID, "email").send_keys("naveen@example.com")
time.sleep(1)

# Step 5: Gender
driver.find_element(By.XPATH, "//label[normalize-space()='Male']").click()
time.sleep(1)

# Step 6: Mobile
driver.find_element(By.ID, "mobile").send_keys("9876543210")
time.sleep(1)

# Step 7: Date of Birth (click first)
dob_field = driver.find_element(By.ID, "dob")
dob_field.click()
time.sleep(0.5)
dob_field.send_keys("01/01/2000")
time.sleep(1)

# Step 8: Subject (type slowly and select)
subject_field = driver.find_element(By.ID, "subject")
type_like_human(subject_field, "Maths", delay=0.3)
time.sleep(1)
subject_field.send_keys("\n")  # Press Enter to select autocomplete
time.sleep(1)

# Step 9: Hobbies
driver.find_element(By.XPATH, "//label[normalize-space()='Sports']").click()
time.sleep(1)

# Step 10: Address
address_field = driver.find_element(By.ID, "address")
address_field.click()
type_like_human(address_field, "123, Selenium Street, Chennai", delay=0.2)
time.sleep(1)

# Step 11: State
driver.find_element(By.ID, "state").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[text()='NCR']").click()
time.sleep(1)

# Step 12: City
driver.find_element(By.ID, "city").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[text()='Agra']").click()
time.sleep(1)

print("✅ Form filled successfully!")
time.sleep(5)
driver.quit()
