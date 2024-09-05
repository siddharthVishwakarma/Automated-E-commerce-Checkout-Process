from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver, username, password):
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()

def fill_payment_details(driver, card_number, expiry_date, cvv):
    driver.find_element(By.ID, 'card-number').send_keys(card_number)
    driver.find_element(By.ID, 'expiry-date').send_keys(expiry_date)
    driver.find_element(By.ID, 'cvv').send_keys(cvv)
