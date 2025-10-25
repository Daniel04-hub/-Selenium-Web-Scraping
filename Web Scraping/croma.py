from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# --- Chrome Options ---
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
# options.add_argument("--headless=new")  # Comment for debugging

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

try:
    # --- Open Croma ---
    driver.get("https://www.croma.com/")

    # --- Search for 'headphones' ---
    search_box = wait.until(EC.presence_of_element_located((By.ID, "searchV2")))
    search_box.clear()
    search_box.send_keys("headphones")
    search_box.send_keys(Keys.RETURN)

    # --- Wait for products to load ---
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cp-product")))
    time.sleep(2)

    products = driver.find_elements(By.CSS_SELECTOR, "div.cp-product")[:10]
    product_list = []

    for i, product in enumerate(products, start=1):
        driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(0.5)

        def safe_get(selector, by=By.CSS_SELECTOR):
            try:
                elem = product.find_element(by, selector)
                return elem.text.strip() if elem.text.strip() else "N/A"
            except:
                return "N/A"

        # --- Extract product details ---
        name = safe_get("h3.product-title a")
        offer_price = safe_get("span[data-testid='new-price']")
        discount = safe_get("span.discount")
        rating = safe_get("div.cp-rating span.rating-text")
        delivery_info = safe_get("span.delivery-text-msg")
        you_save = safe_get("span.dicount-value")  # typo in class is on site: "dicount-value"

        product_list.append({
            "S.No": i,
            "Product Name": name,
            "Offer Price": offer_price.replace("₹", "").strip() if offer_price != "N/A" else offer_price,
            "Discount": discount,
            "Rating": rating,
            "Delivery Info": delivery_info,
            "You Save": you_save.replace("Save", "").replace("₹", "").strip() if you_save != "N/A" else you_save
        })

    # --- Save to CSV ---
    df = pd.DataFrame(product_list)
    df.to_csv("croma_headphones_clean_no_mrp.csv", index=False, encoding="utf-8-sig")
    print("✅ Data successfully scraped and saved to croma_headphones_clean_no_mrp.csv")

except Exception as e:
    print("❌ Error:", e)

finally:
    driver.quit()
