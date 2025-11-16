from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# --- User input ---
item_name = input("Enter the product name to search on Flipkart: ")

# list to store results
all_products = []

# --- Open Chrome ---
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")
time.sleep(2)

# --- Close login popup if present ---
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_button.click()
except:
    pass

# --- Search for the item ---
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(item_name)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

print(f"\n🛒 Products for '{item_name}':\n")

# --- SCRAPE MULTIPLE PAGES ---
for page in range(1, 4):  # scrape pages 1-3
    print(f"\n========== PAGE {page} ==========\n")
    time.sleep(3)

    titles = driver.find_elements(By.CLASS_NAME, "KzDlHZ")
    prices = driver.find_elements(By.CSS_SELECTOR, "div.Nx9bqj._4b5DiR")

    # ⭐ Added rating & reviews scraping
    ratings = driver.find_elements(By.CLASS_NAME, "XQDdHH")
    reviews = driver.find_elements(By.CLASS_NAME, "Wphh3N")

    for i in range(len(titles)):
        title = titles[i].text
        price = prices[i].text if i < len(prices) else "N/A"
        rating = ratings[i].text if i < len(ratings) else "N/A"
        review = reviews[i].text if i < len(reviews) else "N/A"

        print(f"{title} >>> {price} >>> ⭐ {rating} >>> {review}")

        # Save each product
        all_products.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Reviews": review,
            "Page": page
        })

    # --- Click "Next" ---
    try:
        next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button.click()
    except:
        print("No more pages.")
        break

    time.sleep(4)

driver.quit()

# ---- SAVE TO EXCEL ----
df = pd.DataFrame(all_products)
df.to_excel("flipkart_data.xlsx", index=False)

print("\n✔ Saved to flipkart_data.xlsx")
