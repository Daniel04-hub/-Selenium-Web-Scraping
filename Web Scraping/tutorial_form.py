from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the web-tables practice page
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")
time.sleep(2)  # let page load

# Locate the table element
table = driver.find_element(By.TAG_NAME, "table")

# Get all rows (including header)
rows = table.find_elements(By.TAG_NAME, "tr")

print("Total rows:", len(rows))

for i, row in enumerate(rows):
    # For each row, get either th (header) or td (data) cells
    if i == 0:
        # header row
        cells = row.find_elements(By.TAG_NAME, "th")
        print("=== Header ===")
    else:
        cells = row.find_elements(By.TAG_NAME, "td")
        print(f"--- Row {i} ---")

    for j, cell in enumerate(cells):
        print(f"Cell[{i},{j}] = {cell.text}")

# Done
time.sleep(2)
driver.quit()
