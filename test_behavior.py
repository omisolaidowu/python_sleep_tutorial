from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the browser (Chrome)
driver = webdriver.Chrome()

# Go to the target page
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

# Observe the page load by waiting for 10 seconds
time.sleep(10)

first_featured = driver.find_element(By.XPATH, "//h3[text()='Featured']")
first_featured.click()

# Wait for the page transition
time.sleep(5)

next_button = driver.find_element(By.CLASS_NAME, "swiper-button-next")
next_button.click()

# Wait another 10 seconds before closing to see the effect
time.sleep(10)

# Close the browser
driver.quit()
