# 🛒 Flipkart Data Scraper using Python & Selenium

This project is a **Flipkart Product Data Scraper** built using **Python, Selenium, and Pandas**. It automatically searches any product name entered by the user, scrapes details like **title, price, rating, and number of reviews** from multiple pages, and finally saves everything into an **Excel file**.

---

## ⭐ Features

* Automates Chrome browser using Selenium
* Closes Flipkart login popup automatically
* Searches any product typed by the user
* Scrapes:

  * Product Title
  * Price
  * Rating
  * Number of Reviews
* Extracts data from multiple pages (pagination)
* Saves final output to `flipkart_data.xlsx`
* Beginner-friendly and easy to customize

---

## 🧰 Technologies Used

* Python
* Selenium WebDriver
* Pandas
* ChromeDriver
* Flipkart Website

---

## 📂 How It Works

1. User enters a product name (e.g., "mobile", "laptop")
2. Selenium opens Flipkart in Chrome
3. Script removes the login popup
4. Scraper collects all product details across multiple pages
5. Data is stored in a pandas DataFrame
6. Final Excel file is generated automatically

---

## 🚀 How to Run the Project

### 1. Install Required Packages

```bash
pip install selenium pandas
```

### 2. Download ChromeDriver

Make sure your ChromeDriver version matches your Chrome browser.

Download from: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)

Place the ChromeDriver file in the same folder as your script or add it to PATH.

---

## 🧠 Code Overview

The script covers:

* Opening Flipkart
* Searching product
* Scraping titles, prices, ratings, reviews
* Navigating multiple pages
* Saving to Excel

---

## 📊 Output File

The project generates:

```
flipkart_data.xlsx
```

This file contains:

* Title
* Price
* Rating
* Reviews
* Page number

---

## 🎯 Use Cases

* Price comparison
* Data analysis
* E‑commerce research
* Freelancing projects
* Portfolio building

---

## 📧 Contact / Suggestions

If you have suggestions or want improvements, feel free to reach out!

---

### ⭐ If you like this project, don't forget to give a **star ⭐ on GitHub!**
