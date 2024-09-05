import configparser
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import helpers

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Initialize WebDriver
driver = webdriver.Chrome(executable_path=config['WEBDRIVER']['path'])

try:
    # Navigate to login page
    driver.get(config['LOGIN']['url'])

    # Login to the account
    helpers.login(driver, config['LOGIN']['username'], config['LOGIN']['password'])

    # Read products from CSV
    products = pd.read_csv('products.csv')

    for _, row in products.iterrows():
        # Search for the product
        search_box = driver.find_element(By.ID, 'search-box')
        search_box.send_keys(row['product_name'])
        search_box.send_keys(Keys.RETURN)
        
        # Add the product to the cart
        driver.find_element(By.XPATH, '//button[contains(text(),"Add to Cart")]').click()
        # Adjust quantity if necessary
        quantity_box = driver.find_element(By.ID, 'quantity')
        quantity_box.clear()
        quantity_box.send_keys(str(row['quantity']))

    # Proceed to checkout
    driver.find_element(By.ID, 'cart').click()
    driver.find_element(By.ID, 'checkout').click()

    # Apply discount code
    discount_box = driver.find_element(By.ID, 'discount-code')
    discount_box.send_keys(config['DISCOUNT']['code'])
    discount_box.send_keys(Keys.RETURN)

    # Fill in payment details
    helpers.fill_payment_details(driver, config['PAYMENT']['card_number'],
                                 config['PAYMENT']['expiry_date'], config['PAYMENT']['cvv'])

    # Complete the purchase
    driver.find_element(By.ID, 'complete-purchase').click()

    print("Checkout process completed successfully!")

finally:
    driver.quit()
