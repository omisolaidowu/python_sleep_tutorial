from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the browser (Chrome)
driver = webdriver.Chrome()

# Go to the target page
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

# Wait 10 seconds to allow page resources to load
time.sleep(10)


# Navigate to a product page
page_button = driver.find_elements(By.ID, "mz-product-listing-image-39217984-0-1")
assert len(page_button[0]) > 0, "Button not found on the page"
page_button[0].click()

# Wait for the page transition
time.sleep(6)

# Capture the page title
print(driver.title)

# Close the browser
driver.quit()
