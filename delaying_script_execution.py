from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com")

# Simulate delay for external scripts/resources to load
time.sleep(5)

try:
    # This element might not be available immediately on slower networks
    popup = driver.find_element(By.ID, "subscribe-popup")
    popup_close = popup.find_element(By.CSS_SELECTOR, "[aria-label='Close']")
    popup_close.click()
    print("Popup closed.")
except Exception:
    print("Popup did not appear.")

# Continue other actions

driver.quit()
